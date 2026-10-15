# u_mes_plan_interlockEvent

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Every time an interlock rule blocks a transaction, is overridden or is cleared: what was checked, expected and found, and who authorised the override. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 51 (21 required, 30 may be null) |
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
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | interlockRuleId | String | - | Yes | Reference to u_mes_syst_interlockRule._id | `"1332000000000009"` | Reference: u_mes_syst_interlockRule._id |
| 7 | interlockRuleName | String | - | Yes | Display value of interlockRuleId, copied from u_mes_syst_interlockRule.name | `"Variant check at piston and seal assembly start"` |  |
| 8 | ruleType | String | - | Yes | Rule type at the time of the event | `"Variant Check"` |  |
| 9 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 11 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 12 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 13 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000002"` | Reference: u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000419"` |  |
| 15 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000003"` | Reference: u_mes_plan_wipUnit._id |
| 16 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915B0210"` |  |
| 17 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 18 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 19 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `null` | Reference: u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `null` |  |
| 21 | relatedCollectionName | String | - | No (null allowed) | Name of the collection the related document is in | `null` |  |
| 22 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `null` | Reference: Any collection (see relatedCollectionName) |
| 23 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `null` |  |
| 24 | foundValueText | String | - | No (null allowed) | Value found (scan, version, reading) | `"FBC-LH-STD body 5110-20-0110 scanned"` |  |
| 25 | expectedValueText | String | - | No (null allowed) | Value expected | `"FBC-RH-STD body"` |  |
| 26 | messageText | String | - | Yes | Message shown to the operator | `"Scanned body or component does not match the variant of the order"` |  |
| 27 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 28 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 29 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 30 | operatorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: operator user | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 31 | operatorUserName | String | - | No (null allowed) | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 32 | raisedAt | Date | Datetime | Yes | Time the interlock fired | `ISODate("2026-09-15T14:09:00.000+0000")` |  |
| 33 | overrideReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: override reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 34 | overrideReasonCodeName | String | - | No (null allowed) | Display value of overrideReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 35 | overrideComment | String | - | No (null allowed) | Free-text comment on the override | `null` |  |
| 36 | overrideById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'override' | `null` | Reference: u_mes_mast_user._id |
| 37 | overrideBy | String | - | No (null allowed) | Display name of the user in overrideById, copied from u_mes_mast_user.fullName | `null` |  |
| 38 | overrideAt | Date | Datetime | No (null allowed) | Time of the override | `null` |  |
| 39 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 40 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 41 | clearedAt | Date | Datetime | No (null allowed) | Time the condition was cleared without override | `ISODate("2026-09-15T14:16:00.000+0000")` |  |
| 42 | notificationId | String | - | No (null allowed) | Reference to u_mes_syst_notification._id | `null` | Reference: u_mes_syst_notification._id |
| 43 | notificationName | String | - | No (null allowed) | Display value of notificationId, copied from u_mes_syst_notification.title | `null` |  |
| 44 | status | String | - | Yes | Primary lifecycle state of the document | `"Cleared"` | Blocked; Overridden; Cleared; Cancelled |
| 45 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 46 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 47 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 48 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 49 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:16:00.000+0000")` |  |
| 50 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 51 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
