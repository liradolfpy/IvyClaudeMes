# u_mes_mat_goodsReceiptLine

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | One document per line of a goods receipt |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_mat_goodsReceipt |
| _id pattern | <goodsReceiptId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 29 (24 required, 5 may be null) |

## Structure

Child collection. The parent goods receipt can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. goodsReceiptId and goodsReceiptName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <goodsReceiptId>-L<nnn> | `"GRN-2026-000918-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000918-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | goodsReceiptId | String | Yes | Reference to u_mes_mat_goodsReceipt._id: the parent document this one belongs to | `"GRN-2026-000918"` | Reference: u_mes_mat_goodsReceipt._id |
| 6 | goodsReceiptName | String | Yes | Display value of goodsReceiptId, copied from u_mes_mat_goodsReceipt.recordNo | `"2026-000918"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-30-0010"` | Reference: u_mes_prd_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | supplierLotNo | String | No (null allowed) | Supplier lot number | `"KPP-260914-07"` |  |
| 11 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 12 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 13 | orderedQuantity | Decimal128 | Yes | Ordered quantity | `NumberDecimal("5000")` |  |
| 14 | receivedQuantity | Decimal128 | Yes | Received quantity | `NumberDecimal("5000")` |  |
| 15 | acceptedQuantity | Decimal128 | Yes | Accepted quantity | `NumberDecimal("5000")` |  |
| 16 | rejectedQuantity | Decimal128 | Yes | Rejected quantity | `NumberDecimal("0")` |  |
| 17 | unitOfMeasureId | String | No (null allowed) | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-EA"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Each"` |  |
| 19 | storageLocationId | String | Yes | Reference to u_mes_mat_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 20 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 21 | certificateReceived | Boolean | Yes | True when: certificate received | `true` |  |
| 22 | inspectionStatus | String | Yes | Inspection status | `"Accepted"` | Pending; Accepted; Rejected; Accepted Under Deviation |
| 23 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 24 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 25 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 26 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 27 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 28 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 29 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ goodsReceiptId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |
| 3 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 4 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

u_mes_mat_goodsReceiptLineInspectionResult.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_goodsReceiptLine.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_goodsReceiptLine.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_goodsReceiptLine.js
