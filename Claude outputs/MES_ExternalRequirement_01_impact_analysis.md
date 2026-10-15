# MES_ExternalRequirement_01 — Schema and Collection Impact Analysis

| Item | Value |
|---|---|
| Source file | `01_research/MES_ExternalRequirement_01.xlsx` |
| Sheets reviewed | `MES Requirement` (129 requirements, Q1–Q129), `Options_M01_Refined`, `Options_M02` to `Options_M11`, `Options_Switch`, `Options_xx`, `Sheet1` (empty) |
| Model reviewed | `05_generator/model/flat_model.json`: 299 collections, 6,058 keys, ten modules (mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs) |
| Governing rules | `00_governance/data_modeling_standard.md` (DATA-001 flat documents, DATA-002 BSON types, DATA-003 master/enumeration classification, DATA-004 local-time dates with Date/Datetime tag), `00_governance/mongodb_output_rules.md`, `Folder_Guide.md` |
| Nature of this document | Recommendation only. Nothing in the model, generators, specifications, validators, indexes, samples or governance files has been changed. Every change below is a proposal for the owner's decision. |
| Prepared | 12 Oct 2026 |

## 1. How the workbook was read

The `MES Requirement` sheet is an MES maturity audit questionnaire. Each row has a question number, a source module name (Production Execution, Product Tracking And Traceability, Quality Management, Performance And OEE, Maintenance, Process Management, Material And Inventory Management, Personnel And Labor, Document Management, Resource And Equipment Mgmt, Analytics And Intelligence, General), the feature covered, the audit question, an "Implementation Status (Select)" answer and the four maturity descriptions Level 1 to Level 4. The `Options_*` sheets hold the full six-step answer scale (0 to 5) for each question; Level 5 always describes predictive or autonomous behaviour.

For every question this document states:

1. **Coverage today** — one of:
   - **Covered**: the existing collections and keys already hold every record the requirement needs; only application logic is required.
   - **Partly covered**: the existing collections are right but keys, allowed values, status values or relationship collections must be added.
   - **New collection**: one or more new collections are required.
   - **Not schema**: the requirement is about architecture, infrastructure or user interface and needs no collection change (a recommendation is still given where useful).
   - **Not applicable to the caliper**: the requirement describes a product technology that the reference product does not have; the generic schema impact is still stated so that the MES remains product-neutral.
2. **Existing collections used** — full collection names.
3. **Changes required** — keys to add (with BSON type, Date/Datetime tag where the key holds a date, and reference target), allowed-value and status-value additions, and new collections with module code and module name.

Section 3 lists cross-cutting changes that many questions share, so that the per-question entries in section 4 can cite them by their identifier (X1 to X12). Section 5 specifies every proposed new collection key by key. Section 6 consolidates every change to existing collections, collection by collection. Section 7 lists the value-list changes. Section 8 lists proposed decision-log and assumption-log entries. Section 9 gives the implementation order and the effect on the model counts.

## 2. Assumptions

| No. | Assumption |
|---|---|
| ER-A01 | The questionnaire was written for a different product: a power window switch (PWS) built for the OEM "M&M" (stations such as greasing, pusher assembly, PCB CP test, bezel press-fit, FTM and vision). The requirements are read as **generic MES capabilities** and mapped onto the caliper reference process. The term mapping is in section 2.1. Nothing about the switch product is added to the sample-data universe. |
| ER-A02 | The schema is designed to hold the data needed for **Level 3 (system-enforced) and Level 4 (integrated)** of every question. Level 5 (predictive / autonomous) and the "(Adv)" questions are supported through a generic model-registry and prediction record (X10) and a simulation-study record (X11); no algorithm-specific structures are proposed. |
| ER-A03 | The "Implementation Status (Select)" column records the audited plant's answer. It does not change the target for this design and is not used. |
| ER-A04 | "Blocking", "non-bypassable", "interlock" and "auto-routing" are application behaviour. The schema's job is to hold (a) the configuration that tells the application when to block, (b) the evidence that the check ran, and (c) the authorised override when one is allowed. Each question is assessed on these three points. |
| ER-A05 | "Station" in the questionnaire equals `u_mes_mast_workCenter` (a work centre is the station; `trackingGrain` already distinguishes unit and batch stations). "Work Order" equals `u_mes_plan_productionOrder`. "Switch serial" equals `u_mes_trac_serialNumber` / `u_mes_plan_wipUnit`. "Variant" equals `u_mes_prod_productVariant`. |
| ER-A06 | New collections are numbered after the current last collection (1299), in the order of section 5, starting at 1300. Existing collection numbers and existing `_id` prefixes do not change. The numbers in section 5 are indicative; the generator assigns the final numbers. |
| ER-A07 | New child and relationship collections follow the existing pattern: no `status` key; parent ID+Name pair plus `sequenceNo` (or the line/step number of the parent pattern); audit keys only when the parent is transaction data. |
| ER-A08 | All new keys follow DATA-002: Decimal128 for measured values, limits, percentages, scores and money; Int32 for counts and sequence numbers; Boolean for flags; Date for dates. Every new date key carries the Date or Datetime tag under DATA-004 (keys ending in `Date` are Date and are stored at 00:00:00 local time; all other date keys are Datetime). |
| ER-A09 | Fixed lists proposed below are Rule B enumerations (values in `u_mes_syst_enumerationValue`); lists the plant maintains are Rule A masters. Status values go into `u_mes_syst_statusDefinition` and `u_mes_syst_statusTransition`. |

### 2.1 Switch-to-caliper term mapping used in this review

| Questionnaire term (switch plant) | Caliper equivalent used in this review |
|---|---|
| PCB CP barcode, batch code MR/DD/MM/YY | 2D DataMatrix serial laser-marked at OP090 (`u_mes_trac_serialNumber.dataMatrixPayload`) and casting date code (`u_mes_plan_wipUnit.castDateCode`) |
| Greasing robot, greasing weight, greasing needle | Seal and piston grease dispensing at OP060 (piston and seal assembly); grease shot weight; dispensing nozzle |
| Pusher assembly, bezel / light-guide press-fit, snap-fit force curve | Piston press-in and dust-boot seating at OP060; guide-pin bush press-fit; press force–displacement curve |
| Screw bits, torque, torque-vs-angle curve | Bleed-screw tightening at OP070 (`u_mes_perf_torqueResult`); nutrunner socket |
| Air pressure, FTM continuity test | Pressure leak test at OP080 (`u_mes_perf_leakTestResult`, `u_mes_perf_leakTestResultStage`) |
| Vision station, symbol presence, line-cut | Final vision inspection of laser mark, dust boot seating and anodise appearance at OP100 |
| Symbol marking (laser / pad print) | Laser marking at OP090 |
| Colour (Piano Black / Matt Black / Chrome) | Anodise / surface finish (`u_mes_prod_surfaceFinish`) and hand (LH/RH) of the variant |
| Flush and gap per key | Piston protrusion and dust-boot seating height per piston position (single-piston caliper: one position; twin-piston variants: two) |
| Locator / fixture / change-over card | Machining fixture, leak-test fixture, assembly nest (`u_mes_maint_tool` with toolClass Fixture) |
| LED illumination, insulation resistance, haptic click, SMT (SPI/AOI/ICT), firmware flashing | No equivalent on the caliper (no electronics). Treated as **Not applicable to the caliper**; the generic structures (per-position results, curves, program version) still cover them for other products. |
| Moisture-sensitive (MSL) reels, shelf life of grease / adhesives / rubber | Brake-fluid-compatible grease pot life, EPDM seal and dust-boot shelf life, anodising chemical bath life |

## 3. Cross-cutting changes

These twelve changes recur across many questions. Each is specified in full in sections 5 and 6.

| ID | Theme | What changes | Questions served |
|---|---|---|---|
| X1 | Interlock rules and interlock events | New master `u_mes_syst_interlockRule` (what is checked, where, whether override is allowed, which role may override) and new transaction `u_mes_plan_interlockEvent` (every block, pass-after-override and override with reason code, authoriser and e-signature). Six new check flags on `u_mes_plan_operationExecution`. | Q2, Q3, Q4, Q6, Q7, Q8, Q10, Q11, Q13, Q21, Q25, Q29, Q31, Q58, Q60, Q62, Q69, Q71, Q72, Q73, Q74, Q75, Q80, Q81, Q82, Q90, Q91, Q92, Q97, Q99, Q101, Q103, Q120, Q122, Q125, Q126, Q127, Q129 |
| X2 | Escalation rules (role routing and SLA) | New master `u_mes_syst_escalationRule` with child `u_mes_syst_escalationRuleLevel`; new keys on `u_mes_syst_notification`, `u_mes_plan_andonEvent`, `u_mes_plan_andonType`, `u_mes_perf_alarm`, `u_mes_maint_maintenanceWorkOrder`, `u_mes_qual_audit`. | Q9, Q34, Q42, Q43, Q56, Q69, Q70, Q76, Q97 |
| X3 | Alert rules (condition → action) | New master `u_mes_syst_alertRule`; `u_mes_syst_notification` gets `alertRuleId/alertRuleName`. | Q42, Q43, Q70, Q76, Q97, Q112 |
| X4 | Role-authorised status transitions | New relationship `u_mes_syst_statusTransitionRole` so that each allowed status transition names the roles that may perform it. | Q1, Q2, Q28, Q29, Q30, Q61, Q62, Q114 |
| X5 | Reason codes made mandatory where the questionnaire asks for them | New `reasonType` values on `u_mes_perf_reasonCode`; reason-code ID+Name pairs added to production order hold, quality hold release, step override, rework order, alarm closure, maintenance root cause, exposure-timer reset. | Q2, Q6, Q8, Q18, Q19, Q29, Q30, Q51, Q69 |
| X6 | Station acknowledgement of documents and recipes | New transaction `u_mes_plan_documentAcknowledgement`; station and variant relationships for work instructions; re-acknowledgement flag. | Q3, Q4, Q89, Q90, Q91, Q92, Q95 |
| X7 | Operator station session | New transaction `u_mes_plan_operatorSession` (badge / biometric login per station, linked to order and shift). | Q80, Q81, Q82, Q84, Q85, Q114 |
| X8 | Per-position results and measurement curves | New child `u_mes_qual_characteristicPosition`; new masters `u_mes_qual_curveEnvelope` + child `u_mes_qual_curveEnvelopeWindow`; new transaction `u_mes_qual_measurementCurve`; new time-series `u_mes_qual_measurementCurvePoint`; position, image and curve keys on `u_mes_qual_inspectionResult`. | Q24, Q123, Q124, Q125, Q126, Q127, Q128 |
| X9 | Program / recipe version traceability per unit | Recipe version and checksum on `u_mes_plan_operationExecution` and `u_mes_trac_asBuiltRecordOperation`; new transaction `u_mes_plan_recipeDownload`; new relationships `u_mes_prod_recipeProductVariant` and `u_mes_prod_recipeControlledDocument`. | Q3, Q17, Q20, Q21, Q57, Q58, Q62, Q122, Q129 |
| X10 | Analytics model registry and predictions | New master `u_mes_syst_analyticsModel` and new transaction `u_mes_syst_modelPrediction`; model keys on `u_mes_qual_inspectionResult`. | Q33, Q46, Q47, Q54, Q67, Q78, Q87, Q88, Q104, Q105, Q111, Q112, Q129 |
| X11 | Simulation / digital-twin studies | New transaction `u_mes_syst_simulationStudy`. | Q65, Q66, Q79, Q107, Q108 |
| X12 | Record integrity and retention policy | New master `u_mes_syst_recordPolicy` (edit policy, lock-on-status, retention years per collection). `u_mes_syst_auditTrail` and `u_mes_syst_auditTrailChange` already hold user, time, old value and new value. | Q1, Q32, Q115, Q118 |

### 3.1 Summary of the result

| Coverage | Questions | Count |
|---|---|---|
| Covered | Q10, Q12, Q16, Q35, Q39, Q41, Q48, Q50, Q117 | 9 |
| Partly covered (keys, values or relationships only) | Q2, Q5, Q6, Q11, Q13, Q14, Q17, Q18, Q19, Q20, Q22, Q23, Q24, Q26, Q28, Q29, Q30, Q31, Q36, Q37, Q38, Q44, Q51, Q55, Q57, Q59, Q61, Q62, Q63, Q64, Q67, Q68, Q72, Q74, Q75, Q77, Q81, Q82, Q83, Q84, Q85, Q87, Q89, Q91, Q93, Q94, Q95, Q96, Q98, Q99, Q100, Q101, Q102, Q103, Q106, Q109, Q110, Q114, Q116, Q119, Q120, Q122, Q129 | 63 |
| New collection(s) needed | Q1, Q3, Q4, Q7, Q8, Q9, Q15, Q21, Q25, Q27, Q32, Q33, Q34, Q40, Q42, Q43, Q45, Q46, Q47, Q49, Q52, Q53, Q54, Q56, Q58, Q60, Q65, Q66, Q69, Q70, Q71, Q73, Q76, Q78, Q79, Q80, Q86, Q88, Q90, Q92, Q97, Q104, Q105, Q107, Q108, Q111, Q112, Q115, Q118, Q123, Q125, Q126, Q127 | 53 |
| Not schema | Q113 | 1 |
| Not applicable to the caliper (generic impact still stated) | Q121, Q124, Q128 | 3 |
| **Total** | | **129** |

A question is classed "New collection" when it cannot reach Level 3 without a collection that does not exist today and that question is the main reason for the collection. A question whose own data is already modelled is classed "Partly covered" even when it also uses a cross-cutting collection (X1–X12) that is introduced for other questions. Q115 and Q118 are counted under "New collection" because X12 and the optional backup record are proposed; both are also partly infrastructure.

### 3.2 Proposed new collections (44)

| No. | Module code | Module name | Collection | Kind | Type | UI label | Purpose | Questions |
|---|---|---|---|---|---|---|---|---|
| 1300 | mast | Master Data Management | `u_mes_mast_roleRequiredSkill` | Relationship | Master | Role Required Skills | Skills a user must hold before a role's rights become active | Q114, Q81 |
| 1301 | prod | Product Definition | `u_mes_prod_recipeProductVariant` | Relationship | Master | Recipe Variants | Variants a recipe / machine program is released for | Q3, Q57, Q64, Q129 |
| 1302 | prod | Product Definition | `u_mes_prod_recipeControlledDocument` | Relationship | Master | Recipe Reference Files | Golden images, program files and reference curves attached to a recipe version | Q58, Q129 |
| 1303 | prod | Product Definition | `u_mes_prod_workInstructionWorkCenter` | Relationship | Master | Work Instruction Stations | Stations a work instruction is displayed at | Q3, Q89, Q91 |
| 1304 | prod | Product Definition | `u_mes_prod_workInstructionProductVariant` | Relationship | Master | Work Instruction Variants | Variants a whole work instruction applies to | Q3, Q89 |
| 1305 | plan | Planning and Execution | `u_mes_plan_operatorSession` | Entity | Transaction | Operator Sessions | Badge / biometric login and logout at a station | Q80, Q81, Q82, Q84, Q85 |
| 1306 | plan | Planning and Execution | `u_mes_plan_documentAcknowledgement` | Entity | Transaction | Document Acknowledgements | Operator read-and-understood record for a work instruction, recipe or document revision at a station | Q4, Q90, Q92, Q95 |
| 1307 | plan | Planning and Execution | `u_mes_plan_interlockEvent` | Entity | Transaction | Interlock Events | Every interlock that blocked, was overridden or was cleared, with reason and authoriser | X1 list |
| 1308 | plan | Planning and Execution | `u_mes_plan_recipeDownload` | Entity | Transaction | Recipe Downloads | Program / recipe load to a machine with checksum verification | Q58, Q62, Q122 |
| 1309 | plan | Planning and Execution | `u_mes_plan_setupVerification` | Entity | Transaction | Setup Verifications | Pre-start verification of fixture, tool, program, parameter and component set-up | Q60, Q106, Q120 |
| 1310 | plan | Planning and Execution | `u_mes_plan_setupVerificationItem` | Child | Transaction | Setup Verification Items | Each expected-versus-scanned check in a set-up verification | Q60, Q106, Q120 |
| 1311 | matl | Material Management | `u_mes_matl_exposureTimer` | Entity | Transaction | Exposure Timers | Floor-life / pot-life / open-time clock per lot or container | Q73 |
| 1312 | matl | Material Management | `u_mes_matl_replenishmentRule` | Entity | Master | Replenishment Rules | Min-max / e-Kanban rule per item and line-side location | Q76, Q77 |
| 1313 | matl | Material Management | `u_mes_matl_materialDemandForecast` | Entity | Reports | Material Demand Forecast | Short-term component demand and projected shortage per line | Q76, Q78 |
| 1314 | trac | Traceability | `u_mes_trac_traceInvestigation` | Entity | Transaction | Trace Investigations | Saved forward / reverse trace run with its containment link | Q14, Q15 |
| 1315 | trac | Traceability | `u_mes_trac_traceInvestigationResult` | Child | Transaction | Trace Investigation Results | Each serial, lot or container found by a trace run | Q14, Q15 |
| 1316 | qual | Quality Management | `u_mes_qual_characteristicPosition` | Child | Master | Characteristic Positions | Per-position nominal and limits of a characteristic | Q124, Q125, Q126, Q127, Q128 |
| 1317 | qual | Quality Management | `u_mes_qual_curveEnvelope` | Entity | Master | Curve Envelopes | Approved golden-sample envelope for a force, torque, pressure or signal curve | Q123, Q127, Q128 |
| 1318 | qual | Quality Management | `u_mes_qual_curveEnvelopeWindow` | Child | Master | Curve Envelope Windows | Each evaluation window of an envelope | Q123, Q127, Q128 |
| 1319 | qual | Quality Management | `u_mes_qual_measurementCurve` | Entity | Transaction | Measurement Curves | One captured curve per unit, position and test with envelope verdict | Q123, Q127, Q128 |
| 1320 | qual | Quality Management | `u_mes_qual_measurementCurvePoint` | Entity | Telemetry | Measurement Curve Points | Curve points (time-series collection) | Q123, Q127, Q128 |
| 1321 | qual | Quality Management | `u_mes_qual_defectRecord` | Entity | Transaction | Defect Records | One logged defect per unit with first-fail station and 4M data | Q18, Q27, Q44 |
| 1322 | qual | Quality Management | `u_mes_qual_auditSchedule` | Entity | Master | Audit Schedules | Layered process audit plan: layer, area, frequency, auditor role | Q34 |
| 1323 | qual | Quality Management | `u_mes_qual_inspectionPlanProductVariant` | Relationship | Master | Inspection Plan Variants | Variants an inspection plan applies to | Q23 |
| 1324 | perf | Performance Management | `u_mes_perf_alarmDefinition` | Entity | Master | Alarm Definitions | Alarm code master per equipment type with restart-block and escalation | Q68, Q69 |
| 1325 | perf | Performance Management | `u_mes_perf_lossSummary` | Entity | Reports | Loss Summary | Loss Pareto per line, shift, day and reason | Q37, Q44, Q45 |
| 1326 | perf | Performance Management | `u_mes_perf_workCenterPerformance` | Entity | Reports | Station Performance | Hourly throughput, cycle time, WIP, blocked / starved time and constraint flag per station | Q38, Q40, Q45, Q116 |
| 1327 | perf | Performance Management | `u_mes_perf_operatorPerformance` | Entity | Reports | Operator Performance | Labour efficiency per operator, station, variant and shift | Q86, Q88 |
| 1328 | maint | Tooling And Maintenance | `u_mes_maint_maintenanceWorkOrderTask` | Child | Transaction | Work Order Checklist | Checklist task results of a maintenance work order | Q49 |
| 1329 | maint | Tooling And Maintenance | `u_mes_maint_sparePartTransaction` | Entity | Transaction | Spare Part Transactions | Spare-part issue, return, receipt and adjustment | Q52 |
| 1330 | maint | Tooling And Maintenance | `u_mes_maint_reliabilitySummary` | Entity | Reports | Reliability Summary | MTBF / MTTR per equipment, line and period | Q53 |
| 1331 | maint | Tooling And Maintenance | `u_mes_maint_equipmentLifecycleEvent` | Entity | Transaction | Equipment Lifecycle | Commissioning, overhaul, refurbishment, health assessment and decommissioning events | Q104, Q105 |
| 1332 | syst | System and Integration | `u_mes_syst_interlockRule` | Entity | Master | Interlock Rules | Configured checks and their override policy | X1 list |
| 1333 | syst | System and Integration | `u_mes_syst_statusTransitionRole` | Relationship | Master | Status Transition Roles | Roles allowed to perform a status transition | X4 list |
| 1334 | syst | System and Integration | `u_mes_syst_escalationRule` | Entity | Master | Escalation Rules | Routing and SLA rule for an exception type | X2 list |
| 1335 | syst | System and Integration | `u_mes_syst_escalationRuleLevel` | Child | Master | Escalation Levels | Each escalation level: delay, role, channel | X2 list |
| 1336 | syst | System and Integration | `u_mes_syst_alertRule` | Entity | Master | Alert Rules | Threshold rule on a KPI or signal with the resulting action | X3 list |
| 1337 | syst | System and Integration | `u_mes_syst_analyticsModel` | Entity | Master | Analytics Models | Registry of AI / ML / rule models and versions | X10 list |
| 1338 | syst | System and Integration | `u_mes_syst_modelPrediction` | Entity | Transaction | Model Predictions | Each prediction, classification or recommendation and its outcome | X10 list |
| 1339 | syst | System and Integration | `u_mes_syst_simulationStudy` | Entity | Transaction | Simulation Studies | Digital-twin / what-if study, result and controlled rollout | X11 list |
| 1340 | syst | System and Integration | `u_mes_syst_recordPolicy` | Entity | Master | Record Policies | Edit policy, lock-on-status and retention per collection | Q32, Q115, Q118 |
| 1341 | syst | System and Integration | `u_mes_syst_savedView` | Entity | Master | Saved Views | Saved dashboard / comparison filters per user or role | Q45, Q109 |
| 1342 | syst | System and Integration | `u_mes_syst_backupRun` | Entity | Transaction | Backup and Restore Runs | Backup and restore-test evidence with recovery time (optional) | Q118 |
| 1343 | matl | Material Management | `u_mes_matl_storageLocationAllowedItem` | Relationship | Master | Storage Allowed Items | Items (or item groups) a location may hold — storage matrix (from `Options_Switch` row 13, optional) | Options_Switch 13 |

No new collection is needed in the ehs (Environment Health and Safety) module. Environmental monitoring in Q96–Q97 concerns process conditions (lux, ESD, temperature, humidity) that protect product quality, so it stays in perf (Performance Management) with `u_mes_perf_processTag` and `u_mes_perf_processReading`.

By module: mast 1, prod 4, plan 6, matl 4, trac 2, qual 8, perf 4, maint 4, syst 11. By kind: 30 entity, 6 child, 8 relationship (0 value-list). By type: Master 21, Transaction 17, Reports 5, Telemetry 1, Audit Trail 0 (counting `u_mes_syst_backupRun` as Transaction). `u_mes_plan_interlockEvent` could alternatively be classed as Audit Trail; it is proposed as Transaction because it is part of the execution record and is queried with the order and unit.

## 4. Requirement-by-requirement review

Each entry gives the feature, what the requirement needs from the data model, the coverage, the existing collections used and the changes required. Keys listed as "add" are specified with their BSON type in section 6.

### 4.1 Production Execution (Q1–Q9)

**Q1 — Work Order Management: full lifecycle create → release → execute → hold → close, enforced with role-based authorisation and audit trail.**
- Needs: order status model with allowed transitions; the role allowed to perform each transition; a record of who changed what and when; protection of closed orders.
- Coverage: **New collection.**
- Existing: `u_mes_plan_productionOrder` (status values Created, Released, In Progress, On Hold, Completed, Closed, Cancelled; `closedAt`, `closedById`, `closedBy`), `u_mes_plan_productionOrderRelease`, `u_mes_syst_statusDefinition`, `u_mes_syst_statusTransition` (`requiresSignature`, `requiresReason`), `u_mes_mast_role`, `u_mes_mast_rolePermission`, `u_mes_syst_auditTrail`, `u_mes_syst_auditTrailChange`, `u_mes_syst_electronicSignature`.
- Changes: X4 — new `u_mes_syst_statusTransitionRole` (syst) to bind each transition (for example Released → On Hold, On Hold → In Progress, Completed → Closed) to the roles allowed to perform it. X12 — new `u_mes_syst_recordPolicy` (syst) so that `u_mes_plan_productionOrder` is locked when status reaches Closed or Cancelled. Hold keys are added under Q2.

**Q2 — Work Order Management: HOLD on an order / batch blocks all downstream transactions until authorised release with a reason code.**
- Needs: hold flag and hold reference on the order; hold reason code; release decision with reason, authoriser and signature; evidence of blocked transactions.
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_qualityHold`, `u_mes_qual_qualityHoldHeldObject` (polymorphic, can already hold a production order, lot, WIP unit or container), `u_mes_plan_wipUnit.onHold`, `u_mes_plan_lot.onHold`, `u_mes_plan_container.onHold`.
- Changes: add to `u_mes_plan_productionOrder`: `onHold`, `qualityHoldId`/`qualityHoldName`, `holdReasonCodeId`/`holdReasonCodeName`. Add to `u_mes_qual_qualityHold`: `releaseReasonCodeId`/`releaseReasonCodeName`, `releaseElectronicSignatureId`/`releaseElectronicSignatureName`. X5 — `reasonType` values Hold and Hold Release on `u_mes_perf_reasonCode`. X1 — interlock rule type Hold Check; each blocked transaction is written to `u_mes_plan_interlockEvent`. X4 — release transition restricted to roles.

**Q3 — Work Instruction / Recipe Dispatch: auto-load the approved WI / OGS / machine program per variant and station; block if missing or obsolete.**
- Needs: which WI and which recipe apply to an item, variant, operation and station; release status and effectivity; evidence of what was loaded and verified.
- Coverage: **New collection.**
- Existing: `u_mes_prod_workInstruction` (version, effectivity, status In Preparation / Released / Obsolete), `u_mes_prod_workInstructionStepProductVariant`, `u_mes_prod_recipe` (version, checksum, effectivity, status), `u_mes_prod_billOfProcessStep` (`recipeId`, `workInstructionId`, `inspectionPlanId` per step), `u_mes_plan_operationExecution.checksRecipeVerified`.
- Changes: new `u_mes_prod_workInstructionWorkCenter` and `u_mes_prod_workInstructionProductVariant` (prod) so that selection by station and variant is possible at header level; new `u_mes_prod_recipeProductVariant` (prod) for variant-specific programs; X9 — add `recipeVersion`, `recipeChecksum` to `u_mes_plan_operationExecution`; X6 — add `checksDocumentAcknowledged` to `u_mes_plan_operationExecution`; X1 — interlock rule types Recipe Release Check and Work Instruction Release Check.

**Q4 — Work Instruction / Recipe Dispatch: after a revision, force re-validation at the station and block the next operation until confirmed.**
- Needs: a re-acknowledgement requirement on the document; a per-station, per-operator acknowledgement record against the exact revision.
- Coverage: **New collection.**
- Existing: `u_mes_prod_workInstruction.readAcknowledgementRequired`, `u_mes_prod_engineeringChange`, `u_mes_prod_engineeringChangeAffectedObject`.
- Changes: X6 — new `u_mes_plan_documentAcknowledgement` (plan) holding document collection, ID, version, station, operator, variant, order, shift and time; add `reacknowledgeOnRevision` to `u_mes_prod_workInstruction`; X1 — interlock rule type Acknowledgement Check.

**Q5 — Station Logging & Scanner-Based Capture: every unit entry / exit at each station captured by barcode / QR in real time.**
- Needs: start and completion time per unit per station; how the event was captured (scan, PLC, manual); the scanned code.
- Coverage: **Partly covered.**
- Existing: `u_mes_plan_operationExecution` (`startedAt`, `completedAt`, `wipUnitId`, `workCenterId`, `equipmentId`, `operatorUserId`), `u_mes_plan_stepCompletion.scannedCode`, `u_mes_syst_businessEvent`.
- Changes: add to `u_mes_plan_operationExecution`: `captureMethod` (enumeration Scan, PLC Signal, Manual Entry), `startScanCode`, `operatorSessionId`/`operatorSessionName` (X7).

**Q6 — Station Routing Sequence Enforcement: block a unit that skips a prior station; override only with authorised reason code.**
- Needs: routing sequence; previous-step check evidence; override record.
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_routingStep` (`stepNo`, `isOptional`, `reworkReturnStepNo`), `u_mes_prod_routingStepNextStep`, `u_mes_plan_wipUnit.currentStepNo`, `u_mes_plan_wipUnitCompletedStep`, `u_mes_plan_operationExecution.checksPreviousStepComplete`.
- Changes: X1 — interlock rule type Sequence Check and its override events in `u_mes_plan_interlockEvent` (new, plan); X5 — `reasonType` value Interlock Override. No change to the routing collections.

