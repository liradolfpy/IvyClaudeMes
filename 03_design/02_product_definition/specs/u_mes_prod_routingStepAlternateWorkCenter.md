# u_mes_prod_routingStepAlternateWorkCenter

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Links one routing step to one alternate work center; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prod_routingStep |
| _id pattern | <routingStepId>-AWC<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A routing step can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. routingStepId and routingStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <routingStepId>-AWC<nnn> | `"RTG-5110-10-0100-R01-S001-AWC001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01-S001-AWC001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | routingStepId | String | Yes | Reference to u_mes_prod_routingStep._id: the parent document this one belongs to | `"RTG-5110-10-0100-R01-S001"` | Reference: u_mes_prod_routingStep._id |
| 6 | routingStepName | String | Yes | Display value of routingStepId, copied from u_mes_prod_routingStep.recordNo | `"5110-10-0100-R01-S001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | alternateWorkCenterId | String | Yes | Reference to u_mes_mast_workCenter._id: alternate work center | `"WC-LKT-01"` | Reference: u_mes_mast_workCenter._id |
| 9 | alternateWorkCenterName | String | Yes | Display value of alternateWorkCenterId, copied from u_mes_mast_workCenter.name | `"Pressure Leak Test Station"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ routingStepId: 1, alternateWorkCenterId: 1 }` | Yes | One link per pair |
| 2 | `{ alternateWorkCenterId: 1, routingStepId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_routingStepAlternateWorkCenter.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_routingStepAlternateWorkCenter.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_routingStepAlternateWorkCenter.js
