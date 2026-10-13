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
| Keys | 55 (33 required, 22 may be null) |
| Estimated volume per year | ~120,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per downtime event, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with downtimeEventId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_perf_downtimeEventComment | Child | comment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1205000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DT-2026-000196"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 10 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 12 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 13 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 14 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 15 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 17 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 18 | endedAt | Date | Datetime | No (null allowed) | Date and time when the record was ended. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 19 | durationMinutes | Int32 | - | Yes | Duration (minutes) | `NumberInt(95)` |  |
| 20 | downtimeType | String | - | Yes | Downtime type | `"Unplanned"` | Planned; Unplanned |
| 21 | faultCode | String | - | No (null allowed) | Fault code | `"E4107"` |  |
| 22 | faultText | String | - | No (null allowed) | Fault text | `"E1107 Ejector not returned to home position"` |  |
| 23 | reasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 24 | reasonCodeName | String | - | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 25 | reasonPathText | String | - | No (null allowed) | Reason path text | `"Unplanned > Mechanical > Nutrunner > Socket worn"` |  |
| 26 | actionText | String | - | No (null allowed) | Action text | `"Ejector pin polished and die coat thickness corrected"` |  |
| 27 | isPlanned | Boolean | - | Yes | True when the record is planned | `false` |  |
| 28 | isMicroStop | Boolean | - | Yes | True when the record is micro stop | `false` |  |
| 29 | alarmId | String | - | No (null allowed) | Reference to u_mes_perf_alarm._id | `"1212000000000001"` | Reference: u_mes_perf_alarm._id |
| 30 | alarmName | String | - | No (null allowed) | Display value of alarmId, copied from u_mes_perf_alarm.recordNo | `"ALM-2026-000176"` |  |
| 31 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `"1220000000000001"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 32 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 33 | reportedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | reportedBy | String | - | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 35 | classifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'classified' | `null` | Reference: u_mes_mast_user._id |
| 36 | classifiedBy | String | - | No (null allowed) | Display name of the user in classifiedById, copied from u_mes_mast_user.fullName | `null` |  |
| 37 | classifiedAt | Date | Datetime | No (null allowed) | Date and time when the record was classified. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 38 | responseMinutes | Int32 | - | Yes | Response (minutes) | `NumberInt(3)` |  |
| 39 | repairMinutes | Int32 | - | Yes | Repair (minutes) | `NumberInt(66)` |  |
| 40 | unitsLost | Int32 | - | Yes | Units lost | `NumberInt(30)` |  |
| 41 | captureSource | String | - | Yes | How the start of the downtime was captured | `"Operator Entry"` | Equipment Signal; Operator Entry; Andon |
| 42 | equipmentStateId | String | - | No (null allowed) | Reference to u_mes_perf_equipmentState._id | `"1204000000000001"` | Reference: u_mes_perf_equipmentState._id |
| 43 | equipmentStateName | String | - | No (null allowed) | Display value of equipmentStateId, copied from u_mes_perf_equipmentState.recordNo | `"EST-2026-000180"` |  |
| 44 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `null` | Reference: u_mes_prod_productVariant._id |
| 45 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `null` |  |
| 46 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `null` | Reference: u_mes_qual_capa._id |
| 47 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `null` |  |
| 48 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Classified; Closed |
| 49 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 50 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 51 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 52 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 53 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 54 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 55 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
