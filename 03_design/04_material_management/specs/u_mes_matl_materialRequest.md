# u_mes_matl_materialRequest

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Line-side replenishment calls (e-kanban) from a work centre to stores |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 42 (30 required, 12 may be null) |
| Estimated volume per year | ~80,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per material request, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1120000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MRQ-2026-000445"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 10 | requestedQuantity | Decimal128 | - | Yes | Requested quantity | `500` |  |
| 11 | deliveredQuantity | Decimal128 | - | Yes | Delivered quantity | `500` |  |
| 12 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 14 | requestType | String | - | Yes | Request type | `"Kanban"` | Kanban; Andon Call; Manual |
| 15 | triggerSource | String | - | Yes | Trigger source | `"Minimum Level Sensor"` | Minimum Level Sensor; Operator; Schedule |
| 16 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 17 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 18 | requestedAt | Date | Datetime | Yes | Date and time when the record was requested. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 19 | fromLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: from location | `"1112000000000001"` | Reference: u_mes_matl_storageLocation._id |
| 20 | fromLocationName | String | - | No (null allowed) | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `"Raw material yard, ingot bay"` |  |
| 21 | toLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: to location | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 22 | toLocationName | String | - | Yes | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 23 | priority | String | - | Yes | Priority of the material request | `"Normal"` | Low; Normal; High; Urgent |
| 24 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 25 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 26 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 27 | deliveredAt | Date | Datetime | No (null allowed) | Date and time when the record was delivered. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 28 | responseMinutes | Int32 | - | Yes | Response (minutes) | `NumberInt(6)` |  |
| 29 | andonEventId | String | - | No (null allowed) | Reference to u_mes_plan_andonEvent._id | `null` | Reference: u_mes_plan_andonEvent._id |
| 30 | andonEventName | String | - | No (null allowed) | Display value of andonEventId, copied from u_mes_plan_andonEvent.description | `null` |  |
| 31 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 32 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 33 | replenishmentRuleId | String | - | No (null allowed) | Reference to u_mes_matl_replenishmentRule._id | `null` | Reference: u_mes_matl_replenishmentRule._id |
| 34 | replenishmentRuleName | String | - | No (null allowed) | Display value of replenishmentRuleId, copied from u_mes_matl_replenishmentRule.recordNo | `null` |  |
| 35 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Delivered; Cancelled |
| 36 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 38 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 39 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 40 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 41 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 42 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Raised, Acknowledged, Delivered, Cancelled. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 6 | `{ fromLocationId: 1 }` | No | Look-up of documents by from location |
| 7 | `{ toLocationId: 1 }` | No | Look-up of documents by to location |
| 8 | `{ siteId: 1, requestedAt: -1 }` | No | Time-ordered lists and reports by requested at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_materialRequest.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_materialRequest.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_materialRequest.js