**Q7 — Execution Data Validation at Source: reject wrong, duplicate or out-of-context serial / WO / station transactions with audit-trailed exceptions; Level 4 cross-module rules.**
- Needs: configured validation rules; a record of every rejected transaction with the rejected value and reason.
- Coverage: **New collection.**
- Existing: unique index on `u_mes_trac_serialNumber.recordNo`; `u_mes_syst_businessEvent` (generic event log, no rule reference).
- Changes: X1 — new `u_mes_syst_interlockRule` (syst) with rule types Duplicate Serial, Wrong Order, Wrong Station, Wrong Variant, Out-of-Context Scan; new `u_mes_plan_interlockEvent` (plan) with `scannedValue`, `expectedValue`, `outcome`.

**Q8 — Real-Time Execution Exception Handling: non-bypassable interlock / alarm on wrong variant, skipped station, torque or force out of limit, NG test result; mandatory reason code before continuing.**
- Needs: the interlock configuration, the event, the reason code and the clearing authority.
- Coverage: **New collection.**
- Existing: `u_mes_perf_torqueResult.result`, `u_mes_perf_leakTestResult.verdict`, `u_mes_qual_inspectionResult.result`, `u_mes_plan_stepCompletion` (`overridden`, `overrideById`, `overrideBy`, `overrideReason` free text).
- Changes: X1 — `u_mes_syst_interlockRule` and `u_mes_plan_interlockEvent`; add to `u_mes_plan_stepCompletion`: `overrideReasonCodeId`/`overrideReasonCodeName` (X5; the free-text `overrideReason` stays as a comment).

**Q9 — Real-Time Execution Exception Handling: auto-route the exception to the correct role and track closure with escalation if unresolved within a defined time.**
- Needs: routing rule by exception type; SLA per level; escalation record; closure time.
- Coverage: **New collection.**
- Existing: `u_mes_syst_notification` (`escalationLevel`, `raisedAt`, `acknowledgedAt`), `u_mes_syst_notificationRecipient` (`roleId`, `channel`), `u_mes_plan_andonEventEscalation`.
- Changes: X2 — new `u_mes_syst_escalationRule` and `u_mes_syst_escalationRuleLevel` (syst); add to `u_mes_syst_notification`: `escalationRuleId`/`escalationRuleName`, `responseDueAt` (Datetime), `resolvedAt` (Datetime), `resolvedById`/`resolvedBy`, `interlockEventId`/`interlockEventName`. Level 4 (route by skill) uses `u_mes_mast_roleRequiredSkill` (new, mast) and `u_mes_mast_skillCertification`.

### 4.2 Product Tracking And Traceability (Q10–Q21, Q119, Q120)

**Q10 — Unique Serialization & Scanning: unique serial generated at a defined start point; duplicates rejected.**
- Needs: number range, serial record, uniqueness.
- Coverage: **Covered.**
- Existing: `u_mes_syst_numberRange` (`prefix`, `formatMask`, `currentValue`, `checkDigitMethod`), `u_mes_trac_serialNumber` (unique `recordNo`, `dataMatrixPayload`, `issuedAt`, `markedAt`), `u_mes_prod_item.isSerialised`, `u_mes_prod_item.serialNumberRangeId`.
- Changes: none to the schema. Duplicate-rejection evidence is written to `u_mes_plan_interlockEvent` (X1) when that collection is adopted.

**Q11 — Unique Serialization & Scanning: scan enforced at every mandatory station; missing or invalid scan blocks execution.**
- Needs: which steps require a scan; scan evidence per step.
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_workInstructionStep.requiresScan`, `u_mes_prod_billOfProcessStepConsumedComponent.verifyByScan`, `u_mes_plan_stepCompletion.scannedCode`.
- Changes: add `captureMethod` and `startScanCode` to `u_mes_plan_operationExecution` (as Q5); X1 — interlock rule type Mandatory Scan bound to a routing step (`u_mes_syst_interlockRule.operationId`, `workCenterId`).

**Q12 — Timestamp & Lot Linkage: every station event time-stamped and linked to the serial without manual entry.**
- Coverage: **Covered.**
- Existing: `u_mes_plan_operationExecution` (`startedAt`, `completedAt`, `wipUnitId`), `u_mes_plan_stepCompletion`, `u_mes_perf_torqueResult.tightenedAt`, `u_mes_perf_leakTestResult.testedAt`, `u_mes_qual_inspectionResult.measuredAt`, `u_mes_trac_serialNumber.wipUnitId`.
- Changes: none. Capture method recorded once Q5 keys are added.

**Q13 — Timestamp & Lot Linkage: child-part / material lot consumption linked to the serial at point of use as a non-bypassable step.**
- Needs: consumption per unit with component lot; scan verification; block when missing.
- Coverage: **Partly covered.**
- Existing: `u_mes_matl_materialConsumption` (`wipUnitId`, `componentItemId`, `componentLotId`, `componentSerialNo`, `scanVerified`, `bomLineNo`), `u_mes_trac_genealogyLink`, `u_mes_prod_billOfMaterialComponent.isTraceable`, `u_mes_prod_billOfMaterialComponent.traceLevel`.
- Changes: add `checksMaterialReleased` to `u_mes_plan_operationExecution`; X1 — interlock rule type Component Lot Capture.

**Q14 — Forward & Reverse Traceability: self-service reverse trace from serial to components, lots, operators and process parameters.**
- Needs: the links (present) plus a reproducible, audit-ready trace output.
- Coverage: **Partly covered.**
- Existing: `u_mes_trac_genealogyLink`, `u_mes_trac_componentLotLink`, `u_mes_trac_asBuiltRecord` and its child collections, `u_mes_plan_operationExecution`, `u_mes_perf_torqueResult`, `u_mes_perf_leakTestResult`, `u_mes_qual_inspectionResult`, `u_mes_perf_processReading`.
- Changes: new `u_mes_trac_traceInvestigation` and `u_mes_trac_traceInvestigationResult` (trac) to store each trace run and its result list as audit evidence; X9 — `recipeVersion` on operation records so that parameters are part of the trace.

**Q15 — Forward & Reverse Traceability: forward trace from a suspect lot to all affected serials, producing a containment list.**
- Needs: forward links (present) and a stored containment list that can feed a quality hold.
- Coverage: **New collection.**
- Existing: `u_mes_trac_componentLotLink`, `u_mes_trac_genealogyLink`, `u_mes_qual_qualityHold`, `u_mes_qual_qualityHoldHeldObject`, `u_mes_qual_customerComplaintSuspectLot`.
- Changes: new `u_mes_trac_traceInvestigation` (direction Forward, start lot, `qualityHoldId`, `nonconformanceId`, `customerComplaintId`) and `u_mes_trac_traceInvestigationResult` (each affected serial / lot / container with location, status and shipment at the time of the run).

**Q16 — Genealogy & As-Built Record: parent-child genealogy captured as a controlled record.**
- Coverage: **Covered.**
- Existing: `u_mes_trac_genealogyLink` (`parentWipUnitId`, `parentSerialNumberId`, `childType`, `childItemId`, `childLotId`, `childSerialNo`, `linkType`, `removedAt`, `removedReason`), `u_mes_trac_componentLotLink`.
- Changes: none (Q119 adds child serial references for in-house sub-assemblies).

**Q17 — Genealogy & As-Built Record: complete as-built record per unit (BOM + process flow + test results + parameters) on demand.**
- Coverage: **Partly covered.**
- Existing: `u_mes_trac_asBuiltRecord` (torque and leak summary, lots, deviation, release, `recordHash`), `u_mes_trac_asBuiltRecordComponent`, `u_mes_trac_asBuiltRecordOperation`, `u_mes_trac_asBuiltRecordInspectionResult`.
- Changes: add to `u_mes_trac_asBuiltRecordOperation`: `recipeId`/`recipeName`, `recipeVersion`, `recipeChecksum` (X9). Add to `u_mes_trac_asBuiltRecord`: `genealogyComplete`, `missingComponentCount` (used by Q71).

**Q18 — Rework & Scrap Traceability: genealogy and original serial preserved across rework loops, with mandatory reason codes.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_reworkOrder`, `u_mes_qual_reworkOrderWipUnit`, `u_mes_qual_reworkOrderStep`, `u_mes_plan_wipUnit.reworkCount`, `u_mes_plan_operationExecution` (`executionType`, `attemptNo`), `u_mes_trac_genealogyLink` (`removedAt`, `removedReason`).
- Changes: add `reasonCodeId`/`reasonCodeName` to `u_mes_qual_reworkOrder` (X5, reasonType Rework); per-unit defect evidence through new `u_mes_qual_defectRecord` (qual), which carries `reworkOrderId`.

**Q19 — Rework & Scrap Traceability: scrap traceable with mandatory reason and disposition history linked to the serial.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_scrapRecord` (`defectCodeId`, `wipUnitId`, `lotId`, `nonconformanceId`, `approvedById`), `u_mes_qual_nonconformanceAffectedObject` (`dispositionTypeId`, `dispositionById`, `dispositionAt`).
- Changes: add to `u_mes_qual_scrapRecord`: `serialNumberId`/`serialNumberName`, `dispositionTypeId`/`dispositionTypeName`.

**Q20 — Software/Firmware Traceability: firmware / test-program / parameter set per unit linked into genealogy.**
- Coverage: **Partly covered.** For the caliper there is no firmware; the equivalent is the leak-test program, nutrunner program, laser-marking program and vision program used for each serial.
- Existing: `u_mes_perf_torqueResult.programNo`, `u_mes_perf_leakTestResult.programNo`, `u_mes_plan_operationExecution.recipeId`, `u_mes_syst_iotDevice.firmwareVersion` (device level).
- Changes: X9 — `recipeVersion`, `recipeChecksum` on `u_mes_plan_operationExecution` and `u_mes_trac_asBuiltRecordOperation`; `markingRecipeId`/`markingRecipeName`, `markingRecipeVersion` on `u_mes_trac_serialNumber`.

**Q21 — Software/Firmware Traceability: block final assembly / packing on wrong or unapproved program version.**
- Coverage: **New collection.**
- Existing: `u_mes_prod_recipe` (`version`, `checksum`, status Released / Obsolete).
- Changes: X9 — new `u_mes_plan_recipeDownload` (plan) holding expected and reported checksum and the verification result; X1 — interlock rule type Program Version Check.

**Q119 — Multi-Sub-assembly Genealogy: unique serial per assembly and genealogy to every sub-assembly serial.**
- Coverage: **Partly covered.** For the caliper the in-house sub-assemblies are the piston-and-seal set and the bracket-with-guide-pins set.
- Existing: `u_mes_trac_genealogyLink` (`childSerialNo` is free text), `u_mes_trac_serialNumber`, `u_mes_plan_wipUnit`.
- Changes: add to `u_mes_trac_genealogyLink`: `childSerialNumberId`/`childSerialNumberName` and `childWipUnitId`/`childWipUnitName`, so that sub-assemblies serialised by this MES are referenced by ID (bought-in serials stay in `childSerialNo`).

**Q120 — Variant & Colour Verification at Line Start: verify variant part number and colour against WO / BOM and block mismatch.**
- Coverage: **Partly covered.** For the caliper: hand (LH/RH), piston diameter and surface finish (anodise colour).
- Existing: `u_mes_prod_productVariant` (`optionsHand`, `optionsSurfaceFinishId`, `optionsColour`), `u_mes_plan_productionOrder.productVariantId`, `u_mes_plan_wipUnit.productVariantId`.
- Changes: add `productVariantId`/`productVariantName` and `checksVariantVerified` to `u_mes_plan_operationExecution`; set-up level verification through new `u_mes_plan_setupVerification` and `u_mes_plan_setupVerificationItem` (check type Variant); X1 — interlock rule type Variant Check.

### 4.3 Quality Management (Q22–Q34, Q124–Q128)

**Q22 — Quality Planning & Master Data: control plan, inspection and sampling plans, CTQs (CC/SC) and LPA plans as version-controlled master data with approval workflow.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_controlPlan`, `u_mes_qual_controlPlanLine`, `u_mes_qual_inspectionPlan`, `u_mes_qual_inspectionPlanLine`, `u_mes_qual_samplingPlan`, `u_mes_qual_characteristic.classification`, `u_mes_qual_checkSheet` (all with version, approval and effectivity).
- Changes: approval workflow by role through X4 (`u_mes_syst_statusTransitionRole`, counted under Q1). The LPA plan is missing today; it is delivered by the new `u_mes_qual_auditSchedule` counted under Q34.

**Q23 — Quality Planning & Master Data: auto-select the correct control plan / CTQ set / sampling rule by variant, station and revision.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_inspectionPlan` (`itemId`, `operationId`, `workCenterId`, `version`, `effectiveFrom`, `effectiveTo`, `samplingPlanId`), `u_mes_qual_controlPlan.itemRevision`, `u_mes_prod_billOfProcessStep.inspectionPlanId`.
- Changes: add `itemRevision` to `u_mes_qual_inspectionPlan`; new `u_mes_qual_inspectionPlanProductVariant` (qual).

**Q24 — Inspection & Test Data Capture: actual measured values (torque, force, pressure, grease weight, dimensions) captured against serial, station and time.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_inspectionResult` (`measuredValue` Decimal128, limits, `wipUnitId`, `workCenterId`, `measuredAt`), `u_mes_perf_torqueResult`, `u_mes_perf_leakTestResult`, `u_mes_perf_leakTestResultStage`, `u_mes_qual_spcSampleReading`.
- Changes: X8 — `positionNo`, `positionName` on `u_mes_qual_inspectionResult` so that multi-position characteristics (twin-piston variants, coating thickness at several points) are captured per position.

**Q25 — Inspection & Test Data Capture: block progression if a mandatory check is missing or NOK.**
- Coverage: **New collection.**
- Existing: `u_mes_qual_inspectionPlan.blockOnFail`, `u_mes_qual_inspectionPlanLine.overrideAllowed`, `u_mes_qual_inspectionPlanLine.autoNcOnFail`.
- Changes: X1 — interlock rule types Mandatory Inspection and NOK Result; events in `u_mes_plan_interlockEvent`.

**Q26 — SPC Engine: control charts and Cp/Cpk in MES (n = 5); Level 3 violations trigger mandatory reaction.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_spcChart` (Cp, Cpk, Pp, Ppk, subgroup size), `u_mes_qual_spcChartControlLimit`, `u_mes_qual_spcChartRule`, `u_mes_qual_spcSample`, `u_mes_qual_spcSampleReading`, `u_mes_qual_spcSampleViolation`.
- Changes: add to `u_mes_qual_spcSample`: `reactionType` (enumeration Alert, Hold, Recheck, Stop Line), `qualityHoldId`/`qualityHoldName`, `notificationId`/`notificationName`. X3 — alert rule metric SPC Rule Violation.

**Q27 — Defect Logging & Classification: standardised defect codes, first-fail station and time, linked to serial with 4M data.**
- Coverage: **New collection.**
- Existing: `u_mes_qual_defectCode`, `u_mes_qual_defectGroup`, `u_mes_plan_operationExecutionDefectCode` (relationship only, no detail), `u_mes_qual_nonconformance` (`detectedAtOperationId`, `originOperationId`).
- Changes: new `u_mes_qual_defectRecord` (qual) — one document per defect per unit with `defectCodeId`, `isFirstFail`, detected and origin operation and station, `fourMCategory` (enumeration Man, Machine, Material, Method), operator, equipment, component lot, position, image and the links to nonconformance, rework and scrap.

**Q28 — NCR & Disposition Workflow: detect → log → review → disposition → closure with role-based authorisation and audit trail.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_nonconformance` (status Open, Contained, Dispositioned, Closed, Cancelled), `u_mes_qual_nonconformanceAffectedObject` (disposition per object), `u_mes_qual_nonconformanceMrbUser`, `u_mes_qual_dispositionType`.
- Changes: X4 — `u_mes_syst_statusTransitionRole` rows for the NCR transitions; no new keys.

**Q29 — Hold / Quarantine Management: held units / lots cannot be processed, packed or dispatched without authorised MRB release.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_qualityHold`, `u_mes_qual_qualityHoldHeldObject`, `onHold` on WIP unit, lot and container, `u_mes_matl_storageLocation.isQuarantine`.
- Changes: release reason code and e-signature on `u_mes_qual_qualityHold` (as Q2); X1 — interlock rule type Hold Check at pack-out and dispatch.

**Q30 — Rework Quality Verification: mandated post-rework re-inspection and authorised release, linked to original serial and reason.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_reworkOrder` (`reinspectionResult`, `reinspectedById`, `reinspectedAt`, `returnStepNo`, status Awaiting Reinspection).
- Changes: add to `u_mes_qual_reworkOrder`: `reasonCodeId`/`reasonCodeName`, `releasedById`/`releasedBy`, `releasedAt` (Datetime).

**Q31 — Supplier Quality Integration: check IQC / incoming lot status before issue to line; block rejected or held lots; supplier lot in genealogy.**
- Coverage: **Partly covered.**
- Existing: `u_mes_matl_goodsReceiptLine.inspectionStatus`, `u_mes_matl_goodsReceiptLineInspectionResult`, `u_mes_plan_lot` (`qualityStatus`, `onHold`, `supplierLotNo`), `u_mes_matl_stockStatus.isUsable`.
- Changes: `checksMaterialReleased` on `u_mes_plan_operationExecution`; X1 — interlock rule type Lot Release Check at material issue and kitting.

**Q32 — Audit Trail & Data Integrity: quality records non-editable / controlled-edit with before / after audit trail and retention.**
- Coverage: **New collection.**
- Existing: `u_mes_syst_auditTrail` (`changeAction`, `changedAt`, `changedById`, `reasonText`, `previousHash`, `entryHash`), `u_mes_syst_auditTrailChange` (`oldValue`, `newValue`), `u_mes_syst_documentType.retentionYears`.
- Changes: X12 — new `u_mes_syst_recordPolicy` (syst) per collection: `editPolicy`, `lockOnStatusDefinitionId`, `requiresReasonForEdit`, `requiresSignatureForEdit`, `retentionYears`, `deleteAllowed`.

**Q33 — Predictive Quality & AI: AI/ML defect prediction, RCA suggestion or vision-AI inspection with model-version traceability per unit.**
- Coverage: **New collection.**
- Changes: X10 — new `u_mes_syst_analyticsModel` and `u_mes_syst_modelPrediction` (syst); add to `u_mes_qual_inspectionResult`: `analyticsModelId`/`analyticsModelName`, `modelVersion`, `modelClass`, `modelConfidence`.

**Q34 — Layered Process Audit Management: plan, execute, capture findings, escalate, close, with adherence tracking and escalation on missed audits.**
- Coverage: **New collection.**
- Existing: `u_mes_qual_audit` (`layer`, `plannedDate`, `checkSheetId`, `scorePct`, `nextAuditDueAt`), `u_mes_qual_auditFinding`, `u_mes_qual_checkSheet`.
- Changes: new `u_mes_qual_auditSchedule` (qual) for the LPA plan; add to `u_mes_qual_audit`: `auditScheduleId`/`auditScheduleName`, `dueDate` (Date), `isMissed`, `escalationLevel`; X2 — escalation rule for missed audits and overdue findings.

**Q124 — LED Illumination per Key Position: colour, intensity and uniformity per key with OK/NOK against variant limits.**
- Coverage: **Not applicable to the caliper.**
- Generic impact: covered by X8 — `u_mes_qual_characteristicPosition` (per-position limits) and `positionNo` on `u_mes_qual_inspectionResult`. No product-specific collection.

**Q125 — Symbol Presence & Line-Cut / Overfill Vision: vision results per key with image reference linked to serial.**
- Coverage: **New collection.** Caliper equivalent: laser-mark presence and grade, dust-boot seating and anodise appearance at final vision.
- Existing: `u_mes_trac_serialNumber` (`markGrade`, `markVerifiedAt`), `u_mes_syst_controlledDocument` (image files), `u_mes_qual_inspectionResult`.
- Changes: X8 — `u_mes_qual_characteristicPosition`; add `positionNo`, `positionName`, `imageControlledDocumentId`/`imageControlledDocumentName` to `u_mes_qual_inspectionResult`; `documentType` value Inspection Image in `u_mes_syst_documentType`.

**Q126 — Flush & Gap Measurement (3D scanner): per-position height and gap values with automatic limit check.**
- Coverage: **New collection.** Caliper equivalent: piston protrusion and dust-boot seating height per piston.
- Changes: X8 — `u_mes_qual_characteristicPosition` (per-position nominal and limits) and `positionNo` on `u_mes_qual_inspectionResult`.

**Q127 — Force-vs-Displacement & Torque-vs-Angle Curves: full curve per key with envelope evaluation.**
- Coverage: **New collection.** Caliper equivalent: piston press-in force–displacement at OP060 and bleed-screw torque–angle at OP070.
- Existing: `u_mes_perf_torqueResult` (final torque and angle, `curveControlledDocumentId` file only).
- Changes: X8 — new `u_mes_qual_curveEnvelope`, `u_mes_qual_curveEnvelopeWindow`, `u_mes_qual_measurementCurve`, `u_mes_qual_measurementCurvePoint` (qual); add `curveEnvelopeId`/`curveEnvelopeName`, `measurementCurveId`/`measurementCurveName`, `envelopeResult` to `u_mes_perf_torqueResult`; add `measurementCurveId`/`measurementCurveName` to `u_mes_perf_leakTestResult` (pressure-decay curve).

**Q128 — Haptic Test: sound / vibration / click signatures per key against a golden-sample envelope.**
- Coverage: **Not applicable to the caliper.**
- Generic impact: covered by X8 (`curveType` values Sound Spectrum and Vibration Acceleration in `u_mes_qual_curveEnvelope`).

### 4.4 Performance And OEE (Q35–Q47)

**Q35 — OEE Computation Engine: OEE auto-computed from A, P, Q by line, shift and variant.**
- Coverage: **Covered.**
- Existing: `u_mes_perf_oeeRecord` (availability, performance, quality, OEE, TEEP, `itemId`, `calculationVersion`), `u_mes_perf_oeeRecordLoss`, `u_mes_perf_equipmentState`, `u_mes_perf_productionCount`.
- Changes: none. Variant-level OEE uses `itemId` (each variant has its own item in the caliper model).

**Q36 — Downtime Capture & Classification: downtime start / end from equipment signals with reason assignment.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_equipmentState` (`plcStateCode`, `source`), `u_mes_perf_downtimeEvent` (`startedAt`, `endedAt`, `reasonCodeId`, `classifiedById`, `faultCode`).
- Changes: add to `u_mes_perf_downtimeEvent`: `captureSource` (enumeration Equipment Signal, Operator Entry, Andon), `equipmentStateId`/`equipmentStateName`.

**Q37 — Downtime Capture & Classification: enforce planned / unplanned class and auto-build Pareto by line and shift.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_downtimeEvent.isPlanned`, `u_mes_perf_reasonCode.isPlanned`, `u_mes_perf_lossCategory`.
- Changes: new `u_mes_perf_lossSummary` (perf, Reports) holding the Pareto per line, shift, day and reason; Level 4 sharing with maintenance through `maintenanceWorkOrderCount` in that summary.

**Q38 — Speed, Cycle Time & Minor Stoppages: actual cycle time against takt by station and variant in real time.**
- Coverage: **Partly covered.**
- Existing: `u_mes_plan_operationExecution` (`cycleTimeSec`, `standardCycleTimeSec`), `u_mes_mast_line.taktTimeSec`, `u_mes_mast_lineIdealRate`.
- Changes: add to `u_mes_plan_operationExecution`: `taktTimeSec`, `taktBreached`, `productVariantId`/`productVariantName`; trend in new `u_mes_perf_workCenterPerformance` (perf, Reports).

**Q39 — Speed, Cycle Time & Minor Stoppages: minor stoppages under 15 min auto-logged and categorised.**
- Coverage: **Covered.**
- Existing: `u_mes_perf_downtimeEvent.isMicroStop`, `u_mes_perf_equipmentState`, `u_mes_perf_reasonCode`, `u_mes_syst_systemConfiguration` (threshold minutes).
- Changes: none (threshold stored as configuration key `perf.microStopThresholdMinutes`).

**Q40 — Bottleneck Identification: current bottleneck station from live throughput or WIP.**
- Coverage: **New collection.**
- Existing: `u_mes_mast_line.bottleneckWorkCenterId` (static design value only).
- Changes: new `u_mes_perf_workCenterPerformance` (perf, Reports) with `throughputPerHour`, `wipQuantity`, `blockedMinutes`, `starvedMinutes`, `isConstraint`.

**Q41 — Production vs Plan Tracking: plan loaded; actual vs plan in real time by hour, shift and line.**
- Coverage: **Covered.**
- Existing: `u_mes_plan_productionSchedule`, `u_mes_plan_productionScheduleSlot`, `u_mes_perf_productionCount` (`hourStartAt`, `targetQuantity`, `goodQuantity`, `cumulativeTarget`, `cumulativeGood`, `gapReason`).
- Changes: none.

**Q42 — Production vs Plan Tracking: alerts / escalation when output falls behind plan beyond thresholds.**
- Coverage: **New collection.**
- Changes: X3 — new `u_mes_syst_alertRule` (metric Output Gap, scope line / shift); X2 — `u_mes_syst_escalationRule` for SLA and owner tracking; `alertRuleId` on `u_mes_syst_notification`.

**Q43 — Automated Alerts & Escalation: rule-based alerts for OEE drop, downtime spike or quality dip.**
- Coverage: **New collection.**
- Changes: X3 — `u_mes_syst_alertRule` with metrics OEE, Downtime Minutes, Reject Rate; Level 4 tuning uses `falseAlertCount` on the rule.

**Q44 — Loss Drill-Down & Analysis: loss records linked to station, variant, root cause and corrective-action history.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_downtimeEvent` (`workCenterId`, `reasonCodeId`, `actionText`, `maintenanceWorkOrderId`), `u_mes_perf_oeeRecordLoss`, `u_mes_qual_capa`.
- Changes: add to `u_mes_perf_downtimeEvent`: `productVariantId`/`productVariantName`, `capaId`/`capaName`; quality losses through `u_mes_qual_defectRecord` (new); summary in `u_mes_perf_lossSummary` (new).

**Q45 — Benchmarking: auto-rank best / worst shifts or lines with reusable comparison views.**
- Coverage: **New collection.**
- Existing: `u_mes_perf_oeeRecord`.
- Changes: new `u_mes_syst_savedView` (syst) for saved filters; rank values held in `u_mes_perf_lossSummary` and `u_mes_perf_workCenterPerformance` (`rankInLine`).

**Q46 — Predictive OEE & AI: forecast OEE or loss patterns.**
- Coverage: **New collection.**
- Changes: X10 — `u_mes_syst_analyticsModel` (modelType OEE Forecast) and `u_mes_syst_modelPrediction` (predictionType Forecast, `predictedValue`, `horizonMinutes`, `actualValue`).

**Q47 — Predictive OEE & AI: recommend or auto-adjust actions with tracked closure.**
- Coverage: **New collection.**
- Changes: X10 — `u_mes_syst_modelPrediction` (`recommendedAction`, `actionStatus`, `actionTakenById`, `actionTakenAt`, `approvedById`).

### 4.5 Maintenance (Q48–Q56, Q104, Q105)

**Q48 — PM Scheduling & Compliance: PM schedules for line assets linked to equipment and due criteria; Level 3 overdue PM holds equipment release.**
- Coverage: **Covered.**
- Existing: `u_mes_maint_maintenancePlan` (`intervalType`, `intervalValue`, `counterSource`, `lastDoneAt`, `nextDueAt`, `toleranceDays`, `blockEquipmentWhenOverdue`), `u_mes_maint_maintenancePlanTask`, `u_mes_maint_maintenancePlanRequiredSkill`, `u_mes_maint_maintenancePlanRequiredSparePart`.
- Changes: none. The block itself is recorded through X1 (rule type Equipment Readiness).

**Q49 — PM Scheduling & Compliance: PM completion and compliance with WO, equipment, user, shift and audit trail; checklist completion before closure.**
- Coverage: **New collection.**
- Existing: `u_mes_maint_maintenanceWorkOrder`, `u_mes_maint_maintenanceWorkOrderLabour`, `u_mes_maint_maintenancePlanTask` (the plan's task list, not the executed result).
- Changes: new `u_mes_maint_maintenanceWorkOrderTask` (maint) — executed checklist per work order with `result`, `measuredValue`, `completedById`, `completedAt`; add `shiftId`/`shiftName` to `u_mes_maint_maintenanceWorkOrder`.

**Q50 — CM & Breakdown Logging: each breakdown captured with equipment, start, end, cause and action.**
- Coverage: **Covered.**
- Existing: `u_mes_maint_maintenanceWorkOrder` (`workOrderType`, `equipmentId`, `downtimeEventId`, `reportedAt`, `startedAt`, `completedAt`, `failureMode`, `rootCause`, `actionTaken`, `reasonCodeId`).
- Changes: none.

**Q51 — CM & Breakdown Logging: RCA coding and non-bypassable closure approval.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_maint_maintenanceWorkOrder`: `rootCauseCodeId`/`rootCauseCodeName` (reference to `u_mes_perf_reasonCode` with reasonType Root Cause, X5), `closureApprovedById`/`closureApprovedBy`, `closureApprovedAt` (Datetime); X4 — Completed → Closed transition restricted by role.

