# u_mes_prod_workInstructionKeyPoint

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per key point value of a work instruction |
| Kind | Value list |
| Data class | Master |
| Parent collection | u_mes_prod_workInstruction |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Value-list collection. A work instruction can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. workInstructionId and workInstructionName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1072000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP010-001-KP01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workInstructionId | String | - | Yes | Reference to u_mes_prod_workInstruction._id: the parent document this one belongs to | `"1065000000000001"` | Reference: u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Pouring and die cycle - Caliper body LH"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | keyPoint | String | - | Yes | Key point | `"Die face temperature must be above 380 degC before the first pour"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstructionKeyPoint.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstructionKeyPoint.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_workInstructionKeyPoint.js
