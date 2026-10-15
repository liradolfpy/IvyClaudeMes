# u_mes_perf_alarmDefinition

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | Alarm code master per equipment type with class, severity, restart-block and escalation settings. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 22 (15 required, 7 may be null) |
| Estimated volume per year | about 2,000 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per alarm definition, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1324000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ALD-GDC-A2031"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | equipmentTypeId | String | - | Yes | Reference to u_mes_mast_equipmentType._id | `"1261000000000001"` | Reference: u_mes_mast_equipmentType._id |
| 7 | equipmentTypeName | String | - | Yes | Display value of equipmentTypeId, copied from u_mes_mast_equipmentType.name | `"Gravity Die Casting Machine"` |  |
| 8 | alarmCode | String | - | Yes | Controller alarm code | `"A2031"` |  |
| 9 | alarmText | String | - | Yes | Standard alarm text | `"Die temperature upper half above high limit"` |  |
| 10 | alarmClass | String | - | Yes | Alarm class | `"Process"` | Process; Equipment; Safety; Quality; Utility |
| 11 | severityClass | String | - | Yes | Severity | `"High"` | Low; Medium; High; Critical |
| 12 | blocksRestart | Boolean | - | Yes | Restart requires authorisation | `true` |  |
| 13 | authorizingRoleId | String | - | No (null allowed) | Reference to u_mes_mast_role._id: authorizing role | `"1026000000000004"` | Reference: u_mes_mast_role._id |
| 14 | authorizingRoleName | String | - | No (null allowed) | Display value of authorizingRoleId, copied from u_mes_mast_role.name | `"Production Supervisor"` |  |
| 15 | defaultReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: default reason code | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 16 | defaultReasonCodeName | String | - | No (null allowed) | Display value of defaultReasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 17 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000002"` | Reference: u_mes_syst_escalationRule._id |
| 18 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Breakdown, all lines"` |  |
| 19 | createsDowntime | Boolean | - | Yes | Alarm opens a downtime event | `true` |  |
| 20 | responseInstruction | String | - | No (null allowed) | Response instruction text | `"Stop pouring, check die heater zones and thermocouple; restart after supervisor approval"` |  |
| 21 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 22 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentTypeId: 1 }` | No | Look-up of documents by equipment type |
| 4 | `{ authorizingRoleId: 1 }` | No | Look-up of documents by authorizing role |
| 5 | `{ defaultReasonCodeId: 1 }` | No | Look-up of documents by default reason code |
| 6 | `{ escalationRuleId: 1 }` | No | Look-up of documents by escalation rule |

## Referenced by

u_mes_perf_alarm.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_alarmDefinition.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_alarmDefinition.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_alarmDefinition.js
