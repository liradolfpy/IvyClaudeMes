# u_mes_qual_processValidation

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Process validation study of an item on a line by lifecycle stage (process design, process qualification, continued process verification), with protocol, lots, acceptance criteria and result. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 34 (22 required, 12 may be null) |
| Estimated volume per year | about 30 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per process validation, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1365000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PVL-2026-001"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title | `"Front caliper LH, assembly line 1, process qualification"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 10 | validationStage | String | - | Yes | Lifecycle stage | `"Stage 2 Process Qualification"` | Stage 1 Process Design; Stage 2 Process Qualification; Stage 3 Continued Process Verification |
| 11 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 12 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 13 | protocolControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: protocol controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 14 | protocolControlledDocumentName | String | - | No (null allowed) | Display value of protocolControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 15 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 16 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 17 | plannedLotCount | Int32 | - | Yes | Lots or orders planned | `NumberInt(3)` |  |
| 18 | executedLotCount | Int32 | - | Yes | Lots or orders executed | `NumberInt(3)` |  |
| 19 | acceptanceCriteriaText | String | - | Yes | Acceptance criteria | `"Cpk >= 1.67 on bleed screw torque and pressure drop; no leak escapes"` |  |
| 20 | resultText | String | - | No (null allowed) | Result | `"Torque Cpk 1.92, pressure drop Cpk 2.10; criteria met"` |  |
| 21 | plannedStartDate | Date | Date | Yes | Planned start date | `ISODate("2026-04-06T00:00:00.000+0000")` |  |
| 22 | completedAt | Date | Datetime | No (null allowed) | Completion time | `ISODate("2026-04-24T17:00:00.000+0000")` |  |
| 23 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 24 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 25 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-04-28T11:00:00.000+0000")` |  |
| 26 | nextReviewDate | Date | Date | No (null allowed) | Date of the next review | `ISODate("2027-04-28T00:00:00.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Planned; In Execution; Completed; Approved; Rejected |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-24T17:00:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-28T11:00:00.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Planned, In Execution, Completed, Approved, Rejected. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 6 | `{ protocolControlledDocumentId: 1 }` | No | Look-up of documents by protocol controlled document |
| 7 | `{ reportControlledDocumentId: 1 }` | No | Look-up of documents by report controlled document |
| 8 | `{ siteId: 1, plannedStartDate: -1 }` | No | Time-ordered lists and reports by planned start date |

## Referenced by

u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_processValidation.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_processValidation.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_processValidation.js
