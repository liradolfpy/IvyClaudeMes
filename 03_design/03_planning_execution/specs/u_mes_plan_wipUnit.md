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
| Keys | 47 (30 required, 17 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 10 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 12 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"1131000000000001"` | Reference: u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258A00184"` |  |
| 14 | bodyLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: body lot | `"1096000000000004"` | Reference: u_mes_plan_lot._id |
| 15 | bodyLotName | String | - | No (null allowed) | Display value of bodyLotId, copied from u_mes_plan_lot.recordNo | `"L260917-ANO-001"` |  |
| 16 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 17 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 18 | currentStepNo | Int32 | - | Yes | Current step number | `NumberInt(60)` |  |
| 19 | currentOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: current operation | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 20 | currentOperationName | String | - | Yes | Display value of currentOperationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 21 | currentWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: current work center | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 22 | currentWorkCenterName | String | - | Yes | Display value of currentWorkCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 23 | qualityStatus | String | - | Yes | Quality status | `"On Hold"` | Released; Under Inspection; On Hold; Rejected |
| 24 | onHold | Boolean | - | Yes | True when: on hold | `true` |  |
| 25 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `"1172000000000001"` | Reference: u_mes_qual_qualityHold._id |
| 26 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000021"` |  |
| 27 | reworkCount | Int32 | - | Yes | Rework count | `NumberInt(0)` |  |
| 28 | createdAtOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: created at operation | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 29 | createdAtOperationName | String | - | No (null allowed) | Display value of createdAtOperationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 30 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 31 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 32 | lastOperationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id: last operation execution | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 33 | lastOperationExecutionName | String | - | No (null allowed) | Display value of lastOperationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 34 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 35 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 36 | bodyCavityNo | Int32 | - | Yes | Body cavity number | `NumberInt(1)` |  |
| 37 | castDateCode | String | - | Yes | Date, shift and cavity code cast into the body | `"26258A1"` |  |
| 38 | scrappedAt | Date | Datetime | No (null allowed) | Date and time when the record was scrapped. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 39 | shippedAt | Date | Datetime | No (null allowed) | Date and time when the record was shipped. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 40 | status | String | - | Yes | Primary lifecycle state of the document | `"On Hold"` | Created; In Process; On Hold; In Rework; Completed; Packed; Shipped; Scrapped |
| 41 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 42 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 43 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 45 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 46 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 47 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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

u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_wipUnitCompletedStep, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_trac_serialNumber, u_mes_trac_genealogyLink, u_mes_trac_asBuiltRecord, u_mes_qual_inspectionResult, u_mes_qual_reworkOrderWipUnit, u_mes_qual_scrapRecord, u_mes_perf_torqueResult, u_mes_perf_leakTestResult.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_wipUnit.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_wipUnit.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_wipUnit.js
