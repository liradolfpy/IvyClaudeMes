# u_mes_perf_downtimeEventComment

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | One document per comment of a downtime event |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_perf_downtimeEvent |
| _id pattern | <downtimeEventId>-C<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (18 required, 0 may be null) |

## Structure

Child collection. The parent downtime event can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. downtimeEventId and downtimeEventName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <downtimeEventId>-C<nnn> | `"DT-20260929-0009-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0009-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | downtimeEventId | String | Yes | Reference to u_mes_perf_downtimeEvent._id: the parent document this one belongs to | `"DT-20260929-0009"` | Reference: u_mes_perf_downtimeEvent._id |
| 6 | downtimeEventName | String | Yes | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"20260929-0009"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | commentedAt | Date | Yes | Date and time when the record was commented | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 9 | authorUserId | String | Yes | Reference to u_mes_mast_user._id: author user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 10 | authorUserName | String | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | commentText | String | Yes | Comment text | `"Spare socket taken from tool crib"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
- Sample document: 03_design/07_performance_management/samples/u_mes_perf_downtimeEventComment.js
