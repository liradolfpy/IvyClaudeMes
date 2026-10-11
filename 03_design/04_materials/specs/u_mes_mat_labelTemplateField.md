# u_mes_mat_labelTemplateField

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | One document per field of a label template |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mat_labelTemplate |
| _id pattern | <labelTemplateId>-F<nnn> |
| Display value used by references | recordNo |
| Keys | 14 (13 required, 1 may be null) |

## Structure

Child collection. The parent label template can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. labelTemplateId and labelTemplateName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <labelTemplateId>-F<nnn> | `"LBT-SML-BIN-A5-F001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-BIN-A5-F001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | labelTemplateId | String | Yes | Reference to u_mes_mat_labelTemplate._id: the parent document this one belongs to | `"LBT-SML-BIN-A5"` | Reference: u_mes_mat_labelTemplate._id |
| 6 | labelTemplateName | String | Yes | Display value of labelTemplateId, copied from u_mes_mat_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | fieldName | String | Yes | Field name | `"customerPartNo"` |  |
| 9 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 10 | fieldFormat | String | No (null allowed) | Field format | `"%s"` |  |
| 11 | positionXMm | Decimal128 | Yes | Position x (mm) | `NumberDecimal("8.0")` |  |
| 12 | positionYMm | Decimal128 | Yes | Position y (mm) | `NumberDecimal("12.5")` |  |
| 13 | isBarcode | Boolean | Yes | True when the record is barcode | `true` |  |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ labelTemplateId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_labelTemplateField.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_labelTemplateField.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_labelTemplateField.js
