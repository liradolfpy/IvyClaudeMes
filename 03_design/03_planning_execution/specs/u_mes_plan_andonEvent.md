# u_mes_plan_andonEvent

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Help calls from stations (quality, material, maintenance, safety) with response and escalation times |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 46 (29 required, 17 may be null) |
| Estimated volume per year | ~40,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per andon event, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with andonEventId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_andonEventEscalation | Child | escalation |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1251000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"AND-2026-000195"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 10 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 11 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 12 | andonTypeId | String | - | Yes | Reference to u_mes_plan_andonType._id | `"1292000000000003"` | Reference: u_mes_plan_andonType._id |
| 13 | andonTypeName | String | - | Yes | Display value of andonTypeId, copied from u_mes_plan_andonType.name | `"Maintenance"` |  |
| 14 | reasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 15 | reasonCodeName | String | - | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 16 | raisedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'raised' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 17 | raisedBy | String | - | Yes | Display name of the user in raisedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 18 | raisedAt | Date | Datetime | Yes | Date and time when the record was raised. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 19 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 20 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 21 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 22 | resolvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'resolved' | `null` | Reference: u_mes_mast_user._id |
| 23 | resolvedBy | String | - | No (null allowed) | Display name of the user in resolvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 24 | resolvedAt | Date | Datetime | No (null allowed) | Date and time when the record was resolved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 25 | responseSec | Int32 | - | Yes | Response (seconds) | `NumberInt(210)` |  |
| 26 | resolutionSec | Int32 | - | Yes | Resolution (seconds) | `NumberInt(840)` |  |
| 27 | lineStopped | Boolean | - | Yes | True when: line stopped | `true` |  |
| 28 | downtimeEventId | String | - | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 29 | downtimeEventName | String | - | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 30 | description | String | - | Yes | Description of the andon event | `"Castings sticking in die 2, operator needs maintenance"` |  |
| 31 | resolutionText | String | - | No (null allowed) | Resolution text | `"Ejector pin polished and die coat thickness corrected"` |  |
| 32 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 33 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 34 | severityClass | String | - | Yes | Severity of the call | `"High"` | Low; Medium; High; Critical |
| 35 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `"1220000000000001"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 36 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 37 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000002"` | Reference: u_mes_syst_escalationRule._id |
| 38 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Breakdown, all lines"` |  |
| 39 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Resolved; Cancelled |
| 40 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 41 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 42 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 43 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 44 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 45 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 46 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Raised, Acknowledged, Resolved, Cancelled. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ andonTypeId: 1 }` | No | Look-up of documents by andon type |
| 7 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 8 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_matl_materialRequest, u_mes_maint_maintenanceWorkOrder, u_mes_syst_notification, u_mes_plan_andonEventEscalation.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_andonEvent.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_andonEvent.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_andonEvent.js
