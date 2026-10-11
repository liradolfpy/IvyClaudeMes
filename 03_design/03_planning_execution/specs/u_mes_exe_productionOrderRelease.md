# u_mes_exe_productionOrderRelease

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | One document per release of a production order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_exe_productionOrder |
| _id pattern | <productionOrderId>-R<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (15 required, 3 may be null) |

## Structure

Child collection. The parent production order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. productionOrderId and productionOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <productionOrderId>-R<nnn> | `"PO-1000412-R001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"1000412-R001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | Yes | Reference to u_mes_exe_productionOrder._id: the parent document this one belongs to | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 6 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 7 | releaseNo | Int32 | Yes | Release number | `NumberInt(1)` |  |
| 8 | quantity | Int32 | Yes | Quantity of the production order release | `NumberInt(1)` |  |
| 9 | releasedAt | Date | No (null allowed) | Date and time when the record was released | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 10 | releasedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'released' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 11 | releasedBy | String | No (null allowed) | Display name of the user in releasedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ productionOrderId: 1, releaseNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_productionOrderRelease.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_productionOrderRelease.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_productionOrderRelease.js
