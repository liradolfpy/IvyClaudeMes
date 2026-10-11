# u_mes_prod_recipeStage

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per stage of a recipe |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_recipe |
| _id pattern | <recipeId>-S<nnn> |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Child collection. The parent recipe can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. recipeId and recipeName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <recipeId>-S<nnn> | `"RCP-TRQ-PRG-07-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-PRG-07-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | recipeId | String | Yes | Reference to u_mes_prod_recipe._id: the parent document this one belongs to | `"RCP-TRQ-PRG-07"` | Reference: u_mes_prod_recipe._id |
| 6 | recipeName | String | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Bleed screw M10 torque program"` |  |
| 7 | stageNo | Int32 | Yes | Stage number | `NumberInt(2)` |  |
| 8 | name | String | Yes | Name of the recipe stage; used as its display value in other collections | `"Final tightening"` |  |
| 9 | durationSec | Int32 | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 10 | setPoint | Decimal128 | Yes | Set point | `NumberDecimal("14.0")` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ recipeId: 1, stageNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_recipeStage.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_recipeStage.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_recipeStage.js
