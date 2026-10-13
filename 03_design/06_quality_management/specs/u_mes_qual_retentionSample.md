# u_mes_qual_retentionSample

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Reserve or retention sample taken from a lot, with quantity, storage location, retention date and withdrawals. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 34 (24 required, 10 may be null) |
| Estimated volume per year | about 2,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per retention sample, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1360000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RSM-L260915-GDC-014-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 7 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 8 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 9 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 11 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `null` | Reference: u_mes_trac_serialNumber._id |
| 12 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `null` |  |
| 13 | sampleType | String | - | Yes | Kind of sample | `"Retention Sample"` | Reserve Sample; Retention Sample; Master Sample; Boundary Sample |
| 14 | sampleQuantity | Int32 | - | Yes | Quantity retained | `NumberInt(2)` |  |
| 15 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 17 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000003"` | Reference: u_mes_matl_storageLocation._id |
| 18 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Warehouse A, rack 05, bin 03"` |  |
| 19 | collectedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'collected' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | collectedBy | String | - | Yes | Display name of the user in collectedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 21 | collectedAt | Date | Datetime | Yes | Time the sample was taken | `ISODate("2026-09-17T14:40:00.000+0000")` |  |
| 22 | retainUntilDate | Date | Date | Yes | Last day the sample must be kept | `ISODate("2027-12-31T00:00:00.000+0000")` |  |
| 23 | withdrawnAt | Date | Datetime | No (null allowed) | Time the sample was withdrawn | `null` |  |
| 24 | withdrawalReason | String | - | No (null allowed) | Why the sample was withdrawn | `null` |  |
| 25 | customerComplaintId | String | - | No (null allowed) | Reference to u_mes_qual_customerComplaint._id | `null` | Reference: u_mes_qual_customerComplaint._id |
| 26 | customerComplaintName | String | - | No (null allowed) | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `null` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Stored"` | Stored; Withdrawn; Destroyed |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T14:40:00.000+0000")` |  |
| 30 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 32 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T14:40:00.000+0000")` |  |
| 33 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Stored, Withdrawn, Destroyed. Initial state: Stored. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 7 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 8 | `{ siteId: 1, collectedAt: -1 }` | No | Time-ordered lists and reports by collected at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_retentionSample.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_retentionSample.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_retentionSample.js
