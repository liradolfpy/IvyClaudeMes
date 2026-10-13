# u_mes_syst_controlledDocument

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Controlled documents and attachments metadata (drawings, certificates, photos, reports); file in object store |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 39 (31 required, 8 may be null) |
| Estimated volume per year | ~150,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per controlled document, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with controlledDocumentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_controlledDocumentTag | Value list | tag |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1246000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DRW-5110-20-0105-B"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the controlled document; used as its display value in other collections | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 7 | documentTypeId | String | - | Yes | Reference to u_mes_syst_documentType._id | `"1289000000000001"` | Reference: u_mes_syst_documentType._id |
| 8 | documentTypeName | String | - | Yes | Display value of documentTypeId, copied from u_mes_syst_documentType.name | `"Drawing"` |  |
| 9 | revision | String | - | Yes | Revision of the controlled document | `"D"` |  |
| 10 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 11 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 12 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_prod_item"` |  |
| 13 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1043000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 14 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"Front Brake Caliper Assembly, LH"` |  |
| 15 | fileName | String | - | Yes | File name | `"5110-10-0100_revD.pdf"` |  |
| 16 | mimeType | String | - | Yes | Mime type | `"application/pdf"` |  |
| 17 | sizeBytes | Int64 | - | Yes | Size bytes | `NumberLong("482113")` |  |
| 18 | storageProvider | String | - | Yes | Storage provider | `"S3"` | S3; GridFS; File Share |
| 19 | storageKey | String | - | Yes | Storage key | `"pn1/drawings/5110-10-0100_revD.pdf"` |  |
| 20 | checksumSha256 | String | - | Yes | Checksum sha256 | `"2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"` |  |
| 21 | languageId | String | - | Yes | Reference to u_mes_mast_language._id | `"1267000000000001"` | Reference: u_mes_mast_language._id |
| 22 | languageName | String | - | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 23 | authorUserId | String | - | Yes | Reference to u_mes_mast_user._id: author user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 24 | authorUserName | String | - | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 25 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 26 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 27 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 28 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 29 | expiresAt | Date | Datetime | No (null allowed) | Expires date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2027-03-31T23:59:00.000+0000")` |  |
| 30 | retentionYears | Int32 | - | Yes | Retention (years) | `NumberInt(15)` |  |
| 31 | isControlled | Boolean | - | Yes | True when the record is controlled | `true` |  |
| 32 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 33 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 35 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 37 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 38 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ documentTypeId: 1 }` | No | Look-up of documents by document type |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ languageId: 1 }` | No | Look-up of documents by language |
| 6 | `{ authorUserId: 1 }` | No | Look-up of documents by author user |
| 7 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 8 | `{ siteId: 1, approvedAt: -1 }` | No | Time-ordered lists and reports by approved at |

## Referenced by

u_mes_mast_skill, u_mes_mast_skillCertification, u_mes_prod_workInstructionStep, u_mes_prod_workInstructionStepMediaControlledDocument, u_mes_prod_engineeringChangeControlledDocument, u_mes_plan_stepCompletion, u_mes_plan_lot, u_mes_matl_packagingSpecification, u_mes_qual_inspectionResult, u_mes_qual_nonconformancePhotoControlledDocument, u_mes_qual_capaControlledDocument, u_mes_qual_ppapSubmissionElement, u_mes_qual_gaugeCalibration, u_mes_qual_audit, u_mes_perf_torqueResult, u_mes_maint_tool, u_mes_syst_controlledDocumentTag, u_mes_prod_recipeControlledDocument, u_mes_trac_traceInvestigation, u_mes_qual_curveEnvelope, u_mes_qual_measurementCurve, u_mes_qual_defectRecord, u_mes_syst_analyticsModel, u_mes_syst_simulationStudy, u_mes_syst_backupRun, u_mes_syst_systemValidation, u_mes_bmr_batchRelease, u_mes_maint_cleaningRecord, u_mes_qual_productQualityReview, u_mes_qual_processValidation, u_mes_maint_equipmentQualification, u_mes_mmr_masterManufacturingRecord, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_controlledDocument.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_controlledDocument.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_controlledDocument.js
