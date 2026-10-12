# Field list - Material Management (matl)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/04_material_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_matl_storageLocation

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | locationType | String | - |  |
| 7 | areaId | String | - | u_mes_mast_area._id |
| 8 | areaName | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | parentLocationId | String | - | u_mes_matl_storageLocation._id |
| 12 | parentLocationName | String | - |  |
| 13 | zone | String | - |  |
| 14 | rack | String | - |  |
| 15 | level | Int32 | - |  |
| 16 | bin | String | - |  |
| 17 | capacityQuantity | Int32 | - |  |
| 18 | isQuarantine | Boolean | - |  |
| 19 | isLineSide | Boolean | - |  |
| 20 | mixedLotsAllowed | Boolean | - |  |
| 21 | erpStorageLocation | String | - |  |
| 22 | barcode | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_matl_inventoryBalance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | lotId | String | - | u_mes_plan_lot._id |
| 8 | lotName | String | - |  |
| 9 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 10 | storageLocationName | String | - |  |
| 11 | containerId | String | - | u_mes_plan_container._id |
| 12 | containerName | String | - |  |
| 13 | stockStatusId | String | - | u_mes_matl_stockStatus._id |
| 14 | stockStatusName | String | - |  |
| 15 | quantity | Decimal128 | - |  |
| 16 | reservedQuantity | Decimal128 | - |  |
| 17 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | - |  |
| 19 | valueInr | Decimal128 | - |  |
| 20 | firstReceivedAt | Date | Datetime |  |
| 21 | lastMovementAt | Date | Datetime |  |
| 22 | lastCountedAt | Date | Datetime |  |
| 23 | lastCountedById | String | - | u_mes_mast_user._id |
| 24 | lastCountedBy | String | - |  |
| 25 | expiryAt | Date | Date |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_matl_materialMovement

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | movementTypeId | String | - | u_mes_matl_movementType._id |
| 6 | movementTypeName | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | containerId | String | - | u_mes_plan_container._id |
| 12 | containerName | String | - |  |
| 13 | quantity | Decimal128 | - |  |
| 14 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - |  |
| 16 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 17 | fromLocationName | String | - |  |
| 18 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | toLocationName | String | - |  |
| 20 | fromStockStatusId | String | - | u_mes_matl_stockStatus._id |
| 21 | fromStockStatusName | String | - |  |
| 22 | toStockStatusId | String | - | u_mes_matl_stockStatus._id |
| 23 | toStockStatusName | String | - |  |
| 24 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 25 | productionOrderName | String | - |  |
| 26 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 27 | goodsReceiptName | String | - |  |
| 28 | shipmentId | String | - | u_mes_matl_shipment._id |
| 29 | shipmentName | String | - |  |
| 30 | kitId | String | - | u_mes_matl_kit._id |
| 31 | kitName | String | - |  |
| 32 | movedAt | Date | Datetime |  |
| 33 | movedById | String | - | u_mes_mast_user._id |
| 34 | movedBy | String | - |  |
| 35 | scanSource | String | - |  |
| 36 | reasonText | String | - |  |
| 37 | erpDocumentNo | String | - |  |
| 38 | erpMovementType | String | - |  |
| 39 | reversalOfMaterialMovementId | String | - | u_mes_matl_materialMovement._id |
| 40 | reversalOfMaterialMovementName | String | - |  |
| 41 | status | String | - |  |
| 42 | schemaVersion | Int32 | - |  |
| 43 | createdAt | Date | Datetime |  |
| 44 | createdById | String | - | u_mes_mast_user._id |
| 45 | createdBy | String | - |  |
| 46 | updatedAt | Date | Datetime |  |
| 47 | updatedById | String | - | u_mes_mast_user._id |
| 48 | updatedBy | String | - |  |

