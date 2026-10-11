# u_mes_qual_reworkOrderWipUnit

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one rework order to one wip unit; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qual_reworkOrder |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A rework order can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. reworkOrderId and reworkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1169000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"RWK-2026-000052-WU01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | reworkOrderId | String | Yes | Reference to u_mes_qual_reworkOrder._id: the parent document this one belongs to | `"1168000000000001"` | Reference: u_mes_qual_reworkOrder._id |
| 6 | reworkOrderName | String | Yes | Display value of reworkOrderId, copied from u_mes_qual_reworkOrder.recordNo | `"RWK-2026-000052"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | wipUnitId | String | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000005"` | Reference: u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260918B0236"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-18T09:39:48.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-18T09:39:48.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ reworkOrderId: 1, wipUnitId: 1 }` | Yes | One link per pair |
| 2 | `{ wipUnitId: 1, reworkOrderId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_reworkOrderWipUnit.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_reworkOrderWipUnit.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_reworkOrderWipUnit.js
