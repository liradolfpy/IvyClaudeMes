# Query Key Selection Strategy

Model version 2.9 | 12 October 2026 | 369 collections (200 entity, 85 child, 76 relationship, 8 value-list), 8,245 keys
Status: strategy proposal for owner review. It changes no existing file. If adopted, the owner records a decision that supersedes D020.

## 1. Objective

Decide, for every collection, which keys are **query keys**: the keys the application filters, sorts, joins or scans on, and which therefore get an index. The selection must:

- support every MES function that needs a fast or guaranteed answer (shop-floor screens, interlocks, scans, traceability, recall, integration, audit);
- avoid indexes that nobody uses, because each index costs write time, RAM and storage, and slows the high-volume collections most;
- be repeatable, so the same rules give the same result when a collection or key is added.

The strategy also gives a short rule for **return keys** (projection), section 9.

## 2. Starting point and why it needs tuning

D020 (11 Oct 2026) set a uniform default: unique business key, site plus status, up to five reference keys, site plus main date, parent plus line number, both directions for relationship collections. It produced 1,488 indexes over 369 collections and was recorded as "to be tuned against real query patterns". Reading the generated index scripts in `03_design/*/indexes` shows the effect of a mechanical rule:

| Observation | Example | Effect |
|---|---|---|
| Low-selectivity references are indexed | `itemId` on `u_mes_plan_operationExecution` and `u_mes_qual_inspectionResult`; `parentItemId`, `childItemId` on `u_mes_trac_genealogyLink` | In a plant making a few caliper variants, one itemId matches a large share of the collection. The index is rarely chosen and only adds write cost. |
| References needed by a function are missing because of the five-reference cap | `childWipUnitId`, `childSerialNumberId` on `u_mes_trac_genealogyLink`; `operationExecutionId`, `goodsReceiptId` on `u_mes_qual_inspectionResult` | Backward trace and incoming-inspection screens fall back to a collection scan on a multi-million-document collection. |
| Telemetry carries transaction-style indexes | `u_mes_perf_processReading` has 8 indexes, including a unique `siteId + recordNo` | Highest insert rate in the model gets the most write amplification; a unique index is not allowed on a time-series collection. |
| Small masters and value lists carry a status index | `u_mes_mast_country`, `u_mes_mast_currency` | A few hundred documents are read once and cached; the index is never needed. |
| Both directions on every relationship | `u_mes_mast_workCenterEquipment` | The reverse direction is only useful when a screen navigates that way. |
| Status alone or site plus status as a separate index | `ix_siteId_status` on nearly every collection | Useful only for open work lists; better served by a compound or partial index that also carries the sort key. |

The strategy below replaces "index what the schema contains" with "index what a named function asks".

## 3. Inputs used

| Input | Location | Used for |
|---|---|---|
| Collection keys | `02_architecture/collection_keys.md` | Candidate keys per collection |
| Collection type matrix | `02_architecture/collection_type_matrix.md` | Master, Transaction, Reports, Telemetry, Audit Trail |
| Collection inventory (kind) | `02_architecture/collection_inventory.md` | entity, child, relationship, value-list |
| Field lists | `02_architecture/field_lists` | BSON type and reference target of each key |
| Status values | `04_reference_data/code_lists/status_values.md` | Open versus closed statuses for partial indexes |
| Volume basis | `00_governance/assumptions_log.md` A002 (2,400 calipers per day, 300 days) | Volume tier per collection |
| Time-series decisions | A011, D038, `data_modeling_standard.md` | Telemetry collections |
| Process flow | Project instructions (casting to dispatch) | Which functions run at which station and how often |

## 4. Key roles

Every key in `collection_keys.md` falls into one of these roles. The role tells whether the key can be a query key at all and in which position of a compound index.

