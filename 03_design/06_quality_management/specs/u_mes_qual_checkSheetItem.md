# u_mes_qual_checkSheetItem

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per item of a check sheet |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_checkSheet |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (11 required, 5 may be null) |

## Structure

Child collection. The parent check sheet can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. checkSheetId and checkSheetName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1147000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SOS-GDC-01-I01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | checkSheetId | String | Yes | Reference to u_mes_qual_checkSheet._id: the parent document this one belongs to | `"1146000000000001"` | Reference: u_mes_qual_checkSheet._id |
| 6 | checkSheetName | String | Yes | Display value of checkSheetId, copied from u_mes_qual_checkSheet.name | `"Start of shift check, Gravity Die Casting Cell 1"` |  |
| 7 | itemNo | Int32 | Yes | Item number within the parent record | `NumberInt(1)` |  |
| 8 | question | String | Yes | Question of the check sheet item | `"Is the die coating intact on both die halves?"` |  |
| 9 | answerType | String | Yes | Answer type | `"Yes No"` | Yes No; Number; Text |
| 10 | expectedAnswer | String | No (null allowed) | Expected answer | `"Yes"` |  |
| 11 | lowerLimit | Decimal128 | No (null allowed) | Lower limit | `NumberDecimal("7.50")` |  |
| 12 | upperLimit | Decimal128 | No (null allowed) | Upper limit | `NumberDecimal("8.50")` |  |
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

- Validator: 03_design/06_quality_management/validators/u_mes_qual_checkSheetItem.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_checkSheetItem.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_checkSheetItem.js
