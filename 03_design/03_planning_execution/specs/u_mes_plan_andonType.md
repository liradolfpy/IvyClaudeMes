# u_mes_plan_andonType

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Types of andon call with responsible department and target response time |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 16 (10 required, 6 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per andon type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1292000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"QUALITY"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the andon type; used as its display value in other collections | `"Quality"` |  |
| 6 | description | String | - | Yes | Description of the andon type | `"Quality (QUALITY)"` |  |
| 7 | colourCode | String | - | No (null allowed) | Colour code | `"#F5A623"` |  |
| 8 | responsibleDepartmentId | String | - | No (null allowed) | Reference to u_mes_mast_department._id: responsible department | `"1256000000000001"` | Reference: u_mes_mast_department._id |
| 9 | responsibleDepartmentName | String | - | No (null allowed) | Display value of responsibleDepartmentId, copied from u_mes_mast_department.name | `"Production"` |  |
| 10 | targetResponseSec | Int32 | - | Yes | Target response (seconds) | `NumberInt(300)` |  |
| 11 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | targetRepairSec | Int32 | - | No (null allowed) | Target time to resolve (seconds) | `NumberInt(1800)` |  |
| 13 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000003"` | Reference: u_mes_syst_escalationRule._id |
| 14 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Quality andon not acknowledged"` |  |
| 15 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ responsibleDepartmentId: 1 }` | No | Look-up of documents by responsible department |
| 4 | `{ escalationRuleId: 1 }` | No | Look-up of documents by escalation rule |

## Referenced by

u_mes_plan_andonEvent.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_andonType.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_andonType.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_andonType.js
