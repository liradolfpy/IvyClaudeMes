## u_mes_matl_dispenseRecord - Dispense Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_dispenseRecord.json | _id: mes_matl_dispenseRecordStable | rel: CL20261018-23:51 | samples: 10 | columns: 26 | total width: 3920px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | itemName | Item | String | 48 | 300px | left |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | dispenseMethod | Dispense Method | String | 20 | 160px | left |
| 6 | targetWeight | Target Weight | Decimal128 | 5 | 140px | right |
| 7 | tolerancePct | Tolerance (%) | Decimal128 | 3 | 140px | right |
| 8 | tareWeight | Tare Weight | Decimal128 | 4 | 120px | right |
| 9 | grossWeight | Gross Weight | Decimal128 | 6 | 130px | right |
| 10 | netWeight | Net Weight | Decimal128 | 6 | 110px | right |
| 11 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 12 | pieceCount | Piece Count | Int32 | 0 | 120px | right |
| 13 | withinTolerance | Within Tolerance | Boolean | 3 | 160px | center |
| 14 | balanceGaugeName | Balance Gauge | String | 33 | 260px | left |
| 15 | storageLocationName | Storage Location | String | 24 | 190px | left |
| 16 | dispensedBy | Dispensed By | String | 14 | 130px | left |
| 17 | dispensedAt | Dispensed At | Date/Datetime | 19 | 160px | center |
| 18 | verificationMethod | Verification Method | String | 13 | 180px | left |
| 19 | verifiedBy | Verified By | String | 18 | 150px | left |
| 20 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 21 | labelName | Label | String | 0 | 80px | left |
| 22 | status | Status | String | 8 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); unitOfMeasureId (reference key, shown through unitOfMeasureName); balanceGaugeId (reference key, shown through balanceGaugeName); storageLocationId (reference key, shown through storageLocationName); dispensedById (reference key, shown through dispensedBy); verifiedById (reference key, shown through verifiedBy); labelId (reference key, shown through labelName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): pieceCount, labelName

## u_mes_matl_exposureTimer - Exposure Timers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_exposureTimer.json | _id: mes_matl_exposureTimerStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 2870px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | itemName | Item | String | 33 | 260px | left |
| 3 | lotName | Lot | String | 15 | 130px | left |
| 4 | containerName | Container | String | 0 | 110px | left |
| 5 | timerType | Timer Type | String | 9 | 110px | left |
| 6 | limitMinutes | Limit (min) | Int32 | 3 | 120px | right |
| 7 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 8 | pausedAt | Paused At | Date/Datetime | 19 | 160px | center |
| 9 | accumulatedMinutes | Accumulated (min) | Int32 | 3 | 160px | right |
| 10 | expiresAt | Expires At | Date/Datetime | 19 | 160px | center |
| 11 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 12 | resetReasonCodeName | Reset Reason Code | String | 19 | 160px | left |
| 13 | resetBy | Reset By | String | 14 | 120px | left |
| 14 | resetAt | Reset At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 8 | 90px | left |
| 16 | createdBy | Created By | String | 14 | 120px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 14 | 120px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); containerId (reference key, shown through containerName); storageLocationId (reference key, shown through storageLocationName); resetReasonCodeId (reference key, shown through resetReasonCodeName); resetById (reference key, shown through resetBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): containerName

