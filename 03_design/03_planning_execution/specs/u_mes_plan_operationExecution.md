# u_mes_plan_operationExecution

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Start / complete record of an operation on a unit or lot: who, where, when, result, cycle time (track-in / track-out) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | OPX-<recordNo> |
| Display value used by references | recordNo |
| Keys | 53 (42 required, 11 may be null) |
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

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: OPX-<recordNo> | `"OPX-20260929-000184"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000184"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | Yes | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 7 | wipUnitId | String | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_plan_wipUnit._id |
| 8 | wipUnitName | String | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260929A0184"` |  |
| 9 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 10 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 11 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 12 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 13 | routingId | String | Yes | Reference to u_mes_prod_routing._id | `"RTG-5110-10-0100-R01"` | Reference: u_mes_prod_routing._id |
| 14 | routingName | String | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH assembly routing"` |  |
| 15 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 16 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 17 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 18 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 19 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 20 | equipmentId | String | No (null allowed) | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 21 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 22 | recipeId | String | No (null allowed) | Reference to u_mes_prod_recipe._id | `"RCP-TRQ-PRG-07"` | Reference: u_mes_prod_recipe._id |
| 23 | recipeName | String | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Bleed screw M10 torque program"` |  |
| 24 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 25 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 26 | operatorUserId | String | Yes | Reference to u_mes_mast_user._id: operator user | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 27 | operatorUserName | String | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 28 | executionType | String | Yes | Execution type | `"Production"` | Production; Rework; Retest; Setup |
| 29 | attemptNo | Int32 | Yes | 1 for the first attempt, higher for retests or repeats | `NumberInt(1)` |  |
| 30 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 31 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 32 | cycleTimeSec | Decimal128 | Yes | Cycle time (seconds) | `NumberDecimal("34.2")` |  |
| 33 | standardCycleTimeSec | Decimal128 | Yes | Standard cycle time (seconds) | `NumberDecimal("32.0")` |  |
| 34 | quantityIn | Int32 | Yes | Quantity in | `NumberInt(1)` |  |
| 35 | quantityGood | Int32 | Yes | Quantity good | `NumberInt(1)` |  |
| 36 | quantityReject | Int32 | Yes | Quantity reject | `NumberInt(0)` |  |
| 37 | quantityRework | Int32 | Yes | Quantity rework | `NumberInt(0)` |  |
| 38 | result | String | Yes | Result of the operation execution | `"OK"` | OK; Not OK |
| 39 | checksSkillVerified | Boolean | Yes | True when: checks skill verified | `true` |  |
| 40 | checksRecipeVerified | Boolean | Yes | True when: checks recipe verified | `true` |  |
| 41 | checksToolLifeOk | Boolean | Yes | True when: checks tool life ok | `true` |  |
| 42 | checksGaugeCalibrationOk | Boolean | Yes | True when: checks gauge calibration ok | `true` |  |
| 43 | checksPreviousStepComplete | Boolean | Yes | True when: checks previous step complete | `true` |  |
| 44 | nextStepNo | Int32 | No (null allowed) | Next step number | `NumberInt(80)` |  |
| 45 | remarks | String | No (null allowed) | Remarks of the operation execution | `"No abnormality observed"` |  |
| 46 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Started; Completed; Aborted |
| 47 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 48 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 49 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 50 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 51 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 52 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 53 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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

u_mes_plan_operationExecutionDefectCode, u_mes_plan_operationExecutionTool, u_mes_plan_stepCompletion, u_mes_plan_wipUnit, u_mes_matl_materialConsumption, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_qual_inspectionResult, u_mes_perf_torqueResult, u_mes_perf_leakTestResult.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_operationExecution.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_operationExecution.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_operationExecution.js
