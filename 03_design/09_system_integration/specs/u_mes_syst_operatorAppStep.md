# u_mes_syst_operatorAppStep

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per step of a operator app |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_operatorApp |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (13 required, 3 may be null) |

## Structure

Child collection. The parent operator app can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppId and operatorAppName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1236000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-GDC-01-S01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | operatorAppId | String | - | Yes | Reference to u_mes_syst_operatorApp._id: the parent document this one belongs to | `"1233000000000001"` | Reference: u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - | Yes | Display value of operatorAppId, copied from u_mes_syst_operatorApp.name | `"Operator app, Gravity Die Casting Cell 1"` |  |
| 8 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 9 | name | String | - | Yes | Name of the operator app step | `"Prepare and load"` |  |
| 10 | widgetType | String | - | Yes | Widget type | `"Work Instruction"` | Work Instruction; Data Entry; Device Result; Scan; Checklist; Signature; Summary |
| 11 | workInstructionId | String | - | Yes | Reference to u_mes_prod_workInstruction._id | `"1065000000000001"` | Reference: u_mes_prod_workInstruction._id |
| 12 | workInstructionName | String | - | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Pouring and die cycle - Caliper body LH"` |  |
| 13 | inspectionPlanId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"1142000000000001"` | Reference: u_mes_qual_inspectionPlan._id |
| 14 | inspectionPlanName | String | - | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, gravity die casting"` |  |
| 15 | nextStepNo | Int32 | - | No (null allowed) | Next step number | `NumberInt(20)` |  |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operatorAppId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ workInstructionId: 1 }` | No | Look-up of lines by work instruction |
| 3 | `{ inspectionPlanId: 1 }` | No | Look-up of lines by inspection plan |

## Referenced by

u_mes_syst_operatorAppStepTrigger.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_operatorAppStep.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_operatorAppStep.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_operatorAppStep.js
