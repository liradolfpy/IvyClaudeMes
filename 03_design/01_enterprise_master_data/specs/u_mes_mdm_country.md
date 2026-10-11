# u_mes_mdm_country

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Countries used in addresses |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CTY-<recordNo> |
| Display value used by references | name |
| Keys | 10 (10 required, 0 may be null) |
| Estimated volume per year | 10-250 |
| Storage | standard |

## Structure

Flat entity collection: one document per country, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CTY-<recordNo> | `"CTY-IN"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"IN"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the country; used as its display value in other collections | `"India"` |  |
| 6 | isoAlpha3Code | String | Yes | ISO 3166-1 alpha-3 country code | `"IND"` |  |
| 7 | dialCode | String | Yes | Dial code | `"+91"` |  |
| 8 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mdm_enterprise, u_mes_mdm_site, u_mes_mdm_customer, u_mes_mdm_supplier, u_mes_mdm_manufacturer.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_country.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_country.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_country.js
