# u_mes_qual_ppapSubmissionMsaStudy

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one PPAP submission to one MSA study; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qual_ppapSubmission |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A PPAP submission can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. ppapSubmissionId and ppapSubmissionName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1188000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PPAP-5110-10-0100-D-01-MS01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | ppapSubmissionId | String | - | Yes | Reference to u_mes_qual_ppapSubmission._id: the parent document this one belongs to | `"1186000000000001"` | Reference: u_mes_qual_ppapSubmission._id |
| 6 | ppapSubmissionName | String | - | Yes | Display value of ppapSubmissionId, copied from u_mes_qual_ppapSubmission.recordNo | `"PPAP-5110-10-0100-D-01"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | msaStudyId | String | - | Yes | Reference to u_mes_qual_msaStudy._id | `"1192000000000010"` | Reference: u_mes_qual_msaStudy._id |
| 9 | msaStudyName | String | - | Yes | Display value of msaStudyId, copied from u_mes_qual_msaStudy.recordNo | `"MSA-2026-0018"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 12 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 15 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ ppapSubmissionId: 1, msaStudyId: 1 }` | Yes | One link per pair |
| 2 | `{ msaStudyId: 1, ppapSubmissionId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_ppapSubmissionMsaStudy.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_ppapSubmissionMsaStudy.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_ppapSubmissionMsaStudy.js
