# u_mes_perf_workCenterPerformance

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Hourly station performance: throughput, cycle time against takt, WIP, blocked and starved time and constraint flag. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (32 required, 2 may be null) |
| Estimated volume per year | about 90,000 |
| Storage | standard collection (report table) |

## Structure

Flat entity collection: one document per work center performance, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1326000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WCP-2026091506-ASY-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 7 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 9 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 10 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 11 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 12 | periodStartAt | Date | Datetime | Yes | Hour start | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 13 | periodEndAt | Date | Datetime | Yes | Hour end | `ISODate("2026-09-15T07:00:00.000+0000")` |  |
| 14 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 15 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 16 | unitsCompleted | Int32 | - | Yes | Units completed | `NumberInt(98)` |  |
| 17 | throughputPerHour | Decimal128 | - | Yes | Throughput | `NumberDecimal("98")` |  |
| 18 | averageCycleTimeSec | Decimal128 | - | Yes | Average actual cycle time | `NumberDecimal("33.9")` |  |
| 19 | taktTimeSec | Decimal128 | - | Yes | Takt time | `NumberDecimal("36.0")` |  |
| 20 | taktBreachCount | Int32 | - | Yes | Cycles above takt | `NumberInt(6)` |  |
| 21 | wipQuantity | Int32 | - | Yes | WIP in front of the station at hour end | `NumberInt(4)` |  |
| 22 | blockedMinutes | Decimal128 | - | Yes | Minutes blocked by downstream | `NumberDecimal("2.5")` |  |
| 23 | starvedMinutes | Decimal128 | - | Yes | Minutes starved by upstream | `NumberDecimal("0.0")` |  |
| 24 | isConstraint | Boolean | - | Yes | Active constraint in the hour | `false` |  |
| 25 | rankInLine | Int32 | - | Yes | Rank by throughput within the line (1 = slowest) | `NumberInt(3)` |  |
| 26 | calculatedAt | Date | Datetime | Yes | Calculation time | `ISODate("2026-09-15T07:05:00.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:05:00.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 7 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_workCenterPerformance.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_workCenterPerformance.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_workCenterPerformance.js
