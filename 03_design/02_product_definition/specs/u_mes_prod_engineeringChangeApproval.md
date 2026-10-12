# u_mes_prod_engineeringChangeApproval

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per approval of a engineering change |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_prod_engineeringChange |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (18 required, 2 may be null) |

## Structure

Child collection. The parent engineering change can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. engineeringChangeId and engineeringChangeName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1079000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ECN-2026-0027-A01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | engineeringChangeId | String | - | Yes | Reference to u_mes_prod_engineeringChange._id: the parent document this one belongs to | `"1076000000000001"` | Reference: u_mes_prod_engineeringChange._id |
| 6 | engineeringChangeName | String | - | Yes | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 7 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 8 | businessFunction | String | - | Yes | Business function | `"Quality"` | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| 9 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 10 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 11 | decision | String | - | Yes | Decision of the engineering change approval | `"Approved"` | Approved; Rejected; Approved With Conditions |
| 12 | decidedAt | Date | Datetime | No (null allowed) | Date and time when the record was decided. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 13 | comment | String | - | No (null allowed) | Comment of the engineering change approval | `"Verified against customer drawing revision D"` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 16 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 18 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 19 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ engineeringChangeId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_engineeringChangeApproval.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_engineeringChangeApproval.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_engineeringChangeApproval.js