**Q52 — Spare Parts & Consumption Tracking: spare-part issue, return and consumption against work order and equipment in real time.**
- Coverage: **New collection.**
- Existing: `u_mes_maint_sparePart` (`stockQuantity`, `minimumQuantity`, `lastIssuedAt`), `u_mes_maint_maintenanceWorkOrderUsedSparePart` (consumption summary only).
- Changes: new `u_mes_maint_sparePartTransaction` (maint) with `transactionType` (enumeration Issue, Return, Receipt, Adjustment, Scrap), `maintenanceWorkOrderId`, `equipmentId`, `scanVerified`.

**Q53 — Reliability Metrics: MTBF and MTTR auto-calculated and trended by equipment, line and shift.**
- Coverage: **New collection.**
- Changes: new `u_mes_maint_reliabilitySummary` (maint, Reports).

**Q54 — Autonomous Scheduling & Work Orders (Adv): auto-prioritise and schedule maintenance from alerts, criticality, due risk and resources.**
- Coverage: **New collection.**
- Changes: add to `u_mes_maint_maintenanceWorkOrder`: `priorityScore`, `schedulingSource` (enumeration Manual, Rule, Model), `slaResponseDueAt` (Datetime), `slaRepairDueAt` (Datetime); X10 — `u_mes_syst_modelPrediction` (predictionType Maintenance Priority).

**Q55 — Breakdown Response: operators raise breakdown calls from the station with equipment, line and severity auto-tagged.**
- Coverage: **Partly covered.**
- Existing: `u_mes_plan_andonEvent` (`workCenterId`, `lineId`, `andonTypeId`, `raisedAt`, `downtimeEventId`), `u_mes_plan_andonType`.
- Changes: add to `u_mes_plan_andonEvent`: `equipmentId`/`equipmentName`, `severity` (enumeration Low, Medium, High, Critical), `maintenanceWorkOrderId`/`maintenanceWorkOrderName`; add `andonEventId`/`andonEventName` to `u_mes_maint_maintenanceWorkOrder`.

**Q56 — Breakdown Response: auto-dispatch to maintenance and track response and repair time against SLA.**
- Coverage: **New collection.**
- Existing: `u_mes_plan_andonType.targetResponseSec`, `u_mes_plan_andonEvent` (`responseSec`, `resolutionSec`), `u_mes_plan_andonEventEscalation`.
- Changes: add `targetRepairSec`, `escalationRuleId`/`escalationRuleName` to `u_mes_plan_andonType`; add `escalationRuleId`/`escalationRuleName` to `u_mes_plan_andonEvent`; X2 — `u_mes_syst_escalationRule` and `u_mes_syst_escalationRuleLevel`.

**Q104 — Equipment Lifecycle Management (Adv): lifecycle history across commissioning, maintenance, cost, performance and degradation; Level 3 rule-based health score.**
- Coverage: **New collection.**
- Existing: `u_mes_mast_equipment` (`commissionedAt`, `lifetimeCycles`, `lifetimeRunHours`, `criticality`), `u_mes_maint_maintenanceWorkOrder.totalCostInr`.
- Changes: new `u_mes_maint_equipmentLifecycleEvent` (maint); add to `u_mes_mast_equipment`: `healthScore`, `healthScoreAt` (Datetime), `acquisitionCostInr`, `plannedReplacementDate` (Date).

**Q105 — Equipment Lifecycle Management (Adv): replacement / refurbishment decisions from integrated cost and performance data.**
- Coverage: **New collection.**
- Changes: `u_mes_maint_equipmentLifecycleEvent` (eventType Replacement Recommendation, `maintenanceWorkOrderId`), X10 — `u_mes_syst_modelPrediction` (predictionType Remaining Useful Life).

### 4.6 Process Management (Q57–Q70, Q121–Q123)

**Q57 — Recipe & Program Management: programs stored, version-controlled and linked to variant / WO before execution.**
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_recipe` (`version`, `programNo`, `checksum`, effectivity, approval, status In Preparation / Released / Obsolete), `u_mes_prod_recipeParameter`, `u_mes_prod_recipeStage`, `u_mes_plan_operationExecution.recipeId`.
- Changes: new relationship `u_mes_prod_recipeProductVariant` (prod, counted under Q3); `recipeType` values Press-Fit, Dispensing, Vision, Laser Marking added (this also resolves the Schema Observation that `recipeType` lacked press and vision values).

**Q58 — Recipe & Program Management: only the approved version is loaded; unapproved or obsolete versions blocked; Level 4 checksum validation.**
- Coverage: **New collection.**
- Changes: X9 — new `u_mes_plan_recipeDownload` (plan); new `u_mes_prod_recipeControlledDocument` (prod) for the released program file and its checksum.

**Q59 — Process Parameter Control & Locking: critical parameter limits maintained and linked to variant / station / recipe.**
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_recipeParameter` (`setPoint`, `lowerLimit`, `upperLimit`, `isCritical`, `downloadToController`, `processTagId`), `u_mes_prod_billOfProcessStepProcessParameter`, `u_mes_perf_processTag` limits.
- Changes: variant link through `u_mes_prod_recipeProductVariant` (Q3); no new keys on the parameter collections.

**Q60 — Setup Verification: verify set-up values, tooling ID and fixture / locator ID before start; block wrong set-up.**
- Coverage: **New collection.**
- Existing: `u_mes_plan_changeover`, `u_mes_plan_changeoverInstalledTool`, `u_mes_plan_changeoverStep`, `u_mes_prod_billOfProcessStepTool`, `u_mes_prod_billOfProcessStepEquipment`.
- Changes: new `u_mes_plan_setupVerification` and `u_mes_plan_setupVerificationItem` (plan); add `checksSetupVerified` to `u_mes_plan_operationExecution`.

**Q61 — Process Change Control: recipe / parameter changes through approval workflow with request, approver and audit trail.**
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_engineeringChange`, `u_mes_prod_engineeringChangeAffectedObject` (can point to a recipe), `u_mes_prod_engineeringChangeApproval`, `u_mes_prod_recipe` (`engineeringChangeId`, `approvedById`, `approvedAt`).
- Changes: add to `u_mes_prod_recipe`: `previousVersionRecipeId`/`previousVersionRecipeName`, `changeReasonText`; X4 — recipe status transitions by role.

**Q62 — Process Change Control: effective-revision release; block changed parameters before approval becomes active.**
- Coverage: **Partly covered.**
- Changes: add `releasedAt` (Datetime) to `u_mes_prod_recipe` (effectivity already in `effectiveFrom`, `effectiveTo`); enforcement evidence in `u_mes_plan_recipeDownload` (Q58).

**Q63 — Golden Recipe Identification: identify the best-performing parameter set from yield, quality and throughput history.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_prod_recipe`: `isGoldenRecipe`, `goldenDesignatedAt` (Datetime), `goldenDesignatedById`/`goldenDesignatedBy`; the ranking itself is a report over `u_mes_plan_operationExecution`, `u_mes_qual_inspectionResult` and `u_mes_perf_oeeRecord` grouped by `recipeId` and `recipeVersion` (X9).

**Q64 — Golden Recipe Identification: golden recipe suggested or auto-selected by variant / machine.**
- Coverage: **Partly covered.**
- Changes: `isGoldenRecipe` (Q63) together with `u_mes_prod_recipeProductVariant` (Q3).

**Q65 — Digital Twin & Simulation (Adv): what-if simulation before recipe changes.**
- Coverage: **New collection.**
- Changes: X11 — new `u_mes_syst_simulationStudy` (syst) with `studyType` Process.

**Q66 — Digital Twin & Simulation (Adv): simulation recommendations pushed back for controlled rollout and pre / post comparison.**
- Coverage: **New collection.**
- Changes: X11 — `u_mes_syst_simulationStudy` (`recommendedRecipeId`, `rolloutProductionOrderId`, `predictedValue`, `actualValue`, `comparisonResult`).

**Q67 — Autonomous Optimisation (Adv): parameters optimised within safe limits.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_prod_recipe`: `origin` (enumeration Engineering, Optimisation Model, Simulation Study), `analyticsModelId`/`analyticsModelName`; safe limits already in `u_mes_prod_recipeParameter.lowerLimit` / `upperLimit`.

**Q68 — Alarm Management: alarms captured with code, time, WO, station and shift.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_alarm` (`equipmentId`, `alarmCode`, `alarmText`, `severity`, `raisedAt`, `clearedAt`, `productionOrderId`, `downtimeEventId`).
- Changes: add to `u_mes_perf_alarm`: `alarmDefinitionId`/`alarmDefinitionName`, `lineId`/`lineName`, `workCenterId`/`workCenterName`, `shiftId`/`shiftName`, `productionDate` (Date), `wipUnitId`/`wipUnitName`.

**Q69 — Alarm Management: escalate critical alarms and block restart until response or authorisation is complete.**
- Coverage: **New collection.**
- Changes: new `u_mes_perf_alarmDefinition` (perf) with `blocksRestart` and `escalationRuleId`; add to `u_mes_perf_alarm`: `blocksRestart`, `restartAuthorizedById`/`restartAuthorizedBy`, `restartAuthorizedAt` (Datetime), `closureReasonCodeId`/`closureReasonCodeName`, `escalationLevel`.

**Q70 — Real-Time Monitoring: alerts or actions triggered from monitored deviations.**
- Coverage: **New collection.**
- Changes: X3 — `u_mes_syst_alertRule` with `processTagId` and `actionType` (Notify, Hold, Stop Equipment, Create Work Order, Create Nonconformance).

**Q121 — SMT Line Parameter & Result Capture (SPI / AOI / ICT).**
- Coverage: **Not applicable to the caliper** (marked "No Applicable" in the workbook; the caliper has no PCB).
- Generic impact: results fit `u_mes_qual_inspectionResult` with `positionNo` (X8); no SMT-specific collection is proposed.

**Q122 — Symbol Marking Parameter Control: marking parameters locked as approved recipes per variant with deviation block.**
- Coverage: **Partly covered.** Applicable to the caliper laser marking at OP090 (marked "No Applicable" in the audited switch plant, but relevant here).
- Existing: `u_mes_prod_recipe`, `u_mes_prod_recipeParameter` (laser power, speed, frequency, focus), `u_mes_trac_serialNumber.markGrade`.
- Changes: `recipeType` value Laser Marking; add to `u_mes_trac_serialNumber`: `markingRecipeId`/`markingRecipeName`, `markingRecipeVersion`; verification through `u_mes_plan_recipeDownload` (Q58).

**Q123 — Snap-Fit / Housing Assembly Force Curve: full force curve per unit with envelope check.**
- Coverage: **New collection.** Caliper equivalent: piston press-in and guide-pin bush press-fit force–displacement.
- Changes: X8 — `u_mes_qual_curveEnvelope`, `u_mes_qual_curveEnvelopeWindow`, `u_mes_qual_measurementCurve`, `u_mes_qual_measurementCurvePoint` (qual).

### 4.7 Material And Inventory Management (Q71–Q79)

**Q71 — Material Lot Linkage & Traceability: block pack-out, transfer or WO closure when genealogy is incomplete.**
- Coverage: **New collection.**
- Changes: add `genealogyComplete`, `missingComponentCount` to `u_mes_trac_asBuiltRecord`; add `genealogyComplete` to `u_mes_plan_productionOrder`; X1 — interlock rule type Genealogy Completeness and its events in `u_mes_plan_interlockEvent` (Level 4 role-recorded overrides).

**Q72 — Shelf-Life Tracking: expiry checked before issue or consumption; Level 4 FEFO.**
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_item.shelfLifeDays`, `u_mes_plan_lot.expiryAt`, `u_mes_matl_inventoryBalance.expiryAt`, `u_mes_plan_lot.attributesCureDate`.
- Changes: add `fefoRequired` to `u_mes_prod_item`; X1 — interlock rule type Expiry Check.

**Q73 — MSL / Floor-Life Timers: timers per lot / reel; block when exposure limits are exceeded.**
- Coverage: **New collection.** Caliper equivalent: grease pot life after opening, EPDM seal open-bag time.
- Changes: new `u_mes_matl_exposureTimer` (matl); add to `u_mes_prod_item`: `exposureControlled`, `openLifeMinutes`; X5 — reasonType Exposure Reset.

**Q74 — BOM & Kitting Verification: verify part code, revision and quantity against the active variant BOM before kitting.**
- Coverage: **Partly covered.**
- Existing: `u_mes_matl_kit`, `u_mes_matl_kitLine` (`itemId`, `lotId`, `requiredQuantity`, `pickedQuantity`, `shortQuantity`), `u_mes_prod_billOfMaterialComponent`, `u_mes_prod_billOfMaterialComponentProductVariant`.
- Changes: add to `u_mes_matl_kitLine`: `itemRevision`, `scannedItemRevision`, `scannedCode`, `isMandatory`, `verifiedAt` (Datetime), `verificationResult` (enumeration Match, Wrong Item, Wrong Revision, Wrong Quantity, Not Scanned).

**Q75 — BOM & Kitting Verification: confirm kit completeness and block dispatch / start when mandatory items are missing.**
- Coverage: **Partly covered.**
- Existing: `u_mes_matl_kit.isComplete`, status Short.
- Changes: `isMandatory` on `u_mes_matl_kitLine` (Q74); X1 — interlock rule type Kit Completeness.

**Q76 — Material Shortage Alerting: low-material alerts from consumption and WO demand before the line starves.**
- Coverage: **New collection.**
- Changes: X3 — `u_mes_syst_alertRule` (metric Line-side Stock Cover); new `u_mes_matl_materialDemandForecast` (matl, Reports) for projected shortage time.

**Q77 — Material Shortage Alerting: replenishment auto-generated by e-Kanban from point-of-use consumption and min-max.**
- Coverage: **Partly covered.**
- Existing: `u_mes_matl_materialRequest` (`requestType`, `triggerSource`, `fromLocationId`, `toLocationId`).
- Changes: new `u_mes_matl_replenishmentRule` (matl); add `replenishmentRuleId`/`replenishmentRuleName` to `u_mes_matl_materialRequest`. (The rule collection is counted here because the request side already exists.)

**Q78 — Predictive Demand & Supplier JIT (Adv): short-term component demand forecast from schedule, consumption and changeovers.**
- Coverage: **New collection.**
- Changes: `u_mes_matl_materialDemandForecast` (matl, Reports); X10 — `u_mes_syst_modelPrediction` when a model produces the forecast.

**Q79 — Digital Twin Inventory (Adv): simulate inventory scenarios from live stock, WIP and schedule.**
- Coverage: **New collection.**
- Changes: X11 — `u_mes_syst_simulationStudy` with `studyType` Inventory.

### 4.8 Personnel And Labor (Q80–Q88)

**Q80 — Operator Authentication & Authorization: badge / biometric login at each station linked to serial, WO, station and shift.**
- Coverage: **New collection.**
- Existing: `u_mes_mast_user` (`badgeNo`, `lastLoginAt`, `isLocked`), `u_mes_plan_operationExecution.operatorUserId`.
- Changes: X7 — new `u_mes_plan_operatorSession` (plan); `operatorSessionId`/`operatorSessionName` on `u_mes_plan_operationExecution`.

**Q81 — Operator Authentication & Authorization: authorise by skill / role matrix and block untrained or unauthorised operators.**
- Coverage: **Partly covered.**
- Existing: `u_mes_mast_skill`, `u_mes_mast_skillCertification` (`level`, `validTo`, `revokedAt`), `u_mes_mast_workCenterRequiresSkill`, `u_mes_prod_operationRequiredSkill`, `u_mes_prod_billOfProcessStepRequiredSkill`, `u_mes_plan_operationExecution.checksSkillVerified`.
- Changes: `skillVerified` on `u_mes_plan_operatorSession` (new, counted under Q80); X1 — interlock rule type Skill Check.

**Q82 — Training Linkage & Compliance: training and certification linked to operation / station; block when mandatory training is missing.**
- Coverage: **Partly covered.**
- Existing: `u_mes_mast_skill.trainingControlledDocumentId`, `u_mes_mast_skillCertification` (`trainingHours`, `evidenceControlledDocumentId`).
- Changes: blocking evidence needs `u_mes_plan_operatorSession` and `u_mes_plan_interlockEvent` (both new); add `trainedDocumentRevision` to `u_mes_mast_skillCertification`.

**Q83 — Training Linkage & Compliance: auto-revoke execution rights on certification expiry or process revision.**
- Coverage: **Partly covered.**
- Existing: `u_mes_mast_skillCertification` (status Valid, Expiring Soon, Expired, Revoked; `revokedAt`, `revokedReason`, `nextReviewAt`).
- Changes: add to `u_mes_mast_skillCertification`: `requalificationRequired`, `revocationSource` (enumeration Expiry, Document Revision, Manual, Assessment Failure).

**Q84 — Shift & Labor Management: shift assignment and station allocation through MES with live manpower visibility and change log.**
- Coverage: **Partly covered.**
- Existing: `u_mes_mast_shiftRoster`, `u_mes_mast_shiftRosterAssignment` (`userId`, `workCenterId`, `roleInCrew`, `attendance`, `replacedUserId`).
- Changes: add to `u_mes_mast_shiftRosterAssignment`: `assignedFromAt` (Datetime), `assignedToAt` (Datetime); live manpower from `u_mes_plan_operatorSession` (new).

**Q85 — Shift & Labor Management: labour time per task / station captured from transactions; traceable by operator, variant, shift and WO.**
- Coverage: **Partly covered.**
- Existing: `u_mes_plan_labourBooking` (`userId`, `productionOrderId`, `operationId`, `workCenterId`, `clockOnAt`, `clockOffAt`, `durationMinutes`, `source`).
- Changes: add to `u_mes_plan_labourBooking`: `operationExecutionId`/`operationExecutionName`, `productVariantId`/`productVariantName`, `operatorSessionId`/`operatorSessionName`.

**Q86 — Labor Efficiency Analytics: efficiency by operator, station and variant in real time and trend.**
- Coverage: **New collection.**
- Changes: new `u_mes_perf_operatorPerformance` (perf, Reports).

**Q87 — Workforce Optimization (Adv): recommend or auto-assign operators by skill, workload and priority.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_mast_shiftRosterAssignment`: `assignmentSource` (enumeration Manual, Rule, Model), `suggestionScore`; X10 — `u_mes_syst_modelPrediction` (predictionType Assignment Recommendation).

**Q88 — Fatigue Detection & Performance Prediction (Adv): predict fatigue / skill risk and alert or tighten controls.**
- Coverage: **New collection.**
- Changes: `errorCount`, `interlockCount` in `u_mes_perf_operatorPerformance` (new); X10 — `u_mes_syst_modelPrediction` (predictionType Operator Risk).

### 4.9 Document Management (Q89–Q95)

**Q89 — Work Instruction Display: station-specific current WI by variant / WO / station.**
- Coverage: **Partly covered.**
- Changes: `u_mes_prod_workInstructionWorkCenter` and `u_mes_prod_workInstructionProductVariant` (prod, counted under Q3).

**Q90 — Work Instruction Acknowledgement: enforce acknowledgement before cycle start with traceability to operator / variant / station / shift.**
- Coverage: **New collection.**
- Changes: X6 — `u_mes_plan_documentAcknowledgement` (plan; counted under Q4 and Q90); `checksDocumentAcknowledged` on `u_mes_plan_operationExecution`.

**Q91 — Version Control & Access Management: only the latest approved WI is released; obsolete versions blocked at the station.**
- Coverage: **Partly covered.**
- Existing: `u_mes_prod_workInstruction` (status In Preparation / Released / Obsolete, `effectiveFrom`, `effectiveTo`), `u_mes_syst_controlledDocument` (status In Preparation / Released / Obsolete).
- Changes: station binding via `u_mes_prod_workInstructionWorkCenter`; X1 — interlock rule type Work Instruction Release Check.

**Q92 — Change Notification: re-acknowledgement of a revised WI before the next operation.**
- Coverage: **New collection.**
- Changes: `reacknowledgeOnRevision` on `u_mes_prod_workInstruction`; `acknowledgementType` Revision Re-acknowledgement in `u_mes_plan_documentAcknowledgement`.

**Q93 — AI Document Management (Adv): WI drafts auto-generated from process definitions, sequence or BOM and routed for approval.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_prod_workInstruction`: `generationSource` (enumeration Manual, Generated From Bill Of Process, Generated By Model), `sourceBillOfProcessId`/`sourceBillOfProcessName`.

**Q94 — AR Visual Instructions (Adv): AR overlays driven by step / product / station.**
- Coverage: **Partly covered.**
- Changes: add to `u_mes_prod_workInstructionStep`: `arContentControlledDocumentId`/`arContentControlledDocumentName`, `arAnchorRef`; `documentType` value AR Content.

**Q95 — AR Visual Instructions (Adv): AR confirmations captured back per serial / WO / station.**
- Coverage: **Partly covered.**
- Changes: add `arSessionRef` to `u_mes_plan_stepCompletion`; `deviceSource` value AR Headset; `method` value AR Confirmation in `u_mes_plan_documentAcknowledgement`.

### 4.10 Resource And Equipment Management (Q96–Q103, Q106–Q108, Q129)

**Q96 — Environmental Monitoring: lux, ESD, temperature, humidity captured in real time and linked to area / line / shift / time.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_processTag` (`equipmentId`, `tagClass`, limits), `u_mes_perf_processReading` (time-series), `u_mes_syst_iotDevice`.
- Changes: add to `u_mes_perf_processTag`: `areaId`/`areaName`, `lineId`/`lineName`, `workCenterId`/`workCenterName` (environment sensors are not on an equipment); add to `u_mes_perf_processReading`: `areaId`/`areaName`, `shiftId`/`shiftName`, `productionDate` (Date); `tagClass` value Environment.

**Q97 — Environmental Monitoring: threshold alerts and block of the protected process when limits are breached.**
- Coverage: **New collection.**
- Changes: X3 — `u_mes_syst_alertRule` (`actionType` Block Process); X1 — interlock rule type Environment Check; `checksEnvironmentOk` on `u_mes_plan_operationExecution`.

