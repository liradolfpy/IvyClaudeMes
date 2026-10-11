# u_mes_prd_billOfProcessStepProcessParameter

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per process parameter of a bill of process step |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prd_billOfProcessStep |
| _id pattern | <billOfProcessStepId>-PP<nnn> |
| Display value used by references | name |
| Keys | 14 (12 required, 2 may be null) |

## Structure

Child collection. The parent bill of process step can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfProcessStepId and billOfProcessStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <billOfProcessStepId>-PP<nnn> | `"BOP-5110-10-0100-BOP01-S001-PP001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-BOP01-S001-PP001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | billOfProcessStepId | String | Yes | Reference to u_mes_prd_billOfProcessStep._id: the parent document this one belongs to | `"BOP-5110-10-0100-BOP01-S001"` | Reference: u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | Yes | Display value of billOfProcessStepId, copied from u_mes_prd_billOfProcessStep.recordNo | `"5110-10-0100-BOP01-S001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the bill of process step process parameter; used as its display value in other collections | `"Final torque"` |  |
| 9 | nominal | Decimal128 | Yes | Nominal of the bill of process step process parameter | `NumberDecimal("14.0")` |  |
| 10 | lowerLimit | Decimal128 | No (null allowed) | Lower limit | `NumberDecimal("12.0")` |  |
| 11 | upperLimit | Decimal128 | No (null allowed) | Upper limit | `NumberDecimal("16.0")` |  |
| 12 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-NM"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Newton metre"` |  |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfProcessStepId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_billOfProcessStepProcessParameter.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_billOfProcessStepProcessParameter.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_billOfProcessStepProcessParameter.js
