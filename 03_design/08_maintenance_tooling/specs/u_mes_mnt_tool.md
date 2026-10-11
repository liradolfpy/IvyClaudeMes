# u_mes_mnt_tool

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | Dies, fixtures, cutting tools, nutrunner spindles, test seals: life limit, life used, status, location |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | TL-<recordNo> |
| Display value used by references | name |
| Keys | 33 (25 required, 8 may be null) |
| Estimated volume per year | 1,000-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per tool, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with toolId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mnt_toolItem | Relationship | item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: TL-<recordNo> | `"TL-SKT-10-0007"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SKT-10-0007"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the tool; used as its display value in other collections | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 6 | toolTypeId | String | Yes | Reference to u_mes_mnt_toolType._id | `"TLT-SOCKET"` | Reference: u_mes_mnt_toolType._id |
| 7 | toolTypeName | String | Yes | Display value of toolTypeId, copied from u_mes_mnt_toolType.name | `"Nutrunner Socket"` |  |
| 8 | toolClass | String | Yes | Tool class | `"Production Tooling"` | Production Tooling; Customer Owned Tooling; Consumable Tooling |
| 9 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 10 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 11 | mountedPosition | String | No (null allowed) | Mounted position | `"Station 1"` |  |
| 12 | supplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 13 | supplierName | String | No (null allowed) | Display value of supplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 14 | drawingNo | String | Yes | Drawing number | `"5110-10-0100"` |  |
| 15 | serialNo | String | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 16 | cavities | Int32 | Yes | Cavities of the tool | `NumberInt(2)` |  |
| 17 | lifeUom | String | Yes | Life uom | `"Shots"` | Shots; Cycles; Pieces; Run Hours |
| 18 | lifeLimit | Int64 | Yes | Life limit | `NumberLong("80000")` |  |
| 19 | lifeUsed | Int64 | Yes | Life used | `NumberLong("61240")` |  |
| 20 | lifeRemaining | Int64 | Yes | Life remaining | `NumberLong("18760")` |  |
| 21 | warningThresholdPct | Decimal128 | Yes | Warning threshold (percent) | `NumberDecimal("80.0")` |  |
| 22 | regrindCount | Int32 | Yes | Regrind count | `NumberInt(0)` |  |
| 23 | maxRegrinds | Int32 | Yes | Maximum regrinds | `NumberInt(0)` |  |
| 24 | storageLocationId | String | Yes | Reference to u_mes_mat_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 25 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 26 | lastMaintainedAt | Date | No (null allowed) | Last maintained date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 27 | nextMaintenanceDueAt | Date | Yes | Next maintenance due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 28 | purchasedAt | Date | Yes | Date and time when the record was purchased | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 29 | costInr | Decimal128 | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 30 | ownedByCustomerId | String | No (null allowed) | Reference to u_mes_mdm_customer._id: owned by customer | `null` | Reference: u_mes_mdm_customer._id |
| 31 | ownedByCustomerName | String | No (null allowed) | Display value of ownedByCustomerId, copied from u_mes_mdm_customer.name | `null` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Available"` | Available; Mounted; In Maintenance; Life Expired; Scrapped |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Available, Mounted, In Maintenance, Life Expired, Scrapped. Initial state: Available. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ toolTypeId: 1 }` | No | Look-up of documents by tool type |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 6 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 7 | `{ ownedByCustomerId: 1 }` | No | Look-up of documents by owned by customer |

## Referenced by

u_mes_prd_billOfProcessStepTool, u_mes_prd_workInstructionStepTool, u_mes_exe_operationExecutionTool, u_mes_exe_changeoverRemovedTool, u_mes_exe_changeoverInstalledTool, u_mes_eqp_torqueResult, u_mes_eqp_leakTestResult, u_mes_mnt_maintenancePlan, u_mes_mnt_maintenanceWorkOrder, u_mes_mnt_toolItem, u_mes_mnt_toolLifeRecord.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_tool.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_tool.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_tool.js
