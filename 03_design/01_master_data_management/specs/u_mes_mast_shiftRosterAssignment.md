# u_mes_mast_shiftRosterAssignment

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per assignment of a shift roster |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_mast_shiftRoster |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 22 (18 required, 4 may be null) |

## Structure

Child collection. The parent shift roster can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shiftRosterId and shiftRosterName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1025000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ROS-2026-000368-A01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shiftRosterId | String | - | Yes | Reference to u_mes_mast_shiftRoster._id: the parent document this one belongs to | `"1024000000000001"` | Reference: u_mes_mast_shiftRoster._id |
| 6 | shiftRosterName | String | - | Yes | Display value of shiftRosterId, copied from u_mes_mast_shiftRoster.recordNo | `"ROS-2026-000368"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 10 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 12 | roleInCrew | String | - | Yes | Role in crew | `"Operator"` | Operator; Setter; Line Leader; Quality Inspector; Material Handler |
| 13 | attendance | String | - | Yes | Attendance of the shift roster assignment | `"Present"` | Present; Absent; Leave; Overtime |
| 14 | replacedUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: replaced user | `null` | Reference: u_mes_mast_user._id |
| 15 | replacedUserName | String | - | No (null allowed) | Display value of replacedUserId, copied from u_mes_mast_user.fullName | `null` |  |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 18 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 20 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 21 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 22 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shiftRosterId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |
| 3 | `{ workCenterId: 1 }` | No | Look-up of lines by work center |
| 4 | `{ replacedUserId: 1 }` | No | Look-up of lines by replaced user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shiftRosterAssignment.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shiftRosterAssignment.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_shiftRosterAssignment.js
