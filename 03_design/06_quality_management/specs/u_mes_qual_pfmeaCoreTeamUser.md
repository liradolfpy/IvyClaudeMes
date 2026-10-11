# u_mes_qual_pfmeaCoreTeamUser

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one PFMEA to one core team user; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_qual_pfmea |
| _id pattern | <pfmeaId>-CTU<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A PFMEA can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. pfmeaId and pfmeaName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <pfmeaId>-CTU<nnn> | `"FMEA-5110-10-0100-PF-CTU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-PF-CTU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | pfmeaId | String | Yes | Reference to u_mes_qual_pfmea._id: the parent document this one belongs to | `"FMEA-5110-10-0100-PF"` | Reference: u_mes_qual_pfmea._id |
| 6 | pfmeaName | String | Yes | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front Brake Caliper Assembly LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | coreTeamUserId | String | Yes | Reference to u_mes_mast_user._id: core team user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 9 | coreTeamUserName | String | Yes | Display value of coreTeamUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ pfmeaId: 1, coreTeamUserId: 1 }` | Yes | One link per pair |
| 2 | `{ coreTeamUserId: 1, pfmeaId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_pfmeaCoreTeamUser.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_pfmeaCoreTeamUser.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_pfmeaCoreTeamUser.js
