# u_mes_maint_tool

| Property | Value |
|---|---|
| Module | ToolingAndMaintenance (maint) |
| Purpose | Dies, fixtures, cutting tools, nutrunner spindles, test seals: life limit, life used, status, location |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 39 (27 required, 12 may be null) |
| Estimated volume per year | 1,000-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per tool, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with toolId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_maint_toolItem | Relationship | item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1226000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DIE-5110-LH-02"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the tool; used as its display value in other collections | `"Gravity die, caliper body LH, die 2"` |  |
| 7 | toolTypeId | String | - | Yes | Reference to u_mes_maint_toolType._id | `"1288000000000001"` | Reference: u_mes_maint_toolType._id |
| 8 | toolTypeName | String | - | Yes | Display value of toolTypeId, copied from u_mes_maint_toolType.name | `"Die"` |  |
| 9 | toolClass | String | - | Yes | Tool class | `"Production Tooling"` | Production Tooling; Customer Owned Tooling; Consumable Tooling; Fixture |
| 10 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 11 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 12 | mountedPosition | String | - | No (null allowed) | Mounted position | `"Station 1"` |  |
| 13 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `"1038000000000004"` | Reference: u_mes_mast_supplier._id |
| 14 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Western Aluminium Alloys Ltd."` |  |
| 15 | drawingNo | String | - | Yes | Drawing number | `"5110-10-0100"` |  |
| 16 | serialNo | String | - | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 17 | cavities | Int32 | - | Yes | Cavities of the tool | `NumberInt(2)` |  |
| 18 | lifeUom | String | - | Yes | Life uom | `"Shots"` | Shots; Cycles; Pieces; Run Hours; Batches; Tablets |
| 19 | lifeLimit | Int64 | - | Yes | Life limit | `NumberLong("80000")` |  |
| 20 | lifeUsed | Int64 | - | Yes | Life used | `NumberLong("61600")` |  |
| 21 | lifeRemaining | Int64 | - | Yes | Life remaining | `NumberLong("18400")` |  |
| 22 | warningThresholdPct | Decimal128 | - | Yes | Warning threshold (percent) | `80.0` |  |
| 23 | regrindCount | Int32 | - | Yes | Regrind count | `NumberInt(0)` |  |
| 24 | maxRegrinds | Int32 | - | Yes | Maximum regrinds | `NumberInt(0)` |  |
| 25 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 26 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 27 | lastMaintainedAt | Date | Datetime | No (null allowed) | Last maintained date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 28 | nextMaintenanceDueAt | Date | Date | Yes | Next maintenance due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 29 | purchasedAt | Date | Datetime | Yes | Date and time when the record was purchased. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2019-01-04T00:00:00.000+0000")` |  |
| 30 | costInr | Decimal128 | - | Yes | Cost (Indian rupees) | `8640.00` |  |
| 31 | ownedByCustomerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id: owned by customer | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 32 | ownedByCustomerName | String | - | No (null allowed) | Display value of ownedByCustomerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 33 | blockAtLifeLimit | Boolean | - | Yes | True when production is blocked once life used reaches the life limit | `true` |  |
| 34 | lastCertifiedAt | Date | Datetime | No (null allowed) | Time of the last fixture certification | `null` |  |
| 35 | certificationDueDate | Date | Date | No (null allowed) | Next fixture certification due date | `null` |  |
| 36 | certificateControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: certificate controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 37 | certificateControlledDocumentName | String | - | No (null allowed) | Display value of certificateControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 38 | status | String | - | Yes | Primary lifecycle state of the document | `"Mounted"` | Available; Mounted; In Maintenance; Life Expired; Scrapped |
| 39 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Available, Mounted, In Maintenance, Life Expired, Scrapped. Initial state: Available. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_prod_billOfProcessStepTool, u_mes_prod_workInstructionStepTool, u_mes_plan_operationExecutionTool, u_mes_plan_changeoverRemovedTool, u_mes_plan_changeoverInstalledTool, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_maintenancePlan, u_mes_maint_maintenanceWorkOrder, u_mes_maint_toolItem, u_mes_maint_toolLifeRecord.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_tool.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_tool.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_tool.js