**Q98 — Equipment Status Tracking: running / idle / down / maintenance status in real time linked to equipment, station and WO.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_equipmentState` (`stateCode`, `subStateCode`, `workCenterId`, `productionOrderId`), `u_mes_mast_equipment` (`currentState`, `currentStateSince`).
- Changes: add to `u_mes_mast_equipment`: `isProductionReady`, `readinessReasonText`.

**Q99 — Equipment Status Tracking: block dispatch or start on equipment that is down, in maintenance or not ready.**
- Coverage: **Partly covered.**
- Changes: `isProductionReady` on `u_mes_mast_equipment` (Q98); add `checksEquipmentReady` to `u_mes_plan_operationExecution`; X1 — interlock rule type Equipment Readiness.

**Q100 — Tool Life Monitoring: tool / consumable life captured against tool, part, WO and station.**
- Coverage: **Partly covered.**
- Existing: `u_mes_maint_tool` (`lifeLimit`, `lifeUsed`, `lifeRemaining`, `warningThresholdPct`), `u_mes_maint_toolLifeRecord` (`toolId`, `equipmentId`, `productionOrderId`, `cyclesThisEvent`), `u_mes_plan_operationExecutionTool`.
- Changes: add to `u_mes_maint_toolLifeRecord`: `workCenterId`/`workCenterName`, `itemId`/`itemName`, `operationExecutionId`/`operationExecutionName`.

**Q101 — Tool Life Monitoring: alert and block at life limit until changed and verified.**
- Coverage: **Partly covered.**
- Existing: `u_mes_maint_tool` status Life Expired, `u_mes_plan_operationExecution.checksToolLifeOk`.
- Changes: add `blockAtLifeLimit` to `u_mes_maint_tool`; X1 — interlock rule type Tool Life.

**Q102 — Calibration Tracking: calibration status, due date and history by unique gauge ID.**
- Coverage: **Partly covered.**
- Existing: `u_mes_qual_gauge` (`lastCalibratedAt`, `nextCalibrationDueAt`, `blockedForUse`), `u_mes_qual_gaugeCalibration`, `u_mes_qual_gaugeCalibrationReading`.
- Changes: add `equipmentId`/`equipmentName` to `u_mes_qual_gauge` so that measuring systems built into equipment (leak-tester transducer, nutrunner transducer) are calibrated as gauges and linked to the machine.

**Q103 — Calibration Enforcement: block equipment use, lot release or quality confirmation when calibration is overdue, failed or missing.**
- Coverage: **Partly covered.**
- Existing: `u_mes_plan_operationExecution.checksGaugeCalibrationOk`, `u_mes_qual_gauge.blockedForUse`.
- Changes: X1 — interlock rule type Calibration Check; no new keys beyond Q102.

**Q106 — Fixture & Asset Management: fixture IDs, certification status and usage history linked to variant, WO and station.**
- Coverage: **Partly covered.**
- Existing: `u_mes_maint_tool` (toolClass Fixture, `equipmentId`, `mountedPosition`), `u_mes_maint_toolItem`, `u_mes_plan_operationExecutionTool`, `u_mes_perf_leakTestResult.fixtureToolId`.
- Changes: add to `u_mes_maint_tool`: `lastCertifiedAt` (Datetime), `certificationDueDate` (Date), `certificateControlledDocumentId`/`certificateControlledDocumentName`; set-up check through `u_mes_plan_setupVerificationItem` (check type Fixture).

**Q107 — Digital Twin & Auto Calibration (Adv): twin evaluates equipment behaviour or settings before release.**
- Coverage: **New collection.**
- Changes: X11 — `u_mes_syst_simulationStudy` (`studyType` Equipment).

**Q108 — Digital Twin & Auto Calibration (Adv): auto-calibration via closed-loop feedback, propagated across similar equipment.**
- Coverage: **New collection.**
- Changes: `calibrationType` value Automatic Closed Loop in `u_mes_qual_gaugeCalibration`; propagation recorded in `u_mes_syst_simulationStudy` (`studyType` Calibration Baseline) with the target equipment listed in its result text.

**Q129 — Vision Recipe & Golden Image Version Control: vision recipes and golden images version-controlled per variant; AI model traceable per unit.**
- Coverage: **Partly covered.**
- Changes: `recipeType` value Vision; `u_mes_prod_recipeControlledDocument` (golden images, counted under Q58); `u_mes_prod_recipeProductVariant` (counted under Q3); model keys on `u_mes_qual_inspectionResult` (counted under Q33).

### 4.11 Analytics And Intelligence (Q109–Q112)

**Q109 — Enterprise Dashboards & Benchmarking (Adv): KPIs aggregated with plant / line / WO / shift drill-down; cross-plant benchmark.**
- Coverage: **Partly covered.**
- Changes: `u_mes_syst_savedView` (counted under Q45); report collections `u_mes_perf_lossSummary`, `u_mes_perf_workCenterPerformance` all carry `siteId` / `lineId` / `shiftId` / `productionDate` for drill-down.

**Q110 — Cloud Integration & Data Architecture (Adv): governed APIs / events to cloud with asset, serial and site context.**
- Coverage: **Partly covered.**
- Existing: `u_mes_syst_integrationConnector`, `u_mes_syst_integrationConnectorFunction`, `u_mes_syst_erpMessage`, `u_mes_syst_businessEvent`.
- Changes: `targetSystem` value Cloud Data Platform and `direction` value Publish in the connector and message enumerations; no new keys.

**Q111 — Predictive & Prescriptive Analytics (Adv): models invoked by product / asset with predictions recorded.**
- Coverage: **New collection.**
- Changes: X10 — `u_mes_syst_analyticsModel`, `u_mes_syst_modelPrediction`.

**Q112 — Anomaly Detection & Root Cause AI (Adv): anomalies from multiple signals with context.**
- Coverage: **New collection.**
- Changes: X10 — `u_mes_syst_modelPrediction` (predictionType Anomaly, `relatedCollectionName` / `relatedEntityId`, `workCenterId`, `productVariantId`, `shiftId`); X3 — `u_mes_syst_alertRule` (metric Model Anomaly Score).

### 4.12 General (Q113–Q118)

**Q113 — ISA-95 Architecture Alignment.**
- Coverage: **Not schema.** The model already follows the ISA-95 equipment hierarchy (`u_mes_mast_enterprise` → `u_mes_mast_site` → `u_mes_mast_area` → `u_mes_mast_line` → `u_mes_mast_workCenter` → `u_mes_mast_equipment`) and separates ERP exchange (`u_mes_syst_erpMessage`) from control-layer data (`u_mes_syst_iotDevice`, `u_mes_perf_processTag`). Recommendation: add a hand-written level-3/level-4 data-flow diagram to `02_architecture/data_flows` (already planned in the original brief).

**Q114 — User Access & Role Control: individual login with role-based access; Level 4 rights linked to the skill matrix.**
- Coverage: **Partly covered.**
- Existing: `u_mes_mast_user`, `u_mes_mast_userRole`, `u_mes_mast_role`, `u_mes_mast_rolePermission`, `u_mes_mast_permission`.
- Changes: new `u_mes_mast_roleRequiredSkill` (mast); X4 — `u_mes_syst_statusTransitionRole` (counted under Q1).

**Q115 — Record Integrity & Audit Trail: records protected from edit / delete; authorised changes logged with user, time, old and new value.**
- Coverage: **New collection.**
- Existing: `u_mes_syst_auditTrail`, `u_mes_syst_auditTrailChange`, `u_mes_syst_electronicSignature`.
- Changes: X12 — `u_mes_syst_recordPolicy` (counted under Q32; listed here because Q115 is the general-records version of Q32).

**Q116 — Real-Time Shop-Floor Dashboards: count vs plan, OEE, downtime and quality status by line and shift.**
- Coverage: **Partly covered.**
- Existing: `u_mes_perf_productionCount`, `u_mes_perf_oeeRecord`, `u_mes_perf_downtimeEvent`, `u_mes_qual_inspectionResult`.
- Changes: `u_mes_perf_workCenterPerformance` (counted under Q40) for the station view.

**Q117 — ERP / PLC / Quality System Integration with failure handling.**
- Coverage: **Covered.**
- Existing: `u_mes_syst_integrationConnector` (`healthStatus`, retry policy), `u_mes_syst_erpMessage` (`attempts`, `maxAttempts`, `nextRetryAt`, `errorCode`, status Dead Letter), `u_mes_syst_iotDevice`.
- Changes: none.

**Q118 — Data Backup & Recovery: regular backups, periodic restore test, documented recovery time.**
- Coverage: **New collection** (optional; mainly infrastructure).
- Changes: optional `u_mes_syst_backupRun` (syst) as IATF evidence of backup and restore tests; retention per collection in `u_mes_syst_recordPolicy` (X12).

### 4.13 Additional items found only in `Options_Switch`

`Options_Switch` has 13 rows; 11 match Q119–Q129. Two rows have no question in the `MES Requirement` sheet:

**Options_Switch row 8 — Shade / contrast with ambient-light interlock.** Caliper equivalent: anodise colour (L\*a\*b\*) check at final inspection. Covered by `u_mes_qual_characteristic` / `u_mes_qual_inspectionResult` and by the environment tags of Q96 (ambient lux) with an interlock rule (X1). No further change.

**Options_Switch row 13 — Storage matrix, FIFO and blocking of expired or damaged lots at issue.** Covered for FIFO / FEFO and expiry by Q72. The storage matrix (which items may be stored where) is new: optional relationship `u_mes_matl_storageLocationAllowedItem` (matl).

## 5. Specification of the proposed new collections

Every collection below follows the current standard: flat documents (no arrays, no embedded documents), `_id` as a 16-digit numeric string, `recordNo` as the business key, `siteId`/`siteName` on every document, ID+Name reference pairs (`<entity>Id` + `<entity>Name`), user actions as `<action>ById` + `<action>By`, `status` only on entity collections with values held in `u_mes_syst_statusDefinition`, `schemaVersion` Int32, and the six audit keys only on transaction, report and telemetry data (the same rule the existing model applies to `u_mes_perf_processReading` and to the report collections). Every date key is stored as local plant time with a `+0000` suffix and is tagged Date or Datetime (DATA-004). In total the 44 collections carry 1,115 keys.

### 1300 `u_mes_mast_roleRequiredSkill`

| Item | Value |
|---|---|
| Module | mast — Master Data Management |
| Kind / Type / UI label | Relationship / Master / Role Required Skills |
| Purpose | Lists the skills (and minimum level) a user must hold before the rights of a role become effective at execution. |
| Why a separate collection | Many-to-many between role and skill; flat model forbids arrays on `u_mes_mast_role`. |
| Business key (`recordNo`) | parent recordNo + -RS<nnn>, e.g. ROLE-LEAK-OPR-RS001 |
| Indexes | unique `recordNo`; unique (`roleId`, `requiredSkillId`) |
| Questions | Q9, Q81, Q114 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1300 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -RS<nnn>, e.g. ROLE-LEAK-OPR-RS001 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `roleId` | String |  | Yes | `u_mes_mast_role._id` | Parent role (ID) |
| 6 | `roleName` | String |  | Yes | display value of `u_mes_mast_role` | Parent role (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `requiredSkillId` | String |  | Yes | `u_mes_mast_skill._id` | Skill required (ID) |
| 9 | `requiredSkillName` | String |  | Yes | display value of `u_mes_mast_skill` | Skill required (display value) |
| 10 | `minimumLevel` | Int32 |  | Yes | 1 to 4 | Minimum skill level required for the role |
| 11 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1301 `u_mes_prod_recipeProductVariant`

| Item | Value |
|---|---|
| Module | prod — Product Definition |
| Kind / Type / UI label | Relationship / Master / Recipe Variants |
| Purpose | Variants for which a recipe / machine program version is released. |
| Why a separate collection | Many-to-many between recipe and product variant. |
| Business key (`recordNo`) | parent recordNo + -V<nnn>, e.g. RCP-OP080-LT-07-V001 |
| Indexes | unique `recordNo`; (`productVariantId`, `recipeId`) |
| Questions | Q3, Q57, Q59, Q64, Q129 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1301 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -V<nnn>, e.g. RCP-OP080-LT-07-V001 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `recipeId` | String |  | Yes | `u_mes_prod_recipe._id` | Parent recipe (ID) |
| 6 | `recipeName` | String |  | Yes | display value of `u_mes_prod_recipe` | Parent recipe (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `productVariantId` | String |  | Yes | `u_mes_prod_productVariant._id` | Variant the recipe is released for (ID) |
| 9 | `productVariantName` | String |  | Yes | display value of `u_mes_prod_productVariant` | Variant the recipe is released for (display value) |
| 10 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1302 `u_mes_prod_recipeControlledDocument`

| Item | Value |
|---|---|
| Module | prod — Product Definition |
| Kind / Type / UI label | Relationship / Master / Recipe Reference Files |
| Purpose | Program files, golden reference images and reference curves that belong to a recipe version. |
| Why a separate collection | A recipe can have several controlled files; files are already managed in `u_mes_syst_controlledDocument`. |
| Business key (`recordNo`) | parent recordNo + -D<nnn> |
| Indexes | unique `recordNo`; (`recipeId`) |
| Questions | Q58, Q129 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1302 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -D<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `recipeId` | String |  | Yes | `u_mes_prod_recipe._id` | Parent recipe (ID) |
| 6 | `recipeName` | String |  | Yes | display value of `u_mes_prod_recipe` | Parent recipe (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `controlledDocumentId` | String |  | Yes | `u_mes_syst_controlledDocument._id` | Controlled file (ID) |
| 9 | `controlledDocumentName` | String |  | Yes | display value of `u_mes_syst_controlledDocument` | Controlled file (display value) |
| 10 | `fileRole` | String |  | Yes | enumeration: Program File, Golden Image, Reference Curve, Parameter Export | What the file is used for |
| 11 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1303 `u_mes_prod_workInstructionWorkCenter`

| Item | Value |
|---|---|
| Module | prod — Product Definition |
| Kind / Type / UI label | Relationship / Master / Work Instruction Stations |
| Purpose | Stations at which a work instruction is displayed. |
| Why a separate collection | Many-to-many between work instruction and work centre. |
| Business key (`recordNo`) | parent recordNo + -W<nnn> |
| Indexes | unique `recordNo`; (`workCenterId`, `workInstructionId`) |
| Questions | Q3, Q89, Q91 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1303 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -W<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `workInstructionId` | String |  | Yes | `u_mes_prod_workInstruction._id` | Parent work instruction (ID) |
| 6 | `workInstructionName` | String |  | Yes | display value of `u_mes_prod_workInstruction` | Parent work instruction (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 9 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 10 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1304 `u_mes_prod_workInstructionProductVariant`

| Item | Value |
|---|---|
| Module | prod — Product Definition |
| Kind / Type / UI label | Relationship / Master / Work Instruction Variants |
| Purpose | Variants to which a whole work instruction applies (step-level variants stay in `u_mes_prod_workInstructionStepProductVariant`). |
| Why a separate collection | Many-to-many between work instruction and product variant. |
| Business key (`recordNo`) | parent recordNo + -V<nnn> |
| Indexes | unique `recordNo`; (`productVariantId`, `workInstructionId`) |
| Questions | Q3, Q89 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1304 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -V<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `workInstructionId` | String |  | Yes | `u_mes_prod_workInstruction._id` | Parent work instruction (ID) |
| 6 | `workInstructionName` | String |  | Yes | display value of `u_mes_prod_workInstruction` | Parent work instruction (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `productVariantId` | String |  | Yes | `u_mes_prod_productVariant._id` | Variant (ID) |
| 9 | `productVariantName` | String |  | Yes | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 10 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1305 `u_mes_plan_operatorSession`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Entity / Transaction / Operator Sessions |
| Purpose | One login-to-logout session of an operator at a station, with the authentication method and the checks done at login. |
| Why a separate collection | Unbounded event data; referenced by operation executions and labour bookings. |
| Business key (`recordNo`) | OSN-<yyyymmdd>-<nnnnn>, e.g. OSN-20260916-00042 |
| Status values | Active, Closed, Rejected |
| Indexes | unique `recordNo`; (`workCenterId`, `loginAt`); (`userId`, `loginAt`) |
| Questions | Q5, Q80, Q81, Q82, Q84, Q85 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1305 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: OSN-<yyyymmdd>-<nnnnn>, e.g. OSN-20260916-00042 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `userId` | String |  | Yes | `u_mes_mast_user._id` | Operator (ID) |
| 6 | `userName` | String |  | Yes | display value of `u_mes_mast_user` | Operator (display value) |
| 7 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 8 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 9 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Equipment at the station (ID) |
| 10 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Equipment at the station (display value) |
| 11 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 12 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 13 | `productionDate` | Date | Date | Yes |  | Production date the session belongs to |
| 14 | `productionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order active at login (ID) |
| 15 | `productionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order active at login (display value) |
| 16 | `authenticationMethod` | String |  | Yes | enumeration: Badge, Biometric, Badge And PIN, Password | How the operator was authenticated |
| 17 | `loginAt` | Date | Datetime | Yes |  | Login time |
| 18 | `logoutAt` | Date | Datetime | No |  | Logout time; null while the session is active |
| 19 | `logoutReason` | String |  | No | enumeration: Operator Logout, Shift End, Timeout, Supervisor Logout, Skill Revoked | Why the session ended |
| 20 | `skillVerified` | Boolean |  | Yes |  | Required skills were valid at login |
| 21 | `trainingVerified` | Boolean |  | Yes |  | Mandatory training for the station's current documents was valid at login |
| 22 | `interlockEventId` | String |  | No | `u_mes_plan_interlockEvent._id` | Interlock raised when the login was rejected (ID) |
| 23 | `interlockEventName` | String |  | No | display value of `u_mes_plan_interlockEvent` | Interlock raised when the login was rejected (display value) |
| 24 | `clientWorkstation` | String |  | No |  | Terminal or HMI name |
| 25 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Closed, Rejected) | Record status |
| 26 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 27 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 28 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 29 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 30 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 31 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 32 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1306 `u_mes_plan_documentAcknowledgement`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Entity / Transaction / Document Acknowledgements |
| Purpose | Operator confirmation that a specific revision of a work instruction, recipe or controlled document was read at a station. |
| Why a separate collection | Unbounded event data per operator, document revision and station. |
| Business key (`recordNo`) | ACK-<yyyymmdd>-<nnnnn> |
| Status values | Acknowledged, Superseded |
| Indexes | unique `recordNo`; (`relatedEntityId`, `documentVersion`, `userId`); (`workCenterId`, `acknowledgedAt`) |
| Questions | Q4, Q90, Q92, Q95 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1306 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ACK-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `relatedCollectionName` | String |  | Yes | enumeration: u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_syst_controlledDocument | Collection of the acknowledged document |
| 6 | `relatedEntityId` | String |  | Yes | `_id` in the named collection | Acknowledged document (ID) |
| 7 | `relatedEntityName` | String |  | Yes | display value in the named collection | Acknowledged document (display value) |
| 8 | `documentVersion` | String |  | Yes |  | Version / revision acknowledged |
| 9 | `userId` | String |  | Yes | `u_mes_mast_user._id` | Operator (ID) |
| 10 | `userName` | String |  | Yes | display value of `u_mes_mast_user` | Operator (display value) |
| 11 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 12 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 13 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant in production (ID) |
| 14 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant in production (display value) |
| 15 | `productionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order in production (ID) |
| 16 | `productionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order in production (display value) |
| 17 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 18 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 19 | `operatorSessionId` | String |  | No | `u_mes_plan_operatorSession._id` | Session in which the acknowledgement was given (ID) |
| 20 | `operatorSessionName` | String |  | No | display value of `u_mes_plan_operatorSession` | Session in which the acknowledgement was given (display value) |
| 21 | `acknowledgementType` | String |  | Yes | enumeration: First Read, Revision Re-acknowledgement, Shift Start, Periodic Refresh | Reason for the acknowledgement |
| 22 | `method` | String |  | Yes | enumeration: Touch Confirmation, Badge Scan, AR Confirmation, Electronic Signature | How it was given |
| 23 | `electronicSignatureId` | String |  | No | `u_mes_syst_electronicSignature._id` | Signature when the method is Electronic Signature (ID) |
| 24 | `electronicSignatureName` | String |  | No | display value of `u_mes_syst_electronicSignature` | Signature when the method is Electronic Signature (display value) |
| 25 | `acknowledgedAt` | Date | Datetime | Yes |  | Time of acknowledgement |
| 26 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Acknowledged, Superseded) | Record status |
| 27 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 28 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 29 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 30 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 31 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 32 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 33 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1307 `u_mes_plan_interlockEvent`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Entity / Transaction / Interlock Events |
| Purpose | Every time an interlock rule blocks a transaction, is overridden or is cleared: what was checked, expected and found, and who authorised the override. |
| Why a separate collection | Unbounded event data; written by many modules (execution, material issue, packing, dispatch) and queried by unit, order and station. |
| Business key (`recordNo`) | ILK-<yyyymmdd>-<nnnnn> |
| Status values | Blocked, Overridden, Cleared, Cancelled |
| Indexes | unique `recordNo`; (`wipUnitId`, `raisedAt`); (`interlockRuleId`, `raisedAt`); (`workCenterId`, `status`) |
| Questions | X1 list (section 3) |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1307 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ILK-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `interlockRuleId` | String |  | Yes | `u_mes_syst_interlockRule._id` | Rule that fired (ID) |
| 6 | `interlockRuleName` | String |  | Yes | display value of `u_mes_syst_interlockRule` | Rule that fired (display value) |
| 7 | `ruleType` | String |  | Yes | copied from the rule | Rule type at the time of the event |
| 8 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station (ID) |
| 9 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station (display value) |
| 10 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Equipment (ID) |
| 11 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Equipment (display value) |
| 12 | `productionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order (ID) |
| 13 | `productionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order (display value) |
| 14 | `wipUnitId` | String |  | No | `u_mes_plan_wipUnit._id` | Unit (ID) |
| 15 | `wipUnitName` | String |  | No | display value of `u_mes_plan_wipUnit` | Unit (display value) |
| 16 | `lotId` | String |  | No | `u_mes_plan_lot._id` | Lot (ID) |
| 17 | `lotName` | String |  | No | display value of `u_mes_plan_lot` | Lot (display value) |
| 18 | `operationExecutionId` | String |  | No | `u_mes_plan_operationExecution._id` | Operation execution being attempted (ID) |
| 19 | `operationExecutionName` | String |  | No | display value of `u_mes_plan_operationExecution` | Operation execution being attempted (display value) |
| 20 | `relatedCollectionName` | String |  | No | any `u_mes_*` collection | Collection of the blocked object when it is not a unit, lot or order |
| 21 | `relatedEntityId` | String |  | No | `_id` in the named collection | Blocked object (ID) |
| 22 | `relatedEntityName` | String |  | No | display value in the named collection | Blocked object (display value) |
| 23 | `scannedValue` | String |  | No |  | Value found (scan, version, reading) |
| 24 | `expectedValue` | String |  | No |  | Value expected |
| 25 | `messageText` | String |  | Yes |  | Message shown to the operator |
| 26 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 27 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 28 | `productionDate` | Date | Date | Yes |  | Production date |
| 29 | `operatorUserId` | String |  | No | `u_mes_mast_user._id` | Operator who triggered the check (ID) |
| 30 | `operatorUserName` | String |  | No | display value of `u_mes_mast_user` | Operator who triggered the check (display value) |
| 31 | `raisedAt` | Date | Datetime | Yes |  | Time the interlock fired |
| 32 | `overrideReasonCodeId` | String |  | No | `u_mes_perf_reasonCode._id` | Override reason (reasonType Interlock Override) (ID) |
| 33 | `overrideReasonCodeName` | String |  | No | display value of `u_mes_perf_reasonCode` | Override reason (reasonType Interlock Override) (display value) |
| 34 | `overrideComment` | String |  | No |  | Free-text comment on the override |
| 35 | `overrideById` | String |  | No | `u_mes_mast_user._id` | Authoriser of the override (user ID) |
| 36 | `overrideBy` | String |  | No | `u_mes_mast_user.fullName` | Authoriser of the override (user name) |
| 37 | `overrideAt` | Date | Datetime | No |  | Time of the override |
| 38 | `electronicSignatureId` | String |  | No | `u_mes_syst_electronicSignature._id` | Signature of the authoriser (ID) |
| 39 | `electronicSignatureName` | String |  | No | display value of `u_mes_syst_electronicSignature` | Signature of the authoriser (display value) |
| 40 | `clearedAt` | Date | Datetime | No |  | Time the condition was cleared without override |
| 41 | `notificationId` | String |  | No | `u_mes_syst_notification._id` | Notification raised for escalation (ID) |
| 42 | `notificationName` | String |  | No | display value of `u_mes_syst_notification` | Notification raised for escalation (display value) |
| 43 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Blocked, Overridden, Cleared, Cancelled) | Record status |
| 44 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 45 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 46 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 47 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 48 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 49 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 50 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1308 `u_mes_plan_recipeDownload`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Entity / Transaction / Recipe Downloads |
| Purpose | Each download or selection of a program / recipe on a machine with the checksum verification result. |
| Why a separate collection | Unbounded event data per machine and order. |
| Business key (`recordNo`) | RDL-<yyyymmdd>-<nnnnn> |
| Status values | Requested, Verified, Rejected |
| Indexes | unique `recordNo`; (`equipmentId`, `downloadedAt`); (`productionOrderId`) |
| Questions | Q21, Q58, Q62, Q122 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1308 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: RDL-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `recipeId` | String |  | Yes | `u_mes_prod_recipe._id` | Recipe (ID) |
| 6 | `recipeName` | String |  | Yes | display value of `u_mes_prod_recipe` | Recipe (display value) |
| 7 | `recipeVersion` | String |  | Yes |  | Version downloaded |
| 8 | `equipmentId` | String |  | Yes | `u_mes_mast_equipment._id` | Target machine (ID) |
| 9 | `equipmentName` | String |  | Yes | display value of `u_mes_mast_equipment` | Target machine (display value) |
| 10 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 11 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 12 | `productionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order (ID) |
| 13 | `productionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order (display value) |
| 14 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant (ID) |
| 15 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 16 | `trigger` | String |  | Yes | enumeration: Order Start, Changeover, Operator Request, Revision Release, Controller Reconnect | What caused the download |
| 17 | `checksumExpected` | String |  | Yes |  | Checksum of the released version |
| 18 | `checksumReported` | String |  | No |  | Checksum reported back by the controller |
| 19 | `verificationResult` | String |  | Yes | enumeration: Match, Mismatch, No Response, Version Not Released | Verification outcome |
| 20 | `downloadedAt` | Date | Datetime | Yes |  | Download time |
| 21 | `verifiedAt` | Date | Datetime | No |  | Verification time |
| 22 | `requestedById` | String |  | Yes | `u_mes_mast_user._id` | User or system user that requested the download (user ID) |
| 23 | `requestedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User or system user that requested the download (user name) |
| 24 | `interlockEventId` | String |  | No | `u_mes_plan_interlockEvent._id` | Interlock raised on mismatch (ID) |
| 25 | `interlockEventName` | String |  | No | display value of `u_mes_plan_interlockEvent` | Interlock raised on mismatch (display value) |
| 26 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Requested, Verified, Rejected) | Record status |
| 27 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 28 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 29 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 30 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 31 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 32 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 33 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1309 `u_mes_plan_setupVerification`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Entity / Transaction / Setup Verifications |
| Purpose | Pre-start verification of the set-up of a station or machine against the order, variant and bill of process. |
| Why a separate collection | One record per verification; its items are in a child collection. |
| Business key (`recordNo`) | SUV-<yyyymmdd>-<nnnnn> |
| Status values | In Progress, Passed, Failed, Overridden |
| Indexes | unique `recordNo`; (`workCenterId`, `verifiedAt`); (`productionOrderId`) |
| Questions | Q60, Q106, Q120 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1309 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: SUV-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 6 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 7 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Machine (ID) |
| 8 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Machine (display value) |
| 9 | `productionOrderId` | String |  | Yes | `u_mes_plan_productionOrder._id` | Order (ID) |
| 10 | `productionOrderName` | String |  | Yes | display value of `u_mes_plan_productionOrder` | Order (display value) |
| 11 | `productVariantId` | String |  | Yes | `u_mes_prod_productVariant._id` | Variant (ID) |
| 12 | `productVariantName` | String |  | Yes | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 13 | `changeoverId` | String |  | No | `u_mes_plan_changeover._id` | Changeover that preceded the verification (ID) |
| 14 | `changeoverName` | String |  | No | display value of `u_mes_plan_changeover` | Changeover that preceded the verification (display value) |
| 15 | `billOfProcessId` | String |  | Yes | `u_mes_prod_billOfProcess._id` | Bill of process used for the expected values (ID) |
| 16 | `billOfProcessName` | String |  | Yes | display value of `u_mes_prod_billOfProcess` | Bill of process used for the expected values (display value) |
| 17 | `trigger` | String |  | Yes | enumeration: Order Start, Changeover, Shift Start, After Maintenance | Reason for the verification |
| 18 | `itemCount` | Int32 |  | Yes |  | Number of checks |
| 19 | `failedCount` | Int32 |  | Yes |  | Number of failed checks |
| 20 | `verifiedById` | String |  | Yes | `u_mes_mast_user._id` | User who performed the verification (user ID) |
| 21 | `verifiedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who performed the verification (user name) |
| 22 | `verifiedAt` | Date | Datetime | Yes |  | Completion time |
| 23 | `interlockEventId` | String |  | No | `u_mes_plan_interlockEvent._id` | Interlock raised on failure (ID) |
| 24 | `interlockEventName` | String |  | No | display value of `u_mes_plan_interlockEvent` | Interlock raised on failure (display value) |
| 25 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (In Progress, Passed, Failed, Overridden) | Record status |
| 26 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 27 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 28 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 29 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 30 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 31 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 32 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1310 `u_mes_plan_setupVerificationItem`

| Item | Value |
|---|---|
| Module | plan — Planning and Execution |
| Kind / Type / UI label | Child / Transaction / Setup Verification Items |
| Purpose | Each expected-versus-actual check of a set-up verification. |
| Why a separate collection | Replaces an embedded array of checks (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -I<nnn> |
| Indexes | unique `recordNo`; (`setupVerificationId`, `itemNo`) |
| Questions | Q60, Q106, Q120 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1310 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -I<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `setupVerificationId` | String |  | Yes | `u_mes_plan_setupVerification._id` | Parent set-up verification (ID) |
| 6 | `setupVerificationName` | String |  | Yes | display value of `u_mes_plan_setupVerification` | Parent set-up verification (display value) |
| 7 | `itemNo` | Int32 |  | Yes |  | Check number within the verification |
| 8 | `checkType` | String |  | Yes | enumeration: Variant, Fixture, Tool, Program, Parameter, Component, Gauge | What is checked |
| 9 | `expectedRelatedCollectionName` | String |  | No | any `u_mes_*` collection | Collection of the expected object |
| 10 | `expectedEntityId` | String |  | No | `_id` in the named collection | Expected object (ID) |
| 11 | `expectedEntityName` | String |  | No | display value in the named collection | Expected object (display value) |
| 12 | `scannedCode` | String |  | No |  | Code scanned at the station |
| 13 | `expectedValue` | Decimal128 |  | No |  | Expected numeric value for parameter checks |
| 14 | `actualValue` | Decimal128 |  | No |  | Actual numeric value |
| 15 | `unitOfMeasureId` | String |  | No | `u_mes_mast_unitOfMeasure._id` | Unit of the values (ID) |
| 16 | `unitOfMeasureName` | String |  | No | display value of `u_mes_mast_unitOfMeasure` | Unit of the values (display value) |
| 17 | `passed` | Boolean |  | Yes |  | Check result |
| 18 | `checkedAt` | Date | Datetime | Yes |  | Time of the check |
| 19 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 20 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 21 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 22 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 23 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 24 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 25 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1311 `u_mes_matl_exposureTimer`

| Item | Value |
|---|---|
| Module | matl — Material Management |
| Kind / Type / UI label | Entity / Transaction / Exposure Timers |
| Purpose | Floor-life, pot-life or open-time clock for a lot or container of an exposure-controlled item. |
| Why a separate collection | Each opening of a lot or container starts its own clock; unbounded event data. |
| Business key (`recordNo`) | EXT-<yyyymmdd>-<nnnnn> |
| Status values | Running, Paused, Expired, Reset, Consumed |
| Indexes | unique `recordNo`; (`lotId`, `status`); (`expiresAt`) |
| Questions | Q73 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1311 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: EXT-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Item (ID) |
| 6 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Item (display value) |
| 7 | `lotId` | String |  | Yes | `u_mes_plan_lot._id` | Lot (ID) |
| 8 | `lotName` | String |  | Yes | display value of `u_mes_plan_lot` | Lot (display value) |
| 9 | `containerId` | String |  | No | `u_mes_plan_container._id` | Container opened (ID) |
| 10 | `containerName` | String |  | No | display value of `u_mes_plan_container` | Container opened (display value) |
| 11 | `timerType` | String |  | Yes | enumeration: Floor Life, Pot Life, Open Time, Bake | Timer type |
| 12 | `limitMinutes` | Int32 |  | Yes |  | Allowed exposure in minutes |
| 13 | `startedAt` | Date | Datetime | Yes |  | Clock start (container opened) |
| 14 | `pausedAt` | Date | Datetime | No |  | Last pause (container resealed / dry storage) |
| 15 | `accumulatedMinutes` | Int32 |  | Yes |  | Exposure accumulated so far |
| 16 | `expiresAt` | Date | Datetime | Yes |  | Calculated expiry time while running |
| 17 | `storageLocationId` | String |  | No | `u_mes_matl_storageLocation._id` | Current location (ID) |
| 18 | `storageLocationName` | String |  | No | display value of `u_mes_matl_storageLocation` | Current location (display value) |
| 19 | `resetReasonCodeId` | String |  | No | `u_mes_perf_reasonCode._id` | Reason for reset (reasonType Exposure Reset) (ID) |
| 20 | `resetReasonCodeName` | String |  | No | display value of `u_mes_perf_reasonCode` | Reason for reset (reasonType Exposure Reset) (display value) |
| 21 | `resetById` | String |  | No | `u_mes_mast_user._id` | User who reset the clock (user ID) |
| 22 | `resetBy` | String |  | No | `u_mes_mast_user.fullName` | User who reset the clock (user name) |
| 23 | `resetAt` | Date | Datetime | No |  | Reset time |
| 24 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Running, Paused, Expired, Reset, Consumed) | Record status |
| 25 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 26 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 27 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 28 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 29 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 30 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 31 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1312 `u_mes_matl_replenishmentRule`

| Item | Value |
|---|---|
| Module | matl — Material Management |
| Kind / Type / UI label | Entity / Master / Replenishment Rules |
| Purpose | Min-max or e-Kanban rule for replenishing an item at a line-side location. |
| Why a separate collection | Plant-maintained configuration per item and location (Rule A master). |
| Business key (`recordNo`) | RPL-<item code>-<location code>, e.g. RPL-PST-54-LS-OP060 |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; unique (`itemId`, `toLocationId`) |
| Questions | Q76, Q77 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1312 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: RPL-<item code>-<location code>, e.g. RPL-PST-54-LS-OP060 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Item (ID) |
| 6 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Item (display value) |
| 7 | `toLocationId` | String |  | Yes | `u_mes_matl_storageLocation._id` | Line-side location replenished (ID) |
| 8 | `toLocationName` | String |  | Yes | display value of `u_mes_matl_storageLocation` | Line-side location replenished (display value) |
| 9 | `fromLocationId` | String |  | Yes | `u_mes_matl_storageLocation._id` | Supplying location (supermarket / store) (ID) |
| 10 | `fromLocationName` | String |  | Yes | display value of `u_mes_matl_storageLocation` | Supplying location (supermarket / store) (display value) |
| 11 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Consuming station (ID) |
| 12 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Consuming station (display value) |
| 13 | `triggerType` | String |  | Yes | enumeration: Consumption, Kanban Scan, Min-Max, Order Demand | How replenishment is triggered |
| 14 | `minQuantity` | Decimal128 |  | Yes |  | Minimum quantity |
| 15 | `maxQuantity` | Decimal128 |  | Yes |  | Maximum quantity |
| 16 | `reorderPointQuantity` | Decimal128 |  | Yes |  | Quantity that triggers a request |
| 17 | `kanbanQuantity` | Decimal128 |  | No |  | Quantity per kanban |
| 18 | `kanbanCount` | Int32 |  | No |  | Number of kanbans in the loop |
| 19 | `containerTypeId` | String |  | No | `u_mes_plan_containerType._id` | Container used (ID) |
| 20 | `containerTypeName` | String |  | No | display value of `u_mes_plan_containerType` | Container used (display value) |
| 21 | `unitOfMeasureId` | String |  | Yes | `u_mes_mast_unitOfMeasure._id` | Unit (ID) |
| 22 | `unitOfMeasureName` | String |  | Yes | display value of `u_mes_mast_unitOfMeasure` | Unit (display value) |
| 23 | `leadTimeMinutes` | Int32 |  | Yes |  | Replenishment lead time |
| 24 | `validFrom` | Date | Date | Yes |  | Valid from (date stored at 00:00:00) |
| 25 | `validTo` | Date | Date | No |  | Valid to |
| 26 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 27 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1313 `u_mes_matl_materialDemandForecast`

| Item | Value |
|---|---|
| Module | matl — Material Management |
| Kind / Type / UI label | Entity / Reports / Material Demand Forecast |
| Purpose | Short-term component demand and projected line-side shortage per item, line and time bucket. |
| Why a separate collection | Calculated output, refreshed by a job; kept separate from transactions. |
| Business key (`recordNo`) | MDF-<yyyymmdd>-<line code>-<item code>-<hh> |
| Status values | Calculated, Superseded |
| Indexes | unique `recordNo`; (`lineId`, `bucketStartAt`); (`itemId`, `projectedShortageAt`) |
| Questions | Q76, Q78 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1313 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: MDF-<yyyymmdd>-<line code>-<item code>-<hh> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Component (ID) |
| 6 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Component (display value) |
| 7 | `lineId` | String |  | Yes | `u_mes_mast_line._id` | Line (ID) |
| 8 | `lineName` | String |  | Yes | display value of `u_mes_mast_line` | Line (display value) |
| 9 | `productionDate` | Date | Date | Yes |  | Production date |
| 10 | `bucketStartAt` | Date | Datetime | Yes |  | Bucket start |
| 11 | `bucketEndAt` | Date | Datetime | Yes |  | Bucket end |
| 12 | `scheduledDemand` | Decimal128 |  | Yes |  | Demand from the schedule and BOM |
| 13 | `consumptionRatePerHour` | Decimal128 |  | Yes |  | Actual consumption rate |
| 14 | `onHandQuantity` | Decimal128 |  | Yes |  | Line-side and supermarket stock at calculation |
| 15 | `projectedOnHand` | Decimal128 |  | Yes |  | Projected stock at bucket end |
| 16 | `projectedShortageAt` | Date | Datetime | No |  | Projected time the line starves |
| 17 | `unitOfMeasureId` | String |  | Yes | `u_mes_mast_unitOfMeasure._id` | Unit (ID) |
| 18 | `unitOfMeasureName` | String |  | Yes | display value of `u_mes_mast_unitOfMeasure` | Unit (display value) |
| 19 | `method` | String |  | Yes | enumeration: Schedule, Consumption Rate, Model | Calculation method |
| 20 | `analyticsModelId` | String |  | No | `u_mes_syst_analyticsModel._id` | Model when method is Model (ID) |
| 21 | `analyticsModelName` | String |  | No | display value of `u_mes_syst_analyticsModel` | Model when method is Model (display value) |
| 22 | `calculatedAt` | Date | Datetime | Yes |  | Calculation time |
| 23 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Calculated, Superseded) | Record status |
| 24 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 25 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 26 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 27 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 28 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 29 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 30 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1314 `u_mes_trac_traceInvestigation`

| Item | Value |
|---|---|
| Module | trac — Traceability |
| Kind / Type / UI label | Entity / Transaction / Trace Investigations |
| Purpose | A saved forward or reverse trace run, its starting object and the containment it fed. |
| Why a separate collection | Audit evidence of a trace; its result rows are unbounded and stored in a child collection. |
| Business key (`recordNo`) | TRC-<yyyymmdd>-<nnn> |
| Status values | Running, Completed, Closed |
| Indexes | unique `recordNo`; (`startEntityId`); (`requestedAt`) |
| Questions | Q14, Q15 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1314 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: TRC-<yyyymmdd>-<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `title` | String |  | Yes |  | Short title |
| 6 | `direction` | String |  | Yes | enumeration: Forward, Reverse, Both | Trace direction |
| 7 | `startRelatedCollectionName` | String |  | Yes | enumeration: u_mes_trac_serialNumber, u_mes_plan_lot, u_mes_plan_wipUnit, u_mes_plan_container, u_mes_matl_shipment | Collection of the start object |
| 8 | `startEntityId` | String |  | Yes | `_id` in the named collection | Start object (ID) |
| 9 | `startEntityName` | String |  | Yes | display value in the named collection | Start object (display value) |
| 10 | `depthLimit` | Int32 |  | Yes |  | Maximum genealogy levels followed |
| 11 | `resultCount` | Int32 |  | Yes |  | Rows found |
| 12 | `shippedCount` | Int32 |  | Yes |  | Rows already shipped |
| 13 | `qualityHoldId` | String |  | No | `u_mes_qual_qualityHold._id` | Hold created from the result (ID) |
| 14 | `qualityHoldName` | String |  | No | display value of `u_mes_qual_qualityHold` | Hold created from the result (display value) |
| 15 | `nonconformanceId` | String |  | No | `u_mes_qual_nonconformance._id` | Nonconformance investigated (ID) |
| 16 | `nonconformanceName` | String |  | No | display value of `u_mes_qual_nonconformance` | Nonconformance investigated (display value) |
| 17 | `customerComplaintId` | String |  | No | `u_mes_qual_customerComplaint._id` | Complaint investigated (ID) |
| 18 | `customerComplaintName` | String |  | No | display value of `u_mes_qual_customerComplaint` | Complaint investigated (display value) |
| 19 | `requestedById` | String |  | Yes | `u_mes_mast_user._id` | User who ran the trace (user ID) |
| 20 | `requestedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who ran the trace (user name) |
| 21 | `requestedAt` | Date | Datetime | Yes |  | Run start |
| 22 | `completedAt` | Date | Datetime | No |  | Run end |
| 23 | `exportControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Exported trace report (ID) |
| 24 | `exportControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Exported trace report (display value) |
| 25 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Running, Completed, Closed) | Record status |
| 26 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 27 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 28 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 29 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 30 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 31 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 32 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1315 `u_mes_trac_traceInvestigationResult`

