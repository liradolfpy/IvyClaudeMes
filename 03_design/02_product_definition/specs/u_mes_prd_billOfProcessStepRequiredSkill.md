# u_mes_prd_billOfProcessStepRequiredSkill

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Links one bill of process step to one required skill; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prd_billOfProcessStep |
| _id pattern | <billOfProcessStepId>-RS<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A bill of process step can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. billOfProcessStepId and billOfProcessStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <billOfProcessStepId>-RS<nnn> | `"BOP-5110-10-0100-BOP01-S001-RS001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-BOP01-S001-RS001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfProcessStepId | String | Yes | Reference to u_mes_prd_billOfProcessStep._id: the parent document this one belongs to | `"BOP-5110-10-0100-BOP01-S001"` | Reference: u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | Yes | Display value of billOfProcessStepId, copied from u_mes_prd_billOfProcessStep.recordNo | `"5110-10-0100-BOP01-S001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | requiredSkillId | String | Yes | Reference to u_mes_mdm_skill._id: required skill | `"SKL-LEAK-TEST-OP"` | Reference: u_mes_mdm_skill._id |
| 9 | requiredSkillName | String | Yes | Display value of requiredSkillId, copied from u_mes_mdm_skill.name | `"Leak Test Operation"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfProcessStepId: 1, requiredSkillId: 1 }` | Yes | One link per pair |
| 2 | `{ requiredSkillId: 1, billOfProcessStepId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_billOfProcessStepRequiredSkill.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_billOfProcessStepRequiredSkill.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_billOfProcessStepRequiredSkill.js
