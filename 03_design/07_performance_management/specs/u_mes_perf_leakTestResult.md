# u_mes_perf_leakTestResult

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Leak test per unit: stage pressures, decay, leak rate, limits, verdict, retest counter |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 37 (31 required, 6 may be null) |
| Estimated volume per year | ~760,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per leak test result, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with leakTestResultId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_perf_leakTestResultStage | Child | stage |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1214000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LKT-2026-000377"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | wipUnitId | String | - | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000005"` | Reference: u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | - | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260918B0236"` |  |
| 7 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000006"` | Reference: u_mes_plan_operationExecution._id |
| 8 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000391"` |  |
| 9 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000008"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Pressure Leak Tester 1"` |  |
| 11 | recipeId | String | - | Yes | Reference to u_mes_prod_recipe._id | `"1073000000000008"` | Reference: u_mes_prod_recipe._id |
| 12 | recipeName | String | - | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper leak test 5 bar and 140 bar"` |  |
| 13 | testerIotDeviceId | String | - | Yes | Reference to u_mes_syst_iotDevice._id: tester IoT device | `"1232000000000008"` | Reference: u_mes_syst_iotDevice._id |
| 14 | testerIotDeviceName | String | - | Yes | Display value of testerIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Leak tester controller 1"` |  |
| 15 | operatorUserId | String | - | Yes | Reference to u_mes_mast_user._id: operator user | `"1029000000000003"` | Reference: u_mes_mast_user._id |
| 16 | operatorUserName | String | - | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Deepak Gaikwad"` |  |
| 17 | programNo | String | - | Yes | Program number | `"LT-03"` |  |
| 18 | testMedium | String | - | Yes | Test medium | `"Dry Air"` | Dry Air; Nitrogen; Helium |
| 19 | attemptNo | Int32 | - | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 20 | ambientTemperatureC | Decimal128 | - | Yes | Ambient temperature (degrees Celsius) | `NumberDecimal("27.4")` |  |
| 21 | partTemperatureC | Decimal128 | - | Yes | Part temperature (degrees Celsius) | `NumberDecimal("28.1")` |  |
| 22 | fixtureToolId | String | - | No (null allowed) | Reference to u_mes_maint_tool._id: fixture tool | `"1226000000000008"` | Reference: u_mes_maint_tool._id |
| 23 | fixtureToolName | String | - | No (null allowed) | Display value of fixtureToolId, copied from u_mes_maint_tool.name | `"Test seal set, piston bore 54 mm"` |  |
| 24 | masterLeakVerifiedAt | Date | Datetime | No (null allowed) | Master leak verified date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 25 | verdict | String | - | Yes | Verdict of the leak test result | `"Fail"` | Pass; Fail |
| 26 | failureReason | String | - | No (null allowed) | Failure reason | `"Fill pressure not reached at the high-pressure stage, inlet test seal of the tester leaking"` |  |
| 27 | testedAt | Date | Datetime | Yes | Date and time when the record was tested. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:11:33.000+0000")` |  |
| 28 | measurementCurveId | String | - | No (null allowed) | Reference to u_mes_qual_measurementCurve._id | `"1319000000000007"` | Reference: u_mes_qual_measurementCurve._id |
| 29 | measurementCurveName | String | - | No (null allowed) | Display value of measurementCurveId, copied from u_mes_qual_measurementCurve.recordNo | `"CRV-20260918-01882"` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 32 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:11:03.000+0000")` |  |
| 33 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 34 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 35 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:11:33.000+0000")` |  |
| 36 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 37 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
| 6 | `{ recipeId: 1 }` | No | Look-up of documents by recipe |
| 7 | `{ testerIotDeviceId: 1 }` | No | Look-up of documents by tester IoT device |
| 8 | `{ siteId: 1, masterLeakVerifiedAt: -1 }` | No | Time-ordered lists and reports by master leak verified at |
| 9 | `{ wipUnitId: 1, testedAt: -1 }` | No | Test history of one unit |

## Referenced by

u_mes_trac_asBuiltRecord, u_mes_perf_leakTestResultStage.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_leakTestResult.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_leakTestResult.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_leakTestResult.js
