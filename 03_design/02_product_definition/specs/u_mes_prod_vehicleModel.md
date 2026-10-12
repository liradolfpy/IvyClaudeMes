# u_mes_prod_vehicleModel

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Customer vehicle models the parts are fitted to |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 13 (10 required, 3 may be null) |
| Estimated volume per year | 10-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per vehicle model, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1276000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SM-X42"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the vehicle model; used as its display value in other collections | `"Sahyadri X42 Hatchback"` |  |
| 6 | description | String | - | Yes | Description of the vehicle model | `"Sahyadri X42 Hatchback (SM-X42)"` |  |
| 7 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 8 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 9 | modelYear | Int32 | - | Yes | Model year | `NumberInt(2026)` |  |
| 10 | platformCode | String | - | No (null allowed) | Platform code | `"X4"` |  |
| 11 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |

## Referenced by

u_mes_prod_productVariant, u_mes_qual_customerComplaint.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_vehicleModel.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_vehicleModel.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_vehicleModel.js
