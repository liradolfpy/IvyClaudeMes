# u_mes_mast_supplier

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Material, tooling and service suppliers; approval status, certificates, PPM rating |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 26 (25 required, 1 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per supplier, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with supplierId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_supplierContact | Child | contact |
| u_mes_mast_supplierCertificate | Child | certificate |
| u_mes_mast_supplierSuppliedItem | Relationship | supplied item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1038000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"S1042"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the supplier; used as its display value in other collections | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 6 | supplierType | String | - | Yes | Supplier type | `"Direct Material"` | Direct Material; Indirect Material; Tooling; Service; Calibration Laboratory |
| 7 | commodityId | String | - | Yes | Reference to u_mes_mast_commodity._id | `"1269000000000001"` | Reference: u_mes_mast_commodity._id |
| 8 | commodityName | String | - | Yes | Display value of commodityId, copied from u_mes_mast_commodity.name | `"Machined Steel Parts"` |  |
| 9 | gstin | String | - | Yes | Goods and services tax identification number | `"27AAACV4521K1Z6"` |  |
| 10 | addressLine1 | String | - | Yes | Address line1 | `"Plot B-14, Chakan MIDC Phase II"` |  |
| 11 | addressCity | String | - | Yes | Address city | `"Pune"` |  |
| 12 | addressState | String | - | Yes | Address state | `"Maharashtra"` |  |
| 13 | addressPostalCode | String | - | Yes | Address postal code | `"410501"` |  |
| 14 | addressCountryId | String | - | Yes | Reference to u_mes_mast_country._id: address country | `"1266000000000001"` | Reference: u_mes_mast_country._id |
| 15 | addressCountryName | String | - | Yes | Display value of addressCountryId, copied from u_mes_mast_country.name | `"India"` |  |
| 16 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 17 | ppmLast12Months | Int32 | - | Yes | Ppm last12 (months) | `NumberInt(38)` |  |
| 18 | deliveryRatingPct | Decimal128 | - | Yes | Delivery rating (percent) | `NumberDecimal("96.5")` |  |
| 19 | qualityRatingPct | Decimal128 | - | Yes | Quality rating (percent) | `NumberDecimal("98.2")` |  |
| 20 | leadTimeDays | Int32 | - | Yes | Lead time (days) | `NumberInt(21)` |  |
| 21 | paymentTermsDays | Int32 | - | Yes | Payment terms (days) | `NumberInt(45)` |  |
| 22 | currencyId | String | - | Yes | Reference to u_mes_mast_currency._id | `"1265000000000001"` | Reference: u_mes_mast_currency._id |
| 23 | currencyName | String | - | Yes | Display value of currencyId, copied from u_mes_mast_currency.name | `"Indian Rupee"` |  |
| 24 | isDirectedSource | Boolean | - | Yes | True when the record is directed source | `false` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Approved; Conditional; Blocked; Inactive |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Approved, Conditional, Blocked, Inactive. Initial state: Approved. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ commodityId: 1 }` | No | Look-up of documents by commodity |
| 4 | `{ addressCountryId: 1 }` | No | Look-up of documents by address country |
| 5 | `{ currencyId: 1 }` | No | Look-up of documents by currency |

## Referenced by

u_mes_mast_equipment, u_mes_mast_user, u_mes_mast_supplierContact, u_mes_mast_supplierCertificate, u_mes_mast_supplierSuppliedItem, u_mes_prod_item, u_mes_plan_lot, u_mes_matl_goodsReceipt, u_mes_qual_nonconformance, u_mes_qual_gauge, u_mes_qual_gaugeCalibration, u_mes_maint_sparePart, u_mes_maint_tool.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_supplier.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_supplier.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_supplier.js
