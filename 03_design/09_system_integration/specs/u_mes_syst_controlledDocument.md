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
| Keys | 38 (30 required, 8 may be null) |
| Estimated volume per year | ~150,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per controlled document, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with controlledDocumentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_controlledDocumentTag | Value list | tag |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1246000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"DRW-5110-20-0105-B"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the controlled document; used as its display value in other collections | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 6 | documentTypeId | String | Yes | Reference to u_mes_syst_documentType._id | `"1289000000000001"` | Reference: u_mes_syst_documentType._id |
| 7 | documentTypeName | String | Yes | Display value of documentTypeId, copied from u_mes_syst_documentType.name | `"Drawing"` |  |
| 8 | revision | String | Yes | Revision of the controlled document | `"D"` |  |
| 9 | itemId | String | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 11 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_prod_item"` |  |
| 12 | relatedEntityId | String | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1043000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 13 | relatedEntityName | String | No (null allowed) | Display value of the related document | `"Front Brake Caliper Assembly, LH"` |  |
| 14 | fileName | String | Yes | File name | `"5110-10-0100_revD.pdf"` |  |
| 15 | mimeType | String | Yes | Mime type | `"application/pdf"` |  |
| 16 | sizeBytes | Int64 | Yes | Size bytes | `NumberLong("482113")` |  |
| 17 | storageProvider | String | Yes | Storage provider | `"S3"` | S3; GridFS; File Share |
| 18 | storageKey | String | Yes | Storage key | `"pn1/drawings/5110-10-0100_revD.pdf"` |  |
| 19 | checksumSha256 | String | Yes | Checksum sha256 | `"2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"` |  |
| 20 | languageId | String | Yes | Reference to u_mes_mast_language._id | `"1267000000000001"` | Reference: u_mes_mast_language._id |
| 21 | languageName | String | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 22 | authorUserId | String | Yes | Reference to u_mes_mast_user._id: author user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 23 | authorUserName | String | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 24 | approvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 25 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 26 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `null` |  |
| 27 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 28 | expiresAt | Date | No (null allowed) | Expires date and time | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 29 | retentionYears | Int32 | Yes | Retention (years) | `NumberInt(15)` |  |
| 30 | isControlled | Boolean | Yes | True when the record is controlled | `true` |  |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 34 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 36 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 37 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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

u_mes_mast_skill, u_mes_mast_skillCertification, u_mes_prod_workInstructionStepMediaControlledDocument, u_mes_prod_engineeringChangeControlledDocument, u_mes_plan_stepCompletion, u_mes_plan_lot, u_mes_matl_packagingSpecification, u_mes_qual_nonconformancePhotoControlledDocument, u_mes_qual_capaControlledDocument, u_mes_qual_ppapSubmissionElement, u_mes_qual_gaugeCalibration, u_mes_qual_audit, u_mes_perf_torqueResult, u_mes_syst_controlledDocumentTag.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_controlledDocument.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_controlledDocument.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_controlledDocument.js
