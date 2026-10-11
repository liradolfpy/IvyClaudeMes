# u_mes_mdm_shiftRoster

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Crew assignment per production day, shift and line (who is planned where) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | ROS-<recordNo> |
| Display value used by references | recordNo |
| Keys | 25 (23 required, 2 may be null) |
| Estimated volume per year | ~10,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per shift roster, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with shiftRosterId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_shiftRosterAssignment | Child | assignment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ROS-<recordNo> | `"ROS-20260929-A-ASY-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-A-ASY-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 6 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 7 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 8 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 9 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 10 | supervisorUserId | String | Yes | Reference to u_mes_mdm_user._id: supervisor user | `"USR-10045"` | Reference: u_mes_mdm_user._id |
| 11 | supervisorUserName | String | Yes | Display value of supervisorUserId, copied from u_mes_mdm_user.fullName | `"Rajesh Patil"` |  |
| 12 | plannedHeadcount | Int32 | Yes | Planned headcount | `NumberInt(6)` |  |
| 13 | actualHeadcount | Int32 | Yes | Actual headcount | `NumberInt(6)` |  |
| 14 | absentCount | Int32 | Yes | Absent count | `NumberInt(0)` |  |
| 15 | overtimeMinutes | Int32 | Yes | Overtime (minutes) | `NumberInt(0)` |  |
| 16 | remarks | String | No (null allowed) | Remarks of the shift roster | `"No abnormality observed"` |  |
| 17 | publishedAt | Date | No (null allowed) | Date and time when the record was published | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 18 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Planned; Published; Closed |
| 19 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 20 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 21 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 22 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 23 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 24 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 25 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, Published, Closed. Initial state: Planned. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ supervisorUserId: 1 }` | No | Look-up of documents by supervisor user |
| 6 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_mdm_shiftRosterAssignment.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_shiftRoster.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_shiftRoster.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_shiftRoster.js
