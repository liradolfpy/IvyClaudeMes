# u_mes_maint_toolType

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Types of tool (die, fixture, cutting tool, socket, test seal) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | TLT-<recordNo> |
| Display value used by references | name |
| Keys | 10 (10 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per tool type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: TLT-<recordNo> | `"TLT-SOCKET"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SOCKET"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the tool type; used as its display value in other collections | `"Nutrunner Socket"` |  |
| 6 | description | String | Yes | Description of the tool type | `"Nutrunner Socket"` |  |
| 7 | lifeUom | String | Yes | Life uom | `"Shots"` | Shots; Cycles; Pieces; Run Hours |
| 8 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_maint_tool.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_toolType.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_toolType.js
- Sample document: 03_design/08_tooling_maintenance/samples/u_mes_maint_toolType.js
