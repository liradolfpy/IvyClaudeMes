# u_mes_qual_characteristic

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Product and process characteristics with nominal, tolerance, class (critical / significant), method |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 32 (23 required, 9 may be null) |
| Estimated volume per year | 2,000-10,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per characteristic, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1138000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CH-OP010-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the characteristic; used as its display value in other collections | `"Casting wall thickness at bridge"` |  |
| 6 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 8 | operationId | String | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 10 | characteristicType | String | Yes | Characteristic type | `"Product"` | Product; Process |
| 11 | classification | String | Yes | Special characteristic class from the drawing or PFMEA | `"Significant"` | Critical; Significant; Standard |
| 12 | drawingZone | String | No (null allowed) | Drawing zone | `"C4"` |  |
| 13 | balloonNo | String | Yes | Balloon number | `"12"` |  |
| 14 | dataType | String | Yes | Data type | `"Variable"` | Variable; Attribute |
| 15 | nominal | Decimal128 | Yes | Nominal of the characteristic | `NumberDecimal("8.00")` |  |
| 16 | lowerSpecLimit | Decimal128 | No (null allowed) | Lower spec limit | `NumberDecimal("7.50")` |  |
| 17 | upperSpecLimit | Decimal128 | No (null allowed) | Upper spec limit | `NumberDecimal("8.50")` |  |
| 18 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000003"` | Reference: u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Millimetre"` |  |
| 20 | toleranceType | String | Yes | Tolerance type | `"Bilateral"` | Bilateral; Unilateral Upper; Unilateral Lower |
| 21 | measurementMethod | String | Yes | Measurement method | `"Ultrasonic thickness, three points on the bridge"` |  |
| 22 | gaugeId | String | No (null allowed) | Reference to u_mes_qual_gauge._id | `"1189000000000001"` | Reference: u_mes_qual_gauge._id |
| 23 | gaugeName | String | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 24 | gaugeTypeId | String | Yes | Reference to u_mes_qual_gaugeType._id | `"1283000000000001"` | Reference: u_mes_qual_gaugeType._id |
| 25 | gaugeTypeName | String | Yes | Display value of gaugeTypeId, copied from u_mes_qual_gaugeType.name | `"Ultrasonic Thickness Gauge"` |  |
| 26 | attributeAcceptance | String | No (null allowed) | Attribute acceptance | `"No porosity visible on sealing face"` |  |
| 27 | isSpc | Boolean | Yes | True when the record is spc | `true` |  |
| 28 | targetCpk | Decimal128 | No (null allowed) | Target cpk | `NumberDecimal("1.33")` |  |
| 29 | reactionPlan | String | Yes | Reaction plan | `"Stop, segregate parts since last good check, inform line leader, raise NCR"` |  |
| 30 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 6 | `{ gaugeId: 1 }` | No | Look-up of documents by gauge |
| 7 | `{ gaugeTypeId: 1 }` | No | Look-up of documents by gauge type |

## Referenced by

u_mes_prod_workInstructionStepCharacteristic, u_mes_qual_controlPlanLine, u_mes_qual_inspectionPlanLine, u_mes_qual_inspectionResult, u_mes_qual_spcChart, u_mes_qual_spcSample, u_mes_qual_deviationPermit, u_mes_qual_pfmeaLine, u_mes_qual_msaStudy.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_characteristic.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_characteristic.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_characteristic.js
