# u_mes_perf_alarm

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Alarm occurrences with severity, raised / acknowledged / cleared times |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 54 (25 required, 29 may be null) |
| Estimated volume per year | ~500,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per alarm, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1212000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ALM-2026-000176"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 7 | processTagId | String | - | No (null allowed) | Reference to u_mes_perf_processTag._id | `"1210000000000001"` | Reference: u_mes_perf_processTag._id |
| 8 | processTagName | String | - | No (null allowed) | Display value of processTagId, copied from u_mes_perf_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 9 | iotDeviceId | String | - | No (null allowed) | Reference to u_mes_syst_iotDevice._id | `"1232000000000001"` | Reference: u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | - | No (null allowed) | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `"PLC, casting machine 1"` |  |
| 11 | alarmCode | String | - | Yes | Alarm code | `"A2031"` |  |
| 12 | alarmText | String | - | Yes | Alarm text | `"Die temperature upper half above high limit"` |  |
| 13 | alarmClass | String | - | Yes | Alarm class | `"Process"` | Process; Machine; Safety; Quality |
| 14 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 15 | raisedAt | Date | Datetime | Yes | Date and time when the record was raised. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 16 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 17 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 18 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 19 | clearedAt | Date | Datetime | No (null allowed) | Date and time when the record was cleared. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 20 | durationSec | Int32 | - | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 21 | triggerValue | Decimal128 | - | Yes | Trigger value | `NumberDecimal("421.0")` |  |
| 22 | limitValue | Decimal128 | - | Yes | Limit value | `NumberDecimal("420.0")` |  |
| 23 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 24 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 25 | causedStop | Boolean | - | Yes | True when: caused stop | `true` |  |
| 26 | downtimeEventId | String | - | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 27 | downtimeEventName | String | - | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 28 | actionTaken | String | - | No (null allowed) | Action taken | `"Ejector pin polished and die coat thickness corrected"` |  |
| 29 | alarmDefinitionId | String | - | No (null allowed) | Reference to u_mes_perf_alarmDefinition._id | `"1324000000000001"` | Reference: u_mes_perf_alarmDefinition._id |
| 30 | alarmDefinitionName | String | - | No (null allowed) | Display value of alarmDefinitionId, copied from u_mes_perf_alarmDefinition.recordNo | `"ALD-GDC-A2031"` |  |
| 31 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 32 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 33 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 34 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 35 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 36 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 37 | productionDate | Date | Date | No (null allowed) | Production date | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 38 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `null` | Reference: u_mes_plan_wipUnit._id |
| 39 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `null` |  |
| 40 | blocksRestart | Boolean | - | Yes | True when restart needs authorisation (copied from the definition) | `true` |  |
| 41 | restartAuthorizedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'restart authorized' | `null` | Reference: u_mes_mast_user._id |
| 42 | restartAuthorizedBy | String | - | No (null allowed) | Display name of the user in restartAuthorizedById, copied from u_mes_mast_user.fullName | `null` |  |
| 43 | restartAuthorizedAt | Date | Datetime | No (null allowed) | Time of the restart authorisation | `null` |  |
| 44 | closureReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: closure reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 45 | closureReasonCodeName | String | - | No (null allowed) | Display value of closureReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 46 | escalationLevel | Int32 | - | Yes | Escalation level reached (0 = not escalated) | `NumberInt(1)` |  |
| 47 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Cleared |
| 48 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 49 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 50 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 51 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 52 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 53 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 54 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Raised, Acknowledged, Cleared. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ processTagId: 1 }` | No | Look-up of documents by process tag |
| 5 | `{ iotDeviceId: 1 }` | No | Look-up of documents by IoT device |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ downtimeEventId: 1 }` | No | Look-up of documents by downtime event |
| 8 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_perf_downtimeEvent, u_mes_syst_notification.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_alarm.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_alarm.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_alarm.js
