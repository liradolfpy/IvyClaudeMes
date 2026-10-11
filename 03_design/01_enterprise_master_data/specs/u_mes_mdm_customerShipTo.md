# u_mes_mdm_customerShipTo

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | One document per ship to of a customer |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mdm_customer |
| _id pattern | <customerId>-ST<nnn> |
| Display value used by references | name |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Child collection. The parent customer can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. customerId and customerName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <customerId>-ST<nnn> | `"CUS-SML-ST001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-ST001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerId | String | Yes | Reference to u_mes_mdm_customer._id: the parent document this one belongs to | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 6 | customerName | String | Yes | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | shipToCode | String | Yes | Ship to code | `"SML-TLG-D4"` |  |
| 9 | name | String | Yes | Name of the customer ship to; used as its display value in other collections | `"Sahyadri Motors Talegaon Plant, Dock 4"` |  |
| 10 | line1 | String | Yes | Line1 of the customer ship to | `"Gate 3, Chassis Assembly Shop"` |  |
| 11 | city | String | Yes | City of the customer ship to | `"Pune"` |  |
| 12 | state | String | Yes | State of the customer ship to | `"Maharashtra"` |  |
| 13 | postalCode | String | Yes | Postal code | `"410507"` |  |
| 14 | dockCode | String | Yes | Dock code | `"D4"` |  |
| 15 | transitDays | Int32 | Yes | Transit (days) | `NumberInt(1)` |  |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_customerShipTo.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_customerShipTo.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_customerShipTo.js
