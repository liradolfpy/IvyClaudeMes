# u_mes_ehs_safetyIncidentWitnessUser

| Property | Value |
|---|---|
| Module | Environment Health and Safety (ehs) |
| Purpose | Links one safety incident to one witness user; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_ehs_safetyIncident |
| _id pattern | <safetyIncidentId>-WU<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A safety incident can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. safetyIncidentId and safetyIncidentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <safetyIncidentId>-WU<nnn> | `"SAF-2026-0003-WU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0003-WU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | safetyIncidentId | String | Yes | Reference to u_mes_ehs_safetyIncident._id: the parent document this one belongs to | `"SAF-2026-0003"` | Reference: u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String | Yes | Display value of safetyIncidentId, copied from u_mes_ehs_safetyIncident.title | `"Coolant spill near HMC-01 walkway"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | witnessUserId | String | Yes | Reference to u_mes_mast_user._id: witness user | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 9 | witnessUserName | String | Yes | Display value of witnessUserId, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ safetyIncidentId: 1, witnessUserId: 1 }` | Yes | One link per pair |
| 2 | `{ witnessUserId: 1, safetyIncidentId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/10_environment_health_safety/validators/u_mes_ehs_safetyIncidentWitnessUser.json
- Indexes: 03_design/10_environment_health_safety/indexes/u_mes_ehs_safetyIncidentWitnessUser.js
- Sample document: 03_design/10_environment_health_safety/samples/u_mes_ehs_safetyIncidentWitnessUser.js
