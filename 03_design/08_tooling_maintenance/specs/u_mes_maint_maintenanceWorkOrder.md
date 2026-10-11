# u_mes_maint_maintenanceWorkOrder

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Breakdown, preventive and improvement work orders with labour, parts used, root cause |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | MWO-<recordNo> |
| Display value used by references | title |
| Keys | 43 (29 required, 14 may be null) |
| Estimated volume per year | ~8,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per maintenance work order, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with maintenanceWorkOrderId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_maint_maintenanceWorkOrderAssignedToUser | Relationship | assigned to user |
| u_mes_maint_maintenanceWorkOrderLabour | Child | labour |
| u_mes_maint_maintenanceWorkOrderUsedSparePart | Child | used spare part |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MWO-<recordNo> | `"MWO-2026-000341"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000341"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the maintenance work order; used as its display value in other collections | `"Nutrunner rundown fault, station 1"` |  |
| 6 | workOrderType | String | Yes | Work order type | `"Breakdown"` | Breakdown; Preventive; Predictive; Improvement; Calibration |
| 7 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 9 | toolId | String | No (null allowed) | Reference to u_mes_maint_tool._id | `"TL-SKT-10-0007"` | Reference: u_mes_maint_tool._id |
| 10 | toolName | String | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 11 | maintenancePlanId | String | No (null allowed) | Reference to u_mes_maint_maintenancePlan._id | `"MP-PM-LKT-01-M"` | Reference: u_mes_maint_maintenancePlan._id |
| 12 | maintenancePlanName | String | No (null allowed) | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Leak tester monthly preventive maintenance"` |  |
| 13 | downtimeEventId | String | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"DT-20260929-0009"` | Reference: u_mes_perf_downtimeEvent._id |
| 14 | downtimeEventName | String | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"20260929-0009"` |  |
| 15 | priority | String | Yes | Priority of the maintenance work order | `"Normal"` | Low; Normal; High; Urgent |
| 16 | reportedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 17 | reportedBy | String | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 18 | reportedAt | Date | Yes | Date and time when the record was reported | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 19 | problemDescription | String | Yes | Problem description | `"Nutrunner stops with rundown torque not reached on every third cycle"` |  |
| 20 | reasonCodeId | String | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"RSN-MECH-NR-02"` | Reference: u_mes_perf_reasonCode._id |
| 21 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Nutrunner socket worn"` |  |
| 22 | failureMode | String | Yes | Failure mode | `"Seal cut during piston insertion"` |  |
| 23 | rootCause | String | No (null allowed) | Root cause | `"Socket drive worn beyond limit"` |  |
| 24 | actionTaken | String | No (null allowed) | Action taken | `"Vision check installed on HMC-01 unload station"` |  |
| 25 | plannedStartAt | Date | Yes | Planned start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 26 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 27 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 28 | downtimeMinutes | Int32 | Yes | Downtime (minutes) | `NumberInt(18)` |  |
| 29 | responseMinutes | Int32 | Yes | Response (minutes) | `NumberInt(6)` |  |
| 30 | repairMinutes | Int32 | Yes | Repair (minutes) | `NumberInt(12)` |  |
| 31 | totalCostInr | Decimal128 | Yes | Total cost (Indian rupees) | `NumberDecimal("9840.00")` |  |
| 32 | equipmentReleasedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'equipment released' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 33 | equipmentReleasedBy | String | No (null allowed) | Display name of the user in equipmentReleasedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 34 | equipmentReleasedAt | Date | No (null allowed) | Equipment released date and time | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 35 | followUpRequired | Boolean | Yes | True when: follow up required | `false` |  |
| 36 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Reported; Planned; In Progress; Completed; Closed; Cancelled |
| 37 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 38 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 39 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 40 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 41 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 42 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 43 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Reported, Planned, In Progress, Completed, Closed, Cancelled. Initial state: Reported. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 5 | `{ maintenancePlanId: 1 }` | No | Look-up of documents by maintenance plan |
| 6 | `{ downtimeEventId: 1 }` | No | Look-up of documents by downtime event |
| 7 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 8 | `{ siteId: 1, reportedAt: -1 }` | No | Time-ordered lists and reports by reported at |

## Referenced by

u_mes_perf_downtimeEvent, u_mes_maint_maintenanceWorkOrderAssignedToUser, u_mes_maint_maintenanceWorkOrderLabour, u_mes_maint_maintenanceWorkOrderUsedSparePart, u_mes_maint_toolLifeRecord.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrder.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrder.js
- Sample document: 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrder.js
