# u_mes_matl_goodsReceipt

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Receipts from suppliers with lines, supplier lot, certificate, incoming inspection status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 26 (21 required, 5 may be null) |
| Estimated volume per year | ~12,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per goods receipt, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with goodsReceiptId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_goodsReceiptLine | Child | line |
| u_mes_matl_goodsReceiptLineInspectionResult | Relationship | (below u_mes_matl_goodsReceiptLine) inspection result |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1115000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GRN-2026-000918"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | supplierId | String | - | Yes | Reference to u_mes_mast_supplier._id | `"1038000000000001"` | Reference: u_mes_mast_supplier._id |
| 7 | supplierName | String | - | Yes | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 8 | purchaseOrderNo | String | - | Yes | Purchase order number | `"4500117302"` |  |
| 9 | supplierInvoiceNo | String | - | Yes | Supplier invoice number | `"KPP/26-27/1842"` |  |
| 10 | supplierInvoiceDate | Date | Date | Yes | Supplier invoice date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 11 | deliveryChallanNo | String | - | Yes | Delivery challan number | `"DC-07713"` |  |
| 12 | vehicleNo | String | - | Yes | Vehicle number | `"MH14 GT 4471"` |  |
| 13 | receivedAt | Date | Datetime | No (null allowed) | Date and time when the record was received. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 14 | receivedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'received' | `null` | Reference: u_mes_mast_user._id |
| 15 | receivedBy | String | - | No (null allowed) | Display name of the user in receivedById, copied from u_mes_mast_user.fullName | `null` |  |
| 16 | gateEntryNo | String | - | Yes | Gate entry number | `"GE-260925-0044"` |  |
| 17 | inspectionCompletedAt | Date | Datetime | No (null allowed) | Inspection completed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | erpGrnNo | String | - | No (null allowed) | ERP grn number | `"5000209117"` |  |
| 19 | status | String | - | Yes | Primary lifecycle state of the document | `"Received"` | Received; Under Inspection; Accepted; Partially Accepted; Rejected |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 21 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 22 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 23 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 24 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 25 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 26 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Received, Under Inspection, Accepted, Partially Accepted, Rejected. Initial state: Received. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 4 | `{ siteId: 1, supplierInvoiceDate: -1 }` | No | Time-ordered lists and reports by supplier invoice date |

## Referenced by

u_mes_plan_lot, u_mes_matl_materialMovement, u_mes_matl_goodsReceiptLine, u_mes_qual_inspectionResult, u_mes_syst_erpMessage.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_goodsReceipt.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_goodsReceipt.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_goodsReceipt.js
