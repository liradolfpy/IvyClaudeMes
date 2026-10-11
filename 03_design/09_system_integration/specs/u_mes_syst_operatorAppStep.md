# u_mes_syst_operatorAppStep

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per step of a operator app |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_operatorApp |
| _id pattern | <operatorAppId>-S<nnn> |
| Display value used by references | name |
| Keys | 15 (12 required, 3 may be null) |

## Structure

Child collection. The parent operator app can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppId and operatorAppName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <operatorAppId>-S<nnn> | `"APP-APP-TRQ-01-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-TRQ-01-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operatorAppId | String | Yes | Reference to u_mes_syst_operatorApp._id: the parent document this one belongs to | `"APP-APP-TRQ-01"` | Reference: u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | Yes | Display value of operatorAppId, copied from u_mes_syst_operatorApp.name | `"Torque station operator app"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | name | String | Yes | Name of the operator app step; used as its display value in other collections | `"Tighten and confirm result"` |  |
| 9 | widgetType | String | Yes | Widget type | `"Work Instruction"` | Work Instruction; Data Entry; Device Result; Scan; Checklist; Signature; Summary |
| 10 | workInstructionId | String | Yes | Reference to u_mes_prod_workInstruction._id | `"WI-WI-OP070-001"` | Reference: u_mes_prod_workInstruction._id |
| 11 | workInstructionName | String | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 12 | inspectionPlanId | String | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"IP-OP030-INP-01"` | Reference: u_mes_qual_inspectionPlan._id |
| 13 | inspectionPlanName | String | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"Machining in-process inspection, caliper body LH"` |  |
| 14 | nextStepNo | Int32 | No (null allowed) | Next step number | `NumberInt(80)` |  |
| 15 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_operatorAppStep.js
