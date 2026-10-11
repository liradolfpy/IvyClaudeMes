# u_mes_eqp_oeeRecord

| Property | Value |
|---|---|
| Module | Equipment and performance (eqp) |
| Purpose | OEE per equipment / line and shift: availability, performance, quality with the time and count basis |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | OEE-<recordNo> |
| Display value used by references | recordNo |
| Keys | 42 (38 required, 4 may be null) |
| Estimated volume per year | ~110,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per OEE record, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with oeeRecordId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_eqp_oeeRecordLoss | Child | loss |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: OEE-<recordNo> | `"OEE-20260929-A-TRQ-01-NR1"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-A-TRQ-01-NR1"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 9 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 10 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 11 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 12 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 13 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_exe_productionOrder._id | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 16 | periodStartAt | Date | Yes | Period start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 17 | periodEndAt | Date | Yes | Period end date and time | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 18 | calendarMinutes | Int32 | Yes | Calendar (minutes) | `NumberInt(480)` |  |
| 19 | plannedProductionMinutes | Int32 | Yes | Shift duration less paid and unpaid breaks | `NumberInt(430)` |  |
| 20 | plannedDowntimeMinutes | Int32 | Yes | Planned downtime (minutes) | `NumberInt(50)` |  |
| 21 | unplannedDowntimeMinutes | Int32 | Yes | Unplanned downtime (minutes) | `NumberInt(18)` |  |
| 22 | runMinutes | Int32 | Yes | Run (minutes) | `NumberInt(412)` |  |
| 23 | idealCycleTimeSec | Decimal128 | Yes | Ideal cycle time (seconds) | `NumberDecimal("32.0")` |  |
| 24 | totalCount | Int32 | Yes | Total count | `NumberInt(768)` |  |
| 25 | goodCount | Int32 | Yes | Good count | `NumberInt(762)` |  |
| 26 | rejectCount | Int32 | Yes | Reject count | `NumberInt(3)` |  |
| 27 | reworkCount | Int32 | Yes | Rework count | `NumberInt(0)` |  |
| 28 | availabilityPct | Decimal128 | Yes | Availability (percent) | `NumberDecimal("95.8")` |  |
| 29 | performancePct | Decimal128 | Yes | Performance (percent) | `NumberDecimal("85.0")` |  |
| 30 | qualityPct | Decimal128 | Yes | Quality (percent) | `NumberDecimal("99.2")` |  |
| 31 | oeePct | Decimal128 | Yes | OEE (percent) | `NumberDecimal("80.7")` |  |
| 32 | teepPct | Decimal128 | Yes | TEEP (percent) | `NumberDecimal("69.3")` |  |
| 33 | calculatedAt | Date | Yes | Date and time when the record was calculated | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 34 | calculationVersion | Int32 | Yes | Calculation version | `NumberInt(1)` |  |
| 35 | status | String | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 36 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 38 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 39 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"MES System"` |  |
| 40 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 41 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 42 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"MES System"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_eqp_oeeRecordLoss.

## Files

- Validator: 03_design/07_equipment_performance/validators/u_mes_eqp_oeeRecord.json
- Indexes: 03_design/07_equipment_performance/indexes/u_mes_eqp_oeeRecord.js
- Sample document: 03_design/07_equipment_performance/samples/u_mes_eqp_oeeRecord.js
