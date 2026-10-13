# u_mes_qual_controlPlanLine

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per line of a control plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_controlPlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 25 (21 required, 4 may be null) |

## Structure

Child collection. The parent control plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. controlPlanId and controlPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1141000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CP-5110-10-0100-PROD-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | controlPlanId | String | - | Yes | Reference to u_mes_qual_controlPlan._id: the parent document this one belongs to | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 7 | controlPlanName | String | - | Yes | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 9 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 10 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 11 | processName | String | - | Yes | Process name | `"Pouring and die cycle - Caliper body LH"` |  |
| 12 | equipmentText | String | - | Yes | Equipment text | `"Horizontal machining center HMC-01"` |  |
| 13 | characteristicId | String | - | No (null allowed) | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 14 | characteristicName | String | - | No (null allowed) | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 15 | classification | String | - | Yes | Special characteristic class from the drawing or PFMEA | `"Significant"` | Critical; Significant; Standard |
| 16 | specification | String | - | Yes | Specification of the control plan line | `"54.000 +0.046 / 0 mm"` |  |
| 17 | gaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id | `"1189000000000001"` | Reference: u_mes_qual_gauge._id |
| 18 | gaugeName | String | - | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 19 | measurementTechnique | String | - | Yes | Measurement technique | `"Ultrasonic thickness, three points on the bridge"` |  |
| 20 | sampleSize | Int32 | - | Yes | Sample size | `NumberInt(5)` |  |
| 21 | sampleFrequency | String | - | Yes | Sample frequency | `"Every 2 hours"` |  |
| 22 | controlMethod | String | - | Yes | Control method | `"X-bar R chart"` |  |
| 23 | reactionPlan | String | - | Yes | Reaction plan | `"Stop, segregate parts since last good check, inform line leader, raise NCR"` |  |
| 24 | responsible | String | - | Yes | Responsible of the control plan line | `"Operator"` |  |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ controlPlanId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ characteristicId: 1 }` | No | Look-up of lines by characteristic |
| 4 | `{ gaugeId: 1 }` | No | Look-up of lines by gauge |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_controlPlanLine.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_controlPlanLine.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_controlPlanLine.js
