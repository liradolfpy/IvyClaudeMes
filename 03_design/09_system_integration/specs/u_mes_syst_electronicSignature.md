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
| Keys | 29 (26 required, 3 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_prod_recipe"` |  |
| 6 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1073000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 7 | relatedEntityName | String | - | Yes | Display value of the related document | `"Caliper body LH casting parameters"` |  |
| 8 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 10 | roleId | String | - | Yes | Reference to u_mes_mast_role._id | `"1026000000000001"` | Reference: u_mes_mast_role._id |
| 11 | roleName | String | - | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 12 | signatureMeaningId | String | - | Yes | Reference to u_mes_mast_signatureMeaning._id | `"1264000000000001"` | Reference: u_mes_mast_signatureMeaning._id |
| 13 | signatureMeaningName | String | - | Yes | Display value of signatureMeaningId, copied from u_mes_mast_signatureMeaning.name | `"Approved"` |  |
| 14 | signedAt | Date | Datetime | Yes | Date and time when the record was signed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 15 | authenticationMethod | String | - | Yes | Authentication method | `"Password"` | Password; Password And Badge; Single Sign On |
| 16 | contentHash | String | - | Yes | Content hash | `"d0c1b2a3948576e5f4d3c2b1a0f9e8d7c6b5a4938271605f4e3d2c1b0a9f8e7d"` |  |
| 17 | comment | String | - | No (null allowed) | Comment of the electronic signature | `"Verified against customer drawing revision D"` |  |
| 18 | clientIp | String | - | Yes | Client ip | `"10.21.6.118"` |  |
| 19 | workstation | String | - | Yes | Workstation of the electronic signature | `"PN1-ASY-HMI-07"` |  |
| 20 | isSecondSignature | Boolean | - | Yes | True when the record is second signature | `false` |  |
| 21 | witnessUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: witness user | `null` | Reference: u_mes_mast_user._id |
| 22 | witnessUserName | String | - | No (null allowed) | Display value of witnessUserId, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 24 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 25 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 26 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 27 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 28 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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

u_mes_syst_auditTrail.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_electronicSignature.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_electronicSignature.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_electronicSignature.js
