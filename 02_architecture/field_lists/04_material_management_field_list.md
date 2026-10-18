# Field list - MaterialManagement (matl)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/04_material_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_matl_storageLocation

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | locationType | String | - |  |
| 8 | areaId | String | - | u_mes_mast_area._id |
| 9 | areaName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | parentLocationId | String | - | u_mes_matl_storageLocation._id |
| 13 | parentLocationName | String | - |  |
| 14 | zone | String | - |  |
| 15 | rack | String | - |  |
| 16 | level | Int32 | - |  |
| 17 | bin | String | - |  |
| 18 | capacityQuantity | Int32 | - |  |
| 19 | isQuarantine | Boolean | - |  |
| 20 | isLineSide | Boolean | - |  |
| 21 | mixedLotsAllowed | Boolean | - |  |
| 22 | erpStorageLocation | String | - |  |
| 23 | barcode | String | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_matl_inventoryBalance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | lotId | String | - | u_mes_plan_lot._id |
| 9 | lotName | String | - |  |
| 10 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 11 | storageLocationName | String | - |  |
| 12 | containerId | String | - | u_mes_plan_container._id |
| 13 | containerName | String | - |  |
| 14 | stockStatusId | String | - | u_mes_matl_stockStatus._id |
| 15 | stockStatusName | String | - |  |
| 16 | quantity | Decimal128 | - |  |
| 17 | reservedQuantity | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | valueInr | Decimal128 | - |  |
| 21 | firstReceivedAt | Date | Datetime |  |
| 22 | lastMovementAt | Date | Datetime |  |
| 23 | lastCountedAt | Date | Datetime |  |
| 24 | lastCountedById | String | - | u_mes_mast_user._id |
| 25 | lastCountedBy | String | - |  |
| 26 | expiryAt | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_matl_materialMovement

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | movementTypeId | String | - | u_mes_matl_movementType._id |
| 7 | movementTypeName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | containerId | String | - | u_mes_plan_container._id |
| 13 | containerName | String | - |  |
| 14 | quantity | Decimal128 | - |  |
| 15 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - |  |
| 17 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 18 | fromLocationName | String | - |  |
| 19 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 20 | toLocationName | String | - |  |
| 21 | fromStockStatusId | String | - | u_mes_matl_stockStatus._id |
| 22 | fromStockStatusName | String | - |  |
| 23 | toStockStatusId | String | - | u_mes_matl_stockStatus._id |
| 24 | toStockStatusName | String | - |  |
| 25 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 26 | productionOrderName | String | - |  |
| 27 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 28 | goodsReceiptName | String | - |  |
| 29 | shipmentId | String | - | u_mes_matl_shipment._id |
| 30 | shipmentName | String | - |  |
| 31 | kitId | String | - | u_mes_matl_kit._id |
| 32 | kitName | String | - |  |
| 33 | movedAt | Date | Datetime |  |
| 34 | movedById | String | - | u_mes_mast_user._id |
| 35 | movedBy | String | - |  |
| 36 | scanSource | String | - |  |
| 37 | reasonText | String | - |  |
| 38 | erpDocumentNo | String | - |  |
| 39 | erpMovementType | String | - |  |
| 40 | reversalOfMaterialMovementId | String | - | u_mes_matl_materialMovement._id |
| 41 | reversalOfMaterialMovementName | String | - |  |
| 42 | status | String | - |  |
| 43 | schemaVersion | Int32 | - |  |
| 44 | createdAt | Date | Datetime |  |
| 45 | createdById | String | - | u_mes_mast_user._id |
| 46 | createdBy | String | - |  |
| 47 | updatedAt | Date | Datetime |  |
| 48 | updatedById | String | - | u_mes_mast_user._id |
| 49 | updatedBy | String | - |  |

