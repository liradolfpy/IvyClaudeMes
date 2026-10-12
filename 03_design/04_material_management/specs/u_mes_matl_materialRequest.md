# u_mes_matl_materialRequest

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Line-side replenishment calls (e-kanban) from a work centre to stores |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 41 (29 required, 12 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 9 | requestedQuantity | Decimal128 | - | Yes | Requested quantity | `NumberDecimal("500")` |  |
| 10 | deliveredQuantity | Decimal128 | - | Yes | Delivered quantity | `NumberDecimal("500")` |  |
| 11 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 12 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 13 | requestType | String | - | Yes | Request type | `"Kanban"` | Kanban; Andon Call; Manual |
| 14 | triggerSource | String | - | Yes | Trigger source | `"Minimum Level Sensor"` | Minimum Level Sensor; Operator; Schedule |
| 15 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 16 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 17 | requestedAt | Date | Datetime | Yes | Date and time when the record was requested. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 18 | fromLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: from location | `"1112000000000001"` | Reference: u_mes_matl_storageLocation._id |
| 19 | fromLocationName | String | - | No (null allowed) | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `"Raw material yard, ingot bay"` |  |
| 20 | toLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: to location | `"1112000000000004"` | Reference: u_mes_matl_storageLocation._id |
| 21 | toLocationName | String | - | Yes | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side store, foundry"` |  |
| 22 | priority | String | - | Yes | Priority of the material request | `"Normal"` | Low; Normal; High; Urgent |
| 23 | acknowledgedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 24 | acknowledgedBy | String | - | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 25 | acknowledgedAt | Date | Datetime | No (null allowed) | Date and time when the record was acknowledged. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 26 | deliveredAt | Date | Datetime | No (null allowed) | Date and time when the record was delivered. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 27 | responseMinutes | Int32 | - | Yes | Response (minutes) | `NumberInt(6)` |  |
| 28 | andonEventId | String | - | No (null allowed) | Reference to u_mes_plan_andonEvent._id | `null` | Reference: u_mes_plan_andonEvent._id |
| 29 | andonEventName | String | - | No (null allowed) | Display value of andonEventId, copied from u_mes_plan_andonEvent.description | `null` |  |
| 30 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 31 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 32 | replenishmentRuleId | String | - | No (null allowed) | Reference to u_mes_matl_replenishmentRule._id | `null` | Reference: u_mes_matl_replenishmentRule._id |
| 33 | replenishmentRuleName | String | - | No (null allowed) | Display value of replenishmentRuleId, copied from u_mes_matl_replenishmentRule.recordNo | `null` |  |
| 34 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Delivered; Cancelled |
| 35 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 36 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 37 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 38 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 39 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 40 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 41 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

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
