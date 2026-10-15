# u_mes_mast_area

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Production and support areas inside a site (ISA-95 Area) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 21 (15 required, 6 may be null) |
| Estimated volume per year | 10-30 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per area, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1005000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"FDY"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the area; used as its display value in other collections | `"Foundry"` |  |
| 7 | areaType | String | - | Yes | Area type | `"Production"` | Production; Storage; Quality; Maintenance; Utility |
| 8 | parentAreaId | String | - | No (null allowed) | Reference to u_mes_mast_area._id: parent area | `null` | Reference: u_mes_mast_area._id |
| 9 | parentAreaName | String | - | No (null allowed) | Display value of parentAreaId, copied from u_mes_mast_area.name | `null` |  |
| 10 | costCenterId | String | - | No (null allowed) | Reference to u_mes_mast_costCenter._id | `"1259000000000001"` | Reference: u_mes_mast_costCenter._id |
| 11 | costCenterName | String | - | No (null allowed) | Display value of costCenterId, copied from u_mes_mast_costCenter.name | `"Foundry"` |  |
| 12 | supervisorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: supervisor user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 13 | supervisorUserName | String | - | No (null allowed) | Display value of supervisorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 14 | floorAreaSqm | Decimal128 | - | Yes | Floor area (square metres) | `NumberDecimal("1850.0")` |  |
| 15 | isProductionArea | Boolean | - | Yes | True when the record is production area | `true` |  |
| 16 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 17 | cleanlinessClass | String | - | Yes | Cleanliness class of the area (GMP-37) | `"Unclassified"` | ISO 7; ISO 8; Controlled Not Classified; Unclassified |
| 18 | environmentallyMonitored | Boolean | - | Yes | True when the area has environmental monitoring points | `false` |  |
| 19 | gowningRequired | Boolean | - | Yes | True when entry requires gowning | `false` |  |
| 20 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_mast_area, u_mes_mast_line, u_mes_mast_workCenter, u_mes_matl_storageLocation, u_mes_qual_audit, u_mes_perf_processTag, u_mes_perf_processReading, u_mes_ehs_safetyIncident, u_mes_qual_auditSchedule, u_mes_qual_environmentalMonitoringPoint.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_area.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_area.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_area.js
