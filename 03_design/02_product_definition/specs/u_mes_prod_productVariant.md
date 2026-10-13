# u_mes_prod_productVariant

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Product variants (LH/RH, piston diameter, pad compound, market) that drive BOM, instruction and label selection |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 29 (13 required, 16 may be null) |
| Estimated volume per year | 10-200 |
| Storage | standard |

## Structure

Flat entity collection: one document per product variant, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1046000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"FBC-LH-STD"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the product variant; used as its display value in other collections | `"Front Caliper LH, Standard"` |  |
| 7 | baseItemId | String | - | Yes | Reference to u_mes_prod_item._id: base item | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 8 | baseItemName | String | - | Yes | Display value of baseItemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | variantItemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id: variant item | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 10 | variantItemName | String | - | No (null allowed) | Display value of variantItemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 12 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 13 | optionsHand | String | - | No (null allowed) | Options hand | `"LH"` | LH; RH |
| 14 | optionsPistonDiameterMm | Decimal128 | - | No (null allowed) | Options piston diameter (mm) | `NumberDecimal("54.0")` |  |
| 15 | optionsPadCompoundId | String | - | No (null allowed) | Reference to u_mes_prod_padCompound._id: options pad compound | `"1274000000000001"` | Reference: u_mes_prod_padCompound._id |
| 16 | optionsPadCompoundName | String | - | No (null allowed) | Display value of optionsPadCompoundId, copied from u_mes_prod_padCompound.name | `"NAO Ceramic"` |  |
| 17 | optionsMarketId | String | - | No (null allowed) | Reference to u_mes_prod_market._id: options market | `"1273000000000001"` | Reference: u_mes_prod_market._id |
| 18 | optionsMarketName | String | - | No (null allowed) | Display value of optionsMarketId, copied from u_mes_prod_market.name | `"Domestic"` |  |
| 19 | optionsSurfaceFinishId | String | - | No (null allowed) | Reference to u_mes_prod_surfaceFinish._id: options surface finish | `"1275000000000001"` | Reference: u_mes_prod_surfaceFinish._id |
| 20 | optionsSurfaceFinishName | String | - | No (null allowed) | Display value of optionsSurfaceFinishId, copied from u_mes_prod_surfaceFinish.name | `"Anodised Natural"` |  |
| 21 | optionsColour | String | - | No (null allowed) | Options colour | `"Silver"` |  |
| 22 | vehicleModelId | String | - | No (null allowed) | Reference to u_mes_prod_vehicleModel._id | `"1276000000000001"` | Reference: u_mes_prod_vehicleModel._id |
| 23 | vehicleModelName | String | - | No (null allowed) | Display value of vehicleModelId, copied from u_mes_prod_vehicleModel.name | `"Sahyadri X42 Hatchback"` |  |
| 24 | modelYear | Int32 | - | Yes | Model year | `NumberInt(2026)` |  |
| 25 | labelSuffix | String | - | Yes | Label suffix | `"L"` |  |
| 26 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 27 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ baseItemId: 1 }` | No | Look-up of documents by base item |
| 4 | `{ variantItemId: 1 }` | No | Look-up of documents by variant item |
| 5 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 6 | `{ optionsPadCompoundId: 1 }` | No | Look-up of documents by options pad compound |
| 7 | `{ optionsMarketId: 1 }` | No | Look-up of documents by options market |

## Referenced by

u_mes_prod_billOfMaterialComponentProductVariant, u_mes_prod_workInstructionStepProductVariant, u_mes_plan_productionOrder, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_plan_labourBooking, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecord, u_mes_perf_downtimeEvent, u_mes_prod_recipeProductVariant, u_mes_prod_workInstructionProductVariant, u_mes_plan_documentAcknowledgement, u_mes_plan_recipeDownload, u_mes_plan_setupVerification, u_mes_qual_curveEnvelope, u_mes_qual_defectRecord, u_mes_qual_inspectionPlanProductVariant, u_mes_perf_workCenterPerformance, u_mes_perf_operatorPerformance, u_mes_syst_modelPrediction, u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_productVariant.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_productVariant.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_productVariant.js
