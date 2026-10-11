# u_mes_mat_materialMovement

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | Every stock transaction: receipt, putaway, issue to line, return, scrap, transfer, shipment |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | MM-<recordNo> |
| Display value used by references | recordNo |
| Keys | 48 (23 required, 25 may be null) |
| Estimated volume per year | ~1.5 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per material movement, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MM-<recordNo> | `"MM-20260929-000233"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000233"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | movementTypeId | String | Yes | Reference to u_mes_mat_movementType._id | `"MVT-ISSUE-LINE"` | Reference: u_mes_mat_movementType._id |
| 6 | movementTypeName | String | Yes | Display value of movementTypeId, copied from u_mes_mat_movementType.name | `"Issue To Line"` |  |
| 7 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 8 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 10 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 11 | containerId | String | No (null allowed) | Reference to u_mes_exe_container._id | `"CNT-BIN-000731"` | Reference: u_mes_exe_container._id |
| 12 | containerName | String | No (null allowed) | Display value of containerId, copied from u_mes_exe_container.recordNo | `"BIN-000731"` |  |
| 13 | quantity | Decimal128 | Yes | Quantity of the material movement | `NumberDecimal("1")` |  |
| 14 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-EA"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Each"` |  |
| 16 | fromLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: from location | `"LOC-WH-A-R02-B14"` | Reference: u_mes_mat_storageLocation._id |
| 17 | fromLocationName | String | No (null allowed) | Display value of fromLocationId, copied from u_mes_mat_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 18 | toLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: to location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 19 | toLocationName | String | No (null allowed) | Display value of toLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 20 | fromStockStatusId | String | No (null allowed) | Reference to u_mes_mat_stockStatus._id: from stock status | `"STS-QI"` | Reference: u_mes_mat_stockStatus._id |
| 21 | fromStockStatusName | String | No (null allowed) | Display value of fromStockStatusId, copied from u_mes_mat_stockStatus.name | `"Quality Inspection"` |  |
| 22 | toStockStatusId | String | No (null allowed) | Reference to u_mes_mat_stockStatus._id: to stock status | `"STS-UNR"` | Reference: u_mes_mat_stockStatus._id |
| 23 | toStockStatusName | String | No (null allowed) | Display value of toStockStatusId, copied from u_mes_mat_stockStatus.name | `"Unrestricted"` |  |
| 24 | productionOrderId | String | No (null allowed) | Reference to u_mes_exe_productionOrder._id | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 25 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 26 | goodsReceiptId | String | No (null allowed) | Reference to u_mes_mat_goodsReceipt._id | `"GRN-2026-000918"` | Reference: u_mes_mat_goodsReceipt._id |
| 27 | goodsReceiptName | String | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_mat_goodsReceipt.recordNo | `"2026-000918"` |  |
| 28 | shipmentId | String | No (null allowed) | Reference to u_mes_mat_shipment._id | `"SHP-2026-000377"` | Reference: u_mes_mat_shipment._id |
| 29 | shipmentName | String | No (null allowed) | Display value of shipmentId, copied from u_mes_mat_shipment.recordNo | `"2026-000377"` |  |
| 30 | kitId | String | No (null allowed) | Reference to u_mes_mat_kit._id | `"KIT-20260929-0007"` | Reference: u_mes_mat_kit._id |
| 31 | kitName | String | No (null allowed) | Display value of kitId, copied from u_mes_mat_kit.recordNo | `"20260929-0007"` |  |
| 32 | movedAt | Date | Yes | Date and time when the record was moved | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 33 | movedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'moved' | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 34 | movedBy | String | Yes | Display name of the user in movedById, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 35 | scanSource | String | Yes | Scan source | `"Handheld Scanner"` | Handheld Scanner; Fixed Scanner; Manual Entry |
| 36 | reasonText | String | No (null allowed) | Reason text | `"Replenishment against kanban call"` |  |
| 37 | erpDocumentNo | String | No (null allowed) | ERP document number | `"4900318842"` |  |
| 38 | erpMovementType | String | No (null allowed) | ERP movement type | `"261"` |  |
| 39 | reversalOfMaterialMovementId | String | No (null allowed) | Reference to u_mes_mat_materialMovement._id: reversal of material movement | `null` | Reference: u_mes_mat_materialMovement._id |
| 40 | reversalOfMaterialMovementName | String | No (null allowed) | Display value of reversalOfMaterialMovementId, copied from u_mes_mat_materialMovement.recordNo | `null` |  |
| 41 | status | String | Yes | Primary lifecycle state of the document | `"Posted"` | Posted; Reversed |
| 42 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 43 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 44 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 45 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 46 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 47 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 48 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |

## Status values

Posted, Reversed. Initial state: Posted. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ movementTypeId: 1 }` | No | Look-up of documents by movement type |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ containerId: 1 }` | No | Look-up of documents by container |
| 7 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 8 | `{ siteId: 1, movedAt: -1 }` | No | Time-ordered lists and reports by moved at |

## Referenced by

u_mes_mat_materialMovement.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_materialMovement.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_materialMovement.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_materialMovement.js
