# u_mes_qual_characteristicPosition

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per position of a characteristic |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_characteristic |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (10 required, 7 may be null) |

## Structure

Child collection. The parent characteristic can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. characteristicId and characteristicName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1316000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CH-OP050-01-P01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id: the parent document this one belongs to | `"1138000000000005"` | Reference: u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Anodic coating thickness"` |  |
| 8 | positionNo | Int32 | - | Yes | Position number | `NumberInt(1)` |  |
| 9 | positionName | String | - | Yes | Position name, e.g. Piston 1 inboard | `"Outer face, inboard"` |  |
| 10 | nominal | Decimal128 | - | No (null allowed) | Nominal at this position | `NumberDecimal("12.0")` |  |
| 11 | lowerSpecLimit | Decimal128 | - | No (null allowed) | Lower limit at this position | `NumberDecimal("8.0")` |  |
| 12 | upperSpecLimit | Decimal128 | - | No (null allowed) | Upper limit at this position | `NumberDecimal("16.0")` |  |
| 13 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000004"` | Reference: u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Micrometre"` |  |
| 15 | curveEnvelopeId | String | - | No (null allowed) | Reference to u_mes_qual_curveEnvelope._id | `null` | Reference: u_mes_qual_curveEnvelope._id |
| 16 | curveEnvelopeName | String | - | No (null allowed) | Display value of curveEnvelopeId, copied from u_mes_qual_curveEnvelope.name | `null` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ characteristicId: 1, positionNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |
| 3 | `{ curveEnvelopeId: 1 }` | No | Look-up of lines by curve envelope |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_characteristicPosition.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_characteristicPosition.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_characteristicPosition.js
