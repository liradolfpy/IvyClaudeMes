# u_mes_mat_goodsReceipt

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | Receipts from suppliers with lines, supplier lot, certificate, incoming inspection status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | GRN-<recordNo> |
| Display value used by references | recordNo |
| Keys | 25 (20 required, 5 may be null) |
| Estimated volume per year | ~12,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per goods receipt, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with goodsReceiptId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mat_goodsReceiptLine | Child | line |
| u_mes_mat_goodsReceiptLineInspectionResult | Relationship | (below u_mes_mat_goodsReceiptLine) inspection result |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: GRN-<recordNo> | `"GRN-2026-000918"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000918"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | supplierId | String | Yes | Reference to u_mes_mdm_supplier._id | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 6 | supplierName | String | Yes | Display value of supplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 7 | purchaseOrderNo | String | Yes | Purchase order number | `"4500117302"` |  |
| 8 | supplierInvoiceNo | String | Yes | Supplier invoice number | `"KPP/26-27/1842"` |  |
| 9 | supplierInvoiceDate | Date | Yes | Supplier invoice date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 10 | deliveryChallanNo | String | Yes | Delivery challan number | `"DC-07713"` |  |
| 11 | vehicleNo | String | Yes | Vehicle number | `"MH14 GT 4471"` |  |
| 12 | receivedAt | Date | No (null allowed) | Date and time when the record was received | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 13 | receivedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'received' | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 14 | receivedBy | String | No (null allowed) | Display name of the user in receivedById, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 15 | gateEntryNo | String | Yes | Gate entry number | `"GE-260925-0044"` |  |
| 16 | inspectionCompletedAt | Date | No (null allowed) | Inspection completed date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 17 | erpGrnNo | String | No (null allowed) | ERP grn number | `"5000209117"` |  |
| 18 | status | String | Yes | Primary lifecycle state of the document | `"Accepted"` | Received; Under Inspection; Accepted; Partially Accepted; Rejected |
| 19 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 20 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 21 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 22 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 23 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 24 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 25 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |

## Status values

Received, Under Inspection, Accepted, Partially Accepted, Rejected. Initial state: Received. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 4 | `{ siteId: 1, supplierInvoiceDate: -1 }` | No | Time-ordered lists and reports by supplier invoice date |

## Referenced by

u_mes_exe_lot, u_mes_mat_materialMovement, u_mes_mat_goodsReceiptLine, u_mes_qlt_inspectionResult, u_mes_sys_erpMessage.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_goodsReceipt.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_goodsReceipt.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_goodsReceipt.js
