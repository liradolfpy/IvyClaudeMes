# u_mes_perf_equipmentState

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | State intervals per equipment: running, idle, setup, down, starved, blocked |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 31 (24 required, 7 may be null) |
| Estimated volume per year | ~3 million |
| Storage | time-series candidate |

## Structure

Flat entity collection: one document per equipment state, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1204000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EST-2026-000180"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 8 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 10 | stateCode | String | - | Yes | State code | `"Running"` | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| 11 | subStateCode | String | - | No (null allowed) | Sub state code | `"Auto Cycle"` |  |
| 12 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 13 | endedAt | Date | Datetime | No (null allowed) | Date and time when the record was ended. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 14 | durationSec | Int32 | - | Yes | Duration (seconds) | `NumberInt(5400)` |  |
| 15 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 17 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 18 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 19 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 20 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 21 | plcStateCode | String | - | No (null allowed) | PLC state code | `"3"` |  |
| 22 | downtimeEventId | String | - | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `null` | Reference: u_mes_perf_downtimeEvent._id |
| 23 | downtimeEventName | String | - | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `null` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Closed |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 27 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 28 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 29 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 30 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 31 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Open, Closed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ downtimeEventId: 1 }` | No | Look-up of documents by downtime event |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |
| 9 | `{ equipmentId: 1, startedAt: -1 }` | No | State history of one equipment |

## Referenced by

u_mes_perf_downtimeEvent.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_equipmentState.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_equipmentState.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_equipmentState.js
