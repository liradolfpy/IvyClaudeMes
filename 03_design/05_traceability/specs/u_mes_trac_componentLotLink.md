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
| Keys | 33 (29 required, 4 may be null) |
| Estimated volume per year | ~120,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per component lot link, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1133000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CLL-2026-000261"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | parentLotId | String | - | Yes | Reference to u_mes_plan_lot._id: parent lot | `"1096000000000009"` | Reference: u_mes_plan_lot._id |
| 7 | parentLotName | String | - | Yes | Display value of parentLotId, copied from u_mes_plan_lot.recordNo | `"L260910-ING-003"` |  |
| 8 | childLotId | String | - | Yes | Reference to u_mes_plan_lot._id: child lot | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 9 | childLotName | String | - | Yes | Display value of childLotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 10 | parentItemId | String | - | Yes | Reference to u_mes_prod_item._id: parent item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 11 | parentItemName | String | - | Yes | Display value of parentItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 12 | childItemId | String | - | Yes | Reference to u_mes_prod_item._id: child item | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 13 | childItemName | String | - | Yes | Display value of childItemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 14 | linkType | String | - | Yes | Link type | `"Assembled"` | Assembled; Replaced; Split; Merge; Transformed |
| 15 | quantity | Decimal128 | - | Yes | Quantity of the component lot link | `NumberDecimal("1")` |  |
| 16 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 18 | operationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 19 | operationName | String | - | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 20 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000001"` | Reference: u_mes_plan_operationExecution._id |
| 21 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000376"` |  |
| 22 | linkedAt | Date | Datetime | Yes | Date and time when the record was linked. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 23 | linkedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'linked' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 24 | linkedBy | String | - | Yes | Display name of the user in linkedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 25 | yieldPct | Decimal128 | - | Yes | Yield (percent) | `NumberDecimal("98.8")` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Removed |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
