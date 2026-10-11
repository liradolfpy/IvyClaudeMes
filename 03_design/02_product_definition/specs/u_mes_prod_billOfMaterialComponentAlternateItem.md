# u_mes_prod_billOfMaterialComponentAlternateItem

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Links one bill of material component to one alternate item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prod_billOfMaterialComponent |
| _id pattern | <billOfMaterialComponentId>-AI<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A bill of material component can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. billOfMaterialComponentId and billOfMaterialComponentName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <billOfMaterialComponentId>-AI<nnn> | `"BOM-5110-10-0100-D-01-C001-AI001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-D-01-C001-AI001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfMaterialComponentId | String | Yes | Reference to u_mes_prod_billOfMaterialComponent._id: the parent document this one belongs to | `"BOM-5110-10-0100-D-01-C001"` | Reference: u_mes_prod_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String | Yes | Display value of billOfMaterialComponentId, copied from u_mes_prod_billOfMaterialComponent.recordNo | `"5110-10-0100-D-01-C001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | alternateItemId | String | Yes | Reference to u_mes_prod_item._id: alternate item | `"ITM-5110-30-0010"` | Reference: u_mes_prod_item._id |
| 9 | alternateItemName | String | Yes | Display value of alternateItemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfMaterialComponentId: 1, alternateItemId: 1 }` | Yes | One link per pair |
| 2 | `{ alternateItemId: 1, billOfMaterialComponentId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfMaterialComponentAlternateItem.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfMaterialComponentAlternateItem.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_billOfMaterialComponentAlternateItem.js
