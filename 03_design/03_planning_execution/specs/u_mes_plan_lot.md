# u_mes_plan_lot

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Lots and batches: supplier lots, melt/heat lots, casting lots, heat-treatment charges, anodising loads |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 51 (25 required, 26 may be null) |
| Estimated volume per year | ~40,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per lot, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with lotId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_lotParentLot | Relationship | parent lot |
| u_mes_plan_lotAttributesCavityNo | Value list | attributes cavity number |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1096000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"L260915-GDC-014"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 8 | lotType | String | - | Yes | Lot type | `"Casting Lot"` | Supplier Lot; Melt Lot; Casting Lot; Heat Treatment Charge; Machining Lot; Anodising Load; Finished Goods Lot; Granulation Lot; Coated Tablet Lot |
| 9 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 10 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 11 | supplierLotNo | String | - | No (null allowed) | Supplier lot number | `null` |  |
| 12 | heatNo | String | - | No (null allowed) | Heat number of the alloy melt | `"H26-3418"` |  |
| 13 | goodsReceiptId | String | - | No (null allowed) | Reference to u_mes_matl_goodsReceipt._id | `null` | Reference: u_mes_matl_goodsReceipt._id |
| 14 | goodsReceiptName | String | - | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_matl_goodsReceipt.recordNo | `null` |  |
| 15 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 17 | manufacturedAt | Date | Datetime | Yes | Date and time when the record was manufactured. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 18 | receivedAt | Date | Datetime | No (null allowed) | Date and time when the record was received. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 19 | expiryAt | Date | Date | No (null allowed) | Expiry at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 20 | initialQuantity | Decimal128 | - | Yes | Initial quantity | `NumberDecimal("240")` |  |
| 21 | currentQuantity | Decimal128 | - | Yes | Current quantity | `NumberDecimal("0")` |  |
| 22 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 23 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 24 | qualityStatus | String | - | Yes | Quality status | `"Released"` | Released; Under Inspection; On Hold; Rejected |
| 25 | onHold | Boolean | - | Yes | True when: on hold | `false` |  |
| 26 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `null` | Reference: u_mes_qual_qualityHold._id |
| 27 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `null` |  |
| 28 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 29 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 30 | attributesDieNo | String | - | No (null allowed) | Attributes die number | `"DIE-5110-LH-02"` |  |
| 31 | attributesFurnaceChargeNo | String | - | No (null allowed) | Attributes furnace charge number | `null` |  |
| 32 | attributesHardnessHbw | Decimal128 | - | No (null allowed) | Attributes hardness (Brinell HBW) | `null` |  |
| 33 | attributesAnodisingLoadNo | String | - | No (null allowed) | Attributes anodising load number | `null` |  |
| 34 | attributesCoatingThicknessUm | Decimal128 | - | No (null allowed) | Attributes coating thickness (micrometres) | `null` |  |
| 35 | attributesCureDate | Date | Date | No (null allowed) | Attributes cure date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 36 | certificateControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: certificate controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 37 | certificateControlledDocumentName | String | - | No (null allowed) | Display value of certificateControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 38 | currentOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: current operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 39 | currentOperationName | String | - | No (null allowed) | Display value of currentOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 40 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 41 | retestDate | Date | Date | No (null allowed) | Date the lot must be re-tested before further use (GMP-41) | `null` |  |
| 42 | batchReleaseId | String | - | No (null allowed) | Reference to u_mes_bmr_batchRelease._id | `null` | Reference: u_mes_bmr_batchRelease._id |
| 43 | batchReleaseName | String | - | No (null allowed) | Display value of batchReleaseId, copied from u_mes_bmr_batchRelease.recordNo | `null` |  |
| 44 | status | String | - | Yes | Primary lifecycle state of the document | `"Consumed"` | Created; Available; In Process; On Hold; Consumed; Closed; Rejected |
| 45 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 46 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 47 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 48 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 49 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 50 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 51 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Created, Available, In Process, On Hold, Consumed, Closed, Rejected. Initial state: Created. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 5 | `{ goodsReceiptId: 1 }` | No | Look-up of documents by goods receipt |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 8 | `{ siteId: 1, manufacturedAt: -1 }` | No | Time-ordered lists and reports by manufactured at |

## Referenced by

u_mes_plan_productionOrderLot, u_mes_plan_dispatchListEntry, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_plan_lotParentLot, u_mes_plan_lotAttributesCavityNo, u_mes_plan_containerLot, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceiptLine, u_mes_matl_kitLine, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_matl_shipmentLineLot, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_trac_asBuiltRecord, u_mes_trac_asBuiltRecordComponent, u_mes_qual_inspectionResult, u_mes_qual_reworkOrder, u_mes_qual_scrapRecord, u_mes_qual_customerComplaintSuspectLot, u_mes_perf_processReading, u_mes_plan_interlockEvent, u_mes_matl_exposureTimer, u_mes_qual_defectRecord, u_mes_bmr_batchRecordReview, u_mes_bmr_batchRelease, u_mes_maint_logbookEntry, u_mes_matl_dispenseRecord, u_mes_qual_retentionSample, u_mes_qual_productRecallLot, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_lot.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_lot.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_lot.js
