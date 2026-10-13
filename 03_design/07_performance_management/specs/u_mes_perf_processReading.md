# u_mes_perf_processReading

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Tag values over time (die temperature, furnace zone temperature, spindle load, bath pH, current) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 30 (20 required, 10 may be null) |
| Estimated volume per year | ~2 billion raw, down-sampled |
| Storage | time-series (recommended) |

## Structure

Flat entity collection: one document per process reading, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1211000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PD-2026-000356"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | processTagId | String | - | Yes | Reference to u_mes_perf_processTag._id | `"1210000000000001"` | Reference: u_mes_perf_processTag._id |
| 7 | processTagName | String | - | Yes | Display value of processTagId, copied from u_mes_perf_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 8 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 9 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 10 | timestamp | Date | Datetime | Yes | Timestamp. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 11 | tagValue | Double | - | Yes | Numeric value of the tag at the timestamp | `Double(401.6)` |  |
| 12 | tagValueText | String | - | No (null allowed) | Tag value text | `null` |  |
| 13 | signalQuality | String | - | Yes | Signal quality | `"Good"` | Good; Uncertain; Bad |
| 14 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 16 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 17 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 18 | inLimits | Boolean | - | Yes | True when: in limits | `true` |  |
| 19 | areaId | String | - | No (null allowed) | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 20 | areaName | String | - | No (null allowed) | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 21 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 22 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 23 | productionDate | Date | Date | No (null allowed) | Production date of the reading | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 25 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 26 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 27 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 28 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 29 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 30 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ processTagId: 1 }` | No | Look-up of documents by process tag |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 7 | `{ siteId: 1, timestamp: -1 }` | No | Time-ordered lists and reports by timestamp |
| 8 | `{ processTagId: 1, timestamp: -1 }` | No | Trend of one tag over time |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_processReading.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_processReading.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_processReading.js
