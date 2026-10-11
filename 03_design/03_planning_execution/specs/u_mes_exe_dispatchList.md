# u_mes_exe_dispatchList

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Prioritised work queue per work centre shown to the operator |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | DSP-<recordNo> |
| Display value used by references | recordNo |
| Keys | 22 (19 required, 3 may be null) |
| Estimated volume per year | ~100,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per dispatch list, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with dispatchListId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_exe_dispatchListEntry | Child | entry |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DSP-<recordNo> | `"DSP-20260929-TRQ-01-A"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-TRQ-01-A"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 6 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 7 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 8 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 9 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 10 | generatedAt | Date | Yes | Date and time when the record was generated | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 11 | rule | String | Yes | Rule of the dispatch list | `"Earliest Due Date"` | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| 12 | acknowledgedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'acknowledged' | `"USR-10045"` | Reference: u_mes_mdm_user._id |
| 13 | acknowledgedBy | String | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mdm_user.fullName | `"Rajesh Patil"` |  |
| 14 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 15 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Generated; Acknowledged; Closed |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 19 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 20 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 21 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 22 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Generated, Acknowledged, Closed. Initial state: Generated. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 5 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_exe_dispatchListEntry.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_dispatchList.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_dispatchList.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_dispatchList.js