| Role | Keys (pattern) | Query key? | Position in a compound index |
|---|---|---|---|
| R1 Identity | `_id`, `recordNo` | Always | `_id` is indexed by MongoDB; `recordNo` with `siteId` as the unique business key |
| R2 Scope | `siteId` | Prefix only | First, as equality, when the remaining keys are low-cardinality (status, date). Not added in front of globally unique references |
| R3 Lifecycle | `status`, `onHold`, `qualityStatus` | Prefix or partial filter only, never alone | Equality after scope or context; or used in `partialFilterExpression` to keep only open documents |
| R4 Parent | `<parent>Id` plus `sequenceNo`, `lineNo`, `stepNo`, `itemNo`, `levelNo` | Always on child and relationship collections | Parent first, sequence second, unique |
| R5 Context | `workCenterId`, `equipmentId`, `lineId`, `areaId`, `storageLocationId` | When a station, line or warehouse screen reads by it | Equality first, then status, then time |
| R6 Trace | `wipUnitId`, `lotId`, `serialNumberId`, `containerId`, `shipmentId`, `productionOrderId`, `parent*Id`, `child*Id`, `componentLotId` | Yes on T1 and larger collections; required for genealogy and recall | Equality first, then step or time |
| R7 Definition | `itemId`, `routingId`, `billOfMaterialId`, `operationId`, `recipeId`, `characteristicId`, `defectCodeId`, `reasonCodeId` | Only inside a compound with time or a trace key, never as a single-key index on a transaction collection | Equality, followed by a sort key (for example `characteristicId` then `measuredAt` for SPC) |
| R8 Event time | `startedAt`, `measuredAt`, `raisedAt`, `linkedAt`, `timestamp`, `productionDate` with `shiftId` | As sort or range key | Last in the compound (ESR rule, section 6.4) |
| R9 Polymorphic | `relatedCollectionName` with `relatedEntityId` | Yes, as a pair | Collection name, then entity id, then time |
| R10 External and scanned | `dataMatrixPayload`, `barcode`, `badgeNo`, `serialNo`, `supplierLotNo`, `erpOrderNo`, `idempotencyKey`, `customerRefNo`, `asnNo`, `invoiceNo` | Yes when scanned on the shop floor or received from another system | Single key, unique where the value is unique, partial when the key may be null |
| R11 Display and measures | every `...Name`, measured values, text, remarks, flags, counts, money | Never | Projection only. Filter on the `Id`, display the `Name` |
| R12 Audit stamps | `createdAt`, `createdBy`, `updatedAt`, `updatedBy`, `schemaVersion` | Not on business collections | Change streams feed downstream systems; Audit Trail type collections use their own time key |

## 5. Volume tiers

Tier is assigned per collection from the volume basis A002. Assumption: about 12 routed steps per caliper, about 8 traced components per caliper, inspection by control plan sampling with 100 % checks at torque and leak test.

| Tier | Documents per year | Typical collections |
|---|---|---|
| T0 Small | below 10,000 | All value lists; most masters and their child and relationship collections (equipment, work centres, items, routings, characteristics, defect codes, reason codes, users) |
| T1 Medium | 10,000 to 1,000,000 | `u_mes_plan_wipUnit` and `u_mes_trac_serialNumber` (about 720,000), lots, production orders, containers, shipments, labels, downtime events, nonconformances, labour bookings, check-sheet results, alarms |
| T2 Large | 1,000,000 to 50,000,000 | `u_mes_plan_operationExecution` (about 8.6 million), `u_mes_qual_inspectionResult`, `u_mes_trac_genealogyLink` (about 5.8 million), `u_mes_perf_torqueResult`, `u_mes_perf_leakTestResult`, `u_mes_matl_materialConsumption`, `u_mes_plan_stepCompletion`, `u_mes_syst_auditTrail`, `u_mes_syst_businessEvent`, `u_mes_perf_equipmentState` |
| T3 Very large | above 50,000,000 | Time-series: `u_mes_perf_processReading`, `u_mes_qual_measurementCurvePoint`, `u_mes_perf_energyReading` (depends on meter count and interval) |

## 6. Selection method

The method runs per collection in six steps. Steps 1 to 3 decide **which keys** qualify; steps 4 to 6 decide **how** they are combined and capped.

### 6.1 Step 1: List the access patterns

For each collection, list the functions that read it, using this fixed catalogue. A key is a candidate only if it appears in at least one pattern.

