# u_mes_qlt_nonconformanceContainmentAction

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per containment action of a nonconformance |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qlt_nonconformance |
| _id pattern | <nonconformanceId>-CA<nnn> |
| Display value used by references | description |
| Keys | 18 (17 required, 1 may be null) |

## Structure

Child collection. The parent nonconformance can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. nonconformanceId and nonconformanceName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <nonconformanceId>-CA<nnn> | `"NCR-2026-000118-CA001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000118-CA001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | Yes | Reference to u_mes_qlt_nonconformance._id: the parent document this one belongs to | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String | Yes | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 7 | actionNo | Int32 | Yes | Action number | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the nonconformance containment action | `"Hold all units assembled with seal lot S260921-SEL-004 and retest 100 percent"` |  |
| 9 | ownerUserId | String | Yes | Reference to u_mes_mdm_user._id: owner user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 10 | ownerUserName | String | Yes | Display value of ownerUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 11 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ nonconformanceId: 1, actionNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_nonconformanceContainmentAction.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_nonconformanceContainmentAction.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_nonconformanceContainmentAction.js
