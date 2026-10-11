# u_mes_plan_andonType

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Types of andon call with responsible department and target response time |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | ANT-<recordNo> |
| Display value used by references | name |
| Keys | 13 (10 required, 3 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per andon type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ANT-<recordNo> | `"ANT-QUALITY"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"QUALITY"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the andon type; used as its display value in other collections | `"Quality"` |  |
| 6 | description | String | Yes | Description of the andon type | `"Operator needs quality support at the station"` |  |
| 7 | colourCode | String | No (null allowed) | Colour code | `"#F5A623"` |  |
| 8 | responsibleDepartmentId | String | No (null allowed) | Reference to u_mes_mast_department._id: responsible department | `"DEPT-QUAL"` | Reference: u_mes_mast_department._id |
| 9 | responsibleDepartmentName | String | No (null allowed) | Display value of responsibleDepartmentId, copied from u_mes_mast_department.name | `"Quality"` |  |
| 10 | targetResponseSec | Int32 | Yes | Target response (seconds) | `NumberInt(300)` |  |
| 11 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ responsibleDepartmentId: 1 }` | No | Look-up of documents by responsible department |

## Referenced by

u_mes_plan_andonEvent.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_andonType.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_andonType.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_andonType.js
