# u_mes_mdm_manufacturer

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Manufacturers of equipment, gauges, devices and spare parts |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | MFR-<recordNo> |
| Display value used by references | name |
| Keys | 12 (8 required, 4 may be null) |
| Estimated volume per year | 50-300 |
| Storage | standard |

## Structure

Flat entity collection: one document per manufacturer, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MFR-<recordNo> | `"MFR-ATLAS-COPCO"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ATLAS-COPCO"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the manufacturer; used as its display value in other collections | `"Atlas Copco"` |  |
| 6 | description | String | Yes | Description of the manufacturer | `"Atlas Copco"` |  |
| 7 | countryId | String | No (null allowed) | Reference to u_mes_mdm_country._id | `"CTY-IN"` | Reference: u_mes_mdm_country._id |
| 8 | countryName | String | No (null allowed) | Display value of countryId, copied from u_mes_mdm_country.name | `"India"` |  |
| 9 | website | String | No (null allowed) | Website of the manufacturer | `"https://www.varunabrakes.example"` |  |
| 10 | supportPhone | String | No (null allowed) | Support phone | `"+91-20-5550-0188"` |  |
| 11 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ countryId: 1 }` | No | Look-up of documents by country |

## Referenced by

u_mes_mdm_equipment, u_mes_qlt_gauge, u_mes_mnt_sparePart, u_mes_sys_iotDevice.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_manufacturer.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_manufacturer.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_manufacturer.js