| Item | Value |
|---|---|
| Module | trac — Traceability |
| Kind / Type / UI label | Child / Transaction / Trace Investigation Results |
| Purpose | Each serial, lot or container found by a trace run with its state at the time of the run. |
| Why a separate collection | Unbounded result list; replaces an array (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -R<nnnnn> |
| Indexes | unique `recordNo`; (`traceInvestigationId`); (`relatedEntityId`) |
| Questions | Q14, Q15 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1315 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -R<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `traceInvestigationId` | String |  | Yes | `u_mes_trac_traceInvestigation._id` | Parent trace investigation (ID) |
| 6 | `traceInvestigationName` | String |  | Yes | display value of `u_mes_trac_traceInvestigation` | Parent trace investigation (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `relatedCollectionName` | String |  | Yes | enumeration: u_mes_trac_serialNumber, u_mes_plan_lot, u_mes_plan_wipUnit, u_mes_plan_container, u_mes_matl_shipment | Collection of the found object |
| 9 | `relatedEntityId` | String |  | Yes | `_id` in the named collection | Found object (ID) |
| 10 | `relatedEntityName` | String |  | Yes | display value in the named collection | Found object (display value) |
| 11 | `levelNo` | Int32 |  | Yes |  | Genealogy distance from the start object |
| 12 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Item of the found object (ID) |
| 13 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Item of the found object (display value) |
| 14 | `statusAtRun` | String |  | Yes |  | Status of the object at the time of the run |
| 15 | `storageLocationId` | String |  | No | `u_mes_matl_storageLocation._id` | Location at the time of the run (ID) |
| 16 | `storageLocationName` | String |  | No | display value of `u_mes_matl_storageLocation` | Location at the time of the run (display value) |
| 17 | `shipmentId` | String |  | No | `u_mes_matl_shipment._id` | Shipment if already shipped (ID) |
| 18 | `shipmentName` | String |  | No | display value of `u_mes_matl_shipment` | Shipment if already shipped (display value) |
| 19 | `customerId` | String |  | No | `u_mes_mast_customer._id` | Customer if already shipped (ID) |
| 20 | `customerName` | String |  | No | display value of `u_mes_mast_customer` | Customer if already shipped (display value) |
| 21 | `quantity` | Decimal128 |  | Yes |  | Quantity concerned |
| 22 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 23 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 24 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 25 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 26 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 27 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 28 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1316 `u_mes_qual_characteristicPosition`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Child / Master / Characteristic Positions |
| Purpose | Per-position nominal and limits when a characteristic is measured at several positions (piston 1 / piston 2, coating points, key positions). |
| Why a separate collection | Replaces an array of positions on `u_mes_qual_characteristic` (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -P<nn> |
| Indexes | unique `recordNo`; unique (`characteristicId`, `positionNo`) |
| Questions | Q24, Q124, Q125, Q126, Q127, Q128 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1316 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -P<nn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `characteristicId` | String |  | Yes | `u_mes_qual_characteristic._id` | Parent characteristic (ID) |
| 6 | `characteristicName` | String |  | Yes | display value of `u_mes_qual_characteristic` | Parent characteristic (display value) |
| 7 | `positionNo` | Int32 |  | Yes |  | Position number |
| 8 | `positionName` | String |  | Yes |  | Position name, e.g. Piston 1 inboard |
| 9 | `nominal` | Decimal128 |  | No |  | Nominal at this position |
| 10 | `lowerSpecLimit` | Decimal128 |  | No |  | Lower limit at this position |
| 11 | `upperSpecLimit` | Decimal128 |  | No |  | Upper limit at this position |
| 12 | `unitOfMeasureId` | String |  | No | `u_mes_mast_unitOfMeasure._id` | Unit (ID) |
| 13 | `unitOfMeasureName` | String |  | No | display value of `u_mes_mast_unitOfMeasure` | Unit (display value) |
| 14 | `curveEnvelopeId` | String |  | No | `u_mes_qual_curveEnvelope._id` | Envelope when the position is evaluated as a curve (ID) |
| 15 | `curveEnvelopeName` | String |  | No | display value of `u_mes_qual_curveEnvelope` | Envelope when the position is evaluated as a curve (display value) |
| 16 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1317 `u_mes_qual_curveEnvelope`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Entity / Master / Curve Envelopes |
| Purpose | Approved golden-sample envelope for a force–displacement, torque–angle, pressure–time or signal curve. |
| Why a separate collection | Versioned engineering master referenced by every captured curve. |
| Business key (`recordNo`) | ENV-<characteristic code>-<version>, e.g. ENV-OP060-PISTON-PRESS-02 |
| Status values | In Preparation, Released, Obsolete |
| Indexes | unique `recordNo`; (`characteristicId`, `status`) |
| Questions | Q123, Q127, Q128 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1317 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ENV-<characteristic code>-<version>, e.g. ENV-OP060-PISTON-PRESS-02 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Envelope name |
| 6 | `characteristicId` | String |  | Yes | `u_mes_qual_characteristic._id` | Characteristic evaluated (ID) |
| 7 | `characteristicName` | String |  | Yes | display value of `u_mes_qual_characteristic` | Characteristic evaluated (display value) |
| 8 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Item (ID) |
| 9 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Item (display value) |
| 10 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant, when variant-specific (ID) |
| 11 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant, when variant-specific (display value) |
| 12 | `operationId` | String |  | Yes | `u_mes_prod_operation._id` | Operation (ID) |
| 13 | `operationName` | String |  | Yes | display value of `u_mes_prod_operation` | Operation (display value) |
| 14 | `recipeId` | String |  | No | `u_mes_prod_recipe._id` | Recipe the envelope belongs to (ID) |
| 15 | `recipeName` | String |  | No | display value of `u_mes_prod_recipe` | Recipe the envelope belongs to (display value) |
| 16 | `curveType` | String |  | Yes | enumeration: Force Displacement, Torque Angle, Pressure Time, Sound Spectrum, Vibration Acceleration | Curve type |
| 17 | `xQuantity` | String |  | Yes |  | X-axis quantity, e.g. Displacement |
| 18 | `xUnitOfMeasureId` | String |  | Yes | `u_mes_mast_unitOfMeasure._id` | X-axis unit (ID) |
| 19 | `xUnitOfMeasureName` | String |  | Yes | display value of `u_mes_mast_unitOfMeasure` | X-axis unit (display value) |
| 20 | `yQuantity` | String |  | Yes |  | Y-axis quantity, e.g. Force |
| 21 | `yUnitOfMeasureId` | String |  | Yes | `u_mes_mast_unitOfMeasure._id` | Y-axis unit (ID) |
| 22 | `yUnitOfMeasureName` | String |  | Yes | display value of `u_mes_mast_unitOfMeasure` | Y-axis unit (display value) |
| 23 | `version` | String |  | Yes |  | Envelope version |
| 24 | `goldenSampleSerialNo` | String |  | No |  | Serial of the golden sample used |
| 25 | `referenceControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Reference curve file (ID) |
| 26 | `referenceControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Reference curve file (display value) |
| 27 | `effectiveFrom` | Date | Date | Yes |  | Effective from |
| 28 | `effectiveTo` | Date | Date | No |  | Effective to |
| 29 | `approvedById` | String |  | Yes | `u_mes_mast_user._id` | Approver (user ID) |
| 30 | `approvedBy` | String |  | Yes | `u_mes_mast_user.fullName` | Approver (user name) |
| 31 | `approvedAt` | Date | Datetime | Yes |  | Approval time |
| 32 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (In Preparation, Released, Obsolete) | Record status |
| 33 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1318 `u_mes_qual_curveEnvelopeWindow`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Child / Master / Curve Envelope Windows |
| Purpose | Each evaluation window (box or band) of a curve envelope. |
| Why a separate collection | Replaces an array of windows (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -W<nn> |
| Indexes | unique `recordNo`; (`curveEnvelopeId`, `windowNo`) |
| Questions | Q123, Q127, Q128 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1318 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -W<nn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `curveEnvelopeId` | String |  | Yes | `u_mes_qual_curveEnvelope._id` | Parent curve envelope (ID) |
| 6 | `curveEnvelopeName` | String |  | Yes | display value of `u_mes_qual_curveEnvelope` | Parent curve envelope (display value) |
| 7 | `windowNo` | Int32 |  | Yes |  | Window number |
| 8 | `windowType` | String |  | Yes | enumeration: Box, Upper Band, Lower Band, Peak, Final Value | Window type |
| 9 | `xMin` | Decimal128 |  | Yes |  | Window start on X |
| 10 | `xMax` | Decimal128 |  | Yes |  | Window end on X |
| 11 | `yMin` | Decimal128 |  | No |  | Lower Y limit |
| 12 | `yMax` | Decimal128 |  | No |  | Upper Y limit |
| 13 | `entrySide` | String |  | No | enumeration: Left, Right, Top, Bottom | Side the curve must enter (box windows) |
| 14 | `exitSide` | String |  | No | enumeration: Left, Right, Top, Bottom | Side the curve must leave (box windows) |
| 15 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1319 `u_mes_qual_measurementCurve`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Entity / Transaction / Measurement Curves |
| Purpose | One captured curve per unit, position and test, with the envelope verdict and summary values. |
| Why a separate collection | Unbounded test data; the points themselves go to the time-series collection 1320. |
| Business key (`recordNo`) | CRV-<yyyymmdd>-<nnnnnn> |
| Status values | Recorded, Voided |
| Indexes | unique `recordNo`; (`wipUnitId`, `capturedAt`); (`curveEnvelopeId`, `result`) |
| Questions | Q123, Q127, Q128 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1319 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: CRV-<yyyymmdd>-<nnnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `curveEnvelopeId` | String |  | Yes | `u_mes_qual_curveEnvelope._id` | Envelope used (ID) |
| 6 | `curveEnvelopeName` | String |  | Yes | display value of `u_mes_qual_curveEnvelope` | Envelope used (display value) |
| 7 | `characteristicId` | String |  | Yes | `u_mes_qual_characteristic._id` | Characteristic (ID) |
| 8 | `characteristicName` | String |  | Yes | display value of `u_mes_qual_characteristic` | Characteristic (display value) |
| 9 | `positionNo` | Int32 |  | No |  | Position number (see collection 1316) |
| 10 | `wipUnitId` | String |  | Yes | `u_mes_plan_wipUnit._id` | Unit (ID) |
| 11 | `wipUnitName` | String |  | Yes | display value of `u_mes_plan_wipUnit` | Unit (display value) |
| 12 | `serialNumberId` | String |  | No | `u_mes_trac_serialNumber._id` | Serial when already issued (ID) |
| 13 | `serialNumberName` | String |  | No | display value of `u_mes_trac_serialNumber` | Serial when already issued (display value) |
| 14 | `operationExecutionId` | String |  | Yes | `u_mes_plan_operationExecution._id` | Operation execution (ID) |
| 15 | `operationExecutionName` | String |  | Yes | display value of `u_mes_plan_operationExecution` | Operation execution (display value) |
| 16 | `equipmentId` | String |  | Yes | `u_mes_mast_equipment._id` | Machine (ID) |
| 17 | `equipmentName` | String |  | Yes | display value of `u_mes_mast_equipment` | Machine (display value) |
| 18 | `recipeVersion` | String |  | No |  | Program version |
| 19 | `capturedAt` | Date | Datetime | Yes |  | Capture time |
| 20 | `pointCount` | Int32 |  | Yes |  | Number of points stored |
| 21 | `peakX` | Decimal128 |  | No |  | X at peak |
| 22 | `peakY` | Decimal128 |  | No |  | Peak Y value |
| 23 | `finalX` | Decimal128 |  | No |  | Final X |
| 24 | `finalY` | Decimal128 |  | No |  | Final Y |
| 25 | `result` | String |  | Yes | enumeration: OK, NOK | Envelope verdict |
| 26 | `failedWindowNo` | Int32 |  | No |  | First failed window |
| 27 | `rawControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Raw curve file as delivered by the controller (ID) |
| 28 | `rawControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Raw curve file as delivered by the controller (display value) |
| 29 | `inspectionResultId` | String |  | No | `u_mes_qual_inspectionResult._id` | Inspection result written from this curve (ID) |
| 30 | `inspectionResultName` | String |  | No | display value of `u_mes_qual_inspectionResult` | Inspection result written from this curve (display value) |
| 31 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Recorded, Voided) | Record status |
| 32 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 33 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 34 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 35 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 36 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 37 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 38 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1320 `u_mes_qual_measurementCurvePoint`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Entity / Telemetry / Measurement Curve Points |
| Purpose | Points of a measurement curve. Created as a MongoDB time-series collection: timeField `sampledAt`, metaField `measurementCurveId`, granularity seconds. |
| Why a separate collection | High-volume telemetry (hundreds of points per curve). |
| Business key (`recordNo`) | parent curve recordNo + -<nnnn> |
| Status values | none (time-series telemetry, as `u_mes_perf_processReading`) |
| Indexes | time-series index on (`measurementCurveId`, `sampledAt`) |
| Questions | Q123, Q127, Q128 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1320 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent curve recordNo + -<nnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `measurementCurveId` | String |  | Yes | `u_mes_qual_measurementCurve._id` | Curve (ID) |
| 6 | `measurementCurveName` | String |  | Yes | display value of `u_mes_qual_measurementCurve` | Curve (display value) |
| 7 | `pointNo` | Int32 |  | Yes |  | Point number |
| 8 | `sampledAt` | Date | Datetime | Yes |  | Sample time |
| 9 | `xValue` | Decimal128 |  | Yes |  | X value |
| 10 | `yValue` | Decimal128 |  | Yes |  | Y value |
| 11 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 12 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 13 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 14 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 15 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 16 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 17 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1321 `u_mes_qual_defectRecord`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Entity / Transaction / Defect Records |
| Purpose | One logged defect on one unit (or lot sample) with first-fail station, origin, 4M category and follow-up links. |
| Why a separate collection | Unbounded event data; the existing relationship `u_mes_plan_operationExecutionDefectCode` holds no detail. |
| Business key (`recordNo`) | DEF-<yyyymmdd>-<nnnnn> |
| Status values | Open, Reworked, Scrapped, Accepted, Closed |
| Indexes | unique `recordNo`; (`wipUnitId`); (`defectCodeId`, `detectedAt`); (`detectedAtWorkCenterId`, `productionDate`) |
| Questions | Q18, Q27, Q44 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1321 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: DEF-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `defectCodeId` | String |  | Yes | `u_mes_qual_defectCode._id` | Defect code (ID) |
| 6 | `defectCodeName` | String |  | Yes | display value of `u_mes_qual_defectCode` | Defect code (display value) |
| 7 | `wipUnitId` | String |  | No | `u_mes_plan_wipUnit._id` | Unit (ID) |
| 8 | `wipUnitName` | String |  | No | display value of `u_mes_plan_wipUnit` | Unit (display value) |
| 9 | `serialNumberId` | String |  | No | `u_mes_trac_serialNumber._id` | Serial (ID) |
| 10 | `serialNumberName` | String |  | No | display value of `u_mes_trac_serialNumber` | Serial (display value) |
| 11 | `lotId` | String |  | No | `u_mes_plan_lot._id` | Lot (for lot-controlled items) (ID) |
| 12 | `lotName` | String |  | No | display value of `u_mes_plan_lot` | Lot (for lot-controlled items) (display value) |
| 13 | `itemId` | String |  | Yes | `u_mes_prod_item._id` | Item (ID) |
| 14 | `itemName` | String |  | Yes | display value of `u_mes_prod_item` | Item (display value) |
| 15 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant (ID) |
| 16 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 17 | `productionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order (ID) |
| 18 | `productionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order (display value) |
| 19 | `detectedAtOperationId` | String |  | Yes | `u_mes_prod_operation._id` | Operation where detected (ID) |
| 20 | `detectedAtOperationName` | String |  | Yes | display value of `u_mes_prod_operation` | Operation where detected (display value) |
| 21 | `detectedAtWorkCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station where detected (ID) |
| 22 | `detectedAtWorkCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station where detected (display value) |
| 23 | `originOperationId` | String |  | No | `u_mes_prod_operation._id` | Operation where caused (ID) |
| 24 | `originOperationName` | String |  | No | display value of `u_mes_prod_operation` | Operation where caused (display value) |
| 25 | `isFirstFail` | Boolean |  | Yes |  | First failure of this unit |
| 26 | `positionNo` | Int32 |  | No |  | Position on the part |
| 27 | `defectLocationText` | String |  | No |  | Location description, e.g. Bore B edge |
| 28 | `quantity` | Int32 |  | Yes |  | Quantity defective |
| 29 | `fourMCategory` | String |  | Yes | enumeration: Man, Machine, Material, Method | 4M category |
| 30 | `operatorUserId` | String |  | No | `u_mes_mast_user._id` | Operator at origin (ID) |
| 31 | `operatorUserName` | String |  | No | display value of `u_mes_mast_user` | Operator at origin (display value) |
| 32 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Machine at origin (ID) |
| 33 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Machine at origin (display value) |
| 34 | `componentLotId` | String |  | No | `u_mes_plan_lot._id` | Suspect component lot (ID) |
| 35 | `componentLotName` | String |  | No | display value of `u_mes_plan_lot` | Suspect component lot (display value) |
| 36 | `operationExecutionId` | String |  | No | `u_mes_plan_operationExecution._id` | Operation execution where detected (ID) |
| 37 | `operationExecutionName` | String |  | No | display value of `u_mes_plan_operationExecution` | Operation execution where detected (display value) |
| 38 | `inspectionResultId` | String |  | No | `u_mes_qual_inspectionResult._id` | Inspection result that found it (ID) |
| 39 | `inspectionResultName` | String |  | No | display value of `u_mes_qual_inspectionResult` | Inspection result that found it (display value) |
| 40 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 41 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 42 | `productionDate` | Date | Date | Yes |  | Production date |
| 43 | `detectedAt` | Date | Datetime | Yes |  | Detection time |
| 44 | `detectedById` | String |  | Yes | `u_mes_mast_user._id` | User who logged the defect (user ID) |
| 45 | `detectedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who logged the defect (user name) |
| 46 | `imageControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Defect image (ID) |
| 47 | `imageControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Defect image (display value) |
| 48 | `nonconformanceId` | String |  | No | `u_mes_qual_nonconformance._id` | Nonconformance raised (ID) |
| 49 | `nonconformanceName` | String |  | No | display value of `u_mes_qual_nonconformance` | Nonconformance raised (display value) |
| 50 | `reworkOrderId` | String |  | No | `u_mes_qual_reworkOrder._id` | Rework order (ID) |
| 51 | `reworkOrderName` | String |  | No | display value of `u_mes_qual_reworkOrder` | Rework order (display value) |
| 52 | `scrapRecordId` | String |  | No | `u_mes_qual_scrapRecord._id` | Scrap record (ID) |
| 53 | `scrapRecordName` | String |  | No | display value of `u_mes_qual_scrapRecord` | Scrap record (display value) |
| 54 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Open, Reworked, Scrapped, Accepted, Closed) | Record status |
| 55 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 56 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 57 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 58 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 59 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 60 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 61 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1322 `u_mes_qual_auditSchedule`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Entity / Master / Audit Schedules |
| Purpose | Plan for layered process audits (and other recurring audits): layer, area or line, check sheet, frequency and auditor. |
| Why a separate collection | Plant-maintained plan; executions stay in `u_mes_qual_audit`. |
| Business key (`recordNo`) | LPA-<layer>-<line code>-<nn>, e.g. LPA-L2-LN-CAL-01 |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; (`lineId`, `layer`); (`nextDueDate`) |
| Questions | Q22, Q34 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1322 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: LPA-<layer>-<line code>-<nn>, e.g. LPA-L2-LN-CAL-01 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Schedule name |
| 6 | `auditType` | String |  | Yes | enumeration: Layered Process Audit, Product Audit, Process Audit, 5S Audit | Audit type |
| 7 | `layer` | Int32 |  | No | 1 to 4 | LPA layer |
| 8 | `areaId` | String |  | No | `u_mes_mast_area._id` | Area (ID) |
| 9 | `areaName` | String |  | No | display value of `u_mes_mast_area` | Area (display value) |
| 10 | `lineId` | String |  | No | `u_mes_mast_line._id` | Line (ID) |
| 11 | `lineName` | String |  | No | display value of `u_mes_mast_line` | Line (display value) |
| 12 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station (ID) |
| 13 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station (display value) |
| 14 | `checkSheetId` | String |  | Yes | `u_mes_qual_checkSheet._id` | Question set (ID) |
| 15 | `checkSheetName` | String |  | Yes | display value of `u_mes_qual_checkSheet` | Question set (display value) |
| 16 | `frequencyType` | String |  | Yes | enumeration: Shift, Daily, Weekly, Monthly | Frequency |
| 17 | `frequencyValue` | Int32 |  | Yes |  | Every n periods |
| 18 | `auditorRoleId` | String |  | Yes | `u_mes_mast_role._id` | Role that performs the audit (ID) |
| 19 | `auditorRoleName` | String |  | Yes | display value of `u_mes_mast_role` | Role that performs the audit (display value) |
| 20 | `auditorUserId` | String |  | No | `u_mes_mast_user._id` | Named auditor, when fixed (ID) |
| 21 | `auditorUserName` | String |  | No | display value of `u_mes_mast_user` | Named auditor, when fixed (display value) |
| 22 | `toleranceHours` | Int32 |  | Yes |  | Grace period before the audit counts as missed |
| 23 | `escalationRuleId` | String |  | No | `u_mes_syst_escalationRule._id` | Escalation for missed audits (ID) |
| 24 | `escalationRuleName` | String |  | No | display value of `u_mes_syst_escalationRule` | Escalation for missed audits (display value) |
| 25 | `nextDueDate` | Date | Date | Yes |  | Next due date |
| 26 | `validFrom` | Date | Date | Yes |  | Valid from |
| 27 | `validTo` | Date | Date | No |  | Valid to |
| 28 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 29 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1323 `u_mes_qual_inspectionPlanProductVariant`

| Item | Value |
|---|---|
| Module | qual — Quality Management |
| Kind / Type / UI label | Relationship / Master / Inspection Plan Variants |
| Purpose | Variants to which an inspection plan applies. |
| Why a separate collection | Many-to-many between inspection plan and variant. |
| Business key (`recordNo`) | parent recordNo + -V<nnn> |
| Indexes | unique `recordNo`; (`productVariantId`, `inspectionPlanId`) |
| Questions | Q23 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1323 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -V<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `inspectionPlanId` | String |  | Yes | `u_mes_qual_inspectionPlan._id` | Parent inspection plan (ID) |
| 6 | `inspectionPlanName` | String |  | Yes | display value of `u_mes_qual_inspectionPlan` | Parent inspection plan (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `productVariantId` | String |  | Yes | `u_mes_prod_productVariant._id` | Variant (ID) |
| 9 | `productVariantName` | String |  | Yes | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 10 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1324 `u_mes_perf_alarmDefinition`

| Item | Value |
|---|---|
| Module | perf — Performance Management |
| Kind / Type / UI label | Entity / Master / Alarm Definitions |
| Purpose | Alarm code master per equipment type with class, severity, restart-block and escalation settings. |
| Why a separate collection | Plant-maintained list (Rule A master) referenced by every alarm. |
| Business key (`recordNo`) | ALM-<equipment type code>-<alarm code>, e.g. ALM-LEAKTESTER-E104 |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; unique (`equipmentTypeId`, `alarmCode`) |
| Questions | Q68, Q69 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1324 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ALM-<equipment type code>-<alarm code>, e.g. ALM-LEAKTESTER-E104 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `equipmentTypeId` | String |  | Yes | `u_mes_mast_equipmentType._id` | Equipment type (ID) |
| 6 | `equipmentTypeName` | String |  | Yes | display value of `u_mes_mast_equipmentType` | Equipment type (display value) |
| 7 | `alarmCode` | String |  | Yes |  | Controller alarm code |
| 8 | `alarmText` | String |  | Yes |  | Standard alarm text |
| 9 | `alarmClass` | String |  | Yes | enumeration: Process, Equipment, Safety, Quality, Utility | Alarm class |
| 10 | `severity` | String |  | Yes | enumeration: Low, Medium, High, Critical | Severity |
| 11 | `blocksRestart` | Boolean |  | Yes |  | Restart requires authorisation |
| 12 | `authorizingRoleId` | String |  | No | `u_mes_mast_role._id` | Role that may authorise restart (ID) |
| 13 | `authorizingRoleName` | String |  | No | display value of `u_mes_mast_role` | Role that may authorise restart (display value) |
| 14 | `defaultReasonCodeId` | String |  | No | `u_mes_perf_reasonCode._id` | Default downtime reason (ID) |
| 15 | `defaultReasonCodeName` | String |  | No | display value of `u_mes_perf_reasonCode` | Default downtime reason (display value) |
| 16 | `escalationRuleId` | String |  | No | `u_mes_syst_escalationRule._id` | Escalation rule (ID) |
| 17 | `escalationRuleName` | String |  | No | display value of `u_mes_syst_escalationRule` | Escalation rule (display value) |
| 18 | `createsDowntime` | Boolean |  | Yes |  | Alarm opens a downtime event |
| 19 | `responseInstruction` | String |  | No |  | Response instruction text |
| 20 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 21 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1325 `u_mes_perf_lossSummary`

| Item | Value |
|---|---|
| Module | perf — Performance Management |
| Kind / Type / UI label | Entity / Reports / Loss Summary |
| Purpose | Loss Pareto row per line, shift, production date and reason code (downtime, speed and quality losses). |
| Why a separate collection | Calculated report table refreshed by a job; avoids heavy aggregation on dashboards. |
| Business key (`recordNo`) | LSS-<yyyymmdd>-<line code>-<shift code>-<reason code> |
| Status values | Calculated, Recalculated |
| Indexes | unique `recordNo`; (`lineId`, `productionDate`, `shiftId`); (`reasonCodeId`, `productionDate`) |
| Questions | Q37, Q44, Q45 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1325 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: LSS-<yyyymmdd>-<line code>-<shift code>-<reason code> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `lineId` | String |  | Yes | `u_mes_mast_line._id` | Line (ID) |
| 6 | `lineName` | String |  | Yes | display value of `u_mes_mast_line` | Line (display value) |
| 7 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station, when the loss is station-specific (ID) |
| 8 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station, when the loss is station-specific (display value) |
| 9 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 10 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 11 | `productionDate` | Date | Date | Yes |  | Production date |
| 12 | `lossCategoryId` | String |  | Yes | `u_mes_perf_lossCategory._id` | Loss category (ID) |
| 13 | `lossCategoryName` | String |  | Yes | display value of `u_mes_perf_lossCategory` | Loss category (display value) |
| 14 | `reasonCodeId` | String |  | Yes | `u_mes_perf_reasonCode._id` | Reason (ID) |
| 15 | `reasonCodeName` | String |  | Yes | display value of `u_mes_perf_reasonCode` | Reason (display value) |
| 16 | `isPlanned` | Boolean |  | Yes |  | Planned loss |
| 17 | `occurrenceCount` | Int32 |  | Yes |  | Number of events |
| 18 | `lossMinutes` | Decimal128 |  | Yes |  | Lost minutes |
| 19 | `lossUnits` | Int32 |  | Yes |  | Lost units |
| 20 | `lossPctOfPlannedTime` | Decimal128 |  | Yes |  | Share of planned production time |
| 21 | `paretoRank` | Int32 |  | Yes |  | Rank within line, shift and date |
| 22 | `cumulativePct` | Decimal128 |  | Yes |  | Cumulative Pareto percentage |
| 23 | `maintenanceWorkOrderCount` | Int32 |  | Yes |  | Work orders raised for the reason |
| 24 | `capaCount` | Int32 |  | Yes |  | CAPAs linked |
| 25 | `calculatedAt` | Date | Datetime | Yes |  | Calculation time |
| 26 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Calculated, Recalculated) | Record status |
| 27 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 28 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 29 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 30 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 31 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 32 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 33 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1326 `u_mes_perf_workCenterPerformance`

| Item | Value |
|---|---|
| Module | perf — Performance Management |
| Kind / Type / UI label | Entity / Reports / Station Performance |
| Purpose | Hourly station performance: throughput, cycle time against takt, WIP, blocked and starved time and constraint flag. |
| Why a separate collection | Calculated report table per station and hour. |
| Business key (`recordNo`) | WCP-<yyyymmddhh>-<work centre code> |
| Status values | Calculated, Recalculated |
| Indexes | unique `recordNo`; (`lineId`, `periodStartAt`); (`workCenterId`, `periodStartAt`) |
| Questions | Q38, Q40, Q45, Q116 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1326 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: WCP-<yyyymmddhh>-<work centre code> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 6 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 7 | `lineId` | String |  | Yes | `u_mes_mast_line._id` | Line (ID) |
| 8 | `lineName` | String |  | Yes | display value of `u_mes_mast_line` | Line (display value) |
| 9 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 10 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 11 | `productionDate` | Date | Date | Yes |  | Production date |
| 12 | `periodStartAt` | Date | Datetime | Yes |  | Hour start |
| 13 | `periodEndAt` | Date | Datetime | Yes |  | Hour end |
| 14 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Dominant variant in the hour (ID) |
| 15 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Dominant variant in the hour (display value) |
| 16 | `unitsCompleted` | Int32 |  | Yes |  | Units completed |
| 17 | `throughputPerHour` | Decimal128 |  | Yes |  | Throughput |
| 18 | `averageCycleTimeSec` | Decimal128 |  | Yes |  | Average actual cycle time |
| 19 | `taktTimeSec` | Decimal128 |  | Yes |  | Takt time |
| 20 | `taktBreachCount` | Int32 |  | Yes |  | Cycles above takt |
| 21 | `wipQuantity` | Int32 |  | Yes |  | WIP in front of the station at hour end |
| 22 | `blockedMinutes` | Decimal128 |  | Yes |  | Minutes blocked by downstream |
| 23 | `starvedMinutes` | Decimal128 |  | Yes |  | Minutes starved by upstream |
| 24 | `isConstraint` | Boolean |  | Yes |  | Active constraint in the hour |
| 25 | `rankInLine` | Int32 |  | Yes |  | Rank by throughput within the line (1 = slowest) |
| 26 | `calculatedAt` | Date | Datetime | Yes |  | Calculation time |
| 27 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Calculated, Recalculated) | Record status |
| 28 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 29 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 30 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 31 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 32 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 33 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 34 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1327 `u_mes_perf_operatorPerformance`

| Item | Value |
|---|---|
| Module | perf — Performance Management |
| Kind / Type / UI label | Entity / Reports / Operator Performance |
| Purpose | Labour efficiency per operator, station, variant, shift and date. |
| Why a separate collection | Calculated report table. |
| Business key (`recordNo`) | OPF-<yyyymmdd>-<badge no>-<work centre code> |
| Status values | Calculated, Recalculated |
| Indexes | unique `recordNo`; (`userId`, `productionDate`); (`workCenterId`, `productionDate`) |
| Questions | Q86, Q88 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1327 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: OPF-<yyyymmdd>-<badge no>-<work centre code> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `userId` | String |  | Yes | `u_mes_mast_user._id` | Operator (ID) |
| 6 | `userName` | String |  | Yes | display value of `u_mes_mast_user` | Operator (display value) |
| 7 | `workCenterId` | String |  | Yes | `u_mes_mast_workCenter._id` | Station (ID) |
| 8 | `workCenterName` | String |  | Yes | display value of `u_mes_mast_workCenter` | Station (display value) |
| 9 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant (ID) |
| 10 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant (display value) |
| 11 | `shiftId` | String |  | Yes | `u_mes_mast_shift._id` | Shift (ID) |
| 12 | `shiftName` | String |  | Yes | display value of `u_mes_mast_shift` | Shift (display value) |
| 13 | `productionDate` | Date | Date | Yes |  | Production date |
| 14 | `attendedMinutes` | Decimal128 |  | Yes |  | Minutes logged in |
| 15 | `earnedMinutes` | Decimal128 |  | Yes |  | Standard minutes earned |
| 16 | `efficiencyPct` | Decimal128 |  | Yes |  | Earned / attended |
| 17 | `goodQuantity` | Int32 |  | Yes |  | Good units |
| 18 | `rejectQuantity` | Int32 |  | Yes |  | Rejected units |
| 19 | `errorCount` | Int32 |  | Yes |  | Defects with 4M category Man |
| 20 | `interlockCount` | Int32 |  | Yes |  | Interlocks triggered |
| 21 | `calculatedAt` | Date | Datetime | Yes |  | Calculation time |
| 22 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Calculated, Recalculated) | Record status |
| 23 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 24 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 25 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 26 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 27 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 28 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 29 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1328 `u_mes_maint_maintenanceWorkOrderTask`

| Item | Value |
|---|---|
| Module | maint — Tooling And Maintenance |
| Kind / Type / UI label | Child / Transaction / Work Order Checklist |
| Purpose | Executed checklist task of a maintenance work order with its result. |
| Why a separate collection | Replaces an array of task results (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -T<nn> |
| Indexes | unique `recordNo`; (`maintenanceWorkOrderId`, `taskNo`) |
| Questions | Q49 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1328 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -T<nn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `maintenanceWorkOrderId` | String |  | Yes | `u_mes_maint_maintenanceWorkOrder._id` | Parent maintenance work order (ID) |
| 6 | `maintenanceWorkOrderName` | String |  | Yes | display value of `u_mes_maint_maintenanceWorkOrder` | Parent maintenance work order (display value) |
| 7 | `taskNo` | Int32 |  | Yes |  | Task number (copied from the plan task) |
| 8 | `maintenancePlanTaskId` | String |  | No | `u_mes_maint_maintenancePlanTask._id` | Plan task the row comes from (ID) |
| 9 | `maintenancePlanTaskName` | String |  | No | display value of `u_mes_maint_maintenancePlanTask` | Plan task the row comes from (display value) |
| 10 | `description` | String |  | Yes |  | Task text |
| 11 | `result` | String |  | Yes | enumeration: Done OK, Done Not OK, Not Applicable, Not Done | Result |
| 12 | `measuredValue` | Decimal128 |  | No |  | Measured value, when the task asks for one |
| 13 | `unitOfMeasureId` | String |  | No | `u_mes_mast_unitOfMeasure._id` | Unit (ID) |
| 14 | `unitOfMeasureName` | String |  | No | display value of `u_mes_mast_unitOfMeasure` | Unit (display value) |
| 15 | `comment` | String |  | No |  | Comment |
| 16 | `completedById` | String |  | No | `u_mes_mast_user._id` | Technician (user ID) |
| 17 | `completedBy` | String |  | No | `u_mes_mast_user.fullName` | Technician (user name) |
| 18 | `completedAt` | Date | Datetime | No |  | Completion time |
| 19 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 20 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 21 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 22 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 23 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 24 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 25 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1329 `u_mes_maint_sparePartTransaction`

| Item | Value |
|---|---|
| Module | maint — Tooling And Maintenance |
| Kind / Type / UI label | Entity / Transaction / Spare Part Transactions |
| Purpose | Spare-part issue, return, receipt, adjustment and scrap with work order and equipment. |
| Why a separate collection | Unbounded event data; `u_mes_maint_sparePart` keeps the balance. |
| Business key (`recordNo`) | SPT-<yyyymmdd>-<nnnnn> |
| Status values | Posted, Reversed |
| Indexes | unique `recordNo`; (`sparePartId`, `transactedAt`); (`maintenanceWorkOrderId`) |
| Questions | Q52 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1329 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: SPT-<yyyymmdd>-<nnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `sparePartId` | String |  | Yes | `u_mes_maint_sparePart._id` | Spare part (ID) |
| 6 | `sparePartName` | String |  | Yes | display value of `u_mes_maint_sparePart` | Spare part (display value) |
| 7 | `transactionType` | String |  | Yes | enumeration: Issue, Return, Receipt, Adjustment, Scrap | Transaction type |
| 8 | `quantity` | Decimal128 |  | Yes |  | Quantity (positive) |
| 9 | `unitOfMeasureId` | String |  | Yes | `u_mes_mast_unitOfMeasure._id` | Unit (ID) |
| 10 | `unitOfMeasureName` | String |  | Yes | display value of `u_mes_mast_unitOfMeasure` | Unit (display value) |
| 11 | `maintenanceWorkOrderId` | String |  | No | `u_mes_maint_maintenanceWorkOrder._id` | Work order (ID) |
| 12 | `maintenanceWorkOrderName` | String |  | No | display value of `u_mes_maint_maintenanceWorkOrder` | Work order (display value) |
| 13 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Equipment (ID) |
| 14 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Equipment (display value) |
| 15 | `storageLocationId` | String |  | Yes | `u_mes_matl_storageLocation._id` | Store location (ID) |
| 16 | `storageLocationName` | String |  | Yes | display value of `u_mes_matl_storageLocation` | Store location (display value) |
| 17 | `scanVerified` | Boolean |  | Yes |  | Part barcode scanned |
| 18 | `unitCostInr` | Decimal128 |  | Yes |  | Unit cost in INR |
| 19 | `transactedAt` | Date | Datetime | Yes |  | Transaction time |
| 20 | `transactedById` | String |  | Yes | `u_mes_mast_user._id` | User who posted (user ID) |
| 21 | `transactedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who posted (user name) |
| 22 | `erpDocumentNo` | String |  | No |  | ERP document number |
| 23 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Posted, Reversed) | Record status |
| 24 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 25 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 26 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 27 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 28 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 29 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 30 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1330 `u_mes_maint_reliabilitySummary`

| Item | Value |
|---|---|
| Module | maint — Tooling And Maintenance |
| Kind / Type / UI label | Entity / Reports / Reliability Summary |
| Purpose | MTBF and MTTR per equipment, line and period. |
| Why a separate collection | Calculated report table. |
| Business key (`recordNo`) | REL-<yyyymm or yyyymmdd>-<equipment code> |
| Status values | Calculated, Recalculated |
| Indexes | unique `recordNo`; (`equipmentId`, `periodStartAt`); (`lineId`, `periodStartAt`) |
| Questions | Q53 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1330 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: REL-<yyyymm or yyyymmdd>-<equipment code> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `equipmentId` | String |  | Yes | `u_mes_mast_equipment._id` | Equipment (ID) |
| 6 | `equipmentName` | String |  | Yes | display value of `u_mes_mast_equipment` | Equipment (display value) |
| 7 | `lineId` | String |  | Yes | `u_mes_mast_line._id` | Line (ID) |
| 8 | `lineName` | String |  | Yes | display value of `u_mes_mast_line` | Line (display value) |
| 9 | `shiftId` | String |  | No | `u_mes_mast_shift._id` | Shift, when the period is a shift (ID) |
| 10 | `shiftName` | String |  | No | display value of `u_mes_mast_shift` | Shift, when the period is a shift (display value) |
| 11 | `periodType` | String |  | Yes | enumeration: Shift, Day, Week, Month | Period type |
| 12 | `periodStartAt` | Date | Datetime | Yes |  | Period start |
| 13 | `periodEndAt` | Date | Datetime | Yes |  | Period end |
| 14 | `operatingHours` | Decimal128 |  | Yes |  | Run hours |
| 15 | `failureCount` | Int32 |  | Yes |  | Breakdowns |
| 16 | `repairMinutes` | Decimal128 |  | Yes |  | Total repair minutes |
| 17 | `mtbfHours` | Decimal128 |  | No |  | Mean time between failures; null when no failure |
| 18 | `mttrMinutes` | Decimal128 |  | No |  | Mean time to repair; null when no failure |
| 19 | `availabilityPct` | Decimal128 |  | Yes |  | Technical availability |
| 20 | `calculatedAt` | Date | Datetime | Yes |  | Calculation time |
| 21 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Calculated, Recalculated) | Record status |
| 22 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 23 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 24 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 25 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 26 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 27 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 28 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1331 `u_mes_maint_equipmentLifecycleEvent`

| Item | Value |
|---|---|
| Module | maint — Tooling And Maintenance |
| Kind / Type / UI label | Entity / Transaction / Equipment Lifecycle |
| Purpose | Lifecycle events of an equipment: commissioning, relocation, overhaul, refurbishment, upgrade, health assessment, replacement recommendation, decommissioning. |
| Why a separate collection | Unbounded history per equipment. |
| Business key (`recordNo`) | ELE-<equipment code>-<nnn> |
| Status values | Recorded, Approved, Cancelled |
| Indexes | unique `recordNo`; (`equipmentId`, `eventAt`) |
| Questions | Q104, Q105 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1331 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ELE-<equipment code>-<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `equipmentId` | String |  | Yes | `u_mes_mast_equipment._id` | Equipment (ID) |
| 6 | `equipmentName` | String |  | Yes | display value of `u_mes_mast_equipment` | Equipment (display value) |
| 7 | `eventType` | String |  | Yes | enumeration: Commissioning, Relocation, Overhaul, Refurbishment, Upgrade, Health Assessment, Replacement Recommendation, Decommissioning | Event type |
| 8 | `eventAt` | Date | Datetime | Yes |  | Event time |
| 9 | `description` | String |  | Yes |  | Description |
| 10 | `costInr` | Decimal128 |  | No |  | Cost in INR |
| 11 | `healthScore` | Decimal128 |  | No |  | Health score after the event (0 to 100) |
| 12 | `lifetimeCyclesAtEvent` | Int64 |  | No |  | Cycle counter at the event |
| 13 | `lifetimeRunHoursAtEvent` | Decimal128 |  | No |  | Run hours at the event |
| 14 | `maintenanceWorkOrderId` | String |  | No | `u_mes_maint_maintenanceWorkOrder._id` | Work order (ID) |
| 15 | `maintenanceWorkOrderName` | String |  | No | display value of `u_mes_maint_maintenanceWorkOrder` | Work order (display value) |
| 16 | `engineeringChangeId` | String |  | No | `u_mes_prod_engineeringChange._id` | Engineering change (ID) |
| 17 | `engineeringChangeName` | String |  | No | display value of `u_mes_prod_engineeringChange` | Engineering change (display value) |
| 18 | `modelPredictionId` | String |  | No | `u_mes_syst_modelPrediction._id` | Prediction that triggered the event (ID) |
| 19 | `modelPredictionName` | String |  | No | display value of `u_mes_syst_modelPrediction` | Prediction that triggered the event (display value) |
| 20 | `approvedById` | String |  | No | `u_mes_mast_user._id` | Approver (user ID) |
| 21 | `approvedBy` | String |  | No | `u_mes_mast_user.fullName` | Approver (user name) |
| 22 | `approvedAt` | Date | Datetime | No |  | Approval time |
| 23 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Recorded, Approved, Cancelled) | Record status |
| 24 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 25 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 26 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 27 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 28 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 29 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 30 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1332 `u_mes_syst_interlockRule`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Interlock Rules |
| Purpose | Configured check that the application must pass before a transaction is allowed, with its scope and override policy. |
| Why a separate collection | Plant-maintained configuration used by all modules. |
| Business key (`recordNo`) | ILR-<rule type code>-<nnn>, e.g. ILR-SEQ-001 |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; (`ruleType`, `status`); (`workCenterId`); (`operationId`) |
| Questions | X1 list (section 3) |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1332 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ILR-<rule type code>-<nnn>, e.g. ILR-SEQ-001 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Rule name |
| 6 | `ruleType` | String |  | Yes | enumeration: Hold Check, Sequence Check, Mandatory Scan, Duplicate Serial, Wrong Order, Wrong Station, Variant Check, Component Lot Capture, Lot Release Check, Expiry Check, Kit Completeness, Genealogy Completeness, Recipe Release Check, Program Version Check, Work Instruction Release Check, Acknowledgement Check, Mandatory Inspection, NOK Result, Skill Check, Login Check, Equipment Readiness, Tool Life, Calibration Check, Environment Check, Setup Check, Alarm Restart | Check type |
| 7 | `transactionPoint` | String |  | Yes | enumeration: Operation Start, Operation Complete, Material Issue, Kit Release, Pack Out, Dispatch, Order Close, Login, Inspection Accept | Where the check runs |
| 8 | `lineId` | String |  | No | `u_mes_mast_line._id` | Line scope (null = all) (ID) |
| 9 | `lineName` | String |  | No | display value of `u_mes_mast_line` | Line scope (null = all) (display value) |
| 10 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station scope (ID) |
| 11 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station scope (display value) |
| 12 | `operationId` | String |  | No | `u_mes_prod_operation._id` | Operation scope (ID) |
| 13 | `operationName` | String |  | No | display value of `u_mes_prod_operation` | Operation scope (display value) |
| 14 | `itemId` | String |  | No | `u_mes_prod_item._id` | Item scope (ID) |
| 15 | `itemName` | String |  | No | display value of `u_mes_prod_item` | Item scope (display value) |
| 16 | `severity` | String |  | Yes | enumeration: Warning, Block | Warning only or block |
| 17 | `overrideAllowed` | Boolean |  | Yes |  | Override permitted |
| 18 | `overrideRoleId` | String |  | No | `u_mes_mast_role._id` | Role allowed to override (ID) |
| 19 | `overrideRoleName` | String |  | No | display value of `u_mes_mast_role` | Role allowed to override (display value) |
| 20 | `overrideRequiresSignature` | Boolean |  | Yes |  | Override needs an electronic signature |
| 21 | `overrideRequiresReasonCode` | Boolean |  | Yes |  | Override needs a reason code |
| 22 | `escalationRuleId` | String |  | No | `u_mes_syst_escalationRule._id` | Escalation when the block is not cleared (ID) |
| 23 | `escalationRuleName` | String |  | No | display value of `u_mes_syst_escalationRule` | Escalation when the block is not cleared (display value) |
| 24 | `messageText` | String |  | Yes |  | Operator message |
| 25 | `validFrom` | Date | Date | Yes |  | Valid from |
| 26 | `validTo` | Date | Date | No |  | Valid to |
| 27 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 28 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1333 `u_mes_syst_statusTransitionRole`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Relationship / Master / Status Transition Roles |
| Purpose | Roles allowed to perform a status transition defined in `u_mes_syst_statusTransition`. |
| Why a separate collection | Many-to-many between transition and role. |
| Business key (`recordNo`) | parent recordNo + -R<nn> |
| Indexes | unique `recordNo`; unique (`statusTransitionId`, `roleId`) |
| Questions | Q1, Q2, Q22, Q28, Q30, Q51, Q61, Q114 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1333 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -R<nn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `statusTransitionId` | String |  | Yes | `u_mes_syst_statusTransition._id` | Parent status transition (ID) |
| 6 | `statusTransitionName` | String |  | Yes | display value of `u_mes_syst_statusTransition` | Parent status transition (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `roleId` | String |  | Yes | `u_mes_mast_role._id` | Role (ID) |
| 9 | `roleName` | String |  | Yes | display value of `u_mes_mast_role` | Role (display value) |
| 10 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1334 `u_mes_syst_escalationRule`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Escalation Rules |
| Purpose | Routing and SLA rule for an exception type: first owner role, response and resolution targets. |
| Why a separate collection | Plant-maintained configuration; levels in a child collection. |
| Business key (`recordNo`) | ESC-<code>, e.g. ESC-BREAKDOWN-CRIT |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; (`sourceType`) |
| Questions | Q9, Q34, Q42, Q43, Q56, Q69, Q76, Q97 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1334 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ESC-<code>, e.g. ESC-BREAKDOWN-CRIT |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Rule name |
| 6 | `sourceType` | String |  | Yes | enumeration: Interlock, Andon, Alarm, Alert Rule, Breakdown, Audit, Nonconformance, Customer Complaint | Exception source |
| 7 | `severity` | String |  | No | enumeration: Low, Medium, High, Critical | Severity the rule applies to (null = all) |
| 8 | `lineId` | String |  | No | `u_mes_mast_line._id` | Line scope (ID) |
| 9 | `lineName` | String |  | No | display value of `u_mes_mast_line` | Line scope (display value) |
| 10 | `firstResponderRoleId` | String |  | Yes | `u_mes_mast_role._id` | First owner role (ID) |
| 11 | `firstResponderRoleName` | String |  | Yes | display value of `u_mes_mast_role` | First owner role (display value) |
| 12 | `requiredSkillId` | String |  | No | `u_mes_mast_skill._id` | Skill used to pick the person (Level 4) (ID) |
| 13 | `requiredSkillName` | String |  | No | display value of `u_mes_mast_skill` | Skill used to pick the person (Level 4) (display value) |
| 14 | `responseTargetMinutes` | Int32 |  | Yes |  | Target to acknowledge |
| 15 | `resolutionTargetMinutes` | Int32 |  | Yes |  | Target to resolve |
| 16 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 17 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1335 `u_mes_syst_escalationRuleLevel`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Child / Master / Escalation Levels |
| Purpose | Each escalation level of a rule: delay after raise, role and channel. |
| Why a separate collection | Replaces an array of levels (DATA-001). |
| Business key (`recordNo`) | parent recordNo + -L<n> |
| Indexes | unique `recordNo`; (`escalationRuleId`, `level`) |
| Questions | Q9, Q34, Q42, Q56, Q69 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1335 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -L<n> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `escalationRuleId` | String |  | Yes | `u_mes_syst_escalationRule._id` | Parent escalation rule (ID) |
| 6 | `escalationRuleName` | String |  | Yes | display value of `u_mes_syst_escalationRule` | Parent escalation rule (display value) |
| 7 | `level` | Int32 |  | Yes |  | Escalation level (1 = first escalation) |
| 8 | `delayMinutes` | Int32 |  | Yes |  | Minutes after raise without acknowledgement / resolution |
| 9 | `basis` | String |  | Yes | enumeration: Not Acknowledged, Not Resolved | What triggers the level |
| 10 | `roleId` | String |  | Yes | `u_mes_mast_role._id` | Role notified (ID) |
| 11 | `roleName` | String |  | Yes | display value of `u_mes_mast_role` | Role notified (display value) |
| 12 | `notificationTypeId` | String |  | Yes | `u_mes_syst_notificationType._id` | Notification type (ID) |
| 13 | `notificationTypeName` | String |  | Yes | display value of `u_mes_syst_notificationType` | Notification type (display value) |
| 14 | `channel` | String |  | Yes | enumeration: Andon Board, SMS, Email, Mobile App, Public Address | Channel |
| 15 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1336 `u_mes_syst_alertRule`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Alert Rules |
| Purpose | Threshold rule on a KPI or signal with the resulting action. |
| Why a separate collection | Plant-maintained configuration. |
| Business key (`recordNo`) | ALR-<metric code>-<nnn> |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; (`metric`, `status`); (`lineId`) |
| Questions | Q26, Q42, Q43, Q70, Q76, Q97, Q112 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1336 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: ALR-<metric code>-<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Rule name |
| 6 | `metric` | String |  | Yes | enumeration: OEE, Availability, Downtime Minutes, Reject Rate, Output Gap, Process Deviation, SPC Rule Violation, Line-side Stock Cover, Environment Limit, Model Anomaly Score | Metric watched |
| 7 | `lineId` | String |  | No | `u_mes_mast_line._id` | Line scope (ID) |
| 8 | `lineName` | String |  | No | display value of `u_mes_mast_line` | Line scope (display value) |
| 9 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station scope (ID) |
| 10 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station scope (display value) |
| 11 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Equipment scope (ID) |
| 12 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Equipment scope (display value) |
| 13 | `processTagId` | String |  | No | `u_mes_perf_processTag._id` | Tag watched (Process Deviation, Environment Limit) (ID) |
| 14 | `processTagName` | String |  | No | display value of `u_mes_perf_processTag` | Tag watched (Process Deviation, Environment Limit) (display value) |
| 15 | `itemId` | String |  | No | `u_mes_prod_item._id` | Item scope (stock cover) (ID) |
| 16 | `itemName` | String |  | No | display value of `u_mes_prod_item` | Item scope (stock cover) (display value) |
| 17 | `comparison` | String |  | Yes | enumeration: Less Than, Greater Than, Outside Band | Comparison |
| 18 | `thresholdValue` | Decimal128 |  | Yes |  | Threshold |
| 19 | `thresholdUpperValue` | Decimal128 |  | No |  | Upper value for Outside Band |
| 20 | `evaluationWindowMinutes` | Int32 |  | Yes |  | Window evaluated |
| 21 | `severity` | String |  | Yes | enumeration: Low, Medium, High, Critical | Severity |
| 22 | `actionType` | String |  | Yes | enumeration: Notify, Hold, Stop Equipment, Block Process, Create Work Order, Create Nonconformance | Action |
| 23 | `notificationTypeId` | String |  | Yes | `u_mes_syst_notificationType._id` | Notification type (ID) |
| 24 | `notificationTypeName` | String |  | Yes | display value of `u_mes_syst_notificationType` | Notification type (display value) |
| 25 | `escalationRuleId` | String |  | No | `u_mes_syst_escalationRule._id` | Escalation rule (ID) |
| 26 | `escalationRuleName` | String |  | No | display value of `u_mes_syst_escalationRule` | Escalation rule (display value) |
| 27 | `falseAlertCount` | Int32 |  | Yes |  | Alerts closed as false (tuning, Level 4) |
| 28 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 29 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1337 `u_mes_syst_analyticsModel`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Analytics Models |
| Purpose | Registry of AI / ML / rule models and their released versions. |
| Why a separate collection | Each model version must be traceable from every prediction and inspection result. |
| Business key (`recordNo`) | AIM-<code>-<version>, e.g. AIM-VIS-BOOT-1.3 |
| Status values | In Preparation, Released, Retired |
| Indexes | unique `recordNo`; (`modelType`, `status`) |
| Questions | Q33, Q46, Q47, Q54, Q67, Q78, Q87, Q88, Q104, Q105, Q111, Q112, Q129 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1337 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: AIM-<code>-<version>, e.g. AIM-VIS-BOOT-1.3 |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | Model name |
| 6 | `modelType` | String |  | Yes | enumeration: Vision Classification, Defect Prediction, OEE Forecast, Anomaly Detection, Maintenance Prediction, Demand Forecast, Recipe Optimisation, Operator Risk, Assignment Recommendation | Model type |
| 7 | `version` | String |  | Yes |  | Model version |
| 8 | `framework` | String |  | No |  | Framework / runtime |
| 9 | `trainingDatasetRef` | String |  | No |  | Training data set reference |
| 10 | `validationMetricName` | String |  | No |  | Validation metric, e.g. Recall |
| 11 | `validationMetricValue` | Decimal128 |  | No |  | Validation result |
| 12 | `equipmentId` | String |  | No | `u_mes_mast_equipment._id` | Equipment the model runs on, when edge-deployed (ID) |
| 13 | `equipmentName` | String |  | No | display value of `u_mes_mast_equipment` | Equipment the model runs on, when edge-deployed (display value) |
| 14 | `modelControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Model file / card (ID) |
| 15 | `modelControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Model file / card (display value) |
| 16 | `effectiveFrom` | Date | Date | Yes |  | Effective from |
| 17 | `effectiveTo` | Date | Date | No |  | Effective to |
| 18 | `approvedById` | String |  | Yes | `u_mes_mast_user._id` | Approver (user ID) |
| 19 | `approvedBy` | String |  | Yes | `u_mes_mast_user.fullName` | Approver (user name) |
| 20 | `approvedAt` | Date | Datetime | Yes |  | Approval time |
| 21 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (In Preparation, Released, Retired) | Record status |
| 22 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1338 `u_mes_syst_modelPrediction`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Transaction / Model Predictions |
| Purpose | Each prediction, classification, forecast or recommendation produced by a model, with the action and the actual outcome. |
| Why a separate collection | Unbounded event data. |
| Business key (`recordNo`) | PRD-<yyyymmdd>-<nnnnnn> |
| Status values | Open, Actioned, Dismissed, Verified |
| Indexes | unique `recordNo`; (`analyticsModelId`, `predictedAt`); (`relatedEntityId`) |
| Questions | X10 list (section 3) |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1338 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: PRD-<yyyymmdd>-<nnnnnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `analyticsModelId` | String |  | Yes | `u_mes_syst_analyticsModel._id` | Model (ID) |
| 6 | `analyticsModelName` | String |  | Yes | display value of `u_mes_syst_analyticsModel` | Model (display value) |
| 7 | `modelVersion` | String |  | Yes |  | Model version used |
| 8 | `predictionType` | String |  | Yes | enumeration: Classification, Forecast, Anomaly, Maintenance Priority, Remaining Useful Life, Recommendation, Operator Risk, Assignment Recommendation | Prediction type |
| 9 | `relatedCollectionName` | String |  | Yes | any `u_mes_*` collection | Subject collection |
| 10 | `relatedEntityId` | String |  | Yes | `_id` in the named collection | Subject (ID) |
| 11 | `relatedEntityName` | String |  | Yes | display value in the named collection | Subject (display value) |
| 12 | `workCenterId` | String |  | No | `u_mes_mast_workCenter._id` | Station context (ID) |
| 13 | `workCenterName` | String |  | No | display value of `u_mes_mast_workCenter` | Station context (display value) |
| 14 | `productVariantId` | String |  | No | `u_mes_prod_productVariant._id` | Variant context (ID) |
| 15 | `productVariantName` | String |  | No | display value of `u_mes_prod_productVariant` | Variant context (display value) |
| 16 | `shiftId` | String |  | No | `u_mes_mast_shift._id` | Shift context (ID) |
| 17 | `shiftName` | String |  | No | display value of `u_mes_mast_shift` | Shift context (display value) |
| 18 | `predictedAt` | Date | Datetime | Yes |  | Prediction time |
| 19 | `horizonMinutes` | Int32 |  | No |  | Forecast horizon |
| 20 | `predictedClass` | String |  | No |  | Predicted class / label |
| 21 | `predictedValue` | Decimal128 |  | No |  | Predicted numeric value |
| 22 | `confidence` | Decimal128 |  | No |  | Confidence / score 0 to 1 |
| 23 | `recommendedAction` | String |  | No |  | Recommended action |
| 24 | `actionStatus` | String |  | Yes | enumeration: Not Required, Pending, Approved, Applied, Rejected | Action status |
| 25 | `actionTakenById` | String |  | No | `u_mes_mast_user._id` | User who approved / applied the action (user ID) |
| 26 | `actionTakenBy` | String |  | No | `u_mes_mast_user.fullName` | User who approved / applied the action (user name) |
| 27 | `actionTakenAt` | Date | Datetime | No |  | Action time |
| 28 | `actualValue` | Decimal128 |  | No |  | Observed value for accuracy tracking |
| 29 | `actualClass` | String |  | No |  | Observed class |
| 30 | `notificationId` | String |  | No | `u_mes_syst_notification._id` | Notification raised (ID) |
| 31 | `notificationName` | String |  | No | display value of `u_mes_syst_notification` | Notification raised (display value) |
| 32 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Open, Actioned, Dismissed, Verified) | Record status |
| 33 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 34 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 35 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 36 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 37 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 38 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 39 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1339 `u_mes_syst_simulationStudy`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Transaction / Simulation Studies |
| Purpose | Digital-twin / what-if study with its input snapshot, result, approval and controlled rollout and pre / post comparison. |
| Why a separate collection | Study record; inputs and outputs are files in `u_mes_syst_controlledDocument`. |
| Business key (`recordNo`) | SIM-<yyyy>-<nnn> |
| Status values | Planned, Completed, Approved, Rolled Out, Rejected |
| Indexes | unique `recordNo`; (`studyType`, `status`) |
| Questions | Q65, Q66, Q79, Q107, Q108 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1339 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: SIM-<yyyy>-<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `title` | String |  | Yes |  | Title |
| 6 | `studyType` | String |  | Yes | enumeration: Process, Inventory, Equipment, Calibration Baseline | Study type |
| 7 | `relatedCollectionName` | String |  | No | any `u_mes_*` collection | Studied object collection |
| 8 | `relatedEntityId` | String |  | No | `_id` in the named collection | Studied object (ID) |
| 9 | `relatedEntityName` | String |  | No | display value in the named collection | Studied object (display value) |
| 10 | `scenarioText` | String |  | Yes |  | Scenario description |
| 11 | `inputSnapshotAt` | Date | Datetime | Yes |  | Time of the live-data snapshot |
| 12 | `resultText` | String |  | No |  | Result summary |
| 13 | `predictedValue` | Decimal128 |  | No |  | Predicted KPI value |
| 14 | `predictedKpi` | String |  | No |  | KPI predicted, e.g. FPY % |
| 15 | `recommendedRecipeId` | String |  | No | `u_mes_prod_recipe._id` | Recipe version proposed (ID) |
| 16 | `recommendedRecipeName` | String |  | No | display value of `u_mes_prod_recipe` | Recipe version proposed (display value) |
| 17 | `rolloutProductionOrderId` | String |  | No | `u_mes_plan_productionOrder._id` | Order used for the controlled rollout (ID) |
| 18 | `rolloutProductionOrderName` | String |  | No | display value of `u_mes_plan_productionOrder` | Order used for the controlled rollout (display value) |
| 19 | `actualValue` | Decimal128 |  | No |  | Observed KPI after rollout |
| 20 | `comparisonResult` | String |  | No | enumeration: Better, Equal, Worse | Pre / post comparison |
| 21 | `resultControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Study report (ID) |
| 22 | `resultControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Study report (display value) |
| 23 | `approvedById` | String |  | No | `u_mes_mast_user._id` | Approver (user ID) |
| 24 | `approvedBy` | String |  | No | `u_mes_mast_user.fullName` | Approver (user name) |
| 25 | `approvedAt` | Date | Datetime | No |  | Approval time |
| 26 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Planned, Completed, Approved, Rolled Out, Rejected) | Record status |
| 27 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 28 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 29 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 30 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 31 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 32 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 33 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1340 `u_mes_syst_recordPolicy`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Record Policies |
| Purpose | Edit, lock and retention policy per collection. |
| Why a separate collection | One policy per collection; read by the application on every update and delete. |
| Business key (`recordNo`) | RPO-<collection name> |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; unique (`collectionName`) |
| Questions | Q1, Q32, Q115, Q118 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1340 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: RPO-<collection name> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `collectionName` | String |  | Yes | any `u_mes_*` collection | Collection governed |
| 6 | `editPolicy` | String |  | Yes | enumeration: Free Edit, Controlled Edit, No Edit After Lock, Append Only | Edit policy |
| 7 | `lockOnStatusDefinitionId` | String |  | No | `u_mes_syst_statusDefinition._id` | Status from which the record is locked (ID) |
| 8 | `lockOnStatusDefinitionName` | String |  | No | display value of `u_mes_syst_statusDefinition` | Status from which the record is locked (display value) |
| 9 | `requiresReasonForEdit` | Boolean |  | Yes |  | Edit needs a reason |
| 10 | `requiresSignatureForEdit` | Boolean |  | Yes |  | Edit needs an electronic signature |
| 11 | `editRoleId` | String |  | No | `u_mes_mast_role._id` | Role allowed to edit under Controlled Edit (ID) |
| 12 | `editRoleName` | String |  | No | display value of `u_mes_mast_role` | Role allowed to edit under Controlled Edit (display value) |
| 13 | `deleteAllowed` | Boolean |  | Yes |  | Physical delete allowed (false for all transaction data) |
| 14 | `retentionYears` | Int32 |  | Yes |  | Retention period |
| 15 | `archiveAfterMonths` | Int32 |  | No |  | Move to archive storage after |
| 16 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 17 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1341 `u_mes_syst_savedView`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Master / Saved Views |
| Purpose | Saved dashboard and comparison filters per user or role. |
| Why a separate collection | User-maintained configuration. |
| Business key (`recordNo`) | VIEW-<user or role code>-<nnn> |
| Status values | Active, Inactive |
| Indexes | unique `recordNo`; (`ownerUserId`); (`roleId`) |
| Questions | Q45, Q109 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1341 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: VIEW-<user or role code>-<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `name` | String |  | Yes |  | View name |
| 6 | `viewType` | String |  | Yes | enumeration: Dashboard, Comparison, Pareto, Trend, List | View type |
| 7 | `collectionName` | String |  | Yes | any `u_mes_*` collection | Main collection queried |
| 8 | `filterJson` | String |  | Yes |  | Filter as JSON text |
| 9 | `sortJson` | String |  | No |  | Sort as JSON text |
| 10 | `ownerUserId` | String |  | Yes | `u_mes_mast_user._id` | Owner (ID) |
| 11 | `ownerUserName` | String |  | Yes | display value of `u_mes_mast_user` | Owner (display value) |
| 12 | `roleId` | String |  | No | `u_mes_mast_role._id` | Role the view is shared with (ID) |
| 13 | `roleName` | String |  | No | display value of `u_mes_mast_role` | Role the view is shared with (display value) |
| 14 | `isShared` | Boolean |  | Yes |  | Visible to the role |
| 15 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Active, Inactive) | Record status |
| 16 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

