# u_mes_perf_reasonCode

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Reason tree (up to 4 levels) for downtime, scrap, hold and andon with planned / unplanned category |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 23 (19 required, 4 may be null) |
| Estimated volume per year | 200-600 |
| Storage | standard |

## Structure

Flat entity collection: one document per reason code, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1203000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MECH-GDC-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the reason code; used as its display value in other collections | `"Die ejector pin stuck"` |  |
| 6 | reasonType | String | - | Yes | Reason type | `"Downtime"` | Downtime; Scrap; Hold; Andon; Changeover Loss |
| 7 | level | Int32 | - | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 8 | parentReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: parent reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 9 | parentReasonCodeName | String | - | No (null allowed) | Display value of parentReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 10 | pathText | String | - | Yes | Full path of the reason from level 1 to this level | `"Unplanned > Mechanical > Clamping > Clamp cylinder failure"` |  |
| 11 | reasonCategoryId | String | - | Yes | Reference to u_mes_perf_reasonCategory._id | `"1287000000000001"` | Reference: u_mes_perf_reasonCategory._id |
| 12 | reasonCategoryName | String | - | Yes | Display value of reasonCategoryId, copied from u_mes_perf_reasonCategory.name | `"Mechanical"` |  |
| 13 | lossCategoryId | String | - | Yes | Reference to u_mes_perf_lossCategory._id | `"1286000000000001"` | Reference: u_mes_perf_lossCategory._id |
| 14 | lossCategoryName | String | - | Yes | Display value of lossCategoryId, copied from u_mes_perf_lossCategory.name | `"Breakdown"` |  |
| 15 | oeeImpact | String | - | Yes | OEE impact | `"Availability"` | Availability; Performance; Quality; None |
| 16 | isPlanned | Boolean | - | Yes | True when the record is planned | `false` |  |
| 17 | responsibleDepartmentId | String | - | No (null allowed) | Reference to u_mes_mast_department._id: responsible department | `"1256000000000001"` | Reference: u_mes_mast_department._id |
| 18 | responsibleDepartmentName | String | - | No (null allowed) | Display value of responsibleDepartmentId, copied from u_mes_mast_department.name | `"Production"` |  |
| 19 | requiresComment | Boolean | - | Yes | True when comment is required | `true` |  |
| 20 | requiresMaintenanceWorkOrder | Boolean | - | Yes | True when maintenance work order is required | `true` |  |
| 21 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentReasonCodeId: 1 }` | No | Look-up of documents by parent reason code |
| 4 | `{ reasonCategoryId: 1 }` | No | Look-up of documents by reason category |
| 5 | `{ lossCategoryId: 1 }` | No | Look-up of documents by loss category |
| 6 | `{ responsibleDepartmentId: 1 }` | No | Look-up of documents by responsible department |

## Referenced by

u_mes_qual_qualityHold, u_mes_perf_reasonCode, u_mes_perf_downtimeEvent, u_mes_perf_oeeRecordLoss, u_mes_maint_maintenanceWorkOrder, u_mes_plan_andonEvent.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_reasonCode.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_reasonCode.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_reasonCode.js