## u_mes_matl_goodsReceipt

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | supplierId | String | - | u_mes_mast_supplier._id |
| 7 | supplierName | String | - |  |
| 8 | purchaseOrderNo | String | - |  |
| 9 | supplierInvoiceNo | String | - |  |
| 10 | supplierInvoiceDate | Date | Date |  |
| 11 | deliveryChallanNo | String | - |  |
| 12 | vehicleNo | String | - |  |
| 13 | receivedAt | Date | Datetime |  |
| 14 | receivedById | String | - | u_mes_mast_user._id |
| 15 | receivedBy | String | - |  |
| 16 | gateEntryNo | String | - |  |
| 17 | inspectionCompletedAt | Date | Datetime |  |
| 18 | erpGrnNo | String | - |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_matl_goodsReceiptLine

Kind: child | Data class: transaction | Parent: u_mes_matl_goodsReceipt | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 7 | goodsReceiptName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | supplierLotNo | String | - |  |
| 12 | lotId | String | - | u_mes_plan_lot._id |
| 13 | lotName | String | - |  |
| 14 | orderedQuantity | Decimal128 | - |  |
| 15 | receivedQuantity | Decimal128 | - |  |
| 16 | acceptedQuantity | Decimal128 | - |  |
| 17 | rejectedQuantity | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 21 | storageLocationName | String | - |  |
| 22 | certificateReceived | Boolean | - |  |
| 23 | inspectionStatus | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_matl_goodsReceiptLineInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_matl_goodsReceiptLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | goodsReceiptLineId | String | - | u_mes_matl_goodsReceiptLine._id |
| 7 | goodsReceiptLineName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 10 | inspectionResultName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_matl_kit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | kitType | String | - |  |
| 11 | requiredAt | Date | Datetime |  |
| 12 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 13 | toLocationName | String | - |  |
| 14 | pickedById | String | - | u_mes_mast_user._id |
| 15 | pickedBy | String | - |  |
| 16 | pickStartedAt | Date | Datetime |  |
| 17 | pickCompletedAt | Date | Datetime |  |
| 18 | deliveredAt | Date | Datetime |  |
| 19 | receivedById | String | - | u_mes_mast_user._id |
| 20 | receivedBy | String | - |  |
| 21 | isComplete | Boolean | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_matl_kitLine

