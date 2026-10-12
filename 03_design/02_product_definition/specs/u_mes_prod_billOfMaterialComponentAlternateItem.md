# u_mes_prod_billOfMaterialComponentAlternateItem

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Links one bill of material component to one alternate item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prod_billOfMaterialComponent |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A bill of material component can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. billOfMaterialComponentId and billOfMaterialComponentName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1050000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BOM-5110-10-0100-01-C01-AI01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfMaterialComponentId | String | - | Yes | Reference to u_mes_prod_billOfMaterialComponent._id: the parent document this one belongs to | `"1048000000000001"` | Reference: u_mes_prod_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String | - | Yes | Display value of billOfMaterialComponentId, copied from u_mes_prod_billOfMaterialComponent.recordNo | `"BOM-5110-10-0100-01-C01"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | alternateItemId | String | - | Yes | Reference to u_mes_prod_item._id: alternate item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 9 | alternateItemName | String | - | Yes | Display value of alternateItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfMaterialComponentAlternateItem.js
