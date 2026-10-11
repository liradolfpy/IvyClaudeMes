# u_mes_exe_changeoverPerformedByUser

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Links one changeover to one performed by user; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_exe_changeover |
| _id pattern | <changeoverId>-PBU<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A changeover can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. changeoverId and changeoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <changeoverId>-PBU<nnn> | `"CHG-20260930-ASY-01-01-PBU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260930-ASY-01-01-PBU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | changeoverId | String | Yes | Reference to u_mes_exe_changeover._id: the parent document this one belongs to | `"CHG-20260930-ASY-01-01"` | Reference: u_mes_exe_changeover._id |
| 6 | changeoverName | String | Yes | Display value of changeoverId, copied from u_mes_exe_changeover.recordNo | `"20260930-ASY-01-01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | performedByUserId | String | Yes | Reference to u_mes_mdm_user._id: performed by user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 9 | performedByUserName | String | Yes | Display value of performedByUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ changeoverId: 1, performedByUserId: 1 }` | Yes | One link per pair |
| 2 | `{ performedByUserId: 1, changeoverId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_changeoverPerformedByUser.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_changeoverPerformedByUser.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_changeoverPerformedByUser.js
