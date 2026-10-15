# u_mes_bmr_batchRecordReviewException

| Property | Value |
|---|---|
| Module | BatchManufacturingRecord (bmr) |
| Purpose | One document per exception of a batch record review |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_bmr_batchRecordReview |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 24 (20 required, 4 may be null) |

## Structure

Child collection. The parent batch record review can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. batchRecordReviewId and batchRecordReviewName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1351000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BRR-PCM5B26091-E01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | batchRecordReviewId | String | - | Yes | Reference to u_mes_bmr_batchRecordReview._id: the parent document this one belongs to | `"1350000000000001"` | Reference: u_mes_bmr_batchRecordReview._id |
| 7 | batchRecordReviewName | String | - | Yes | Display value of batchRecordReviewId, copied from u_mes_bmr_batchRecordReview.recordNo | `"BRR-PCM5B26091"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number | `NumberInt(10)` |  |
| 9 | exceptionType | String | - | Yes | Kind of exception | `"Interlock Override"` | Interlock Override; Out Of Specification Result; Manual Data Entry; Data Correction; Missing Signature; Deviation; Late Entry; Hold |
| 10 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_interlockEvent"` | u_mes_plan_interlockEvent; u_mes_qual_inspectionResult; u_mes_syst_auditTrail; u_mes_qual_nonconformance; u_mes_qual_qualityHold; u_mes_plan_operationExecution |
| 11 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1307000000000014"` | Reference: Any collection (see relatedCollectionName) |
| 12 | relatedEntityName | String | - | Yes | Display value of the related document | `"ILK-20260921-00228"` |  |
| 13 | description | String | - | Yes | What was found | `"Capping chuck life limit overridden by the supervisor for the last 300 bottles until the planned chuck change"` |  |
| 14 | assessment | String | - | No (null allowed) | Assessment; null while open | `"Impact Assessed Acceptable"` | No Impact; Impact Assessed Acceptable; Requires Deviation; Requires Correction |
| 15 | assessedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'assessed' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 16 | assessedBy | String | - | No (null allowed) | Display name of the user in assessedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 17 | assessedAt | Date | Datetime | No (null allowed) | Time of the assessment | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 20 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 22 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 23 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ batchRecordReviewId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/11_batch_manufacturing_record/validators/u_mes_bmr_batchRecordReviewException.json
- Indexes: 03_design/11_batch_manufacturing_record/indexes/u_mes_bmr_batchRecordReviewException.js
- Sample documents (10): 03_design/11_batch_manufacturing_record/samples/u_mes_bmr_batchRecordReviewException.js
