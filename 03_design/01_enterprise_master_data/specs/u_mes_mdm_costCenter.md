# u_mes_mdm_costCenter

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Cost centers charged with activities, mapped to ERP |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CC-<recordNo> |
| Display value used by references | name |
| Keys | 11 (10 required, 1 may be null) |
| Estimated volume per year | 20-200 |
| Storage | standard |

## Structure

Flat entity collection: one document per cost center, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CC-<recordNo> | `"CC-5120"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5120"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the cost center; used as its display value in other collections | `"Assembly Line 1"` |  |
| 6 | description | String | Yes | Description of the cost center | `"Assembly Line 1"` |  |
| 7 | erpCostCenterCode | String | Yes | ERP cost center code | `"PN015120"` |  |
| 8 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 9 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mdm_area, u_mes_mdm_line, u_mes_mdm_workCenter, u_mes_mdm_department, u_mes_exe_indirectActivity.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_costCenter.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_costCenter.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_costCenter.js
