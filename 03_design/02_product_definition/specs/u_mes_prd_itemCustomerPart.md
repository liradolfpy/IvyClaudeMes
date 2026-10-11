# u_mes_prd_itemCustomerPart

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per customer part of a item |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prd_item |
| _id pattern | <itemId>-CP<nnn> |
| Display value used by references | recordNo |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Child collection. The parent item can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. itemId and itemName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <itemId>-CP<nnn> | `"ITM-5110-10-0100-CP001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-CP001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prd_item._id: the parent document this one belongs to | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | customerId | String | Yes | Reference to u_mes_mdm_customer._id | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 9 | customerName | String | Yes | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 10 | customerPartNo | String | Yes | Customer part number | `"SM-3501-0421-LH"` |  |
| 11 | customerRevision | String | Yes | Customer revision | `"04"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ itemId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ customerId: 1 }` | No | Look-up of lines by customer |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_itemCustomerPart.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_itemCustomerPart.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_itemCustomerPart.js
