# u_mes_plan_documentAcknowledgement

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Operator confirmation that a specific revision of a work instruction, recipe or controlled document was read at a station. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (26 required, 8 may be null) |
| Estimated volume per year | about 15,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per document acknowledgement, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1306000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ACK-20260915-00118"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_prod_workInstruction"` | u_mes_prod_workInstruction; u_mes_prod_recipe; u_mes_syst_controlledDocument |
| 7 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1065000000000006"` | Reference: Any collection (see relatedCollectionName) |
| 8 | relatedEntityName | String | - | Yes | Display value of the related document | `"Seal, piston and dust boot assembly - Front caliper LH"` |  |
| 9 | documentVersion | String | - | Yes | Version / revision acknowledged | `"1"` |  |
| 10 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 11 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 12 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 14 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 15 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 16 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 17 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 18 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 19 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 20 | operatorSessionId | String | - | No (null allowed) | Reference to u_mes_plan_operatorSession._id | `"1305000000000001"` | Reference: u_mes_plan_operatorSession._id |
| 21 | operatorSessionName | String | - | No (null allowed) | Display value of operatorSessionId, copied from u_mes_plan_operatorSession.recordNo | `"OSN-20260915-00041"` |  |
| 22 | acknowledgementType | String | - | Yes | Reason for the acknowledgement | `"Shift Start"` | First Read; Revision Re-acknowledgement; Shift Start; Periodic Refresh |
| 23 | method | String | - | Yes | How it was given | `"Badge Scan"` | Touch Confirmation; Badge Scan; AR Confirmation; Electronic Signature |
| 24 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 25 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 26 | acknowledgedAt | Date | Datetime | Yes | Time of acknowledgement | `ISODate("2026-09-15T05:39:27.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Acknowledged"` | Acknowledged; Superseded |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:39:27.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:39:27.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Acknowledged, Superseded. Initial state: Acknowledged. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ userId: 1 }` | No | Look-up of documents by user |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 8 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 9 | `{ siteId: 1, acknowledgedAt: -1 }` | No | Time-ordered lists and reports by acknowledged at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_documentAcknowledgement.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_documentAcknowledgement.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_documentAcknowledgement.js
