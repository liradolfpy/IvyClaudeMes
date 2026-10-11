# u_mes_prd_productVariant

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Product variants (LH/RH, piston diameter, pad compound, market) that drive BOM, instruction and label selection |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | VAR-<recordNo> |
| Display value used by references | name |
| Keys | 28 (14 required, 14 may be null) |
| Estimated volume per year | 10-200 |
| Storage | standard |

## Structure

Flat entity collection: one document per product variant, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: VAR-<recordNo> | `"VAR-FBC-LH-STD"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"FBC-LH-STD"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the product variant; used as its display value in other collections | `"Front Caliper LH Standard"` |  |
| 6 | baseItemId | String | Yes | Reference to u_mes_prd_item._id: base item | `"ITM-5110-30-0010"` | Reference: u_mes_prd_item._id |
| 7 | baseItemName | String | Yes | Display value of baseItemId, copied from u_mes_prd_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 8 | variantItemId | String | No (null allowed) | Reference to u_mes_prd_item._id: variant item | `"ITM-5110-30-0010"` | Reference: u_mes_prd_item._id |
| 9 | variantItemName | String | No (null allowed) | Display value of variantItemId, copied from u_mes_prd_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | customerId | String | No (null allowed) | Reference to u_mes_mdm_customer._id | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 11 | customerName | String | No (null allowed) | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 12 | optionsHand | String | Yes | Options hand | `"LH"` | LH; RH |
| 13 | optionsPistonDiameterMm | Decimal128 | Yes | Options piston diameter (mm) | `NumberDecimal("54.0")` |  |
| 14 | optionsPadCompoundId | String | No (null allowed) | Reference to u_mes_prd_padCompound._id: options pad compound | `"PDC-NAO-CER"` | Reference: u_mes_prd_padCompound._id |
| 15 | optionsPadCompoundName | String | No (null allowed) | Display value of optionsPadCompoundId, copied from u_mes_prd_padCompound.name | `"NAO-Ceramic"` |  |
| 16 | optionsMarketId | String | No (null allowed) | Reference to u_mes_prd_market._id: options market | `"MKT-DOM"` | Reference: u_mes_prd_market._id |
| 17 | optionsMarketName | String | No (null allowed) | Display value of optionsMarketId, copied from u_mes_prd_market.name | `"Domestic"` |  |
| 18 | optionsSurfaceFinishId | String | No (null allowed) | Reference to u_mes_prd_surfaceFinish._id: options surface finish | `"SFN-ANOD-NAT"` | Reference: u_mes_prd_surfaceFinish._id |
| 19 | optionsSurfaceFinishName | String | No (null allowed) | Display value of optionsSurfaceFinishId, copied from u_mes_prd_surfaceFinish.name | `"Anodised Natural"` |  |
| 20 | optionsColour | String | No (null allowed) | Options colour | `"Silver"` |  |
| 21 | vehicleModelId | String | No (null allowed) | Reference to u_mes_prd_vehicleModel._id | `"VHM-SM-X42"` | Reference: u_mes_prd_vehicleModel._id |
| 22 | vehicleModelName | String | No (null allowed) | Display value of vehicleModelId, copied from u_mes_prd_vehicleModel.name | `"Sahyadri X42"` |  |
| 23 | modelYear | Int32 | Yes | Model year | `NumberInt(2026)` |  |
| 24 | labelSuffix | String | Yes | Label suffix | `"L"` |  |
| 25 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 26 | effectiveTo | Date | No (null allowed) | Effective to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 27 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 28 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_prd_billOfMaterialComponentProductVariant, u_mes_prd_workInstructionStepProductVariant, u_mes_exe_productionOrder, u_mes_exe_wipUnit, u_mes_trc_serialNumber, u_mes_trc_asBuiltRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_productVariant.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_productVariant.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_productVariant.js
