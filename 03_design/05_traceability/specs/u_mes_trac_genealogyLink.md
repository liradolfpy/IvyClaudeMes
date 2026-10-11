# u_mes_trac_genealogyLink

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | As-built parent-child edges: unit to component serial or component lot, with operation and time |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 39 (26 required, 13 may be null) |
| Estimated volume per year | ~6.5 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per genealogy link, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1132000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"GEN-2026-000372"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | parentWipUnitId | String | No (null allowed) | Reference to u_mes_plan_wipUnit._id: parent wip unit | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 6 | parentWipUnitName | String | No (null allowed) | Display value of parentWipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 7 | parentSerialNumberId | String | No (null allowed) | Reference to u_mes_trac_serialNumber._id: parent serial number | `null` | Reference: u_mes_trac_serialNumber._id |
| 8 | parentSerialNumberName | String | No (null allowed) | Display value of parentSerialNumberId, copied from u_mes_trac_serialNumber.recordNo | `null` |  |
| 9 | parentItemId | String | Yes | Reference to u_mes_prod_item._id: parent item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 10 | parentItemName | String | Yes | Display value of parentItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 11 | childType | String | Yes | Child type | `"Lot"` | Lot; Serial |
| 12 | childItemId | String | Yes | Reference to u_mes_prod_item._id: child item | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 13 | childItemName | String | Yes | Display value of childItemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 14 | childLotId | String | No (null allowed) | Reference to u_mes_plan_lot._id: child lot | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 15 | childLotName | String | No (null allowed) | Display value of childLotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 16 | childSerialNo | String | No (null allowed) | Child serial number | `null` |  |
| 17 | quantity | Decimal128 | Yes | Quantity of the genealogy link | `NumberDecimal("1")` |  |
| 18 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 20 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 21 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 22 | operationExecutionId | String | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 23 | operationExecutionName | String | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 24 | materialConsumptionId | String | No (null allowed) | Reference to u_mes_matl_materialConsumption._id | `"1121000000000001"` | Reference: u_mes_matl_materialConsumption._id |
| 25 | materialConsumptionName | String | No (null allowed) | Display value of materialConsumptionId, copied from u_mes_matl_materialConsumption.recordNo | `"CON-2026-000311"` |  |
| 26 | linkedAt | Date | Yes | Date and time when the record was linked | `ISODate("2026-09-15T00:32:37.000+0000")` |  |
| 27 | linkedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'linked' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 28 | linkedBy | String | Yes | Display name of the user in linkedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 29 | linkType | String | Yes | Link type | `"Assembled"` | Assembled; Replaced; Split; Merge; Transformed |
| 30 | removedAt | Date | No (null allowed) | Date and time when the record was removed | `null` |  |
| 31 | removedReason | String | No (null allowed) | Removed reason | `null` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Removed |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:32:07.000+0000")` |  |
| 35 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 37 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:32:37.000+0000")` |  |
| 38 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Active, Removed. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentWipUnitId: 1 }` | No | Look-up of documents by parent wip unit |
| 4 | `{ parentSerialNumberId: 1 }` | No | Look-up of documents by parent serial number |
| 5 | `{ parentItemId: 1 }` | No | Look-up of documents by parent item |
| 6 | `{ childItemId: 1 }` | No | Look-up of documents by child item |
| 7 | `{ childLotId: 1 }` | No | Look-up of documents by child lot |
| 8 | `{ siteId: 1, linkedAt: -1 }` | No | Time-ordered lists and reports by linked at |

## Referenced by

u_mes_trac_asBuiltRecordComponent.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_genealogyLink.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_genealogyLink.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_genealogyLink.js
