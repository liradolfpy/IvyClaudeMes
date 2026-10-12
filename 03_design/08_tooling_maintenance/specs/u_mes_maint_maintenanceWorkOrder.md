# u_mes_maint_maintenanceWorkOrder

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Breakdown, preventive and improvement work orders with labour, parts used, root cause |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 56 (30 required, 26 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title of the maintenance work order; used as its display value in other collections | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 6 | workOrderType | String | - | Yes | Work order type | `"Breakdown"` | Breakdown; Preventive; Predictive; Improvement; Calibration |
| 7 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 9 | toolId | String | - | No (null allowed) | Reference to u_mes_maint_tool._id | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 10 | toolName | String | - | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 11 | maintenancePlanId | String | - | No (null allowed) | Reference to u_mes_maint_maintenancePlan._id | `"1216000000000001"` | Reference: u_mes_maint_maintenancePlan._id |
| 12 | maintenancePlanName | String | - | No (null allowed) | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 13 | downtimeEventId | String | - | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 14 | downtimeEventName | String | - | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 15 | priority | String | - | Yes | Priority of the maintenance work order | `"Normal"` | Low; Normal; High; Urgent |
| 16 | reportedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 17 | reportedBy | String | - | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 18 | reportedAt | Date | Datetime | Yes | Date and time when the record was reported. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 19 | problemDescription | String | - | Yes | Problem description | `"Ejector pin sticks on cavity 2 and the casting does not release"` |  |
| 20 | reasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 21 | reasonCodeName | String | - | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 22 | failureMode | String | - | Yes | Failure mode | `"Shrinkage porosity in the bridge section"` |  |
| 23 | rootCause | String | - | No (null allowed) | Root cause | `"Ejector pin galled after die coating build-up"` |  |
| 24 | actionTaken | String | - | No (null allowed) | Action taken | `"Ejector pin polished and die coat thickness corrected"` |  |
| 25 | plannedStartAt | Date | Datetime | Yes | Planned start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 26 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 27 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 28 | downtimeMinutes | Int32 | - | Yes | Downtime (minutes) | `NumberInt(95)` |  |
| 29 | responseMinutes | Int32 | - | Yes | Response (minutes) | `NumberInt(6)` |  |
| 30 | repairMinutes | Int32 | - | Yes | Repair (minutes) | `NumberInt(12)` |  |
| 31 | totalCostInr | Decimal128 | - | Yes | Total cost (Indian rupees) | `NumberDecimal("9840.00")` |  |
| 32 | equipmentReleasedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'equipment released' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 33 | equipmentReleasedBy | String | - | No (null allowed) | Display name of the user in equipmentReleasedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 34 | equipmentReleasedAt | Date | Datetime | No (null allowed) | Equipment released date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:30.000+0000")` |  |
| 35 | followUpRequired | Boolean | - | Yes | True when: follow up required | `false` |  |
| 36 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 37 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 38 | rootCauseCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: root cause code | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 39 | rootCauseCodeName | String | - | No (null allowed) | Display value of rootCauseCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 40 | closureApprovedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closure approved' | `null` | Reference: u_mes_mast_user._id |
| 41 | closureApprovedBy | String | - | No (null allowed) | Display name of the user in closureApprovedById, copied from u_mes_mast_user.fullName | `null` |  |
| 42 | closureApprovedAt | Date | Datetime | No (null allowed) | Time of the closure approval | `null` |  |
| 43 | andonEventId | String | - | No (null allowed) | Reference to u_mes_plan_andonEvent._id | `"1251000000000001"` | Reference: u_mes_plan_andonEvent._id |
| 44 | andonEventName | String | - | No (null allowed) | Display value of andonEventId, copied from u_mes_plan_andonEvent.description | `"Castings sticking in die 2, operator needs maintenance"` |  |
| 45 | priorityScore | Decimal128 | - | No (null allowed) | Priority score from criticality, due risk and production impact (0 to 100) | `NumberDecimal("72")` |  |
| 46 | schedulingSource | String | - | Yes | How the work order was prioritised and scheduled | `"Manual"` | Manual; Rule; Model |
| 47 | slaResponseDueAt | Date | Datetime | No (null allowed) | Time by which a technician must respond | `ISODate("2026-09-15T06:10:00.000+0000")` |  |
| 48 | slaRepairDueAt | Date | Datetime | No (null allowed) | Time by which the repair must be complete | `ISODate("2026-09-15T08:00:00.000+0000")` |  |
| 49 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Reported; Planned; In Progress; Completed; Closed; Cancelled |
| 50 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 51 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 52 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 53 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 54 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T07:10:30.000+0000")` |  |
| 55 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 56 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

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

u_mes_perf_downtimeEvent, u_mes_maint_maintenanceWorkOrderAssignedToUser, u_mes_maint_maintenanceWorkOrderLabour, u_mes_maint_maintenanceWorkOrderUsedSparePart, u_mes_maint_toolLifeRecord, u_mes_plan_andonEvent, u_mes_maint_maintenanceWorkOrderTask, u_mes_maint_sparePartTransaction, u_mes_maint_equipmentLifecycleEvent.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrder.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrder.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrder.js
