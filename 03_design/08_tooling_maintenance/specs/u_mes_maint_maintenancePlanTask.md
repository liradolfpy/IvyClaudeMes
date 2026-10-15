# u_mes_maint_maintenancePlanTask

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | One document per task of a maintenance plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_maint_maintenancePlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 13 (12 required, 1 may be null) |

## Structure

Child collection. The parent maintenance plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1217000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-GDC-01-M1-T01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | maintenancePlanId | String | - | Yes | Reference to u_mes_maint_maintenancePlan._id: the parent document this one belongs to | `"1216000000000001"` | Reference: u_mes_maint_maintenancePlan._id |
| 7 | maintenancePlanName | String | - | Yes | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 8 | taskNo | Int32 | - | Yes | Task number | `NumberInt(10)` |  |
| 9 | description | String | - | Yes | Description of the maintenance plan task | `"Skim the ladle, pour in one continuous stream and start the tilt cycle"` |  |
| 10 | standardMinutes | Int32 | - | Yes | Standard (minutes) | `NumberInt(15)` |  |
| 11 | requiresShutdown | Boolean | - | Yes | True when shutdown is required | `false` |  |
| 12 | acceptanceCriteria | String | - | No (null allowed) | Acceptance criteria | `"Master leak 0.5 sccm detected within plus or minus 10 percent"` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, taskNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

u_mes_maint_maintenanceWorkOrderTask.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenancePlanTask.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenancePlanTask.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenancePlanTask.js
