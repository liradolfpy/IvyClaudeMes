# u_mes_qual_deviationPermitApproval

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per approval of a deviation permit |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_deviationPermit |
| _id pattern | <deviationPermitId>-A<nnn> |
| Display value used by references | recordNo |
| Keys | 19 (18 required, 1 may be null) |

## Structure

Child collection. The parent deviation permit can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. deviationPermitId and deviationPermitName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <deviationPermitId>-A<nnn> | `"DEV-2026-0006-A001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0006-A001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | deviationPermitId | String | Yes | Reference to u_mes_qual_deviationPermit._id: the parent document this one belongs to | `"DEV-2026-0006"` | Reference: u_mes_qual_deviationPermit._id |
| 6 | deviationPermitName | String | Yes | Display value of deviationPermitId, copied from u_mes_qual_deviationPermit.title | `"Anodising thickness upper limit deviation"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | businessFunction | String | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 9 | userId | String | Yes | Reference to u_mes_mast_user._id | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 10 | userName | String | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 11 | decision | String | Yes | Decision of the deviation permit approval | `"Approved"` | Approved; Rejected; Approved With Conditions |
| 12 | decidedAt | Date | No (null allowed) | Date and time when the record was decided | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ deviationPermitId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_deviationPermitApproval.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_deviationPermitApproval.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_deviationPermitApproval.js
