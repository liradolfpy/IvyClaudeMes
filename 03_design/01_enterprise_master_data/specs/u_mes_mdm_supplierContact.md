# u_mes_mdm_supplierContact

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | One document per contact of a supplier |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mdm_supplier |
| _id pattern | <supplierId>-C<nnn> |
| Display value used by references | name |
| Keys | 12 (10 required, 2 may be null) |

## Structure

Child collection. The parent supplier can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. supplierId and supplierName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <supplierId>-C<nnn> | `"SUP-S1042-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"S1042-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | supplierId | String | Yes | Reference to u_mes_mdm_supplier._id: the parent document this one belongs to | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 6 | supplierName | String | Yes | Display value of supplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the supplier contact; used as its display value in other collections | `"Mahesh Gawde"` |  |
| 9 | businessFunction | String | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 10 | email | String | No (null allowed) | Email of the supplier contact | `"sunil.jadhav@varunabrakes.example"` |  |
| 11 | phone | String | No (null allowed) | Phone of the supplier contact | `"+91-2135-555-0142"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ supplierId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_supplierContact.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_supplierContact.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_supplierContact.js
