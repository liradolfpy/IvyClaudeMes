# u_mes_qual_reworkOrderStep

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per step of a rework order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_reworkOrder |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (17 required, 3 may be null) |

## Structure

Child collection. The parent rework order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. reworkOrderId and reworkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1170000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"RWK-2026-000052-S01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | reworkOrderId | String | Yes | Reference to u_mes_qual_reworkOrder._id: the parent document this one belongs to | `"1168000000000001"` | Reference: u_mes_qual_reworkOrder._id |
| 6 | reworkOrderName | String | Yes | Display value of reworkOrderId, copied from u_mes_qual_reworkOrder.recordNo | `"RWK-2026-000052"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"1051000000000008"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Pressure leak test"` |  |
| 10 | description | String | Yes | Description of the rework order step | `"Clamp the caliper in the nest, connect the inlet adaptor and start program LT-03"` |  |
| 11 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-22T10:33:10.000+0000")` |  |
| 12 | completedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'completed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 13 | completedBy | String | No (null allowed) | Display name of the user in completedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-22T10:32:40.000+0000")` |  |
| 16 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 18 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-22T10:33:10.000+0000")` |  |
| 19 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ reworkOrderId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_reworkOrderStep.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_reworkOrderStep.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_reworkOrderStep.js