### 1342 `u_mes_syst_backupRun`

| Item | Value |
|---|---|
| Module | syst — System and Integration |
| Kind / Type / UI label | Entity / Transaction / Backup and Restore Runs |
| Purpose | Evidence of database backups and restore tests with measured recovery time (optional). |
| Why a separate collection | Unbounded run history; IATF record-retention evidence. |
| Business key (`recordNo`) | BKP-<yyyymmdd>-<nn> |
| Status values | Running, Succeeded, Failed |
| Indexes | unique `recordNo`; (`runType`, `startedAt`) |
| Questions | Q118 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1342 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: BKP-<yyyymmdd>-<nn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `runType` | String |  | Yes | enumeration: Full Backup, Incremental Backup, Restore Test, Failover Test | Run type |
| 6 | `startedAt` | Date | Datetime | Yes |  | Start |
| 7 | `completedAt` | Date | Datetime | No |  | End |
| 8 | `sizeBytes` | Int64 |  | No |  | Backup size |
| 9 | `storageTarget` | String |  | Yes |  | Target storage |
| 10 | `recoveryTimeMinutes` | Int32 |  | No |  | Measured recovery time (restore tests) |
| 11 | `recoveryPointMinutes` | Int32 |  | No |  | Data loss window (restore tests) |
| 12 | `evidenceControlledDocumentId` | String |  | No | `u_mes_syst_controlledDocument._id` | Test report (ID) |
| 13 | `evidenceControlledDocumentName` | String |  | No | display value of `u_mes_syst_controlledDocument` | Test report (display value) |
| 14 | `performedById` | String |  | Yes | `u_mes_mast_user._id` | User or system user (user ID) |
| 15 | `performedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User or system user (user name) |
| 16 | `status` | String |  | Yes | `u_mes_syst_statusDefinition` (Running, Succeeded, Failed) | Record status |
| 17 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |
| 18 | `createdAt` | Date | Datetime | Yes |  | Time the document was created (local plant time, DATA-004) |
| 19 | `createdById` | String |  | Yes | `u_mes_mast_user._id` | User who created the document (ID) |
| 20 | `createdBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who created the document (name) |
| 21 | `updatedAt` | Date | Datetime | Yes |  | Time the document was last updated |
| 22 | `updatedById` | String |  | Yes | `u_mes_mast_user._id` | User who last updated the document (ID) |
| 23 | `updatedBy` | String |  | Yes | `u_mes_mast_user.fullName` | User who last updated the document (name) |

