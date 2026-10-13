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
| Keys | 12 (11 required, 1 may be null) |
| Estimated volume per year | 20-200 |
| Storage | standard |

## Structure

Flat entity collection: one document per cost center, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1259000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5010"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the cost center; used as its display value in other collections | `"Foundry"` |  |
| 7 | description | String | - | Yes | Description of the cost center | `"Foundry (5010)"` |  |
| 8 | erpCostCenterCode | String | - | Yes | ERP cost center code | `"PN015120"` |  |
| 9 | validFrom | Date | Date | Yes | Valid from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 10 | validTo | Date | Date | No (null allowed) | Valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 11 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
