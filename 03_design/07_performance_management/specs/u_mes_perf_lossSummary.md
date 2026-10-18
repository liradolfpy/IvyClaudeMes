# u_mes_perf_lossSummary

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | Loss Pareto row per line, shift, production date and reason code (downtime, speed and quality losses). |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (32 required, 2 may be null) |
| Estimated volume per year | about 30,000 |
| Storage | standard collection (report table) |

## Structure

Flat entity collection: one document per loss summary, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1325000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LSS-20260915-ASY-01-A-MATL-ASY-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 7 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 8 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 10 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 11 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 12 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 13 | lossCategoryId | String | - | Yes | Reference to u_mes_perf_lossCategory._id | `"1286000000000004"` | Reference: u_mes_perf_lossCategory._id |
| 14 | lossCategoryName | String | - | Yes | Display value of lossCategoryId, copied from u_mes_perf_lossCategory.name | `"Reduced Speed"` |  |
| 15 | reasonCodeId | String | - | Yes | Reference to u_mes_perf_reasonCode._id | `"1203000000000006"` | Reference: u_mes_perf_reasonCode._id |
| 16 | reasonCodeName | String | - | Yes | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Seal feeder jam"` |  |
| 17 | isPlanned | Boolean | - | Yes | Planned loss | `false` |  |
| 18 | occurrenceCount | Int32 | - | Yes | Number of events | `NumberInt(6)` |  |
| 19 | lossMinutes | Int32 | - | Yes | Lost minutes | `NumberInt(14)` |  |
| 20 | lossUnits | Int32 | - | Yes | Lost units | `NumberInt(23)` |  |
| 21 | lossPctOfPlannedTime | Decimal128 | - | Yes | Share of planned production time | `3.3` |  |
| 22 | paretoRank | Int32 | - | Yes | Rank within line, shift and date | `NumberInt(2)` |  |
| 23 | cumulativePct | Decimal128 | - | Yes | Cumulative Pareto percentage | `79.5` |  |
| 24 | maintenanceWorkOrderCount | Int32 | - | Yes | Work orders raised for the reason | `NumberInt(0)` |  |
| 25 | capaCount | Int32 | - | Yes | CAPAs linked | `NumberInt(1)` |  |
| 26 | calculatedAt | Date | Datetime | Yes | Calculation time | `ISODate("2026-09-16T00:15:00.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T00:15:00.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ lossCategoryId: 1 }` | No | Look-up of documents by loss category |
| 7 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_lossSummary.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_lossSummary.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_lossSummary.js
