# u_mes_prod_routingStep

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | One document per step of a routing |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_routing |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (16 required, 4 may be null) |

## Structure

Child collection. The parent routing can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. routingId and routingName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1054000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01-S01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id: the parent document this one belongs to | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 7 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 8 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 9 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 10 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 11 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 13 | cycleTimeSec | Decimal128 | - | Yes | Cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 14 | setupTimeMin | Int32 | - | Yes | Setup time (minutes) | `NumberInt(45)` |  |
| 15 | isMilestone | Boolean | - | Yes | True when the record is milestone | `true` |  |
| 16 | isOptional | Boolean | - | Yes | True when the record is optional | `false` |  |
| 17 | reworkReturnStepNo | Int32 | - | No (null allowed) | Step to which a unit returns after rework | `null` |  |
| 18 | maxQueueTimeMin | Int32 | - | No (null allowed) | Longest allowed waiting time before this step | `NumberInt(240)` |  |
| 19 | maxReworkCount | Int32 | - | Yes | Maximum rework count | `NumberInt(2)` |  |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_routingStep.js
