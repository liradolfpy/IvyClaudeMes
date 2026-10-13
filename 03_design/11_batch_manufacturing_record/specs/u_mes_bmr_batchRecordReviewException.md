# u_mes_bmr_batchRecordReviewException

| Property | Value |
|---|---|
| Module | Batch Manufacturing Record (bmr) |
| Purpose | One document per exception of a batch record review |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_bmr_batchRecordReview |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (19 required, 4 may be null) |

## Structure

Child collection. The parent batch record review can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. batchRecordReviewId and batchRecordReviewName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1351000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BRR-PO-1000412-E01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | batchRecordReviewId | String | - | Yes | Reference to u_mes_bmr_batchRecordReview._id: the parent document this one belongs to | `"1350000000000001"` | Reference: u_mes_bmr_batchRecordReview._id |
| 6 | batchRecordReviewName | String | - | Yes | Display value of batchRecordReviewId, copied from u_mes_bmr_batchRecordReview.recordNo | `"BRR-PO-1000412"` |  |
| 7 | lineNo | Int32 | - | Yes | Line number | `NumberInt(10)` |  |
| 8 | exceptionType | String | - | Yes | Kind of exception | `"Interlock Override"` | Interlock Override; Out Of Specification Result; Manual Data Entry; Data Correction; Missing Signature; Deviation; Late Entry; Hold |
| 9 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_interlockEvent"` | u_mes_plan_interlockEvent; u_mes_qual_inspectionResult; u_mes_syst_auditTrail; u_mes_qual_nonconformance; u_mes_qual_qualityHold; u_mes_plan_operationExecution |
| 10 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1307000000000004"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | Yes | Display value of the related document | `"ILK-20260921-00228"` |  |
| 12 | description | String | - | Yes | What was found | `"Tool life limit of the nutrunner socket overridden by the supervisor for 40 rundowns until the socket change"` |  |
| 13 | assessment | String | - | No (null allowed) | Assessment; null while open | `"Impact Assessed Acceptable"` | No Impact; Impact Assessed Acceptable; Requires Deviation; Requires Correction |
| 14 | assessedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'assessed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 15 | assessedBy | String | - | No (null allowed) | Display name of the user in assessedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | assessedAt | Date | Datetime | No (null allowed) | Time of the assessment | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T09:50:00.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
