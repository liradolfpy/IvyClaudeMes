# u_mes_exe_changeover

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Changeover from one item / variant to another: planned vs actual duration, checklist, first-off approval |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | CHG-<recordNo> |
| Display value used by references | recordNo |
| Keys | 40 (27 required, 13 may be null) |
| Estimated volume per year | ~3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per changeover, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with changeoverId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_exe_changeoverStep | Child | step |
| u_mes_exe_changeoverRemovedTool | Relationship | removed tool |
| u_mes_exe_changeoverInstalledTool | Relationship | installed tool |
| u_mes_exe_changeoverPerformedByUser | Relationship | performed by user |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CHG-<recordNo> | `"CHG-20260930-ASY-01-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260930-ASY-01-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 6 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 7 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 8 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 9 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 10 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 11 | fromProductionOrderId | String | No (null allowed) | Reference to u_mes_exe_productionOrder._id: from production order | `"PO-1000409"` | Reference: u_mes_exe_productionOrder._id |
| 12 | fromProductionOrderName | String | No (null allowed) | Display value of fromProductionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000409"` |  |
| 13 | toProductionOrderId | String | Yes | Reference to u_mes_exe_productionOrder._id: to production order | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 14 | toProductionOrderName | String | Yes | Display value of toProductionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 15 | fromItemId | String | No (null allowed) | Reference to u_mes_prd_item._id: from item | `"ITM-5110-30-0010"` | Reference: u_mes_prd_item._id |
| 16 | fromItemName | String | No (null allowed) | Display value of fromItemId, copied from u_mes_prd_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 17 | toItemId | String | Yes | Reference to u_mes_prd_item._id: to item | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 18 | toItemName | String | Yes | Display value of toItemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 19 | changeoverType | String | Yes | Changeover type | `"Variant Change"` | Variant Change; Item Change; Tool Change; Die Change |
| 20 | plannedStartAt | Date | Yes | Planned start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 21 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 22 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 23 | plannedMinutes | Int32 | Yes | Planned (minutes) | `NumberInt(20)` |  |
| 24 | actualMinutes | Int32 | Yes | Actual (minutes) | `NumberInt(27)` |  |
| 25 | recipeId | String | No (null allowed) | Reference to u_mes_prd_recipe._id | `"RCP-TRQ-PRG-07"` | Reference: u_mes_prd_recipe._id |
| 26 | recipeName | String | No (null allowed) | Display value of recipeId, copied from u_mes_prd_recipe.name | `"Bleed screw M10 torque program"` |  |
| 27 | firstOffCheckSheetResultId | String | Yes | Reference to u_mes_qlt_checkSheetResult._id: first off check sheet result | `"CKR-20260929-A-TRQ-01"` | Reference: u_mes_qlt_checkSheetResult._id |
| 28 | firstOffCheckSheetResultName | String | Yes | Display value of firstOffCheckSheetResultId, copied from u_mes_qlt_checkSheetResult.recordNo | `"20260929-A-TRQ-01"` |  |
| 29 | firstOffApprovedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'first off approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 30 | firstOffApprovedBy | String | No (null allowed) | Display name of the user in firstOffApprovedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 31 | firstOffApprovedAt | Date | No (null allowed) | First off approved date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 32 | lossReason | String | No (null allowed) | Loss reason | `"Socket for RH variant not at point of use"` |  |
| 33 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Planned; In Progress; Awaiting First Off Approval; Completed |
| 34 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 36 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 37 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 38 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 39 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 40 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, In Progress, Awaiting First Off Approval, Completed. Initial state: Planned. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_exe_changeoverStep, u_mes_exe_changeoverRemovedTool, u_mes_exe_changeoverInstalledTool, u_mes_exe_changeoverPerformedByUser.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_changeover.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_changeover.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_changeover.js
