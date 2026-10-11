# u_mes_qual_auditAuditorUser

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one audit to one auditor user; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qual_audit |
| _id pattern | <auditId>-AU<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A audit can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. auditId and auditName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <auditId>-AU<nnn> | `"AUD-LPA-2026-0931-AU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LPA-2026-0931-AU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | auditId | String | Yes | Reference to u_mes_qual_audit._id: the parent document this one belongs to | `"AUD-LPA-2026-0931"` | Reference: u_mes_qual_audit._id |
| 6 | auditName | String | Yes | Display value of auditId, copied from u_mes_qual_audit.title | `"Layered process audit, Assembly line 1, week 40"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | auditorUserId | String | Yes | Reference to u_mes_mast_user._id: auditor user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 9 | auditorUserName | String | Yes | Display value of auditorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ auditId: 1, auditorUserId: 1 }` | Yes | One link per pair |
| 2 | `{ auditorUserId: 1, auditId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_auditAuditorUser.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_auditAuditorUser.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_auditAuditorUser.js
