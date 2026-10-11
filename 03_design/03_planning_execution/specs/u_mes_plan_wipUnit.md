# u_mes_plan_wipUnit

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Serialised unit in production (shop-floor control number): current operation, status, quality state |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | WU-<recordNo> |
| Display value used by references | recordNo |
| Keys | 47 (30 required, 17 may be null) |
| Estimated volume per year | ~720,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per wip unit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with wipUnitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_wipUnitCompletedStep | Value list | completed step |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: WU-<recordNo> | `"WU-U260929A0184"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"U260929A0184"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | Yes | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 7 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 10 | productVariantId | String | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"VAR-FBC-LH-STD"` | Reference: u_mes_prod_productVariant._id |
| 11 | productVariantName | String | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH Standard"` |  |
| 12 | serialNumberId | String | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"SN-VB26272A00184"` | Reference: u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26272A00184"` |  |
| 14 | bodyLotId | String | No (null allowed) | Reference to u_mes_plan_lot._id: body lot | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 15 | bodyLotName | String | No (null allowed) | Display value of bodyLotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 16 | routingId | String | Yes | Reference to u_mes_prod_routing._id | `"RTG-5110-10-0100-R01"` | Reference: u_mes_prod_routing._id |
| 17 | routingName | String | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH assembly routing"` |  |
| 18 | currentStepNo | Int32 | Yes | Current step number | `NumberInt(70)` |  |
| 19 | currentOperationId | String | Yes | Reference to u_mes_prod_operation._id: current operation | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 20 | currentOperationName | String | Yes | Display value of currentOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 21 | currentWorkCenterId | String | Yes | Reference to u_mes_mast_workCenter._id: current work center | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 22 | currentWorkCenterName | String | Yes | Display value of currentWorkCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 23 | qualityStatus | String | Yes | Quality status | `"Released"` | Released; Under Inspection; On Hold; Rejected |
| 24 | onHold | Boolean | Yes | True when: on hold | `false` |  |
| 25 | qualityHoldId | String | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `null` | Reference: u_mes_qual_qualityHold._id |
| 26 | qualityHoldName | String | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `null` |  |
| 27 | reworkCount | Int32 | Yes | Rework count | `NumberInt(0)` |  |
| 28 | createdAtOperationId | String | No (null allowed) | Reference to u_mes_prod_operation._id: created at operation | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 29 | createdAtOperationName | String | No (null allowed) | Display value of createdAtOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 30 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 31 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 32 | lastOperationExecutionId | String | No (null allowed) | Reference to u_mes_plan_operationExecution._id: last operation execution | `"OPX-20260929-000184"` | Reference: u_mes_plan_operationExecution._id |
| 33 | lastOperationExecutionName | String | No (null allowed) | Display value of lastOperationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"20260929-000184"` |  |
| 34 | containerId | String | No (null allowed) | Reference to u_mes_plan_container._id | `"CNT-BIN-000731"` | Reference: u_mes_plan_container._id |
| 35 | containerName | String | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `"BIN-000731"` |  |
| 36 | bodyCavityNo | Int32 | Yes | Body cavity number | `NumberInt(1)` |  |
| 37 | castDateCode | String | Yes | Date, shift and cavity code cast into the body | `"26272A1"` |  |
| 38 | scrappedAt | Date | No (null allowed) | Date and time when the record was scrapped | `null` |  |
| 39 | shippedAt | Date | No (null allowed) | Date and time when the record was shipped | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 40 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Created; In Process; On Hold; In Rework; Completed; Packed; Shipped; Scrapped |
| 41 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 42 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 43 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 44 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 45 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 46 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 47 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Created, In Process, On Hold, In Rework, Completed, Packed, Shipped, Scrapped. Initial state: Created. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 7 | `{ bodyLotId: 1 }` | No | Look-up of documents by body lot |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_wipUnitCompletedStep, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_trac_serialNumber, u_mes_trac_genealogyLink, u_mes_trac_asBuiltRecord, u_mes_qual_inspectionResult, u_mes_qual_reworkOrderWipUnit, u_mes_qual_scrapRecord, u_mes_perf_torqueResult, u_mes_perf_leakTestResult.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_wipUnit.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_wipUnit.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_wipUnit.js
