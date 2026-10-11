# u_mes_qual_spcSample

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Subgroups with readings, mean, range, rule violations and reaction |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 36 (32 required, 4 may be null) |
| Estimated volume per year | ~900,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per SPC sample, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with spcSampleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_spcSampleReading | Value list | reading |
| u_mes_qual_spcSampleInspectionResult | Relationship | inspection result |
| u_mes_qual_spcSampleViolation | Child | violation |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1154000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SPS-2026-000253"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | spcChartId | String | Yes | Reference to u_mes_qual_spcChart._id | `"1151000000000001"` | Reference: u_mes_qual_spcChart._id |
| 6 | spcChartName | String | Yes | Display value of spcChartId, copied from u_mes_qual_spcChart.name | `"Casting wall thickness at bridge, X-bar R chart"` |  |
| 7 | characteristicId | String | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 8 | characteristicName | String | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 9 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 10 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 11 | subgroupNo | Int32 | Yes | Subgroup number | `NumberInt(147)` |  |
| 12 | sampledAt | Date | Yes | Date and time when the record was sampled | `ISODate("2026-09-15T00:30:30.000+0000")` |  |
| 13 | sampledById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'sampled' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 14 | sampledBy | String | Yes | Display name of the user in sampledById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 15 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 16 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 17 | subgroupMean | Decimal128 | Yes | Subgroup mean | `NumberDecimal("8.03")` |  |
| 18 | subgroupRange | Decimal128 | Yes | Subgroup range | `NumberDecimal("0.14")` |  |
| 19 | stdDev | Decimal128 | Yes | Std dev | `NumberDecimal("0.0600")` |  |
| 20 | ucl | Decimal128 | Yes | Upper control limit | `NumberDecimal("8.20")` |  |
| 21 | lcl | Decimal128 | Yes | Lower control limit | `NumberDecimal("7.84")` |  |
| 22 | centerLine | Decimal128 | Yes | Center line | `NumberDecimal("8.02")` |  |
| 23 | inControl | Boolean | Yes | True when: in control | `true` |  |
| 24 | assignableCause | String | No (null allowed) | Assignable cause | `null` |  |
| 25 | correctiveAction | String | No (null allowed) | Corrective action | `"Ejector pin polished and die coat thickness corrected"` |  |
| 26 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 27 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 28 | excludedFromLimits | Boolean | Yes | True when: excluded from limits | `false` |  |
| 29 | status | String | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Under Investigation; Closed |
| 30 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 32 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 34 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:30.000+0000")` |  |
| 35 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Recorded, Under Investigation, Closed. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ spcChartId: 1 }` | No | Look-up of documents by SPC chart |
| 4 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 8 | `{ siteId: 1, sampledAt: -1 }` | No | Time-ordered lists and reports by sampled at |

## Referenced by

u_mes_qual_spcSampleReading, u_mes_qual_spcSampleInspectionResult, u_mes_qual_spcSampleViolation.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_spcSample.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_spcSample.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_spcSample.js