## u_mes_matl_goodsReceipt

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | supplierId | String | - | u_mes_mast_supplier._id |
| 6 | supplierName | String | - |  |
| 7 | purchaseOrderNo | String | - |  |
| 8 | supplierInvoiceNo | String | - |  |
| 9 | supplierInvoiceDate | Date | Date |  |
| 10 | deliveryChallanNo | String | - |  |
| 11 | vehicleNo | String | - |  |
| 12 | receivedAt | Date | Datetime |  |
| 13 | receivedById | String | - | u_mes_mast_user._id |
| 14 | receivedBy | String | - |  |
| 15 | gateEntryNo | String | - |  |
| 16 | inspectionCompletedAt | Date | Datetime |  |
| 17 | erpGrnNo | String | - |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |
| 20 | createdAt | Date | Datetime |  |
| 21 | createdById | String | - | u_mes_mast_user._id |
| 22 | createdBy | String | - |  |
| 23 | updatedAt | Date | Datetime |  |
| 24 | updatedById | String | - | u_mes_mast_user._id |
| 25 | updatedBy | String | - |  |

## u_mes_matl_goodsReceiptLine

Kind: child | Data class: transaction | Parent: u_mes_matl_goodsReceipt | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 6 | goodsReceiptName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | supplierLotNo | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | orderedQuantity | Decimal128 | - |  |
| 14 | receivedQuantity | Decimal128 | - |  |
| 15 | acceptedQuantity | Decimal128 | - |  |
| 16 | rejectedQuantity | Decimal128 | - |  |
| 17 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | - |  |
| 19 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 20 | storageLocationName | String | - |  |
| 21 | certificateReceived | Boolean | - |  |
| 22 | inspectionStatus | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_matl_goodsReceiptLineInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_matl_goodsReceiptLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | goodsReceiptLineId | String | - | u_mes_matl_goodsReceiptLine._id |
| 6 | goodsReceiptLineName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_matl_kit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - |  |
| 7 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - |  |
| 9 | kitType | String | - |  |
| 10 | requiredAt | Date | Datetime |  |
| 11 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 12 | toLocationName | String | - |  |
| 13 | pickedById | String | - | u_mes_mast_user._id |
| 14 | pickedBy | String | - |  |
| 15 | pickStartedAt | Date | Datetime |  |
| 16 | pickCompletedAt | Date | Datetime |  |
| 17 | deliveredAt | Date | Datetime |  |
| 18 | receivedById | String | - | u_mes_mast_user._id |
| 19 | receivedBy | String | - |  |
| 20 | isComplete | Boolean | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |
| 23 | createdAt | Date | Datetime |  |
| 24 | createdById | String | - | u_mes_mast_user._id |
| 25 | createdBy | String | - |  |
| 26 | updatedAt | Date | Datetime |  |
| 27 | updatedById | String | - | u_mes_mast_user._id |
| 28 | updatedBy | String | - |  |

## u_mes_matl_kitLine

