# u_mes_mdm_workCenter

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Stations where operations are executed and booked; ERP work centre mapping |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | WC-<recordNo> |
| Display value used by references | name |
| Keys | 24 (18 required, 6 may be null) |
| Estimated volume per year | 50-200 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per work center, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with workCenterId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_workCenterEquipment | Relationship | equipment |
| u_mes_mdm_workCenterOperation | Relationship | operation |
| u_mes_mdm_workCenterRequiresSkill | Relationship | requires skill |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: WC-<recordNo> | `"WC-TRQ-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the work center; used as its display value in other collections | `"Bleed Screw Torque Station"` |  |
| 6 | areaId | String | Yes | Reference to u_mes_mdm_area._id | `"AR-ASY"` | Reference: u_mes_mdm_area._id |
| 7 | areaName | String | Yes | Display value of areaId, copied from u_mes_mdm_area.name | `"Assembly and Test"` |  |
| 8 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 9 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 10 | workCenterType | String | Yes | Work center type | `"Machine Station"` | Machine Station; Manual Station; Test Station; Inspection Station; Batch Process |
| 11 | erpWorkCenterCode | String | Yes | ERP work center code | `"PN01-TRQ01"` |  |
| 12 | costCenterId | String | No (null allowed) | Reference to u_mes_mdm_costCenter._id | `"CC-5120"` | Reference: u_mes_mdm_costCenter._id |
| 13 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mdm_costCenter.name | `"Assembly Line 1"` |  |
| 14 | capacityPerShift | Int32 | Yes | CAPAcity per shift | `NumberInt(800)` |  |
| 15 | standardManning | Int32 | Yes | Standard manning | `NumberInt(1)` |  |
| 16 | trackingGrain | String | Yes | Level at which material is tracked at this point | `"Unit"` | Lot; Unit; Container |
| 17 | inputLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: input location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 18 | inputLocationName | String | No (null allowed) | Display value of inputLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 19 | outputLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: output location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 20 | outputLocationName | String | No (null allowed) | Display value of outputLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 21 | andonEnabled | Boolean | Yes | True when: andon enabled | `true` |  |
| 22 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 23 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_mdm_line, u_mes_mdm_workCenterEquipment, u_mes_mdm_workCenterOperation, u_mes_mdm_workCenterRequiresSkill, u_mes_mdm_equipment, u_mes_mdm_shiftRosterAssignment, u_mes_mdm_user, u_mes_prd_operation, u_mes_prd_routingStep, u_mes_prd_routingStepAlternateWorkCenter, u_mes_exe_dispatchList, u_mes_exe_operationExecution, u_mes_exe_stepCompletion, u_mes_exe_wipUnit, u_mes_exe_labourBooking, u_mes_exe_changeover, u_mes_mat_storageLocation, u_mes_mat_kit, u_mes_mat_materialRequest, u_mes_mat_materialConsumption, u_mes_trc_asBuiltRecordOperation, u_mes_qlt_inspectionPlan, u_mes_qlt_checkSheet, u_mes_qlt_checkSheetResult, u_mes_qlt_inspectionResult, u_mes_qlt_spcChart, u_mes_qlt_spcSample, u_mes_qlt_nonconformance, u_mes_qlt_reworkOrder, u_mes_qlt_scrapRecord, u_mes_qlt_gauge, u_mes_eqp_equipmentState, u_mes_eqp_downtimeEvent, u_mes_eqp_productionCount, u_mes_sys_iotDevice, u_mes_sys_operatorAppWorkCenter, u_mes_sys_businessEvent, u_mes_ehs_andonEvent, u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_workCenter.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_workCenter.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_workCenter.js
