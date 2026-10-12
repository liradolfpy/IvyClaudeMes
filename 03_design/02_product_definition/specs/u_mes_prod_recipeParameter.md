# u_mes_prod_recipeParameter

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per parameter of a recipe |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_recipe |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (14 required, 4 may be null) |

## Structure

Child collection. The parent recipe can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. recipeId and recipeName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1074000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-5110-LH-01-P01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | recipeId | String | - | Yes | Reference to u_mes_prod_recipe._id: the parent document this one belongs to | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 6 | recipeName | String | - | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | - | Yes | Name of the recipe parameter | `"Die temperature, upper half, casting machine 1"` |  |
| 9 | processTagId | String | - | Yes | Reference to u_mes_perf_processTag._id | `"1210000000000001"` | Reference: u_mes_perf_processTag._id |
| 10 | processTagName | String | - | Yes | Display value of processTagId, copied from u_mes_perf_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 11 | setPoint | Decimal128 | - | Yes | Set point | `NumberDecimal("400.0")` |  |
| 12 | lowerLimit | Decimal128 | - | No (null allowed) | Lower limit | `NumberDecimal("380.0")` |  |
| 13 | upperLimit | Decimal128 | - | No (null allowed) | Upper limit | `NumberDecimal("420.0")` |  |
| 14 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000008"` | Reference: u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Degree Celsius"` |  |
| 16 | isCritical | Boolean | - | Yes | True when the record is critical | `true` |  |
| 17 | downloadToController | Boolean | - | Yes | True when: download to controller | `true` |  |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ recipeId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ processTagId: 1 }` | No | Look-up of lines by process tag |
| 3 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_recipeParameter.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_recipeParameter.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_recipeParameter.js
