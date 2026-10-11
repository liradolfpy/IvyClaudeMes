# u_mes_perf_equipmentState

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | State intervals per equipment: running, idle, setup, down, starved, blocked |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | EST-<recordNo> |
| Display value used by references | recordNo |
| Keys | 30 (23 required, 7 may be null) |
| Estimated volume per year | ~3 million |
| Storage | time-series candidate |

## Structure

Flat entity collection: one document per equipment state, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: EST-<recordNo> | `"EST-20260929-000077"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000077"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 7 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 9 | stateCode | String | Yes | State code | `"Running"` | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| 10 | subStateCode | String | No (null allowed) | Sub state code | `"Auto Cycle"` |  |
| 11 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | endedAt | Date | No (null allowed) | Date and time when the record was ended | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 13 | durationSec | Int32 | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 16 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 17 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 18 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 19 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 20 | plcStateCode | String | No (null allowed) | PLC state code | `"3"` |  |
| 21 | downtimeEventId | String | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"DT-20260929-0009"` | Reference: u_mes_perf_downtimeEvent._id |
| 22 | downtimeEventName | String | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"20260929-0009"` |  |
| 23 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Open; Closed |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 25 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 26 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 27 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 28 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 29 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 30 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_equipmentState.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_equipmentState.js
- Sample document: 03_design/07_performance_management/samples/u_mes_perf_equipmentState.js
