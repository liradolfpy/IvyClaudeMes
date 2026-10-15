# u_mes_plan_container

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Bins, trolleys, returnable crates and pallets with contents and nesting |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (28 required, 12 may be null) |
| Estimated volume per year | ~60,000 active and historic |
| Storage | standard |

## Structure

Flat entity collection: one document per container, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with containerId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_containerLot | Relationship | lot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1099000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"TRL-00031"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | containerTypeId | String | - | Yes | Reference to u_mes_plan_containerType._id | `"1278000000000003"` | Reference: u_mes_plan_containerType._id |
| 7 | containerTypeName | String | - | Yes | Display value of containerTypeId, copied from u_mes_plan_containerType.name | `"Casting Trolley"` |  |
| 8 | packagingSpecificationId | String | - | Yes | Reference to u_mes_matl_packagingSpecification._id | `"1122000000000001"` | Reference: u_mes_matl_packagingSpecification._id |
| 9 | packagingSpecificationName | String | - | Yes | Display value of packagingSpecificationId, copied from u_mes_matl_packagingSpecification.recordNo | `"PKS-5110-10-0100-SML-01"` |  |
| 10 | isReturnable | Boolean | - | Yes | True when the record is returnable | `false` |  |
| 11 | ownerCustomerId | String | - | Yes | Reference to u_mes_mast_customer._id: owner customer | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 12 | ownerCustomerName | String | - | Yes | Display value of ownerCustomerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 13 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 15 | quantity | Int32 | - | Yes | Quantity of the container | `NumberInt(120)` |  |
| 16 | capacity | Int32 | - | Yes | CAPAcity of the container | `NumberInt(120)` |  |
| 17 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 18 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 19 | parentContainerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id: parent container | `null` | Reference: u_mes_plan_container._id |
| 20 | parentContainerName | String | - | No (null allowed) | Display value of parentContainerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 21 | tareWeightKg | Decimal128 | - | Yes | Tare weight (kg) | `NumberDecimal("2.100")` |  |
| 22 | grossWeightKg | Decimal128 | - | Yes | Gross weight (kg) | `NumberDecimal("3.480")` |  |
| 23 | onHold | Boolean | - | Yes | True when: on hold | `false` |  |
| 24 | packedAt | Date | Datetime | No (null allowed) | Date and time when the record was packed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 25 | packedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'packed' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 26 | packedBy | String | - | No (null allowed) | Display name of the user in packedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 27 | labelId | String | - | No (null allowed) | Reference to u_mes_matl_label._id | `null` | Reference: u_mes_matl_label._id |
| 28 | labelName | String | - | No (null allowed) | Display value of labelId, copied from u_mes_matl_label.recordNo | `null` |  |
| 29 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 30 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 31 | lastCleanedAt | Date | Datetime | No (null allowed) | Last cleaned date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 32 | cycleCount | Int32 | - | Yes | Number of trips the returnable container has made | `NumberInt(37)` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Full"` | Empty; Filling; Full; Sealed; Shipped; Returned; Under Repair |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Empty, Filling, Full, Sealed, Shipped, Returned, Under Repair. Initial state: Empty. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ containerTypeId: 1 }` | No | Look-up of documents by container type |
| 4 | `{ packagingSpecificationId: 1 }` | No | Look-up of documents by packaging specification |
| 5 | `{ ownerCustomerId: 1 }` | No | Look-up of documents by owner customer |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 7 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 8 | `{ siteId: 1, packedAt: -1 }` | No | Time-ordered lists and reports by packed at |

## Referenced by

u_mes_plan_wipUnit, u_mes_plan_container, u_mes_plan_containerLot, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_label, u_mes_matl_shipmentLineContainer, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecord, u_mes_matl_exposureTimer.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_container.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_container.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_container.js
