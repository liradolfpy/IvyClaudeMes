# u_mes_mast_supplierSuppliedItem

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Links one supplier to one supplied item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_supplier |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (11 required, 1 may be null) |

## Structure

Relationship collection. A supplier can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. supplierId and supplierName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1041000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"S1042-SI01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | supplierId | String | - | Yes | Reference to u_mes_mast_supplier._id: the parent document this one belongs to | `"1038000000000001"` | Reference: u_mes_mast_supplier._id |
| 6 | supplierName | String | - | Yes | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | suppliedItemId | String | - | Yes | Reference to u_mes_prod_item._id: supplied item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 9 | suppliedItemName | String | - | Yes | Display value of suppliedItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 10 | qualificationStatus | String | - | Yes | Approval of the supplier for this item (GMP-40) | `"Qualified"` | Qualified; Conditionally Approved; Disqualified |
| 11 | qualifiedUntilDate | Date | Date | No (null allowed) | Last day of the supplier approval for the item | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ supplierId: 1, suppliedItemId: 1 }` | Yes | One link per pair |
| 2 | `{ suppliedItemId: 1, supplierId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_supplierSuppliedItem.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_supplierSuppliedItem.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_supplierSuppliedItem.js
