# u_mes_prod_item

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | Parts: finished caliper, semi-finished body, purchased components, raw material, consumables; drawing revision |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 39 (27 required, 12 may be null) |
| Estimated volume per year | 500-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per item, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with itemId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_itemRevision | Child | revision |
| u_mes_prod_itemCustomerPart | Child | customer part |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1043000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | description | String | - | Yes | Description of the item | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemType | String | - | Yes | Item type | `"Finished Good"` | Finished Good; Semi Finished; Purchased Component; Raw Material; Consumable; Packaging |
| 8 | itemGroupId | String | - | Yes | Reference to u_mes_prod_itemGroup._id | `"1270000000000001"` | Reference: u_mes_prod_itemGroup._id |
| 9 | itemGroupName | String | - | Yes | Display value of itemGroupId, copied from u_mes_prod_itemGroup.name | `"Brake Caliper Assembly"` |  |
| 10 | baseUnitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id: base unit of measure | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 11 | baseUnitOfMeasureName | String | - | Yes | Display value of baseUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 12 | drawingNo | String | - | Yes | Drawing number | `"5110-10-0100"` |  |
| 13 | drawingRevision | String | - | Yes | Drawing revision | `"D"` |  |
| 14 | revisionDate | Date | Date | Yes | Revision date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 15 | materialSpecification | String | - | No (null allowed) | Material specification | `null` |  |
| 16 | materialGrade | String | - | No (null allowed) | Material grade | `null` |  |
| 17 | netWeightKg | Decimal128 | - | Yes | Net weight (kg) | `NumberDecimal("3.420")` |  |
| 18 | grossWeightKg | Decimal128 | - | Yes | Gross weight (kg) | `NumberDecimal("3.480")` |  |
| 19 | procurementType | String | - | Yes | Procurement type | `"In House"` | In House; Purchased; Subcontracted |
| 20 | defaultSupplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id: default supplier | `null` | Reference: u_mes_mast_supplier._id |
| 21 | defaultSupplierName | String | - | No (null allowed) | Display value of defaultSupplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 22 | isSerialised | Boolean | - | Yes | True when the record is serialised | `true` |  |
| 23 | isLotControlled | Boolean | - | Yes | True when the record is lot controlled | `false` |  |
| 24 | serialNumberRangeId | String | - | No (null allowed) | Reference to u_mes_syst_numberRange._id: serial number range | `"1248000000000001"` | Reference: u_mes_syst_numberRange._id |
| 25 | serialNumberRangeName | String | - | No (null allowed) | Display value of serialNumberRangeId, copied from u_mes_syst_numberRange.name | `"Serial numbers, front caliper LH"` |  |
| 26 | lotNumberRangeId | String | - | No (null allowed) | Reference to u_mes_syst_numberRange._id: lot number range | `null` | Reference: u_mes_syst_numberRange._id |
| 27 | lotNumberRangeName | String | - | No (null allowed) | Display value of lotNumberRangeId, copied from u_mes_syst_numberRange.name | `null` |  |
| 28 | shelfLifeDays | Int32 | - | No (null allowed) | Shelf life (days) | `null` |  |
| 29 | safetyCharacteristic | Boolean | - | Yes | True when: safety characteristic | `true` |  |
| 30 | hsnCode | String | - | Yes | Harmonised system of nomenclature code | `"87083000"` |  |
| 31 | standardCostInr | Decimal128 | - | Yes | Standard cost (Indian rupees) | `NumberDecimal("2184.50")` |  |
| 32 | erpMaterialNo | String | - | Yes | ERP material number | `"000000000051110100"` |  |
| 33 | defaultStorageLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: default storage location | `"1112000000000008"` | Reference: u_mes_matl_storageLocation._id |
| 34 | defaultStorageLocationName | String | - | No (null allowed) | Display value of defaultStorageLocationId, copied from u_mes_matl_storageLocation.name | `"Finished goods rack 01"` |  |
| 35 | fefoRequired | Boolean | - | Yes | True when lots of the item must be issued first-expiry-first-out | `false` |  |
| 36 | exposureControlled | Boolean | - | Yes | True when opened lots of the item run an exposure timer (pot life, open time) | `false` |  |
| 37 | openLifeMinutes | Int32 | - | No (null allowed) | Allowed exposure after opening (minutes); null when not exposure-controlled | `null` |  |
| 38 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Phase Out; Obsolete |
| 39 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Phase Out, Obsolete. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemGroupId: 1 }` | No | Look-up of documents by item group |
| 4 | `{ baseUnitOfMeasureId: 1 }` | No | Look-up of documents by base unit of measure |
| 5 | `{ defaultSupplierId: 1 }` | No | Look-up of documents by default supplier |
| 6 | `{ serialNumberRangeId: 1 }` | No | Look-up of documents by serial number range |
| 7 | `{ lotNumberRangeId: 1 }` | No | Look-up of documents by lot number range |

## Referenced by

u_mes_mast_lineIdealRate, u_mes_mast_supplierSuppliedItem, u_mes_prod_itemRevision, u_mes_prod_itemCustomerPart, u_mes_prod_productVariant, u_mes_prod_billOfMaterial, u_mes_prod_billOfMaterialComponent, u_mes_prod_billOfMaterialComponentAlternateItem, u_mes_prod_routing, u_mes_prod_billOfProcess, u_mes_prod_billOfProcessStepConsumedComponent, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_prod_engineeringChangeAffectedItem, u_mes_plan_customerScheduleLine, u_mes_plan_productionOrder, u_mes_plan_productionScheduleSlot, u_mes_plan_dispatchListEntry, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_plan_lot, u_mes_plan_container, u_mes_plan_changeover, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceiptLine, u_mes_matl_kitLine, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_matl_packagingSpecification, u_mes_matl_shipmentLine, u_mes_trac_serialNumber, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_trac_asBuiltRecord, u_mes_trac_asBuiltRecordComponent, u_mes_qual_characteristic, u_mes_qual_controlPlan, u_mes_qual_inspectionPlan, u_mes_qual_checkSheet, u_mes_qual_inspectionResult, u_mes_qual_spcChart, u_mes_qual_nonconformance, u_mes_qual_reworkOrder, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_deviationPermit, u_mes_qual_capa, u_mes_qual_pfmea, u_mes_qual_ppapSubmission, u_mes_qual_msaStudy, u_mes_qual_customerComplaint, u_mes_perf_productionCount, u_mes_perf_oeeRecord, u_mes_maint_toolItem, u_mes_maint_toolLifeRecord, u_mes_syst_controlledDocument, u_mes_syst_numberRange, u_mes_matl_exposureTimer, u_mes_matl_replenishmentRule, u_mes_matl_materialDemandForecast, u_mes_trac_traceInvestigationResult, u_mes_qual_curveEnvelope, u_mes_qual_defectRecord, u_mes_syst_interlockRule, u_mes_syst_alertRule, u_mes_matl_storageLocationAllowedItem, u_mes_bmr_batchRecordReview, u_mes_bmr_batchRelease, u_mes_bmr_yieldReconciliation, u_mes_maint_cleaningRecord, u_mes_matl_dispenseRecord, u_mes_qual_retentionSample, u_mes_qual_productQualityReview, u_mes_qual_processValidation, u_mes_mmr_masterManufacturingRecord, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_item.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_item.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_item.js
