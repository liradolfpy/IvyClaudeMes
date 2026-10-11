# Field list - Materials (mat)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/04_materials/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mat_storageLocation

Kind: entity | Data class: master | Parent: - | _id pattern: LOC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | locationType | String |  |
| 7 | areaId | String | u_mes_mdm_area._id |
| 8 | areaName | String |  |
| 9 | workCenterId | String | u_mes_mdm_workCenter._id |
| 10 | workCenterName | String |  |
| 11 | parentLocationId | String | u_mes_mat_storageLocation._id |
| 12 | parentLocationName | String |  |
| 13 | zone | String |  |
| 14 | rack | String |  |
| 15 | level | Int32 |  |
| 16 | bin | String |  |
| 17 | capacityQuantity | Int32 |  |
| 18 | isQuarantine | Boolean |  |
| 19 | isLineSide | Boolean |  |
| 20 | mixedLotsAllowed | Boolean |  |
| 21 | erpStorageLocation | String |  |
| 22 | barcode | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_mat_inventoryBalance

Kind: entity | Data class: transaction | Parent: - | _id pattern: INV-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | lotId | String | u_mes_exe_lot._id |
| 8 | lotName | String |  |
| 9 | storageLocationId | String | u_mes_mat_storageLocation._id |
| 10 | storageLocationName | String |  |
| 11 | containerId | String | u_mes_exe_container._id |
| 12 | containerName | String |  |
| 13 | stockStatus | String |  |
| 14 | quantity | Decimal128 |  |
| 15 | reservedQuantity | Decimal128 |  |
| 16 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 17 | unitOfMeasureName | String |  |
| 18 | valueInr | Decimal128 |  |
| 19 | firstReceivedAt | Date |  |
| 20 | lastMovementAt | Date |  |
| 21 | lastCountedAt | Date |  |
| 22 | lastCountedById | String | u_mes_mdm_user._id |
| 23 | lastCountedBy | String |  |
| 24 | expiryAt | Date |  |
| 25 | status | String |  |
| 26 | schemaVersion | Int32 |  |
| 27 | createdAt | Date |  |
| 28 | createdById | String | u_mes_mdm_user._id |
| 29 | createdBy | String |  |
| 30 | updatedAt | Date |  |
| 31 | updatedById | String | u_mes_mdm_user._id |
| 32 | updatedBy | String |  |

## u_mes_mat_materialMovement

Kind: entity | Data class: transaction | Parent: - | _id pattern: MM-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | movementType | String |  |
| 6 | itemId | String | u_mes_prd_item._id |
| 7 | itemName | String |  |
| 8 | lotId | String | u_mes_exe_lot._id |
| 9 | lotName | String |  |
| 10 | containerId | String | u_mes_exe_container._id |
| 11 | containerName | String |  |
| 12 | quantity | Decimal128 |  |
| 13 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 14 | unitOfMeasureName | String |  |
| 15 | fromLocationId | String | u_mes_mat_storageLocation._id |
| 16 | fromLocationName | String |  |
| 17 | toLocationId | String | u_mes_mat_storageLocation._id |
| 18 | toLocationName | String |  |
| 19 | fromStockStatus | String |  |
| 20 | toStockStatus | String |  |
| 21 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 22 | productionOrderName | String |  |
| 23 | goodsReceiptId | String | u_mes_mat_goodsReceipt._id |
| 24 | goodsReceiptName | String |  |
| 25 | shipmentId | String | u_mes_mat_shipment._id |
| 26 | shipmentName | String |  |
| 27 | kitId | String | u_mes_mat_kit._id |
| 28 | kitName | String |  |
| 29 | movedAt | Date |  |
| 30 | movedById | String | u_mes_mdm_user._id |
| 31 | movedBy | String |  |
| 32 | scanSource | String |  |
| 33 | reasonText | String |  |
| 34 | erpDocumentNo | String |  |
| 35 | erpMovementType | String |  |
| 36 | reversalOfMaterialMovementId | String | u_mes_mat_materialMovement._id |
| 37 | reversalOfMaterialMovementName | String |  |
| 38 | status | String |  |
| 39 | schemaVersion | Int32 |  |
| 40 | createdAt | Date |  |
| 41 | createdById | String | u_mes_mdm_user._id |
| 42 | createdBy | String |  |
| 43 | updatedAt | Date |  |
| 44 | updatedById | String | u_mes_mdm_user._id |
| 45 | updatedBy | String |  |

