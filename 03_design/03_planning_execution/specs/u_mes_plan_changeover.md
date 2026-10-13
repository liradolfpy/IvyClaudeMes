# u_mes_plan_changeover

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Changeover from one item / variant to another: planned vs actual duration, checklist, first-off approval |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (27 required, 13 may be null) |
| Estimated volume per year | ~3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per changeover, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with changeoverId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_changeoverStep | Child | step |
| u_mes_plan_changeoverRemovedTool | Relationship | removed tool |
| u_mes_plan_changeoverInstalledTool | Relationship | installed tool |
| u_mes_plan_changeoverPerformedByUser | Relationship | performed by user |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1102000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CHG-2026-000307"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 6 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 7 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 9 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 11 | fromProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: from production order | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 12 | fromProductionOrderName | String | - | No (null allowed) | Display value of fromProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 13 | toProductionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id: to production order | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 14 | toProductionOrderName | String | - | Yes | Display value of toProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 15 | fromItemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id: from item | `"1043000000000002"` | Reference: u_mes_prod_item._id |
| 16 | fromItemName | String | - | No (null allowed) | Display value of fromItemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, RH"` |  |
| 17 | toItemId | String | - | Yes | Reference to u_mes_prod_item._id: to item | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 18 | toItemName | String | - | Yes | Display value of toItemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 19 | changeoverType | String | - | Yes | Changeover type | `"Variant Change"` | Variant Change; Item Change; Tool Change; Die Change |
| 20 | plannedStartAt | Date | Datetime | Yes | Planned start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 21 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 22 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 23 | plannedMinutes | Int32 | - | Yes | Planned (minutes) | `NumberInt(20)` |  |
| 24 | actualMinutes | Int32 | - | Yes | Actual (minutes) | `NumberInt(27)` |  |
| 25 | recipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 26 | recipeName | String | - | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 27 | firstOffCheckSheetResultId | String | - | Yes | Reference to u_mes_qual_checkSheetResult._id: first off check sheet result | `"1148000000000001"` | Reference: u_mes_qual_checkSheetResult._id |
| 28 | firstOffCheckSheetResultName | String | - | Yes | Display value of firstOffCheckSheetResultId, copied from u_mes_qual_checkSheetResult.recordNo | `"CKR-2026-000479"` |  |
| 29 | firstOffApprovedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'first off approved' | `null` | Reference: u_mes_mast_user._id |
| 30 | firstOffApprovedBy | String | - | No (null allowed) | Display name of the user in firstOffApprovedById, copied from u_mes_mast_user.fullName | `null` |  |
| 31 | firstOffApprovedAt | Date | Datetime | No (null allowed) | First off approved date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 32 | lossReason | String | - | No (null allowed) | Loss reason | `"Socket for RH variant not at point of use"` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; In Progress; Awaiting First Off Approval; Completed |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, In Progress, Awaiting First Off Approval, Completed. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ fromProductionOrderId: 1 }` | No | Look-up of documents by from production order |
| 7 | `{ toProductionOrderId: 1 }` | No | Look-up of documents by to production order |
| 8 | `{ siteId: 1, plannedStartAt: -1 }` | No | Time-ordered lists and reports by planned start at |

## Referenced by

u_mes_plan_changeoverStep, u_mes_plan_changeoverRemovedTool, u_mes_plan_changeoverInstalledTool, u_mes_plan_changeoverPerformedByUser, u_mes_plan_setupVerification, u_mes_plan_lineClearance.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_changeover.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_changeover.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_changeover.js
