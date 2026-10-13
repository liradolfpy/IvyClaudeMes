# u_mes_syst_userAccessReview

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Periodic review of the user accounts and roles of a computerised system, confirming that every account is still needed and has the right authority. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 26 (22 required, 4 may be null) |
| Estimated volume per year | about 20 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per user access review, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with userAccessReviewId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_userAccessReviewLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1348000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"UAR-MES-RJ1-2026-02"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | computerisedSystemId | String | - | Yes | Reference to u_mes_syst_computerisedSystem._id | `"1344000000000001"` | Reference: u_mes_syst_computerisedSystem._id |
| 7 | computerisedSystemName | String | - | Yes | Display value of computerisedSystemId, copied from u_mes_syst_computerisedSystem.name | `"Manufacturing execution system, Ranjangaon OSD plant"` |  |
| 8 | reviewPeriodFromDate | Date | Date | Yes | First day of the review period | `ISODate("2026-04-01T00:00:00.000+0000")` |  |
| 9 | reviewPeriodToDate | Date | Date | Yes | Last day of the review period | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 10 | usersReviewedCount | Int32 | - | Yes | Accounts reviewed | `NumberInt(146)` |  |
| 11 | accessRemovedCount | Int32 | - | Yes | Accounts locked or roles removed | `NumberInt(1)` |  |
| 12 | accessChangedCount | Int32 | - | Yes | Roles changed | `NumberInt(1)` |  |
| 13 | reviewedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000019"` | Reference: u_mes_mast_user._id |
| 14 | reviewedBy | String | - | Yes | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Tejas Bapat"` |  |
| 15 | reviewedAt | Date | Datetime | No (null allowed) | Time the review was completed | `ISODate("2026-09-16T15:00:00.000+0000")` |  |
| 16 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 17 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 18 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-17T10:00:00.000+0000")` |  |
| 19 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Open; In Review; Completed |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 21 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T15:00:00.000+0000")` |  |
| 22 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 23 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 24 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T10:00:00.000+0000")` |  |
| 25 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 26 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |

## Status values

Open, In Review, Completed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ computerisedSystemId: 1 }` | No | Look-up of documents by computerised system |
| 4 | `{ siteId: 1, reviewPeriodFromDate: -1 }` | No | Time-ordered lists and reports by review period from date |

## Referenced by

u_mes_syst_userAccessReviewLine.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_userAccessReview.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_userAccessReview.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_userAccessReview.js
