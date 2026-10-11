# u_mes_trac_componentLotLink

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | Lot-to-lot lineage: ingot heat to melt to casting lot to heat-treatment charge to anodising load; split and merge |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (28 required, 4 may be null) |
| Estimated volume per year | ~120,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per component lot link, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1133000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CLL-2026-000261"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | parentLotId | String | Yes | Reference to u_mes_plan_lot._id: parent lot | `"1096000000000009"` | Reference: u_mes_plan_lot._id |
| 6 | parentLotName | String | Yes | Display value of parentLotId, copied from u_mes_plan_lot.recordNo | `"L260910-ING-003"` |  |
| 7 | childLotId | String | Yes | Reference to u_mes_plan_lot._id: child lot | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 8 | childLotName | String | Yes | Display value of childLotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 9 | parentItemId | String | Yes | Reference to u_mes_prod_item._id: parent item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 10 | parentItemName | String | Yes | Display value of parentItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 11 | childItemId | String | Yes | Reference to u_mes_prod_item._id: child item | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 12 | childItemName | String | Yes | Display value of childItemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 13 | linkType | String | Yes | Link type | `"Assembled"` | Assembled; Replaced; Split; Merge; Transformed |
| 14 | quantity | Decimal128 | Yes | Quantity of the component lot link | `NumberDecimal("1")` |  |
| 15 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 17 | operationId | String | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 18 | operationName | String | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 19 | operationExecutionId | String | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000001"` | Reference: u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000376"` |  |
| 21 | linkedAt | Date | Yes | Date and time when the record was linked | `ISODate("2026-09-17T01:22:50.000+0000")` |  |
| 22 | linkedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'linked' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | linkedBy | String | Yes | Display name of the user in linkedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 24 | yieldPct | Decimal128 | Yes | Yield (percent) | `NumberDecimal("98.8")` |  |
| 25 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Removed |
| 26 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-17T01:22:20.000+0000")` |  |
| 28 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 30 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-17T01:22:50.000+0000")` |  |
| 31 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Active, Removed. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentLotId: 1 }` | No | Look-up of documents by parent lot |
| 4 | `{ childLotId: 1 }` | No | Look-up of documents by child lot |
| 5 | `{ parentItemId: 1 }` | No | Look-up of documents by parent item |
| 6 | `{ childItemId: 1 }` | No | Look-up of documents by child item |
| 7 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 8 | `{ siteId: 1, linkedAt: -1 }` | No | Time-ordered lists and reports by linked at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_componentLotLink.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_componentLotLink.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_componentLotLink.js
