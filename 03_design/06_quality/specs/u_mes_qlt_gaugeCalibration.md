# u_mes_qlt_gaugeCalibration

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Calibration events: as-found / as-left readings, standard used, result, certificate |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | GCAL-<recordNo> |
| Display value used by references | recordNo |
| Keys | 35 (30 required, 5 may be null) |
| Estimated volume per year | ~3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per gauge calibration, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with gaugeCalibrationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_gaugeCalibrationReading | Child | reading |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: GCAL-<recordNo> | `"GCAL-G-BG-054-2026-02"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"G-BG-054-2026-02"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | gaugeId | String | Yes | Reference to u_mes_qlt_gauge._id | `"GAU-G-BG-054"` | Reference: u_mes_qlt_gauge._id |
| 6 | gaugeName | String | Yes | Display value of gaugeId, copied from u_mes_qlt_gauge.name | `"Bore gauge 50-75 mm"` |  |
| 7 | calibrationType | String | Yes | Calibration type | `"Periodic"` | Initial; Periodic; After Repair; After Shock Or Damage |
| 8 | calibratedAt | Date | Yes | Date and time when the record was calibrated | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 9 | calibratedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'calibrated' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 10 | calibratedBy | String | Yes | Display name of the user in calibratedById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 11 | calibrationSupplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id: calibration supplier | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 12 | calibrationSupplierName | String | No (null allowed) | Display value of calibrationSupplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 13 | masterStandardRef | String | Yes | Master standard ref | `"Setting ring 54.000 mm, cert NABL-CC-2231"` |  |
| 14 | traceability | String | Yes | Traceability of the gauge calibration | `"NABL accredited laboratory, traceable to NPL India"` |  |
| 15 | temperatureC | Decimal128 | Yes | Temperature c | `NumberDecimal("20.1")` |  |
| 16 | humidityPct | Decimal128 | Yes | Humidity (percent) | `NumberDecimal("48.0")` |  |
| 17 | asFoundResult | String | Yes | As found result | `"Within Tolerance"` | Within Tolerance; Out Of Tolerance |
| 18 | asLeftResult | String | Yes | As left result | `"Within Tolerance"` | Within Tolerance; Out Of Tolerance |
| 19 | overallResult | String | Yes | Overall result | `"Pass"` | Pass; Fail |
| 20 | uncertainty | Decimal128 | Yes | Uncertainty of the gauge calibration | `NumberDecimal("0.0012")` |  |
| 21 | adjustmentMade | Boolean | Yes | True when: adjustment made | `false` |  |
| 22 | certificateNo | String | Yes | Certificate number | `"IATF-0412877"` |  |
| 23 | certificateControlledDocumentId | String | No (null allowed) | Reference to u_mes_sys_controlledDocument._id: certificate controlled document | `"DOC-CRT-KPP-260914-07"` | Reference: u_mes_sys_controlledDocument._id |
| 24 | certificateControlledDocumentName | String | No (null allowed) | Display value of certificateControlledDocumentId, copied from u_mes_sys_controlledDocument.title | `"Material certificate, piston lot KPP-260914-07"` |  |
| 25 | nextDueAt | Date | Yes | Next due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 26 | impactAssessmentRequired | Boolean | Yes | True when: impact assessment required | `false` |  |
| 27 | remarks | String | No (null allowed) | Remarks of the gauge calibration | `"No abnormality observed"` |  |
| 28 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Planned; Completed; Failed |
| 29 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 31 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 32 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 33 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 34 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 35 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Planned, Completed, Failed. Initial state: Planned. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_qlt_gauge, u_mes_qlt_gaugeCalibrationReading.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_gaugeCalibration.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_gaugeCalibration.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_gaugeCalibration.js
