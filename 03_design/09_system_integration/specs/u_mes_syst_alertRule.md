# u_mes_syst_alertRule

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Threshold rule on a KPI or signal with the resulting action. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 30 (17 required, 13 may be null) |
| Estimated volume per year | about 150 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per alert rule, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1336000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ALR-OEE-ASY01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Rule name | `"OEE below 75 percent on assembly line 1"` |  |
| 7 | metric | String | - | Yes | Metric watched | `"OEE"` | OEE; Availability; Downtime Minutes; Reject Rate; Output Gap; Process Deviation; SPC Rule Violation; Line-side Stock Cover; Environment Limit; Model Anomaly Score |
| 8 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 10 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `null` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `null` |  |
| 12 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `null` | Reference: u_mes_mast_equipment._id |
| 13 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 14 | processTagId | String | - | No (null allowed) | Reference to u_mes_perf_processTag._id | `null` | Reference: u_mes_perf_processTag._id |
| 15 | processTagName | String | - | No (null allowed) | Display value of processTagId, copied from u_mes_perf_processTag.description | `null` |  |
| 16 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `null` | Reference: u_mes_prod_item._id |
| 17 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `null` |  |
| 18 | comparison | String | - | Yes | Comparison | `"Less Than"` | Less Than; Greater Than; Outside Band |
| 19 | thresholdValue | Decimal128 | - | Yes | Threshold | `NumberDecimal("75.0")` |  |
| 20 | thresholdUpperValue | Decimal128 | - | No (null allowed) | Upper value for Outside Band | `null` |  |
| 21 | evaluationWindowMinutes | Int32 | - | Yes | Window evaluated | `NumberInt(60)` |  |
| 22 | severityClass | String | - | Yes | Severity | `"Medium"` | Low; Medium; High; Critical |
| 23 | actionType | String | - | Yes | Action | `"Notify"` | Notify; Hold; Stop Equipment; Block Process; Create Work Order; Create Nonconformance |
| 24 | notificationTypeId | String | - | Yes | Reference to u_mes_syst_notificationType._id | `"1291000000000005"` | Reference: u_mes_syst_notificationType._id |
| 25 | notificationTypeName | String | - | Yes | Display value of notificationTypeId, copied from u_mes_syst_notificationType.name | `"Order Late"` |  |
| 26 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000008"` | Reference: u_mes_syst_escalationRule._id |
| 27 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"KPI alert on OEE and rejects"` |  |
| 28 | falseAlertCount | Int32 | - | Yes | Alerts closed as false (tuning, Level 4) | `NumberInt(3)` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ processTagId: 1 }` | No | Look-up of documents by process tag |
| 7 | `{ itemId: 1 }` | No | Look-up of documents by item |

## Referenced by

u_mes_syst_notification.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_alertRule.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_alertRule.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_alertRule.js
