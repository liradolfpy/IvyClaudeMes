# u_mes_mast_site

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Plants and warehouses (ISA-95 Site); timezone, address, IATF certificate |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 30 (27 required, 3 may be null) |
| Estimated volume per year | <20 total |
| Storage | standard |

## Structure

Flat entity collection: one document per site, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with siteId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_siteCertificate | Child | certificate |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1003000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1"` |  |
| 3 | name | String | Yes | Name of the site; used as its display value in other collections | `"Chakan Plant, Pune"` |  |
| 4 | enterpriseId | String | Yes | Reference to u_mes_mast_enterprise._id | `"1001000000000001"` | Reference: u_mes_mast_enterprise._id |
| 5 | enterpriseName | String | Yes | Display value of enterpriseId, copied from u_mes_mast_enterprise.name | `"Varuna Brake Systems Pvt. Ltd."` |  |
| 6 | siteType | String | Yes | Site type | `"Manufacturing Plant"` | Manufacturing Plant; Warehouse; Technical Center; Head Office |
| 7 | timezone | String | Yes | IANA time zone name | `"Asia/Kolkata"` |  |
| 8 | utcOffsetMinutes | Int32 | Yes | Offset of local time from UTC in minutes (IST = 330) | `NumberInt(330)` |  |
| 9 | addressLine1 | String | Yes | Address line1 | `"Plot B-14, Chakan MIDC Phase II"` |  |
| 10 | addressLine2 | String | No (null allowed) | Address line2 | `"Village Khalumbre, Taluka Khed"` |  |
| 11 | addressCity | String | Yes | Address city | `"Pune"` |  |
| 12 | addressDistrict | String | Yes | Address district | `"Pune"` |  |
| 13 | addressState | String | Yes | Address state | `"Maharashtra"` |  |
| 14 | addressPostalCode | String | Yes | Address postal code | `"410501"` |  |
| 15 | addressCountryId | String | Yes | Reference to u_mes_mast_country._id: address country | `"1266000000000001"` | Reference: u_mes_mast_country._id |
| 16 | addressCountryName | String | Yes | Display value of addressCountryId, copied from u_mes_mast_country.name | `"India"` |  |
| 17 | geoLatitude | Double | Yes | Geo latitude | `Double(18.7606)` |  |
| 18 | geoLongitude | Double | Yes | Geo longitude | `Double(73.8636)` |  |
| 19 | gstin | String | Yes | Goods and services tax identification number | `"27AAACV4521K1Z6"` |  |
| 20 | factoryLicenceNo | String | Yes | Factory licence number | `"MH/PUN/2(m)(i)/34300/2011/0871"` |  |
| 21 | erpPlantCode | String | Yes | ERP plant code | `"PN01"` |  |
| 22 | defaultWorkCalendarId | String | No (null allowed) | Reference to u_mes_mast_workCalendar._id: default work calendar | `"1018000000000001"` | Reference: u_mes_mast_workCalendar._id |
| 23 | defaultWorkCalendarName | String | No (null allowed) | Display value of defaultWorkCalendarId, copied from u_mes_mast_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 24 | currencyId | String | Yes | Reference to u_mes_mast_currency._id | `"1265000000000001"` | Reference: u_mes_mast_currency._id |
| 25 | currencyName | String | Yes | Display value of currencyId, copied from u_mes_mast_currency.name | `"Indian Rupee"` |  |
| 26 | languageId | String | Yes | Reference to u_mes_mast_language._id | `"1267000000000001"` | Reference: u_mes_mast_language._id |
| 27 | languageName | String | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 28 | headcount | Int32 | Yes | Headcount of the site | `NumberInt(412)` |  |
| 29 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 30 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ enterpriseId: 1 }` | No | Look-up of documents by enterprise |
| 4 | `{ addressCountryId: 1 }` | No | Look-up of documents by address country |
| 5 | `{ defaultWorkCalendarId: 1 }` | No | Look-up of documents by default work calendar |
| 6 | `{ currencyId: 1 }` | No | Look-up of documents by currency |
| 7 | `{ languageId: 1 }` | No | Look-up of documents by language |

## Referenced by

No other collection refers to this one.

In addition, every collection carries siteId, and every transaction collection carries createdById and updatedById.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_site.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_site.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_site.js
