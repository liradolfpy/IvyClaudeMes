# u_mes_matl_labelTemplateField

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | One document per field of a label template |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_matl_labelTemplate |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 15 (14 required, 1 may be null) |

## Structure

Child collection. The parent label template can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. labelTemplateId and labelTemplateName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1125000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-BIN-A5-F01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | labelTemplateId | String | - | Yes | Reference to u_mes_matl_labelTemplate._id: the parent document this one belongs to | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 7 | labelTemplateName | String | - | Yes | Display value of labelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | fieldName | String | - | Yes | Field name | `"customerPartNo"` |  |
| 10 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 11 | fieldFormat | String | - | No (null allowed) | Field format | `"%s"` |  |
| 12 | positionXMm | Decimal128 | - | Yes | Position x (mm) | `NumberDecimal("8.0")` |  |
| 13 | positionYMm | Decimal128 | - | Yes | Position y (mm) | `NumberDecimal("12.5")` |  |
| 14 | isBarcode | Boolean | - | Yes | True when the record is barcode | `true` |  |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ labelTemplateId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_labelTemplateField.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_labelTemplateField.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_labelTemplateField.js
