# u_mes_qual_environmentalMonitoringResult

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | One environmental monitoring result with its evaluation against alert and action limits and the excursion handling. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 25 (20 required, 5 may be null) |
| Estimated volume per year | about 30,000 per year |
| Storage | standard collection (continuous points stay in processReading) |

## Structure

Flat entity collection: one document per environmental monitoring result, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1358000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EMR-20260915-0004"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | environmentalMonitoringPointId | String | - | Yes | Reference to u_mes_qual_environmentalMonitoringPoint._id | `"1357000000000001"` | Reference: u_mes_qual_environmentalMonitoringPoint._id |
| 7 | environmentalMonitoringPointName | String | - | Yes | Display value of environmentalMonitoringPointId, copied from u_mes_qual_environmentalMonitoringPoint.name | `"Dispensing booth, airborne particles 0.5 um"` |  |
| 8 | sampledAt | Date | Datetime | Yes | Sampling time | `ISODate("2026-09-15T07:10:00.000+0000")` |  |
| 9 | measuredValue | Decimal128 | - | Yes | Measured value | `1840000` |  |
| 10 | limitEvaluation | String | - | Yes | Evaluation against the limits | `"Within Limits"` | Within Limits; Alert Limit Exceeded; Action Limit Exceeded |
| 11 | sampledById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'sampled' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 12 | sampledBy | String | - | Yes | Display name of the user in sampledById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 13 | gaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id | `null` | Reference: u_mes_qual_gauge._id |
| 14 | gaugeName | String | - | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `null` |  |
| 15 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 16 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 17 | productImpactText | String | - | No (null allowed) | Assessment of the impact on product made during the excursion | `null` |  |
| 18 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Excursion Open; Excursion Closed; Invalidated |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 20 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:00.000+0000")` |  |
| 21 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 22 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 23 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:00.000+0000")` |  |
| 24 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 25 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Status values

Recorded, Excursion Open, Excursion Closed, Invalidated. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ environmentalMonitoringPointId: 1 }` | No | Look-up of documents by environmental monitoring point |
| 4 | `{ gaugeId: 1 }` | No | Look-up of documents by gauge |
| 5 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 6 | `{ siteId: 1, sampledAt: -1 }` | No | Time-ordered lists and reports by sampled at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_environmentalMonitoringResult.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_environmentalMonitoringResult.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_environmentalMonitoringResult.js