| Pattern | Description | Typical keys | Example in the caliper plant |
|---|---|---|---|
| QP01 Business-key lookup | Open a record by its number | `siteId`, `recordNo` | Open PO-1000433 |
| QP02 Scan lookup | Barcode, DataMatrix or badge scanned at a station | R10 key | Scan the laser-marked DataMatrix at final inspection; scan a lot label at piston assembly |
| QP03 Open work list | Records waiting for action, sorted | `siteId` or context, `status`, time | Open nonconformances; queued ERP messages; running operations at a station |
| QP04 Parent to children | Lines of a header | parent id, sequence | Steps of routing RT-CAL-LH; lines of a goods receipt |
| QP05 Station or line context | What happened at one place recently | `workCenterId` or `equipmentId`, time | Last 50 cycles at the leak tester; downtime at the CNC cell this shift |
| QP06 Unit or lot history | Everything done to one caliper or one lot | `wipUnitId` or `lotId`, step or time | Operation history of one caliper body; furnace readings for one T6 load |
| QP07 Trace forward and backward | Genealogy and recall | parent and child trace keys | Which shipped calipers contain seal lot SL-2609-118 |
| QP08 Interlock check | Validation at a transaction point, must answer in milliseconds | trace key plus step | Previous step complete; gauge calibration valid; tool life remaining |
| QP09 Time window extract | Jobs that build Reports collections or feed ERP | `siteId`, time | Hourly production count; OEE per shift |
| QP10 Trend by definition | Values of one characteristic or tag over time | definition key, time | SPC chart for bore diameter; leak rate trend |
| QP11 Polymorphic lookup | Records attached to any other record | `relatedCollectionName`, `relatedEntityId` | Audit trail of one control plan; signatures on one batch release |
| QP12 Integration | Idempotency and retry | `idempotencyKey`, `status`, `nextRetryAt` | Resend failed goods-issue postings |

Source of the patterns, in order of preference: the screen and API list of each module; the interlock rules (`u_mes_syst_interlockRule.transactionPoint`); the report build jobs; the saved views (`u_mes_syst_savedView.filterJson`) once the system is live.

### 6.2 Step 2: Apply the gates to each candidate key

A candidate key becomes a query key only if it passes all gates that apply.

| Gate | Rule |
|---|---|
| G1 Mandatory | Every collection keeps its business key `{siteId, recordNo}` unique. Child collections keep `{parentId, sequence}` unique. Relationship collections keep `{ownerId, targetId}` unique in the owner direction. Exception: time-series collections, where uniqueness is enforced by the application (unique indexes are not supported). |
| G2 Pattern | The key must appear in a QP pattern of section 6.1. No pattern, no index. |
| G3 Tier | T0 collections get no secondary index beyond G1, unless a QP02 scan or QP08 interlock reads them by a non-business key (for example `u_mes_mast_user.badgeNo`, `u_mes_matl_storageLocation.barcode`). The application caches T0 data. |
| G4 Selectivity | The key, alone or with its equality prefix, must narrow the result to a small share of the collection (guideline: under 1 % or a few thousand documents). Low-cardinality keys (`status`, `siteId`, `shiftId`, flags, R7 definition keys in a few-product plant) never form a single-key index. |
| G5 Frequency and latency | Hot (station screen, scan, interlock; many times per minute; answer under 100 ms): index required. Warm (supervisor and quality screens; several times per shift): index on T1 and above. Cold (monthly reports, ad-hoc analysis): no index; served by a Reports collection, an analytics node or a secondary. |
| G6 Regulatory | Trace, recall, complaint containment, audit trail and electronic signature retrieval are indexed even when cold, because the answer is owed to the customer or auditor within hours (IATF 16949 traceability and 8D containment, 21 CFR Part 11 / EU GMP Annex 11 for the GMP option). |

Tie-breaker for borderline warm cases: score Frequency, Latency need, Tier and Selectivity from 0 to 3 each; index when the total is 8 or more.

### 6.3 Step 3: Mark nullable keys

Many references are null for part of the collection (`wipUnitId` is null for lot-level operations such as casting, heat treatment and anodising; `nonconformanceId` is null for good results). For such keys use a partial index with `partialFilterExpression: { <key>: { $type: "string" } }`. The index then holds only the documents that can be found by that key.

### 6.4 Step 4: Shape compound indexes (ESR)

Order keys as **Equality, Sort, Range**:

