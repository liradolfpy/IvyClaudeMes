# u_mes_maint_toolLifeRecord

| Property | Value |
|---|---|
| Module | ToolingAndMaintenance (maint) |
| Purpose | Tool mount / dismount / usage / regrind events with shots or cycles consumed |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (23 required, 17 may be null) |
| Estimated volume per year | ~60,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per tool life record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1228000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"TLR-2026-000160"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | toolId | String | - | Yes | Reference to u_mes_maint_tool._id | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 7 | toolName | String | - | Yes | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 8 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 9 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 10 | eventType | String | - | Yes | Event type | `"Regrind"` | Mounted; Usage; Dismounted; Regrind; Maintenance; Scrapped |
| 11 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 12 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 13 | eventAt | Date | Datetime | Yes | Event date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:10.000+0000")` |  |
| 14 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 15 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | cyclesThisEvent | Int64 | - | Yes | Cycles this event | `NumberLong("480")` |  |
| 17 | lifeUsedBefore | Int64 | - | Yes | Life used before | `NumberLong("60760")` |  |
| 18 | lifeUsedAfter | Int64 | - | Yes | Life used after | `NumberLong("61240")` |  |
| 19 | lifeRemaining | Int64 | - | Yes | Life remaining | `NumberLong("18400")` |  |
| 20 | regrindNo | Int32 | - | No (null allowed) | Regrind number | `null` |  |
| 21 | conditionOnRemoval | String | - | No (null allowed) | Condition on removal | `"Normal wear"` |  |
| 22 | removalReason | String | - | No (null allowed) | Removal reason | `"Life limit reached"` |  |
| 23 | measuredWearMm | Decimal128 | - | No (null allowed) | Measured wear (mm) | `NumberDecimal("0.12")` |  |
| 24 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `null` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 25 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `null` |  |
| 26 | remarks | String | - | No (null allowed) | Remarks of the tool life record | `"No abnormality observed"` |  |
| 27 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 28 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 29 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 30 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 31 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `null` | Reference: u_mes_plan_operationExecution._id |
| 32 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `null` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:10.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ maintenanceWorkOrderId: 1 }` | No | Look-up of documents by maintenance work order |
| 7 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 8 | `{ siteId: 1, eventAt: -1 }` | No | Time-ordered lists and reports by event at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_toolLifeRecord.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_toolLifeRecord.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_toolLifeRecord.js
