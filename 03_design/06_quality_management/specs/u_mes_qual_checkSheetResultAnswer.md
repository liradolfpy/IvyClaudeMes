# u_mes_qual_checkSheetResultAnswer

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per answer of a check sheet result |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_checkSheetResult |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (16 required, 3 may be null) |

## Structure

Child collection. The parent check sheet result can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. checkSheetResultId and checkSheetResultName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1149000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CKR-2026-000479-A01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | checkSheetResultId | String | - | Yes | Reference to u_mes_qual_checkSheetResult._id: the parent document this one belongs to | `"1148000000000001"` | Reference: u_mes_qual_checkSheetResult._id |
| 7 | checkSheetResultName | String | - | Yes | Display value of checkSheetResultId, copied from u_mes_qual_checkSheetResult.recordNo | `"CKR-2026-000479"` |  |
| 8 | itemNo | Int32 | - | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 9 | answerText | String | - | No (null allowed) | Answer text | `"Yes"` |  |
| 10 | answerNumber | Decimal128 | - | No (null allowed) | Answer number | `null` |  |
| 11 | passed | Boolean | - | Yes | True when: passed | `true` |  |
| 12 | comment | String | - | No (null allowed) | Comment of the check sheet result answer | `"Verified against customer drawing revision D"` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:54:40.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:54:40.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ checkSheetResultId: 1, itemNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_checkSheetResultAnswer.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_checkSheetResultAnswer.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_checkSheetResultAnswer.js