## u_mes_mat_goodsReceipt

Kind: entity | Data class: transaction | Parent: - | _id pattern: GRN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | supplierId | String | u_mes_mdm_supplier._id |
| 6 | supplierName | String |  |
| 7 | purchaseOrderNo | String |  |
| 8 | supplierInvoiceNo | String |  |
| 9 | supplierInvoiceDate | Date |  |
| 10 | deliveryChallanNo | String |  |
| 11 | vehicleNo | String |  |
| 12 | receivedAt | Date |  |
| 13 | receivedById | String | u_mes_mdm_user._id |
| 14 | receivedBy | String |  |
| 15 | gateEntryNo | String |  |
| 16 | inspectionCompletedAt | Date |  |
| 17 | erpGrnNo | String |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |
| 20 | createdAt | Date |  |
| 21 | createdById | String | u_mes_mdm_user._id |
| 22 | createdBy | String |  |
| 23 | updatedAt | Date |  |
| 24 | updatedById | String | u_mes_mdm_user._id |
| 25 | updatedBy | String |  |

## u_mes_mat_goodsReceiptLine

Kind: child | Data class: transaction | Parent: u_mes_mat_goodsReceipt | _id pattern: <goodsReceiptId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | goodsReceiptId | String | u_mes_mat_goodsReceipt._id |
| 6 | goodsReceiptName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | supplierLotNo | String |  |
| 11 | lotId | String | u_mes_exe_lot._id |
| 12 | lotName | String |  |
| 13 | orderedQuantity | Decimal128 |  |
| 14 | receivedQuantity | Decimal128 |  |
| 15 | acceptedQuantity | Decimal128 |  |
| 16 | rejectedQuantity | Decimal128 |  |
| 17 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 18 | unitOfMeasureName | String |  |
| 19 | storageLocationId | String | u_mes_mat_storageLocation._id |
| 20 | storageLocationName | String |  |
| 21 | certificateReceived | Boolean |  |
| 22 | inspectionStatus | String |  |
| 23 | schemaVersion | Int32 |  |
| 24 | createdAt | Date |  |
| 25 | createdById | String | u_mes_mdm_user._id |
| 26 | createdBy | String |  |
| 27 | updatedAt | Date |  |
| 28 | updatedById | String | u_mes_mdm_user._id |
| 29 | updatedBy | String |  |

## u_mes_mat_goodsReceiptLineInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_mat_goodsReceiptLine | _id pattern: <goodsReceiptLineId>-IR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | goodsReceiptLineId | String | u_mes_mat_goodsReceiptLine._id |
| 6 | goodsReceiptLineName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | inspectionResultId | String | u_mes_qlt_inspectionResult._id |
| 9 | inspectionResultName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_mat_kit

Kind: entity | Data class: transaction | Parent: - | _id pattern: KIT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 6 | productionOrderName | String |  |
| 7 | workCenterId | String | u_mes_mdm_workCenter._id |
| 8 | workCenterName | String |  |
| 9 | kitType | String |  |
| 10 | requiredAt | Date |  |
| 11 | toLocationId | String | u_mes_mat_storageLocation._id |
| 12 | toLocationName | String |  |
| 13 | pickedById | String | u_mes_mdm_user._id |
| 14 | pickedBy | String |  |
| 15 | pickStartedAt | Date |  |
| 16 | pickCompletedAt | Date |  |
| 17 | deliveredAt | Date |  |
| 18 | receivedById | String | u_mes_mdm_user._id |
| 19 | receivedBy | String |  |
| 20 | isComplete | Boolean |  |
| 21 | status | String |  |
| 22 | schemaVersion | Int32 |  |
| 23 | createdAt | Date |  |
| 24 | createdById | String | u_mes_mdm_user._id |
| 25 | createdBy | String |  |
| 26 | updatedAt | Date |  |
| 27 | updatedById | String | u_mes_mdm_user._id |
| 28 | updatedBy | String |  |

