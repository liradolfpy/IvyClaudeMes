# u_mes_sys_operatorAppStepTrigger

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | One document per trigger of a operator app step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_sys_operatorAppStep |
| _id pattern | <operatorAppStepId>-T<nnn> |
| Display value used by references | recordNo |
| Keys | 11 (10 required, 1 may be null) |

## Structure

Child collection. The parent operator app step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppStepId and operatorAppStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <operatorAppStepId>-T<nnn> | `"APP-APP-TRQ-01-S001-T001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-TRQ-01-S001-T001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operatorAppStepId | String | Yes | Reference to u_mes_sys_operatorAppStep._id: the parent document this one belongs to | `"APP-APP-TRQ-01-S001"` | Reference: u_mes_sys_operatorAppStep._id |
| 6 | operatorAppStepName | String | Yes | Display value of operatorAppStepId, copied from u_mes_sys_operatorAppStep.name | `"APP-TRQ-01-S001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | triggerEvent | String | Yes | Trigger event | `"Device Result Received"` | Step Opened; Button Pressed; Scan Completed; Device Result Received; Value Out Of Limit; Timer Expired |
| 9 | triggerAction | String | Yes | Trigger action | `"Go To Step"` | Go To Step; Complete Operation; Raise Nonconformance; Raise Andon; Print Label; Block Station |
| 10 | triggerTarget | String | No (null allowed) | Trigger target | `"30"` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operatorAppStepId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_operatorAppStepTrigger.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_operatorAppStepTrigger.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_operatorAppStepTrigger.js
