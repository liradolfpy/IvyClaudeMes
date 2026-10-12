# u_mes_qual_measurementCurve

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One captured curve per unit, position and test, with the envelope verdict and summary values. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 38 (25 required, 13 may be null) |
| Estimated volume per year | about 600,000 |
| Storage | standard collection, archive after 1 year |

## Structure

Flat entity collection: one document per measurement curve, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1319000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CRV-20260915-01840"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | curveEnvelopeId | String | - | Yes | Reference to u_mes_qual_curveEnvelope._id | `"1317000000000001"` | Reference: u_mes_qual_curveEnvelope._id |
| 6 | curveEnvelopeName | String | - | Yes | Display value of curveEnvelopeId, copied from u_mes_qual_curveEnvelope.name | `"Piston press-in force, front caliper LH"` |  |
| 7 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000006"` | Reference: u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Dust boot seating height"` |  |
| 9 | positionNo | Int32 | - | No (null allowed) | Position number (see collection 1316) | `NumberInt(1)` |  |
| 10 | wipUnitId | String | - | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 12 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"1131000000000001"` | Reference: u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258A00184"` |  |
| 14 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 15 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 16 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 17 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 18 | recipeVersion | String | - | No (null allowed) | Program version | `null` |  |
| 19 | capturedAt | Date | Datetime | Yes | Capture time | `ISODate("2026-09-15T06:01:39.000+0000")` |  |
| 20 | pointCount | Int32 | - | Yes | Number of points stored | `NumberInt(400)` |  |
| 21 | peakX | Decimal128 | - | No (null allowed) | X at peak | `NumberDecimal("41.9")` |  |
| 22 | peakY | Decimal128 | - | No (null allowed) | Peak Y value | `NumberDecimal("1180")` |  |
| 23 | finalX | Decimal128 | - | No (null allowed) | Final X | `NumberDecimal("41.9")` |  |
| 24 | finalY | Decimal128 | - | No (null allowed) | Final Y | `NumberDecimal("1150")` |  |
| 25 | result | String | - | Yes | Envelope verdict | `"OK"` | OK; NOK |
| 26 | failedWindowNo | Int32 | - | No (null allowed) | First failed window | `null` |  |
| 27 | rawControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: raw controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 28 | rawControlledDocumentName | String | - | No (null allowed) | Display value of rawControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 29 | inspectionResultId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionResult._id | `"1150000000000006"` | Reference: u_mes_qual_inspectionResult._id |
| 30 | inspectionResultName | String | - | No (null allowed) | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `"IR-2026-000177"` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:39.000+0000")` |  |
| 34 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 36 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:39.000+0000")` |  |
| 37 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ curveEnvelopeId: 1 }` | No | Look-up of documents by curve envelope |
| 4 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 5 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 6 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 7 | `{ operationExecutionId: 1 }` | No | Look-up of documents by operation execution |
| 8 | `{ siteId: 1, capturedAt: -1 }` | No | Time-ordered lists and reports by captured at |

## Referenced by

u_mes_qual_inspectionResult, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_qual_measurementCurvePoint.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_measurementCurve.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_measurementCurve.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_measurementCurve.js
