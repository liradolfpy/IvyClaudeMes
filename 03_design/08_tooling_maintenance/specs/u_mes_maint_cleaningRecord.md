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
| Keys | 37 (24 required, 13 may be null) |
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
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000012"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Rapid Mixer Granulator 600 L"` |  |
| 8 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000012"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Rapid Mixer Granulator Suite 1"` |  |
| 10 | cleaningType | String | - | Yes | Kind of cleaning | `"Major Cleaning"` | Minor Cleaning; Major Cleaning; Product Changeover Cleaning; Bath Change |
| 11 | procedureControlledDocumentId | String | - | Yes | Reference to u_mes_syst_controlledDocument._id: procedure controlled document | `"1246000000000012"` | Reference: u_mes_syst_controlledDocument._id |
| 12 | procedureControlledDocumentName | String | - | Yes | Display value of procedureControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"SOP cleaning of rapid mixer granulator SOP-PRD-014 revision 6"` |  |
| 13 | previousProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: previous production order | `"1083000000000014"` | Reference: u_mes_plan_productionOrder._id |
| 14 | previousProductionOrderName | String | - | No (null allowed) | Display value of previousProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5G26091"` |  |
| 15 | previousItemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id: previous item | `"1043000000000014"` | Reference: u_mes_prod_item._id |
| 16 | previousItemName | String | - | No (null allowed) | Display value of previousItemId, copied from u_mes_prod_item.description | `"Paracetamol 500 mg lubricated granules and core tablets, bulk"` |  |
| 17 | dirtyHoldStartAt | Date | Datetime | No (null allowed) | End of use: start of the dirty hold time | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 18 | startedAt | Date | Datetime | Yes | Start of cleaning | `ISODate("2026-09-15T13:41:00.000+0000")` |  |
| 19 | completedAt | Date | Datetime | No (null allowed) | End of cleaning | `ISODate("2026-09-15T13:44:00.000+0000")` |  |
| 20 | cleanedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'cleaned' | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 21 | cleanedBy | String | - | Yes | Display name of the user in cleanedById, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 22 | verificationMethod | String | - | Yes | How cleanliness is verified | `"Rinse Sample"` | Visual Inspection; Cleanliness Test; Rinse Sample; Swab Sample |
| 23 | verificationResult | String | - | No (null allowed) | Verification result; null until verified | `"Pass"` | Pass; Fail |
| 24 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000015"` | Reference: u_mes_mast_user._id |
| 25 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Nilesh Sawant"` |  |
| 26 | verifiedAt | Date | Datetime | No (null allowed) | Time of verification | `ISODate("2026-09-15T13:45:00.000+0000")` |  |
| 27 | cleanHoldExpiresAt | Date | Datetime | No (null allowed) | End of the validated clean hold time | `ISODate("2026-09-16T13:45:00.000+0000")` |  |
| 28 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 29 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | In Progress; Completed; Verified; Expired; Rejected |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 32 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 33 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 34 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |
| 35 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T13:45:00.000+0000")` |  |
| 36 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 37 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |

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
