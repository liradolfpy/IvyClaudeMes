# u_mes_maint_maintenancePlan

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | Preventive / condition-based plans per equipment or tool with tasks, interval and next due |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 25 (19 required, 6 may be null) |
| Estimated volume per year | 500-2,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per maintenance plan, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with maintenancePlanId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_maint_maintenancePlanTask | Child | task |
| u_mes_maint_maintenancePlanRequiredSkill | Relationship | required skill |
| u_mes_maint_maintenancePlanRequiredSparePart | Child | required spare part |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1216000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-GDC-01-M1"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the maintenance plan; used as its display value in other collections | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 7 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 9 | toolId | String | - | No (null allowed) | Reference to u_mes_maint_tool._id | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 10 | toolName | String | - | No (null allowed) | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 11 | planType | String | - | Yes | Plan type | `"In Process"` | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| 12 | strategy | String | - | Yes | Strategy of the maintenance plan | `"Torque Control"` | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| 13 | intervalType | String | - | Yes | Interval type | `"Calendar"` | Calendar; Counter; Condition |
| 14 | intervalValue | Decimal128 | - | Yes | Interval value | `NumberDecimal("30")` |  |
| 15 | intervalUom | String | - | Yes | Interval uom | `"Days"` | Days; Weeks; Months; Cycles; Shots; Run Hours |
| 16 | counterSource | String | - | No (null allowed) | Counter source | `null` |  |
| 17 | estimatedMinutes | Int32 | - | Yes | Estimated (minutes) | `NumberInt(8)` |  |
| 18 | lastDoneAt | Date | Datetime | No (null allowed) | Last done date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 19 | nextDueAt | Date | Date | Yes | Next due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 20 | toleranceDays | Int32 | - | Yes | Tolerance (days) | `NumberInt(7)` |  |
| 21 | blockEquipmentWhenOverdue | Boolean | - | Yes | True when: block equipment when overdue | `true` |  |
| 22 | ownerDepartmentId | String | - | Yes | Reference to u_mes_mast_department._id: owner department | `"1256000000000003"` | Reference: u_mes_mast_department._id |
| 23 | ownerDepartmentName | String | - | Yes | Display value of ownerDepartmentId, copied from u_mes_mast_department.name | `"Maintenance"` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Inactive |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Suspended, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 5 | `{ ownerDepartmentId: 1 }` | No | Look-up of documents by owner department |

## Referenced by

u_mes_maint_maintenancePlanTask, u_mes_maint_maintenancePlanRequiredSkill, u_mes_maint_maintenancePlanRequiredSparePart, u_mes_maint_maintenanceWorkOrder.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenancePlan.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenancePlan.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenancePlan.js
