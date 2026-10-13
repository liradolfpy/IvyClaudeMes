# u_mes_syst_operatorAppStepTrigger

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per trigger of a operator app step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_operatorAppStep |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (11 required, 1 may be null) |

## Structure

Child collection. The parent operator app step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppStepId and operatorAppStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1237000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-GDC-01-S01-T01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | operatorAppStepId | String | - | Yes | Reference to u_mes_syst_operatorAppStep._id: the parent document this one belongs to | `"1236000000000001"` | Reference: u_mes_syst_operatorAppStep._id |
| 7 | operatorAppStepName | String | - | Yes | Display value of operatorAppStepId, copied from u_mes_syst_operatorAppStep.recordNo | `"APP-GDC-01-S01"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | triggerEvent | String | - | Yes | Trigger event | `"Step Opened"` | Step Opened; Button Pressed; Scan Completed; Device Result Received; Value Out Of Limit; Timer Expired |
| 10 | triggerAction | String | - | Yes | Trigger action | `"Go To Step"` | Go To Step; Complete Operation; Raise Nonconformance; Raise Andon; Print Label; Block Station |
| 11 | triggerTarget | String | - | No (null allowed) | Trigger target | `"30"` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operatorAppStepId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_operatorAppStepTrigger.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_operatorAppStepTrigger.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_operatorAppStepTrigger.js
