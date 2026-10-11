# u_mes_qual_capaImplementationAction

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per implementation action of a CAPA |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_capa |
| _id pattern | <capaId>-IA<nnn> |
| Display value used by references | description |
| Keys | 19 (16 required, 3 may be null) |

## Structure

Child collection. The parent CAPA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. capaId and capaName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <capaId>-IA<nnn> | `"CAPA-2026-0014-IA001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0014-IA001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | capaId | String | Yes | Reference to u_mes_qual_capa._id: the parent document this one belongs to | `"CAPA-2026-0014"` | Reference: u_mes_qual_capa._id |
| 6 | capaName | String | Yes | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Leak at piston seal"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the CAPA implementation action | `"Tool life counter activated on HMC-01 and verified over 2,000 pieces"` |  |
| 9 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 10 | verifiedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 11 | verifiedBy | String | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 12 | effective | Boolean | Yes | True when: effective | `true` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ capaId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capaImplementationAction.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capaImplementationAction.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_capaImplementationAction.js
