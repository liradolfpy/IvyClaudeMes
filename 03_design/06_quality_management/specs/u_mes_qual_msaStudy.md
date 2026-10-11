# u_mes_qual_msaStudy

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Measurement system analysis: gauge R&R, bias, linearity, attribute agreement |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | MSA-<recordNo> |
| Display value used by references | recordNo |
| Keys | 41 (28 required, 13 may be null) |
| Estimated volume per year | ~200 |
| Storage | standard |

## Structure

Flat entity collection: one document per MSA study, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with msaStudyId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_msaStudyAppraiserUser | Relationship | appraiser user |
| u_mes_qual_msaStudyTrial | Child | trial |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MSA-<recordNo> | `"MSA-2026-0009"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0009"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | gaugeId | String | Yes | Reference to u_mes_qual_gauge._id | `"GAU-G-BG-054"` | Reference: u_mes_qual_gauge._id |
| 6 | gaugeName | String | Yes | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Bore gauge 50-75 mm"` |  |
| 7 | characteristicId | String | Yes | Reference to u_mes_qual_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qual_characteristic._id |
| 8 | characteristicName | String | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Piston bore diameter"` |  |
| 9 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | studyType | String | Yes | Study type | `"Gauge R and R"` | Gauge R and R; Bias; Linearity; Stability; Attribute Agreement |
| 12 | studyMethod | String | Yes | Study method | `"ANOVA"` | ANOVA; Average And Range; Kappa |
| 13 | studyDate | Date | Yes | Study date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 14 | partsCount | Int32 | Yes | Parts count | `NumberInt(10)` |  |
| 15 | trialsCount | Int32 | Yes | Trials count | `NumberInt(3)` |  |
| 16 | resultsEquipmentVariation | Decimal128 | No (null allowed) | Results equipment variation | `NumberDecimal("0.0031")` |  |
| 17 | resultsAppraiserVariation | Decimal128 | No (null allowed) | Results appraiser variation | `NumberDecimal("0.0012")` |  |
| 18 | resultsGrr | Decimal128 | No (null allowed) | Results grr | `NumberDecimal("0.0033")` |  |
| 19 | resultsPartVariation | Decimal128 | No (null allowed) | Results part variation | `NumberDecimal("0.0408")` |  |
| 20 | resultsTotalVariation | Decimal128 | No (null allowed) | Results total variation | `NumberDecimal("0.0409")` |  |
| 21 | resultsGrrPctTolerance | Decimal128 | No (null allowed) | Results grr pct tolerance | `NumberDecimal("7.2")` |  |
| 22 | resultsGrrPctStudyVariation | Decimal128 | No (null allowed) | Results grr pct study variation | `NumberDecimal("8.1")` |  |
| 23 | resultsNdc | Decimal128 | No (null allowed) | Number of distinct categories | `NumberDecimal("17")` |  |
| 24 | resultsBiasValue | Decimal128 | No (null allowed) | Results bias value | `null` |  |
| 25 | resultsKappa | Decimal128 | No (null allowed) | Results kappa | `null` |  |
| 26 | conclusion | String | Yes | Conclusion of the MSA study | `"Acceptable"` | Acceptable; Conditionally Acceptable; Not Acceptable |
| 27 | actionRequired | Boolean | Yes | True when: action required | `false` |  |
| 28 | conductedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'conducted' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 29 | conductedBy | String | Yes | Display name of the user in conductedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 30 | approvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 31 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 32 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 33 | nextStudyDueAt | Date | Yes | Next study due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 34 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Planned; Completed; Accepted; Not Accepted |
| 35 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 36 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 37 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 38 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 39 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 40 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 41 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Planned, Completed, Accepted, Not Accepted. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ gaugeId: 1 }` | No | Look-up of documents by gauge |
| 4 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ siteId: 1, studyDate: -1 }` | No | Time-ordered lists and reports by study date |

## Referenced by

u_mes_qual_ppapSubmissionMsaStudy, u_mes_qual_msaStudyAppraiserUser, u_mes_qual_msaStudyTrial.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_msaStudy.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_msaStudy.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_msaStudy.js
