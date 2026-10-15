# u_mes_maint_logbookEntry

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | Chronological use log of a piece of equipment or an area: production, cleaning, maintenance, calibration, line clearance, qualification and idle periods, with the order and lot concerned. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 35 (21 required, 14 may be null) |
| Estimated volume per year | about 40,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per logbook entry, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1355000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LOG-BLS-01-P1-00412"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_mast_equipment"` | u_mes_mast_equipment; u_mes_mast_area |
| 7 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1013000000000018"` | Reference: Any collection (see relatedCollectionName) |
| 8 | relatedEntityName | String | - | Yes | Display value of the related document | `"Alu-PVC Blister Packing Machine"` |  |
| 9 | activityType | String | - | Yes | Activity logged | `"Production"` | Production; Cleaning; Maintenance; Calibration; Line Clearance; Qualification; Idle |
| 10 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000011"` | Reference: u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5B26091"` |  |
| 12 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 13 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 14 | cleaningRecordId | String | - | No (null allowed) | Reference to u_mes_maint_cleaningRecord._id | `null` | Reference: u_mes_maint_cleaningRecord._id |
| 15 | cleaningRecordName | String | - | No (null allowed) | Display value of cleaningRecordId, copied from u_mes_maint_cleaningRecord.recordNo | `null` |  |
| 16 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `null` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 17 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `null` |  |
| 18 | lineClearanceId | String | - | No (null allowed) | Reference to u_mes_plan_lineClearance._id | `null` | Reference: u_mes_plan_lineClearance._id |
| 19 | lineClearanceName | String | - | No (null allowed) | Display value of lineClearanceId, copied from u_mes_plan_lineClearance.recordNo | `null` |  |
| 20 | entryText | String | - | Yes | Logbook text | `"Blister packing of batch PCM5B26091: 4,741 cartons good, 22 rejected"` |  |
| 21 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 22 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 23 | startedAt | Date | Datetime | Yes | Start of the activity | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 24 | completedAt | Date | Datetime | No (null allowed) | End of the activity | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 25 | reviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000015"` | Reference: u_mes_mast_user._id |
| 26 | reviewedBy | String | - | No (null allowed) | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Nilesh Sawant"` |  |
| 27 | reviewedAt | Date | Datetime | No (null allowed) | Time of the review | `ISODate("2026-09-15T14:10:00.000+0000")` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Reviewed"` | Recorded; Reviewed |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 31 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |
| 33 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:10:00.000+0000")` |  |
| 34 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |

## Status values

Recorded, Reviewed. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 5 | `{ cleaningRecordId: 1 }` | No | Look-up of documents by cleaning record |
| 6 | `{ maintenanceWorkOrderId: 1 }` | No | Look-up of documents by maintenance work order |
| 7 | `{ lineClearanceId: 1 }` | No | Look-up of documents by line clearance |
| 8 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 9 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_logbookEntry.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_logbookEntry.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_logbookEntry.js
