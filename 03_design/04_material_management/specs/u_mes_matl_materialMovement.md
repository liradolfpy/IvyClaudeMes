# u_mes_matl_materialMovement

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Every stock transaction: receipt, putaway, issue to line, return, scrap, transfer, shipment |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 49 (24 required, 25 may be null) |
| Estimated volume per year | ~1.5 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per material movement, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1114000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MM-2026-000331"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | movementTypeId | String | - | Yes | Reference to u_mes_matl_movementType._id | `"1279000000000001"` | Reference: u_mes_matl_movementType._id |
| 7 | movementTypeName | String | - | Yes | Display value of movementTypeId, copied from u_mes_matl_movementType.name | `"Goods Receipt Against Purchase Order"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 12 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 13 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 14 | quantity | Decimal128 | - | Yes | Quantity of the material movement | `NumberDecimal("5000")` |  |
| 15 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 17 | fromLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: from location | `null` | Reference: u_mes_matl_storageLocation._id |
| 18 | fromLocationName | String | - | No (null allowed) | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `null` |  |
| 19 | toLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: to location | `"1112000000000002"` | Reference: u_mes_matl_storageLocation._id |
| 20 | toLocationName | String | - | No (null allowed) | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 21 | fromStockStatusId | String | - | No (null allowed) | Reference to u_mes_matl_stockStatus._id: from stock status | `null` | Reference: u_mes_matl_stockStatus._id |
| 22 | fromStockStatusName | String | - | No (null allowed) | Display value of fromStockStatusId, copied from u_mes_matl_stockStatus.name | `null` |  |
| 23 | toStockStatusId | String | - | No (null allowed) | Reference to u_mes_matl_stockStatus._id: to stock status | `"1280000000000002"` | Reference: u_mes_matl_stockStatus._id |
| 24 | toStockStatusName | String | - | No (null allowed) | Display value of toStockStatusId, copied from u_mes_matl_stockStatus.name | `"Quality Inspection"` |  |
| 25 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `null` | Reference: u_mes_plan_productionOrder._id |
| 26 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `null` |  |
| 27 | goodsReceiptId | String | - | No (null allowed) | Reference to u_mes_matl_goodsReceipt._id | `"1115000000000001"` | Reference: u_mes_matl_goodsReceipt._id |
| 28 | goodsReceiptName | String | - | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_matl_goodsReceipt.recordNo | `"GRN-2026-000918"` |  |
| 29 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 30 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 31 | kitId | String | - | No (null allowed) | Reference to u_mes_matl_kit._id | `null` | Reference: u_mes_matl_kit._id |
| 32 | kitName | String | - | No (null allowed) | Display value of kitId, copied from u_mes_matl_kit.recordNo | `null` |  |
| 33 | movedAt | Date | Datetime | Yes | Date and time when the record was moved. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:18.000+0000")` |  |
| 34 | movedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'moved' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 35 | movedBy | String | - | Yes | Display name of the user in movedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 36 | scanSource | String | - | Yes | Scan source | `"Handheld Scanner"` | Handheld Scanner; Fixed Scanner; Manual Entry |
| 37 | reasonText | String | - | No (null allowed) | Reason text | `"Replenishment against kanban call"` |  |
| 38 | erpDocumentNo | String | - | No (null allowed) | ERP document number | `"4900318842"` |  |
| 39 | erpMovementType | String | - | No (null allowed) | ERP movement type | `"261"` |  |
| 40 | reversalOfMaterialMovementId | String | - | No (null allowed) | Reference to u_mes_matl_materialMovement._id: reversal of material movement | `null` | Reference: u_mes_matl_materialMovement._id |
| 41 | reversalOfMaterialMovementName | String | - | No (null allowed) | Display value of reversalOfMaterialMovementId, copied from u_mes_matl_materialMovement.recordNo | `null` |  |
| 42 | status | String | - | Yes | Primary lifecycle state of the document | `"Posted"` | Posted; Reversed |
| 43 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 44 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:48.000+0000")` |  |
| 45 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 46 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 47 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:18.000+0000")` |  |
| 48 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 49 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Posted, Reversed. Initial state: Posted. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_matl_materialMovement.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_materialMovement.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_materialMovement.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_materialMovement.js
