# u_mes_matl_goodsReceiptLine

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | One document per line of a goods receipt |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_matl_goodsReceipt |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 30 (25 required, 5 may be null) |

## Structure

Child collection. The parent goods receipt can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. goodsReceiptId and goodsReceiptName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1116000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GRN-2026-000918-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | goodsReceiptId | String | - | Yes | Reference to u_mes_matl_goodsReceipt._id: the parent document this one belongs to | `"1115000000000001"` | Reference: u_mes_matl_goodsReceipt._id |
| 7 | goodsReceiptName | String | - | Yes | Display value of goodsReceiptId, copied from u_mes_matl_goodsReceipt.recordNo | `"GRN-2026-000918"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 9 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 11 | supplierLotNo | String | - | No (null allowed) | Supplier lot number | `"KPP-260905-07"` |  |
| 12 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 13 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 14 | orderedQuantity | Decimal128 | - | Yes | Ordered quantity | `NumberDecimal("5000")` |  |
| 15 | receivedQuantity | Decimal128 | - | Yes | Received quantity | `NumberDecimal("5000")` |  |
| 16 | acceptedQuantity | Decimal128 | - | Yes | Accepted quantity | `NumberDecimal("5000")` |  |
| 17 | rejectedQuantity | Decimal128 | - | Yes | Rejected quantity | `NumberDecimal("0")` |  |
| 18 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 20 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 21 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 22 | certificateReceived | Boolean | - | Yes | True when: certificate received | `true` |  |
| 23 | inspectionStatus | String | - | Yes | Inspection status | `"Accepted"` | Pending; Accepted; Rejected; Accepted Under Deviation |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 25 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:48.000+0000")` |  |
| 26 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 27 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 28 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:48.000+0000")` |  |
| 29 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 30 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ goodsReceiptId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |
| 3 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 4 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

u_mes_matl_goodsReceiptLineInspectionResult.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_goodsReceiptLine.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_goodsReceiptLine.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_goodsReceiptLine.js
