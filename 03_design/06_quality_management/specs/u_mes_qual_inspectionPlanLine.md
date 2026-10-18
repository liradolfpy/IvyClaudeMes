# u_mes_qual_inspectionPlanLine

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | One document per line of a inspection plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_inspectionPlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 21 (17 required, 4 may be null) |

## Structure

Child collection. The parent inspection plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. inspectionPlanId and inspectionPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1143000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"INP-OP010-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | inspectionPlanId | String | - | Yes | Reference to u_mes_qual_inspectionPlan._id: the parent document this one belongs to | `"1142000000000001"` | Reference: u_mes_qual_inspectionPlan._id |
| 7 | inspectionPlanName | String | - | Yes | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, gravity die casting"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 9 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 11 | gaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id | `"1189000000000001"` | Reference: u_mes_qual_gauge._id |
| 12 | gaugeName | String | - | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 13 | sampleSize | Int32 | - | Yes | Sample size | `NumberInt(5)` |  |
| 14 | frequencyType | String | - | Yes | Frequency type | `"Per Lot"` | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| 15 | frequencyValue | Decimal128 | - | Yes | Frequency value | `50` |  |
| 16 | recordType | String | - | Yes | Record type | `"Measured Value"` | Measured Value; Pass Fail; Count |
| 17 | autoNcOnFail | Boolean | - | Yes | True when: auto nc on fail | `true` |  |
| 18 | defectCodeId | String | - | No (null allowed) | Reference to u_mes_qual_defectCode._id | `"1158000000000001"` | Reference: u_mes_qual_defectCode._id |
| 19 | defectCodeName | String | - | No (null allowed) | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Shrinkage porosity"` |  |
| 20 | overrideAllowed | Boolean | - | Yes | True when: override allowed | `false` |  |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ inspectionPlanId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ characteristicId: 1 }` | No | Look-up of lines by characteristic |
| 3 | `{ gaugeId: 1 }` | No | Look-up of lines by gauge |
| 4 | `{ defectCodeId: 1 }` | No | Look-up of lines by defect code |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_inspectionPlanLine.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_inspectionPlanLine.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_inspectionPlanLine.js