1. Equality keys first (scope, context, trace or definition key, status);
2. then the sort key (usually the event time, descending for "latest first");
3. then range keys (date windows, numeric ranges).

Example: station work list `{ workCenterId: 1, status: 1, startedAt: -1 }` answers "running operations at WC-LEAK-01, newest first" without an in-memory sort.

### 6.5 Step 5: Consolidate

- Prefix rule: an index `{a, b, c}` also serves queries on `{a}` and `{a, b}`. Drop any index that is a prefix of another.
- One index per pattern family: if QP03 and QP05 share the same equality key, merge them into one compound.
- Open-only work lists: when closed documents are the large majority, use a partial index on open statuses from `status_values.md` (for example `u_mes_syst_erpMessage` statuses Queued and Failed).
- Covered queries for interlocks: where an interlock needs only two or three keys, include them all in the index so the query never reads the document.

### 6.6 Step 6: Apply the budget

Caps per collection, by type and kind. A collection may exceed its cap only with a written justification in the query pattern register (section 8).

| Type / kind | Tier | Index budget including G1 |
|---|---|---|
| Value list | T0 | 1 |
| Master entity | T0 | 1 to 2 (business key, plus a scan key if any) |
| Master child or relationship | T0 | 1 (parent plus sequence, or owner plus target) |
| Transaction entity | T1 | 3 to 5 |
| Transaction entity | T2 | 4 to 7 |
| Transaction child or relationship | T1 / T2 | 1 to 2 (parent plus sequence; reverse direction only if a QP pattern navigates it) |
| Reports | T1 / T2 | 2 to 3 (unique grain key, for example line plus shift plus productionDate; plus time) |
| Telemetry (time-series) | T3 | 1 to 2 (metaField plus timeField, plus one trace key if required) |
| Audit Trail | T2 | 2 to 3 (polymorphic plus time; time; signature lookup) |

Hard ceiling for any collection: 8 indexes.

## 7. Worked examples (baseline D020 against this strategy)

### 7.1 u_mes_plan_operationExecution (Transaction, T2)

| Index | D020 | Strategy | Reason |
|---|---|---|---|
| `{siteId, recordNo}` unique | Yes | Keep | G1 |
| `{siteId, status}` | Yes | Drop | Status alone is low-cardinality; open operations are found per station by the index below |
| `{productionOrderId}` | Yes | Replace by `{productionOrderId, stepNo}` | QP06 order progress by step |
| `{wipUnitId}` | Yes | Drop | Prefix of the next index |
| `{wipUnitId, stepNo, attemptNo}` | Yes | Keep, make partial (wipUnitId is a string) | QP06 unit history, QP08 "previous step complete" interlock |
| `{lotId}` | Yes | Replace by `{lotId, stepNo}` partial | QP06 for lot-level steps (casting, T6, anodising) |
| `{itemId}` | Yes | Drop | G4: few caliper items, poor selectivity |
| `{routingId}` | Yes | Drop | G2: no function reads executions by routing |
| `{siteId, startedAt}` | Yes | Keep | QP09 build of productionCount and workCenterPerformance |
| `{workCenterId, startedAt}` | Yes | Replace by `{workCenterId, status, startedAt}` | QP03 and QP05 merged |
| Total | 10 | 6 | |

### 7.2 u_mes_qual_inspectionResult (Transaction, T2)

| Index | D020 | Strategy | Reason |
|---|---|---|---|
| `{siteId, recordNo}` unique | Yes | Keep | G1 |
| `{siteId, status}` | Yes | Drop | Statuses Recorded and Voided; no work list |
| `{inspectionPlanId}` | Yes | Drop | G2: plans are read forward, not results by plan |
| `{characteristicId}` | Yes | Replace by `{characteristicId, measuredAt}` | QP10 SPC and trend |
| `{itemId}` | Yes | Drop | G4 |
| `{wipUnitId}` | Yes | Replace by `{wipUnitId, characteristicId}` partial | QP06 caliper inspection history, final release check |
| `{lotId}` | Yes | Keep, make partial | QP06 lot inspection |
| `{siteId, measuredAt}` | Yes | Keep | QP09 |
| `{operationExecutionId}` | No | Add, partial | QP05 results shown on the operation screen |
| `{goodsReceiptId}` | No | Add, partial | QP04 incoming inspection of a receipt |
| `{nonconformanceId}` | No | Not added | Served by the relationship collection `u_mes_qual_nonconformanceInspectionResult` |
| Total | 8 | 7 | Fewer low-value indexes, two functional gaps closed |