Kind: child | Data class: transaction | Parent: u_mes_matl_kit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | kitId | String | - | u_mes_matl_kit._id |
| 7 | kitName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | requiredQuantity | Decimal128 | - |  |
| 14 | pickedQuantity | Decimal128 | - |  |
| 15 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 16 | fromLocationName | String | - |  |
| 17 | shortQuantity | Decimal128 | - |  |
| 18 | itemRevision | String | - |  |
| 19 | scannedItemRevision | String | - |  |
| 20 | scannedCode | String | - |  |
| 21 | isMandatory | Boolean | - |  |
| 22 | verifiedAt | Date | Datetime |  |
| 23 | verificationResult | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_matl_materialRequest

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | requestedQuantity | Decimal128 | - |  |
| 11 | deliveredQuantity | Decimal128 | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | requestType | String | - |  |
| 15 | triggerSource | String | - |  |
| 16 | requestedById | String | - | u_mes_mast_user._id |
| 17 | requestedBy | String | - |  |
| 18 | requestedAt | Date | Datetime |  |
| 19 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 20 | fromLocationName | String | - |  |
| 21 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 22 | toLocationName | String | - |  |
| 23 | priority | String | - |  |
| 24 | acknowledgedById | String | - | u_mes_mast_user._id |
| 25 | acknowledgedBy | String | - |  |
| 26 | acknowledgedAt | Date | Datetime |  |
| 27 | deliveredAt | Date | Datetime |  |
| 28 | responseMinutes | Int32 | - |  |
| 29 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 30 | andonEventName | String | - |  |
| 31 | lotId | String | - | u_mes_plan_lot._id |
| 32 | lotName | String | - |  |
| 33 | replenishmentRuleId | String | - | u_mes_matl_replenishmentRule._id |
| 34 | replenishmentRuleName | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_matl_materialConsumption

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - |  |
| 8 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String | - |  |
| 10 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - |  |
| 12 | parentLotId | String | - | u_mes_plan_lot._id |
| 13 | parentLotName | String | - |  |
| 14 | componentItemId | String | - | u_mes_prod_item._id |
| 15 | componentItemName | String | - |  |
| 16 | componentLotId | String | - | u_mes_plan_lot._id |
| 17 | componentLotName | String | - |  |
| 18 | componentSerialNo | String | - |  |
| 19 | quantity | Decimal128 | - |  |
| 20 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 21 | unitOfMeasureName | String | - |  |
| 22 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 23 | workCenterName | String | - |  |
| 24 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 25 | fromLocationName | String | - |  |
| 26 | consumptionType | String | - |  |
| 27 | scanVerified | Boolean | - |  |
| 28 | consumedAt | Date | Datetime |  |
| 29 | consumedById | String | - | u_mes_mast_user._id |
| 30 | consumedBy | String | - |  |
| 31 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 32 | billOfMaterialName | String | - |  |
| 33 | bomLineNo | Int32 | - |  |
| 34 | erpPosted | Boolean | - |  |
| 35 | erpMessageId | String | - | u_mes_syst_erpMessage._id |
| 36 | erpMessageName | String | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_matl_packagingSpecification

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | customerId | String | - | u_mes_mast_customer._id |
| 9 | customerName | String | - |  |
| 10 | version | Int32 | - |  |
| 11 | containerTypeId | String | - | u_mes_plan_containerType._id |
| 12 | containerTypeName | String | - |  |
| 13 | quantityPerContainer | Int32 | - |  |
| 14 | dunnage | String | - |  |
| 15 | vciRequired | Boolean | - |  |
| 16 | layersPerContainer | Int32 | - |  |
| 17 | unitsPerLayer | Int32 | - |  |
| 18 | containersPerPallet | Int32 | - |  |
| 19 | maxGrossWeightKg | Decimal128 | - |  |
| 20 | unitLabelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 21 | unitLabelTemplateName | String | - |  |
| 22 | containerLabelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 23 | containerLabelTemplateName | String | - |  |
| 24 | instructionControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 25 | instructionControlledDocumentName | String | - |  |
| 26 | approvedByCustomer | Boolean | - |  |
| 27 | effectiveFrom | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_matl_packagingSpecificationLevel

Kind: child | Data class: master | Parent: u_mes_matl_packagingSpecification | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | packagingSpecificationId | String | - | u_mes_matl_packagingSpecification._id |
| 7 | packagingSpecificationName | String | - |  |
| 8 | levelNo | Int32 | - |  |
| 9 | packTypeId | String | - | u_mes_matl_packType._id |
| 10 | packTypeName | String | - |  |
| 11 | quantity | Int32 | - |  |
| 12 | lengthMm | Decimal128 | - |  |
| 13 | widthMm | Decimal128 | - |  |
| 14 | heightMm | Decimal128 | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_matl_labelTemplate

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | labelType | String | - |  |
| 8 | customerId | String | - | u_mes_mast_customer._id |
| 9 | customerName | String | - |  |
| 10 | standard | String | - |  |
| 11 | widthMm | Decimal128 | - |  |
| 12 | heightMm | Decimal128 | - |  |
| 13 | printerLanguage | String | - |  |
| 14 | symbology | String | - |  |
| 15 | payloadPattern | String | - |  |
| 16 | version | Int32 | - |  |
| 17 | copies | Int32 | - |  |
| 18 | effectiveFrom | Date | Date |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_matl_labelTemplateField

