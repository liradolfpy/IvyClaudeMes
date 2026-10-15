# u_mes_plan_indirectActivity

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Indirect labour activities (cleaning, training, waiting for material ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 13 (11 required, 2 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per indirect activity, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1277000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WAIT-MAT"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the indirect activity; used as its display value in other collections | `"Waiting For Material"` |  |
| 7 | description | String | - | Yes | Description of the indirect activity | `"Waiting For Material (WAIT-MAT)"` |  |
| 8 | isPaid | Boolean | - | Yes | True when the record is paid | `true` |  |
| 9 | costCenterId | String | - | No (null allowed) | Reference to u_mes_mast_costCenter._id | `"1259000000000001"` | Reference: u_mes_mast_costCenter._id |
| 10 | costCenterName | String | - | No (null allowed) | Display value of costCenterId, copied from u_mes_mast_costCenter.name | `"Foundry"` |  |
| 11 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |

## Referenced by

u_mes_plan_labourBooking.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_indirectActivity.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_indirectActivity.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_indirectActivity.js
