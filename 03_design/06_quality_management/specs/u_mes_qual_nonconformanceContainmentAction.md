# u_mes_qual_nonconformanceContainmentAction

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per containment action of a nonconformance |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_nonconformance |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (17 required, 1 may be null) |

## Structure

Child collection. The parent nonconformance can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. nonconformanceId and nonconformanceName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1162000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"NCR-2026-000118-CA01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | Yes | Reference to u_mes_qual_nonconformance._id: the parent document this one belongs to | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | Yes | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 7 | actionNo | Int32 | Yes | Action number | `NumberInt(1)` |  |
| 8 | description | String | Yes | Description of the nonconformance containment action | `"Segregate and hold all suspect material at Gravity Die Casting Cell 1"` |  |
| 9 | ownerUserId | String | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 10 | ownerUserName | String | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-15T00:33:30.000+0000")` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:30.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ nonconformanceId: 1, actionNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_nonconformanceContainmentAction.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_nonconformanceContainmentAction.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_nonconformanceContainmentAction.js
