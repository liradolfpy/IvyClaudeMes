# u_mes_maint_maintenanceWorkOrderTask

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | One document per task of a maintenance work order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_maint_maintenanceWorkOrder |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 26 (17 required, 9 may be null) |

## Structure

Child collection. The parent maintenance work order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenanceWorkOrderId and maintenanceWorkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1328000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MWO-2026-000383-T01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | maintenanceWorkOrderId | String | - | Yes | Reference to u_mes_maint_maintenanceWorkOrder._id: the parent document this one belongs to | `"1220000000000008"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - | Yes | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Leak tester inlet seal replacement"` |  |
| 8 | taskNo | Int32 | - | Yes | Task number (copied from the plan task) | `NumberInt(10)` |  |
| 9 | maintenancePlanTaskId | String | - | No (null allowed) | Reference to u_mes_maint_maintenancePlanTask._id | `null` | Reference: u_mes_maint_maintenancePlanTask._id |
| 10 | maintenancePlanTaskName | String | - | No (null allowed) | Display value of maintenancePlanTaskId, copied from u_mes_maint_maintenancePlanTask.recordNo | `null` |  |
| 11 | description | String | - | Yes | Task text | `"Remove and inspect the inlet test seal set"` |  |
| 12 | result | String | - | Yes | Result | `"Not Done"` | Done OK; Done Not OK; Not Applicable; Not Done |
| 13 | measuredValue | Decimal128 | - | No (null allowed) | Measured value, when the task asks for one | `null` |  |
| 14 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `null` | Reference: u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `null` |  |
| 16 | comment | String | - | No (null allowed) | Comment | `null` |  |
| 17 | completedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'completed' | `null` | Reference: u_mes_mast_user._id |
| 18 | completedBy | String | - | No (null allowed) | Display name of the user in completedById, copied from u_mes_mast_user.fullName | `null` |  |
| 19 | completedAt | Date | Datetime | No (null allowed) | Completion time | `null` |  |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 21 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-22T16:02:00.000+0000")` |  |
| 22 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 23 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 24 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-22T16:02:00.000+0000")` |  |
| 25 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 26 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenanceWorkOrderId: 1, taskNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ maintenancePlanTaskId: 1 }` | No | Look-up of lines by maintenance plan task |
| 3 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrderTask.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrderTask.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrderTask.js
