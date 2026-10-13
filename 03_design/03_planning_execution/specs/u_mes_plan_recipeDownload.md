# u_mes_plan_recipeDownload

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Each download or selection of a program / recipe on a machine with the checksum verification result. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (26 required, 8 may be null) |
| Estimated volume per year | about 8,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per recipe download, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1308000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RDL-20260917-00031"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | recipeId | String | - | Yes | Reference to u_mes_prod_recipe._id | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 7 | recipeName | String | - | Yes | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 8 | recipeVersion | String | - | Yes | Version downloaded | `"1"` |  |
| 9 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 11 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 13 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 15 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `null` | Reference: u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `null` |  |
| 17 | trigger | String | - | Yes | What caused the download | `"Order Start"` | Order Start; Changeover; Operator Request; Revision Release; Controller Reconnect |
| 18 | checksumExpected | String | - | Yes | Checksum of the released version | `"9f2c4a1be07d53c6"` |  |
| 19 | checksumReported | String | - | No (null allowed) | Checksum reported back by the controller | `"9f2c4a1be07d53c6"` |  |
| 20 | verificationResult | String | - | Yes | Verification outcome | `"Match"` | Match; Mismatch; No Response; Version Not Released |
| 21 | downloadedAt | Date | Datetime | Yes | Download time | `ISODate("2026-09-17T06:40:00.000+0000")` |  |
| 22 | verifiedAt | Date | Datetime | No (null allowed) | Verification time | `ISODate("2026-09-17T06:40:40.000+0000")` |  |
| 23 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 24 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 25 | interlockEventId | String | - | No (null allowed) | Reference to u_mes_plan_interlockEvent._id | `null` | Reference: u_mes_plan_interlockEvent._id |
| 26 | interlockEventName | String | - | No (null allowed) | Display value of interlockEventId, copied from u_mes_plan_interlockEvent.recordNo | `null` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | Requested; Verified; Rejected |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:40:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:40:40.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Requested, Verified, Rejected. Initial state: Requested. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ recipeId: 1 }` | No | Look-up of documents by recipe |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 8 | `{ siteId: 1, downloadedAt: -1 }` | No | Time-ordered lists and reports by downloaded at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_recipeDownload.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_recipeDownload.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_recipeDownload.js
