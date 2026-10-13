# u_mes_maint_cleaningRecord

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Cleaning of a piece of equipment after use or before a product change: procedure, dirty hold time, cleaning, verification and the clean hold time it opens. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 36 (23 required, 13 may be null) |
| Estimated volume per year | about 6,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per cleaning record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1356000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CLN-20260915-001"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 7 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 9 | cleaningType | String | - | Yes | Kind of cleaning | `"Product Changeover Cleaning"` | Minor Cleaning; Major Cleaning; Product Changeover Cleaning; Bath Change |
| 10 | procedureControlledDocumentId | String | - | Yes | Reference to u_mes_syst_controlledDocument._id: procedure controlled document | `"1246000000000004"` | Reference: u_mes_syst_controlledDocument._id |
| 11 | procedureControlledDocumentName | String | - | Yes | Display value of procedureControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Cleanliness instruction VBS-CL-001 revision 2"` |  |
| 12 | previousProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: previous production order | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 13 | previousProductionOrderName | String | - | No (null allowed) | Display value of previousProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 14 | previousItemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id: previous item | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 15 | previousItemName | String | - | No (null allowed) | Display value of previousItemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 16 | dirtyHoldStartAt | Date | Datetime | No (null allowed) | End of use: start of the dirty hold time | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 17 | startedAt | Date | Datetime | Yes | Start of cleaning | `ISODate("2026-09-15T13:41:00.000+0000")` |  |
| 18 | completedAt | Date | Datetime | No (null allowed) | End of cleaning | `ISODate("2026-09-15T13:44:00.000+0000")` |  |
| 19 | cleanedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'cleaned' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | cleanedBy | String | - | Yes | Display name of the user in cleanedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 21 | verificationMethod | String | - | Yes | How cleanliness is verified | `"Visual Inspection"` | Visual Inspection; Cleanliness Test; Rinse Sample; Swab Sample |
| 22 | verificationResult | String | - | No (null allowed) | Verification result; null until verified | `"Pass"` | Pass; Fail |
| 23 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 24 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 25 | verifiedAt | Date | Datetime | No (null allowed) | Time of verification | `ISODate("2026-09-15T13:45:00.000+0000")` |  |
| 26 | cleanHoldExpiresAt | Date | Datetime | No (null allowed) | End of the validated clean hold time | `ISODate("2026-09-16T13:45:00.000+0000")` |  |
| 27 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 28 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | In Progress; Completed; Verified; Expired; Rejected |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 32 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 34 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T13:45:00.000+0000")` |  |
| 35 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

In Progress, Completed, Verified, Expired, Rejected. Initial state: In Progress. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ procedureControlledDocumentId: 1 }` | No | Look-up of documents by procedure controlled document |
| 6 | `{ previousProductionOrderId: 1 }` | No | Look-up of documents by previous production order |
| 7 | `{ previousItemId: 1 }` | No | Look-up of documents by previous item |
| 8 | `{ siteId: 1, dirtyHoldStartAt: -1 }` | No | Time-ordered lists and reports by dirty hold start at |

## Referenced by

u_mes_mast_equipment, u_mes_maint_logbookEntry.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_cleaningRecord.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_cleaningRecord.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_cleaningRecord.js
