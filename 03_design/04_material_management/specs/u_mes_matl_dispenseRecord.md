# u_mes_matl_dispenseRecord

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Weighing or counting of a material lot for an order, with target, tolerance, tare, gross and net weight and the second-person or system verification. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 41 (33 required, 8 may be null) |
| Estimated volume per year | about 20,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per dispense record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1359000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DSP-20260917-0011"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000010"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Aluminium alloy ingot AlSi7Mg0.3 (A356)"` |  |
| 9 | lotId | String | - | Yes | Reference to u_mes_plan_lot._id | `"1096000000000009"` | Reference: u_mes_plan_lot._id |
| 10 | lotName | String | - | Yes | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260910-ING-003"` |  |
| 11 | dispenseMethod | String | - | Yes | How the quantity is determined | `"Gravimetric Weighing"` | Gravimetric Weighing; Count By Weight |
| 12 | targetWeight | Decimal128 | - | Yes | Target net weight | `NumberDecimal("280.000")` |  |
| 13 | tolerancePct | Decimal128 | - | Yes | Allowed deviation from the target (percent) | `NumberDecimal("0.50")` |  |
| 14 | tareWeight | Decimal128 | - | Yes | Tare weight of the container | `NumberDecimal("42.300")` |  |
| 15 | grossWeight | Decimal128 | - | Yes | Gross weight | `NumberDecimal("322.450")` |  |
| 16 | netWeight | Decimal128 | - | Yes | Net weight | `NumberDecimal("280.150")` |  |
| 17 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000002"` | Reference: u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Kilogram"` |  |
| 19 | pieceCount | Int32 | - | No (null allowed) | Pieces calculated by count-by-weight; null for bulk material | `null` |  |
| 20 | withinTolerance | Boolean | - | Yes | Net weight within tolerance | `true` |  |
| 21 | balanceGaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id: balance gauge | `null` | Reference: u_mes_qual_gauge._id |
| 22 | balanceGaugeName | String | - | No (null allowed) | Display value of balanceGaugeId, copied from u_mes_qual_gauge.name | `null` |  |
| 23 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000001"` | Reference: u_mes_matl_storageLocation._id |
| 24 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Raw material yard, ingot bay"` |  |
| 25 | dispensedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'dispensed' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 26 | dispensedBy | String | - | Yes | Display name of the user in dispensedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 27 | dispensedAt | Date | Datetime | Yes | Time of dispensing | `ISODate("2026-09-17T06:05:00.000+0000")` |  |
| 28 | verificationMethod | String | - | Yes | How the dispense is verified | `"System Check"` | Second Person; System Check |
| 29 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `null` | Reference: u_mes_mast_user._id |
| 30 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `null` |  |
| 31 | verifiedAt | Date | Datetime | No (null allowed) | Time of verification | `ISODate("2026-09-17T06:05:20.000+0000")` |  |
| 32 | labelId | String | - | No (null allowed) | Reference to u_mes_matl_label._id | `null` | Reference: u_mes_matl_label._id |
| 33 | labelName | String | - | No (null allowed) | Display value of labelId, copied from u_mes_matl_label.recordNo | `null` |  |
| 34 | status | String | - | Yes | Primary lifecycle state of the document | `"Issued"` | Dispensed; Verified; Issued; Returned; Rejected |
| 35 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 36 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:05:00.000+0000")` |  |
| 37 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 38 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 39 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:05:20.000+0000")` |  |
| 40 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 41 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Dispensed, Verified, Issued, Returned, Rejected. Initial state: Dispensed. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 7 | `{ balanceGaugeId: 1 }` | No | Look-up of documents by balance gauge |
| 8 | `{ siteId: 1, dispensedAt: -1 }` | No | Time-ordered lists and reports by dispensed at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_dispenseRecord.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_dispenseRecord.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_dispenseRecord.js
