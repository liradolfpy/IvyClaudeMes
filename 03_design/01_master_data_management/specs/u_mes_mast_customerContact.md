# u_mes_mast_customerContact

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per contact of a customer |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_customer |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (10 required, 2 may be null) |

## Structure

Child collection. The parent customer can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. customerId and customerName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1037000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-C01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerId | String | Yes | Reference to u_mes_mast_customer._id: the parent document this one belongs to | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 6 | customerName | String | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the customer contact | `"Arvind Kelkar"` |  |
| 9 | businessFunction | String | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 10 | email | String | No (null allowed) | Email of the customer contact | `"sunil.jadhav@varunabrakes.example"` |  |
| 11 | phone | String | No (null allowed) | Phone of the customer contact | `"+91-2135-555-0142"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_customerContact.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_customerContact.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_customerContact.js
