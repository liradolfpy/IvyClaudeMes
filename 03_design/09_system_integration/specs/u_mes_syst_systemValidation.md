# u_mes_syst_systemValidation

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One validation or computer software assurance activity on a computerised system: initial validation, revalidation after a change, or decommissioning, with its test evidence and approval. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 38 (22 required, 16 may be null) |
| Estimated volume per year | about 40 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per system validation, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1345000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CSV-2026-011"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | computerisedSystemId | String | - | Yes | Reference to u_mes_syst_computerisedSystem._id | `"1344000000000001"` | Reference: u_mes_syst_computerisedSystem._id |
| 6 | computerisedSystemName | String | - | Yes | Display value of computerisedSystemId, copied from u_mes_syst_computerisedSystem.name | `"Manufacturing execution system, Chakan plant"` |  |
| 7 | title | String | - | Yes | Validation title | `"MES release 2.7.0, batch record review, release and reconciliation functions"` |  |
| 8 | validationType | String | - | Yes | Kind of validation | `"Change Revalidation"` | Initial Validation; Change Revalidation; Retrospective Validation; Decommissioning |
| 9 | assuranceApproach | String | - | Yes | Main assurance activity, chosen by risk (FDA Computer Software Assurance) | `"Scripted Testing"` | Scripted Testing; Unscripted Testing; Ad Hoc Testing; Supplier Assurance |
| 10 | releaseVersion | String | - | Yes | Software version validated | `"2.7.0"` |  |
| 11 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 12 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 13 | riskAssessmentId | String | - | No (null allowed) | Reference to u_mes_qual_riskAssessment._id | `"1361000000000001"` | Reference: u_mes_qual_riskAssessment._id |
| 14 | riskAssessmentName | String | - | No (null allowed) | Display value of riskAssessmentId, copied from u_mes_qual_riskAssessment.title | `"MES release 2.7.0, validation risk assessment of GMP functions"` |  |
| 15 | protocolControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: protocol controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 16 | protocolControlledDocumentName | String | - | No (null allowed) | Display value of protocolControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 17 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 18 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 19 | testCaseCount | Int32 | - | Yes | Number of test cases or assurance records executed | `NumberInt(186)` |  |
| 20 | testFailedCount | Int32 | - | Yes | Number of failed tests | `NumberInt(3)` |  |
| 21 | openDeviationCount | Int32 | - | Yes | Validation deviations still open | `NumberInt(0)` |  |
| 22 | plannedStartDate | Date | Date | Yes | Planned start date | `ISODate("2026-08-17T00:00:00.000+0000")` |  |
| 23 | startedAt | Date | Datetime | No (null allowed) | Start of execution | `ISODate("2026-08-18T09:00:00.000+0000")` |  |
| 24 | completedAt | Date | Datetime | No (null allowed) | End of execution | `ISODate("2026-09-03T18:00:00.000+0000")` |  |
| 25 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 26 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 27 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-05T11:00:00.000+0000")` |  |
| 28 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 29 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 30 | conclusionText | String | - | No (null allowed) | Conclusion of the validation report | `"186 test cases executed; 3 failures in report layout corrected and retested; release fit for intended use"` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Planned; In Execution; Executed; Approved; Rejected |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-08-18T09:00:00.000+0000")` |  |
| 34 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 36 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-05T11:00:00.000+0000")` |  |
| 37 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, In Execution, Executed, Approved, Rejected. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ computerisedSystemId: 1 }` | No | Look-up of documents by computerised system |
| 4 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 5 | `{ riskAssessmentId: 1 }` | No | Look-up of documents by risk assessment |
| 6 | `{ protocolControlledDocumentId: 1 }` | No | Look-up of documents by protocol controlled document |
| 7 | `{ reportControlledDocumentId: 1 }` | No | Look-up of documents by report controlled document |
| 8 | `{ siteId: 1, plannedStartDate: -1 }` | No | Time-ordered lists and reports by planned start date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_systemValidation.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_systemValidation.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_systemValidation.js
