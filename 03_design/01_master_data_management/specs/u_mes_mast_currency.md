# u_mes_mast_currency

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Currencies used for costs and invoices |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CUR-<recordNo> |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per currency, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CUR-<recordNo> | `"CUR-INR"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"INR"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the currency; used as its display value in other collections | `"Indian Rupee"` |  |
| 6 | symbol | String | Yes | Symbol of the currency | `"N.m"` |  |
| 7 | decimalPlaces | Int32 | Yes | Decimal places | `NumberInt(1)` |  |
| 8 | isoNumericCode | String | Yes | ISO 4217 numeric currency code | `"356"` |  |
| 9 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
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

u_mes_mast_enterprise, u_mes_mast_site, u_mes_mast_customer, u_mes_mast_supplier.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_currency.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_currency.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_currency.js
