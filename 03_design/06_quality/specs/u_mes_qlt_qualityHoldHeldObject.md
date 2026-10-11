# u_mes_qlt_qualityHoldHeldObject

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per held object of a quality hold |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qlt_qualityHold |
| _id pattern | <qualityHoldId>-HO<nnn> |
| Display value used by references | recordNo |
| Keys | 20 (18 required, 2 may be null) |

## Structure

Child collection. The parent quality hold can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. qualityHoldId and qualityHoldName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <qualityHoldId>-HO<nnn> | `"HLD-2026-000021-HO001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000021-HO001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | qualityHoldId | String | Yes | Reference to u_mes_qlt_qualityHold._id: the parent document this one belongs to | `"HLD-2026-000021"` | Reference: u_mes_qlt_qualityHold._id |
| 6 | qualityHoldName | String | Yes | Display value of qualityHoldId, copied from u_mes_qlt_qualityHold.recordNo | `"2026-000021"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_exe_wipUnit"` |  |
| 9 | relatedEntityId | String | Yes | _id of the related document in the collection named by relatedCollectionName | `"WU-U260929A0184"` | Reference: Any collection (see relatedCollectionName) |
| 10 | relatedEntityName | String | Yes | Display value of the related document | `"U260929A0184"` |  |
| 11 | quantity | Int32 | Yes | Quantity of the quality hold held object | `NumberInt(1)` |  |
| 12 | releasedAt | Date | No (null allowed) | Date and time when the record was released | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 13 | releaseDecision | String | No (null allowed) | Release decision | `"Released"` | Released; Rework; Scrap; Return To Supplier |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 17 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 18 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 19 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 20 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ qualityHoldId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_qualityHoldHeldObject.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_qualityHoldHeldObject.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_qualityHoldHeldObject.js
