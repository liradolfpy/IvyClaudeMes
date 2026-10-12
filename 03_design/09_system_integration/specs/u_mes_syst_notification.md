# u_mes_syst_notification

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Alerts and escalations sent to users / groups with delivery and acknowledgement status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 32 (20 required, 12 may be null) |
| Estimated volume per year | ~400,000 |
| Storage | standard, TTL |

## Structure

Flat entity collection: one document per notification, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with notificationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_notificationRecipient | Child | recipient |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1244000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"NTF-2026-000310"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | notificationTypeId | String | - | Yes | Reference to u_mes_syst_notificationType._id | `"1291000000000001"` | Reference: u_mes_syst_notificationType._id |
| 6 | notificationTypeName | String | - | Yes | Display value of notificationTypeId, copied from u_mes_syst_notificationType.name | `"Andon Escalation"` |  |
| 7 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 8 | title | String | - | Yes | Title of the notification; used as its display value in other collections | `"Die temperature alarm not acknowledged"` |  |
| 9 | bodyText | String | - | Yes | Body text | `"Quality andon at WC-TRQ-01 not acknowledged within 5 minutes"` |  |
| 10 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_andonEvent"` |  |
| 11 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1251000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 12 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"Castings sticking in die 2, operator needs maintenance"` |  |
| 13 | andonEventId | String | - | No (null allowed) | Reference to u_mes_plan_andonEvent._id | `null` | Reference: u_mes_plan_andonEvent._id |
| 14 | andonEventName | String | - | No (null allowed) | Display value of andonEventId, copied from u_mes_plan_andonEvent.description | `null` |  |
| 15 | alarmId | String | - | No (null allowed) | Reference to u_mes_perf_alarm._id | `"1212000000000001"` | Reference: u_mes_perf_alarm._id |
| 16 | alarmName | String | - | No (null allowed) | Display value of alarmId, copied from u_mes_perf_alarm.recordNo | `"ALM-2026-000176"` |  |
| 17 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 18 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 19 | escalationLevel | Int32 | - | Yes | Escalation level | `NumberInt(1)` |  |
| 20 | raisedAt | Date | Datetime | Yes | Date and time when the record was raised. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 21 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 22 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | expiresAt | Date | Datetime | No (null allowed) | Expires date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2027-03-31T23:59:00.000+0000")` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Sent; Acknowledged; Expired |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Raised, Sent, Acknowledged, Expired. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ notificationTypeId: 1 }` | No | Look-up of documents by notification type |
| 4 | `{ andonEventId: 1 }` | No | Look-up of documents by andon event |
| 5 | `{ alarmId: 1 }` | No | Look-up of documents by alarm |
| 6 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 7 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 8 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_syst_notificationRecipient.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_notification.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_notification.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_notification.js
