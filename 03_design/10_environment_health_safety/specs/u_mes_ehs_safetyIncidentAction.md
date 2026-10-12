# u_mes_ehs_safetyIncidentAction

| Property | Value |
|---|---|
| Module | Environment Health and Safety (ehs) |
| Purpose | One document per action of a safety incident |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_ehs_safetyIncident |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (18 required, 1 may be null) |

## Structure

Child collection. The parent safety incident can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. safetyIncidentId and safetyIncidentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1255000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SAF-2026-0003-A01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | safetyIncidentId | String | - | Yes | Reference to u_mes_ehs_safetyIncident._id: the parent document this one belongs to | `"1253000000000001"` | Reference: u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String | - | Yes | Display value of safetyIncidentId, copied from u_mes_ehs_safetyIncident.title | `"Molten metal splash near casting machine 1"` |  |
| 7 | actionNo | Int32 | - | Yes | Action number | `NumberInt(1)` |  |
| 8 | description | String | - | Yes | Description of the safety incident action | `"Brief all shifts on the incident at the start-of-shift meeting"` |  |
| 9 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 10 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 12 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
- Sample documents (10): 03_design/10_environment_health_safety/samples/u_mes_ehs_safetyIncidentAction.js
