# u_mes_prod_routingStepNextStep

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per next step of a routing step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_routingStep |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Child collection. The parent routing step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. routingStepId and routingStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1056000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01-S01-NS01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | routingStepId | String | - | Yes | Reference to u_mes_prod_routingStep._id: the parent document this one belongs to | `"1054000000000001"` | Reference: u_mes_prod_routingStep._id |
| 7 | routingStepName | String | - | Yes | Display value of routingStepId, copied from u_mes_prod_routingStep.recordNo | `"5110-10-0100-R01-S01"` |  |
| 8 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 9 | nextStepCondition | String | - | Yes | Next step condition | `"Result OK"` | Result OK; Result Not OK; Rework Complete; Always |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ routingStepId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_routingStepNextStep.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_routingStepNextStep.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_routingStepNextStep.js
