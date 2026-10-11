# u_mes_prd_workInstructionKeyPoint

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per key point value of a work instruction |
| Kind | Value list |
| Data class | Master |
| Parent collection | u_mes_prd_workInstruction |
| _id pattern | <workInstructionId>-KP<nnn> |
| Display value used by references | recordNo |
| Keys | 9 (9 required, 0 may be null) |

## Structure

Value-list collection. A work instruction can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. workInstructionId and workInstructionName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workInstructionId>-KP<nnn> | `"WI-WI-OP070-001-KP001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP070-001-KP001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workInstructionId | String | Yes | Reference to u_mes_prd_workInstruction._id: the parent document this one belongs to | `"WI-WI-OP070-001"` | Reference: u_mes_prd_workInstruction._id |
| 6 | workInstructionName | String | Yes | Display value of workInstructionId, copied from u_mes_prd_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | keyPoint | String | Yes | Key point | `"Bleed screw seat must be dry and free of chips"` |  |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_workInstructionKeyPoint.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_workInstructionKeyPoint.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_workInstructionKeyPoint.js
