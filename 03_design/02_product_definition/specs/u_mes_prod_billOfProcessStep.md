# u_mes_prod_billOfProcessStep

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per step of a bill of process |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_billOfProcess |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (12 required, 6 may be null) |

## Structure

Child collection. The parent bill of process can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfProcessId and billOfProcessName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1058000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"BOP-5110-10-0100-R01-S01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfProcessId | String | Yes | Reference to u_mes_prod_billOfProcess._id: the parent document this one belongs to | `"1057000000000001"` | Reference: u_mes_prod_billOfProcess._id |
| 6 | billOfProcessName | String | Yes | Display value of billOfProcessId, copied from u_mes_prod_billOfProcess.recordNo | `"BOP-5110-10-0100-R01"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 10 | recipeId | String | No (null allowed) | Reference to u_mes_prod_recipe._id | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 11 | recipeName | String | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 12 | workInstructionId | String | No (null allowed) | Reference to u_mes_prod_workInstruction._id | `"1065000000000001"` | Reference: u_mes_prod_workInstruction._id |
| 13 | workInstructionName | String | No (null allowed) | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Pouring and die cycle - Caliper body LH"` |  |
| 14 | inspectionPlanId | String | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"1142000000000001"` | Reference: u_mes_qual_inspectionPlan._id |
| 15 | inspectionPlanName | String | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, gravity die casting"` |  |
| 16 | cycleTimeSec | Decimal128 | Yes | Cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 17 | manning | Int32 | Yes | Manning of the bill of process step | `NumberInt(1)` |  |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfProcessId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ recipeId: 1 }` | No | Look-up of lines by recipe |
| 4 | `{ workInstructionId: 1 }` | No | Look-up of lines by work instruction |

## Referenced by

u_mes_prod_billOfProcessStepEquipment, u_mes_prod_billOfProcessStepTool, u_mes_prod_billOfProcessStepRequiredSkill, u_mes_prod_billOfProcessStepConsumedComponent, u_mes_prod_billOfProcessStepInterlock, u_mes_prod_billOfProcessStepProcessParameter.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfProcessStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfProcessStep.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfProcessStep.js
