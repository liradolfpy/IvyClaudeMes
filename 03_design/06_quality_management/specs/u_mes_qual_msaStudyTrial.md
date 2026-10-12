# u_mes_qual_msaStudyTrial

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per trial of a MSA study |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_msaStudy |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (17 required, 1 may be null) |

## Structure

Child collection. The parent MSA study can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. msaStudyId and msaStudyName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1194000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MSA-2026-0009-T01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | msaStudyId | String | - | Yes | Reference to u_mes_qual_msaStudy._id: the parent document this one belongs to | `"1192000000000001"` | Reference: u_mes_qual_msaStudy._id |
| 6 | msaStudyName | String | - | Yes | Display value of msaStudyId, copied from u_mes_qual_msaStudy.recordNo | `"MSA-2026-0009"` |  |
| 7 | appraiserUserId | String | - | Yes | Reference to u_mes_mast_user._id: appraiser user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 8 | appraiserUserName | String | - | Yes | Display value of appraiserUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 9 | partNo | Int32 | - | Yes | Number of the study part | `NumberInt(4)` |  |
| 10 | trialNo | Int32 | - | Yes | Trial number | `NumberInt(1)` |  |
| 11 | measuredValue | Decimal128 | - | No (null allowed) | Measured value | `NumberDecimal("8.05")` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 14 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 17 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ msaStudyId: 1, appraiserUserId: 1, partNo: 1, trialNo: 1 }` | Yes | One reading per appraiser, part and trial |
| 2 | `{ appraiserUserId: 1 }` | No | Look-up of lines by appraiser user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_msaStudyTrial.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_msaStudyTrial.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_msaStudyTrial.js
