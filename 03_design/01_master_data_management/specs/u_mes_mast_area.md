# u_mes_mast_area

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Production and support areas inside a site (ISA-95 Area) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | AR-<recordNo> |
| Display value used by references | name |
| Keys | 17 (11 required, 6 may be null) |
| Estimated volume per year | 10-30 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per area, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: AR-<recordNo> | `"AR-ASY"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ASY"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the area; used as its display value in other collections | `"Assembly and Test"` |  |
| 6 | areaType | String | Yes | Area type | `"Production"` | Production; Storage; Quality; Maintenance; Utility |
| 7 | parentAreaId | String | No (null allowed) | Reference to u_mes_mast_area._id: parent area | `"AR-PRD"` | Reference: u_mes_mast_area._id |
| 8 | parentAreaName | String | No (null allowed) | Display value of parentAreaId, copied from u_mes_mast_area.name | `"Production"` |  |
| 9 | costCenterId | String | No (null allowed) | Reference to u_mes_mast_costCenter._id | `"CC-5120"` | Reference: u_mes_mast_costCenter._id |
| 10 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mast_costCenter.name | `"Assembly Line 1"` |  |
| 11 | supervisorUserId | String | No (null allowed) | Reference to u_mes_mast_user._id: supervisor user | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 12 | supervisorUserName | String | No (null allowed) | Display value of supervisorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 13 | floorAreaSqm | Decimal128 | Yes | Floor area (square metres) | `NumberDecimal("1850.0")` |  |
| 14 | isProductionArea | Boolean | Yes | True when the record is production area | `true` |  |
| 15 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 16 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentAreaId: 1 }` | No | Look-up of documents by parent area |
| 4 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |
| 5 | `{ supervisorUserId: 1 }` | No | Look-up of documents by supervisor user |

## Referenced by

u_mes_mast_area, u_mes_mast_line, u_mes_mast_workCenter, u_mes_matl_storageLocation, u_mes_qual_audit, u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_area.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_area.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_area.js