### 7.3 u_mes_trac_genealogyLink (Transaction, T2, regulatory)

| Index | D020 | Strategy | Reason |
|---|---|---|---|
| `{siteId, recordNo}` unique | Yes | Keep | G1 |
| `{siteId, status}` | Yes | Drop | Statuses Active and Removed only |
| `{parentWipUnitId}` | Yes | Keep | QP07 forward: components of one caliper |
| `{parentSerialNumberId}` | Yes | Keep, partial | QP07 from a customer complaint serial |
| `{parentItemId}`, `{childItemId}` | Yes | Drop | G4 |
| `{childLotId}` | Yes | Keep, partial | QP07 backward: seal, piston or pad lot to calipers (recall) |
| `{childSerialNumberId}` | No | Add, partial | QP07 backward for serialised sub-assemblies |
| `{childWipUnitId}` | No | Add, partial | QP07 backward for in-house sub-assemblies |
| `{siteId, linkedAt}` | Yes | Keep | QP09 genealogy completeness check per shift |
| Total | 8 | 7 | Both trace directions complete |

### 7.4 u_mes_perf_processReading (Telemetry, T3, time-series per A011)

| Index | D020 | Strategy | Reason |
|---|---|---|---|
| Collection options | Not set | timeField `timestamp`, metaField `processTagId`, granularity seconds | Time-series storage |
| `{siteId, recordNo}` unique | Yes | Drop | Unique indexes are not supported on time-series; recordNo stays a business key enforced by the writer |
| `{processTagId, timestamp}` | Yes | Keep (created automatically on meta plus time in recent MongoDB versions) | QP10 tag trend |
| `{lotId, timestamp}` | No (only `{lotId}`) | Keep as compound, partial | QP06 furnace curve for one T6 load (special process evidence, CQI-9) |
| `{equipmentId}`, `{productionOrderId}`, `{areaId}`, `{siteId, timestamp}` | Yes | Drop | Tag implies equipment and area; order and window queries go through lot or tag |
| Total | 8 | 2 | Highest insert rate, lowest write amplification |

### 7.5 u_mes_syst_erpMessage (Transaction, T2, integration)

| Index | D020 | Strategy | Reason |
|---|---|---|---|
| `{siteId, recordNo}` unique | Yes | Keep | G1 |
| `{idempotencyKey}` | Yes, not unique | Make unique, partial | QP12: a repeated message must be rejected, not stored twice |
| `{siteId, status}` | Yes | Replace by `{status, nextRetryAt}` partial on Queued and Failed | QP03 and QP12 retry job; the index holds only open messages |
| `{relatedCollectionName, relatedEntityId}` | Yes | Extend to `{relatedCollectionName, relatedEntityId, createdInSourceAt}` | QP11 message history of one order, receipt or shipment |
| `{productionOrderId}`, `{goodsReceiptId}`, `{shipmentId}` | Yes | Drop | Covered by the polymorphic index, on the assumption that relatedEntity always names the primary object |
| `{integrationConnectorId}` | Yes | Drop | G4: a handful of connectors |
| `{siteId, createdInSourceAt}` | Yes | Keep | Monitor screen and QP09 |
| Total | 9 | 5 | |

### 7.6 Small masters, child and relationship collections

| Collection | D020 | Strategy | Reason |
|---|---|---|---|
| `u_mes_mast_country` (value-list style master, T0) | 2 | 1 | Status index never used; data cached |
| `u_mes_mast_equipment` (T0) | 7 (business key, status, five references) | 1 | Around a hundred documents; cached |
| `u_mes_mast_user` (T0) | 9 (business key, status, five references, userName, badgeNo) | 3 | Business key; `userName` unique (login); `badgeNo` unique (QP02 badge scan at the station). Department, designation, shift, work centre and manager references dropped: cached |
| `u_mes_mast_workCenterEquipment` (relationship, T0) | 2 (both directions) | 1 | Reverse direction not navigated by any screen |
| `u_mes_prod_routingStep` (child, T0) | 3 (routing plus step, operationId, workCenterId) | 1 | `{routingId, stepNo}` unique; routings are read forward and cached |

