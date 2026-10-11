# u_mes_mast_unitOfMeasure

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Units and conversion factors (EA, kg, N.m, bar, mm, um, kWh) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 17 (14 required, 3 may be null) |
| Estimated volume per year | 30-80 |
| Storage | standard |

## Structure

Flat entity collection: one document per unit of measure, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1042000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"EA"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the unit of measure; used as its display value in other collections | `"Each"` |  |
| 6 | scope | String | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 7 | symbol | String | Yes | Symbol of the unit of measure | `"ea"` |  |
| 8 | dimension | String | Yes | Dimension of the unit of measure | `"Count"` | Count; Mass; Length; Torque; Pressure; Temperature; Time; Energy; Volume; Hardness; Leak Rate |
| 9 | baseUnitOfMeasureId | String | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id: base unit of measure | `null` | Reference: u_mes_mast_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String | No (null allowed) | Display value of baseUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `null` |  |
| 11 | factorToBase | Decimal128 | Yes | Multiplier to convert to the base unit of the dimension | `NumberDecimal("1.000000")` |  |
| 12 | offsetToBase | Decimal128 | Yes | Offset to base | `NumberDecimal("0.000000")` |  |
| 13 | decimalPlaces | Int32 | Yes | Decimal places | `NumberInt(0)` |  |
| 14 | isoCode | String | No (null allowed) | UN/ECE Recommendation 20 unit code | `"C62"` |  |
| 15 | isBaseUnit | Boolean | Yes | True when the record is base unit | `false` |  |
| 16 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ baseUnitOfMeasureId: 1 }` | No | Look-up of documents by base unit of measure |

## Referenced by

u_mes_mast_equipment, u_mes_mast_unitOfMeasure, u_mes_prod_item, u_mes_prod_billOfMaterial, u_mes_prod_billOfMaterialComponent, u_mes_prod_billOfProcessStepProcessParameter, u_mes_prod_recipeParameter, u_mes_plan_productionOrder, u_mes_plan_lot, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceiptLine, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_qual_characteristic, u_mes_qual_inspectionResult, u_mes_qual_scrapRecord, u_mes_qual_gauge, u_mes_perf_processTag, u_mes_maint_sparePart, u_mes_perf_energyReading, u_mes_perf_energyType.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_unitOfMeasure.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_unitOfMeasure.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_unitOfMeasure.js
