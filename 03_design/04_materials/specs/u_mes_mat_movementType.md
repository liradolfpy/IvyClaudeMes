# u_mes_mat_movementType

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | Stock movement types with their ERP movement code and stock effect |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | MVT-<recordNo> |
| Display value used by references | name |
| Keys | 12 (11 required, 1 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per movement type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MVT-<recordNo> | `"MVT-ISSUE-LINE"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ISSUE-LINE"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the movement type; used as its display value in other collections | `"Issue To Line"` |  |
| 6 | description | String | Yes | Description of the movement type | `"Issue of components from stores to a line-side location"` |  |
| 7 | erpMovementType | String | No (null allowed) | ERP movement type | `"261"` |  |
| 8 | stockEffect | String | Yes | Effect of the movement on stock on hand | `"Decrease"` | Increase; Decrease; Transfer; None |
| 9 | requiresReason | Boolean | Yes | True when reason is required | `false` |  |
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

## Referenced by

u_mes_mat_materialMovement.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_movementType.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_movementType.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_movementType.js
