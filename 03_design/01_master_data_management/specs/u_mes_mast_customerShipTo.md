# u_mes_mast_customerShipTo

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | One document per ship to of a customer |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_customer |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Child collection. The parent customer can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. customerId and customerName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1036000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-ST01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id: the parent document this one belongs to | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 7 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | shipToCode | String | - | Yes | Ship to code | `"SML-TLG-D4"` |  |
| 10 | name | String | - | Yes | Name of the customer ship to | `"Sahyadri Motors Ltd., Dock 3"` |  |
| 11 | line1 | String | - | Yes | Line1 of the customer ship to | `"Gate 3, Chassis Assembly Shop"` |  |
| 12 | city | String | - | Yes | City of the customer ship to | `"Pune"` |  |
| 13 | state | String | - | Yes | State of the customer ship to | `"Maharashtra"` |  |
| 14 | postalCode | String | - | Yes | Postal code | `"410507"` |  |
| 15 | dockCode | String | - | Yes | Dock code | `"D4"` |  |
| 16 | transitDays | Int32 | - | Yes | Transit (days) | `NumberInt(1)` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_customerShipTo.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_customerShipTo.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_customerShipTo.js
