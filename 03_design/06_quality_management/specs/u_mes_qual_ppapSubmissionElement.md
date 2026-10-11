# u_mes_qual_ppapSubmissionElement

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per element of a PPAP submission |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_ppapSubmission |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent PPAP submission can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. ppapSubmissionId and ppapSubmissionName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1187000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PPAP-5110-10-0100-D-01-E01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | ppapSubmissionId | String | Yes | Reference to u_mes_qual_ppapSubmission._id: the parent document this one belongs to | `"1186000000000001"` | Reference: u_mes_qual_ppapSubmission._id |
| 6 | ppapSubmissionName | String | Yes | Display value of ppapSubmissionId, copied from u_mes_qual_ppapSubmission.recordNo | `"PPAP-5110-10-0100-D-01"` |  |
| 7 | elementNo | Int32 | Yes | PPAP element number 1 to 18 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the PPAP submission element | `"Design Records"` |  |
| 9 | required | Boolean | Yes | True when: required | `true` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Not Started"` | Not Started; In Progress; Complete; Not Applicable |
| 11 | controlledDocumentId | String | Yes | Reference to u_mes_syst_controlledDocument._id | `"1246000000000010"` | Reference: u_mes_syst_controlledDocument._id |
| 12 | controlledDocumentName | String | Yes | Display value of controlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Not Started, In Progress, Complete, Not Applicable. Initial state: Not Started. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ ppapSubmissionId: 1, elementNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ controlledDocumentId: 1 }` | No | Look-up of lines by controlled document |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_ppapSubmissionElement.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_ppapSubmissionElement.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_ppapSubmissionElement.js
