# u_mes_ehs_andonEventEscalation

| Property | Value |
|---|---|
| Module | Energy, safety and andon (ehs) |
| Purpose | One document per escalation of a andon event |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_ehs_andonEvent |
| _id pattern | <andonEventId>-E<nnn> |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent andon event can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. andonEventId and andonEventName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <andonEventId>-E<nnn> | `"AND-20260929-0005-E001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0005-E001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | andonEventId | String | Yes | Reference to u_mes_ehs_andonEvent._id: the parent document this one belongs to | `"AND-20260929-0005"` | Reference: u_mes_ehs_andonEvent._id |
| 6 | andonEventName | String | Yes | Display value of andonEventId, copied from u_mes_ehs_andonEvent.description | `"Leak test rejects repeating at station LKT-01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | level | Int32 | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 9 | escalatedAt | Date | Yes | Date and time when the record was escalated | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 10 | toUserId | String | Yes | Reference to u_mes_mdm_user._id: to user | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 11 | toUserName | String | Yes | Display value of toUserId, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 12 | channel | String | Yes | Channel of the andon event escalation | `"Mobile Push"` | Screen; Email; SMS; Mobile Push |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ andonEventId: 1, level: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ toUserId: 1 }` | No | Look-up of lines by to user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/10_energy_safety_andon/validators/u_mes_ehs_andonEventEscalation.json
- Indexes: 03_design/10_energy_safety_andon/indexes/u_mes_ehs_andonEventEscalation.js
- Sample document: 03_design/10_energy_safety_andon/samples/u_mes_ehs_andonEventEscalation.js