Kind: child | Data class: master | Parent: u_mes_matl_labelTemplate | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 7 | labelTemplateName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | fieldName | String | - |  |
| 10 | source | String | - |  |
| 11 | fieldFormat | String | - |  |
| 12 | positionXMm | Decimal128 | - |  |
| 13 | positionYMm | Decimal128 | - |  |
| 14 | isBarcode | Boolean | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_matl_label

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 7 | labelTemplateName | String | - |  |
| 8 | labelType | String | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 13 | wipUnitName | String | - |  |
| 14 | containerId | String | - | u_mes_plan_container._id |
| 15 | containerName | String | - |  |
| 16 | lotId | String | - | u_mes_plan_lot._id |
| 17 | lotName | String | - |  |
| 18 | shipmentId | String | - | u_mes_matl_shipment._id |
| 19 | shipmentName | String | - |  |
| 20 | payload | String | - |  |
| 21 | humanReadable | String | - |  |
| 22 | printerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 23 | printerIotDeviceName | String | - |  |
| 24 | printedAt | Date | Datetime |  |
| 25 | printedById | String | - | u_mes_mast_user._id |
| 26 | printedBy | String | - |  |
| 27 | copies | Int32 | - |  |
| 28 | reprintCount | Int32 | - |  |
| 29 | reprintReason | String | - |  |
| 30 | verified | Boolean | - |  |
| 31 | verificationGrade | String | - |  |
| 32 | voidedAt | Date | Datetime |  |
| 33 | voidedById | String | - | u_mes_mast_user._id |
| 34 | voidedBy | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_matl_shipment

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerId | String | - | u_mes_mast_customer._id |
| 7 | customerName | String | - |  |
| 8 | shipToCode | String | - |  |
| 9 | customerScheduleId | String | - | u_mes_plan_customerSchedule._id |
| 10 | customerScheduleName | String | - |  |
| 11 | invoiceNo | String | - |  |
| 12 | invoiceDate | Date | Date |  |
| 13 | asnNo | String | - |  |
| 14 | asnSentAt | Date | Datetime |  |
| 15 | eWayBillNo | String | - |  |
| 16 | transporterId | String | - | u_mes_mast_transporter._id |
| 17 | transporterName | String | - |  |
| 18 | vehicleNo | String | - |  |
| 19 | driverName | String | - |  |
| 20 | lrNo | String | - |  |
| 21 | totalQuantity | Int32 | - |  |
| 22 | totalContainers | Int32 | - |  |
| 23 | grossWeightKg | Decimal128 | - |  |
| 24 | invoiceValueInr | Decimal128 | - |  |
| 25 | dockLocationId | String | - | u_mes_matl_storageLocation._id |
| 26 | dockLocationName | String | - |  |
| 27 | loadedById | String | - | u_mes_mast_user._id |
| 28 | loadedBy | String | - |  |
| 29 | plannedDispatchAt | Date | Datetime |  |
| 30 | dispatchedAt | Date | Datetime |  |
| 31 | deliveredAt | Date | Datetime |  |
| 32 | podReceivedAt | Date | Datetime |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_matl_shipmentLine

Kind: child | Data class: transaction | Parent: u_mes_matl_shipment | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shipmentId | String | - | u_mes_matl_shipment._id |
| 7 | shipmentName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | customerPartNo | String | - |  |
| 12 | quantity | Int32 | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_matl_shipmentLineContainer

Kind: relationship | Data class: transaction | Parent: u_mes_matl_shipmentLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shipmentLineId | String | - | u_mes_matl_shipmentLine._id |
| 7 | shipmentLineName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | containerId | String | - | u_mes_plan_container._id |
| 10 | containerName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_matl_shipmentLineLot

