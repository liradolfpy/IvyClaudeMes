# u_mes_prod_billOfProcessStepProcessParameter

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | One document per process parameter of a bill of process step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_billOfProcessStep |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 15 (13 required, 2 may be null) |

## Structure

Child collection. The parent bill of process step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfProcessStepId and billOfProcessStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1064000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BOP-5110-10-0100-R01-S01-PP01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | billOfProcessStepId | String | - | Yes | Reference to u_mes_prod_billOfProcessStep._id: the parent document this one belongs to | `"1058000000000001"` | Reference: u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - | Yes | Display value of billOfProcessStepId, copied from u_mes_prod_billOfProcessStep.recordNo | `"BOP-5110-10-0100-R01-S01"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | name | String | - | Yes | Name of the bill of process step process parameter | `"Die temperature, upper half, casting machine 1"` |  |
| 10 | nominal | Decimal128 | - | Yes | Nominal of the bill of process step process parameter | `NumberDecimal("400.0")` |  |
| 11 | lowerLimit | Decimal128 | - | No (null allowed) | Lower limit | `NumberDecimal("380.0")` |  |
| 12 | upperLimit | Decimal128 | - | No (null allowed) | Upper limit | `NumberDecimal("420.0")` |  |
| 13 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000008"` | Reference: u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Degree Celsius"` |  |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfProcessStepId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfProcessStepProcessParameter.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfProcessStepProcessParameter.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfProcessStepProcessParameter.js
