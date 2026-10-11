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
| Keys | 27 (24 required, 3 may be null) |
| Estimated volume per year | ~3 million |
| Storage | standard, immutable |

## Structure

Flat entity collection: one document per audit trail, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with auditTrailId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_auditTrailChange | Child | change |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1241000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ADT-2026-000202"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_qual_characteristic"` |  |
| 6 | relatedEntityId | String | Yes | _id of the related document in the collection named by relatedCollectionName | `"1138000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 7 | relatedEntityName | String | Yes | Display value of the related document | `"Casting wall thickness at bridge"` |  |
| 8 | changeAction | String | Yes | Change action | `"Create"` | Create; Update; Obsolete |
| 9 | changedAt | Date | Yes | Date and time when the record was changed | `ISODate("2026-09-15T00:30:30.000+0000")` |  |
| 10 | changedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'changed' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 11 | changedBy | String | Yes | Display name of the user in changedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 12 | reasonText | String | No (null allowed) | Reason text | `"Replenishment against kanban call"` |  |
| 13 | electronicSignatureId | String | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `"1243000000000001"` | Reference: u_mes_syst_electronicSignature._id |
| 14 | electronicSignatureName | String | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `"SIG-2026-000171"` |  |
| 15 | clientIp | String | Yes | Client ip | `"10.21.6.118"` |  |
| 16 | application | String | Yes | Application of the audit trail | `"MES Operator Client 1.4.2"` |  |
| 17 | documentVersionBefore | Int32 | Yes | Document version before | `NumberInt(4)` |  |
| 18 | documentVersionAfter | Int32 | Yes | Document version after | `NumberInt(5)` |  |
| 19 | previousHash | String | Yes | Hash of the previous audit entry, forming a tamper-evident chain | `"a3f19c0e55d2b7a48c61e0f3d92b7c4a1e6f08d5b3c2a1908f7e6d5c4b3a2f10"` |  |
| 20 | entryHash | String | Yes | Entry hash | `"7b2e41d09c8f3a65e1d4c7b0a9f8e2d3c6b5a4f1e0d9c8b7a6f5e4d3c2b1a0f9"` |  |
| 21 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 22 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 23 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 24 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 25 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:30.000+0000")` |  |
| 26 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 27 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ electronicSignatureId: 1 }` | No | Look-up of documents by electronic signature |
| 3 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 4 | `{ siteId: 1, changedAt: -1 }` | No | Time-ordered lists and reports by changed at |
| 5 | `{ relatedCollectionName: 1, relatedEntityId: 1, changedAt: -1 }` | No | Change history of one document |

## Referenced by

u_mes_syst_auditTrailChange.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_auditTrail.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_auditTrail.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_auditTrail.js