Kind: relationship | Data class: transaction | Parent: u_mes_matl_shipmentLine | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shipmentLineId | String | - | u_mes_matl_shipmentLine._id |
| 7 | shipmentLineName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_matl_movementType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | erpMovementType | String | - |  |
| 9 | stockEffect | String | - |  |
| 10 | requiresReason | Boolean | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_matl_stockStatus

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | isUsable | Boolean | - |  |
| 9 | erpStockType | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_matl_packType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_matl_exposureTimer

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | lotId | String | - | u_mes_plan_lot._id |
| 9 | lotName | String | - |  |
| 10 | containerId | String | - | u_mes_plan_container._id |
| 11 | containerName | String | - |  |
| 12 | timerType | String | - |  |
| 13 | limitMinutes | Int32 | - |  |
| 14 | startedAt | Date | Datetime |  |
| 15 | pausedAt | Date | Datetime |  |
| 16 | accumulatedMinutes | Int32 | - |  |
| 17 | expiresAt | Date | Datetime |  |
| 18 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | storageLocationName | String | - |  |
| 20 | resetReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 21 | resetReasonCodeName | String | - |  |
| 22 | resetById | String | - | u_mes_mast_user._id |
| 23 | resetBy | String | - |  |
| 24 | resetAt | Date | Datetime |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |
| 27 | createdAt | Date | Datetime |  |
| 28 | createdById | String | - | u_mes_mast_user._id |
| 29 | createdBy | String | - |  |
| 30 | updatedAt | Date | Datetime |  |
| 31 | updatedById | String | - | u_mes_mast_user._id |
| 32 | updatedBy | String | - |  |

## u_mes_matl_replenishmentRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | toLocationId | String | - | u_mes_matl_storageLocation._id |
| 9 | toLocationName | String | - |  |
| 10 | fromLocationId | String | - | u_mes_matl_storageLocation._id |
| 11 | fromLocationName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | triggerType | String | - |  |
| 15 | minQuantity | Decimal128 | - |  |
| 16 | maxQuantity | Decimal128 | - |  |
| 17 | reorderPointQuantity | Decimal128 | - |  |
| 18 | kanbanQuantity | Decimal128 | - |  |
| 19 | kanbanCount | Int32 | - |  |
| 20 | containerTypeId | String | - | u_mes_plan_containerType._id |
| 21 | containerTypeName | String | - |  |
| 22 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 23 | unitOfMeasureName | String | - |  |
| 24 | leadTimeMinutes | Int32 | - |  |
| 25 | validFrom | Date | Date |  |
| 26 | validTo | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_matl_materialDemandForecast

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | productionDate | Date | Date |  |
| 11 | bucketStartAt | Date | Datetime |  |
| 12 | bucketEndAt | Date | Datetime |  |
| 13 | scheduledDemand | Decimal128 | - |  |
| 14 | consumptionRatePerHour | Decimal128 | - |  |
| 15 | onHandQuantity | Decimal128 | - |  |
| 16 | projectedOnHand | Decimal128 | - |  |
| 17 | projectedShortageAt | Date | Datetime |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | method | String | - |  |
| 21 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 22 | analyticsModelName | String | - |  |
| 23 | calculatedAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_matl_storageLocationAllowedItem

Kind: relationship | Data class: master | Parent: u_mes_matl_storageLocation | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 7 | storageLocationName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | itemGroupId | String | - | u_mes_prod_itemGroup._id |
| 12 | itemGroupName | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_matl_dispenseRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | dispenseMethod | String | - |  |
| 13 | targetWeight | Decimal128 | - |  |
| 14 | tolerancePct | Decimal128 | - |  |
| 15 | tareWeight | Decimal128 | - |  |
| 16 | grossWeight | Decimal128 | - |  |
| 17 | netWeight | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | pieceCount | Int32 | - |  |
| 21 | withinTolerance | Boolean | - |  |
| 22 | balanceGaugeId | String | - | u_mes_qual_gauge._id |
| 23 | balanceGaugeName | String | - |  |
| 24 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 25 | storageLocationName | String | - |  |
| 26 | dispensedById | String | - | u_mes_mast_user._id |
| 27 | dispensedBy | String | - |  |
| 28 | dispensedAt | Date | Datetime |  |
| 29 | verificationMethod | String | - |  |
| 30 | verifiedById | String | - | u_mes_mast_user._id |
| 31 | verifiedBy | String | - |  |
| 32 | verifiedAt | Date | Datetime |  |
| 33 | labelId | String | - | u_mes_matl_label._id |
| 34 | labelName | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |
