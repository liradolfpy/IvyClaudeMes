# u_mes_plan_shiftHandoverOpenItem

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per open item of a shift handover |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_shiftHandover |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (20 required, 0 may be null) |

## Structure

Child collection. The parent shift handover can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shiftHandoverId and shiftHandoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1111000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SHO-2026-000456-OI01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | shiftHandoverId | String | - | Yes | Reference to u_mes_plan_shiftHandover._id: the parent document this one belongs to | `"1107000000000001"` | Reference: u_mes_plan_shiftHandover._id |
| 7 | shiftHandoverName | String | - | Yes | Display value of shiftHandoverId, copied from u_mes_plan_shiftHandover.recordNo | `"SHO-2026-000456"` |  |
| 8 | itemNo | Int32 | - | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 9 | description | String | - | Yes | Description of the shift handover open item | `"Follow up: ejector pin sticks on cavity 2 and the casting does not release"` |  |
| 10 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 11 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 12 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 13 | closed | Boolean | - | Yes | True when: closed | `true` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 16 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 18 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 19 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shiftHandoverId: 1, itemNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_shiftHandoverOpenItem.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_shiftHandoverOpenItem.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_shiftHandoverOpenItem.js
