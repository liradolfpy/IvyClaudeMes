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
| Keys | 36 (23 required, 13 may be null) |
| Estimated volume per year | ~500,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per alarm, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1212000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ALM-2026-000176"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 7 | processTagId | String | No (null allowed) | Reference to u_mes_perf_processTag._id | `"1210000000000001"` | Reference: u_mes_perf_processTag._id |
| 8 | processTagName | String | No (null allowed) | Display value of processTagId, copied from u_mes_perf_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 9 | iotDeviceId | String | No (null allowed) | Reference to u_mes_syst_iotDevice._id | `"1232000000000001"` | Reference: u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | No (null allowed) | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `"PLC, casting machine 1"` |  |
| 11 | alarmCode | String | Yes | Alarm code | `"A2031"` |  |
| 12 | alarmText | String | Yes | Alarm text | `"Die temperature upper half above high limit"` |  |
| 13 | alarmClass | String | Yes | Alarm class | `"Process"` | Process; Machine; Safety; Quality |
| 14 | severity | Int32 | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 15 | raisedAt | Date | Yes | Date and time when the record was raised | `ISODate("2026-09-17T01:21:40.000+0000")` |  |
| 16 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `null` |  |
| 17 | acknowledgedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 18 | acknowledgedBy | String | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 19 | clearedAt | Date | No (null allowed) | Date and time when the record was cleared | `null` |  |
| 20 | durationSec | Int32 | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 21 | triggerValue | Decimal128 | Yes | Trigger value | `NumberDecimal("421.0")` |  |
| 22 | limitValue | Decimal128 | Yes | Limit value | `NumberDecimal("420.0")` |  |
| 23 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 24 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 25 | causedStop | Boolean | Yes | True when: caused stop | `true` |  |
| 26 | downtimeEventId | String | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 27 | downtimeEventName | String | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 28 | actionTaken | String | No (null allowed) | Action taken | `"Ejector pin polished and die coat thickness corrected"` |  |
| 29 | status | String | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Cleared |
| 30 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-17T01:21:40.000+0000")` |  |
| 32 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 34 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-17T01:21:40.000+0000")` |  |
| 35 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
