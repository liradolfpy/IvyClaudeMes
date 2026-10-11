# u_mes_prod_routingStep

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per step of a routing |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_routing |
| _id pattern | <routingId>-S<nnn> |
| Display value used by references | recordNo |
| Keys | 19 (15 required, 4 may be null) |

## Structure

Child collection. The parent routing can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. routingId and routingName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <routingId>-S<nnn> | `"RTG-5110-10-0100-R01-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | routingId | String | Yes | Reference to u_mes_prod_routing._id: the parent document this one belongs to | `"RTG-5110-10-0100-R01"` | Reference: u_mes_prod_routing._id |
| 6 | routingName | String | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH assembly routing"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 10 | workCenterId | String | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 12 | cycleTimeSec | Decimal128 | Yes | Cycle time (seconds) | `NumberDecimal("34.2")` |  |
| 13 | setupTimeMin | Int32 | Yes | Setup time (minutes) | `NumberInt(15)` |  |
| 14 | isMilestone | Boolean | Yes | True when the record is milestone | `true` |  |
| 15 | isOptional | Boolean | Yes | True when the record is optional | `false` |  |
| 16 | reworkReturnStepNo | Int32 | No (null allowed) | Step to which a unit returns after rework | `NumberInt(80)` |  |
| 17 | maxQueueTimeMin | Int32 | No (null allowed) | Longest allowed waiting time before this step | `NumberInt(240)` |  |
| 18 | maxReworkCount | Int32 | Yes | Maximum rework count | `NumberInt(2)` |  |
| 19 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ routingId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ workCenterId: 1 }` | No | Look-up of lines by work center |

## Referenced by

u_mes_prod_routingStepAlternateWorkCenter, u_mes_prod_routingStepNextStep.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_routingStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_routingStep.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_routingStep.js
