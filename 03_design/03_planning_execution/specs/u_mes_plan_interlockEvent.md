# u_mes_plan_interlockEvent

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Every time an interlock rule blocks a transaction, is overridden or is cleared: what was checked, expected and found, and who authorised the override. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 50 (20 required, 30 may be null) |
| Estimated volume per year | about 20,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per interlock event, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1307000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ILK-20260915-00207"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | interlockRuleId | String | - | Yes | Reference to u_mes_syst_interlockRule._id | `"1332000000000009"` | Reference: u_mes_syst_interlockRule._id |
| 6 | interlockRuleName | String | - | Yes | Display value of interlockRuleId, copied from u_mes_syst_interlockRule.name | `"Variant check at piston and seal assembly start"` |  |
| 7 | ruleType | String | - | Yes | Rule type at the time of the event | `"Variant Check"` |  |
| 8 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 10 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 11 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 12 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000002"` | Reference: u_mes_plan_productionOrder._id |
| 13 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000419"` |  |
| 14 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000003"` | Reference: u_mes_plan_wipUnit._id |
| 15 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915B0210"` |  |
| 16 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 17 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 18 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `null` | Reference: u_mes_plan_operationExecution._id |
| 19 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `null` |  |
| 20 | relatedCollectionName | String | - | No (null allowed) | Name of the collection the related document is in | `null` |  |
| 21 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `null` | Reference: Any collection (see relatedCollectionName) |
| 22 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `null` |  |
| 23 | foundValueText | String | - | No (null allowed) | Value found (scan, version, reading) | `"FBC-LH-STD body 5110-20-0110 scanned"` |  |
| 24 | expectedValueText | String | - | No (null allowed) | Value expected | `"FBC-RH-STD body"` |  |
| 25 | messageText | String | - | Yes | Message shown to the operator | `"Scanned body or component does not match the variant of the order"` |  |
| 26 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 27 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 28 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 29 | operatorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: operator user | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 30 | operatorUserName | String | - | No (null allowed) | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 31 | raisedAt | Date | Datetime | Yes | Time the interlock fired | `ISODate("2026-09-15T14:09:00.000+0000")` |  |
| 32 | overrideReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: override reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 33 | overrideReasonCodeName | String | - | No (null allowed) | Display value of overrideReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 34 | overrideComment | String | - | No (null allowed) | Free-text comment on the override | `null` |  |
| 35 | overrideById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'override' | `null` | Reference: u_mes_mast_user._id |
| 36 | overrideBy | String | - | No (null allowed) | Display name of the user in overrideById, copied from u_mes_mast_user.fullName | `null` |  |
| 37 | overrideAt | Date | Datetime | No (null allowed) | Time of the override | `null` |  |
| 38 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 39 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 40 | clearedAt | Date | Datetime | No (null allowed) | Time the condition was cleared without override | `ISODate("2026-09-15T14:16:00.000+0000")` |  |
| 41 | notificationId | String | - | No (null allowed) | Reference to u_mes_syst_notification._id | `null` | Reference: u_mes_syst_notification._id |
| 42 | notificationName | String | - | No (null allowed) | Display value of notificationId, copied from u_mes_syst_notification.title | `null` |  |
| 43 | status | String | - | Yes | Primary lifecycle state of the document | `"Cleared"` | Blocked; Overridden; Cleared; Cancelled |
| 44 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 45 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 46 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 47 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 48 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:16:00.000+0000")` |  |
| 49 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 50 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Blocked, Overridden, Cleared, Cancelled. Initial state: Blocked. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ interlockRuleId: 1 }` | No | Look-up of documents by interlock rule |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 8 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 9 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_syst_notification, u_mes_plan_operatorSession, u_mes_plan_recipeDownload, u_mes_plan_setupVerification.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_interlockEvent.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_interlockEvent.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_interlockEvent.js
