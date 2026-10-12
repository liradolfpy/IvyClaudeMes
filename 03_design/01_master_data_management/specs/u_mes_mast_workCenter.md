# u_mes_mast_workCenter

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Stations where operations are executed and booked; ERP work centre mapping |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 24 (18 required, 6 may be null) |
| Estimated volume per year | 50-200 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per work center, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with workCenterId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_workCenterEquipment | Relationship | equipment |
| u_mes_mast_workCenterOperation | Relationship | operation |
| u_mes_mast_workCenterRequiresSkill | Relationship | requires skill |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1009000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the work center; used as its display value in other collections | `"Gravity Die Casting Cell 1"` |  |
| 6 | areaId | String | - | Yes | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 7 | areaName | String | - | Yes | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 10 | workCenterType | String | - | Yes | Work center type | `"Machine Station"` | Machine Station; Manual Station; Test Station; Inspection Station; Batch Process |
| 11 | erpWorkCenterCode | String | - | Yes | ERP work center code | `"PN01-TRQ01"` |  |
| 12 | costCenterId | String | - | No (null allowed) | Reference to u_mes_mast_costCenter._id | `"1259000000000001"` | Reference: u_mes_mast_costCenter._id |
| 13 | costCenterName | String | - | No (null allowed) | Display value of costCenterId, copied from u_mes_mast_costCenter.name | `"Foundry"` |  |
| 14 | capacityPerShift | Int32 | - | Yes | CAPAcity per shift | `NumberInt(800)` |  |
| 15 | standardManning | Int32 | - | Yes | Standard manning | `NumberInt(1)` |  |
| 16 | trackingGrain | String | - | Yes | Level at which material is tracked at this point | `"Lot"` | Lot; Unit; Container |
| 17 | inputLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: input location | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 18 | inputLocationName | String | - | No (null allowed) | Display value of inputLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 19 | outputLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: output location | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 20 | outputLocationName | String | - | No (null allowed) | Display value of outputLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 21 | andonEnabled | Boolean | - | Yes | True when: andon enabled | `true` |  |
| 22 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 23 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |
| 6 | `{ inputLocationId: 1 }` | No | Look-up of documents by input location |
| 7 | `{ outputLocationId: 1 }` | No | Look-up of documents by output location |

## Referenced by

u_mes_mast_line, u_mes_mast_workCenterEquipment, u_mes_mast_workCenterOperation, u_mes_mast_workCenterRequiresSkill, u_mes_mast_equipment, u_mes_mast_shiftRosterAssignment, u_mes_mast_user, u_mes_prod_operation, u_mes_prod_routingStep, u_mes_prod_routingStepAlternateWorkCenter, u_mes_plan_dispatchList, u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_wipUnit, u_mes_plan_labourBooking, u_mes_plan_changeover, u_mes_matl_storageLocation, u_mes_matl_kit, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_trac_asBuiltRecordOperation, u_mes_qual_inspectionPlan, u_mes_qual_checkSheet, u_mes_qual_checkSheetResult, u_mes_qual_inspectionResult, u_mes_qual_spcChart, u_mes_qual_spcSample, u_mes_qual_nonconformance, u_mes_qual_reworkOrder, u_mes_qual_scrapRecord, u_mes_qual_gauge, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_productionCount, u_mes_perf_processTag, u_mes_perf_alarm, u_mes_maint_toolLifeRecord, u_mes_syst_iotDevice, u_mes_syst_operatorAppWorkCenter, u_mes_syst_businessEvent, u_mes_plan_andonEvent, u_mes_ehs_safetyIncident, u_mes_prod_workInstructionWorkCenter, u_mes_plan_operatorSession, u_mes_plan_documentAcknowledgement, u_mes_plan_interlockEvent, u_mes_plan_recipeDownload, u_mes_plan_setupVerification, u_mes_matl_replenishmentRule, u_mes_qual_defectRecord, u_mes_qual_auditSchedule, u_mes_perf_lossSummary, u_mes_perf_workCenterPerformance, u_mes_perf_operatorPerformance, u_mes_syst_interlockRule, u_mes_syst_alertRule, u_mes_syst_modelPrediction.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_workCenter.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_workCenter.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_workCenter.js
