# u_mes_qual_capaTeamMember

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per team member of a CAPA |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_capa |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Child collection. The parent CAPA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. capaId and capaName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1178000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CAPA-2026-0014-TM01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | capaId | String | Yes | Reference to u_mes_qual_capa._id: the parent document this one belongs to | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 6 | capaName | String | Yes | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | userId | String | Yes | Reference to u_mes_mast_user._id | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 10 | roleInTeam | String | Yes | Role in team | `"Champion"` | Champion; Leader; Member |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 13 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 14 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 15 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 16 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ capaId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capaTeamMember.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capaTeamMember.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_capaTeamMember.js
