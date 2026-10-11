# u_mes_prd_billOfMaterialComponentProductVariant

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Links one bill of material component to one product variant; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prd_billOfMaterialComponent |
| _id pattern | <billOfMaterialComponentId>-PV<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A bill of material component can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. billOfMaterialComponentId and billOfMaterialComponentName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <billOfMaterialComponentId>-PV<nnn> | `"BOM-5110-10-0100-D-01-C001-PV001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-D-01-C001-PV001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfMaterialComponentId | String | Yes | Reference to u_mes_prd_billOfMaterialComponent._id: the parent document this one belongs to | `"BOM-5110-10-0100-D-01-C001"` | Reference: u_mes_prd_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String | Yes | Display value of billOfMaterialComponentId, copied from u_mes_prd_billOfMaterialComponent.recordNo | `"5110-10-0100-D-01-C001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | productVariantId | String | Yes | Reference to u_mes_prd_productVariant._id | `"VAR-FBC-LH-STD"` | Reference: u_mes_prd_productVariant._id |
| 9 | productVariantName | String | Yes | Display value of productVariantId, copied from u_mes_prd_productVariant.name | `"Front Caliper LH Standard"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfMaterialComponentId: 1, productVariantId: 1 }` | Yes | One link per pair |
| 2 | `{ productVariantId: 1, billOfMaterialComponentId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_billOfMaterialComponentProductVariant.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_billOfMaterialComponentProductVariant.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_billOfMaterialComponentProductVariant.js
