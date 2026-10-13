# u_mes_qual_gaugeCalibrationReading

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per reading of a gauge calibration |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_gaugeCalibration |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (20 required, 0 may be null) |

## Structure

Child collection. The parent gauge calibration can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. gaugeCalibrationId and gaugeCalibrationName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1191000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GCAL-G-UT-001-2026-01-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | gaugeCalibrationId | String | - | Yes | Reference to u_mes_qual_gaugeCalibration._id: the parent document this one belongs to | `"1190000000000001"` | Reference: u_mes_qual_gaugeCalibration._id |
| 7 | gaugeCalibrationName | String | - | Yes | Display value of gaugeCalibrationId, copied from u_mes_qual_gaugeCalibration.recordNo | `"GCAL-G-UT-001-2026-01"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | nominal | Decimal128 | - | Yes | Nominal of the gauge calibration reading | `NumberDecimal("8.00")` |  |
| 10 | asFound | Decimal128 | - | Yes | As found | `NumberDecimal("54.001")` |  |
| 11 | asLeft | Decimal128 | - | Yes | As left | `NumberDecimal("54.000")` |  |
| 12 | tolerance | Decimal128 | - | Yes | Tolerance of the gauge calibration reading | `NumberDecimal("0.002")` |  |
| 13 | withinTolerance | Boolean | - | Yes | True when: within tolerance | `true` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 16 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 18 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 19 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ gaugeCalibrationId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_gaugeCalibrationReading.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_gaugeCalibrationReading.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_gaugeCalibrationReading.js
