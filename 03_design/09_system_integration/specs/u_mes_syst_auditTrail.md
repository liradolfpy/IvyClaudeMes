# u_mes_syst_auditTrail

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Field-level change history of master and quality data (who, when, old, new, reason) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 31 (26 required, 5 may be null) |
| Estimated volume per year | ~3 million |
| Storage | standard, immutable |

## Structure

Flat entity collection: one document per audit trail, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with auditTrailId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_auditTrailChange | Child | change |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1241000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ADT-2026-000202"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_qual_characteristic"` |  |
| 7 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1138000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 8 | relatedEntityName | String | - | Yes | Display value of the related document | `"Casting wall thickness at bridge"` |  |
| 9 | changeAction | String | - | Yes | Change action | `"Create"` | Create; Update; Obsolete |
| 10 | changedAt | Date | Datetime | Yes | Date and time when the record was changed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 11 | changedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'changed' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 12 | changedBy | String | - | Yes | Display name of the user in changedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 13 | reasonText | String | - | No (null allowed) | Reason text | `"Replenishment against kanban call"` |  |
| 14 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `"1243000000000001"` | Reference: u_mes_syst_electronicSignature._id |
| 15 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `"SIG-2026-000171"` |  |
| 16 | clientIp | String | - | Yes | Client ip | `"10.21.6.118"` |  |
| 17 | application | String | - | Yes | Application of the audit trail | `"MES Operator Client 1.4.2"` |  |
| 18 | documentVersionBefore | Int32 | - | Yes | Document version before | `NumberInt(4)` |  |
| 19 | documentVersionAfter | Int32 | - | Yes | Document version after | `NumberInt(5)` |  |
| 20 | previousHash | String | - | Yes | Hash of the previous audit entry, forming a tamper-evident chain | `"a3f19c0e55d2b7a48c61e0f3d92b7c4a1e6f08d5b3c2a1908f7e6d5c4b3a2f10"` |  |
| 21 | entryHash | String | - | Yes | Entry hash | `"7b2e41d09c8f3a65e1d4c7b0a9f8e2d3c6b5a4f1e0d9c8b7a6f5e4d3c2b1a0f9"` |  |
| 22 | gxpRelevant | Boolean | - | Yes | True when the entry concerns GMP-relevant data (GMP-04, GMP-05) | `true` |  |
| 23 | auditTrailReviewId | String | - | No (null allowed) | Reference to u_mes_syst_auditTrailReview._id | `null` | Reference: u_mes_syst_auditTrailReview._id |
| 24 | auditTrailReviewName | String | - | No (null allowed) | Display value of auditTrailReviewId, copied from u_mes_syst_auditTrailReview.recordNo | `null` |  |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 27 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 28 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 29 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 30 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 31 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ electronicSignatureId: 1 }` | No | Look-up of documents by electronic signature |
| 3 | `{ auditTrailReviewId: 1 }` | No | Look-up of documents by audit trail review |
| 4 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 5 | `{ siteId: 1, changedAt: -1 }` | No | Time-ordered lists and reports by changed at |
| 6 | `{ relatedCollectionName: 1, relatedEntityId: 1, changedAt: -1 }` | No | Change history of one document |

## Referenced by

u_mes_syst_auditTrailChange.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_auditTrail.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_auditTrail.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_auditTrail.js
