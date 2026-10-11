# u_mes_plan_shiftHandoverOpenItem

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per open item of a shift handover |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_shiftHandover |
| _id pattern | <shiftHandoverId>-OI<nnn> |
| Display value used by references | description |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent shift handover can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shiftHandoverId and shiftHandoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <shiftHandoverId>-OI<nnn> | `"SHO-20260929-ASY-01-A-OI001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-ASY-01-A-OI001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shiftHandoverId | String | Yes | Reference to u_mes_plan_shiftHandover._id: the parent document this one belongs to | `"SHO-20260929-ASY-01-A"` | Reference: u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String | Yes | Display value of shiftHandoverId, copied from u_mes_plan_shiftHandover.recordNo | `"20260929-ASY-01-A"` |  |
| 7 | itemNo | Int32 | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the shift handover open item | `"Verify seal lot S260921-SEL-004 before use on shift B"` |  |
| 9 | ownerUserId | String | Yes | Reference to u_mes_mast_user._id: owner user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 10 | ownerUserName | String | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | dueAt | Date | Yes | Due date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 12 | closed | Boolean | Yes | True when: closed | `false` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_shiftHandoverOpenItem.js
