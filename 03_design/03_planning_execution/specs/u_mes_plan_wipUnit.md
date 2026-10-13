# u_mes_plan_wipUnit

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Serialised unit in production (shop-floor control number): current operation, status, quality state |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 48 (29 required, 19 may be null) |
| Estimated volume per year | ~720,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per wip unit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with wipUnitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_wipUnitCompletedStep | Value list | completed step |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1094000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"U260915A0184"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 11 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 13 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"1131000000000001"` | Reference: u_mes_trac_serialNumber._id |
| 14 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258A00184"` |  |
| 15 | bodyLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: body lot | `"1096000000000004"` | Reference: u_mes_plan_lot._id |
| 16 | bodyLotName | String | - | No (null allowed) | Display value of bodyLotId, copied from u_mes_plan_lot.recordNo | `"L260917-ANO-001"` |  |
| 17 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 18 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 19 | currentStepNo | Int32 | - | Yes | Current step number | `NumberInt(60)` |  |
| 20 | currentOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: current operation | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 21 | currentOperationName | String | - | Yes | Display value of currentOperationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 22 | currentWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: current work center | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 23 | currentWorkCenterName | String | - | Yes | Display value of currentWorkCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 24 | qualityStatus | String | - | Yes | Quality status | `"On Hold"` | Released; Under Inspection; On Hold; Rejected |
| 25 | onHold | Boolean | - | Yes | True when: on hold | `true` |  |
| 26 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `"1172000000000001"` | Reference: u_mes_qual_qualityHold._id |
| 27 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000021"` |  |
| 28 | reworkCount | Int32 | - | Yes | Rework count | `NumberInt(0)` |  |
| 29 | createdAtOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: created at operation | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 30 | createdAtOperationName | String | - | No (null allowed) | Display value of createdAtOperationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 31 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 32 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 33 | lastOperationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id: last operation execution | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 34 | lastOperationExecutionName | String | - | No (null allowed) | Display value of lastOperationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 35 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 36 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 37 | bodyCavityNo | Int32 | - | No (null allowed) | Body cavity number | `NumberInt(1)` |  |
| 38 | castDateCode | String | - | No (null allowed) | Date, shift and cavity code cast into the body | `"26258A1"` |  |
| 39 | scrappedAt | Date | Datetime | No (null allowed) | Date and time when the record was scrapped. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 40 | shippedAt | Date | Datetime | No (null allowed) | Date and time when the record was shipped. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 41 | status | String | - | Yes | Primary lifecycle state of the document | `"On Hold"` | Created; In Process; On Hold; In Rework; Completed; Packed; Shipped; Scrapped |
| 42 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 43 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 44 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 45 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 46 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 47 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 48 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Created, In Process, On Hold, In Rework, Completed, Packed, Shipped, Scrapped. Initial state: Created. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 7 | `{ bodyLotId: 1 }` | No | Look-up of documents by body lot |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_wipUnitCompletedStep, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_trac_serialNumber, u_mes_trac_genealogyLink, u_mes_trac_asBuiltRecord, u_mes_qual_inspectionResult, u_mes_qual_reworkOrderWipUnit, u_mes_qual_scrapRecord, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_plan_interlockEvent, u_mes_qual_measurementCurve, u_mes_qual_defectRecord.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_wipUnit.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_wipUnit.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_wipUnit.js
