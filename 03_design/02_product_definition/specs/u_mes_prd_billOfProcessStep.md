# u_mes_prd_billOfProcessStep

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per step of a bill of process |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prd_billOfProcess |
| _id pattern | <billOfProcessId>-S<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (12 required, 6 may be null) |

## Structure

Child collection. The parent bill of process can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfProcessId and billOfProcessName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <billOfProcessId>-S<nnn> | `"BOP-5110-10-0100-BOP01-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-BOP01-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfProcessId | String | Yes | Reference to u_mes_prd_billOfProcess._id: the parent document this one belongs to | `"BOP-5110-10-0100-BOP01"` | Reference: u_mes_prd_billOfProcess._id |
| 6 | billOfProcessName | String | Yes | Display value of billOfProcessId, copied from u_mes_prd_billOfProcess.recordNo | `"5110-10-0100-BOP01"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 10 | recipeId | String | No (null allowed) | Reference to u_mes_prd_recipe._id | `"RCP-TRQ-PRG-07"` | Reference: u_mes_prd_recipe._id |
| 11 | recipeName | String | No (null allowed) | Display value of recipeId, copied from u_mes_prd_recipe.name | `"Bleed screw M10 torque program"` |  |
| 12 | workInstructionId | String | No (null allowed) | Reference to u_mes_prd_workInstruction._id | `"WI-WI-OP070-001"` | Reference: u_mes_prd_workInstruction._id |
| 13 | workInstructionName | String | No (null allowed) | Display value of workInstructionId, copied from u_mes_prd_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 14 | inspectionPlanId | String | No (null allowed) | Reference to u_mes_qlt_inspectionPlan._id | `"IP-OP030-INP-01"` | Reference: u_mes_qlt_inspectionPlan._id |
| 15 | inspectionPlanName | String | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qlt_inspectionPlan.name | `"Machining in-process inspection, caliper body LH"` |  |
| 16 | cycleTimeSec | Decimal128 | Yes | Cycle time (seconds) | `NumberDecimal("34.2")` |  |
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

u_mes_prd_billOfProcessStepEquipment, u_mes_prd_billOfProcessStepTool, u_mes_prd_billOfProcessStepRequiredSkill, u_mes_prd_billOfProcessStepConsumedComponent, u_mes_prd_billOfProcessStepInterlock, u_mes_prd_billOfProcessStepProcessParameter.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_billOfProcessStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_billOfProcessStep.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_billOfProcessStep.js
