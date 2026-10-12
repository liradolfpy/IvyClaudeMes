# u_mes_qual_gaugeCalibration

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Calibration events: as-found / as-left readings, standard used, result, certificate |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 35 (30 required, 5 may be null) |
| Estimated volume per year | ~3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per gauge calibration, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with gaugeCalibrationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_gaugeCalibrationReading | Child | reading |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1190000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GCAL-G-UT-001-2026-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | gaugeId | String | - | Yes | Reference to u_mes_qual_gauge._id | `"1189000000000001"` | Reference: u_mes_qual_gauge._id |
| 6 | gaugeName | String | - | Yes | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 7 | calibrationType | String | - | Yes | Calibration type | `"Periodic"` | Initial; Periodic; After Repair; After Shock Or Damage; Automatic Closed Loop |
| 8 | calibratedAt | Date | Datetime | Yes | Date and time when the record was calibrated. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 9 | calibratedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'calibrated' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 10 | calibratedBy | String | - | Yes | Display name of the user in calibratedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | calibrationSupplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id: calibration supplier | `"1038000000000004"` | Reference: u_mes_mast_supplier._id |
| 12 | calibrationSupplierName | String | - | No (null allowed) | Display value of calibrationSupplierId, copied from u_mes_mast_supplier.name | `"Western Aluminium Alloys Ltd."` |  |
| 13 | masterStandardRef | String | - | Yes | Master standard ref | `"Setting ring 54.000 mm, cert NABL-CC-2231"` |  |
| 14 | traceability | String | - | Yes | Traceability of the gauge calibration | `"NABL accredited laboratory, traceable to NPL India"` |  |
| 15 | temperatureC | Decimal128 | - | Yes | Temperature c | `NumberDecimal("20.1")` |  |
| 16 | humidityPct | Decimal128 | - | Yes | Humidity (percent) | `NumberDecimal("48.0")` |  |
| 17 | asFoundResult | String | - | Yes | As found result | `"Within Tolerance"` | Within Tolerance; Out Of Tolerance |
| 18 | asLeftResult | String | - | Yes | As left result | `"Within Tolerance"` | Within Tolerance; Out Of Tolerance |
| 19 | overallResult | String | - | Yes | Overall result | `"Pass"` | Pass; Fail |
| 20 | uncertainty | Decimal128 | - | Yes | Uncertainty of the gauge calibration | `NumberDecimal("0.0012")` |  |
| 21 | adjustmentMade | Boolean | - | Yes | True when: adjustment made | `false` |  |
| 22 | certificateNo | String | - | Yes | Certificate number | `"IATF-0412877"` |  |
| 23 | certificateControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: certificate controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 24 | certificateControlledDocumentName | String | - | No (null allowed) | Display value of certificateControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 25 | nextDueAt | Date | Date | Yes | Next due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 26 | impactAssessmentRequired | Boolean | - | Yes | True when: impact assessment required | `false` |  |
| 27 | remarks | String | - | No (null allowed) | Remarks of the gauge calibration | `"No abnormality observed"` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; Completed; Failed |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 31 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 33 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 34 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Planned, Completed, Failed. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ gaugeId: 1 }` | No | Look-up of documents by gauge |
| 4 | `{ calibrationSupplierId: 1 }` | No | Look-up of documents by calibration supplier |
| 5 | `{ certificateControlledDocumentId: 1 }` | No | Look-up of documents by certificate controlled document |
| 6 | `{ siteId: 1, calibratedAt: -1 }` | No | Time-ordered lists and reports by calibrated at |

## Referenced by

u_mes_qual_gauge, u_mes_qual_gaugeCalibrationReading.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_gaugeCalibration.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_gaugeCalibration.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_gaugeCalibration.js
