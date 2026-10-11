# u_mes_qual_controlPlanLine

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per line of a control plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_controlPlan |
| _id pattern | <controlPlanId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 24 (20 required, 4 may be null) |

## Structure

Child collection. The parent control plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. controlPlanId and controlPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <controlPlanId>-L<nnn> | `"CP-5110-10-0100-PROD-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-PROD-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | controlPlanId | String | Yes | Reference to u_mes_qual_controlPlan._id: the parent document this one belongs to | `"CP-5110-10-0100-PROD"` | Reference: u_mes_qual_controlPlan._id |
| 6 | controlPlanName | String | Yes | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"5110-10-0100-PROD"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 10 | processName | String | Yes | Process name | `"CNC machining of piston bore"` |  |
| 11 | equipmentText | String | Yes | Equipment text | `"Horizontal machining center HMC-01"` |  |
| 12 | characteristicId | String | No (null allowed) | Reference to u_mes_qual_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qual_characteristic._id |
| 13 | characteristicName | String | No (null allowed) | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Piston bore diameter"` |  |
| 14 | classification | String | Yes | Special characteristic class from the drawing or PFMEA | `"Critical"` | Critical; Significant; Standard |
| 15 | specification | String | Yes | Specification of the control plan line | `"54.000 +0.046 / 0 mm"` |  |
| 16 | gaugeId | String | No (null allowed) | Reference to u_mes_qual_gauge._id | `"GAU-G-BG-054"` | Reference: u_mes_qual_gauge._id |
| 17 | gaugeName | String | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Bore gauge 50-75 mm"` |  |
| 18 | measurementTechnique | String | Yes | Measurement technique | `"Air gauge"` |  |
| 19 | sampleSize | Int32 | Yes | Sample size | `NumberInt(5)` |  |
| 20 | sampleFrequency | String | Yes | Sample frequency | `"Every 2 hours"` |  |
| 21 | controlMethod | String | Yes | Control method | `"X-bar R chart"` |  |
| 22 | reactionPlan | String | Yes | Reaction plan | `"Stop, segregate parts since last good check, inform line leader, raise NCR"` |  |
| 23 | responsible | String | Yes | Responsible of the control plan line | `"Operator"` |  |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_controlPlanLine.js