Kind: child | Data class: transaction | Parent: u_mes_matl_kit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | kitId | String | - | u_mes_matl_kit._id |
| 6 | kitName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | requiredQuantity | Decimal128 | - |  |
| 13 | pickedQuantity | Decimal128 | - |  |
| 14 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 15 | fromLocationName | String | - |  |
| 16 | shortQuantity | Decimal128 | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_matl_materialRequest

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | requestedQuantity | Decimal128 | - |  |
| 10 | deliveredQuantity | Decimal128 | - |  |
| 11 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 12 | unitOfMeasureName | String | - |  |
| 13 | requestType | String | - |  |
| 14 | triggerSource | String | - |  |
| 15 | requestedById | String | - | u_mes_mast_user._id |
| 16 | requestedBy | String | - |  |
| 17 | requestedAt | Date | Datetime |  |
| 18 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | fromLocationName | String | - |  |
| 20 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 21 | toLocationName | String | - |  |
| 22 | priority | String | - |  |
| 23 | acknowledgedById | String | - | u_mes_mast_user._id |
| 24 | acknowledgedBy | String | - |  |
| 25 | acknowledgedAt | Date | Datetime |  |
| 26 | deliveredAt | Date | Datetime |  |
| 27 | responseMinutes | Int32 | - |  |
| 28 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 29 | andonEventName | String | - |  |
| 30 | lotId | String | - | u_mes_plan_lot._id |
| 31 | lotName | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_matl_materialConsumption

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 6 | operationExecutionName | String | - |  |
| 7 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 8 | productionOrderName | String | - |  |
| 9 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 10 | wipUnitName | String | - |  |
| 11 | parentLotId | String | - | u_mes_plan_lot._id |
| 12 | parentLotName | String | - |  |
| 13 | componentItemId | String | - | u_mes_prod_item._id |
| 14 | componentItemName | String | - |  |
| 15 | componentLotId | String | - | u_mes_plan_lot._id |
| 16 | componentLotName | String | - |  |
| 17 | componentSerialNo | String | - |  |
| 18 | quantity | Decimal128 | - |  |
| 19 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - |  |
| 21 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 22 | workCenterName | String | - |  |
| 23 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 24 | fromLocationName | String | - |  |
| 25 | consumptionType | String | - |  |
| 26 | scanVerified | Boolean | - |  |
| 27 | consumedAt | Date | Datetime |  |
| 28 | consumedById | String | - | u_mes_mast_user._id |
| 29 | consumedBy | String | - |  |
| 30 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 31 | billOfMaterialName | String | - |  |
| 32 | bomLineNo | Int32 | - |  |
| 33 | erpPosted | Boolean | - |  |
| 34 | erpMessageId | String | - | u_mes_syst_erpMessage._id |
| 35 | erpMessageName | String | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_matl_packagingSpecification

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | customerId | String | - | u_mes_mast_customer._id |
| 8 | customerName | String | - |  |
| 9 | version | Int32 | - |  |
| 10 | containerTypeId | String | - | u_mes_plan_containerType._id |
| 11 | containerTypeName | String | - |  |
| 12 | quantityPerContainer | Int32 | - |  |
| 13 | dunnage | String | - |  |
| 14 | vciRequired | Boolean | - |  |
| 15 | layersPerContainer | Int32 | - |  |
| 16 | unitsPerLayer | Int32 | - |  |
| 17 | containersPerPallet | Int32 | - |  |
| 18 | maxGrossWeightKg | Decimal128 | - |  |
| 19 | unitLabelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 20 | unitLabelTemplateName | String | - |  |
| 21 | containerLabelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 22 | containerLabelTemplateName | String | - |  |
| 23 | instructionControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 24 | instructionControlledDocumentName | String | - |  |
| 25 | approvedByCustomer | Boolean | - |  |
| 26 | effectiveFrom | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_matl_packagingSpecificationLevel

Kind: child | Data class: master | Parent: u_mes_matl_packagingSpecification | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | packagingSpecificationId | String | - | u_mes_matl_packagingSpecification._id |
| 6 | packagingSpecificationName | String | - |  |
| 7 | levelNo | Int32 | - |  |
| 8 | packTypeId | String | - | u_mes_matl_packType._id |
| 9 | packTypeName | String | - |  |
| 10 | quantity | Int32 | - |  |
| 11 | lengthMm | Decimal128 | - |  |
| 12 | widthMm | Decimal128 | - |  |
| 13 | heightMm | Decimal128 | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_matl_labelTemplate

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | labelType | String | - |  |
| 7 | customerId | String | - | u_mes_mast_customer._id |
| 8 | customerName | String | - |  |
| 9 | standard | String | - |  |
| 10 | widthMm | Decimal128 | - |  |
| 11 | heightMm | Decimal128 | - |  |
| 12 | printerLanguage | String | - |  |
| 13 | symbology | String | - |  |
| 14 | payloadPattern | String | - |  |
| 15 | version | Int32 | - |  |
| 16 | copies | Int32 | - |  |
| 17 | effectiveFrom | Date | Date |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_matl_labelTemplateField

