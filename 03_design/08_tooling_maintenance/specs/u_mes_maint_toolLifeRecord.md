# u_mes_maint_toolLifeRecord

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Tool mount / dismount / usage / regrind events with shots or cycles consumed |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | TLR-<recordNo> |
| Display value used by references | recordNo |
| Keys | 33 (22 required, 11 may be null) |
| Estimated volume per year | ~60,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per tool life record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: TLR-<recordNo> | `"TLR-20260929-000019"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000019"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | toolId | String | Yes | Reference to u_mes_maint_tool._id | `"TL-SKT-10-0007"` | Reference: u_mes_maint_tool._id |
| 6 | toolName | String | Yes | Display value of toolId, copied from u_mes_maint_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 7 | equipmentId | String | No (null allowed) | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 9 | eventType | String | Yes | Event type | `"Usage"` | Mounted; Usage; Dismounted; Regrind; Maintenance; Scrapped |
| 10 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 12 | eventAt | Date | Yes | Event date and time | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 13 | performedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 14 | performedBy | String | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 15 | cyclesThisEvent | Int64 | Yes | Cycles this event | `NumberLong("480")` |  |
| 16 | lifeUsedBefore | Int64 | Yes | Life used before | `NumberLong("60760")` |  |
| 17 | lifeUsedAfter | Int64 | Yes | Life used after | `NumberLong("61240")` |  |
| 18 | lifeRemaining | Int64 | Yes | Life remaining | `NumberLong("18760")` |  |
| 19 | regrindNo | Int32 | No (null allowed) | Regrind number | `null` |  |
| 20 | conditionOnRemoval | String | No (null allowed) | Condition on removal | `"Normal wear"` |  |
| 21 | removalReason | String | No (null allowed) | Removal reason | `"Life limit reached"` |  |
| 22 | measuredWearMm | Decimal128 | No (null allowed) | Measured wear (mm) | `NumberDecimal("0.12")` |  |
| 23 | maintenanceWorkOrderId | String | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `"MWO-2026-000341"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 24 | maintenanceWorkOrderName | String | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Nutrunner rundown fault, station 1"` |  |
| 25 | remarks | String | No (null allowed) | Remarks of the tool life record | `"No abnormality observed"` |  |
| 26 | status | String | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 27 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 29 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 31 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 32 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ toolId: 1 }` | No | Look-up of documents by tool |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ maintenanceWorkOrderId: 1 }` | No | Look-up of documents by maintenance work order |
| 7 | `{ siteId: 1, eventAt: -1 }` | No | Time-ordered lists and reports by event at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_toolLifeRecord.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_toolLifeRecord.js
- Sample document: 03_design/08_tooling_maintenance/samples/u_mes_maint_toolLifeRecord.js
