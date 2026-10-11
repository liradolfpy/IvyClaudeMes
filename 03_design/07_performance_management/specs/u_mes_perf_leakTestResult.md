# u_mes_perf_leakTestResult

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Leak test per unit: stage pressures, decay, leak rate, limits, verdict, retest counter |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | LKT-<recordNo> |
| Display value used by references | recordNo |
| Keys | 35 (31 required, 4 may be null) |
| Estimated volume per year | ~760,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per leak test result, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with leakTestResultId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_perf_leakTestResultStage | Child | stage |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: LKT-<recordNo> | `"LKT-20260929-000184"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000184"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | wipUnitId | String | Yes | Reference to u_mes_plan_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260929A0184"` |  |
| 7 | operationExecutionId | String | Yes | Reference to u_mes_plan_operationExecution._id | `"OPX-20260929-000184"` | Reference: u_mes_plan_operationExecution._id |
| 8 | operationExecutionName | String | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"20260929-000184"` |  |
| 9 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"EQ-LKT-01"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Pressure Leak Tester 1"` |  |
| 11 | recipeId | String | Yes | Reference to u_mes_prod_recipe._id | `"RCP-LKT-PRG-03"` | Reference: u_mes_prod_recipe._id |
| 12 | recipeName | String | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper leak test program, 5 bar and 140 bar"` |  |
| 13 | testerIotDeviceId | String | Yes | Reference to u_mes_syst_iotDevice._id: tester IoT device | `"IOT-LKT-CTRL-01"` | Reference: u_mes_syst_iotDevice._id |
| 14 | testerIotDeviceName | String | Yes | Display value of testerIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Leak tester controller 1"` |  |
| 15 | operatorUserId | String | Yes | Reference to u_mes_mast_user._id: operator user | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | operatorUserName | String | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | programNo | String | Yes | Program number | `"PSET-07"` |  |
| 18 | testMedium | String | Yes | Test medium | `"Dry Air"` | Dry Air; Nitrogen; Helium |
| 19 | attemptNo | Int32 | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 20 | ambientTemperatureC | Decimal128 | Yes | Ambient temperature (degrees Celsius) | `NumberDecimal("27.4")` |  |
| 21 | partTemperatureC | Decimal128 | Yes | Part temperature (degrees Celsius) | `NumberDecimal("28.1")` |  |
| 22 | fixtureToolId | String | No (null allowed) | Reference to u_mes_maint_tool._id: fixture tool | `"TL-TSL-54-0003"` | Reference: u_mes_maint_tool._id |
| 23 | fixtureToolName | String | No (null allowed) | Display value of fixtureToolId, copied from u_mes_maint_tool.name | `"Test seal set, piston bore 54 mm"` |  |
| 24 | masterLeakVerifiedAt | Date | No (null allowed) | Master leak verified date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 25 | verdict | String | Yes | Verdict of the leak test result | `"Pass"` | Pass; Fail |
| 26 | failureReason | String | No (null allowed) | Failure reason | `null` |  |
| 27 | testedAt | Date | Yes | Date and time when the record was tested | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 28 | status | String | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 29 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 31 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 33 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 34 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
- Sample document: 03_design/07_performance_management/samples/u_mes_perf_leakTestResult.js
