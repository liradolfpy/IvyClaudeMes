# u_mes_syst_analyticsModel

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Registry of AI / ML / rule models and their released versions. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 23 (14 required, 9 may be null) |
| Estimated volume per year | about 30 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per analytics model, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1337000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"AIM-VIS-BOOT-1.3"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Model name | `"Dust boot seating and cap presence classifier"` |  |
| 7 | modelType | String | - | Yes | Model type | `"Vision Classification"` | Vision Classification; Defect Prediction; OEE Forecast; Anomaly Detection; Maintenance Prediction; Demand Forecast; Recipe Optimisation; Operator Risk; Assignment Recommendation |
| 8 | modelVersion | String | - | Yes | Model version | `"1.3"` |  |
| 9 | framework | String | - | No (null allowed) | Framework / runtime | `"Keyence XG-X deep learning tool"` |  |
| 10 | trainingDatasetRef | String | - | No (null allowed) | Training data set reference | `"DS-VIS-BOOT-2026-08 (18,400 labelled images)"` |  |
| 11 | validationMetricName | String | - | No (null allowed) | Validation metric, e.g. Recall | `"Recall NOK"` |  |
| 12 | validationMetricValue | Decimal128 | - | No (null allowed) | Validation result | `NumberDecimal("0.995")` |  |
| 13 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000010"` | Reference: u_mes_mast_equipment._id |
| 14 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Final Inspection Vision Station"` |  |
| 15 | modelControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: model controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 16 | modelControlledDocumentName | String | - | No (null allowed) | Display value of modelControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 17 | effectiveFrom | Date | Date | Yes | Effective from | `ISODate("2026-09-01T00:00:00.000+0000")` |  |
| 18 | effectiveTo | Date | Date | No (null allowed) | Effective to | `null` |  |
| 19 | approvedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 20 | approvedBy | String | - | Yes | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 21 | approvedAt | Date | Datetime | Yes | Approval time | `ISODate("2026-08-29T15:00:00.000+0000")` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Retired |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Retired. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ modelControlledDocumentId: 1 }` | No | Look-up of documents by model controlled document |

## Referenced by

u_mes_prod_recipe, u_mes_qual_inspectionResult, u_mes_matl_materialDemandForecast, u_mes_syst_modelPrediction.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_analyticsModel.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_analyticsModel.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_analyticsModel.js