### 1343 `u_mes_matl_storageLocationAllowedItem`

| Item | Value |
|---|---|
| Module | matl — Material Management |
| Kind / Type / UI label | Relationship / Master / Storage Allowed Items |
| Purpose | Items or item groups a storage location may hold (storage matrix) — optional. |
| Why a separate collection | Many-to-many between location and item / item group. |
| Business key (`recordNo`) | parent recordNo + -A<nnn> |
| Indexes | unique `recordNo`; (`itemId`); (`itemGroupId`) |
| Questions | Options_Switch row 13 |

| # | Key | BSON type | Date tag | Required | Reference / allowed values | Description |
|---|---|---|---|---|---|---|
| 1 | `_id` | String |  | Yes |  | 16-digit numeric string: collection number 1343 + 12-digit running number |
| 2 | `recordNo` | String |  | Yes |  | Business key: parent recordNo + -A<nnn> |
| 3 | `siteId` | String |  | Yes | `u_mes_mast_site._id` | Site the record belongs to (ID) |
| 4 | `siteName` | String |  | Yes | display value of `u_mes_mast_site` | Site the record belongs to (display value) |
| 5 | `storageLocationId` | String |  | Yes | `u_mes_matl_storageLocation._id` | Parent storage location (ID) |
| 6 | `storageLocationName` | String |  | Yes | display value of `u_mes_matl_storageLocation` | Parent storage location (display value) |
| 7 | `sequenceNo` | Int32 |  | Yes |  | Order of the row within the parent |
| 8 | `itemId` | String |  | No | `u_mes_prod_item._id` | Item allowed (null when an item group is given) (ID) |
| 9 | `itemName` | String |  | No | display value of `u_mes_prod_item` | Item allowed (null when an item group is given) (display value) |
| 10 | `itemGroupId` | String |  | No | `u_mes_prod_itemGroup._id` | Item group allowed (ID) |
| 11 | `itemGroupName` | String |  | No | display value of `u_mes_prod_itemGroup` | Item group allowed (display value) |
| 12 | `schemaVersion` | Int32 |  | Yes |  | Document schema version, starts at NumberInt(1) |

## 6. Changes to existing collections

All keys below are additions; no existing key is renamed, removed or re-typed. Under the validator rule (every key present, null allowed where the specification allows it), "Required = No" means the key is present and may be null; "Required = Yes" Booleans are written as `false` for existing documents during migration. Date tags follow DATA-004.

