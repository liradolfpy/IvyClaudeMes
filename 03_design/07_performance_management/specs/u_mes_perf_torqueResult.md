# u_mes_perf_torqueResult

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Tightening results per unit: program, final torque, angle, status, curve reference |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 52 (42 required, 10 may be null) |
| Estimated volume per year | ~1.5 million |
| Storage | standard |

## Structure

Flat entity collection: one document per torque result, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1213000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-2026-000478"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | wipUnitId | String | - | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000002"` | Reference: u_mes_plan_wipUnit._id |
| 7 | wipUnitName | String | - | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0197"` |  |
| 8 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000003"` | Reference: u_mes_plan_operationExecution._id |
| 9 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000382"` |  |
| 10 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 11 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 12 | toolId | String | - | No (null allowed) | Reference to u_mes_maint_tool._id | `"1226000000000007"` | Reference: u_mes_maint_tool._id |
| 13 | toolName | String | - | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Nutrunner socket 10 mm, station 1"` |  |
| 14 | recipeId | String | - | Yes | Reference to u_mes_prod_recipe._id | `"1073000000000007"` | Reference: u_mes_prod_recipe._id |
| 15 | recipeName | String | - | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Bleed screw M10 torque program"` |  |
| 16 | controllerIotDeviceId | String | - | Yes | Reference to u_mes_syst_iotDevice._id: controller IoT device | `"1232000000000007"` | Reference: u_mes_syst_iotDevice._id |
| 17 | controllerIotDeviceName | String | - | Yes | Display value of controllerIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Nutrunner controller, torque station 1"` |  |
| 18 | operatorUserId | String | - | Yes | Reference to u_mes_mast_user._id: operator user | `"1029000000000003"` | Reference: u_mes_mast_user._id |
| 19 | operatorUserName | String | - | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Deepak Gaikwad"` |  |
| 20 | jointName | String | - | Yes | Joint name | `"Bleed screw M10x1.0"` |  |
| 21 | programNo | String | - | Yes | Program number | `"PSET-07"` |  |
| 22 | tighteningNo | Int32 | - | Yes | Tightening number | `NumberInt(1)` |  |
| 23 | attemptNo | Int32 | - | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 24 | targetTorqueNm | Decimal128 | - | Yes | Target torque (N.m) | `NumberDecimal("14.0")` |  |
| 25 | minTorqueNm | Decimal128 | - | Yes | Minimum torque (N.m) | `NumberDecimal("12.0")` |  |
| 26 | maxTorqueNm | Decimal128 | - | Yes | Maximum torque (N.m) | `NumberDecimal("16.0")` |  |
| 27 | finalTorqueNm | Decimal128 | - | Yes | Final torque (N.m) | `NumberDecimal("14.2")` |  |
| 28 | targetAngleDeg | Decimal128 | - | Yes | Target angle (degrees) | `NumberDecimal("40.0")` |  |
| 29 | minAngleDeg | Decimal128 | - | Yes | Minimum angle (degrees) | `NumberDecimal("20.0")` |  |
| 30 | maxAngleDeg | Decimal128 | - | Yes | Maximum angle (degrees) | `NumberDecimal("70.0")` |  |
| 31 | finalAngleDeg | Decimal128 | - | Yes | Final angle (degrees) | `NumberDecimal("38.5")` |  |
| 32 | rundownTimeMs | Int32 | - | Yes | Rundown time (milliseconds) | `NumberInt(1840)` |  |
| 33 | strategy | String | - | Yes | Strategy of the torque result | `"Torque Control"` | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| 34 | result | String | - | Yes | Result of the torque result | `"OK"` | OK; Not OK |
| 35 | failureReason | String | - | No (null allowed) | Failure reason | `null` |  |
| 36 | curveControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: curve controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 37 | curveControlledDocumentName | String | - | No (null allowed) | Display value of curveControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 38 | tightenedAt | Date | Datetime | Yes | Date and time when the record was tightened. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:51.000+0000")` |  |
| 39 | controllerResultNo | String | - | Yes | Result identifier issued by the device controller | `"PF6-000418871"` |  |
| 40 | curveEnvelopeId | String | - | No (null allowed) | Reference to u_mes_qual_curveEnvelope._id | `"1317000000000003"` | Reference: u_mes_qual_curveEnvelope._id |
| 41 | curveEnvelopeName | String | - | No (null allowed) | Display value of curveEnvelopeId, copied from u_mes_qual_curveEnvelope.name | `"Bleed screw M10 torque-angle, LH"` |  |
| 42 | measurementCurveId | String | - | No (null allowed) | Reference to u_mes_qual_measurementCurve._id | `"1319000000000002"` | Reference: u_mes_qual_measurementCurve._id |
| 43 | measurementCurveName | String | - | No (null allowed) | Display value of measurementCurveId, copied from u_mes_qual_measurementCurve.recordNo | `"CRV-20260915-01847"` |  |
| 44 | envelopeResult | String | - | No (null allowed) | Verdict of the envelope check | `"OK"` | OK; NOK |
| 45 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 46 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 47 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:21.000+0000")` |  |
| 48 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 49 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 50 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:51.000+0000")` |  |
| 51 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 52 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 4 | `{ operationExecutionId: 1 }` | No | Look-up of documents by operation execution |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 7 | `{ recipeId: 1 }` | No | Look-up of documents by recipe |
| 8 | `{ siteId: 1, tightenedAt: -1 }` | No | Time-ordered lists and reports by tightened at |
| 9 | `{ wipUnitId: 1, tightenedAt: -1 }` | No | Tightening history of one unit |

## Referenced by

u_mes_trac_asBuiltRecord.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_torqueResult.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_torqueResult.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_torqueResult.js
