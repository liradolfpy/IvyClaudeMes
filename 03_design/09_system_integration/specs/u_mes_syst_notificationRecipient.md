# u_mes_syst_notificationRecipient

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per recipient of a notification |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_syst_notification |
| _id pattern | <notificationId>-R<nnn> |
| Display value used by references | recordNo |
| Keys | 22 (17 required, 5 may be null) |

## Structure

Child collection. The parent notification can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. notificationId and notificationName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <notificationId>-R<nnn> | `"NTF-20260929-000096-R001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000096-R001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | notificationId | String | Yes | Reference to u_mes_syst_notification._id: the parent document this one belongs to | `"NTF-20260929-000096"` | Reference: u_mes_syst_notification._id |
| 6 | notificationName | String | Yes | Display value of notificationId, copied from u_mes_syst_notification.title | `"Quality andon not acknowledged"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | userId | String | Yes | Reference to u_mes_mast_user._id | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 10 | roleId | String | No (null allowed) | Reference to u_mes_mast_role._id | `"ROLE-OPERATOR"` | Reference: u_mes_mast_role._id |
| 11 | roleName | String | No (null allowed) | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 12 | channel | String | Yes | Channel of the notification recipient | `"Mobile Push"` | Screen; Email; SMS; Mobile Push |
| 13 | sentAt | Date | No (null allowed) | Date and time when the record was sent | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 14 | deliveredAt | Date | No (null allowed) | Date and time when the record was delivered | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 15 | readAt | Date | No (null allowed) | Date and time when the record was read | `ISODate("2026-09-29T00:31:14.000+0000")` |  |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 19 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 20 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:31:14.000+0000")` |  |
| 21 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 22 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ notificationId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |
| 3 | `{ roleId: 1 }` | No | Look-up of lines by role |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_notificationRecipient.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_notificationRecipient.js
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_notificationRecipient.js
