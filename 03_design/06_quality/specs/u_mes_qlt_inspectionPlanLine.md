# u_mes_qlt_inspectionPlanLine

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per line of a inspection plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qlt_inspectionPlan |
| _id pattern | <inspectionPlanId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 20 (16 required, 4 may be null) |

## Structure

Child collection. The parent inspection plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. inspectionPlanId and inspectionPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <inspectionPlanId>-L<nnn> | `"IP-OP030-INP-01-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"OP030-INP-01-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | inspectionPlanId | String | Yes | Reference to u_mes_qlt_inspectionPlan._id: the parent document this one belongs to | `"IP-OP030-INP-01"` | Reference: u_mes_qlt_inspectionPlan._id |
| 6 | inspectionPlanName | String | Yes | Display value of inspectionPlanId, copied from u_mes_qlt_inspectionPlan.name | `"Machining in-process inspection, caliper body LH"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | characteristicId | String | Yes | Reference to u_mes_qlt_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qlt_characteristic._id |
| 9 | characteristicName | String | Yes | Display value of characteristicId, copied from u_mes_qlt_characteristic.name | `"Piston bore diameter"` |  |
| 10 | gaugeId | String | No (null allowed) | Reference to u_mes_qlt_gauge._id | `"GAU-G-BG-054"` | Reference: u_mes_qlt_gauge._id |
| 11 | gaugeName | String | No (null allowed) | Display value of gaugeId, copied from u_mes_qlt_gauge.name | `"Bore gauge 50-75 mm"` |  |
| 12 | sampleSize | Int32 | Yes | Sample size | `NumberInt(5)` |  |
| 13 | frequencyType | String | Yes | Frequency type | `"Every N Units"` | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| 14 | frequencyValue | Decimal128 | Yes | Frequency value | `NumberDecimal("50")` |  |
| 15 | recordType | String | Yes | Record type | `"Measured Value"` | Measured Value; Pass Fail; Count |
| 16 | autoNcOnFail | Boolean | Yes | True when: auto nc on fail | `true` |  |
| 17 | defectCodeId | String | No (null allowed) | Reference to u_mes_qlt_defectCode._id | `"DEF-LK01"` | Reference: u_mes_qlt_defectCode._id |
| 18 | defectCodeName | String | No (null allowed) | Display value of defectCodeId, copied from u_mes_qlt_defectCode.name | `"Leak at piston seal"` |  |
| 19 | overrideAllowed | Boolean | Yes | True when: override allowed | `false` |  |
| 20 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

- Validator: 03_design/06_quality/validators/u_mes_qlt_inspectionPlanLine.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_inspectionPlanLine.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_inspectionPlanLine.js
