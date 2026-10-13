# u_mes_mmr_masterManufacturingRecordRecipe

| Property | Value |
|---|---|
| Module | Master Manufacturing Record (mmr) |
| Purpose | Links one master manufacturing record to one recipe; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mmr_masterManufacturingRecord |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A master manufacturing record can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. masterManufacturingRecordId and masterManufacturingRecordName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1368000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MMR-5110-10-0100-03-R01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | masterManufacturingRecordId | String | - | Yes | Reference to u_mes_mmr_masterManufacturingRecord._id: the parent document this one belongs to | `"1367000000000001"` | Reference: u_mes_mmr_masterManufacturingRecord._id |
| 6 | masterManufacturingRecordName | String | - | Yes | Display value of masterManufacturingRecordId, copied from u_mes_mmr_masterManufacturingRecord.title | `"Front brake caliper assembly LH, master manufacturing record version 3"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | recipeId | String | - | Yes | Reference to u_mes_prod_recipe._id | `"1073000000000006"` | Reference: u_mes_prod_recipe._id |
| 9 | recipeName | String | - | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Guide pin bolt M8 torque program"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ masterManufacturingRecordId: 1, recipeId: 1 }` | Yes | One link per pair |
| 2 | `{ recipeId: 1, masterManufacturingRecordId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/12_master_manufacturing_record/validators/u_mes_mmr_masterManufacturingRecordRecipe.json
- Indexes: 03_design/12_master_manufacturing_record/indexes/u_mes_mmr_masterManufacturingRecordRecipe.js
- Sample documents (10): 03_design/12_master_manufacturing_record/samples/u_mes_mmr_masterManufacturingRecordRecipe.js
