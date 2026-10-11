# u_mes_qual_controlPlanCoreTeamUser

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one control plan to one core team user; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_qual_controlPlan |
| _id pattern | <controlPlanId>-CTU<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A control plan can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. controlPlanId and controlPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <controlPlanId>-CTU<nnn> | `"CP-5110-10-0100-PROD-CTU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-PROD-CTU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | controlPlanId | String | Yes | Reference to u_mes_qual_controlPlan._id: the parent document this one belongs to | `"CP-5110-10-0100-PROD"` | Reference: u_mes_qual_controlPlan._id |
| 6 | controlPlanName | String | Yes | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"5110-10-0100-PROD"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | coreTeamUserId | String | Yes | Reference to u_mes_mast_user._id: core team user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 9 | coreTeamUserName | String | Yes | Display value of coreTeamUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ controlPlanId: 1, coreTeamUserId: 1 }` | Yes | One link per pair |
| 2 | `{ coreTeamUserId: 1, controlPlanId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_controlPlanCoreTeamUser.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_controlPlanCoreTeamUser.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_controlPlanCoreTeamUser.js
