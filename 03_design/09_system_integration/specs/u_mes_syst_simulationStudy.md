# u_mes_syst_simulationStudy

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Digital-twin / what-if study with its input snapshot, result, approval and controlled rollout and pre / post comparison. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 33 (16 required, 17 may be null) |
| Estimated volume per year | about 50 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per simulation study, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1339000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SIM-2026-014"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title | `"Leak test stabilisation time 5.0 s to 4.0 s, what-if on cycle time and escape risk"` |  |
| 6 | studyType | String | - | Yes | Study type | `"Process"` | Process; Inventory; Equipment; Calibration Baseline |
| 7 | relatedCollectionName | String | - | No (null allowed) | Name of the collection the related document is in | `"u_mes_prod_recipe"` |  |
| 8 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1073000000000008"` | Reference: Any collection (see relatedCollectionName) |
| 9 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"Caliper leak test 5 bar and 140 bar"` |  |
| 10 | scenarioText | String | - | Yes | Scenario description | `"Stabilisation time of both stages reduced by 1.0 s on 5,000 historical curves"` |  |
| 11 | inputSnapshotAt | Date | Datetime | Yes | Time of the live-data snapshot | `ISODate("2026-09-16T10:00:00.000+0000")` |  |
| 12 | resultText | String | - | No (null allowed) | Result summary | `"Cycle time 24.0 s to 22.0 s; no additional escapes on the 5,000-curve replay"` |  |
| 13 | predictedValue | Decimal128 | - | No (null allowed) | Predicted KPI value | `NumberDecimal("22.0")` |  |
| 14 | predictedKpi | String | - | No (null allowed) | KPI predicted, e.g. FPY % | `"Cycle time (s)"` |  |
| 15 | recommendedRecipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id: recommended recipe | `"1073000000000008"` | Reference: u_mes_prod_recipe._id |
| 16 | recommendedRecipeName | String | - | No (null allowed) | Display value of recommendedRecipeId, copied from u_mes_prod_recipe.name | `"Caliper leak test 5 bar and 140 bar"` |  |
| 17 | rolloutProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: rollout production order | `"1083000000000008"` | Reference: u_mes_plan_productionOrder._id |
| 18 | rolloutProductionOrderName | String | - | No (null allowed) | Display value of rolloutProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000461"` |  |
| 19 | actualValue | Decimal128 | - | No (null allowed) | Observed KPI after rollout | `NumberDecimal("22.3")` |  |
| 20 | comparisonResult | String | - | No (null allowed) | Pre / post comparison | `"Equal"` | Better; Equal; Worse |
| 21 | resultControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: result controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 22 | resultControlledDocumentName | String | - | No (null allowed) | Display value of resultControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 23 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 24 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 25 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-17T09:00:00.000+0000")` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Rolled Out"` | Planned; Completed; Approved; Rolled Out; Rejected |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T09:00:00.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, Completed, Approved, Rolled Out, Rejected. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ recommendedRecipeId: 1 }` | No | Look-up of documents by recommended recipe |
| 4 | `{ rolloutProductionOrderId: 1 }` | No | Look-up of documents by rollout production order |
| 5 | `{ resultControlledDocumentId: 1 }` | No | Look-up of documents by result controlled document |
| 6 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 7 | `{ siteId: 1, inputSnapshotAt: -1 }` | No | Time-ordered lists and reports by input snapshot at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_simulationStudy.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_simulationStudy.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_simulationStudy.js
