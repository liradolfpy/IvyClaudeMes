# u_mes_mast_supplierCertificate

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per certificate of a supplier |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_supplier |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (10 required, 1 may be null) |

## Structure

Child collection. The parent supplier can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. supplierId and supplierName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1040000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"S1042-C201"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | supplierId | String | - | Yes | Reference to u_mes_mast_supplier._id: the parent document this one belongs to | `"1038000000000001"` | Reference: u_mes_mast_supplier._id |
| 6 | supplierName | String | - | Yes | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | standard | String | - | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 9 | certificateNo | String | - | Yes | Certificate number | `"IATF-0412877"` |  |
| 10 | validTo | Date | Date | No (null allowed) | Valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ supplierId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_supplierCertificate.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_supplierCertificate.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_supplierCertificate.js
