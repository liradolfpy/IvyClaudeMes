# u_mes_prd_item

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Parts: finished caliper, semi-finished body, purchased components, raw material, consumables; drawing revision |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | ITM-<recordNo> |
| Display value used by references | description |
| Keys | 35 (24 required, 11 may be null) |
| Estimated volume per year | 500-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per item, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with itemId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prd_itemRevision | Child | revision |
| u_mes_prd_itemCustomerPart | Child | customer part |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ITM-<recordNo> | `"ITM-5110-10-0100"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | description | String | Yes | Description of the item | `"Front Brake Caliper Assembly, LH"` |  |
| 6 | itemType | String | Yes | Item type | `"Finished Good"` | Finished Good; Semi Finished; Purchased Component; Raw Material; Consumable; Packaging |
| 7 | itemGroupId | String | Yes | Reference to u_mes_prd_itemGroup._id | `"IGR-CALIPER"` | Reference: u_mes_prd_itemGroup._id |
| 8 | itemGroupName | String | Yes | Display value of itemGroupId, copied from u_mes_prd_itemGroup.name | `"Brake Caliper"` |  |
| 9 | baseUnitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id: base unit of measure | `"UOM-EA"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String | Yes | Display value of baseUnitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Each"` |  |
| 11 | drawingNo | String | Yes | Drawing number | `"5110-10-0100"` |  |
| 12 | drawingRevision | String | Yes | Drawing revision | `"D"` |  |
| 13 | revisionDate | Date | Yes | Revision date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 14 | materialSpecification | String | No (null allowed) | Material specification | `"EN 1706 AC-42100"` |  |
| 15 | materialGrade | String | No (null allowed) | Material grade | `"AlSi7Mg0.3 T6"` |  |
| 16 | netWeightKg | Decimal128 | Yes | Net weight (kg) | `NumberDecimal("3.420")` |  |
| 17 | grossWeightKg | Decimal128 | Yes | Gross weight (kg) | `NumberDecimal("3.480")` |  |
| 18 | procurementType | String | Yes | Procurement type | `"In House"` | In House; Purchased; Subcontracted |
| 19 | defaultSupplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id: default supplier | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 20 | defaultSupplierName | String | No (null allowed) | Display value of defaultSupplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 21 | isSerialised | Boolean | Yes | True when the record is serialised | `true` |  |
| 22 | isLotControlled | Boolean | Yes | True when the record is lot controlled | `true` |  |
| 23 | serialNumberRangeId | String | No (null allowed) | Reference to u_mes_sys_numberRange._id: serial number range | `"NR-SERIAL-FBC-LH"` | Reference: u_mes_sys_numberRange._id |
| 24 | serialNumberRangeName | String | No (null allowed) | Display value of serialNumberRangeId, copied from u_mes_sys_numberRange.name | `"Serial numbers, front caliper LH"` |  |
| 25 | lotNumberRangeId | String | No (null allowed) | Reference to u_mes_sys_numberRange._id: lot number range | `"NR-SERIAL-FBC-LH"` | Reference: u_mes_sys_numberRange._id |
| 26 | lotNumberRangeName | String | No (null allowed) | Display value of lotNumberRangeId, copied from u_mes_sys_numberRange.name | `"Serial numbers, front caliper LH"` |  |
| 27 | shelfLifeDays | Int32 | No (null allowed) | Shelf life (days) | `NumberInt(730)` |  |
| 28 | safetyCharacteristic | Boolean | Yes | True when: safety characteristic | `true` |  |
| 29 | hsnCode | String | Yes | Harmonised system of nomenclature code | `"87083000"` |  |
| 30 | standardCostInr | Decimal128 | Yes | Standard cost (Indian rupees) | `NumberDecimal("2184.50")` |  |
| 31 | erpMaterialNo | String | Yes | ERP material number | `"000000000051101001"` |  |
| 32 | defaultStorageLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: default storage location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 33 | defaultStorageLocationName | String | No (null allowed) | Display value of defaultStorageLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 34 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Phase Out; Obsolete |
| 35 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Phase Out, Obsolete. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_mdm_lineIdealRate, u_mes_mdm_supplierSuppliedItem, u_mes_prd_itemRevision, u_mes_prd_itemCustomerPart, u_mes_prd_productVariant, u_mes_prd_billOfMaterial, u_mes_prd_billOfMaterialComponent, u_mes_prd_billOfMaterialComponentAlternateItem, u_mes_prd_routing, u_mes_prd_billOfProcess, u_mes_prd_billOfProcessStepConsumedComponent, u_mes_prd_workInstruction, u_mes_prd_recipe, u_mes_prd_engineeringChangeAffectedItem, u_mes_exe_customerScheduleLine, u_mes_exe_productionOrder, u_mes_exe_productionScheduleSlot, u_mes_exe_dispatchListEntry, u_mes_exe_operationExecution, u_mes_exe_wipUnit, u_mes_exe_lot, u_mes_exe_container, u_mes_exe_changeover, u_mes_mat_inventoryBalance, u_mes_mat_materialMovement, u_mes_mat_goodsReceiptLine, u_mes_mat_kitLine, u_mes_mat_materialRequest, u_mes_mat_materialConsumption, u_mes_mat_packagingSpecification, u_mes_mat_shipmentLine, u_mes_trc_serialNumber, u_mes_trc_genealogyLink, u_mes_trc_componentLotLink, u_mes_trc_asBuiltRecord, u_mes_trc_asBuiltRecordComponent, u_mes_qlt_characteristic, u_mes_qlt_controlPlan, u_mes_qlt_inspectionPlan, u_mes_qlt_checkSheet, u_mes_qlt_inspectionResult, u_mes_qlt_spcChart, u_mes_qlt_nonconformance, u_mes_qlt_reworkOrder, u_mes_qlt_scrapRecord, u_mes_qlt_qualityHold, u_mes_qlt_deviationPermit, u_mes_qlt_capa, u_mes_qlt_pfmea, u_mes_qlt_ppapSubmission, u_mes_qlt_msaStudy, u_mes_qlt_customerComplaint, u_mes_eqp_productionCount, u_mes_eqp_oeeRecord, u_mes_mnt_toolItem, u_mes_sys_controlledDocument, u_mes_sys_numberRange.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_item.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_item.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_item.js
