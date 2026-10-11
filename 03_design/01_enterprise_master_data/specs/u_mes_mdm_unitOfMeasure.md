# u_mes_mdm_unitOfMeasure

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Units and conversion factors (EA, kg, N.m, bar, mm, um, kWh) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | UOM-<recordNo> |
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
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: UOM-<recordNo> | `"UOM-EA"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"EA"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the unit of measure; used as its display value in other collections | `"Each"` |  |
| 6 | scope | String | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 7 | symbol | String | Yes | Symbol of the unit of measure | `"N.m"` |  |
| 8 | dimension | String | Yes | Dimension of the unit of measure | `"Torque"` | Count; Mass; Length; Torque; Pressure; Temperature; Time; Energy; Volume; Hardness; Leak Rate |
| 9 | baseUnitOfMeasureId | String | No (null allowed) | Reference to u_mes_mdm_unitOfMeasure._id: base unit of measure | `null` | Reference: u_mes_mdm_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String | No (null allowed) | Display value of baseUnitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `null` |  |
| 11 | factorToBase | Decimal128 | Yes | Multiplier to convert to the base unit of the dimension | `NumberDecimal("1.000000")` |  |
| 12 | offsetToBase | Decimal128 | Yes | Offset to base | `NumberDecimal("0.000000")` |  |
| 13 | decimalPlaces | Int32 | Yes | Decimal places | `NumberInt(1)` |  |
| 14 | isoCode | String | No (null allowed) | UN/ECE Recommendation 20 unit code | `"NU"` |  |
| 15 | isBaseUnit | Boolean | Yes | True when the record is base unit | `false` |  |
| 16 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ baseUnitOfMeasureId: 1 }` | No | Look-up of documents by base unit of measure |

## Referenced by

u_mes_mdm_equipment, u_mes_mdm_unitOfMeasure, u_mes_prd_item, u_mes_prd_billOfMaterial, u_mes_prd_billOfMaterialComponent, u_mes_prd_billOfProcessStepProcessParameter, u_mes_prd_recipeParameter, u_mes_exe_productionOrder, u_mes_exe_lot, u_mes_mat_inventoryBalance, u_mes_mat_materialMovement, u_mes_mat_goodsReceiptLine, u_mes_mat_materialRequest, u_mes_mat_materialConsumption, u_mes_trc_genealogyLink, u_mes_trc_componentLotLink, u_mes_qlt_characteristic, u_mes_qlt_inspectionResult, u_mes_qlt_scrapRecord, u_mes_qlt_gauge, u_mes_eqp_processTag, u_mes_mnt_sparePart, u_mes_ehs_energyReading, u_mes_ehs_energyType.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_unitOfMeasure.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_unitOfMeasure.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_unitOfMeasure.js
