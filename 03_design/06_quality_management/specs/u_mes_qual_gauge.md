# u_mes_qual_gauge

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Gauges and measuring instruments: type, range, resolution, calibration interval and due date, status |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 39 (26 required, 13 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per gauge, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1189000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"G-UT-001"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the gauge; used as its display value in other collections | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 6 | gaugeTypeId | String | - | Yes | Reference to u_mes_qual_gaugeType._id | `"1283000000000001"` | Reference: u_mes_qual_gaugeType._id |
| 7 | gaugeTypeName | String | - | Yes | Display value of gaugeTypeId, copied from u_mes_qual_gaugeType.name | `"Ultrasonic Thickness Gauge"` |  |
| 8 | manufacturerId | String | - | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `null` | Reference: u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | - | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `null` |  |
| 10 | model | String | - | Yes | Model of the gauge | `"38DL Plus"` |  |
| 11 | serialNo | String | - | Yes | Serial number | `"UT-21-0457"` |  |
| 12 | rangeMin | Decimal128 | - | Yes | Range (minutes) | `NumberDecimal("1.000")` |  |
| 13 | rangeMax | Decimal128 | - | Yes | Range max | `NumberDecimal("25.000")` |  |
| 14 | rangeUnitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id: range unit of measure | `"1042000000000003"` | Reference: u_mes_mast_unitOfMeasure._id |
| 15 | rangeUnitOfMeasureName | String | - | Yes | Display value of rangeUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Millimetre"` |  |
| 16 | resolution | Decimal128 | - | Yes | Resolution of the gauge | `NumberDecimal("0.010")` |  |
| 17 | accuracy | Decimal128 | - | Yes | Accuracy of the gauge | `NumberDecimal("0.050")` |  |
| 18 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 19 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 20 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 21 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 22 | ownerUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 23 | ownerUserName | String | - | No (null allowed) | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 24 | calibrationIntervalDays | Int32 | - | Yes | Calibration interval (days) | `NumberInt(180)` |  |
| 25 | calibrationSource | String | - | Yes | Calibration source | `"Internal"` | Internal; External |
| 26 | calibrationSupplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id: calibration supplier | `"1038000000000004"` | Reference: u_mes_mast_supplier._id |
| 27 | calibrationSupplierName | String | - | No (null allowed) | Display value of calibrationSupplierId, copied from u_mes_mast_supplier.name | `"Western Aluminium Alloys Ltd."` |  |
| 28 | lastCalibratedAt | Date | Datetime | No (null allowed) | Last calibrated date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-05-06T00:00:00.000+0000")` |  |
| 29 | nextCalibrationDueAt | Date | Date | Yes | Next calibration due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-11-06T00:00:00.000+0000")` |  |
| 30 | lastGaugeCalibrationId | String | - | No (null allowed) | Reference to u_mes_qual_gaugeCalibration._id: last gauge calibration | `"1190000000000001"` | Reference: u_mes_qual_gaugeCalibration._id |
| 31 | lastGaugeCalibrationName | String | - | No (null allowed) | Display value of lastGaugeCalibrationId, copied from u_mes_qual_gaugeCalibration.recordNo | `"GCAL-G-UT-001-2026-01"` |  |
| 32 | usageCount | Int32 | - | Yes | Usage count | `NumberInt(1840)` |  |
| 33 | purchasedAt | Date | Datetime | Yes | Date and time when the record was purchased. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2019-01-04T00:00:00.000+0000")` |  |
| 34 | isMasterGauge | Boolean | - | Yes | True when the record is master gauge | `false` |  |
| 35 | blockedForUse | Boolean | - | Yes | True when: blocked for use | `false` |  |
| 36 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `null` | Reference: u_mes_mast_equipment._id |
| 37 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 38 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Due For Calibration; Overdue; Under Calibration; Blocked; Retired |
| 39 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Due For Calibration, Overdue, Under Calibration, Blocked, Retired. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_qual_characteristic, u_mes_qual_controlPlanLine, u_mes_qual_inspectionPlanLine, u_mes_qual_inspectionResult, u_mes_qual_gaugeCalibration, u_mes_qual_msaStudy.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_gauge.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_gauge.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_gauge.js
