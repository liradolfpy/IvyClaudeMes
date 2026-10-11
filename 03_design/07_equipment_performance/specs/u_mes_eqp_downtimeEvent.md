# u_mes_eqp_downtimeEvent

| Property | Value |
|---|---|
| Module | Equipment and performance (eqp) |
| Purpose | Classified stops with fault, reason path, action taken, duration, responsible group |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | DT-<recordNo> |
| Display value used by references | recordNo |
| Keys | 47 (31 required, 16 may be null) |
| Estimated volume per year | ~120,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per downtime event, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with downtimeEventId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_eqp_downtimeEventComment | Child | comment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DT-<recordNo> | `"DT-20260929-0009"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0009"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 9 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 10 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 11 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 12 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 13 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_exe_productionOrder._id | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 16 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 17 | endedAt | Date | No (null allowed) | Date and time when the record was ended | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 18 | durationMinutes | Int32 | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 19 | downtimeType | String | Yes | Downtime type | `"Unplanned"` | Planned; Unplanned |
| 20 | faultCode | String | No (null allowed) | Fault code | `"E4107"` |  |
| 21 | faultText | String | No (null allowed) | Fault text | `"Rundown torque not reached, spindle 1"` |  |
| 22 | reasonCodeId | String | No (null allowed) | Reference to u_mes_eqp_reasonCode._id | `"RSN-MECH-NR-02"` | Reference: u_mes_eqp_reasonCode._id |
| 23 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_eqp_reasonCode.name | `"Nutrunner socket worn"` |  |
| 24 | reasonPathText | String | No (null allowed) | Reason path text | `"Unplanned > Mechanical > Nutrunner > Socket worn"` |  |
| 25 | actionText | String | No (null allowed) | Action text | `"Socket replaced and verified with torque analyser"` |  |
| 26 | isPlanned | Boolean | Yes | True when the record is planned | `false` |  |
| 27 | isMicroStop | Boolean | Yes | True when the record is micro stop | `false` |  |
| 28 | alarmId | String | No (null allowed) | Reference to u_mes_eqp_alarm._id | `"ALM-20260929-000031"` | Reference: u_mes_eqp_alarm._id |
| 29 | alarmName | String | No (null allowed) | Display value of alarmId, copied from u_mes_eqp_alarm.recordNo | `"20260929-000031"` |  |
| 30 | maintenanceWorkOrderId | String | No (null allowed) | Reference to u_mes_mnt_maintenanceWorkOrder._id | `"MWO-2026-000341"` | Reference: u_mes_mnt_maintenanceWorkOrder._id |
| 31 | maintenanceWorkOrderName | String | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_mnt_maintenanceWorkOrder.title | `"Nutrunner rundown fault, station 1"` |  |
| 32 | reportedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'reported' | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 33 | reportedBy | String | Yes | Display name of the user in reportedById, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 34 | classifiedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'classified' | `"USR-10045"` | Reference: u_mes_mdm_user._id |
| 35 | classifiedBy | String | No (null allowed) | Display name of the user in classifiedById, copied from u_mes_mdm_user.fullName | `"Rajesh Patil"` |  |
| 36 | classifiedAt | Date | No (null allowed) | Date and time when the record was classified | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 37 | responseMinutes | Int32 | Yes | Response (minutes) | `NumberInt(6)` |  |
| 38 | repairMinutes | Int32 | Yes | Repair (minutes) | `NumberInt(12)` |  |
| 39 | unitsLost | Int32 | Yes | Units lost | `NumberInt(30)` |  |
| 40 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Open; Classified; Closed |
| 41 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 42 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 43 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 44 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 45 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 46 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 47 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Classified, Closed. Initial state: Open. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_exe_shiftHandoverDowntimeEvent, u_mes_eqp_equipmentState, u_mes_eqp_downtimeEventComment, u_mes_eqp_alarm, u_mes_mnt_maintenanceWorkOrder, u_mes_ehs_andonEvent.

## Files

- Validator: 03_design/07_equipment_performance/validators/u_mes_eqp_downtimeEvent.json
- Indexes: 03_design/07_equipment_performance/indexes/u_mes_eqp_downtimeEvent.js
- Sample document: 03_design/07_equipment_performance/samples/u_mes_eqp_downtimeEvent.js
