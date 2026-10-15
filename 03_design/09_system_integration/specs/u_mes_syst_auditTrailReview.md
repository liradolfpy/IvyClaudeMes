# u_mes_syst_auditTrailReview

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Documented review of the audit-trail entries of a production record, a system or an investigation: period, number of entries, critical entries, anomalies and outcome. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (23 required, 9 may be null) |
| Estimated volume per year | about 3,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per audit trail review, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1347000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ATR-20260916-001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | reviewType | String | - | Yes | Why the review is done | `"Batch Record Review"` | Batch Record Review; Periodic System Review; For Cause |
| 7 | computerisedSystemId | String | - | Yes | Reference to u_mes_syst_computerisedSystem._id | `"1344000000000001"` | Reference: u_mes_syst_computerisedSystem._id |
| 8 | computerisedSystemName | String | - | Yes | Display value of computerisedSystemId, copied from u_mes_syst_computerisedSystem.name | `"Manufacturing execution system, Ranjangaon OSD plant"` |  |
| 9 | relatedCollectionName | String | - | No (null allowed) | Name of the collection the related document is in | `"u_mes_plan_productionOrder"` | u_mes_plan_productionOrder; u_mes_syst_systemPeriodicReview; u_mes_qual_nonconformance |
| 10 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1083000000000011"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"PCM5B26091"` |  |
| 12 | reviewFromAt | Date | Datetime | Yes | Start of the reviewed period | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 13 | reviewToAt | Date | Datetime | Yes | End of the reviewed period | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 14 | entriesReviewedCount | Int32 | - | Yes | Audit-trail entries in scope | `NumberInt(38)` |  |
| 15 | criticalEntriesCount | Int32 | - | Yes | Entries on critical data (results, limits, status, recipes) | `NumberInt(5)` |  |
| 16 | anomalyCount | Int32 | - | Yes | Entries that needed justification | `NumberInt(1)` |  |
| 17 | findingsText | String | - | No (null allowed) | Findings | `"Change part life override justified in the interlock event"` |  |
| 18 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 19 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 20 | reviewedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 21 | reviewedBy | String | - | Yes | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 22 | reviewedAt | Date | Datetime | No (null allowed) | Time the review was completed | `ISODate("2026-09-16T10:00:00.000+0000")` |  |
| 23 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 24 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Open; In Review; Completed; Escalated |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:00:00.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |

## Status values

Open, In Review, Completed, Escalated. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ computerisedSystemId: 1 }` | No | Look-up of documents by computerised system |
| 4 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 5 | `{ electronicSignatureId: 1 }` | No | Look-up of documents by electronic signature |
| 6 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 7 | `{ siteId: 1, reviewFromAt: -1 }` | No | Time-ordered lists and reports by review from at |

## Referenced by

u_mes_syst_auditTrail, u_mes_bmr_batchRecordReview.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_auditTrailReview.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_auditTrailReview.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_auditTrailReview.js
