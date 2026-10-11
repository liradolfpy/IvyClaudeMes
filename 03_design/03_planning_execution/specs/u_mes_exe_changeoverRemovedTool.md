# u_mes_exe_changeoverRemovedTool

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Links one changeover to one removed tool; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_exe_changeover |
| _id pattern | <changeoverId>-RT<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A changeover can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. changeoverId and changeoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <changeoverId>-RT<nnn> | `"CHG-20260930-ASY-01-01-RT001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260930-ASY-01-01-RT001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | changeoverId | String | Yes | Reference to u_mes_exe_changeover._id: the parent document this one belongs to | `"CHG-20260930-ASY-01-01"` | Reference: u_mes_exe_changeover._id |
| 6 | changeoverName | String | Yes | Display value of changeoverId, copied from u_mes_exe_changeover.recordNo | `"20260930-ASY-01-01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | removedToolId | String | Yes | Reference to u_mes_mnt_tool._id: removed tool | `"TL-SKT-10-0007"` | Reference: u_mes_mnt_tool._id |
| 9 | removedToolName | String | Yes | Display value of removedToolId, copied from u_mes_mnt_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
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
| 1 | `{ changeoverId: 1, removedToolId: 1 }` | Yes | One link per pair |
| 2 | `{ removedToolId: 1, changeoverId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_changeoverRemovedTool.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_changeoverRemovedTool.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_changeoverRemovedTool.js
