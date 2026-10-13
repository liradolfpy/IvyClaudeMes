# u_mes_perf_operatorPerformance

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Labour efficiency per operator, station, variant, shift and date. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 30 (28 required, 2 may be null) |
| Estimated volume per year | about 40,000 |
| Storage | standard collection (report table) |

## Structure

Flat entity collection: one document per operator performance, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1327000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OPF-20260915-10344-ASY-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 7 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 8 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 10 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 12 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 13 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 14 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 15 | attendedMinutes | Decimal128 | - | Yes | Minutes logged in | `NumberDecimal("455")` |  |
| 16 | earnedMinutes | Decimal128 | - | Yes | Standard minutes earned | `NumberDecimal("421")` |  |
| 17 | efficiencyPct | Decimal128 | - | Yes | Earned / attended | `NumberDecimal("92.5")` |  |
| 18 | goodQuantity | Int32 | - | Yes | Good units | `NumberInt(742)` |  |
| 19 | rejectQuantity | Int32 | - | Yes | Rejected units | `NumberInt(2)` |  |
| 20 | errorCount | Int32 | - | Yes | Defects with 4M category Man | `NumberInt(0)` |  |
| 21 | interlockCount | Int32 | - | Yes | Interlocks triggered | `NumberInt(1)` |  |
| 22 | calculatedAt | Date | Datetime | Yes | Calculation time | `ISODate("2026-09-16T00:20:00.000+0000")` |  |
| 23 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 25 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 26 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 27 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 28 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T00:20:00.000+0000")` |  |
| 29 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ userId: 1 }` | No | Look-up of documents by user |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_operatorPerformance.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_operatorPerformance.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_operatorPerformance.js
