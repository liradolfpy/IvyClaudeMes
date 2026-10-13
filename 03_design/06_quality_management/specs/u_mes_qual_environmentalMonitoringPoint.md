# u_mes_qual_environmentalMonitoringPoint

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | A monitored location and parameter in a controlled area, with its alert and action limits and sampling frequency. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 20 (14 required, 6 may be null) |
| Estimated volume per year | about 120 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per environmental monitoring point, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1357000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EMP-ASY-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Monitoring point name | `"Assembly clean area, airborne particles 0.5 um"` |  |
| 6 | areaId | String | - | Yes | Reference to u_mes_mast_area._id | `"1005000000000005"` | Reference: u_mes_mast_area._id |
| 7 | areaName | String | - | Yes | Display value of areaId, copied from u_mes_mast_area.name | `"Assembly and Test"` |  |
| 8 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 10 | monitoredParameter | String | - | Yes | Parameter monitored | `"Airborne Particles 0.5 um"` | Temperature; Relative Humidity; Differential Pressure; Airborne Particles 0.5 um; Airborne Particles 5.0 um; Surface Particle Count; Illuminance |
| 11 | parameterUnitText | String | - | Yes | Unit of the parameter as shown on the instrument | `"particles per m3"` |  |
| 12 | limitDirection | String | - | Yes | Which side of the limits is an excursion | `"Upper"` | Upper; Lower; Range |
| 13 | alertLimit | Decimal128 | - | No (null allowed) | Alert limit (upper, or lower for a Lower direction) | `NumberDecimal("2800000")` |  |
| 14 | actionLimit | Decimal128 | - | Yes | Action limit (upper, or lower for a Lower direction) | `NumberDecimal("3520000")` |  |
| 15 | lowerActionLimit | Decimal128 | - | No (null allowed) | Lower action limit for a Range direction | `null` |  |
| 16 | samplingFrequency | String | - | Yes | How often the point is sampled | `"Weekly"` | Continuous; Every Shift; Daily; Weekly |
| 17 | processTagId | String | - | No (null allowed) | Reference to u_mes_perf_processTag._id | `null` | Reference: u_mes_perf_processTag._id |
| 18 | processTagName | String | - | No (null allowed) | Display value of processTagId, copied from u_mes_perf_processTag.description | `null` |  |
| 19 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ processTagId: 1 }` | No | Look-up of documents by process tag |

## Referenced by

u_mes_qual_environmentalMonitoringResult.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_environmentalMonitoringPoint.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_environmentalMonitoringPoint.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_environmentalMonitoringPoint.js
