# u_mes_prod_recipe

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Machine parameter sets with set-points and limits (die temperature, furnace profile, CNC program, torque program, leak-test program) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 36 (18 required, 18 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per recipe, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with recipeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_recipeParameter | Child | parameter |
| u_mes_prod_recipeStage | Child | stage |
| u_mes_prod_recipeProductVariant | Relationship | product variant |
| u_mes_prod_recipeControlledDocument | Relationship | controlled document |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1073000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-5110-LH-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the recipe; used as its display value in other collections | `"Caliper body LH casting parameters"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 8 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 10 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 11 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 12 | version | Int32 | - | Yes | Version of the recipe | `NumberInt(1)` |  |
| 13 | recipeType | String | - | Yes | Recipe type | `"Die Casting Parameters"` | Die Casting Parameters; Furnace Profile; CNC Program; Washing Program; Anodising Program; Tightening Program; Leak Test Program; Laser Marking Program; Press Program; Dispensing Program; Vision Job |
| 14 | programNo | String | - | Yes | Program number | `"GDC-P12"` |  |
| 15 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 16 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 17 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000001"` | Reference: u_mes_prod_engineeringChange._id |
| 18 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 19 | checksum | String | - | Yes | Checksum of the parameter set used to detect an unapproved change at the controller | `"9f2c4a1be07d53c6"` |  |
| 20 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 21 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 22 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 23 | lastDownloadedAt | Date | Datetime | No (null allowed) | Last downloaded date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | previousVersionRecipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id: previous version recipe | `null` | Reference: u_mes_prod_recipe._id |
| 25 | previousVersionRecipeName | String | - | No (null allowed) | Display value of previousVersionRecipeId, copied from u_mes_prod_recipe.name | `null` |  |
| 26 | changeReasonText | String | - | No (null allowed) | Reason for the change from the previous version | `null` |  |
| 27 | releasedAt | Date | Datetime | No (null allowed) | Time the version was released for production | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 28 | isGoldenRecipe | Boolean | - | Yes | True when the version is the approved golden recipe for its variant and machine | `false` |  |
| 29 | goldenDesignatedAt | Date | Datetime | No (null allowed) | Time the version was designated golden recipe | `null` |  |
| 30 | goldenDesignatedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'golden designated' | `null` | Reference: u_mes_mast_user._id |
| 31 | goldenDesignatedBy | String | - | No (null allowed) | Display name of the user in goldenDesignatedById, copied from u_mes_mast_user.fullName | `null` |  |
| 32 | origin | String | - | Yes | Where the parameter set came from | `"Engineering"` | Engineering; Optimisation Model; Simulation Study |
| 33 | analyticsModelId | String | - | No (null allowed) | Reference to u_mes_syst_analyticsModel._id | `null` | Reference: u_mes_syst_analyticsModel._id |
| 34 | analyticsModelName | String | - | No (null allowed) | Display value of analyticsModelId, copied from u_mes_syst_analyticsModel.name | `null` |  |
| 35 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 36 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 6 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 7 | `{ previousVersionRecipeId: 1 }` | No | Look-up of documents by previous version recipe |

## Referenced by

u_mes_prod_billOfProcessStep, u_mes_prod_recipe, u_mes_prod_recipeParameter, u_mes_prod_recipeStage, u_mes_plan_operationExecution, u_mes_plan_changeover, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecordOperation, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_prod_recipeProductVariant, u_mes_prod_recipeControlledDocument, u_mes_plan_recipeDownload, u_mes_qual_curveEnvelope, u_mes_syst_simulationStudy.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_recipe.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_recipe.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_recipe.js
