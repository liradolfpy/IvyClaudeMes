# u_mes_perf_downtimeEvent

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Classified stops with fault, reason path, action taken, duration, responsible group |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 47 (31 required, 16 may be null) |
| Estimated volume per year | ~120,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per downtime event, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with downtimeEventId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_perf_downtimeEventComment | Child | comment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1205000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"DT-2026-000196"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 9 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 10 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 11 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 12 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 13 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-16T18:30:00.000+0000")` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 16 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-17T01:21:40.000+0000")` |  |
| 17 | endedAt | Date | No (null allowed) | Date and time when the record was ended | `null` |  |
| 18 | durationMinutes | Int32 | Yes | Duration (minutes) | `NumberInt(95)` |  |
| 19 | downtimeType | String | Yes | Downtime type | `"Unplanned"` | Planned; Unplanned |
| 20 | faultCode | String | No (null allowed) | Fault code | `"E4107"` |  |
| 21 | faultText | String | No (null allowed) | Fault text | `"E1107 Ejector not returned to home position"` |  |
| 22 | reasonCodeId | String | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 23 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 24 | reasonPathText | String | No (null allowed) | Reason path text | `"Unplanned > Mechanical > Nutrunner > Socket worn"` |  |
| 25 | actionText | String | No (null allowed) | Action text | `"Ejector pin polished and die coat thickness corrected"` |  |
| 26 | isPlanned | Boolean | Yes | True when the record is planned | `false` |  |
| 27 | isMicroStop | Boolean | Yes | True when the record is micro stop | `false` |  |
| 28 | alarmId | String | No (null allowed) | Reference to u_mes_perf_alarm._id | `"1212000000000001"` | Reference: u_mes_perf_alarm._id |
| 29 | alarmName | String | No (null allowed) | Display value of alarmId, copied from u_mes_perf_alarm.recordNo | `"ALM-2026-000176"` |  |
| 30 | maintenanceWorkOrderId | String | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `"1220000000000001"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 31 | maintenanceWorkOrderName | String | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 32 | reportedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | reportedBy | String | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 34 | classifiedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'classified' | `null` | Reference: u_mes_mast_user._id |
| 35 | classifiedBy | String | No (null allowed) | Display name of the user in classifiedById, copied from u_mes_mast_user.fullName | `null` |  |
| 36 | classifiedAt | Date | No (null allowed) | Date and time when the record was classified | `null` |  |
| 37 | responseMinutes | Int32 | Yes | Response (minutes) | `NumberInt(3)` |  |
| 38 | repairMinutes | Int32 | Yes | Repair (minutes) | `NumberInt(66)` |  |
| 39 | unitsLost | Int32 | Yes | Units lost | `NumberInt(30)` |  |
| 40 | status | String | Yes | Primary lifecycle state of the document | `"Open"` | Open; Classified; Closed |
| 41 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 42 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-16T18:30:00.000+0000")` |  |
| 43 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 45 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-17T01:21:40.000+0000")` |  |
| 46 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 47 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Classified, Closed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_shiftHandoverDowntimeEvent, u_mes_perf_equipmentState, u_mes_perf_downtimeEventComment, u_mes_perf_alarm, u_mes_maint_maintenanceWorkOrder, u_mes_plan_andonEvent.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_downtimeEvent.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_downtimeEvent.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_downtimeEvent.js
