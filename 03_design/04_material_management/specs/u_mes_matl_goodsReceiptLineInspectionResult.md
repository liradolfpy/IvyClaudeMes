# u_mes_matl_goodsReceiptLineInspectionResult

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Links one goods receipt line to one inspection result; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_matl_goodsReceiptLine |
| _id pattern | <goodsReceiptLineId>-IR<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A goods receipt line can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. goodsReceiptLineId and goodsReceiptLineName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <goodsReceiptLineId>-IR<nnn> | `"GRN-2026-000918-L001-IR001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000918-L001-IR001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | goodsReceiptLineId | String | Yes | Reference to u_mes_matl_goodsReceiptLine._id: the parent document this one belongs to | `"GRN-2026-000918-L001"` | Reference: u_mes_matl_goodsReceiptLine._id |
| 6 | goodsReceiptLineName | String | Yes | Display value of goodsReceiptLineId, copied from u_mes_matl_goodsReceiptLine.recordNo | `"2026-000918-L001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | inspectionResultId | String | Yes | Reference to u_mes_qual_inspectionResult._id | `"IR-20260929-000342"` | Reference: u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | Yes | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `"20260929-000342"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ goodsReceiptLineId: 1, inspectionResultId: 1 }` | Yes | One link per pair |
| 2 | `{ inspectionResultId: 1, goodsReceiptLineId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_goodsReceiptLineInspectionResult.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_goodsReceiptLineInspectionResult.js
- Sample document: 03_design/04_material_management/samples/u_mes_matl_goodsReceiptLineInspectionResult.js
