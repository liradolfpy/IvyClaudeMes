# u_mes_prod_operation

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Standard operation library (casting, T6, machining ... packing) reused by routings |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 21 (20 required, 1 may be null) |
| Estimated volume per year | 50-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per operation, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with operationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_operationRequiredSkill | Relationship | required skill |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1051000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OP010"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the operation; used as its display value in other collections | `"Gravity die casting"` |  |
| 6 | operationType | String | - | Yes | Operation type | `"Casting"` | Casting; Heat Treatment; Machining; Cleaning; Surface Treatment; Assembly; Test; Marking; Inspection; Packing |
| 7 | description | String | - | Yes | Description of the operation | `"Fill the die cavity completely with sound metal"` |  |
| 8 | defaultWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: default work center | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 9 | defaultWorkCenterName | String | - | Yes | Display value of defaultWorkCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 10 | trackingGrain | String | - | Yes | Level at which material is tracked at this point | `"Lot"` | Lot; Unit; Container |
| 11 | standardCycleTimeSec | Decimal128 | - | Yes | Standard cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 12 | standardSetupTimeMin | Int32 | - | Yes | Standard setup time (minutes) | `NumberInt(45)` |  |
| 13 | standardManning | Int32 | - | Yes | Standard manning | `NumberInt(1)` |  |
| 14 | isInspection | Boolean | - | Yes | True when the record is inspection | `false` |  |
| 15 | isSpecialProcess | Boolean | - | Yes | True when the record is special process | `true` |  |
| 16 | specialProcessStandard | String | - | No (null allowed) | AIAG special process assessment that applies | `"CQI-27"` |  |
| 17 | requiresFirstOffApproval | Boolean | - | Yes | True when first off approval is required | `true` |  |
| 18 | erpControlKey | String | - | Yes | ERP control key | `"PP01"` |  |
| 19 | sequenceHint | Int32 | - | Yes | Default position of the operation in a routing | `NumberInt(10)` |  |
| 20 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ defaultWorkCenterId: 1 }` | No | Look-up of documents by default work center |

## Referenced by

u_mes_mast_workCenterOperation, u_mes_mast_skillOperation, u_mes_prod_billOfMaterialComponent, u_mes_prod_operationRequiredSkill, u_mes_prod_routingStep, u_mes_prod_billOfProcessStep, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_plan_lot, u_mes_plan_labourBooking, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_trac_asBuiltRecordOperation, u_mes_qual_characteristic, u_mes_qual_controlPlanLine, u_mes_qual_inspectionPlan, u_mes_qual_checkSheet, u_mes_qual_inspectionResult, u_mes_qual_defectCodeApplicableOperation, u_mes_qual_nonconformance, u_mes_qual_reworkOrderStep, u_mes_qual_scrapRecord, u_mes_qual_pfmeaLine, u_mes_syst_operatorAppOperation, u_mes_qual_curveEnvelope, u_mes_qual_defectRecord, u_mes_syst_interlockRule.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_operation.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_operation.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_operation.js
