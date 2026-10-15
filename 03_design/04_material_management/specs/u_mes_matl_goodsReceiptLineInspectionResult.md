# u_mes_matl_goodsReceiptLineInspectionResult

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Links one goods receipt line to one inspection result; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_matl_goodsReceiptLine |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Relationship collection. A goods receipt line can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. goodsReceiptLineId and goodsReceiptLineName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1117000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GRN-2026-000918-L01-IR01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | goodsReceiptLineId | String | - | Yes | Reference to u_mes_matl_goodsReceiptLine._id: the parent document this one belongs to | `"1116000000000001"` | Reference: u_mes_matl_goodsReceiptLine._id |
| 7 | goodsReceiptLineName | String | - | Yes | Display value of goodsReceiptLineId, copied from u_mes_matl_goodsReceiptLine.recordNo | `"GRN-2026-000918-L01"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | inspectionResultId | String | - | Yes | Reference to u_mes_qual_inspectionResult._id | `"1150000000000006"` | Reference: u_mes_qual_inspectionResult._id |
| 10 | inspectionResultName | String | - | Yes | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `"IR-2026-000177"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:48.000+0000")` |  |
| 13 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 14 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 15 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:48.000+0000")` |  |
| 16 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 17 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

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
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_goodsReceiptLineInspectionResult.js
