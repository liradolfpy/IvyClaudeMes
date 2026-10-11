# u_mes_prod_workInstructionStep

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per step of a work instruction |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_workInstruction |
| _id pattern | <workInstructionId>-S<nnn> |
| Display value used by references | title |
| Keys | 18 (14 required, 4 may be null) |

## Structure

Child collection. The parent work instruction can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. workInstructionId and workInstructionName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workInstructionId>-S<nnn> | `"WI-WI-OP070-001-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP070-001-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workInstructionId | String | Yes | Reference to u_mes_prod_workInstruction._id: the parent document this one belongs to | `"WI-WI-OP070-001"` | Reference: u_mes_prod_workInstruction._id |
| 6 | workInstructionName | String | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | title | String | Yes | Title of the work instruction step; used as its display value in other collections | `"Tighten bleed screw"` |  |
| 9 | instructionText | String | Yes | Instruction text | `"Place the bleed screw in the socket and press both start buttons"` |  |
| 10 | inputType | String | Yes | Input type | `"Confirmation"` | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| 11 | expectedValue | Decimal128 | No (null allowed) | Expected value | `NumberDecimal("14.0")` |  |
| 12 | lowerLimit | Decimal128 | No (null allowed) | Lower limit | `NumberDecimal("12.0")` |  |
| 13 | upperLimit | Decimal128 | No (null allowed) | Upper limit | `NumberDecimal("16.0")` |  |
| 14 | isMandatory | Boolean | Yes | True when the record is mandatory | `true` |  |
| 15 | requiresScan | Boolean | Yes | True when scan is required | `true` |  |
| 16 | caution | String | No (null allowed) | Caution of the work instruction step | `"Do not reuse a bleed screw that has been tightened once"` |  |
| 17 | standardTimeSec | Decimal128 | Yes | Standard time (seconds) | `NumberDecimal("12.0")` |  |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

u_mes_prod_workInstructionStepMediaControlledDocument, u_mes_prod_workInstructionStepProductVariant, u_mes_prod_workInstructionStepTool, u_mes_prod_workInstructionStepCharacteristic.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstructionStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstructionStep.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_workInstructionStep.js