## u_mes_mat_kitLine

Kind: child | Data class: transaction | Parent: u_mes_mat_kit | _id pattern: <kitId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | kitId | String | u_mes_mat_kit._id |
| 6 | kitName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | lotId | String | u_mes_exe_lot._id |
| 11 | lotName | String |  |
| 12 | requiredQuantity | Decimal128 |  |
| 13 | pickedQuantity | Decimal128 |  |
| 14 | fromLocationId | String | u_mes_mat_storageLocation._id |
| 15 | fromLocationName | String |  |
| 16 | shortQuantity | Decimal128 |  |
| 17 | schemaVersion | Int32 |  |
| 18 | createdAt | Date |  |
| 19 | createdById | String | u_mes_mdm_user._id |
| 20 | createdBy | String |  |
| 21 | updatedAt | Date |  |
| 22 | updatedById | String | u_mes_mdm_user._id |
| 23 | updatedBy | String |  |

## u_mes_mat_materialRequest

Kind: entity | Data class: transaction | Parent: - | _id pattern: MRQ-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | itemId | String | u_mes_prd_item._id |
| 8 | itemName | String |  |
| 9 | requestedQuantity | Decimal128 |  |
| 10 | deliveredQuantity | Decimal128 |  |
| 11 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 12 | unitOfMeasureName | String |  |
| 13 | requestType | String |  |
| 14 | triggerSource | String |  |
| 15 | requestedById | String | u_mes_mdm_user._id |
| 16 | requestedBy | String |  |
| 17 | requestedAt | Date |  |
| 18 | fromLocationId | String | u_mes_mat_storageLocation._id |
| 19 | fromLocationName | String |  |
| 20 | toLocationId | String | u_mes_mat_storageLocation._id |
| 21 | toLocationName | String |  |
| 22 | priority | String |  |
| 23 | acknowledgedById | String | u_mes_mdm_user._id |
| 24 | acknowledgedBy | String |  |
| 25 | acknowledgedAt | Date |  |
| 26 | deliveredAt | Date |  |
| 27 | responseMinutes | Int32 |  |
| 28 | andonEventId | String | u_mes_ehs_andonEvent._id |
| 29 | andonEventName | String |  |
| 30 | lotId | String | u_mes_exe_lot._id |
| 31 | lotName | String |  |
| 32 | status | String |  |
| 33 | schemaVersion | Int32 |  |
| 34 | createdAt | Date |  |
| 35 | createdById | String | u_mes_mdm_user._id |
| 36 | createdBy | String |  |
| 37 | updatedAt | Date |  |
| 38 | updatedById | String | u_mes_mdm_user._id |
| 39 | updatedBy | String |  |

## u_mes_mat_materialConsumption

Kind: entity | Data class: transaction | Parent: - | _id pattern: CON-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operationExecutionId | String | u_mes_exe_operationExecution._id |
| 6 | operationExecutionName | String |  |
| 7 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 8 | productionOrderName | String |  |
| 9 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 10 | wipUnitName | String |  |
| 11 | parentLotId | String | u_mes_exe_lot._id |
| 12 | parentLotName | String |  |
| 13 | componentItemId | String | u_mes_prd_item._id |
| 14 | componentItemName | String |  |
| 15 | componentLotId | String | u_mes_exe_lot._id |
| 16 | componentLotName | String |  |
| 17 | componentSerialNo | String |  |
| 18 | quantity | Decimal128 |  |
| 19 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 20 | unitOfMeasureName | String |  |
| 21 | workCenterId | String | u_mes_mdm_workCenter._id |
| 22 | workCenterName | String |  |
| 23 | fromLocationId | String | u_mes_mat_storageLocation._id |
| 24 | fromLocationName | String |  |
| 25 | consumptionType | String |  |
| 26 | scanVerified | Boolean |  |
| 27 | consumedAt | Date |  |
| 28 | consumedById | String | u_mes_mdm_user._id |
| 29 | consumedBy | String |  |
| 30 | billOfMaterialId | String | u_mes_prd_billOfMaterial._id |
| 31 | billOfMaterialName | String |  |
| 32 | bomLineNo | Int32 |  |
| 33 | erpPosted | Boolean |  |
| 34 | erpMessageId | String | u_mes_sys_erpMessage._id |
| 35 | erpMessageName | String |  |
| 36 | status | String |  |
| 37 | schemaVersion | Int32 |  |
| 38 | createdAt | Date |  |
| 39 | createdById | String | u_mes_mdm_user._id |
| 40 | createdBy | String |  |
| 41 | updatedAt | Date |  |
| 42 | updatedById | String | u_mes_mdm_user._id |
| 43 | updatedBy | String |  |

