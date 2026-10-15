# u_mes_syst_systemValidation

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | One validation or computer software assurance activity on a computerised system: initial validation, revalidation after a change, or decommissioning, with its test evidence and approval. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 39 (23 required, 16 may be null) |
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
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | computerisedSystemId | String | - | Yes | Reference to u_mes_syst_computerisedSystem._id | `"1344000000000001"` | Reference: u_mes_syst_computerisedSystem._id |
| 7 | computerisedSystemName | String | - | Yes | Display value of computerisedSystemId, copied from u_mes_syst_computerisedSystem.name | `"Manufacturing execution system, Ranjangaon OSD plant"` |  |
| 8 | title | String | - | Yes | Validation title | `"MES release 2.7.0, review by exception, batch release and reconciliation functions"` |  |
| 9 | validationType | String | - | Yes | Kind of validation | `"Change Revalidation"` | Initial Validation; Change Revalidation; Retrospective Validation; Decommissioning |
| 10 | assuranceApproach | String | - | Yes | Main assurance activity, chosen by risk (FDA Computer Software Assurance) | `"Scripted Testing"` | Scripted Testing; Unscripted Testing; Ad Hoc Testing; Supplier Assurance |
| 11 | releaseVersion | String | - | Yes | Software version validated | `"2.7.0"` |  |
| 12 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 13 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 14 | riskAssessmentId | String | - | No (null allowed) | Reference to u_mes_qual_riskAssessment._id | `"1361000000000001"` | Reference: u_mes_qual_riskAssessment._id |
| 15 | riskAssessmentName | String | - | No (null allowed) | Display value of riskAssessmentId, copied from u_mes_qual_riskAssessment.title | `"MES release 2.7.0, validation risk assessment of GMP functions"` |  |
| 16 | protocolControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: protocol controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 17 | protocolControlledDocumentName | String | - | No (null allowed) | Display value of protocolControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 18 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 19 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 20 | testCaseCount | Int32 | - | Yes | Number of test cases or assurance records executed | `NumberInt(186)` |  |
| 21 | testFailedCount | Int32 | - | Yes | Number of failed tests | `NumberInt(3)` |  |
| 22 | openDeviationCount | Int32 | - | Yes | Validation deviations still open | `NumberInt(0)` |  |
| 23 | plannedStartDate | Date | Date | Yes | Planned start date | `ISODate("2026-08-17T00:00:00.000+0000")` |  |
| 24 | startedAt | Date | Datetime | No (null allowed) | Start of execution | `ISODate("2026-08-18T09:00:00.000+0000")` |  |
| 25 | completedAt | Date | Datetime | No (null allowed) | End of execution | `ISODate("2026-09-03T18:00:00.000+0000")` |  |
| 26 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 27 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 28 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-05T11:00:00.000+0000")` |  |
| 29 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 30 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 31 | conclusionText | String | - | No (null allowed) | Conclusion of the validation report | `"186 test cases executed; 3 failures in report layout corrected and retested; release fit for intended use"` |  |
| 32 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Planned; In Execution; Executed; Approved; Rejected |
| 33 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-08-18T09:00:00.000+0000")` |  |
| 35 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 37 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-05T11:00:00.000+0000")` |  |
| 38 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |

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
