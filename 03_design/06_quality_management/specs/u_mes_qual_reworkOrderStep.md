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
| Keys | 21 (18 required, 3 may be null) |

## Structure

Child collection. The parent rework order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. reworkOrderId and reworkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1170000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RWK-2026-000052-S01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | reworkOrderId | String | - | Yes | Reference to u_mes_qual_reworkOrder._id: the parent document this one belongs to | `"1168000000000001"` | Reference: u_mes_qual_reworkOrder._id |
| 7 | reworkOrderName | String | - | Yes | Display value of reworkOrderId, copied from u_mes_qual_reworkOrder.recordNo | `"RWK-2026-000052"` |  |
| 8 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 9 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000008"` | Reference: u_mes_prod_operation._id |
| 10 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Pressure leak test"` |  |
| 11 | description | String | - | Yes | Description of the rework order step | `"Clamp the caliper in the nest, connect the inlet adaptor and start program LT-03"` |  |
| 12 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-22T16:03:10.000+0000")` |  |
| 13 | completedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'completed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 14 | completedBy | String | - | No (null allowed) | Display name of the user in completedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 15 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 16 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-22T16:02:40.000+0000")` |  |
| 17 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-22T16:03:10.000+0000")` |  |
| 20 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
