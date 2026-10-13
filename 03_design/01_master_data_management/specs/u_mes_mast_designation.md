# u_mes_mast_designation

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Job designations of employees |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 14 (14 required, 0 may be null) |
| Estimated volume per year | 20-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per designation, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1257000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ASM-OPR"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the designation; used as its display value in other collections | `"Assembly Operator"` |  |
| 7 | description | String | - | Yes | Description of the designation | `"Assembly Operator (ASM-OPR)"` |  |
| 8 | departmentId | String | - | Yes | Reference to u_mes_mast_department._id | `"1256000000000001"` | Reference: u_mes_mast_department._id |
| 9 | departmentName | String | - | Yes | Display value of departmentId, copied from u_mes_mast_department.name | `"Production"` |  |
| 10 | gradeLevel | Int32 | - | Yes | Grade of the designation in the plant's grade structure (1 = lowest) | `NumberInt(3)` |  |
| 11 | isSupervisory | Boolean | - | Yes | True when the record is supervisory | `false` |  |
| 12 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 13 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ departmentId: 1 }` | No | Look-up of documents by department |

## Referenced by

u_mes_mast_user.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_designation.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_designation.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_designation.js
