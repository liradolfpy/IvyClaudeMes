# u_mes_mast_enterprise

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Legal entities of the group (ISA-95 Enterprise level); tax and registration data |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 27 (23 required, 4 may be null) |
| Estimated volume per year | <20 total |
| Storage | standard |

## Structure

Flat entity collection: one document per enterprise, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with enterpriseId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_enterpriseContact | Child | contact |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1001000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"VBS"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the enterprise; used as its display value in other collections | `"Varuna Brake Systems Pvt. Ltd."` |  |
| 7 | legalName | String | - | Yes | Legal name | `"Varuna Brake Systems Private Limited"` |  |
| 8 | scope | String | - | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 9 | parentEnterpriseId | String | - | No (null allowed) | Reference to u_mes_mast_enterprise._id: parent enterprise | `null` | Reference: u_mes_mast_enterprise._id |
| 10 | parentEnterpriseName | String | - | No (null allowed) | Display value of parentEnterpriseId, copied from u_mes_mast_enterprise.name | `null` |  |
| 11 | cin | String | - | Yes | Corporate identification number | `"U34300PN2009PTC134567"` |  |
| 12 | gstin | String | - | Yes | Goods and services tax identification number | `"27AAACV4521K1Z6"` |  |
| 13 | pan | String | - | Yes | Permanent account number | `"AAACV4521K"` |  |
| 14 | industryCode | String | - | Yes | National industrial classification code | `"29301"` |  |
| 15 | registeredAddressLine1 | String | - | Yes | Registered address line1 | `"Plot B-14, Chakan MIDC Phase II"` |  |
| 16 | registeredAddressLine2 | String | - | No (null allowed) | Registered address line2 | `"Village Khalumbre, Taluka Khed"` |  |
| 17 | registeredAddressCity | String | - | Yes | Registered address city | `"Pune"` |  |
| 18 | registeredAddressState | String | - | Yes | Registered address state | `"Maharashtra"` |  |
| 19 | registeredAddressPostalCode | String | - | Yes | Registered address postal code | `"410501"` |  |
| 20 | registeredAddressCountryId | String | - | Yes | Reference to u_mes_mast_country._id: registered address country | `"1266000000000001"` | Reference: u_mes_mast_country._id |
| 21 | registeredAddressCountryName | String | - | Yes | Display value of registeredAddressCountryId, copied from u_mes_mast_country.name | `"India"` |  |
| 22 | baseCurrencyId | String | - | Yes | Reference to u_mes_mast_currency._id: base currency | `"1265000000000001"` | Reference: u_mes_mast_currency._id |
| 23 | baseCurrencyName | String | - | Yes | Display value of baseCurrencyId, copied from u_mes_mast_currency.name | `"Indian Rupee"` |  |
| 24 | fiscalYearStartMonth | Int32 | - | Yes | Month number in which the fiscal year starts (4 = April) | `NumberInt(4)` |  |
| 25 | website | String | - | No (null allowed) | Website of the enterprise | `"https://www.varunabrakes.example"` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentEnterpriseId: 1 }` | No | Look-up of documents by parent enterprise |
| 4 | `{ registeredAddressCountryId: 1 }` | No | Look-up of documents by registered address country |
| 5 | `{ baseCurrencyId: 1 }` | No | Look-up of documents by base currency |

## Referenced by

u_mes_mast_enterprise, u_mes_mast_enterpriseContact, u_mes_mast_site.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_enterprise.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_enterprise.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_enterprise.js
