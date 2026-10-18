# u_mes_mast_shift

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Shift patterns with start/end and breaks |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 15 (15 required, 0 may be null) |
| Estimated volume per year | 3-10 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per shift, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with shiftId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_shiftBreak | Child | break |
| u_mes_mast_shiftWorkingDay | Value list | working day |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1015000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"A"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the shift; used as its display value in other collections | `"Shift A"` |  |
| 7 | startTimeLocal | String | - | Yes | Local start time, 24-hour HH:mm | `"06:00"` |  |
| 8 | endTimeLocal | String | - | Yes | Local end time, 24-hour HH:mm | `"14:00"` |  |
| 9 | crossesMidnight | Boolean | - | Yes | True when: crosses midnight | `false` |  |
| 10 | durationMinutes | Int32 | - | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 11 | plannedProductionMinutes | Int32 | - | Yes | Shift duration less paid and unpaid breaks | `NumberInt(430)` |  |
| 12 | shiftAllowancePerDay | Decimal128 | - | Yes | Shift allowance per day | `0.00` |  |
| 13 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 14 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_lineDefaultShift, u_mes_mast_shiftBreak, u_mes_mast_shiftWorkingDay, u_mes_mast_workCalendarShift, u_mes_mast_workCalendarExceptionShift, u_mes_mast_shiftRoster, u_mes_mast_user, u_mes_plan_productionSchedule, u_mes_plan_dispatchList, u_mes_plan_operationExecution, u_mes_plan_labourBooking, u_mes_plan_shiftHandover, u_mes_qual_checkSheetResult, u_mes_qual_spcSample, u_mes_qual_scrapRecord, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_productionCount, u_mes_perf_oeeRecord, u_mes_perf_processReading, u_mes_perf_alarm, u_mes_maint_maintenanceWorkOrder, u_mes_perf_energyReading, u_mes_plan_andonEvent, u_mes_plan_operatorSession, u_mes_plan_documentAcknowledgement, u_mes_plan_interlockEvent, u_mes_qual_defectRecord, u_mes_perf_lossSummary, u_mes_perf_workCenterPerformance, u_mes_perf_operatorPerformance, u_mes_maint_reliabilitySummary, u_mes_syst_modelPrediction.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shift.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shift.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_shift.js
