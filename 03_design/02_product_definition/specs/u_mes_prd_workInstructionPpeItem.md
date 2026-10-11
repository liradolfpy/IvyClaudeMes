# u_mes_prd_workInstructionPpeItem

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Links one work instruction to one ppe item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prd_workInstruction |
| _id pattern | <workInstructionId>-PI<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A work instruction can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. workInstructionId and workInstructionName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workInstructionId>-PI<nnn> | `"WI-WI-OP070-001-PI001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP070-001-PI001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workInstructionId | String | Yes | Reference to u_mes_prd_workInstruction._id: the parent document this one belongs to | `"WI-WI-OP070-001"` | Reference: u_mes_prd_workInstruction._id |
| 6 | workInstructionName | String | Yes | Display value of workInstructionId, copied from u_mes_prd_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | ppeItemId | String | Yes | Reference to u_mes_prd_ppeItem._id | `"PPE-SAFETY-GLASSES"` | Reference: u_mes_prd_ppeItem._id |
| 9 | ppeItemName | String | Yes | Display value of ppeItemId, copied from u_mes_prd_ppeItem.name | `"Safety Glasses"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionId: 1, ppeItemId: 1 }` | Yes | One link per pair |
| 2 | `{ ppeItemId: 1, workInstructionId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_workInstructionPpeItem.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_workInstructionPpeItem.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_workInstructionPpeItem.js
