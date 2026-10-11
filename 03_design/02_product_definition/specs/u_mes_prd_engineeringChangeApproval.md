# u_mes_prd_engineeringChangeApproval

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per approval of a engineering change |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_prd_engineeringChange |
| _id pattern | <engineeringChangeId>-A<nnn> |
| Display value used by references | recordNo |
| Keys | 20 (18 required, 2 may be null) |

## Structure

Child collection. The parent engineering change can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. engineeringChangeId and engineeringChangeName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <engineeringChangeId>-A<nnn> | `"ECN-2026-0031-A001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0031-A001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | engineeringChangeId | String | Yes | Reference to u_mes_prd_engineeringChange._id: the parent document this one belongs to | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String | Yes | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | businessFunction | String | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 9 | userId | String | Yes | Reference to u_mes_mdm_user._id | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 10 | userName | String | Yes | Display value of userId, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 11 | decision | String | Yes | Decision of the engineering change approval | `"Approved"` | Approved; Rejected; Approved With Conditions |
| 12 | decidedAt | Date | No (null allowed) | Date and time when the record was decided | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 13 | comment | String | No (null allowed) | Comment of the engineering change approval | `"Verified against customer drawing revision D"` |  |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 17 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 18 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 19 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 20 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ engineeringChangeId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_engineeringChangeApproval.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_engineeringChangeApproval.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_engineeringChangeApproval.js
