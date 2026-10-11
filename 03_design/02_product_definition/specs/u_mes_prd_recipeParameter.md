# u_mes_prd_recipeParameter

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per parameter of a recipe |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prd_recipe |
| _id pattern | <recipeId>-P<nnn> |
| Display value used by references | name |
| Keys | 18 (14 required, 4 may be null) |

## Structure

Child collection. The parent recipe can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. recipeId and recipeName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <recipeId>-P<nnn> | `"RCP-TRQ-PRG-07-P001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-PRG-07-P001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | recipeId | String | Yes | Reference to u_mes_prd_recipe._id: the parent document this one belongs to | `"RCP-TRQ-PRG-07"` | Reference: u_mes_prd_recipe._id |
| 6 | recipeName | String | Yes | Display value of recipeId, copied from u_mes_prd_recipe.name | `"Bleed screw M10 torque program"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the recipe parameter; used as its display value in other collections | `"Target torque"` |  |
| 9 | processTagId | String | Yes | Reference to u_mes_eqp_processTag._id | `"TAG-PN1.GDC01.DIE_TEMP_UPPER"` | Reference: u_mes_eqp_processTag._id |
| 10 | processTagName | String | Yes | Display value of processTagId, copied from u_mes_eqp_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 11 | setPoint | Decimal128 | Yes | Set point | `NumberDecimal("14.0")` |  |
| 12 | lowerLimit | Decimal128 | No (null allowed) | Lower limit | `NumberDecimal("12.0")` |  |
| 13 | upperLimit | Decimal128 | No (null allowed) | Upper limit | `NumberDecimal("16.0")` |  |
| 14 | unitOfMeasureId | String | No (null allowed) | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-NM"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Newton metre"` |  |
| 16 | isCritical | Boolean | Yes | True when the record is critical | `true` |  |
| 17 | downloadToController | Boolean | Yes | True when: download to controller | `true` |  |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ recipeId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ processTagId: 1 }` | No | Look-up of lines by process tag |
| 3 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_recipeParameter.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_recipeParameter.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_recipeParameter.js
