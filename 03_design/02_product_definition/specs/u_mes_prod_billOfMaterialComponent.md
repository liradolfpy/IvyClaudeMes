# u_mes_prod_billOfMaterialComponent

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | One document per component of a bill of material |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_billOfMaterial |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 21 (16 required, 5 may be null) |

## Structure

Child collection. The parent bill of material can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. billOfMaterialId and billOfMaterialName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1048000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BOM-5110-10-0100-01-C01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | billOfMaterialId | String | - | Yes | Reference to u_mes_prod_billOfMaterial._id: the parent document this one belongs to | `"1047000000000001"` | Reference: u_mes_prod_billOfMaterial._id |
| 7 | billOfMaterialName | String | - | Yes | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-5110-10-0100-01"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 9 | componentItemId | String | - | Yes | Reference to u_mes_prod_item._id: component item | `"1043000000000003"` | Reference: u_mes_prod_item._id |
| 10 | componentItemName | String | - | Yes | Display value of componentItemId, copied from u_mes_prod_item.description | `"Caliper Body, LH, machined and anodised"` |  |
| 11 | quantity | Decimal128 | - | Yes | Quantity of the bill of material component | `1` |  |
| 12 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 14 | scrapPct | Decimal128 | - | Yes | Scrap (percent) | `0.5` |  |
| 15 | operationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 16 | operationName | String | - | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 17 | isTraceable | Boolean | - | Yes | True when the record is traceable | `true` |  |
| 18 | traceLevel | String | - | Yes | Level at which the consumed component must be recorded | `"Lot"` | None; Lot; Serial |
| 19 | backflush | Boolean | - | Yes | True when: backflush | `false` |  |
| 20 | referenceDesignator | String | - | No (null allowed) | Position reference on the drawing | `"P1"` |  |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ billOfMaterialId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ componentItemId: 1 }` | No | Look-up of lines by component item |
| 3 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |
| 4 | `{ operationId: 1 }` | No | Look-up of lines by operation |

## Referenced by

u_mes_prod_billOfMaterialComponentProductVariant, u_mes_prod_billOfMaterialComponentAlternateItem.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfMaterialComponent.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfMaterialComponent.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfMaterialComponent.js
