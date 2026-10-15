# u_mes_mast_supplierContact

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | One document per contact of a supplier |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_supplier |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 13 (11 required, 2 may be null) |

## Structure

Child collection. The parent supplier can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. supplierId and supplierName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1039000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"S1042-C01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | supplierId | String | - | Yes | Reference to u_mes_mast_supplier._id: the parent document this one belongs to | `"1038000000000001"` | Reference: u_mes_mast_supplier._id |
| 7 | supplierName | String | - | Yes | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | name | String | - | Yes | Name of the supplier contact | `"Arvind Kelkar"` |  |
| 10 | businessFunction | String | - | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 11 | email | String | - | No (null allowed) | Email of the supplier contact | `"sunil.jadhav@varunabrakes.example"` |  |
| 12 | phone | String | - | No (null allowed) | Phone of the supplier contact | `"+91-2135-555-0142"` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ supplierId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_supplierContact.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_supplierContact.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_supplierContact.js
