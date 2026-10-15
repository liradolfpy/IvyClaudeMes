# u_mes_mast_shiftRoster

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Crew assignment per production day, shift and line (who is planned where) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 26 (24 required, 2 may be null) |
| Estimated volume per year | ~10,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per shift roster, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with shiftRosterId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_shiftRosterAssignment | Child | assignment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1024000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ROS-2026-000368"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 7 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 8 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 9 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 10 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 11 | supervisorUserId | String | - | Yes | Reference to u_mes_mast_user._id: supervisor user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 12 | supervisorUserName | String | - | Yes | Display value of supervisorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 13 | plannedHeadcount | Int32 | - | Yes | Planned headcount | `NumberInt(6)` |  |
| 14 | actualHeadcount | Int32 | - | Yes | Actual headcount | `NumberInt(6)` |  |
| 15 | absentCount | Int32 | - | Yes | Absent count | `NumberInt(0)` |  |
| 16 | overtimeMinutes | Int32 | - | Yes | Overtime (minutes) | `NumberInt(0)` |  |
| 17 | remarks | String | - | No (null allowed) | Remarks of the shift roster | `"No abnormality observed"` |  |
| 18 | publishedAt | Date | Datetime | No (null allowed) | Date and time when the record was published. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 19 | status | String | - | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; Published; Closed |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 21 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 22 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 24 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 25 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 26 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, Published, Closed. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_mast_shiftRosterAssignment.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shiftRoster.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shiftRoster.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_shiftRoster.js
