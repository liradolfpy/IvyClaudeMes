# u_mes_qual_capaCorrectiveAction

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per corrective action of a CAPA |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_capa |
| _id pattern | <capaId>-CA2<nnn> |
| Display value used by references | description |
| Keys | 18 (18 required, 0 may be null) |

## Structure

Child collection. The parent CAPA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. capaId and capaName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <capaId>-CA2<nnn> | `"CAPA-2026-0014-CA2001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0014-CA2001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | capaId | String | Yes | Reference to u_mes_qual_capa._id: the parent document this one belongs to | `"CAPA-2026-0014"` | Reference: u_mes_qual_capa._id |
| 6 | capaName | String | Yes | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Leak at piston seal"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the CAPA corrective action | `"Enforce tool life interlock on grooving insert at 400 pieces"` |  |
| 9 | ownerUserId | String | Yes | Reference to u_mes_mast_user._id: owner user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 10 | ownerUserName | String | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | dueAt | Date | Yes | Due date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ capaId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capaCorrectiveAction.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capaCorrectiveAction.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_capaCorrectiveAction.js
