# u_mes_syst_escalationRuleLevel

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per level of a escalation rule |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_escalationRule |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Child collection. The parent escalation rule can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. escalationRuleId and escalationRuleName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1335000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ESC-BRKDN-CRIT-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | escalationRuleId | String | - | Yes | Reference to u_mes_syst_escalationRule._id: the parent document this one belongs to | `"1334000000000001"` | Reference: u_mes_syst_escalationRule._id |
| 7 | escalationRuleName | String | - | Yes | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Critical breakdown, assembly line"` |  |
| 8 | level | Int32 | - | Yes | Escalation level (1 = first escalation) | `NumberInt(1)` |  |
| 9 | delayMinutes | Int32 | - | Yes | Minutes after raise without acknowledgement / resolution | `NumberInt(5)` |  |
| 10 | basis | String | - | Yes | What triggers the level | `"Not Acknowledged"` | Not Acknowledged; Not Resolved |
| 11 | roleId | String | - | Yes | Reference to u_mes_mast_role._id | `"1026000000000004"` | Reference: u_mes_mast_role._id |
| 12 | roleName | String | - | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Supervisor"` |  |
| 13 | notificationTypeId | String | - | Yes | Reference to u_mes_syst_notificationType._id | `"1291000000000001"` | Reference: u_mes_syst_notificationType._id |
| 14 | notificationTypeName | String | - | Yes | Display value of notificationTypeId, copied from u_mes_syst_notificationType.name | `"Andon Escalation"` |  |
| 15 | channel | String | - | Yes | Channel | `"Andon Board"` | Andon Board; SMS; Email; Mobile App; Public Address |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ escalationRuleId: 1, level: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ roleId: 1 }` | No | Look-up of lines by role |
| 3 | `{ notificationTypeId: 1 }` | No | Look-up of lines by notification type |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_escalationRuleLevel.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_escalationRuleLevel.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_escalationRuleLevel.js
