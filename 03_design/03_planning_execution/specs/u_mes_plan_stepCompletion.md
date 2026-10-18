# u_mes_plan_stepCompletion

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Completion record for each work-instruction step: values entered, confirmations, duration, device data |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 44 (29 required, 15 may be null) |
| Estimated volume per year | ~20 million |
| Storage | standard, archive after 15 months |

## Structure

Flat entity collection: one document per step completion, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1093000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"STC-2026-000159"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 8 | workInstructionId | String | - | Yes | Reference to u_mes_prod_workInstruction._id | `"1065000000000006"` | Reference: u_mes_prod_workInstruction._id |
| 9 | workInstructionName | String | - | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Seal, piston and dust boot assembly - Front caliper LH"` |  |
| 10 | workInstructionVersion | Int32 | - | Yes | Work instruction version | `NumberInt(3)` |  |
| 11 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(60)` |  |
| 12 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 13 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 14 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 15 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 16 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 17 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 18 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:07.000+0000")` |  |
| 19 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 20 | durationSec | Int32 | - | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 21 | inputType | String | - | Yes | Input type | `"None"` | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| 22 | enteredText | String | - | No (null allowed) | Entered text | `"Seat checked, dry"` |  |
| 23 | enteredNumber | Decimal128 | - | No (null allowed) | Entered number | `42.0` |  |
| 24 | enteredFlag | Boolean | - | Yes | True when: entered flag | `false` |  |
| 25 | scannedCode | String | - | No (null allowed) | Scanned code | `"5110300040/L260921-BS-003"` |  |
| 26 | withinLimits | Boolean | - | Yes | True when: within limits | `true` |  |
| 27 | deviceSource | String | - | No (null allowed) | Device source | `"Manual Entry"` | Manual Entry; Scanner; Nutrunner Controller; Leak Tester; Gauge Interface; PLC; AR Headset |
| 28 | overridden | Boolean | - | Yes | True when: overridden | `false` |  |
| 29 | overrideById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'override' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | overrideBy | String | - | No (null allowed) | Display name of the user in overrideById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | overrideReason | String | - | No (null allowed) | Override reason | `null` |  |
| 32 | photoControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: photo controlled document | `"1246000000000006"` | Reference: u_mes_syst_controlledDocument._id |
| 33 | photoControlledDocumentName | String | - | No (null allowed) | Display value of photoControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Material certificate, piston lot KPP-260905-07"` |  |
| 34 | overrideReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: override reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 35 | overrideReasonCodeName | String | - | No (null allowed) | Display value of overrideReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 36 | arSessionRef | String | - | No (null allowed) | Reference of the AR session that confirmed the step | `null` |  |
| 37 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Completed; Skipped; Overridden |
| 38 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 39 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:07.000+0000")` |  |
| 40 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 41 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 42 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 43 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Completed, Skipped, Overridden. Initial state: Completed. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ operationExecutionId: 1 }` | No | Look-up of documents by operation execution |
| 4 | `{ workInstructionId: 1 }` | No | Look-up of documents by work instruction |
| 5 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 6 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 7 | `{ userId: 1 }` | No | Look-up of documents by user |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_stepCompletion.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_stepCompletion.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_stepCompletion.js
