# u_mes_syst_userAccessReviewLine

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per line of a user access review |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_syst_userAccessReview |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 22 (20 required, 2 may be null) |

## Structure

Child collection. The parent user access review can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. userAccessReviewId and userAccessReviewName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1349000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"UAR-MES-PN1-2026-02-L01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userAccessReviewId | String | - | Yes | Reference to u_mes_syst_userAccessReview._id: the parent document this one belongs to | `"1348000000000001"` | Reference: u_mes_syst_userAccessReview._id |
| 6 | userAccessReviewName | String | - | Yes | Display value of userAccessReviewId, copied from u_mes_syst_userAccessReview.recordNo | `"UAR-MES-PN1-2026-02"` |  |
| 7 | lineNo | Int32 | - | Yes | Line number | `NumberInt(10)` |  |
| 8 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 10 | roleId | String | - | Yes | Reference to u_mes_mast_role._id | `"1026000000000001"` | Reference: u_mes_mast_role._id |
| 11 | roleName | String | - | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 12 | accessStillRequired | Boolean | - | Yes | True when the role is still needed | `true` |  |
| 13 | reviewAction | String | - | Yes | Decision | `"Retain"` | Retain; Remove Role; Change Role; Lock Account |
| 14 | actionCompletedAt | Date | Datetime | No (null allowed) | Time the decision was carried out; null for Retain | `null` |  |
| 15 | comment | String | - | No (null allowed) | Reviewer comment | `null` |  |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 18 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 20 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 21 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 22 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ userAccessReviewId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |
| 3 | `{ roleId: 1 }` | No | Look-up of lines by role |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_userAccessReviewLine.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_userAccessReviewLine.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_userAccessReviewLine.js
