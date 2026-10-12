# u_mes_maint_maintenancePlanTask

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | One document per task of a maintenance plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_maint_maintenancePlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (11 required, 1 may be null) |

## Structure

Child collection. The parent maintenance plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1217000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-GDC-01-M1-T01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenancePlanId | String | - | Yes | Reference to u_mes_maint_maintenancePlan._id: the parent document this one belongs to | `"1216000000000001"` | Reference: u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String | - | Yes | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 7 | taskNo | Int32 | - | Yes | Task number | `NumberInt(10)` |  |
| 8 | description | String | - | Yes | Description of the maintenance plan task | `"Skim the ladle, pour in one continuous stream and start the tilt cycle"` |  |
| 9 | standardMinutes | Int32 | - | Yes | Standard (minutes) | `NumberInt(15)` |  |
| 10 | requiresShutdown | Boolean | - | Yes | True when shutdown is required | `false` |  |
| 11 | acceptanceCriteria | String | - | No (null allowed) | Acceptance criteria | `"Master leak 0.5 sccm detected within plus or minus 10 percent"` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, taskNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenancePlanTask.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenancePlanTask.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenancePlanTask.js
