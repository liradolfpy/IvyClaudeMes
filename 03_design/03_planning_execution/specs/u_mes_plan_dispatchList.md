# u_mes_plan_dispatchList

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Prioritised work queue per work centre shown to the operator |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (20 required, 3 may be null) |
| Estimated volume per year | ~100,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per dispatch list, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with dispatchListId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_dispatchListEntry | Child | entry |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1088000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DSP-2026-000121"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 8 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 9 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 10 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 11 | generatedAt | Date | Datetime | Yes | Date and time when the record was generated. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 12 | rule | String | - | Yes | Rule of the dispatch list | `"Earliest Due Date"` | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| 13 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 14 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 15 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 16 | status | String | - | Yes | Primary lifecycle state of the document | `"Generated"` | Generated; Acknowledged; Closed |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Generated, Acknowledged, Closed. Initial state: Generated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 5 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_dispatchListEntry.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_dispatchList.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_dispatchList.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_dispatchList.js
