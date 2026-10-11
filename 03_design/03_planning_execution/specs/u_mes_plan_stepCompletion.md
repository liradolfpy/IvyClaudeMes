# u_mes_plan_stepCompletion

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Completion record for each work-instruction step: values entered, confirmations, duration, device data |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | STC-<recordNo> |
| Display value used by references | recordNo |
| Keys | 40 (28 required, 12 may be null) |
| Estimated volume per year | ~20 million |
| Storage | standard, archive after 15 months |

## Structure

Flat entity collection: one document per step completion, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: STC-<recordNo> | `"STC-20260929-000911"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000911"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operationExecutionId | String | Yes | Reference to u_mes_plan_operationExecution._id | `"OPX-20260929-000184"` | Reference: u_mes_plan_operationExecution._id |
| 6 | operationExecutionName | String | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"20260929-000184"` |  |
| 7 | workInstructionId | String | Yes | Reference to u_mes_prod_workInstruction._id | `"WI-WI-OP070-001"` | Reference: u_mes_prod_workInstruction._id |
| 8 | workInstructionName | String | Yes | Display value of workInstructionId, copied from u_mes_prod_workInstruction.title | `"Bleed screw tightening - Front caliper LH"` |  |
| 9 | workInstructionVersion | Int32 | Yes | Work instruction version | `NumberInt(3)` |  |
| 10 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 11 | wipUnitId | String | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260929A0184"` |  |
| 13 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 14 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 15 | userId | String | Yes | Reference to u_mes_mast_user._id | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | userName | String | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 19 | durationSec | Int32 | Yes | Duration (seconds) | `NumberInt(42)` |  |
| 20 | inputType | String | Yes | Input type | `"Confirmation"` | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| 21 | enteredText | String | No (null allowed) | Entered text | `"Seat checked, dry"` |  |
| 22 | enteredNumber | Decimal128 | No (null allowed) | Entered number | `null` |  |
| 23 | enteredFlag | Boolean | Yes | True when: entered flag | `false` |  |
| 24 | scannedCode | String | No (null allowed) | Scanned code | `"5110300040/L260921-BS-003"` |  |
| 25 | withinLimits | Boolean | Yes | True when: within limits | `true` |  |
| 26 | deviceSource | String | No (null allowed) | Device source | `"Nutrunner Controller"` | Manual Entry; Scanner; Nutrunner Controller; Leak Tester; Gauge Interface; PLC |
| 27 | overridden | Boolean | Yes | True when: overridden | `false` |  |
| 28 | overrideById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'override' | `null` | Reference: u_mes_mast_user._id |
| 29 | overrideBy | String | No (null allowed) | Display name of the user in overrideById, copied from u_mes_mast_user.fullName | `null` |  |
| 30 | overrideReason | String | No (null allowed) | Override reason | `null` |  |
| 31 | photoControlledDocumentId | String | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: photo controlled document | `"DOC-PHT-20260929-0031"` | Reference: u_mes_syst_controlledDocument._id |
| 32 | photoControlledDocumentName | String | No (null allowed) | Display value of photoControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Photo, leak at piston seal, unit U260929A0171"` |  |
| 33 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Completed; Skipped; Overridden |
| 34 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 36 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 38 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 39 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_stepCompletion.js
