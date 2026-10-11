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
| Keys | 46 (41 required, 5 may be null) |
| Estimated volume per year | ~1.5 million |
| Storage | standard |

## Structure

Flat entity collection: one document per torque result, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1213000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-2026-000478"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | wipUnitId | String | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000002"` | Reference: u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0197"` |  |
| 7 | operationExecutionId | String | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000003"` | Reference: u_mes_plan_operationExecution._id |
| 8 | operationExecutionName | String | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000382"` |  |
| 9 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 11 | toolId | String | No (null allowed) | Reference to u_mes_maint_tool._id | `"1226000000000007"` | Reference: u_mes_maint_tool._id |
| 12 | toolName | String | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Nutrunner socket 10 mm, station 1"` |  |
| 13 | recipeId | String | Yes | Reference to u_mes_prod_recipe._id | `"1073000000000007"` | Reference: u_mes_prod_recipe._id |
| 14 | recipeName | String | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Bleed screw M10 torque program"` |  |
| 15 | controllerIotDeviceId | String | Yes | Reference to u_mes_syst_iotDevice._id: controller IoT device | `"1232000000000007"` | Reference: u_mes_syst_iotDevice._id |
| 16 | controllerIotDeviceName | String | Yes | Display value of controllerIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Nutrunner controller, torque station 1"` |  |
| 17 | operatorUserId | String | Yes | Reference to u_mes_mast_user._id: operator user | `"1029000000000003"` | Reference: u_mes_mast_user._id |
| 18 | operatorUserName | String | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Deepak Gaikwad"` |  |
| 19 | jointName | String | Yes | Joint name | `"Bleed screw M10x1.0"` |  |
| 20 | programNo | String | Yes | Program number | `"PSET-07"` |  |
| 21 | tighteningNo | Int32 | Yes | Tightening number | `NumberInt(1)` |  |
| 22 | attemptNo | Int32 | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 23 | targetTorqueNm | Decimal128 | Yes | Target torque (N.m) | `NumberDecimal("14.0")` |  |
| 24 | minTorqueNm | Decimal128 | Yes | Minimum torque (N.m) | `NumberDecimal("12.0")` |  |
| 25 | maxTorqueNm | Decimal128 | Yes | Maximum torque (N.m) | `NumberDecimal("16.0")` |  |
| 26 | finalTorqueNm | Decimal128 | Yes | Final torque (N.m) | `NumberDecimal("14.2")` |  |
| 27 | targetAngleDeg | Decimal128 | Yes | Target angle (degrees) | `NumberDecimal("40.0")` |  |
| 28 | minAngleDeg | Decimal128 | Yes | Minimum angle (degrees) | `NumberDecimal("20.0")` |  |
| 29 | maxAngleDeg | Decimal128 | Yes | Maximum angle (degrees) | `NumberDecimal("70.0")` |  |
| 30 | finalAngleDeg | Decimal128 | Yes | Final angle (degrees) | `NumberDecimal("38.5")` |  |
| 31 | rundownTimeMs | Int32 | Yes | Rundown time (milliseconds) | `NumberInt(1840)` |  |
| 32 | strategy | String | Yes | Strategy of the torque result | `"Torque Control"` | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| 33 | result | String | Yes | Result of the torque result | `"OK"` | OK; Not OK |
| 34 | failureReason | String | No (null allowed) | Failure reason | `null` |  |
| 35 | curveControlledDocumentId | String | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: curve controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 36 | curveControlledDocumentName | String | No (null allowed) | Display value of curveControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 37 | tightenedAt | Date | Yes | Date and time when the record was tightened | `ISODate("2026-09-15T00:32:51.000+0000")` |  |
| 38 | controllerResultNo | String | Yes | Result identifier issued by the device controller | `"PF6-000418871"` |  |
| 39 | status | String | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 40 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 41 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:32:21.000+0000")` |  |
| 42 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 43 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 44 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:32:51.000+0000")` |  |
| 45 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 46 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