Kind: child | Data class: master | Parent: u_mes_matl_labelTemplate | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 6 | labelTemplateName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | fieldName | String | - |  |
| 9 | source | String | - |  |
| 10 | fieldFormat | String | - |  |
| 11 | positionXMm | Decimal128 | - |  |
| 12 | positionYMm | Decimal128 | - |  |
| 13 | isBarcode | Boolean | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_matl_label

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 6 | labelTemplateName | String | - |  |
| 7 | labelType | String | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String | - |  |
| 13 | containerId | String | - | u_mes_plan_container._id |
| 14 | containerName | String | - |  |
| 15 | lotId | String | - | u_mes_plan_lot._id |
| 16 | lotName | String | - |  |
| 17 | shipmentId | String | - | u_mes_matl_shipment._id |
| 18 | shipmentName | String | - |  |
| 19 | payload | String | - |  |
| 20 | humanReadable | String | - |  |
| 21 | printerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 22 | printerIotDeviceName | String | - |  |
| 23 | printedAt | Date | Datetime |  |
| 24 | printedById | String | - | u_mes_mast_user._id |
| 25 | printedBy | String | - |  |
| 26 | copies | Int32 | - |  |
| 27 | reprintCount | Int32 | - |  |
| 28 | reprintReason | String | - |  |
| 29 | verified | Boolean | - |  |
| 30 | verificationGrade | String | - |  |
| 31 | voidedAt | Date | Datetime |  |
| 32 | voidedById | String | - | u_mes_mast_user._id |
| 33 | voidedBy | String | - |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |

## u_mes_matl_shipment

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerId | String | - | u_mes_mast_customer._id |
| 6 | customerName | String | - |  |
| 7 | shipToCode | String | - |  |
| 8 | customerScheduleId | String | - | u_mes_plan_customerSchedule._id |
| 9 | customerScheduleName | String | - |  |
| 10 | invoiceNo | String | - |  |
| 11 | invoiceDate | Date | Date |  |
| 12 | asnNo | String | - |  |
| 13 | asnSentAt | Date | Datetime |  |
| 14 | eWayBillNo | String | - |  |
| 15 | transporterId | String | - | u_mes_mast_transporter._id |
| 16 | transporterName | String | - |  |
| 17 | vehicleNo | String | - |  |
| 18 | driverName | String | - |  |
| 19 | lrNo | String | - |  |
| 20 | totalQuantity | Int32 | - |  |
| 21 | totalContainers | Int32 | - |  |
| 22 | grossWeightKg | Decimal128 | - |  |
| 23 | invoiceValueInr | Decimal128 | - |  |
| 24 | dockLocationId | String | - | u_mes_matl_storageLocation._id |
| 25 | dockLocationName | String | - |  |
| 26 | loadedById | String | - | u_mes_mast_user._id |
| 27 | loadedBy | String | - |  |
| 28 | plannedDispatchAt | Date | Datetime |  |
| 29 | dispatchedAt | Date | Datetime |  |
| 30 | deliveredAt | Date | Datetime |  |
| 31 | podReceivedAt | Date | Datetime |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_matl_shipmentLine

Kind: child | Data class: transaction | Parent: u_mes_matl_shipment | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shipmentId | String | - | u_mes_matl_shipment._id |
| 6 | shipmentName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | customerPartNo | String | - |  |
| 11 | quantity | Int32 | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_matl_shipmentLineContainer

Kind: relationship | Data class: transaction | Parent: u_mes_matl_shipmentLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shipmentLineId | String | - | u_mes_matl_shipmentLine._id |
| 6 | shipmentLineName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | containerId | String | - | u_mes_plan_container._id |
| 9 | containerName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_matl_shipmentLineLot

Kind: relationship | Data class: transaction | Parent: u_mes_matl_shipmentLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shipmentLineId | String | - | u_mes_matl_shipmentLine._id |
| 6 | shipmentLineName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | lotId | String | - | u_mes_plan_lot._id |
| 9 | lotName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_matl_movementType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | erpMovementType | String | - |  |
| 8 | stockEffect | String | - |  |
| 9 | requiresReason | Boolean | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_matl_stockStatus

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | isUsable | Boolean | - |  |
| 8 | erpStockType | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_matl_packType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |
