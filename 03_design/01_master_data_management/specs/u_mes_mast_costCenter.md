# u_mes_mast_costCenter

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Cost centers charged with activities, mapped to ERP |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
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
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1259000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5010"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the cost center; used as its display value in other collections | `"Foundry"` |  |
| 6 | description | String | Yes | Description of the cost center | `"Foundry (5010)"` |  |
| 7 | erpCostCenterCode | String | Yes | ERP cost center code | `"PN015120"` |  |
| 8 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 9 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_area, u_mes_mast_line, u_mes_mast_workCenter, u_mes_mast_department, u_mes_plan_indirectActivity.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_costCenter.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_costCenter.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_costCenter.js
