# u_mes_syst_notificationRecipient

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | One document per recipient of a notification |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_syst_notification |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (18 required, 5 may be null) |

## Structure

Child collection. The parent notification can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. notificationId and notificationName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1245000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"NTF-2026-000310-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | notificationId | String | - | Yes | Reference to u_mes_syst_notification._id: the parent document this one belongs to | `"1244000000000001"` | Reference: u_mes_syst_notification._id |
| 7 | notificationName | String | - | Yes | Display value of notificationId, copied from u_mes_syst_notification.title | `"Die temperature alarm not acknowledged"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 10 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 11 | roleId | String | - | No (null allowed) | Reference to u_mes_mast_role._id | `"1026000000000001"` | Reference: u_mes_mast_role._id |
| 12 | roleName | String | - | No (null allowed) | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 13 | channel | String | - | Yes | Channel of the notification recipient | `"Screen"` | Screen; Email; SMS; Mobile Push |
| 14 | sentAt | Date | Datetime | No (null allowed) | Date and time when the record was sent. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 15 | deliveredAt | Date | Datetime | No (null allowed) | Date and time when the record was delivered. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:55.000+0000")` |  |
| 16 | readAt | Date | Datetime | No (null allowed) | Date and time when the record was read. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:20.000+0000")` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:20.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_notificationRecipient.js
