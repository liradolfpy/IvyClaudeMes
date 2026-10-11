# u_mes_prd_itemGroup

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Item groups (brake caliper, piston, seal, fastener ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | IGR-<recordNo> |
| Display value used by references | name |
| Keys | 9 (9 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per item group, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: IGR-<recordNo> | `"IGR-CALIPER"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CALIPER"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the item group; used as its display value in other collections | `"Brake Caliper"` |  |
| 6 | description | String | Yes | Description of the item group | `"Brake Caliper"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_prd_item.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_itemGroup.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_itemGroup.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_itemGroup.js
