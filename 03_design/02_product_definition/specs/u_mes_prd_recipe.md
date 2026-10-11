# u_mes_prd_recipe

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Machine parameter sets with set-points and limits (die temperature, furnace profile, CNC program, torque program, leak-test program) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | RCP-<recordNo> |
| Display value used by references | name |
| Keys | 25 (16 required, 9 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per recipe, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with recipeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prd_recipeParameter | Child | parameter |
| u_mes_prd_recipeStage | Child | stage |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: RCP-<recordNo> | `"RCP-TRQ-PRG-07"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-PRG-07"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the recipe; used as its display value in other collections | `"Bleed screw M10 torque program"` |  |
| 6 | equipmentId | String | Yes | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 7 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 8 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 9 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | operationId | String | Yes | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 11 | operationName | String | Yes | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 12 | version | Int32 | Yes | Version of the recipe | `NumberInt(3)` |  |
| 13 | recipeType | String | Yes | Recipe type | `"Tightening Program"` | Die Casting Parameters; Furnace Profile; CNC Program; Washing Program; Anodising Program; Tightening Program; Leak Test Program; Laser Marking Program |
| 14 | programNo | String | Yes | Program number | `"PSET-07"` |  |
| 15 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 16 | effectiveTo | Date | No (null allowed) | Effective to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 17 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prd_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 18 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 19 | checksum | String | Yes | Checksum of the parameter set used to detect an unapproved change at the controller | `"9f2c4a1be07d53c6"` |  |
| 20 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 21 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 22 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 23 | lastDownloadedAt | Date | No (null allowed) | Last downloaded date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 24 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 25 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 6 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |

## Referenced by

u_mes_prd_billOfProcessStep, u_mes_prd_recipeParameter, u_mes_prd_recipeStage, u_mes_exe_operationExecution, u_mes_exe_changeover, u_mes_eqp_torqueResult, u_mes_eqp_leakTestResult.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_recipe.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_recipe.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_recipe.js
