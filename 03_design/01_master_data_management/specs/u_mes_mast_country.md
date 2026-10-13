# u_mes_mast_country

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Countries used in addresses |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |
| Estimated volume per year | 10-250 |
| Storage | standard |

## Structure

Flat entity collection: one document per country, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1266000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"IN"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Common"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the country; used as its display value in other collections | `"India"` |  |
| 7 | isoAlpha3Code | String | - | Yes | ISO 3166-1 alpha-3 country code | `"IND"` |  |
| 8 | dialCode | String | - | Yes | Dial code | `"+91"` |  |
| 9 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 10 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_enterprise, u_mes_mast_site, u_mes_mast_customer, u_mes_mast_supplier, u_mes_mast_manufacturer.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_country.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_country.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_country.js
