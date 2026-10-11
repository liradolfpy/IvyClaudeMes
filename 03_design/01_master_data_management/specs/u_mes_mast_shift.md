# u_mes_mast_shift

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Shift patterns with start/end and breaks |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | SH-<recordNo> |
| Display value used by references | name |
| Keys | 14 (14 required, 0 may be null) |
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

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SH-<recordNo> | `"SH-A"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"A"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the shift; used as its display value in other collections | `"Shift A"` |  |
| 6 | startTimeLocal | String | Yes | Local start time, 24-hour HH:mm | `"06:00"` |  |
| 7 | endTimeLocal | String | Yes | Local end time, 24-hour HH:mm | `"14:00"` |  |
| 8 | crossesMidnight | Boolean | Yes | True when: crosses midnight | `false` |  |
| 9 | durationMinutes | Int32 | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 10 | plannedProductionMinutes | Int32 | Yes | Shift duration less paid and unpaid breaks | `NumberInt(430)` |  |
| 11 | shiftAllowancePerDay | Decimal128 | Yes | Shift allowance per day | `NumberDecimal("0.00")` |  |
| 12 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 13 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_lineDefaultShift, u_mes_mast_shiftBreak, u_mes_mast_shiftWorkingDay, u_mes_mast_workCalendarShift, u_mes_mast_workCalendarExceptionShift, u_mes_mast_shiftRoster, u_mes_mast_user, u_mes_plan_productionSchedule, u_mes_plan_dispatchList, u_mes_plan_operationExecution, u_mes_plan_labourBooking, u_mes_plan_shiftHandover, u_mes_qual_checkSheetResult, u_mes_qual_spcSample, u_mes_qual_scrapRecord, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_productionCount, u_mes_perf_oeeRecord, u_mes_perf_energyReading, u_mes_plan_andonEvent.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shift.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shift.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_shift.js