## u_mes_matl_goodsReceipt - Goods Receipts (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_goodsReceipt.json | _id: mes_matl_goodsReceiptStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | supplierName | Supplier | String | 44 | 300px | left |
| 3 | purchaseOrderNo | Purchase Order No | String | 10 | 160px | left |
| 4 | supplierInvoiceNo | Supplier Invoice No | String | 14 | 180px | left |
| 5 | supplierInvoiceDate | Supplier Invoice Date | Date/Date | 10 | 190px | center |
| 6 | deliveryChallanNo | Delivery Challan No | String | 8 | 180px | left |
| 7 | vehicleNo | Vehicle No | String | 12 | 110px | left |
| 8 | receivedAt | Received At | Date/Datetime | 19 | 160px | center |
| 9 | receivedBy | Received By | String | 14 | 120px | left |
| 10 | gateEntryNo | Gate Entry No | String | 14 | 140px | left |
| 11 | inspectionCompletedAt | Inspection Completed At | Date/Datetime | 19 | 210px | center |
| 12 | erpGrnNo | ERP Grn No | String | 10 | 110px | left |
| 13 | status | Status | String | 18 | 150px | left |
| 14 | createdBy | Created By | String | 14 | 120px | left |
| 15 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 16 | updatedBy | Updated By | String | 14 | 120px | left |
| 17 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); supplierId (reference key, shown through supplierName); receivedById (reference key, shown through receivedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_goodsReceiptLine - Goods Receipt Lines (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_goodsReceiptLine.json | _id: mes_matl_goodsReceiptLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 18 | total width: 2930px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | goodsReceiptName | Goods Receipt | String | 15 | 140px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | itemName | Item | String | 39 | 300px | left |
| 5 | supplierLotNo | Supplier Lot No | String | 13 | 150px | left |
| 6 | lotName | Lot | String | 15 | 130px | left |
| 7 | orderedQuantity | Ordered Quantity | Decimal128 | 6 | 160px | right |
| 8 | receivedQuantity | Received Quantity | Decimal128 | 6 | 160px | right |
| 9 | acceptedQuantity | Accepted Quantity | Decimal128 | 6 | 160px | right |
| 10 | rejectedQuantity | Rejected Quantity | Decimal128 | 4 | 160px | right |
| 11 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 12 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 13 | certificateReceived | Certificate Received | Boolean | 3 | 180px | center |
| 14 | inspectionStatus | Inspection Status | String | 24 | 190px | left |
| 15 | createdBy | Created By | String | 12 | 110px | left |
| 16 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 17 | updatedBy | Updated By | String | 12 | 110px | left |
| 18 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); goodsReceiptId (reference key, shown through goodsReceiptName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); unitOfMeasureId (reference key, shown through unitOfMeasureName); storageLocationId (reference key, shown through storageLocationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_goodsReceiptLineInspectionResult - Goods Receipt Line Inspection Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_goodsReceiptLineInspectionResult.json | _id: mes_matl_goodsReceiptLineInspectionResultStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1180px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 24 | 190px | left |
| 2 | goodsReceiptLineName | Goods Receipt Line | String | 19 | 170px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 5 | createdBy | Created By | String | 12 | 110px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 12 | 110px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); goodsReceiptLineId (reference key, shown through goodsReceiptLineName); inspectionResultId (reference key, shown through inspectionResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_inventoryBalance - Inventory Balances (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_inventoryBalance.json | _id: mes_matl_inventoryBalanceStable | rel: CL20261018-23:51 | samples: 10 | columns: 20 | total width: 2940px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | itemName | Item | String | 39 | 300px | left |
| 3 | lotName | Lot | String | 15 | 130px | left |
| 4 | storageLocationName | Storage Location | String | 32 | 250px | left |
| 5 | containerName | Container | String | 9 | 110px | left |
| 6 | stockStatusName | Stock Status | String | 12 | 130px | left |
| 7 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 8 | reservedQuantity | Reserved Quantity | Decimal128 | 1 | 160px | right |
| 9 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 10 | valueInr | Value (INR) | Decimal128 | 8 | 120px | right |
| 11 | firstReceivedAt | First Received At | Date/Datetime | 19 | 160px | center |
| 12 | lastMovementAt | Last Movement At | Date/Datetime | 0 | 160px | center |
| 13 | lastCountedAt | Last Counted At | Date/Datetime | 0 | 150px | center |
| 14 | lastCountedBy | Last Counted By | String | 0 | 150px | left |
| 15 | expiryAt | Expiry At | Date/Date | 10 | 110px | center |
| 16 | status | Status | String | 6 | 90px | left |
| 17 | createdBy | Created By | String | 12 | 110px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 12 | 110px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); storageLocationId (reference key, shown through storageLocationName); containerId (reference key, shown through containerName); stockStatusId (reference key, shown through stockStatusName); unitOfMeasureId (reference key, shown through unitOfMeasureName); lastCountedById (reference key, shown through lastCountedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastMovementAt, lastCountedAt, lastCountedBy

## u_mes_matl_kit - Kits (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_kit.json | _id: mes_matl_kitStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2530px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | workCenterName | Work Center | String | 32 | 250px | left |
| 4 | kitType | Kit Type | String | 9 | 100px | left |
| 5 | requiredAt | Required At | Date/Datetime | 19 | 160px | center |
| 6 | toLocationName | To Location | String | 33 | 260px | left |
| 7 | pickedBy | Picked By | String | 14 | 120px | left |
| 8 | pickStartedAt | Pick Started At | Date/Datetime | 19 | 160px | center |
| 9 | pickCompletedAt | Pick Completed At | Date/Datetime | 19 | 160px | center |
| 10 | deliveredAt | Delivered At | Date/Datetime | 19 | 160px | center |
| 11 | receivedBy | Received By | String | 14 | 120px | left |
| 12 | isComplete | Complete | Boolean | 3 | 100px | center |
| 13 | status | Status | String | 9 | 90px | left |
| 14 | createdBy | Created By | String | 14 | 120px | left |
| 15 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 16 | updatedBy | Updated By | String | 14 | 120px | left |
| 17 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); workCenterId (reference key, shown through workCenterName); toLocationId (reference key, shown through toLocationName); pickedById (reference key, shown through pickedBy); receivedById (reference key, shown through receivedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_kitLine - Kit Lines (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_kitLine.json | _id: mes_matl_kitLineStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 3070px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | kitName | Kit | String | 15 | 130px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | itemName | Item | String | 48 | 300px | left |
| 5 | lotName | Lot | String | 15 | 130px | left |
| 6 | requiredQuantity | Required Quantity | Decimal128 | 3 | 160px | right |
| 7 | pickedQuantity | Picked Quantity | Decimal128 | 3 | 150px | right |
| 8 | fromLocationName | From Location | String | 34 | 260px | left |
| 9 | shortQuantity | Short Quantity | Decimal128 | 1 | 140px | right |
| 10 | itemRevision | Item Revision | String | 1 | 140px | left |
| 11 | scannedItemRevision | Scanned Item Revision | String | 1 | 190px | left |
| 12 | scannedCode | Scanned Code | String | 26 | 210px | left |
| 13 | isMandatory | Mandatory | Boolean | 3 | 110px | center |
| 14 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 15 | verificationResult | Verification Result | String | 14 | 180px | left |
| 16 | createdBy | Created By | String | 14 | 120px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 14 | 120px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); kitId (reference key, shown through kitName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); fromLocationId (reference key, shown through fromLocationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_label - Printed Labels (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_label.json | _id: mes_matl_labelStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | labelTemplateName | Label Template | String | 44 | 300px | left |
| 3 | labelType | Label Type | String | 15 | 130px | left |
| 4 | relatedCollectionName | Related Collection Name | String | 20 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 10 | 140px | left |
| 6 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 7 | containerName | Container | String | 10 | 110px | left |
| 8 | lotName | Lot | String | 0 | 80px | left |
| 9 | shipmentName | Shipment | String | 15 | 130px | left |
| 10 | payload | Payload | String | 48 | 300px | left |
| 11 | humanReadable | Human Readable | String | 46 | 300px | left |
| 12 | printerIotDeviceName | Printer IoT Device | String | 32 | 250px | left |
| 13 | printedAt | Printed At | Date/Datetime | 19 | 160px | center |
| 14 | printedBy | Printed By | String | 14 | 120px | left |
| 15 | copies | Copies | Int32 | 1 | 90px | right |
| 16 | reprintCount | Reprint Count | Int32 | 1 | 140px | right |
| 17 | reprintReason | Reprint Reason | String | 0 | 140px | left |
| 18 | verified | Verified | Boolean | 3 | 100px | center |
| 19 | verificationGrade | Verification Grade | String | 1 | 170px | left |
| 20 | voidedAt | Voided At | Date/Datetime | 19 | 160px | center |
| 21 | voidedBy | Voided By | String | 14 | 120px | left |
| 22 | status | Status | String | 9 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); labelTemplateId (reference key, shown through labelTemplateName); relatedEntityId (reference key, shown through relatedEntityName); wipUnitId (reference key, shown through wipUnitName); containerId (reference key, shown through containerName); lotId (reference key, shown through lotName); shipmentId (reference key, shown through shipmentName); printerIotDeviceId (reference key, shown through printerIotDeviceName); printedById (reference key, shown through printedBy); voidedById (reference key, shown through voidedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lotName, reprintReason

## u_mes_matl_labelTemplate - Label Templates (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_labelTemplate.json | _id: mes_matl_labelTemplateStable | rel: CL20261018-23:51 | samples: 20 | columns: 14 | total width: 2360px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 44 | 300px | left |
| 3 | labelType | Label Type | String | 15 | 130px | left |
| 4 | customerName | Customer | String | 42 | 300px | left |
| 5 | standard | Standard | String | 33 | 260px | left |
| 6 | widthMm | Width (mm) | Decimal128 | 5 | 110px | right |
| 7 | heightMm | Height (mm) | Decimal128 | 5 | 120px | right |
| 8 | printerLanguage | Printer Language | String | 3 | 160px | left |
| 9 | symbology | Symbology | String | 18 | 150px | left |
| 10 | payloadPattern | Payload Pattern | String | 67 | 300px | left |
| 11 | version | Version | Int32 | 1 | 90px | right |
| 12 | copies | Copies | Int32 | 1 | 90px | right |
| 13 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 14 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_labelTemplateField - Label Template Fields (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_labelTemplateField.json | _id: mes_matl_labelTemplateFieldStable | rel: CL20261018-23:51 | samples: 20 | columns: 9 | total width: 1300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | labelTemplateName | Label Template | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | fieldName | Field Name | String | 14 | 120px | left |
| 5 | source | Source | String | 12 | 110px | left |
| 6 | fieldFormat | Field Format | String | 2 | 130px | left |
| 7 | positionXMm | Position X (mm) | Decimal128 | 3 | 150px | right |
| 8 | positionYMm | Position Y (mm) | Decimal128 | 4 | 150px | right |
| 9 | isBarcode | Barcode | Boolean | 3 | 90px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); labelTemplateId (reference key, shown through labelTemplateName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_materialConsumption - Material Consumptions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_materialConsumption.json | _id: mes_matl_materialConsumptionStable | rel: CL20261018-23:51 | samples: 20 | columns: 25 | total width: 3910px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 3 | productionOrderName | Production Order | String | 10 | 160px | left |
| 4 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 5 | parentLotName | Parent Lot | String | 0 | 110px | left |
| 6 | componentItemName | Component Item | String | 48 | 300px | left |
| 7 | componentLotName | Component Lot | String | 15 | 140px | left |
| 8 | componentSerialNo | Component Serial No | String | 0 | 180px | left |
| 9 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 10 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 11 | workCenterName | Work Center | String | 37 | 280px | left |
| 12 | fromLocationName | From Location | String | 34 | 260px | left |
| 13 | consumptionType | Consumption Type | String | 7 | 160px | left |
| 14 | scanVerified | Scan Verified | Boolean | 3 | 140px | center |
| 15 | consumedAt | Consumed At | Date/Datetime | 19 | 160px | center |
| 16 | consumedBy | Consumed By | String | 14 | 120px | left |
| 17 | billOfMaterialName | Bill of Material | String | 21 | 170px | left |
| 18 | bomLineNo | BOM Line No | Int32 | 2 | 120px | right |
| 19 | erpPosted | ERP Posted | Boolean | 3 | 110px | center |
| 20 | erpMessageName | ERP Message | String | 15 | 130px | left |
| 21 | status | Status | String | 6 | 90px | left |
| 22 | createdBy | Created By | String | 14 | 120px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 14 | 120px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operationExecutionId (reference key, shown through operationExecutionName); productionOrderId (reference key, shown through productionOrderName); wipUnitId (reference key, shown through wipUnitName); parentLotId (reference key, shown through parentLotName); componentItemId (reference key, shown through componentItemName); componentLotId (reference key, shown through componentLotName); unitOfMeasureId (reference key, shown through unitOfMeasureName); workCenterId (reference key, shown through workCenterName); fromLocationId (reference key, shown through fromLocationName); consumedById (reference key, shown through consumedBy); billOfMaterialId (reference key, shown through billOfMaterialName); erpMessageId (reference key, shown through erpMessageName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentLotName, componentSerialNo

## u_mes_matl_materialDemandForecast - Material Demand Forecast (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_materialDemandForecast.json | _id: mes_matl_materialDemandForecastStable | rel: CL20261018-23:51 | samples: 10 | columns: 20 | total width: 3510px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 35 | 270px | left |
| 2 | itemName | Item | String | 39 | 300px | left |
| 3 | lineName | Line | String | 29 | 230px | left |
| 4 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 5 | bucketStartAt | Bucket Start At | Date/Datetime | 19 | 160px | center |
| 6 | bucketEndAt | Bucket End At | Date/Datetime | 19 | 160px | center |
| 7 | scheduledDemand | Scheduled Demand | Decimal128 | 3 | 160px | right |
| 8 | consumptionRatePerHour | Consumption Rate per Hour | Decimal128 | 3 | 220px | right |
| 9 | onHandQuantity | On Hand Quantity | Decimal128 | 3 | 160px | right |
| 10 | projectedOnHand | Projected on Hand | Decimal128 | 3 | 160px | right |
| 11 | projectedShortageAt | Projected Shortage At | Date/Datetime | 19 | 190px | center |
| 12 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 13 | method | Method | String | 16 | 140px | left |
| 14 | analyticsModelName | Analytics Model | String | 35 | 270px | left |
| 15 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 16 | status | Status | String | 10 | 90px | left |
| 17 | createdBy | Created By | String | 12 | 110px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 12 | 110px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); lineId (reference key, shown through lineName); unitOfMeasureId (reference key, shown through unitOfMeasureName); analyticsModelId (reference key, shown through analyticsModelName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_materialMovement - Material Movements (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_materialMovement.json | _id: mes_matl_materialMovementStable | rel: CL20261018-23:51 | samples: 20 | columns: 27 | total width: 4570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | movementTypeName | Movement Type | String | 38 | 290px | left |
| 3 | itemName | Item | String | 48 | 300px | left |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | containerName | Container | String | 10 | 110px | left |
| 6 | quantity | Quantity | Decimal128 | 6 | 100px | right |
| 7 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 8 | fromLocationName | From Location | String | 33 | 260px | left |
| 9 | toLocationName | To Location | String | 36 | 280px | left |
| 10 | fromStockStatusName | From Stock Status | String | 18 | 160px | left |
| 11 | toStockStatusName | To Stock Status | String | 22 | 180px | left |
| 12 | productionOrderName | Production Order | String | 10 | 160px | left |
| 13 | goodsReceiptName | Goods Receipt | String | 15 | 140px | left |
| 14 | shipmentName | Shipment | String | 15 | 130px | left |
| 15 | kitName | Kit | String | 15 | 130px | left |
| 16 | movedAt | Moved At | Date/Datetime | 19 | 160px | center |
| 17 | movedBy | Moved By | String | 14 | 120px | left |
| 18 | scanSource | Scan Source | String | 16 | 140px | left |
| 19 | reasonText | Reason Text | String | 43 | 300px | left |
| 20 | erpDocumentNo | ERP Document No | String | 10 | 150px | left |
| 21 | erpMovementType | ERP Movement Type | String | 3 | 160px | left |
| 22 | reversalOfMaterialMovementName | Reversal of Material Movement | String | 0 | 250px | left |
| 23 | status | Status | String | 8 | 90px | left |
| 24 | createdBy | Created By | String | 14 | 120px | left |
| 25 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 26 | updatedBy | Updated By | String | 14 | 120px | left |
| 27 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); movementTypeId (reference key, shown through movementTypeName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); containerId (reference key, shown through containerName); unitOfMeasureId (reference key, shown through unitOfMeasureName); fromLocationId (reference key, shown through fromLocationName); toLocationId (reference key, shown through toLocationName); fromStockStatusId (reference key, shown through fromStockStatusName); toStockStatusId (reference key, shown through toStockStatusName); productionOrderId (reference key, shown through productionOrderName); goodsReceiptId (reference key, shown through goodsReceiptName); shipmentId (reference key, shown through shipmentName); kitId (reference key, shown through kitName); movedById (reference key, shown through movedBy); reversalOfMaterialMovementId (reference key, shown through reversalOfMaterialMovementName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): reversalOfMaterialMovementName

## u_mes_matl_materialRequest - Material Requests (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_materialRequest.json | _id: mes_matl_materialRequestStable | rel: CL20261018-23:51 | samples: 10 | columns: 25 | total width: 4240px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | itemName | Item | String | 39 | 300px | left |
| 4 | requestedQuantity | Requested Quantity | Decimal128 | 4 | 170px | right |
| 5 | deliveredQuantity | Delivered Quantity | Decimal128 | 4 | 170px | right |
| 6 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 7 | requestType | Request Type | String | 6 | 130px | left |
| 8 | triggerSource | Trigger Source | String | 20 | 160px | left |
| 9 | requestedBy | Requested By | String | 12 | 130px | left |
| 10 | requestedAt | Requested At | Date/Datetime | 19 | 160px | center |
| 11 | fromLocationName | From Location | String | 28 | 220px | left |
| 12 | toLocationName | To Location | String | 33 | 260px | left |
| 13 | priority | Priority | String | 6 | 100px | left |
| 14 | acknowledgedBy | Acknowledged By | String | 12 | 150px | left |
| 15 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 16 | deliveredAt | Delivered At | Date/Datetime | 19 | 160px | center |
| 17 | responseMinutes | Response (min) | Int32 | 1 | 140px | right |
| 18 | andonEventName | Andon Event | String | 44 | 300px | left |
| 19 | lotName | Lot | String | 15 | 130px | left |
| 20 | replenishmentRuleName | Replenishment Rule | String | 26 | 210px | left |
| 21 | status | Status | String | 12 | 110px | left |
| 22 | createdBy | Created By | String | 12 | 110px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 12 | 110px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); itemId (reference key, shown through itemName); unitOfMeasureId (reference key, shown through unitOfMeasureName); requestedById (reference key, shown through requestedBy); fromLocationId (reference key, shown through fromLocationName); toLocationId (reference key, shown through toLocationName); acknowledgedById (reference key, shown through acknowledgedBy); andonEventId (reference key, shown through andonEventName); lotId (reference key, shown through lotName); replenishmentRuleId (reference key, shown through replenishmentRuleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_movementType - Movement Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_movementType.json | _id: mes_matl_movementTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1350px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 38 | 290px | left |
| 3 | description | Description | String | 48 | 300px | left |
| 4 | erpMovementType | ERP Movement Type | String | 3 | 160px | left |
| 5 | stockEffect | Stock Effect | String | 8 | 130px | left |
| 6 | requiresReason | Requires Reason | Boolean | 3 | 150px | center |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_packType - Pack Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_packType.json | _id: mes_matl_packTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 7 | 110px | left |
| 2 | name | Name | String | 27 | 210px | left |
| 3 | description | Description | String | 33 | 260px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_packagingSpecification - Packaging Specifications (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_packagingSpecification.json | _id: mes_matl_packagingSpecificationStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 3790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | itemName | Item | String | 46 | 300px | left |
| 3 | customerName | Customer | String | 42 | 300px | left |
| 4 | version | Version | Int32 | 1 | 90px | right |
| 5 | containerTypeName | Container Type | String | 33 | 260px | left |
| 6 | quantityPerContainer | Quantity per Container | Int32 | 2 | 200px | right |
| 7 | dunnage | Dunnage | String | 44 | 300px | left |
| 8 | vciRequired | Vci Required | Boolean | 3 | 130px | center |
| 9 | layersPerContainer | Layers per Container | Int32 | 1 | 180px | right |
| 10 | unitsPerLayer | Units per Layer | Int32 | 2 | 150px | right |
| 11 | containersPerPallet | Containers per Pallet | Int32 | 2 | 190px | right |
| 12 | maxGrossWeightKg | Max Gross Weight Kg | Decimal128 | 4 | 180px | right |
| 13 | unitLabelTemplateName | Unit Label Template | String | 44 | 300px | left |
| 14 | containerLabelTemplateName | Container Label Template | String | 44 | 300px | left |
| 15 | instructionControlledDocumentName | Instruction Controlled Document | String | 64 | 300px | left |
| 16 | approvedByCustomer | Approved By Customer | Boolean | 3 | 180px | center |
| 17 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 18 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); customerId (reference key, shown through customerName); containerTypeId (reference key, shown through containerTypeName); unitLabelTemplateId (reference key, shown through unitLabelTemplateName); containerLabelTemplateId (reference key, shown through containerLabelTemplateName); instructionControlledDocumentId (reference key, shown through instructionControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_packagingSpecificationLevel - Packaging Specification Levels (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_packagingSpecificationLevel.json | _id: mes_matl_packagingSpecificationLevelStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1200px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 29 | 230px | left |
| 2 | packagingSpecificationName | Packaging Specification | String | 25 | 210px | left |
| 3 | levelNo | Level No | Int32 | 1 | 100px | right |
| 4 | packTypeName | Pack Type | String | 27 | 210px | left |
| 5 | quantity | Quantity | Int32 | 1 | 100px | right |
| 6 | lengthMm | Length (mm) | Decimal128 | 5 | 120px | right |
| 7 | widthMm | Width (mm) | Decimal128 | 5 | 110px | right |
| 8 | heightMm | Height (mm) | Decimal128 | 5 | 120px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); packagingSpecificationId (reference key, shown through packagingSpecificationName); packTypeId (reference key, shown through packTypeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_replenishmentRule - Replenishment Rules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_replenishmentRule.json | _id: mes_matl_replenishmentRuleStable | rel: CL20261018-23:51 | samples: 10 | columns: 17 | total width: 2900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | itemName | Item | String | 39 | 300px | left |
| 3 | toLocationName | To Location | String | 33 | 260px | left |
| 4 | fromLocationName | From Location | String | 28 | 220px | left |
| 5 | workCenterName | Work Center | String | 32 | 250px | left |
| 6 | triggerType | Trigger Type | String | 12 | 130px | left |
| 7 | minQuantity | Min Quantity | Decimal128 | 4 | 130px | right |
| 8 | maxQuantity | Max Quantity | Decimal128 | 4 | 130px | right |
| 9 | reorderPointQuantity | Reorder Point Quantity | Decimal128 | 4 | 200px | right |
| 10 | kanbanQuantity | Kanban Quantity | Decimal128 | 3 | 150px | right |
| 11 | kanbanCount | Kanban Count | Int32 | 1 | 130px | right |
| 12 | containerTypeName | Container Type | String | 24 | 190px | left |
| 13 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 14 | leadTimeMinutes | Lead Time (min) | Int32 | 3 | 150px | right |
| 15 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 16 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 17 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); toLocationId (reference key, shown through toLocationName); fromLocationId (reference key, shown through fromLocationName); workCenterId (reference key, shown through workCenterName); containerTypeId (reference key, shown through containerTypeName); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_shipment - Shipments (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_shipment.json | _id: mes_matl_shipmentStable | rel: CL20261018-23:51 | samples: 20 | columns: 28 | total width: 4280px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | customerName | Customer | String | 42 | 300px | left |
| 3 | shipToCode | Ship to Code | String | 6 | 130px | left |
| 4 | customerScheduleName | Customer Schedule | String | 18 | 160px | left |
| 5 | invoiceNo | Invoice No | String | 16 | 140px | left |
| 6 | invoiceDate | Invoice Date | Date/Date | 10 | 130px | center |
| 7 | asnNo | Asn No | String | 15 | 130px | left |
| 8 | asnSentAt | Asn Sent At | Date/Datetime | 19 | 160px | center |
| 9 | eWayBillNo | E Way Bill No | String | 12 | 140px | left |
| 10 | transporterName | Transporter | String | 30 | 230px | left |
| 11 | vehicleNo | Vehicle No | String | 12 | 110px | left |
| 12 | driverName | Driver Name | String | 16 | 140px | left |
| 13 | lrNo | Lr No | String | 10 | 90px | left |
| 14 | totalQuantity | Total Quantity | Int32 | 3 | 140px | right |
| 15 | totalContainers | Total Containers | Int32 | 2 | 160px | right |
| 16 | grossWeightKg | Gross Weight Kg | Decimal128 | 5 | 150px | right |
| 17 | invoiceValueInr | Invoice Value (INR) | Decimal128 | 9 | 180px | right |
| 18 | dockLocationName | Dock Location | String | 29 | 230px | left |
| 19 | loadedBy | Loaded By | String | 14 | 120px | left |
| 20 | plannedDispatchAt | Planned Dispatch At | Date/Datetime | 19 | 180px | center |
| 21 | dispatchedAt | Dispatched At | Date/Datetime | 19 | 160px | center |
| 22 | deliveredAt | Delivered At | Date/Datetime | 19 | 160px | center |
| 23 | podReceivedAt | Pod Received At | Date/Datetime | 19 | 160px | center |
| 24 | status | Status | String | 10 | 90px | left |
| 25 | createdBy | Created By | String | 14 | 120px | left |
| 26 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 27 | updatedBy | Updated By | String | 14 | 120px | left |
| 28 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); customerScheduleId (reference key, shown through customerScheduleName); transporterId (reference key, shown through transporterName); dockLocationId (reference key, shown through dockLocationName); loadedById (reference key, shown through loadedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_shipmentLine - Shipment Lines (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_shipmentLine.json | _id: mes_matl_shipmentLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1430px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | shipmentName | Shipment | String | 15 | 130px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | itemName | Item | String | 32 | 250px | left |
| 5 | customerPartNo | Customer Part No | String | 15 | 160px | left |
| 6 | quantity | Quantity | Int32 | 3 | 100px | right |
| 7 | createdBy | Created By | String | 12 | 110px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 12 | 110px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shipmentId (reference key, shown through shipmentName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_shipmentLineContainer - Shipment Line Containers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_shipmentLineContainer.json | _id: mes_matl_shipmentLineContainerStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1120px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | shipmentLineName | Shipment Line | String | 19 | 160px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | containerName | Container | String | 10 | 110px | left |
| 5 | createdBy | Created By | String | 12 | 110px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 12 | 110px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shipmentLineId (reference key, shown through shipmentLineName); containerId (reference key, shown through containerName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_shipmentLineLot - Shipment Line Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_shipmentLineLot.json | _id: mes_matl_shipmentLineLotStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1140px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | shipmentLineName | Shipment Line | String | 19 | 160px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 12 | 110px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 12 | 110px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shipmentLineId (reference key, shown through shipmentLineName); lotId (reference key, shown through lotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_matl_stockStatus - Stock Statuses (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_stockStatus.json | _id: mes_matl_stockStatusStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 950px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 6 | 110px | left |
| 2 | name | Name | String | 22 | 180px | left |
| 3 | description | Description | String | 28 | 220px | left |
| 4 | isUsable | Usable | Boolean | 3 | 90px | center |
| 5 | erpStockType | ERP Stock Type | String | 16 | 140px | left |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_matl_storageLocation - Storage Locations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_storageLocation.json | _id: mes_matl_storageLocationStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2460px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 36 | 280px | left |
| 3 | locationType | Location Type | String | 14 | 140px | left |
| 4 | areaName | Area | String | 29 | 230px | left |
| 5 | workCenterName | Work Center | String | 37 | 280px | left |
| 6 | parentLocationName | Parent Location | String | 0 | 150px | left |
| 7 | zone | Zone | String | 3 | 80px | left |
| 8 | rack | Rack | String | 3 | 80px | left |
| 9 | level | Level | Int32 | 1 | 80px | right |
| 10 | bin | Bin | String | 3 | 80px | left |
| 11 | capacityQuantity | Capacity Quantity | Int32 | 4 | 160px | right |
| 12 | isQuarantine | Quarantine | Boolean | 3 | 110px | center |
| 13 | isLineSide | Line Side | Boolean | 3 | 110px | center |
| 14 | mixedLotsAllowed | Mixed Lots Allowed | Boolean | 3 | 170px | center |
| 15 | erpStorageLocation | ERP Storage Location | String | 4 | 180px | left |
| 16 | barcode | Barcode | String | 14 | 120px | left |
| 17 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); workCenterId (reference key, shown through workCenterName); parentLocationId (reference key, shown through parentLocationName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentLocationName

## u_mes_matl_storageLocationAllowedItem - Storage Allowed Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_matl_storageLocationAllowedItem.json | _id: mes_matl_storageLocationAllowedItemStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 990px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 39 | 300px | left |
| 5 | itemGroupName | Item Group | String | 22 | 180px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); storageLocationId (reference key, shown through storageLocationName); itemId (reference key, shown through itemName); itemGroupId (reference key, shown through itemGroupName); schemaVersion (excluded key (identifier, site, app or schema))
