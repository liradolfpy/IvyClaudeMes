# u_mes_prod_billOfProcessStepInterlock

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per interlock of a bill of process step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_billOfProcessStep |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Child collection. The parent bill of process step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfProcessStepId and billOfProcessStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1063000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"BOP-5110-10-0100-R01-S01-I01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfProcessStepId | String | Yes | Reference to u_mes_prod_billOfProcessStep._id: the parent document this one belongs to | `"1058000000000001"` | Reference: u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | Yes | Display value of billOfProcessStepId, copied from u_mes_prod_billOfProcessStep.recordNo | `"BOP-5110-10-0100-R01-S01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | interlockType | String | Yes | Interlock type | `"Skill"` | Skill; Recipe; Tool Life; Gauge Calibration; Previous Step; Component Scan; Maintenance Due |
| 9 | description | String | Yes | Description of the bill of process step interlock | `"Operator must hold a valid certification for gravity die casting operation"` |  |
| 10 | enforced | Boolean | Yes | True when: enforced | `true` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfProcessStepId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfProcessStepInterlock.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfProcessStepInterlock.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfProcessStepInterlock.js
