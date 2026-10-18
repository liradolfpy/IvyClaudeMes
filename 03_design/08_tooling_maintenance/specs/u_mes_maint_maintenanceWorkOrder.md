# u_mes_maint_maintenanceWorkOrder

| Property | Value |
|---|---|
| Module | ToolingAndMaintenance (maint) |
| Purpose | Breakdown, preventive and improvement work orders with labour, parts used, root cause |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 57 (31 required, 26 may be null) |
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
| u_mes_maint_maintenanceWorkOrderTask | Child | task |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1220000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MWO-2026-000341"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the maintenance work order; used as its display value in other collections | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 7 | workOrderType | String | - | Yes | Work order type | `"Breakdown"` | Breakdown; Preventive; Predictive; Improvement; Calibration |
| 8 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 9 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 10 | toolId | String | - | No (null allowed) | Reference to u_mes_maint_tool._id | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 11 | toolName | String | - | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 12 | maintenancePlanId | String | - | No (null allowed) | Reference to u_mes_maint_maintenancePlan._id | `"1216000000000001"` | Reference: u_mes_maint_maintenancePlan._id |
| 13 | maintenancePlanName | String | - | No (null allowed) | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 14 | downtimeEventId | String | - | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 15 | downtimeEventName | String | - | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 16 | priority | String | - | Yes | Priority of the maintenance work order | `"Normal"` | Low; Normal; High; Urgent |
| 17 | reportedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 18 | reportedBy | String | - | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 19 | reportedAt | Date | Datetime | Yes | Date and time when the record was reported. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 20 | problemDescription | String | - | Yes | Problem description | `"Ejector pin sticks on cavity 2 and the casting does not release"` |  |
| 21 | reasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 22 | reasonCodeName | String | - | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 23 | failureMode | String | - | Yes | Failure mode | `"Shrinkage porosity in the bridge section"` |  |
| 24 | rootCause | String | - | No (null allowed) | Root cause | `"Ejector pin galled after die coating build-up"` |  |
| 25 | actionTaken | String | - | No (null allowed) | Action taken | `"Ejector pin polished and die coat thickness corrected"` |  |
| 26 | plannedStartAt | Date | Datetime | Yes | Planned start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 27 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 28 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 29 | downtimeMinutes | Int32 | - | Yes | Downtime (minutes) | `NumberInt(95)` |  |
| 30 | responseMinutes | Int32 | - | Yes | Response (minutes) | `NumberInt(6)` |  |
| 31 | repairMinutes | Int32 | - | Yes | Repair (minutes) | `NumberInt(12)` |  |
| 32 | totalCostInr | Decimal128 | - | Yes | Total cost (Indian rupees) | `9840.00` |  |
| 33 | equipmentReleasedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'equipment released' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 34 | equipmentReleasedBy | String | - | No (null allowed) | Display name of the user in equipmentReleasedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 35 | equipmentReleasedAt | Date | Datetime | No (null allowed) | Equipment released date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:30.000+0000")` |  |
| 36 | followUpRequired | Boolean | - | Yes | True when: follow up required | `false` |  |
| 37 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 38 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 39 | rootCauseCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: root cause code | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 40 | rootCauseCodeName | String | - | No (null allowed) | Display value of rootCauseCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 41 | closureApprovedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closure approved' | `null` | Reference: u_mes_mast_user._id |
| 42 | closureApprovedBy | String | - | No (null allowed) | Display name of the user in closureApprovedById, copied from u_mes_mast_user.fullName | `null` |  |
| 43 | closureApprovedAt | Date | Datetime | No (null allowed) | Time of the closure approval | `null` |  |
| 44 | andonEventId | String | - | No (null allowed) | Reference to u_mes_plan_andonEvent._id | `"1251000000000001"` | Reference: u_mes_plan_andonEvent._id |
| 45 | andonEventName | String | - | No (null allowed) | Display value of andonEventId, copied from u_mes_plan_andonEvent.description | `"Castings sticking in die 2, operator needs maintenance"` |  |
| 46 | priorityScore | Decimal128 | - | No (null allowed) | Priority score from criticality, due risk and production impact (0 to 100) | `72` |  |
| 47 | schedulingSource | String | - | Yes | How the work order was prioritised and scheduled | `"Manual"` | Manual; Rule; Model |
| 48 | slaResponseDueAt | Date | Datetime | No (null allowed) | Time by which a technician must respond | `ISODate("2026-09-15T06:10:00.000+0000")` |  |
| 49 | slaRepairDueAt | Date | Datetime | No (null allowed) | Time by which the repair must be complete | `ISODate("2026-09-15T08:00:00.000+0000")` |  |
| 50 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Reported; Planned; In Progress; Completed; Closed; Cancelled |
| 51 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 52 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 53 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 54 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 55 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:30.000+0000")` |  |
| 56 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 57 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

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

u_mes_perf_downtimeEvent, u_mes_maint_maintenanceWorkOrderAssignedToUser, u_mes_maint_maintenanceWorkOrderLabour, u_mes_maint_maintenanceWorkOrderUsedSparePart, u_mes_maint_toolLifeRecord, u_mes_plan_andonEvent, u_mes_maint_maintenanceWorkOrderTask, u_mes_maint_sparePartTransaction, u_mes_maint_equipmentLifecycleEvent, u_mes_maint_logbookEntry.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrder.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrder.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrder.js
