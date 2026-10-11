# u_mes_mdm_line

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Production lines / cells (ISA-95 Production Line / Work Cell) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | LN-<recordNo> |
| Display value used by references | name |
| Keys | 22 (16 required, 6 may be null) |
| Estimated volume per year | 10-40 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per line, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with lineId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_lineDefaultShift | Relationship | default shift |
| u_mes_mdm_lineIdealRate | Child | ideal rate |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: LN-<recordNo> | `"LN-ASY-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ASY-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the line; used as its display value in other collections | `"Caliper Assembly Line 1"` |  |
| 6 | areaId | String | Yes | Reference to u_mes_mdm_area._id | `"AR-ASY"` | Reference: u_mes_mdm_area._id |
| 7 | areaName | String | Yes | Display value of areaId, copied from u_mes_mdm_area.name | `"Assembly and Test"` |  |
| 8 | lineType | String | Yes | Line type | `"Assembly"` | Casting; Heat Treatment; Machining; Surface Treatment; Assembly; Inspection; Packing |
| 9 | itemFamilyId | String | Yes | Reference to u_mes_prd_itemFamily._id | `"IFM-FRONT-CALIPER"` | Reference: u_mes_prd_itemFamily._id |
| 10 | itemFamilyName | String | Yes | Display value of itemFamilyId, copied from u_mes_prd_itemFamily.name | `"Front Caliper"` |  |
| 11 | workCalendarId | String | No (null allowed) | Reference to u_mes_mdm_workCalendar._id | `"CAL-PN1-2026"` | Reference: u_mes_mdm_workCalendar._id |
| 12 | workCalendarName | String | No (null allowed) | Display value of workCalendarId, copied from u_mes_mdm_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 13 | taktTimeSec | Decimal128 | Yes | Takt time (seconds) | `NumberDecimal("36.0")` |  |
| 14 | manningStandard | Int32 | Yes | Standard number of operators for the line | `NumberInt(6)` |  |
| 15 | bottleneckWorkCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id: bottleneck work center | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 16 | bottleneckWorkCenterName | String | No (null allowed) | Display value of bottleneckWorkCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 17 | oeeTarget | Decimal128 | Yes | Target OEE in percent | `NumberDecimal("85.0")` |  |
| 18 | costCenterId | String | No (null allowed) | Reference to u_mes_mdm_costCenter._id | `"CC-5120"` | Reference: u_mes_mdm_costCenter._id |
| 19 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mdm_costCenter.name | `"Assembly Line 1"` |  |
| 20 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 21 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 22 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ itemFamilyId: 1 }` | No | Look-up of documents by item family |
| 5 | `{ workCalendarId: 1 }` | No | Look-up of documents by work calendar |
| 6 | `{ bottleneckWorkCenterId: 1 }` | No | Look-up of documents by bottleneck work center |
| 7 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |

## Referenced by

u_mes_mdm_lineDefaultShift, u_mes_mdm_lineIdealRate, u_mes_mdm_workCenter, u_mes_mdm_equipment, u_mes_mdm_workCalendarLine, u_mes_mdm_shiftRoster, u_mes_exe_productionOrder, u_mes_exe_productionSchedule, u_mes_exe_changeover, u_mes_exe_shiftHandover, u_mes_qlt_audit, u_mes_eqp_downtimeEvent, u_mes_eqp_productionCount, u_mes_eqp_oeeRecord, u_mes_ehs_energyReading, u_mes_ehs_andonEvent.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_line.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_line.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_line.js
