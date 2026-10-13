# u_mes_qual_pfmeaCoreTeamUser

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one PFMEA to one core team user; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_qual_pfmea |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Relationship collection. A PFMEA can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. pfmeaId and pfmeaName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1184000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PF-5110-10-0100-R01-CTU01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | pfmeaId | String | - | Yes | Reference to u_mes_qual_pfmea._id: the parent document this one belongs to | `"1183000000000001"` | Reference: u_mes_qual_pfmea._id |
| 7 | pfmeaName | String | - | Yes | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | coreTeamUserId | String | - | Yes | Reference to u_mes_mast_user._id: core team user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 10 | coreTeamUserName | String | - | Yes | Display value of coreTeamUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_pfmeaCoreTeamUser.js
