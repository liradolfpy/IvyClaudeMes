# u_mes_qual_checkSheetResultAnswer

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per answer of a check sheet result |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_checkSheetResult |
| _id pattern | <checkSheetResultId>-A<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (15 required, 3 may be null) |

## Structure

Child collection. The parent check sheet result can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. checkSheetResultId and checkSheetResultName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <checkSheetResultId>-A<nnn> | `"CKR-20260929-A-TRQ-01-A001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-A-TRQ-01-A001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | checkSheetResultId | String | Yes | Reference to u_mes_qual_checkSheetResult._id: the parent document this one belongs to | `"CKR-20260929-A-TRQ-01"` | Reference: u_mes_qual_checkSheetResult._id |
| 6 | checkSheetResultName | String | Yes | Display value of checkSheetResultId, copied from u_mes_qual_checkSheetResult.recordNo | `"20260929-A-TRQ-01"` |  |
| 7 | itemNo | Int32 | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 8 | answerText | String | No (null allowed) | Answer text | `"Yes"` |  |
| 9 | answerNumber | Decimal128 | No (null allowed) | Answer number | `null` |  |
| 10 | passed | Boolean | Yes | True when: passed | `true` |  |
| 11 | comment | String | No (null allowed) | Comment of the check sheet result answer | `"Verified against customer drawing revision D"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ checkSheetResultId: 1, itemNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_checkSheetResultAnswer.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_checkSheetResultAnswer.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_checkSheetResultAnswer.js
