# u_mes_qlt_reworkOrderWipUnit

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Links one rework order to one wip unit; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qlt_reworkOrder |
| _id pattern | <reworkOrderId>-WU<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A rework order can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. reworkOrderId and reworkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <reworkOrderId>-WU<nnn> | `"RWK-2026-000052-WU001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000052-WU001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | reworkOrderId | String | Yes | Reference to u_mes_qlt_reworkOrder._id: the parent document this one belongs to | `"RWK-2026-000052"` | Reference: u_mes_qlt_reworkOrder._id |
| 6 | reworkOrderName | String | Yes | Display value of reworkOrderId, copied from u_mes_qlt_reworkOrder.recordNo | `"2026-000052"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | wipUnitId | String | Yes | Reference to u_mes_exe_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_exe_wipUnit._id |
| 9 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_exe_wipUnit.recordNo | `"U260929A0184"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ reworkOrderId: 1, wipUnitId: 1 }` | Yes | One link per pair |
| 2 | `{ wipUnitId: 1, reworkOrderId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_reworkOrderWipUnit.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_reworkOrderWipUnit.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_reworkOrderWipUnit.js
