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
| Keys | 44 (27 required, 17 may be null) |
| Estimated volume per year | ~6.5 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per genealogy link, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1132000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GEN-2026-000372"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | parentWipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id: parent wip unit | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 7 | parentWipUnitName | String | - | No (null allowed) | Display value of parentWipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 8 | parentSerialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id: parent serial number | `null` | Reference: u_mes_trac_serialNumber._id |
| 9 | parentSerialNumberName | String | - | No (null allowed) | Display value of parentSerialNumberId, copied from u_mes_trac_serialNumber.recordNo | `null` |  |
| 10 | parentItemId | String | - | Yes | Reference to u_mes_prod_item._id: parent item | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 11 | parentItemName | String | - | Yes | Display value of parentItemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 12 | childType | String | - | Yes | Child type | `"Lot"` | Lot; Serial |
| 13 | childItemId | String | - | Yes | Reference to u_mes_prod_item._id: child item | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 14 | childItemName | String | - | Yes | Display value of childItemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 15 | childLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: child lot | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 16 | childLotName | String | - | No (null allowed) | Display value of childLotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 17 | childSerialNo | String | - | No (null allowed) | Child serial number | `null` |  |
| 18 | quantity | Decimal128 | - | Yes | Quantity of the genealogy link | `1` |  |
| 19 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 21 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 22 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 23 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 24 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 25 | materialConsumptionId | String | - | No (null allowed) | Reference to u_mes_matl_materialConsumption._id | `"1121000000000001"` | Reference: u_mes_matl_materialConsumption._id |
| 26 | materialConsumptionName | String | - | No (null allowed) | Display value of materialConsumptionId, copied from u_mes_matl_materialConsumption.recordNo | `"CON-2026-000311"` |  |
| 27 | linkedAt | Date | Datetime | Yes | Date and time when the record was linked. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 28 | linkedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'linked' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | linkedBy | String | - | Yes | Display name of the user in linkedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 30 | linkType | String | - | Yes | Link type | `"Assembled"` | Assembled; Replaced; Split; Merge; Transformed |
| 31 | removedAt | Date | Datetime | No (null allowed) | Date and time when the record was removed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 32 | removedReason | String | - | No (null allowed) | Removed reason | `null` |  |
| 33 | childSerialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id: child serial number | `null` | Reference: u_mes_trac_serialNumber._id |
| 34 | childSerialNumberName | String | - | No (null allowed) | Display value of childSerialNumberId, copied from u_mes_trac_serialNumber.recordNo | `null` |  |
| 35 | childWipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id: child wip unit | `null` | Reference: u_mes_plan_wipUnit._id |
| 36 | childWipUnitName | String | - | No (null allowed) | Display value of childWipUnitId, copied from u_mes_plan_wipUnit.recordNo | `null` |  |
| 37 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Removed |
| 38 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 39 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:07.000+0000")` |  |
| 40 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 41 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 42 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 43 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