## u_mes_mat_packagingSpecification

Kind: entity | Data class: master | Parent: - | _id pattern: PKS-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | customerId | String | u_mes_mdm_customer._id |
| 8 | customerName | String |  |
| 9 | version | Int32 |  |
| 10 | containerType | String |  |
| 11 | quantityPerContainer | Int32 |  |
| 12 | dunnage | String |  |
| 13 | vciRequired | Boolean |  |
| 14 | layersPerContainer | Int32 |  |
| 15 | unitsPerLayer | Int32 |  |
| 16 | containersPerPallet | Int32 |  |
| 17 | maxGrossWeightKg | Decimal128 |  |
| 18 | unitLabelTemplateId | String | u_mes_mat_labelTemplate._id |
| 19 | unitLabelTemplateName | String |  |
| 20 | containerLabelTemplateId | String | u_mes_mat_labelTemplate._id |
| 21 | containerLabelTemplateName | String |  |
| 22 | instructionControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 23 | instructionControlledDocumentName | String |  |
| 24 | approvedByCustomer | Boolean |  |
| 25 | effectiveFrom | Date |  |
| 26 | status | String |  |
| 27 | schemaVersion | Int32 |  |

## u_mes_mat_packagingSpecificationLevel

Kind: child | Data class: master | Parent: u_mes_mat_packagingSpecification | _id pattern: <packagingSpecificationId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | packagingSpecificationId | String | u_mes_mat_packagingSpecification._id |
| 6 | packagingSpecificationName | String |  |
| 7 | levelNo | Int32 |  |
| 8 | packType | String |  |
| 9 | quantity | Int32 |  |
| 10 | lengthMm | Decimal128 |  |
| 11 | widthMm | Decimal128 |  |
| 12 | heightMm | Decimal128 |  |
| 13 | schemaVersion | Int32 |  |

## u_mes_mat_labelTemplate

Kind: entity | Data class: master | Parent: - | _id pattern: LBT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | labelType | String |  |
| 7 | customerId | String | u_mes_mdm_customer._id |
| 8 | customerName | String |  |
| 9 | standard | String |  |
| 10 | widthMm | Decimal128 |  |
| 11 | heightMm | Decimal128 |  |
| 12 | printerLanguage | String |  |
| 13 | symbology | String |  |
| 14 | payloadPattern | String |  |
| 15 | version | Int32 |  |
| 16 | copies | Int32 |  |
| 17 | effectiveFrom | Date |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |

## u_mes_mat_labelTemplateField

Kind: child | Data class: master | Parent: u_mes_mat_labelTemplate | _id pattern: <labelTemplateId>-F<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | labelTemplateId | String | u_mes_mat_labelTemplate._id |
| 6 | labelTemplateName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | fieldName | String |  |
| 9 | source | String |  |
| 10 | fieldFormat | String |  |
| 11 | positionXMm | Decimal128 |  |
| 12 | positionYMm | Decimal128 |  |
| 13 | isBarcode | Boolean |  |
| 14 | schemaVersion | Int32 |  |

## u_mes_mat_label

