# u_mes_maint_equipmentQualification

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | Qualification of a piece of equipment by phase (design, installation, operational, performance, periodic requalification), with protocol, tests, deviations, approval and the next requalification date. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 35 (21 required, 14 may be null) |
| Estimated volume per year | about 80 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per equipment qualification, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1366000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EQQ-BLS-01-P1-PQ-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000018"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Alu-PVC Blister Packing Machine"` |  |
| 8 | qualificationPhase | String | - | Yes | Phase | `"Performance Qualification"` | Design Qualification; Installation Qualification; Operational Qualification; Performance Qualification; Periodic Requalification |
| 9 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000014"` | Reference: u_mes_prod_engineeringChange._id |
| 10 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Blister foil supplier changed"` |  |
| 11 | protocolControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: protocol controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 12 | protocolControlledDocumentName | String | - | No (null allowed) | Display value of protocolControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 13 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 14 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 15 | testCaseCount | Int32 | - | Yes | Tests executed | `NumberInt(18)` |  |
| 16 | testFailedCount | Int32 | - | Yes | Tests failed | `NumberInt(0)` |  |
| 17 | openDeviationCount | Int32 | - | Yes | Deviations still open | `NumberInt(0)` |  |
| 18 | executedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'executed' | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 19 | executedBy | String | - | Yes | Display name of the user in executedById, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |
| 20 | startedAt | Date | Datetime | No (null allowed) | Start of execution | `ISODate("2026-06-10T08:00:00.000+0000")` |  |
| 21 | completedAt | Date | Datetime | No (null allowed) | End of execution | `ISODate("2026-06-12T17:00:00.000+0000")` |  |
| 22 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 23 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 24 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-06-15T11:00:00.000+0000")` |  |
| 25 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 26 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 27 | requalificationDueDate | Date | Date | No (null allowed) | Date the next requalification is due | `ISODate("2027-06-15T00:00:00.000+0000")` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Planned; In Execution; Passed; Failed; Approved |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-06-10T08:00:00.000+0000")` |  |
| 31 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |
| 33 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-06-15T11:00:00.000+0000")` |  |
| 34 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000016"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Farhan Qureshi"` |  |

## Status values

Planned, In Execution, Passed, Failed, Approved. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 5 | `{ protocolControlledDocumentId: 1 }` | No | Look-up of documents by protocol controlled document |
| 6 | `{ reportControlledDocumentId: 1 }` | No | Look-up of documents by report controlled document |
| 7 | `{ electronicSignatureId: 1 }` | No | Look-up of documents by electronic signature |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_equipmentQualification.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_equipmentQualification.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_equipmentQualification.js
