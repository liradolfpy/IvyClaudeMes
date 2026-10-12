# u_mes_mast_customer

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | OEMs and aftermarket customers; ship-to addresses, label and ASN requirements |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 26 (24 required, 2 may be null) |
| Estimated volume per year | 10-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per customer, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with customerId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_customerShipTo | Child | ship to |
| u_mes_mast_customerContact | Child | contact |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1035000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SML"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the customer; used as its display value in other collections | `"Sahyadri Motors Ltd."` |  |
| 6 | customerType | String | - | Yes | Customer type | `"OEM"` | OEM; Tier 1; Aftermarket |
| 7 | parentCustomerCode | String | - | No (null allowed) | Code of the customer's parent group | `"SMG"` |  |
| 8 | gstin | String | - | Yes | Goods and services tax identification number | `"27AAACV4521K1Z6"` |  |
| 9 | billingAddressLine1 | String | - | Yes | Billing address line1 | `"Survey No. 212, Talegaon Industrial Area"` |  |
| 10 | billingAddressCity | String | - | Yes | Billing address city | `"Pune"` |  |
| 11 | billingAddressState | String | - | Yes | Billing address state | `"Maharashtra"` |  |
| 12 | billingAddressPostalCode | String | - | Yes | Billing address postal code | `"410507"` |  |
| 13 | billingAddressCountryId | String | - | Yes | Reference to u_mes_mast_country._id: billing address country | `"1266000000000001"` | Reference: u_mes_mast_country._id |
| 14 | billingAddressCountryName | String | - | Yes | Display value of billingAddressCountryId, copied from u_mes_mast_country.name | `"India"` |  |
| 15 | supplierCodeAtCustomer | String | - | Yes | Vendor code the customer uses for this plant | `"V10487"` |  |
| 16 | labelTemplateId | String | - | Yes | Reference to u_mes_matl_labelTemplate._id | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 17 | labelTemplateName | String | - | Yes | Display value of labelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 18 | asnRequired | Boolean | - | Yes | True when: ASN required | `true` |  |
| 19 | ppapLevelDefault | Int32 | - | Yes | PPAP level default | `NumberInt(3)` |  |
| 20 | ppmTarget | Int32 | - | Yes | Customer target in defective parts per million | `NumberInt(25)` |  |
| 21 | paymentTermsDays | Int32 | - | Yes | Payment terms (days) | `NumberInt(45)` |  |
| 22 | currencyId | String | - | Yes | Reference to u_mes_mast_currency._id | `"1265000000000001"` | Reference: u_mes_mast_currency._id |
| 23 | currencyName | String | - | Yes | Display value of currencyId, copied from u_mes_mast_currency.name | `"Indian Rupee"` |  |
| 24 | portalUrl | String | - | No (null allowed) | Portal url | `"https://supplier.sahyadrimotors.example"` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ billingAddressCountryId: 1 }` | No | Look-up of documents by billing address country |
| 4 | `{ labelTemplateId: 1 }` | No | Look-up of documents by label template |
| 5 | `{ currencyId: 1 }` | No | Look-up of documents by currency |

## Referenced by

u_mes_mast_customerShipTo, u_mes_mast_customerContact, u_mes_prod_itemCustomerPart, u_mes_prod_productVariant, u_mes_prod_engineeringChange, u_mes_plan_customerSchedule, u_mes_plan_container, u_mes_matl_packagingSpecification, u_mes_matl_labelTemplate, u_mes_matl_shipment, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecord, u_mes_qual_nonconformance, u_mes_qual_deviationPermit, u_mes_qual_capa, u_mes_qual_ppapSubmission, u_mes_qual_audit, u_mes_qual_customerComplaint, u_mes_maint_tool, u_mes_prod_vehicleModel.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_customer.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_customer.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_customer.js
