# u_mes_maint_logbookEntry

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Chronological use log of a piece of equipment or an area: production, cleaning, maintenance, calibration, line clearance, qualification and idle periods, with the order and lot concerned. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (20 required, 14 may be null) |
| Estimated volume per year | about 40,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per logbook entry, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1355000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LOG-ASY-01-P1-00412"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_mast_equipment"` | u_mes_mast_equipment; u_mes_mast_area |
| 6 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1013000000000006"` | Reference: Any collection (see relatedCollectionName) |
| 7 | relatedEntityName | String | - | Yes | Display value of the related document | `"Piston Assembly Press 1"` |  |
| 8 | activityType | String | - | Yes | Activity logged | `"Production"` | Production; Cleaning; Maintenance; Calibration; Line Clearance; Qualification; Idle |
| 9 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 11 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 12 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 13 | cleaningRecordId | String | - | No (null allowed) | Reference to u_mes_maint_cleaningRecord._id | `null` | Reference: u_mes_maint_cleaningRecord._id |
| 14 | cleaningRecordName | String | - | No (null allowed) | Display value of cleaningRecordId, copied from u_mes_maint_cleaningRecord.recordNo | `null` |  |
| 15 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `null` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 16 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `null` |  |
| 17 | lineClearanceId | String | - | No (null allowed) | Reference to u_mes_plan_lineClearance._id | `null` | Reference: u_mes_plan_lineClearance._id |
| 18 | lineClearanceName | String | - | No (null allowed) | Display value of lineClearanceId, copied from u_mes_plan_lineClearance.recordNo | `null` |  |
| 19 | entryText | String | - | Yes | Logbook text | `"Piston press-in for PO-1000412: 474 good, 2 rejected"` |  |
| 20 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 21 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 22 | startedAt | Date | Datetime | Yes | Start of the activity | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 23 | completedAt | Date | Datetime | No (null allowed) | End of the activity | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 24 | reviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 25 | reviewedBy | String | - | No (null allowed) | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 26 | reviewedAt | Date | Datetime | No (null allowed) | Time of the review | `ISODate("2026-09-15T14:10:00.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Reviewed"` | Recorded; Reviewed |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:10:00.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

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
