# u_mes_sys_controlledDocument

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | Controlled documents and attachments metadata (drawings, certificates, photos, reports); file in object store |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | DOC-<recordNo> |
| Display value used by references | title |
| Keys | 38 (30 required, 8 may be null) |
| Estimated volume per year | ~150,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per controlled document, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with controlledDocumentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_sys_controlledDocumentTag | Value list | tag |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DOC-<recordNo> | `"DOC-DRW-5110-10-0100-D"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"DRW-5110-10-0100-D"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the controlled document; used as its display value in other collections | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 6 | documentTypeId | String | Yes | Reference to u_mes_sys_documentType._id | `"DCT-DRAWING"` | Reference: u_mes_sys_documentType._id |
| 7 | documentTypeName | String | Yes | Display value of documentTypeId, copied from u_mes_sys_documentType.name | `"Drawing"` |  |
| 8 | revision | String | Yes | Revision of the controlled document | `"D"` |  |
| 9 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 10 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_exe_wipUnit"` |  |
| 12 | relatedEntityId | String | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"WU-U260929A0184"` | Reference: Any collection (see relatedCollectionName) |
| 13 | relatedEntityName | String | No (null allowed) | Display value of the related document | `"U260929A0184"` |  |
| 14 | fileName | String | Yes | File name | `"5110-10-0100_revD.pdf"` |  |
| 15 | mimeType | String | Yes | Mime type | `"application/pdf"` |  |
| 16 | sizeBytes | Int64 | Yes | Size bytes | `NumberLong("482113")` |  |
| 17 | storageProvider | String | Yes | Storage provider | `"S3"` | S3; GridFS; File Share |
| 18 | storageKey | String | Yes | Storage key | `"pn1/drawings/5110-10-0100_revD.pdf"` |  |
| 19 | checksumSha256 | String | Yes | Checksum sha256 | `"2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"` |  |
| 20 | languageId | String | Yes | Reference to u_mes_mdm_language._id | `"LNG-en"` | Reference: u_mes_mdm_language._id |
| 21 | languageName | String | Yes | Display value of languageId, copied from u_mes_mdm_language.name | `"English"` |  |
| 22 | authorUserId | String | Yes | Reference to u_mes_mdm_user._id: author user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 23 | authorUserName | String | Yes | Display value of authorUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 24 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 25 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 26 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 27 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 28 | expiresAt | Date | No (null allowed) | Expires date and time | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 29 | retentionYears | Int32 | Yes | Retention (years) | `NumberInt(15)` |  |
| 30 | isControlled | Boolean | Yes | True when the record is controlled | `true` |  |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 34 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 35 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 36 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 37 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 38 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_mdm_skill, u_mes_mdm_skillCertification, u_mes_prd_workInstructionStepMediaControlledDocument, u_mes_prd_engineeringChangeControlledDocument, u_mes_exe_stepCompletion, u_mes_exe_lot, u_mes_mat_packagingSpecification, u_mes_qlt_nonconformancePhotoControlledDocument, u_mes_qlt_capaControlledDocument, u_mes_qlt_ppapSubmissionElement, u_mes_qlt_gaugeCalibration, u_mes_qlt_audit, u_mes_eqp_torqueResult, u_mes_sys_controlledDocumentTag.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_controlledDocument.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_controlledDocument.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_controlledDocument.js
