# u_mes_maint_sparePartTransaction

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Spare-part issue, return, receipt, adjustment and scrap with work order and equipment. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 30 (25 required, 5 may be null) |
| Estimated volume per year | about 5,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per spare part transaction, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1329000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SPT-20260915-00088"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | sparePartId | String | - | Yes | Reference to u_mes_maint_sparePart._id | `"1224000000000001"` | Reference: u_mes_maint_sparePart._id |
| 6 | sparePartName | String | - | Yes | Display value of sparePartId, copied from u_mes_maint_sparePart.description | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 7 | transactionType | String | - | Yes | Transaction type | `"Issue"` | Issue; Return; Receipt; Adjustment; Scrap |
| 8 | quantity | Decimal128 | - | Yes | Quantity (positive) | `NumberDecimal("1")` |  |
| 9 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 10 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 11 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `"1220000000000007"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 12 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Nutrunner rundown fault, station 1"` |  |
| 13 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 14 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 15 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000003"` | Reference: u_mes_matl_storageLocation._id |
| 16 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Warehouse A, rack 05, bin 03"` |  |
| 17 | scanVerified | Boolean | - | Yes | Part barcode scanned | `true` |  |
| 18 | unitCostInr | Decimal128 | - | Yes | Unit cost in INR | `NumberDecimal("4320.00")` |  |
| 19 | transactedAt | Date | Datetime | Yes | Transaction time | `ISODate("2026-09-21T07:47:00.000+0000")` |  |
| 20 | transactedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'transacted' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 21 | transactedBy | String | - | Yes | Display name of the user in transactedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 22 | erpDocumentNo | String | - | No (null allowed) | ERP document number | `"4900127731"` |  |
| 23 | status | String | - | Yes | Primary lifecycle state of the document | `"Posted"` | Posted; Reversed |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 25 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-21T07:42:40.000+0000")` |  |
| 26 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 27 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 28 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-21T07:47:00.000+0000")` |  |
| 29 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 30 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Posted, Reversed. Initial state: Posted. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ sparePartId: 1 }` | No | Look-up of documents by spare part |
| 4 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 5 | `{ maintenanceWorkOrderId: 1 }` | No | Look-up of documents by maintenance work order |
| 6 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 7 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 8 | `{ siteId: 1, transactedAt: -1 }` | No | Time-ordered lists and reports by transacted at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_sparePartTransaction.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_sparePartTransaction.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_sparePartTransaction.js