## 8. Recording the result

The selection is kept in one register so it can be reviewed, generated and checked.

1. **Query pattern register** (proposed new file; not created by this task). One row per pattern per collection:

   | Collection | Pattern | Function or screen | Equality keys | Sort key | Range key | Frequency | Latency | Index name | Decision and reason |
   |---|---|---|---|---|---|---|---|---|---|

2. **Generator**: `gen_specs.py` today builds indexes from the D020 rule. If adopted, the index list would be read from a pattern dictionary in `05_generator` (one entry per collection, as in the register), with the D020 rule kept only as the fallback for collections not yet reviewed. Index scripts and specifications in `03_design/*/indexes` are then regenerated, never edited by hand (Folder_Guide rule 4).

3. **Decision log**: a new decision supersedes D020 and states the gates G1 to G6 and the budget of section 6.6.

## 9. Return keys (projection)

The model is flat and every reference carries its display name, so screens never need `$lookup` for display.

| View | Keys returned |
|---|---|
| List or grid | `_id`, `recordNo`, `status`, the main event time, the `...Name` keys shown as columns, and the `...Id` keys only where the column is a link |
| Detail | Full document |
| Interlock and scan checks | Only the keys the rule tests, so the query is covered by its index |
| Integration extract | Keys in the interface mapping only |

Rule: filter on `Id` keys, display `Name` keys; never filter on a `Name` key. Free-text search on names (masters) is handled by the cached T0 data or, if needed later, a dedicated text or search index, not by regular indexes on every name key.

## 10. Rollout order

| Phase | Scope | Approximate collections |
|---|---|---|
| A | T2 and T3 collections and every collection read by an interlock or scan (hot path) | about 25 |
| B | T1 transaction collections, Reports and Audit Trail | about 135 |
| C | T0 masters, child, relationship and value-list collections: trim to the G1 index plus scan keys | about 210 |

## 11. Verification

| Check | When | Pass condition |
|---|---|---|
| `explain("executionStats")` for each register pattern on seed data scaled to one month of volume | Before handover of each phase | Stage IXSCAN; `totalDocsExamined / nReturned` close to 1; no in-memory SORT for work lists |
| Interlock and scan latency | Before go-live | Under 100 ms at the 95th percentile |
| Pattern coverage | Each model change | Every register pattern maps to an index; every index maps to a pattern |
| `$indexStats` | 30 days after go-live, then quarterly | Indexes with zero accesses are proposed for removal |
| Database profiler or Performance Advisor (slow queries over 100 ms) | Continuous | New repeated slow queries are added to the register as patterns |
| Index size against RAM | Quarterly | Indexes of the T2 and T3 collections fit the working set |

## 12. Assumptions

| No. | Assumption | If wrong |
|---|---|---|
| QA1 | Volumes follow A002: 2,400 calipers per day, about 12 routed steps and 8 traced components per caliper | Tiers of section 5 move; budgets are re-applied |
| QA2 | One site today; `siteId` kept as an equality prefix on low-cardinality indexes so a second site needs no index change | If the system stays single-site, the `siteId` prefix can be dropped from those indexes |
| QA3 | MongoDB 7.0 or later: partial indexes, time-series collections with secondary indexes and automatic meta plus time index | Time-series index handling is created explicitly |
| QA4 | Shift, line and OEE reporting reads the Reports collections (`productionCount`, `oeeRecord`, `lossSummary`, `workCenterPerformance`, `operatorPerformance`, `reliabilitySummary`), not raw transactions | Raw transaction collections need additional reporting indexes |
| QA5 | The application caches T0 master data and refreshes it on change | T0 collections need secondary indexes for frequent reads |
| QA6 | `relatedCollectionName` and `relatedEntityId` on `u_mes_syst_erpMessage` always name the primary object of the message | Keep the single reference indexes that were proposed for removal |
| QA7 | Index counts in section 7 are for illustration; the binding list comes from the query pattern register once the module screens are confirmed | Counts change; the method does not |
