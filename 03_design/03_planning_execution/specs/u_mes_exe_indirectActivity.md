# u_mes_exe_indirectActivity

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Indirect labour activities (cleaning, training, waiting for material ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | IND-<recordNo> |
| Display value used by references | name |
| Keys | 12 (10 required, 2 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per indirect activity, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: IND-<recordNo> | `"IND-WAIT-MAT"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WAIT-MAT"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the indirect activity; used as its display value in other collections | `"Waiting For Material"` |  |
| 6 | description | String | Yes | Description of the indirect activity | `"Waiting For Material"` |  |
| 7 | isPaid | Boolean | Yes | True when the record is paid | `true` |  |
| 8 | costCenterId | String | No (null allowed) | Reference to u_mes_mdm_costCenter._id | `"CC-5120"` | Reference: u_mes_mdm_costCenter._id |
| 9 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mdm_costCenter.name | `"Assembly Line 1"` |  |
| 10 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 11 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |

## Referenced by

u_mes_exe_labourBooking.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_indirectActivity.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_indirectActivity.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_indirectActivity.js
