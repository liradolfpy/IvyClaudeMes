# u_mes_plan_setupVerification

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Pre-start verification of the set-up of a station or machine against the order, variant and bill of process. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (24 required, 8 may be null) |
| Estimated volume per year | about 3,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per setup verification, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with setupVerificationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_setupVerificationItem | Child | item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1309000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SUV-20260915-00012"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 7 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 9 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 11 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 13 | changeoverId | String | - | No (null allowed) | Reference to u_mes_plan_changeover._id | `null` | Reference: u_mes_plan_changeover._id |
| 14 | changeoverName | String | - | No (null allowed) | Display value of changeoverId, copied from u_mes_plan_changeover.recordNo | `null` |  |
| 15 | billOfProcessId | String | - | Yes | Reference to u_mes_prod_billOfProcess._id | `"1057000000000001"` | Reference: u_mes_prod_billOfProcess._id |
| 16 | billOfProcessName | String | - | Yes | Display value of billOfProcessId, copied from u_mes_prod_billOfProcess.recordNo | `"BOP-5110-10-0100-R01"` |  |
| 17 | trigger | String | - | Yes | Reason for the verification | `"Order Start"` | Order Start; Changeover; Shift Start; After Maintenance |
| 18 | itemCount | Int32 | - | Yes | Number of checks | `NumberInt(3)` |  |
| 19 | failedCount | Int32 | - | Yes | Number of failed checks | `NumberInt(0)` |  |
| 20 | verifiedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 21 | verifiedBy | String | - | Yes | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 22 | verifiedAt | Date | Datetime | Yes | Completion time | `ISODate("2026-09-15T05:48:00.000+0000")` |  |
| 23 | interlockEventId | String | - | No (null allowed) | Reference to u_mes_plan_interlockEvent._id | `null` | Reference: u_mes_plan_interlockEvent._id |
| 24 | interlockEventName | String | - | No (null allowed) | Display value of interlockEventId, copied from u_mes_plan_interlockEvent.recordNo | `null` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Passed"` | In Progress; Passed; Failed; Overridden |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:48:00.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:48:00.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

In Progress, Passed, Failed, Overridden. Initial state: In Progress. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 7 | `{ changeoverId: 1 }` | No | Look-up of documents by changeover |
| 8 | `{ siteId: 1, verifiedAt: -1 }` | No | Time-ordered lists and reports by verified at |

## Referenced by

u_mes_plan_setupVerificationItem.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_setupVerification.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_setupVerification.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_setupVerification.js
