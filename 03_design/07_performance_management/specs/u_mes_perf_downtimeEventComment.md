# u_mes_perf_downtimeEventComment

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | One document per comment of a downtime event |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_perf_downtimeEvent |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent downtime event can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. downtimeEventId and downtimeEventName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1206000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DT-2026-000196-C01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | downtimeEventId | String | - | Yes | Reference to u_mes_perf_downtimeEvent._id: the parent document this one belongs to | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 7 | downtimeEventName | String | - | Yes | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | commentedAt | Date | Datetime | Yes | Date and time when the record was commented. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:55:10.000+0000")` |  |
| 10 | authorUserId | String | - | Yes | Reference to u_mes_mast_user._id: author user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 11 | authorUserName | String | - | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 12 | commentText | String | - | Yes | Comment text | `"Spare socket taken from tool crib"` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:54:40.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:55:10.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ downtimeEventId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ authorUserId: 1 }` | No | Look-up of lines by author user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_downtimeEventComment.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_downtimeEventComment.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_downtimeEventComment.js
