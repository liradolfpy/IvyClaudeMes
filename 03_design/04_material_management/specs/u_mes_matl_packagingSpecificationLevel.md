# u_mes_matl_packagingSpecificationLevel

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | One document per level of a packaging specification |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_matl_packagingSpecification |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 15 (15 required, 0 may be null) |

## Structure

Child collection. The parent packaging specification can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. packagingSpecificationId and packagingSpecificationName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1123000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PKS-5110-10-0100-SML-01-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | packagingSpecificationId | String | - | Yes | Reference to u_mes_matl_packagingSpecification._id: the parent document this one belongs to | `"1122000000000001"` | Reference: u_mes_matl_packagingSpecification._id |
| 7 | packagingSpecificationName | String | - | Yes | Display value of packagingSpecificationId, copied from u_mes_matl_packagingSpecification.recordNo | `"PKS-5110-10-0100-SML-01"` |  |
| 8 | levelNo | Int32 | - | Yes | Level number | `NumberInt(1)` |  |
| 9 | packTypeId | String | - | Yes | Reference to u_mes_matl_packType._id | `"1281000000000001"` | Reference: u_mes_matl_packType._id |
| 10 | packTypeName | String | - | Yes | Display value of packTypeId, copied from u_mes_matl_packType.name | `"VCI Bag"` |  |
| 11 | quantity | Int32 | - | Yes | Quantity of the packaging specification level | `NumberInt(1)` |  |
| 12 | lengthMm | Decimal128 | - | Yes | Length (mm) | `NumberDecimal("600.0")` |  |
| 13 | widthMm | Decimal128 | - | Yes | Width (mm) | `NumberDecimal("400.0")` |  |
| 14 | heightMm | Decimal128 | - | Yes | Height (mm) | `NumberDecimal("280.0")` |  |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ packagingSpecificationId: 1, levelNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ packTypeId: 1 }` | No | Look-up of lines by pack type |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_packagingSpecificationLevel.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_packagingSpecificationLevel.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_packagingSpecificationLevel.js
