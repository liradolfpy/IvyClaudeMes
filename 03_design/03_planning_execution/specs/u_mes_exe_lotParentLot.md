# u_mes_exe_lotParentLot

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Links one lot to one parent lot; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_exe_lot |
| _id pattern | <lotId>-PL<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A lot can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. lotId and lotName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <lotId>-PL<nnn> | `"LOT-L260928-GDC-014-PL001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"L260928-GDC-014-PL001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lotId | String | Yes | Reference to u_mes_exe_lot._id: the parent document this one belongs to | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 6 | lotName | String | Yes | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | parentLotId | String | Yes | Reference to u_mes_exe_lot._id: parent lot | `"LOT-S260914-PST-007"` | Reference: u_mes_exe_lot._id |
| 9 | parentLotName | String | Yes | Display value of parentLotId, copied from u_mes_exe_lot.recordNo | `"S260914-PST-007"` |  |
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
| 1 | `{ lotId: 1, parentLotId: 1 }` | Yes | One link per pair |
| 2 | `{ parentLotId: 1, lotId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_lotParentLot.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_lotParentLot.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_lotParentLot.js
