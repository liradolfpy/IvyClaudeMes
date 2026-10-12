# u_mes_trac_asBuiltRecordInspectionResult

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | Links one as built record to one inspection result; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_trac_asBuiltRecord |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A as built record can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. asBuiltRecordId and asBuiltRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1137000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ABR-VB26258A00184-IR01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | asBuiltRecordId | String | - | Yes | Reference to u_mes_trac_asBuiltRecord._id: the parent document this one belongs to | `"1134000000000001"` | Reference: u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - | Yes | Display value of asBuiltRecordId, copied from u_mes_trac_asBuiltRecord.recordNo | `"ABR-VB26258A00184"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | inspectionResultId | String | - | Yes | Reference to u_mes_qual_inspectionResult._id | `"1150000000000006"` | Reference: u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | - | Yes | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `"IR-2026-000177"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:20.000+0000")` |  |
| 12 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:20.000+0000")` |  |
| 15 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ asBuiltRecordId: 1, inspectionResultId: 1 }` | Yes | One link per pair |
| 2 | `{ inspectionResultId: 1, asBuiltRecordId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_asBuiltRecordInspectionResult.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_asBuiltRecordInspectionResult.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_asBuiltRecordInspectionResult.js