| # | Collection | Key to add | BSON type | Date tag | Required | Reference / allowed values | Questions |
|---|---|---|---|---|---|---|---|
| 1 | `u_mes_mast_equipment` | `isProductionReady` | Boolean | | Yes | | Q98, Q99 |
| 2 | `u_mes_mast_equipment` | `readinessReasonText` | String | | No | | Q98 |
| 3 | `u_mes_mast_equipment` | `healthScore` | Decimal128 | | No | 0 to 100 | Q104 |
| 4 | `u_mes_mast_equipment` | `healthScoreAt` | Date | Datetime | No | | Q104 |
| 5 | `u_mes_mast_equipment` | `acquisitionCostInr` | Decimal128 | | No | | Q104 |
| 6 | `u_mes_mast_equipment` | `plannedReplacementDate` | Date | Date | No | | Q104, Q105 |
| 7 | `u_mes_mast_shiftRosterAssignment` | `assignedFromAt` | Date | Datetime | No | | Q84 |
| 8 | `u_mes_mast_shiftRosterAssignment` | `assignedToAt` | Date | Datetime | No | | Q84 |
| 9 | `u_mes_mast_shiftRosterAssignment` | `assignmentSource` | String | | Yes | enumeration: Manual, Rule, Model | Q87 |
| 10 | `u_mes_mast_shiftRosterAssignment` | `suggestionScore` | Decimal128 | | No | | Q87 |
| 11 | `u_mes_mast_skillCertification` | `trainedDocumentRevision` | String | | No | | Q82, Q83 |
| 12 | `u_mes_mast_skillCertification` | `requalificationRequired` | Boolean | | Yes | | Q83 |
| 13 | `u_mes_mast_skillCertification` | `revocationSource` | String | | No | enumeration: Expiry, Document Revision, Manual, Assessment Failure | Q83 |
| 14 | `u_mes_prod_item` | `fefoRequired` | Boolean | | Yes | | Q72 |
| 15 | `u_mes_prod_item` | `exposureControlled` | Boolean | | Yes | | Q73 |
| 16 | `u_mes_prod_item` | `openLifeMinutes` | Int32 | | No | | Q73 |
| 17 | `u_mes_prod_recipe` | `previousVersionRecipeId` | String | | No | `u_mes_prod_recipe._id` | Q61 |
| 18 | `u_mes_prod_recipe` | `previousVersionRecipeName` | String | | No | display value of `u_mes_prod_recipe` | Q61 |
| 19 | `u_mes_prod_recipe` | `changeReasonText` | String | | No | | Q61 |
| 20 | `u_mes_prod_recipe` | `releasedAt` | Date | Datetime | No | | Q62 |
| 21 | `u_mes_prod_recipe` | `isGoldenRecipe` | Boolean | | Yes | | Q63, Q64 |
| 22 | `u_mes_prod_recipe` | `goldenDesignatedAt` | Date | Datetime | No | | Q63 |
| 23 | `u_mes_prod_recipe` | `goldenDesignatedById` | String | | No | `u_mes_mast_user._id` | Q63 |
| 24 | `u_mes_prod_recipe` | `goldenDesignatedBy` | String | | No | `u_mes_mast_user.fullName` | Q63 |
| 25 | `u_mes_prod_recipe` | `origin` | String | | Yes | enumeration: Engineering, Optimisation Model, Simulation Study | Q67 |
| 26 | `u_mes_prod_recipe` | `analyticsModelId` | String | | No | `u_mes_syst_analyticsModel._id` | Q67 |
| 27 | `u_mes_prod_recipe` | `analyticsModelName` | String | | No | display value of `u_mes_syst_analyticsModel` | Q67 |
| 28 | `u_mes_prod_workInstruction` | `reacknowledgeOnRevision` | Boolean | | Yes | | Q4, Q92 |
| 29 | `u_mes_prod_workInstruction` | `generationSource` | String | | Yes | enumeration: Manual, Generated From Bill Of Process, Generated By Model | Q93 |
| 30 | `u_mes_prod_workInstruction` | `sourceBillOfProcessId` | String | | No | `u_mes_prod_billOfProcess._id` | Q93 |
| 31 | `u_mes_prod_workInstruction` | `sourceBillOfProcessName` | String | | No | display value of `u_mes_prod_billOfProcess` | Q93 |
| 32 | `u_mes_prod_workInstructionStep` | `arContentControlledDocumentId` | String | | No | `u_mes_syst_controlledDocument._id` | Q94 |
| 33 | `u_mes_prod_workInstructionStep` | `arContentControlledDocumentName` | String | | No | display value of `u_mes_syst_controlledDocument` | Q94 |
| 34 | `u_mes_prod_workInstructionStep` | `arAnchorRef` | String | | No | | Q94 |
| 35 | `u_mes_plan_productionOrder` | `onHold` | Boolean | | Yes | | Q2 |
| 36 | `u_mes_plan_productionOrder` | `qualityHoldId` | String | | No | `u_mes_qual_qualityHold._id` | Q2 |
| 37 | `u_mes_plan_productionOrder` | `qualityHoldName` | String | | No | display value of `u_mes_qual_qualityHold` | Q2 |
| 38 | `u_mes_plan_productionOrder` | `holdReasonCodeId` | String | | No | `u_mes_perf_reasonCode._id` | Q2 |
| 39 | `u_mes_plan_productionOrder` | `holdReasonCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q2 |
| 40 | `u_mes_plan_productionOrder` | `genealogyComplete` | Boolean | | Yes | | Q71 |
| 41 | `u_mes_plan_operationExecution` | `productVariantId` | String | | No | `u_mes_prod_productVariant._id` | Q38, Q120 |
| 42 | `u_mes_plan_operationExecution` | `productVariantName` | String | | No | display value of `u_mes_prod_productVariant` | Q38, Q120 |
| 43 | `u_mes_plan_operationExecution` | `recipeVersion` | String | | No | | Q3, Q20 |
| 44 | `u_mes_plan_operationExecution` | `recipeChecksum` | String | | No | | Q3, Q20 |
| 45 | `u_mes_plan_operationExecution` | `taktTimeSec` | Decimal128 | | No | | Q38 |
| 46 | `u_mes_plan_operationExecution` | `taktBreached` | Boolean | | Yes | | Q38 |
| 47 | `u_mes_plan_operationExecution` | `captureMethod` | String | | Yes | enumeration: Scan, PLC Signal, Manual Entry | Q5, Q11 |
| 48 | `u_mes_plan_operationExecution` | `startScanCode` | String | | No | | Q5, Q11 |
| 49 | `u_mes_plan_operationExecution` | `operatorSessionId` | String | | No | `u_mes_plan_operatorSession._id` | Q5, Q80 |
| 50 | `u_mes_plan_operationExecution` | `operatorSessionName` | String | | No | display value of `u_mes_plan_operatorSession` | Q5, Q80 |
| 51 | `u_mes_plan_operationExecution` | `checksVariantVerified` | Boolean | | Yes | | Q120 |
| 52 | `u_mes_plan_operationExecution` | `checksDocumentAcknowledged` | Boolean | | Yes | | Q3, Q90 |
| 53 | `u_mes_plan_operationExecution` | `checksEquipmentReady` | Boolean | | Yes | | Q99 |
| 54 | `u_mes_plan_operationExecution` | `checksMaterialReleased` | Boolean | | Yes | | Q13, Q31 |
| 55 | `u_mes_plan_operationExecution` | `checksSetupVerified` | Boolean | | Yes | | Q60 |
| 56 | `u_mes_plan_operationExecution` | `checksEnvironmentOk` | Boolean | | Yes | | Q97 |
| 57 | `u_mes_plan_operationExecution` | `interlockEventCount` | Int32 | | Yes | | X1 |
| 58 | `u_mes_plan_stepCompletion` | `overrideReasonCodeId` | String | | No | `u_mes_perf_reasonCode._id` | Q8 |
| 59 | `u_mes_plan_stepCompletion` | `overrideReasonCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q8 |
| 60 | `u_mes_plan_stepCompletion` | `arSessionRef` | String | | No | | Q95 |
| 61 | `u_mes_plan_labourBooking` | `operationExecutionId` | String | | No | `u_mes_plan_operationExecution._id` | Q85 |
| 62 | `u_mes_plan_labourBooking` | `operationExecutionName` | String | | No | display value of `u_mes_plan_operationExecution` | Q85 |
| 63 | `u_mes_plan_labourBooking` | `productVariantId` | String | | No | `u_mes_prod_productVariant._id` | Q85 |
| 64 | `u_mes_plan_labourBooking` | `productVariantName` | String | | No | display value of `u_mes_prod_productVariant` | Q85 |
| 65 | `u_mes_plan_labourBooking` | `operatorSessionId` | String | | No | `u_mes_plan_operatorSession._id` | Q85 |
| 66 | `u_mes_plan_labourBooking` | `operatorSessionName` | String | | No | display value of `u_mes_plan_operatorSession` | Q85 |
| 67 | `u_mes_plan_andonEvent` | `equipmentId` | String | | No | `u_mes_mast_equipment._id` | Q55 |
| 68 | `u_mes_plan_andonEvent` | `equipmentName` | String | | No | display value of `u_mes_mast_equipment` | Q55 |
| 69 | `u_mes_plan_andonEvent` | `severity` | String | | Yes | enumeration: Low, Medium, High, Critical | Q55 |
| 70 | `u_mes_plan_andonEvent` | `maintenanceWorkOrderId` | String | | No | `u_mes_maint_maintenanceWorkOrder._id` | Q55 |
| 71 | `u_mes_plan_andonEvent` | `maintenanceWorkOrderName` | String | | No | display value of `u_mes_maint_maintenanceWorkOrder` | Q55 |
| 72 | `u_mes_plan_andonEvent` | `escalationRuleId` | String | | No | `u_mes_syst_escalationRule._id` | Q56 |
| 73 | `u_mes_plan_andonEvent` | `escalationRuleName` | String | | No | display value of `u_mes_syst_escalationRule` | Q56 |
| 74 | `u_mes_plan_andonType` | `targetRepairSec` | Int32 | | No | | Q56 |
| 75 | `u_mes_plan_andonType` | `escalationRuleId` | String | | No | `u_mes_syst_escalationRule._id` | Q56 |
| 76 | `u_mes_plan_andonType` | `escalationRuleName` | String | | No | display value of `u_mes_syst_escalationRule` | Q56 |
| 77 | `u_mes_matl_kitLine` | `itemRevision` | String | | No | | Q74 |
| 78 | `u_mes_matl_kitLine` | `scannedItemRevision` | String | | No | | Q74 |
| 79 | `u_mes_matl_kitLine` | `scannedCode` | String | | No | | Q74 |
| 80 | `u_mes_matl_kitLine` | `isMandatory` | Boolean | | Yes | | Q74, Q75 |
| 81 | `u_mes_matl_kitLine` | `verifiedAt` | Date | Datetime | No | | Q74 |
| 82 | `u_mes_matl_kitLine` | `verificationResult` | String | | No | enumeration: Match, Wrong Item, Wrong Revision, Wrong Quantity, Not Scanned | Q74 |
| 83 | `u_mes_matl_materialRequest` | `replenishmentRuleId` | String | | No | `u_mes_matl_replenishmentRule._id` | Q77 |
| 84 | `u_mes_matl_materialRequest` | `replenishmentRuleName` | String | | No | display value of `u_mes_matl_replenishmentRule` | Q77 |
| 85 | `u_mes_trac_serialNumber` | `markingRecipeId` | String | | No | `u_mes_prod_recipe._id` | Q20, Q122 |
| 86 | `u_mes_trac_serialNumber` | `markingRecipeName` | String | | No | display value of `u_mes_prod_recipe` | Q20, Q122 |
| 87 | `u_mes_trac_serialNumber` | `markingRecipeVersion` | String | | No | | Q20, Q122 |
| 88 | `u_mes_trac_genealogyLink` | `childSerialNumberId` | String | | No | `u_mes_trac_serialNumber._id` | Q119 |
| 89 | `u_mes_trac_genealogyLink` | `childSerialNumberName` | String | | No | display value of `u_mes_trac_serialNumber` | Q119 |
| 90 | `u_mes_trac_genealogyLink` | `childWipUnitId` | String | | No | `u_mes_plan_wipUnit._id` | Q119 |
| 91 | `u_mes_trac_genealogyLink` | `childWipUnitName` | String | | No | display value of `u_mes_plan_wipUnit` | Q119 |
| 92 | `u_mes_trac_asBuiltRecord` | `genealogyComplete` | Boolean | | Yes | | Q17, Q71 |
| 93 | `u_mes_trac_asBuiltRecord` | `missingComponentCount` | Int32 | | Yes | | Q17, Q71 |
| 94 | `u_mes_trac_asBuiltRecordOperation` | `recipeId` | String | | No | `u_mes_prod_recipe._id` | Q17, Q20 |
| 95 | `u_mes_trac_asBuiltRecordOperation` | `recipeName` | String | | No | display value of `u_mes_prod_recipe` | Q17, Q20 |
| 96 | `u_mes_trac_asBuiltRecordOperation` | `recipeVersion` | String | | No | | Q17, Q20 |
| 97 | `u_mes_trac_asBuiltRecordOperation` | `recipeChecksum` | String | | No | | Q17, Q20 |
| 98 | `u_mes_qual_characteristic` | `positionCount` | Int32 | | Yes | 1 when the characteristic has a single position | Q24, Q126 |
| 99 | `u_mes_qual_inspectionPlan` | `itemRevision` | String | | No | | Q23 |
| 100 | `u_mes_qual_inspectionResult` | `positionNo` | Int32 | | No | matches `u_mes_qual_characteristicPosition.positionNo` | Q24, Q124, Q125, Q126 |
| 101 | `u_mes_qual_inspectionResult` | `positionName` | String | | No | | Q24, Q124, Q125, Q126 |
| 102 | `u_mes_qual_inspectionResult` | `imageControlledDocumentId` | String | | No | `u_mes_syst_controlledDocument._id` | Q125 |
| 103 | `u_mes_qual_inspectionResult` | `imageControlledDocumentName` | String | | No | display value of `u_mes_syst_controlledDocument` | Q125 |
| 104 | `u_mes_qual_inspectionResult` | `measurementCurveId` | String | | No | `u_mes_qual_measurementCurve._id` | Q127 |
| 105 | `u_mes_qual_inspectionResult` | `measurementCurveName` | String | | No | display value of `u_mes_qual_measurementCurve` | Q127 |
| 106 | `u_mes_qual_inspectionResult` | `analyticsModelId` | String | | No | `u_mes_syst_analyticsModel._id` | Q33, Q129 |
| 107 | `u_mes_qual_inspectionResult` | `analyticsModelName` | String | | No | display value of `u_mes_syst_analyticsModel` | Q33, Q129 |
| 108 | `u_mes_qual_inspectionResult` | `modelVersion` | String | | No | | Q33, Q129 |
| 109 | `u_mes_qual_inspectionResult` | `modelClass` | String | | No | e.g. OK, NOK, Low Confidence | Q33, Q129 |
| 110 | `u_mes_qual_inspectionResult` | `modelConfidence` | Decimal128 | | No | 0 to 1 | Q33, Q129 |
| 111 | `u_mes_qual_spcSample` | `reactionType` | String | | No | enumeration: Alert, Hold, Recheck, Stop Line | Q26 |
| 112 | `u_mes_qual_spcSample` | `qualityHoldId` | String | | No | `u_mes_qual_qualityHold._id` | Q26 |
| 113 | `u_mes_qual_spcSample` | `qualityHoldName` | String | | No | display value of `u_mes_qual_qualityHold` | Q26 |
| 114 | `u_mes_qual_spcSample` | `notificationId` | String | | No | `u_mes_syst_notification._id` | Q26 |
| 115 | `u_mes_qual_spcSample` | `notificationName` | String | | No | display value of `u_mes_syst_notification` | Q26 |
| 116 | `u_mes_qual_qualityHold` | `releaseReasonCodeId` | String | | No | `u_mes_perf_reasonCode._id` | Q2, Q29 |
| 117 | `u_mes_qual_qualityHold` | `releaseReasonCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q2, Q29 |
| 118 | `u_mes_qual_qualityHold` | `releaseElectronicSignatureId` | String | | No | `u_mes_syst_electronicSignature._id` | Q2, Q29 |
| 119 | `u_mes_qual_qualityHold` | `releaseElectronicSignatureName` | String | | No | display value of `u_mes_syst_electronicSignature` | Q2, Q29 |
| 120 | `u_mes_qual_reworkOrder` | `reasonCodeId` | String | | No | `u_mes_perf_reasonCode._id` | Q18, Q30 |
| 121 | `u_mes_qual_reworkOrder` | `reasonCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q18, Q30 |
| 122 | `u_mes_qual_reworkOrder` | `releasedById` | String | | No | `u_mes_mast_user._id` | Q30 |
| 123 | `u_mes_qual_reworkOrder` | `releasedBy` | String | | No | `u_mes_mast_user.fullName` | Q30 |
| 124 | `u_mes_qual_reworkOrder` | `releasedAt` | Date | Datetime | No | | Q30 |
| 125 | `u_mes_qual_scrapRecord` | `serialNumberId` | String | | No | `u_mes_trac_serialNumber._id` | Q19 |
| 126 | `u_mes_qual_scrapRecord` | `serialNumberName` | String | | No | display value of `u_mes_trac_serialNumber` | Q19 |
| 127 | `u_mes_qual_scrapRecord` | `dispositionTypeId` | String | | No | `u_mes_qual_dispositionType._id` | Q19 |
| 128 | `u_mes_qual_scrapRecord` | `dispositionTypeName` | String | | No | display value of `u_mes_qual_dispositionType` | Q19 |
| 129 | `u_mes_qual_audit` | `auditScheduleId` | String | | No | `u_mes_qual_auditSchedule._id` | Q34 |
| 130 | `u_mes_qual_audit` | `auditScheduleName` | String | | No | display value of `u_mes_qual_auditSchedule` | Q34 |
| 131 | `u_mes_qual_audit` | `dueDate` | Date | Date | No | | Q34 |
| 132 | `u_mes_qual_audit` | `isMissed` | Boolean | | Yes | | Q34 |
| 133 | `u_mes_qual_audit` | `escalationLevel` | Int32 | | Yes | 0 when not escalated | Q34 |
| 134 | `u_mes_qual_gauge` | `equipmentId` | String | | No | `u_mes_mast_equipment._id` | Q102 |
| 135 | `u_mes_qual_gauge` | `equipmentName` | String | | No | display value of `u_mes_mast_equipment` | Q102 |
| 136 | `u_mes_perf_processTag` | `areaId` | String | | No | `u_mes_mast_area._id` | Q96 |
| 137 | `u_mes_perf_processTag` | `areaName` | String | | No | display value of `u_mes_mast_area` | Q96 |
| 138 | `u_mes_perf_processTag` | `lineId` | String | | No | `u_mes_mast_line._id` | Q96 |
| 139 | `u_mes_perf_processTag` | `lineName` | String | | No | display value of `u_mes_mast_line` | Q96 |
| 140 | `u_mes_perf_processTag` | `workCenterId` | String | | No | `u_mes_mast_workCenter._id` | Q96 |
| 141 | `u_mes_perf_processTag` | `workCenterName` | String | | No | display value of `u_mes_mast_workCenter` | Q96 |
| 142 | `u_mes_perf_processReading` | `areaId` | String | | No | `u_mes_mast_area._id` | Q96 |
| 143 | `u_mes_perf_processReading` | `areaName` | String | | No | display value of `u_mes_mast_area` | Q96 |
| 144 | `u_mes_perf_processReading` | `shiftId` | String | | No | `u_mes_mast_shift._id` | Q96 |
| 145 | `u_mes_perf_processReading` | `shiftName` | String | | No | display value of `u_mes_mast_shift` | Q96 |
| 146 | `u_mes_perf_processReading` | `productionDate` | Date | Date | No | | Q96 |
| 147 | `u_mes_perf_alarm` | `alarmDefinitionId` | String | | No | `u_mes_perf_alarmDefinition._id` | Q68, Q69 |
| 148 | `u_mes_perf_alarm` | `alarmDefinitionName` | String | | No | display value of `u_mes_perf_alarmDefinition` | Q68, Q69 |
| 149 | `u_mes_perf_alarm` | `lineId` | String | | No | `u_mes_mast_line._id` | Q68 |
| 150 | `u_mes_perf_alarm` | `lineName` | String | | No | display value of `u_mes_mast_line` | Q68 |
| 151 | `u_mes_perf_alarm` | `workCenterId` | String | | No | `u_mes_mast_workCenter._id` | Q68 |
| 152 | `u_mes_perf_alarm` | `workCenterName` | String | | No | display value of `u_mes_mast_workCenter` | Q68 |
| 153 | `u_mes_perf_alarm` | `shiftId` | String | | No | `u_mes_mast_shift._id` | Q68 |
| 154 | `u_mes_perf_alarm` | `shiftName` | String | | No | display value of `u_mes_mast_shift` | Q68 |
| 155 | `u_mes_perf_alarm` | `productionDate` | Date | Date | No | | Q68 |
| 156 | `u_mes_perf_alarm` | `wipUnitId` | String | | No | `u_mes_plan_wipUnit._id` | Q68 |
| 157 | `u_mes_perf_alarm` | `wipUnitName` | String | | No | display value of `u_mes_plan_wipUnit` | Q68 |
| 158 | `u_mes_perf_alarm` | `blocksRestart` | Boolean | | Yes | copied from the alarm definition | Q69 |
| 159 | `u_mes_perf_alarm` | `restartAuthorizedById` | String | | No | `u_mes_mast_user._id` | Q69 |
| 160 | `u_mes_perf_alarm` | `restartAuthorizedBy` | String | | No | `u_mes_mast_user.fullName` | Q69 |
| 161 | `u_mes_perf_alarm` | `restartAuthorizedAt` | Date | Datetime | No | | Q69 |
| 162 | `u_mes_perf_alarm` | `closureReasonCodeId` | String | | No | `u_mes_perf_reasonCode._id` | Q69 |
| 163 | `u_mes_perf_alarm` | `closureReasonCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q69 |
| 164 | `u_mes_perf_alarm` | `escalationLevel` | Int32 | | Yes | 0 when not escalated | Q69 |
| 165 | `u_mes_perf_downtimeEvent` | `captureSource` | String | | Yes | enumeration: Equipment Signal, Operator Entry, Andon | Q36 |
| 166 | `u_mes_perf_downtimeEvent` | `equipmentStateId` | String | | No | `u_mes_perf_equipmentState._id` | Q36 |
| 167 | `u_mes_perf_downtimeEvent` | `equipmentStateName` | String | | No | display value of `u_mes_perf_equipmentState` | Q36 |
| 168 | `u_mes_perf_downtimeEvent` | `productVariantId` | String | | No | `u_mes_prod_productVariant._id` | Q44 |
| 169 | `u_mes_perf_downtimeEvent` | `productVariantName` | String | | No | display value of `u_mes_prod_productVariant` | Q44 |
| 170 | `u_mes_perf_downtimeEvent` | `capaId` | String | | No | `u_mes_qual_capa._id` | Q44 |
| 171 | `u_mes_perf_downtimeEvent` | `capaName` | String | | No | display value of `u_mes_qual_capa` | Q44 |
| 172 | `u_mes_perf_torqueResult` | `curveEnvelopeId` | String | | No | `u_mes_qual_curveEnvelope._id` | Q127 |
| 173 | `u_mes_perf_torqueResult` | `curveEnvelopeName` | String | | No | display value of `u_mes_qual_curveEnvelope` | Q127 |
| 174 | `u_mes_perf_torqueResult` | `measurementCurveId` | String | | No | `u_mes_qual_measurementCurve._id` | Q127 |
| 175 | `u_mes_perf_torqueResult` | `measurementCurveName` | String | | No | display value of `u_mes_qual_measurementCurve` | Q127 |
| 176 | `u_mes_perf_torqueResult` | `envelopeResult` | String | | No | enumeration: OK, NOK | Q127 |
| 177 | `u_mes_perf_leakTestResult` | `measurementCurveId` | String | | No | `u_mes_qual_measurementCurve._id` | Q127 |
| 178 | `u_mes_perf_leakTestResult` | `measurementCurveName` | String | | No | display value of `u_mes_qual_measurementCurve` | Q127 |
| 179 | `u_mes_maint_maintenanceWorkOrder` | `shiftId` | String | | No | `u_mes_mast_shift._id` | Q49 |
| 180 | `u_mes_maint_maintenanceWorkOrder` | `shiftName` | String | | No | display value of `u_mes_mast_shift` | Q49 |
| 181 | `u_mes_maint_maintenanceWorkOrder` | `rootCauseCodeId` | String | | No | `u_mes_perf_reasonCode._id` (reasonType Root Cause) | Q51 |
| 182 | `u_mes_maint_maintenanceWorkOrder` | `rootCauseCodeName` | String | | No | display value of `u_mes_perf_reasonCode` | Q51 |
| 183 | `u_mes_maint_maintenanceWorkOrder` | `closureApprovedById` | String | | No | `u_mes_mast_user._id` | Q51 |
| 184 | `u_mes_maint_maintenanceWorkOrder` | `closureApprovedBy` | String | | No | `u_mes_mast_user.fullName` | Q51 |
| 185 | `u_mes_maint_maintenanceWorkOrder` | `closureApprovedAt` | Date | Datetime | No | | Q51 |
| 186 | `u_mes_maint_maintenanceWorkOrder` | `andonEventId` | String | | No | `u_mes_plan_andonEvent._id` | Q55 |
| 187 | `u_mes_maint_maintenanceWorkOrder` | `andonEventName` | String | | No | display value of `u_mes_plan_andonEvent` | Q55 |
| 188 | `u_mes_maint_maintenanceWorkOrder` | `priorityScore` | Decimal128 | | No | | Q54 |
| 189 | `u_mes_maint_maintenanceWorkOrder` | `schedulingSource` | String | | Yes | enumeration: Manual, Rule, Model | Q54 |
| 190 | `u_mes_maint_maintenanceWorkOrder` | `slaResponseDueAt` | Date | Datetime | No | | Q54, Q56 |
| 191 | `u_mes_maint_maintenanceWorkOrder` | `slaRepairDueAt` | Date | Datetime | No | | Q54, Q56 |
| 192 | `u_mes_maint_tool` | `blockAtLifeLimit` | Boolean | | Yes | | Q101 |
| 193 | `u_mes_maint_tool` | `lastCertifiedAt` | Date | Datetime | No | | Q106 |
| 194 | `u_mes_maint_tool` | `certificationDueDate` | Date | Date | No | | Q106 |
| 195 | `u_mes_maint_tool` | `certificateControlledDocumentId` | String | | No | `u_mes_syst_controlledDocument._id` | Q106 |
| 196 | `u_mes_maint_tool` | `certificateControlledDocumentName` | String | | No | display value of `u_mes_syst_controlledDocument` | Q106 |
| 197 | `u_mes_maint_toolLifeRecord` | `workCenterId` | String | | No | `u_mes_mast_workCenter._id` | Q100 |
| 198 | `u_mes_maint_toolLifeRecord` | `workCenterName` | String | | No | display value of `u_mes_mast_workCenter` | Q100 |
| 199 | `u_mes_maint_toolLifeRecord` | `itemId` | String | | No | `u_mes_prod_item._id` | Q100 |
| 200 | `u_mes_maint_toolLifeRecord` | `itemName` | String | | No | display value of `u_mes_prod_item` | Q100 |
| 201 | `u_mes_maint_toolLifeRecord` | `operationExecutionId` | String | | No | `u_mes_plan_operationExecution._id` | Q100 |
| 202 | `u_mes_maint_toolLifeRecord` | `operationExecutionName` | String | | No | display value of `u_mes_plan_operationExecution` | Q100 |
| 203 | `u_mes_syst_notification` | `alertRuleId` | String | | No | `u_mes_syst_alertRule._id` | Q42, Q43 |
| 204 | `u_mes_syst_notification` | `alertRuleName` | String | | No | display value of `u_mes_syst_alertRule` | Q42, Q43 |
| 205 | `u_mes_syst_notification` | `escalationRuleId` | String | | No | `u_mes_syst_escalationRule._id` | Q9 |
| 206 | `u_mes_syst_notification` | `escalationRuleName` | String | | No | display value of `u_mes_syst_escalationRule` | Q9 |
| 207 | `u_mes_syst_notification` | `responseDueAt` | Date | Datetime | No | | Q9 |
| 208 | `u_mes_syst_notification` | `resolvedAt` | Date | Datetime | No | | Q9 |
| 209 | `u_mes_syst_notification` | `resolvedById` | String | | No | `u_mes_mast_user._id` | Q9 |
| 210 | `u_mes_syst_notification` | `resolvedBy` | String | | No | `u_mes_mast_user.fullName` | Q9 |
| 211 | `u_mes_syst_notification` | `interlockEventId` | String | | No | `u_mes_plan_interlockEvent._id` | Q9 |
| 212 | `u_mes_syst_notification` | `interlockEventName` | String | | No | display value of `u_mes_plan_interlockEvent` | Q9 |

Totals: 212 new keys on 38 existing collections. No key is added to an ehs collection.

Note on `u_mes_syst_notification`: it already carries dedicated pairs for `andonEventId`, `alarmId` and `nonconformanceId` besides the polymorphic `relatedCollectionName` / `relatedEntityId`. The new `interlockEventId` pair follows that existing pattern; if the owner prefers, interlock notifications can use only the polymorphic keys and keys 211–212 can be dropped.

## 7. Value-list, status and master-data changes

### 7.1 Enumeration values to add to existing keys (`u_mes_syst_enumerationValue`)

| Collection | Key | Values to add | Questions |
|---|---|---|---|
| `u_mes_perf_reasonCode` | `reasonType` | Hold, Hold Release, Interlock Override, Rework, Root Cause, Alarm Closure, Exposure Reset | X5 |
| `u_mes_prod_recipe` | `recipeType` | Press-Fit, Dispensing, Vision, Laser Marking (also closes the existing Schema Observation on missing press and vision values) | Q57, Q122, Q129 |
| `u_mes_perf_processTag` | `tagClass` | Environment | Q96 |
| `u_mes_plan_stepCompletion` | `deviceSource` | AR Headset | Q95 |
| `u_mes_qual_gaugeCalibration` | `calibrationType` | Automatic Closed Loop | Q108 |
| `u_mes_syst_integrationConnector` | `targetSystem` | Cloud Data Platform | Q110 |
| `u_mes_syst_integrationConnectorFunction` and `u_mes_syst_erpMessage` | `direction` | Publish | Q110 |
| `u_mes_qual_audit` | `auditType` | Layered Process Audit (if not already present) | Q34 |
| `u_mes_maint_tool` | `toolClass` | Fixture, Dispensing Nozzle, Nutrunner Socket (if not already present) | Q100, Q106 |

All new enumeration keys listed in sections 5 and 6 (for example `captureMethod`, `fourMCategory`, `ruleType`, `transactionPoint`, `curveType`) are added to `u_mes_syst_enumerationValue` with their values as listed there.

### 7.2 Master-data rows to add

| Collection | Rows | Questions |
|---|---|---|
| `u_mes_syst_documentType` | Inspection Image, Golden Image, Reference Curve, AR Content, Analytics Model Card, Simulation Report, Backup Test Report | Q58, Q94, Q125, Q129, X10, X11, Q118 |
| `u_mes_syst_notificationType` | Interlock Block, Escalation, KPI Alert, Model Prediction, Missed Audit | X1, X2, X3, X10, Q34 |
| `u_mes_perf_lossCategory` | no change (existing six-big-loss rows cover the Pareto) | Q37 |
| `u_mes_mast_permission` | Override Interlock, Authorise Restart, Release Hold, Approve Recipe Release, Approve Maintenance Closure, Edit Locked Record | X1, X4, Q69, Q51, X12 |
| `u_mes_syst_systemConfiguration` | `perf.microStopThresholdMinutes` (number, 15 per the questionnaire), `plan.sessionTimeoutMinutes`, `qual.spcSubgroupSizeDefault` (5) | Q39, Q80, Q26 |

### 7.3 Status definitions and transitions

New entity collections bring their status values (section 5) into `u_mes_syst_statusDefinition`, with their transitions in `u_mes_syst_statusTransition`. No existing status value is removed. Proposed additions to existing status models:

| Collection | Change | Questions |
|---|---|---|
| `u_mes_plan_productionOrder` | none to the values (On Hold already exists); transitions In Progress → On Hold and On Hold → In Progress get `requiresReason` = true and `requiresSignature` = true | Q1, Q2 |
| `u_mes_maint_maintenanceWorkOrder` | transition Completed → Closed gets `requiresSignature` = true | Q51 |
| `u_mes_qual_reworkOrder` | transition Awaiting Reinspection → Completed gets `requiresSignature` = true | Q30 |
| `u_mes_prod_recipe` | transition In Preparation → Released gets `requiresSignature` = true | Q61, Q62 |

## 8. Proposed governance entries (not recorded)

Nothing has been written to `00_governance`. If the owner accepts the proposals, the following entries would be added.

| Proposed entry | Text |
|---|---|
| D036 | Interlocks are configured in `u_mes_syst_interlockRule` and every block, override and clearance is recorded in `u_mes_plan_interlockEvent`. Overrides need a reason code of reasonType Interlock Override and, when the rule says so, an electronic signature. |
| D037 | Status transitions are authorised by role through `u_mes_syst_statusTransitionRole`; `requiresReason` and `requiresSignature` on `u_mes_syst_statusTransition` are enforced. |
| D038 | Multi-position characteristics use `u_mes_qual_characteristicPosition`; curves use `u_mes_qual_curveEnvelope` / `u_mes_qual_measurementCurve`, and curve points are stored in the time-series collection `u_mes_qual_measurementCurvePoint` (Telemetry). |
| D039 | Program traceability: every operation execution and as-built operation stores `recipeVersion` and `recipeChecksum`; every program load is recorded in `u_mes_plan_recipeDownload`. |
| D040 | AI / ML and rule models are registered in `u_mes_syst_analyticsModel`; every prediction is stored in `u_mes_syst_modelPrediction`; inspection results classified by a model carry the model ID and version. |
| D041 | Edit, lock and retention behaviour per collection is configured in `u_mes_syst_recordPolicy`; transaction data is never physically deleted. |
| D042 | New collections are numbered from 1300 upward in the order they are added; existing collection numbers never change. |
| A016 | The questionnaire MES_ExternalRequirement_01 describes a switch product; its requirements are adopted as generic MES capabilities and mapped to the caliper reference process (section 2.1 of the impact analysis). |
| A017 | Target maturity for the schema is Level 3 (system-enforced) with Level 4 (integrated) data links; Level 5 is supported only through the analytics model registry and simulation studies. |

Standard sections that would need text updates: `data_modeling_standard.md` (new section on interlock and override records; time-series rule for curve points), `schema_review_checklist.md` (checks that every enforced rule has a configuration collection and an evidence record), `collection_type_matrix` (44 new rows with Type and Label as in section 3.2), `Folder_Guide.md` section 3 (this document's location).

## 9. Implementation order and effect on the model

### 9.1 Suggested order

| Step | Content | Reason |
|---|---|---|
| 1 | X5 reason types, X4 `u_mes_syst_statusTransitionRole`, X12 `u_mes_syst_recordPolicy`, enumeration and master rows of section 7 | No dependencies; needed by every later step |
| 2 | X1 `u_mes_syst_interlockRule`, `u_mes_plan_interlockEvent`; X2 `u_mes_syst_escalationRule`, `u_mes_syst_escalationRuleLevel`; X3 `u_mes_syst_alertRule`; key additions on `u_mes_syst_notification` | Core enforcement framework used by 40 questions |
| 3 | X7 `u_mes_plan_operatorSession`, X6 `u_mes_plan_documentAcknowledgement`, X9 `u_mes_plan_recipeDownload`, `u_mes_plan_setupVerification`, `u_mes_plan_setupVerificationItem`, prod relationships 1301–1304, key additions on `u_mes_plan_operationExecution` | Execution-level evidence |
| 4 | X8 quality collections 1316–1321, `u_mes_qual_auditSchedule`, `u_mes_qual_inspectionPlanProductVariant`, quality key additions | Quality data depth |
| 5 | Material (1311–1313, 1343), traceability (1314–1315), maintenance (1328–1331), performance (1324–1327) | Module-specific additions |
| 6 | X10 `u_mes_syst_analyticsModel`, `u_mes_syst_modelPrediction`; X11 `u_mes_syst_simulationStudy`; `u_mes_syst_savedView`; optional `u_mes_syst_backupRun` | Advanced (Level 4/5) items |
| 7 | Regenerate specifications, validators, indexes, 10 sample documents per new collection, field lists, register, type matrix and validation reports | Keeps every generated file consistent |

### 9.2 Effect on the counts (if all proposals are accepted)

| Measure | Today | Change | After |
|---|---|---|---|
| Collections | 299 | +44 | 343 |
| Entity / Child / Relationship / Value-list | 148 / 76 / 67 / 8 | +30 / +6 / +8 / 0 | 178 / 82 / 75 / 8 |
| Master / Transaction / Reports / Telemetry / Audit Trail | 162 / 122 / 7 / 4 / 4 | +21 / +17 / +5 / +1 / 0 | 183 / 139 / 12 / 5 / 4 |
| Keys | 6,058 | +1,115 in new collections, +212 in existing collections | 7,385 |
| Sample documents (10 per collection) | 2,990 | +440 | 3,430 |

| Module | Code | Collections today | New | After |
|---|---|---|---|---|
| Master Data Management | mast | 56 | 1 | 57 |
| Product Definition | prod | 45 | 4 | 49 |
| Planning and Execution | plan | 36 | 6 | 42 |
| Material Management | matl | 22 | 4 | 26 |
| Traceability | trac | 7 | 2 | 9 |
| Quality Management | qual | 69 | 8 | 77 |
| Performance Management | perf | 17 | 4 | 21 |
| Tooling And Maintenance | maint | 14 | 4 | 18 |
| System and Integration | syst | 27 | 11 | 38 |
| Environment Health and Safety | ehs | 6 | 0 | 6 |
| **Total** | | **299** | **44** | **343** |

### 9.3 Decisions needed from the owner

1. Accept, reject or modify each new collection in section 3.2 (the optional ones are `u_mes_syst_backupRun` and `u_mes_matl_storageLocationAllowedItem`).
2. Confirm the classification of `u_mes_plan_interlockEvent` as Transaction (alternative: Audit Trail).
3. Confirm that the advanced (Level 5) questions should be supported only through the generic model registry and simulation study, and not through algorithm-specific collections.
4. Confirm the switch-to-caliper mapping in section 2.1, in particular that Q121 (SMT), Q124 (LED illumination) and Q128 (haptic) stay out of the caliper sample data.
