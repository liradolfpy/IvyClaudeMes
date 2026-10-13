# u_mes_syst_electronicSignature

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Signature records for approvals and releases with meaning and signed-content hash |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 33 (29 required, 4 may be null) |
| Estimated volume per year | ~200,000 |
| Storage | standard, immutable |

## Structure

Flat entity collection: one document per electronic signature, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1243000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SIG-2026-000171"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_prod_recipe"` |  |
| 7 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1073000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 8 | relatedEntityName | String | - | Yes | Display value of the related document | `"Caliper body LH casting parameters"` |  |
| 9 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 10 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 11 | roleId | String | - | Yes | Reference to u_mes_mast_role._id | `"1026000000000001"` | Reference: u_mes_mast_role._id |
| 12 | roleName | String | - | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 13 | signatureMeaningId | String | - | Yes | Reference to u_mes_mast_signatureMeaning._id | `"1264000000000001"` | Reference: u_mes_mast_signatureMeaning._id |
| 14 | signatureMeaningName | String | - | Yes | Display value of signatureMeaningId, copied from u_mes_mast_signatureMeaning.name | `"Approved"` |  |
| 15 | signedAt | Date | Datetime | Yes | Date and time when the record was signed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 16 | authenticationMethod | String | - | Yes | Authentication method | `"Password"` | Password; Password And Badge; Single Sign On |
| 17 | contentHash | String | - | Yes | Content hash | `"d0c1b2a3948576e5f4d3c2b1a0f9e8d7c6b5a4938271605f4e3d2c1b0a9f8e7d"` |  |
| 18 | comment | String | - | No (null allowed) | Comment of the electronic signature | `"Verified against customer drawing revision D"` |  |
| 19 | clientIp | String | - | Yes | Client ip | `"10.21.6.118"` |  |
| 20 | workstation | String | - | Yes | Workstation of the electronic signature | `"PN1-ASY-HMI-07"` |  |
| 21 | isSecondSignature | Boolean | - | Yes | True when the record is second signature | `false` |  |
| 22 | witnessUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: witness user | `null` | Reference: u_mes_mast_user._id |
| 23 | witnessUserName | String | - | No (null allowed) | Display value of witnessUserId, copied from u_mes_mast_user.fullName | `null` |  |
| 24 | signatureManifestationText | String | - | Yes | Printed name, date and time and meaning shown with the signed record (GMP-06) | `"Sunil Jadhav, 15 Sep 2026 06:00 IST, Approved"` |  |
| 25 | signedRecordVersion | Int32 | - | No (null allowed) | Version of the record that was signed | `NumberInt(3)` |  |
| 26 | isFirstSigningInSession | Boolean | - | Yes | True when both signature components were entered (first signing of a session) | `true` |  |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ userId: 1 }` | No | Look-up of documents by user |
| 3 | `{ roleId: 1 }` | No | Look-up of documents by role |
| 4 | `{ signatureMeaningId: 1 }` | No | Look-up of documents by signature meaning |
| 5 | `{ witnessUserId: 1 }` | No | Look-up of documents by witness user |
| 6 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 7 | `{ siteId: 1, signedAt: -1 }` | No | Time-ordered lists and reports by signed at |

## Referenced by

u_mes_qual_qualityHold, u_mes_syst_auditTrail, u_mes_plan_documentAcknowledgement, u_mes_plan_interlockEvent, u_mes_syst_systemValidation, u_mes_syst_auditTrailReview, u_mes_bmr_batchRecordReview, u_mes_bmr_batchRelease, u_mes_plan_lineClearance, u_mes_maint_cleaningRecord, u_mes_maint_equipmentQualification.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_electronicSignature.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_electronicSignature.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_electronicSignature.js
