# u_mes_qlt_nonconformanceScrapRecord

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Links one nonconformance to one scrap record; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qlt_nonconformance |
| _id pattern | <nonconformanceId>-SR<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A nonconformance can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. nonconformanceId and nonconformanceName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <nonconformanceId>-SR<nnn> | `"NCR-2026-000118-SR001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000118-SR001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | Yes | Reference to u_mes_qlt_nonconformance._id: the parent document this one belongs to | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String | Yes | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | scrapRecordId | String | Yes | Reference to u_mes_qlt_scrapRecord._id | `"SCR-2026-000203"` | Reference: u_mes_qlt_scrapRecord._id |
| 9 | scrapRecordName | String | Yes | Display value of scrapRecordId, copied from u_mes_qlt_scrapRecord.recordNo | `"2026-000203"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ nonconformanceId: 1, scrapRecordId: 1 }` | Yes | One link per pair |
| 2 | `{ scrapRecordId: 1, nonconformanceId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_nonconformanceScrapRecord.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_nonconformanceScrapRecord.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_nonconformanceScrapRecord.js
