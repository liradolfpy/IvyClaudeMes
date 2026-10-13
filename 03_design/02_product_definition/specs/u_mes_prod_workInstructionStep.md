# u_mes_prod_workInstructionStep

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per step of a work instruction |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_workInstruction |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 22 (15 required, 7 may be null) |

## Structure

Child collection. The parent work instruction can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. workInstructionId and workInstructionName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1066000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP010-001-S01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workInstructionId | String | - | Yes | Reference to u_mes_prod_workInstruction._id: the parent document this one belongs to | `"1065000000000001"` | Reference: u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Pouring and die cycle - Caliper body LH"` |  |
| 8 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 9 | title | String | - | Yes | Title of the work instruction step | `"Skim the ladle, pour in one continuous stream and start the tilt cycle"` |  |
| 10 | instructionText | String | - | Yes | Instruction text | `"Skim the ladle, pour in one continuous stream and start the tilt cycle"` |  |
| 11 | inputType | String | - | Yes | Input type | `"None"` | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| 12 | expectedValue | Decimal128 | - | No (null allowed) | Expected value | `NumberDecimal("400.0")` |  |
| 13 | lowerLimit | Decimal128 | - | No (null allowed) | Lower limit | `NumberDecimal("380.0")` |  |
| 14 | upperLimit | Decimal128 | - | No (null allowed) | Upper limit | `NumberDecimal("420.0")` |  |
| 15 | isMandatory | Boolean | - | Yes | True when the record is mandatory | `true` |  |
| 16 | requiresScan | Boolean | - | Yes | True when scan is required | `true` |  |
| 17 | caution | String | - | No (null allowed) | Caution of the work instruction step | `"Do not reuse a bleed screw that has been tightened once"` |  |
| 18 | standardTimeSec | Decimal128 | - | Yes | Standard time (seconds) | `NumberDecimal("12.0")` |  |
| 19 | arContentControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: ar content controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 20 | arContentControlledDocumentName | String | - | No (null allowed) | Display value of arContentControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 21 | arAnchorRef | String | - | No (null allowed) | Anchor reference of the overlay on the part or fixture | `null` |  |
| 22 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ arContentControlledDocumentId: 1 }` | No | Look-up of lines by ar content controlled document |

## Referenced by

u_mes_prod_workInstructionStepMediaControlledDocument, u_mes_prod_workInstructionStepProductVariant, u_mes_prod_workInstructionStepTool, u_mes_prod_workInstructionStepCharacteristic.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstructionStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstructionStep.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_workInstructionStep.js
