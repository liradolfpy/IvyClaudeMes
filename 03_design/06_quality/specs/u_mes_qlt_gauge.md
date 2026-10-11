# u_mes_qlt_gauge

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Gauges and measuring instruments: type, range, resolution, calibration interval and due date, status |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | GAU-<recordNo> |
| Display value used by references | name |
| Keys | 37 (26 required, 11 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per gauge, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: GAU-<recordNo> | `"GAU-G-BG-054"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"G-BG-054"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the gauge; used as its display value in other collections | `"Bore gauge 50-75 mm"` |  |
| 6 | gaugeTypeId | String | Yes | Reference to u_mes_qlt_gaugeType._id | `"GTY-BORE-GAUGE"` | Reference: u_mes_qlt_gaugeType._id |
| 7 | gaugeTypeName | String | Yes | Display value of gaugeTypeId, copied from u_mes_qlt_gaugeType.name | `"Bore Gauge"` |  |
| 8 | manufacturerId | String | No (null allowed) | Reference to u_mes_mdm_manufacturer._id | `"MFR-ATLAS-COPCO"` | Reference: u_mes_mdm_manufacturer._id |
| 9 | manufacturerName | String | No (null allowed) | Display value of manufacturerId, copied from u_mes_mdm_manufacturer.name | `"Atlas Copco"` |  |
| 10 | model | String | Yes | Model of the gauge | `"PF6000 with ETV STR61"` |  |
| 11 | serialNo | String | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 12 | rangeMin | Decimal128 | Yes | Range (minutes) | `NumberDecimal("50.000")` |  |
| 13 | rangeMax | Decimal128 | Yes | Range max | `NumberDecimal("75.000")` |  |
| 14 | rangeUnitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id: range unit of measure | `"UOM-MM"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 15 | rangeUnitOfMeasureName | String | Yes | Display value of rangeUnitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Millimetre"` |  |
| 16 | resolution | Decimal128 | Yes | Resolution of the gauge | `NumberDecimal("0.001")` |  |
| 17 | accuracy | Decimal128 | Yes | Accuracy of the gauge | `NumberDecimal("0.002")` |  |
| 18 | storageLocationId | String | Yes | Reference to u_mes_mat_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 19 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 20 | workCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 21 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 22 | ownerUserId | String | No (null allowed) | Reference to u_mes_mdm_user._id: owner user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 23 | ownerUserName | String | No (null allowed) | Display value of ownerUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 24 | calibrationIntervalDays | Int32 | Yes | Calibration interval (days) | `NumberInt(180)` |  |
| 25 | calibrationSource | String | Yes | Calibration source | `"External"` | Internal; External |
| 26 | calibrationSupplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id: calibration supplier | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 27 | calibrationSupplierName | String | No (null allowed) | Display value of calibrationSupplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 28 | lastCalibratedAt | Date | No (null allowed) | Last calibrated date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 29 | nextCalibrationDueAt | Date | Yes | Next calibration due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 30 | lastGaugeCalibrationId | String | No (null allowed) | Reference to u_mes_qlt_gaugeCalibration._id: last gauge calibration | `"GCAL-G-BG-054-2026-02"` | Reference: u_mes_qlt_gaugeCalibration._id |
| 31 | lastGaugeCalibrationName | String | No (null allowed) | Display value of lastGaugeCalibrationId, copied from u_mes_qlt_gaugeCalibration.recordNo | `"G-BG-054-2026-02"` |  |
| 32 | usageCount | Int32 | Yes | Usage count | `NumberInt(1840)` |  |
| 33 | purchasedAt | Date | Yes | Date and time when the record was purchased | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 34 | isMasterGauge | Boolean | Yes | True when the record is master gauge | `false` |  |
| 35 | blockedForUse | Boolean | Yes | True when: blocked for use | `false` |  |
| 36 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Due For Calibration; Overdue; Under Calibration; Blocked; Retired |
| 37 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Due For Calibration, Overdue, Under Calibration, Blocked, Retired. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ gaugeTypeId: 1 }` | No | Look-up of documents by gauge type |
| 4 | `{ manufacturerId: 1 }` | No | Look-up of documents by manufacturer |
| 5 | `{ rangeUnitOfMeasureId: 1 }` | No | Look-up of documents by range unit of measure |
| 6 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 7 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |

## Referenced by

u_mes_qlt_characteristic, u_mes_qlt_controlPlanLine, u_mes_qlt_inspectionPlanLine, u_mes_qlt_inspectionResult, u_mes_qlt_gaugeCalibration, u_mes_qlt_msaStudy.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_gauge.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_gauge.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_gauge.js
