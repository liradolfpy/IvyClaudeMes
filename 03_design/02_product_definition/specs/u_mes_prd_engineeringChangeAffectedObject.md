# u_mes_prd_engineeringChangeAffectedObject

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per affected object of a engineering change |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_prd_engineeringChange |
| _id pattern | <engineeringChangeId>-AO<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (18 required, 0 may be null) |

## Structure

Child collection. The parent engineering change can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. engineeringChangeId and engineeringChangeName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <engineeringChangeId>-AO<nnn> | `"ECN-2026-0031-AO001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0031-AO001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | engineeringChangeId | String | Yes | Reference to u_mes_prd_engineeringChange._id: the parent document this one belongs to | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String | Yes | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_exe_wipUnit"` |  |
| 9 | relatedEntityId | String | Yes | _id of the related document in the collection named by relatedCollectionName | `"WU-U260929A0184"` | Reference: Any collection (see relatedCollectionName) |
| 10 | relatedEntityName | String | Yes | Display value of the related document | `"U260929A0184"` |  |
| 11 | changeAction | String | Yes | Change action | `"Update"` | Create; Update; Obsolete |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ engineeringChangeId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_engineeringChangeAffectedObject.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_engineeringChangeAffectedObject.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_engineeringChangeAffectedObject.js
