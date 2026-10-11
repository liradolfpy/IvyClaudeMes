# u_mes_qlt_checkSheetItem

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per item of a check sheet |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qlt_checkSheet |
| _id pattern | <checkSheetId>-I<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (11 required, 5 may be null) |

## Structure

Child collection. The parent check sheet can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. checkSheetId and checkSheetName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <checkSheetId>-I<nnn> | `"CKS-TRQ-01-SOS-I001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01-SOS-I001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | checkSheetId | String | Yes | Reference to u_mes_qlt_checkSheet._id: the parent document this one belongs to | `"CKS-TRQ-01-SOS"` | Reference: u_mes_qlt_checkSheet._id |
| 6 | checkSheetName | String | Yes | Display value of checkSheetId, copied from u_mes_qlt_checkSheet.name | `"Start of shift check, torque station"` |  |
| 7 | itemNo | Int32 | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 8 | question | String | Yes | Question of the check sheet item | `"Is the master leak part detected as Not OK by the tester?"` |  |
| 9 | answerType | String | Yes | Answer type | `"Yes No"` | Yes No; Number; Text |
| 10 | expectedAnswer | String | No (null allowed) | Expected answer | `"Yes"` |  |
| 11 | lowerLimit | Decimal128 | No (null allowed) | Lower limit | `NumberDecimal("12.0")` |  |
| 12 | upperLimit | Decimal128 | No (null allowed) | Upper limit | `NumberDecimal("16.0")` |  |
| 13 | unitText | String | No (null allowed) | Unit text | `"N.m"` |  |
| 14 | isCritical | Boolean | Yes | True when the record is critical | `true` |  |
| 15 | reactionOnFail | String | No (null allowed) | Reaction on fail | `"Stop the station and call the line leader"` |  |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ checkSheetId: 1, itemNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_checkSheetItem.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_checkSheetItem.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_checkSheetItem.js
