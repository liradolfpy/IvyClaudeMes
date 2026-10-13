# u_mes_plan_operationExecution

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Start / complete record of an operation on a unit or lot: who, where, when, result, cycle time (track-in / track-out) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 71 (52 required, 19 may be null) |
| Estimated volume per year | ~4.3 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per operation execution, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with operationExecutionId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_operationExecutionDefectCode | Relationship | defect code |
| u_mes_plan_operationExecutionTool | Relationship | tool |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1090000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OPX-2026-000376"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 8 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `null` | Reference: u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `null` |  |
| 10 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 12 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 13 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 14 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000004"` | Reference: u_mes_prod_routing._id |
| 15 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Caliper body casting LH, casting and T6"` |  |
| 16 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 17 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 18 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 19 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 20 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 21 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 22 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 23 | recipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 24 | recipeName | String | - | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 25 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 26 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 27 | operatorUserId | String | - | Yes | Reference to u_mes_mast_user._id: operator user | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 28 | operatorUserName | String | - | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 29 | executionType | String | - | Yes | Execution type | `"Production"` | Production; Rework; Retest; Setup |
| 30 | attemptNo | Int32 | - | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 31 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 32 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:53:15.000+0000")` |  |
| 33 | cycleTimeSec | Decimal128 | - | Yes | Cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 34 | standardCycleTimeSec | Decimal128 | - | Yes | Standard cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 35 | quantityIn | Int32 | - | Yes | Quantity in | `NumberInt(240)` |  |
| 36 | quantityGood | Int32 | - | Yes | Quantity good | `NumberInt(231)` |  |
| 37 | quantityReject | Int32 | - | Yes | Quantity reject | `NumberInt(9)` |  |
| 38 | quantityRework | Int32 | - | Yes | Quantity rework | `NumberInt(0)` |  |
| 39 | result | String | - | Yes | Result of the operation execution | `"OK"` | OK; Not OK |
| 40 | checksSkillVerified | Boolean | - | Yes | True when: checks skill verified | `true` |  |
| 41 | checksRecipeVerified | Boolean | - | Yes | True when: checks recipe verified | `true` |  |
| 42 | checksToolLifeOk | Boolean | - | Yes | True when: checks tool life ok | `true` |  |
| 43 | checksGaugeCalibrationOk | Boolean | - | Yes | True when: checks gauge calibration ok | `true` |  |
| 44 | checksPreviousStepComplete | Boolean | - | Yes | True when: checks previous step complete | `true` |  |
| 45 | nextStepNo | Int32 | - | No (null allowed) | Next step number | `NumberInt(20)` |  |
| 46 | remarks | String | - | No (null allowed) | Remarks of the operation execution | `"Die 2, both cavities running"` |  |
| 47 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `null` | Reference: u_mes_prod_productVariant._id |
| 48 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `null` |  |
| 49 | recipeVersion | String | - | No (null allowed) | Version of the recipe / program used | `"1"` |  |
| 50 | recipeChecksum | String | - | No (null allowed) | Checksum of the program reported by the controller | `"9f2c4a1be07d53c6"` |  |
| 51 | taktTimeSec | Decimal128 | - | No (null allowed) | Takt time of the line at the time of the operation (seconds) | `null` |  |
| 52 | taktBreached | Boolean | - | Yes | True when the cycle time was above takt | `false` |  |
| 53 | captureMethod | String | - | Yes | How the start and completion were captured | `"PLC Signal"` | Scan; PLC Signal; Manual Entry |
| 54 | startScanCode | String | - | No (null allowed) | Code scanned at operation start | `null` |  |
| 55 | operatorSessionId | String | - | No (null allowed) | Reference to u_mes_plan_operatorSession._id | `null` | Reference: u_mes_plan_operatorSession._id |
| 56 | operatorSessionName | String | - | No (null allowed) | Display value of operatorSessionId, copied from u_mes_plan_operatorSession.recordNo | `null` |  |
| 57 | checksVariantVerified | Boolean | - | Yes | Variant check passed at start | `true` |  |
| 58 | checksDocumentAcknowledged | Boolean | - | Yes | Current work instruction revision acknowledged by the operator | `true` |  |
| 59 | checksEquipmentReady | Boolean | - | Yes | Equipment was production-ready at start | `true` |  |
| 60 | checksMaterialReleased | Boolean | - | Yes | All consumed lots were released (not held, not expired) | `true` |  |
| 61 | checksSetupVerified | Boolean | - | Yes | Set-up verification passed for the order | `true` |  |
| 62 | checksEnvironmentOk | Boolean | - | Yes | Environmental conditions of the station were within limits | `true` |  |
| 63 | interlockEventCount | Int32 | - | Yes | Number of interlock events raised during the operation | `NumberInt(0)` |  |
| 64 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Started; Completed; Aborted |
| 65 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 66 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 67 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 68 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 69 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:53:15.000+0000")` |  |
| 70 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 71 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Started, Completed, Aborted. Initial state: Started. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 7 | `{ routingId: 1 }` | No | Look-up of documents by routing |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |
| 9 | `{ wipUnitId: 1, stepNo: 1, attemptNo: 1 }` | No | History of one unit through the routing |
| 10 | `{ workCenterId: 1, startedAt: -1 }` | No | Activity of one work center over time |

## Referenced by

u_mes_plan_operationExecutionDefectCode, u_mes_plan_operationExecutionTool, u_mes_plan_stepCompletion, u_mes_plan_wipUnit, u_mes_plan_labourBooking, u_mes_matl_materialConsumption, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_qual_inspectionResult, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_toolLifeRecord, u_mes_plan_interlockEvent, u_mes_qual_measurementCurve, u_mes_qual_defectRecord.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_operationExecution.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_operationExecution.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_operationExecution.js
