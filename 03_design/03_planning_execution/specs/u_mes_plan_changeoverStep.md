# u_mes_plan_changeoverStep

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per step of a changeover |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_changeover |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (16 required, 3 may be null) |

## Structure

Child collection. The parent changeover can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. changeoverId and changeoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1103000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CHG-2026-000307-S01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | changeoverId | String | Yes | Reference to u_mes_plan_changeover._id: the parent document this one belongs to | `"1102000000000001"` | Reference: u_mes_plan_changeover._id |
| 6 | changeoverName | String | Yes | Display value of changeoverId, copied from u_mes_plan_changeover.recordNo | `"CHG-2026-000307"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 8 | description | String | Yes | Description of the changeover step | `"Skim the ladle, pour in one continuous stream and start the tilt cycle"` |  |
| 9 | internalExternal | String | Yes | Internal steps need the equipment stopped; external steps are done while it runs | `"Internal"` | Internal; External |
| 10 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-15T00:33:30.000+0000")` |  |
| 11 | completedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'completed' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 12 | completedBy | String | No (null allowed) | Display name of the user in completedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:30.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ changeoverId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_changeoverStep.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_changeoverStep.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_changeoverStep.js
