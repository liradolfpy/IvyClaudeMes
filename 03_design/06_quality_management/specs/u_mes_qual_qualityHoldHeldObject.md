# u_mes_qual_qualityHoldHeldObject

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per held object of a quality hold |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_qualityHold |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 21 (19 required, 2 may be null) |

## Structure

Child collection. The parent quality hold can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. qualityHoldId and qualityHoldName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1173000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"HLD-2026-000021-HO01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | qualityHoldId | String | - | Yes | Reference to u_mes_qual_qualityHold._id: the parent document this one belongs to | `"1172000000000001"` | Reference: u_mes_qual_qualityHold._id |
| 7 | qualityHoldName | String | - | Yes | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000021"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_lot"` |  |
| 10 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1096000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | Yes | Display value of the related document | `"L260915-GDC-014"` |  |
| 12 | quantity | Int32 | - | Yes | Quantity of the quality hold held object | `NumberInt(1)` |  |
| 13 | releasedAt | Date | Datetime | No (null allowed) | Date and time when the record was released. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:29:10.000+0000")` |  |
| 14 | releaseDecision | String | - | No (null allowed) | Release decision | `null` | Released; Rework; Scrap; Return To Supplier |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 16 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:28:40.000+0000")` |  |
| 17 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:29:10.000+0000")` |  |
| 20 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ qualityHoldId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_qualityHoldHeldObject.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_qualityHoldHeldObject.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_qualityHoldHeldObject.js
