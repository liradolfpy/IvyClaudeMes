# u_mes_syst_modelPrediction

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Each prediction, classification, forecast or recommendation produced by a model, with the action and the actual outcome. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (22 required, 18 may be null) |
| Estimated volume per year | about 500,000 |
| Storage | standard collection, archive after 1 year |

## Structure

Flat entity collection: one document per model prediction, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1338000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PRD-20260915-05112"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | analyticsModelId | String | - | Yes | Reference to u_mes_syst_analyticsModel._id | `"1337000000000001"` | Reference: u_mes_syst_analyticsModel._id |
| 7 | analyticsModelName | String | - | Yes | Display value of analyticsModelId, copied from u_mes_syst_analyticsModel.name | `"Dust boot seating and cap presence classifier"` |  |
| 8 | modelVersion | String | - | Yes | Model version used | `"1.3"` |  |
| 9 | predictionType | String | - | Yes | Prediction type | `"Classification"` | Classification; Forecast; Anomaly; Maintenance Priority; Remaining Useful Life; Recommendation; Operator Risk; Assignment Recommendation |
| 10 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_wipUnit"` |  |
| 11 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1094000000000009"` | Reference: Any collection (see relatedCollectionName) |
| 12 | relatedEntityName | String | - | Yes | Display value of the related document | `"U260924A0288"` |  |
| 13 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000010"` | Reference: u_mes_mast_workCenter._id |
| 14 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Final Inspection and Packing Cell"` |  |
| 15 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 17 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 18 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 19 | predictedAt | Date | Datetime | Yes | Prediction time | `ISODate("2026-09-24T08:35:00.000+0000")` |  |
| 20 | horizonMinutes | Int32 | - | No (null allowed) | Forecast horizon | `null` |  |
| 21 | predictedClass | String | - | No (null allowed) | Predicted class / label | `"OK"` |  |
| 22 | predictedValue | Decimal128 | - | No (null allowed) | Predicted numeric value | `null` |  |
| 23 | confidence | Decimal128 | - | No (null allowed) | Confidence / score 0 to 1 | `NumberDecimal("0.993")` |  |
| 24 | recommendedAction | String | - | No (null allowed) | Recommended action | `null` |  |
| 25 | actionStatus | String | - | Yes | Action status | `"Not Required"` | Not Required; Pending; Approved; Applied; Rejected |
| 26 | actionTakenById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'action taken' | `null` | Reference: u_mes_mast_user._id |
| 27 | actionTakenBy | String | - | No (null allowed) | Display name of the user in actionTakenById, copied from u_mes_mast_user.fullName | `null` |  |
| 28 | actionTakenAt | Date | Datetime | No (null allowed) | Action time | `null` |  |
| 29 | actualValue | Decimal128 | - | No (null allowed) | Observed value for accuracy tracking | `null` |  |
| 30 | actualClass | String | - | No (null allowed) | Observed class | `"OK"` |  |
| 31 | notificationId | String | - | No (null allowed) | Reference to u_mes_syst_notification._id | `null` | Reference: u_mes_syst_notification._id |
| 32 | notificationName | String | - | No (null allowed) | Display value of notificationId, copied from u_mes_syst_notification.title | `null` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | Open; Actioned; Dismissed; Verified |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T08:35:00.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Actioned, Dismissed, Verified. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ analyticsModelId: 1 }` | No | Look-up of documents by analytics model |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ notificationId: 1 }` | No | Look-up of documents by notification |
| 8 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 9 | `{ siteId: 1, predictedAt: -1 }` | No | Time-ordered lists and reports by predicted at |

## Referenced by

u_mes_maint_equipmentLifecycleEvent.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_modelPrediction.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_modelPrediction.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_modelPrediction.js