Kind: entity | Data class: transaction | Parent: - | _id pattern: LBL-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | labelTemplateId | String | u_mes_mat_labelTemplate._id |
| 6 | labelTemplateName | String |  |
| 7 | labelType | String |  |
| 8 | relatedCollectionName | String |  |
| 9 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String |  |
| 11 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 12 | wipUnitName | String |  |
| 13 | containerId | String | u_mes_exe_container._id |
| 14 | containerName | String |  |
| 15 | lotId | String | u_mes_exe_lot._id |
| 16 | lotName | String |  |
| 17 | shipmentId | String | u_mes_mat_shipment._id |
| 18 | shipmentName | String |  |
| 19 | payload | String |  |
| 20 | humanReadable | String |  |
| 21 | printerIotDeviceId | String | u_mes_sys_iotDevice._id |
| 22 | printerIotDeviceName | String |  |
| 23 | printedAt | Date |  |
| 24 | printedById | String | u_mes_mdm_user._id |
| 25 | printedBy | String |  |
| 26 | copies | Int32 |  |
| 27 | reprintCount | Int32 |  |
| 28 | reprintReason | String |  |
| 29 | verified | Boolean |  |
| 30 | verificationGrade | String |  |
| 31 | voidedAt | Date |  |
| 32 | voidedById | String | u_mes_mdm_user._id |
| 33 | voidedBy | String |  |
| 34 | status | String |  |
| 35 | schemaVersion | Int32 |  |
| 36 | createdAt | Date |  |
| 37 | createdById | String | u_mes_mdm_user._id |
| 38 | createdBy | String |  |
| 39 | updatedAt | Date |  |
| 40 | updatedById | String | u_mes_mdm_user._id |
| 41 | updatedBy | String |  |

## u_mes_mat_shipment

Kind: entity | Data class: transaction | Parent: - | _id pattern: SHP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerId | String | u_mes_mdm_customer._id |
| 6 | customerName | String |  |
| 7 | shipToCode | String |  |
| 8 | customerScheduleId | String | u_mes_exe_customerSchedule._id |
| 9 | customerScheduleName | String |  |
| 10 | invoiceNo | String |  |
| 11 | invoiceDate | Date |  |
| 12 | asnNo | String |  |
| 13 | asnSentAt | Date |  |
| 14 | eWayBillNo | String |  |
| 15 | transporter | String |  |
| 16 | vehicleNo | String |  |
| 17 | driverName | String |  |
| 18 | lrNo | String |  |
| 19 | totalQuantity | Int32 |  |
| 20 | totalContainers | Int32 |  |
| 21 | grossWeightKg | Decimal128 |  |
| 22 | invoiceValueInr | Decimal128 |  |
| 23 | dockLocationId | String | u_mes_mat_storageLocation._id |
| 24 | dockLocationName | String |  |
| 25 | loadedById | String | u_mes_mdm_user._id |
| 26 | loadedBy | String |  |
| 27 | plannedDispatchAt | Date |  |
| 28 | dispatchedAt | Date |  |
| 29 | deliveredAt | Date |  |
| 30 | podReceivedAt | Date |  |
| 31 | status | String |  |
| 32 | schemaVersion | Int32 |  |
| 33 | createdAt | Date |  |
| 34 | createdById | String | u_mes_mdm_user._id |
| 35 | createdBy | String |  |
| 36 | updatedAt | Date |  |
| 37 | updatedById | String | u_mes_mdm_user._id |
| 38 | updatedBy | String |  |

## u_mes_mat_shipmentLine

Kind: child | Data class: transaction | Parent: u_mes_mat_shipment | _id pattern: <shipmentId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shipmentId | String | u_mes_mat_shipment._id |
| 6 | shipmentName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | customerPartNo | String |  |
| 11 | quantity | Int32 |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_mat_shipmentLineContainer

Kind: relationship | Data class: transaction | Parent: u_mes_mat_shipmentLine | _id pattern: <shipmentLineId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shipmentLineId | String | u_mes_mat_shipmentLine._id |
| 6 | shipmentLineName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | containerId | String | u_mes_exe_container._id |
| 9 | containerName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_mat_shipmentLineLot

Kind: relationship | Data class: transaction | Parent: u_mes_mat_shipmentLine | _id pattern: <shipmentLineId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shipmentLineId | String | u_mes_mat_shipmentLine._id |
| 6 | shipmentLineName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lotId | String | u_mes_exe_lot._id |
| 9 | lotName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |
