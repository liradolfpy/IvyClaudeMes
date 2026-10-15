# u_mes_plan_productionOrderRelease

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | One document per release of a production order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_productionOrder |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (16 required, 3 may be null) |

## Structure

Child collection. The parent production order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. productionOrderId and productionOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1084000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PO-1000412-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id: the parent document this one belongs to | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 8 | releaseNo | Int32 | - | Yes | Release number | `NumberInt(1)` |  |
| 9 | quantity | Int32 | - | Yes | Quantity of the production order release | `NumberInt(1)` |  |
| 10 | releasedAt | Date | Datetime | No (null allowed) | Date and time when the record was released. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 11 | releasedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'released' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 12 | releasedBy | String | - | No (null allowed) | Display name of the user in releasedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ productionOrderId: 1, releaseNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_productionOrderRelease.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_productionOrderRelease.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_productionOrderRelease.js
