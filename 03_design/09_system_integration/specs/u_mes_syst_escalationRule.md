# u_mes_syst_escalationRule

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Routing and SLA rule for an exception type: first owner role, response and resolution targets. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 17 (12 required, 5 may be null) |
| Estimated volume per year | about 40 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per escalation rule, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with escalationRuleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_escalationRuleLevel | Child | level |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1334000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ESC-BRKDN-CRIT"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Rule name | `"Critical breakdown, assembly line"` |  |
| 6 | sourceType | String | - | Yes | Exception source | `"Breakdown"` | Interlock; Andon; Alarm; Alert Rule; Breakdown; Audit; Nonconformance; Customer Complaint |
| 7 | severityClass | String | - | No (null allowed) | Severity the rule applies to (null = all) | `"Critical"` | Low; Medium; High; Critical |
| 8 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 10 | firstResponderRoleId | String | - | Yes | Reference to u_mes_mast_role._id: first responder role | `"1026000000000007"` | Reference: u_mes_mast_role._id |
| 11 | firstResponderRoleName | String | - | Yes | Display value of firstResponderRoleId, copied from u_mes_mast_role.name | `"Maintenance Technician"` |  |
| 12 | requiredSkillId | String | - | No (null allowed) | Reference to u_mes_mast_skill._id: required skill | `null` | Reference: u_mes_mast_skill._id |
| 13 | requiredSkillName | String | - | No (null allowed) | Display value of requiredSkillId, copied from u_mes_mast_skill.name | `null` |  |
| 14 | responseTargetMinutes | Int32 | - | Yes | Target to acknowledge | `NumberInt(5)` |  |
| 15 | resolutionTargetMinutes | Int32 | - | Yes | Target to resolve | `NumberInt(60)` |  |
| 16 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ firstResponderRoleId: 1 }` | No | Look-up of documents by first responder role |
| 5 | `{ requiredSkillId: 1 }` | No | Look-up of documents by required skill |

## Referenced by

u_mes_syst_notification, u_mes_plan_andonEvent, u_mes_plan_andonType, u_mes_qual_auditSchedule, u_mes_perf_alarmDefinition, u_mes_syst_interlockRule, u_mes_syst_escalationRuleLevel, u_mes_syst_alertRule.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_escalationRule.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_escalationRule.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_escalationRule.js
