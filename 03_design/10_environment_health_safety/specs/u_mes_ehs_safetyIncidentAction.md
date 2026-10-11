# u_mes_ehs_safetyIncidentAction

| Property | Value |
|---|---|
| Module | Environment Health and Safety (ehs) |
| Purpose | One document per action of a safety incident |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_ehs_safetyIncident |
| _id pattern | <safetyIncidentId>-A<nnn> |
| Display value used by references | description |
| Keys | 19 (18 required, 1 may be null) |

## Structure

Child collection. The parent safety incident can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. safetyIncidentId and safetyIncidentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <safetyIncidentId>-A<nnn> | `"SAF-2026-0003-A001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0003-A001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | safetyIncidentId | String | Yes | Reference to u_mes_ehs_safetyIncident._id: the parent document this one belongs to | `"SAF-2026-0003"` | Reference: u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String | Yes | Display value of safetyIncidentId, copied from u_mes_ehs_safetyIncident.title | `"Coolant spill near HMC-01 walkway"` |  |
| 7 | actionNo | Int32 | Yes | Action number | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the safety incident action | `"Replace coolant hose and add drip tray under the HMC-01 coupling"` |  |
| 9 | ownerUserId | String | Yes | Reference to u_mes_mast_user._id: owner user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 10 | ownerUserName | String | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | dueAt | Date | Yes | Due date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 12 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ safetyIncidentId: 1, actionNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/10_environment_health_safety/validators/u_mes_ehs_safetyIncidentAction.json
- Indexes: 03_design/10_environment_health_safety/indexes/u_mes_ehs_safetyIncidentAction.js
- Sample document: 03_design/10_environment_health_safety/samples/u_mes_ehs_safetyIncidentAction.js
