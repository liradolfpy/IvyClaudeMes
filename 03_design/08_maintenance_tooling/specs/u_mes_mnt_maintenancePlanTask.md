# u_mes_mnt_maintenancePlanTask

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | One document per task of a maintenance plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mnt_maintenancePlan |
| _id pattern | <maintenancePlanId>-T<nnn> |
| Display value used by references | description |
| Keys | 12 (11 required, 1 may be null) |

## Structure

Child collection. The parent maintenance plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <maintenancePlanId>-T<nnn> | `"MP-PM-LKT-01-M-T001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-LKT-01-M-T001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenancePlanId | String | Yes | Reference to u_mes_mnt_maintenancePlan._id: the parent document this one belongs to | `"MP-PM-LKT-01-M"` | Reference: u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String | Yes | Display value of maintenancePlanId, copied from u_mes_mnt_maintenancePlan.name | `"Leak tester monthly preventive maintenance"` |  |
| 7 | taskNo | Int32 | Yes | Task number | `NumberInt(10)` |  |
| 8 | description | String | Yes | Description of the maintenance plan task | `"Verify tester with the 0.5 sccm master leak and record the reading"` |  |
| 9 | standardMinutes | Int32 | Yes | Standard (minutes) | `NumberInt(15)` |  |
| 10 | requiresShutdown | Boolean | Yes | True when shutdown is required | `false` |  |
| 11 | acceptanceCriteria | String | No (null allowed) | Acceptance criteria | `"Master leak 0.5 sccm detected within plus or minus 10 percent"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, taskNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_maintenancePlanTask.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_maintenancePlanTask.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_maintenancePlanTask.js
