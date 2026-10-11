# u_mes_plan_wipUnitCompletedStep

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per completed step value of a wip unit |
| Kind | Value list |
| Data class | Transaction |
| Parent collection | u_mes_plan_wipUnit |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 15 (15 required, 0 may be null) |

## Structure

Value-list collection. A wip unit can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. wipUnitId and wipUnitName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1095000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"U260915A0184-CS01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | wipUnitId | String | Yes | Reference to u_mes_plan_wipUnit._id: the parent document this one belongs to | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | completedStep | Int32 | Yes | Step number already completed by the unit | `NumberInt(60)` |  |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 10 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:40.000+0000")` |  |
| 11 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 12 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 13 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:40.000+0000")` |  |
| 14 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 15 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ wipUnitId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_wipUnitCompletedStep.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_wipUnitCompletedStep.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_wipUnitCompletedStep.js
