# u_mes_syst_backupRun

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Evidence of database backups and restore tests with measured recovery time (optional). |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 24 (18 required, 6 may be null) |
| Estimated volume per year | about 800 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per backup run, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1342000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BKP-20260915-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | runType | String | - | Yes | Run type | `"Incremental Backup"` | Full Backup; Incremental Backup; Restore Test; Failover Test |
| 7 | startedAt | Date | Datetime | Yes | Start | `ISODate("2026-09-15T01:00:00.000+0000")` |  |
| 8 | completedAt | Date | Datetime | No (null allowed) | End | `ISODate("2026-09-15T01:18:00.000+0000")` |  |
| 9 | sizeBytes | Int64 | - | No (null allowed) | Backup size | `NumberLong("6100000000")` |  |
| 10 | storageTarget | String | - | Yes | Target storage | `"NAS-PN1-BK01"` |  |
| 11 | recoveryTimeMinutes | Int32 | - | No (null allowed) | Measured recovery time (restore tests) | `null` |  |
| 12 | recoveryPointMinutes | Int32 | - | No (null allowed) | Data loss window (restore tests) | `null` |  |
| 13 | evidenceControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: evidence controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 14 | evidenceControlledDocumentName | String | - | No (null allowed) | Display value of evidenceControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 15 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 16 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 17 | status | String | - | Yes | Primary lifecycle state of the document | `"Succeeded"` | Running; Succeeded; Failed |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T01:00:00.000+0000")` |  |
| 20 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 22 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T01:18:00.000+0000")` |  |
| 23 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Running, Succeeded, Failed. Initial state: Running. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ evidenceControlledDocumentId: 1 }` | No | Look-up of documents by evidence controlled document |
| 4 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_backupRun.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_backupRun.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_backupRun.js
