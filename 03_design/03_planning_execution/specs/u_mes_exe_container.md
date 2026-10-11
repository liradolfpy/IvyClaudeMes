# u_mes_exe_container

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Bins, trolleys, returnable crates and pallets with contents and nesting |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | CNT-<recordNo> |
| Display value used by references | recordNo |
| Keys | 39 (27 required, 12 may be null) |
| Estimated volume per year | ~60,000 active and historic |
| Storage | standard |

## Structure

Flat entity collection: one document per container, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with containerId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_exe_containerLot | Relationship | lot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CNT-<recordNo> | `"CNT-BIN-000731"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"BIN-000731"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | containerTypeId | String | Yes | Reference to u_mes_exe_containerType._id | `"CTT-RB-6040"` | Reference: u_mes_exe_containerType._id |
| 6 | containerTypeName | String | Yes | Display value of containerTypeId, copied from u_mes_exe_containerType.name | `"Returnable Bin 600 x 400"` |  |
| 7 | packagingSpecificationId | String | Yes | Reference to u_mes_mat_packagingSpecification._id | `"PKS-5110-10-0100-SML-01"` | Reference: u_mes_mat_packagingSpecification._id |
| 8 | packagingSpecificationName | String | Yes | Display value of packagingSpecificationId, copied from u_mes_mat_packagingSpecification.recordNo | `"5110-10-0100-SML-01"` |  |
| 9 | isReturnable | Boolean | Yes | True when the record is returnable | `false` |  |
| 10 | ownerCustomerId | String | Yes | Reference to u_mes_mdm_customer._id: owner customer | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 11 | ownerCustomerName | String | Yes | Display value of ownerCustomerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 12 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 13 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 14 | quantity | Int32 | Yes | Quantity of the container | `NumberInt(1)` |  |
| 15 | capacity | Int32 | Yes | CAPAcity of the container | `NumberInt(24)` |  |
| 16 | storageLocationId | String | Yes | Reference to u_mes_mat_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 17 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 18 | parentContainerId | String | No (null allowed) | Reference to u_mes_exe_container._id: parent container | `null` | Reference: u_mes_exe_container._id |
| 19 | parentContainerName | String | No (null allowed) | Display value of parentContainerId, copied from u_mes_exe_container.recordNo | `null` |  |
| 20 | tareWeightKg | Decimal128 | Yes | Tare weight (kg) | `NumberDecimal("2.100")` |  |
| 21 | grossWeightKg | Decimal128 | Yes | Gross weight (kg) | `NumberDecimal("3.480")` |  |
| 22 | onHold | Boolean | Yes | True when: on hold | `false` |  |
| 23 | packedAt | Date | No (null allowed) | Date and time when the record was packed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 24 | packedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'packed' | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 25 | packedBy | String | No (null allowed) | Display name of the user in packedById, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 26 | labelId | String | No (null allowed) | Reference to u_mes_mat_label._id | `"LBL-20260929-000412"` | Reference: u_mes_mat_label._id |
| 27 | labelName | String | No (null allowed) | Display value of labelId, copied from u_mes_mat_label.recordNo | `"20260929-000412"` |  |
| 28 | shipmentId | String | No (null allowed) | Reference to u_mes_mat_shipment._id | `"SHP-2026-000377"` | Reference: u_mes_mat_shipment._id |
| 29 | shipmentName | String | No (null allowed) | Display value of shipmentId, copied from u_mes_mat_shipment.recordNo | `"2026-000377"` |  |
| 30 | lastCleanedAt | Date | No (null allowed) | Last cleaned date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 31 | cycleCount | Int32 | Yes | Number of trips the returnable container has made | `NumberInt(37)` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Shipped"` | Empty; Filling; Full; Sealed; Shipped; Returned; Under Repair |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 35 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 36 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 37 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 38 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 39 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Empty, Filling, Full, Sealed, Shipped, Returned, Under Repair. Initial state: Empty. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_exe_wipUnit, u_mes_exe_container, u_mes_exe_containerLot, u_mes_mat_inventoryBalance, u_mes_mat_materialMovement, u_mes_mat_label, u_mes_mat_shipmentLineContainer, u_mes_trc_serialNumber, u_mes_trc_asBuiltRecord.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_container.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_container.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_container.js
