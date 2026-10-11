# u_mes_mnt_maintenancePlan

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | Preventive / condition-based plans per equipment or tool with tasks, interval and next due |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | MP-<recordNo> |
| Display value used by references | name |
| Keys | 24 (18 required, 6 may be null) |
| Estimated volume per year | 500-2,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per maintenance plan, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with maintenancePlanId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mnt_maintenancePlanTask | Child | task |
| u_mes_mnt_maintenancePlanRequiredSkill | Relationship | required skill |
| u_mes_mnt_maintenancePlanRequiredSparePart | Child | required spare part |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MP-<recordNo> | `"MP-PM-LKT-01-M"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-LKT-01-M"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the maintenance plan; used as its display value in other collections | `"Leak tester monthly preventive maintenance"` |  |
| 6 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 7 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 8 | toolId | String | No (null allowed) | Reference to u_mes_mnt_tool._id | `"TL-SKT-10-0007"` | Reference: u_mes_mnt_tool._id |
| 9 | toolName | String | No (null allowed) | Display value of toolId, copied from u_mes_mnt_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 10 | planType | String | Yes | Plan type | `"In Process"` | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| 11 | strategy | String | Yes | Strategy of the maintenance plan | `"Torque Control Angle Monitor"` | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| 12 | intervalType | String | Yes | Interval type | `"Calendar"` | Calendar; Counter; Condition |
| 13 | intervalValue | Decimal128 | Yes | Interval value | `NumberDecimal("30")` |  |
| 14 | intervalUom | String | Yes | Interval uom | `"Days"` | Days; Weeks; Months; Cycles; Shots; Run Hours |
| 15 | counterSource | String | No (null allowed) | Counter source | `null` |  |
| 16 | estimatedMinutes | Int32 | Yes | Estimated (minutes) | `NumberInt(8)` |  |
| 17 | lastDoneAt | Date | No (null allowed) | Last done date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 18 | nextDueAt | Date | Yes | Next due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 19 | toleranceDays | Int32 | Yes | Tolerance (days) | `NumberInt(7)` |  |
| 20 | blockEquipmentWhenOverdue | Boolean | Yes | True when: block equipment when overdue | `true` |  |
| 21 | ownerDepartmentId | String | Yes | Reference to u_mes_mdm_department._id: owner department | `"DEPT-MAINT"` | Reference: u_mes_mdm_department._id |
| 22 | ownerDepartmentName | String | Yes | Display value of ownerDepartmentId, copied from u_mes_mdm_department.name | `"Maintenance"` |  |
| 23 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Inactive |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Suspended, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 5 | `{ ownerDepartmentId: 1 }` | No | Look-up of documents by owner department |

## Referenced by

u_mes_mnt_maintenancePlanTask, u_mes_mnt_maintenancePlanRequiredSkill, u_mes_mnt_maintenancePlanRequiredSparePart, u_mes_mnt_maintenanceWorkOrder.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_maintenancePlan.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_maintenancePlan.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_maintenancePlan.js
