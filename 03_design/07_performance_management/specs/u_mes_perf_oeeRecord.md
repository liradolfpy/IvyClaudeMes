# u_mes_perf_oeeRecord

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | OEE per equipment / line and shift: availability, performance, quality with the time and count basis |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 43 (39 required, 4 may be null) |
| Estimated volume per year | ~110,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per OEE record, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with oeeRecordId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_perf_oeeRecordLoss | Child | loss |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1208000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OEE-2026-000141"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 10 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 11 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 12 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 13 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 15 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 17 | periodStartAt | Date | Datetime | Yes | Period start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 18 | periodEndAt | Date | Datetime | Yes | Period end date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T14:51:40.000+0000")` |  |
| 19 | calendarMinutes | Int32 | - | Yes | Calendar (minutes) | `NumberInt(480)` |  |
| 20 | plannedProductionMinutes | Int32 | - | Yes | Shift duration less paid and unpaid breaks | `NumberInt(430)` |  |
| 21 | plannedDowntimeMinutes | Int32 | - | Yes | Planned downtime (minutes) | `NumberInt(50)` |  |
| 22 | unplannedDowntimeMinutes | Int32 | - | Yes | Unplanned downtime (minutes) | `NumberInt(18)` |  |
| 23 | runMinutes | Int32 | - | Yes | Run (minutes) | `NumberInt(412)` |  |
| 24 | idealCycleTimeSec | Decimal128 | - | Yes | Ideal cycle time (seconds) | `95.0` |  |
| 25 | totalCount | Int32 | - | Yes | Total count | `NumberInt(768)` |  |
| 26 | goodCount | Int32 | - | Yes | Good count | `NumberInt(762)` |  |
| 27 | rejectCount | Int32 | - | Yes | Reject count | `NumberInt(3)` |  |
| 28 | reworkCount | Int32 | - | Yes | Rework count | `NumberInt(0)` |  |
| 29 | availabilityPct | Decimal128 | - | Yes | Availability (percent) | `95.8` |  |
| 30 | performancePct | Decimal128 | - | Yes | Performance (percent) | `85.0` |  |
| 31 | qualityPct | Decimal128 | - | Yes | Quality (percent) | `99.2` |  |
| 32 | oeePct | Decimal128 | - | Yes | OEE (percent) | `80.7` |  |
| 33 | teepPct | Decimal128 | - | Yes | TEEP (percent) | `69.3` |  |
| 34 | calculatedAt | Date | Datetime | Yes | Date and time when the record was calculated. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:10.000+0000")` |  |
| 35 | calculationVersion | Int32 | - | Yes | Calculation version | `NumberInt(1)` |  |
| 36 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 37 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 38 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 39 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 40 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 41 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T14:51:40.000+0000")` |  |
| 42 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 43 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 7 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_perf_oeeRecordLoss.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_oeeRecord.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_oeeRecord.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_oeeRecord.js
