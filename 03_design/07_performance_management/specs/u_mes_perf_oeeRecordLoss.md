# u_mes_perf_oeeRecordLoss

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | One document per loss of a OEE record |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_perf_oeeRecord |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (18 required, 2 may be null) |

## Structure

Child collection. The parent OEE record can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. oeeRecordId and oeeRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1209000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"OEE-2026-000141-L01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | oeeRecordId | String | Yes | Reference to u_mes_perf_oeeRecord._id: the parent document this one belongs to | `"1208000000000001"` | Reference: u_mes_perf_oeeRecord._id |
| 6 | oeeRecordName | String | Yes | Display value of oeeRecordId, copied from u_mes_perf_oeeRecord.recordNo | `"OEE-2026-000141"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | lossCategoryId | String | Yes | Reference to u_mes_perf_lossCategory._id | `"1286000000000001"` | Reference: u_mes_perf_lossCategory._id |
| 9 | lossCategoryName | String | Yes | Display value of lossCategoryId, copied from u_mes_perf_lossCategory.name | `"Breakdown"` |  |
| 10 | reasonCodeId | String | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 11 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 12 | lossMinutes | Int32 | Yes | Loss (minutes) | `NumberInt(18)` |  |
| 13 | lossUnits | Int32 | Yes | Loss units | `NumberInt(30)` |  |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-17T01:24:40.000+0000")` |  |
| 16 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 18 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-17T01:24:40.000+0000")` |  |
| 19 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ oeeRecordId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ lossCategoryId: 1 }` | No | Look-up of lines by loss category |
| 3 | `{ reasonCodeId: 1 }` | No | Look-up of lines by reason code |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_oeeRecordLoss.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_oeeRecordLoss.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_oeeRecordLoss.js
