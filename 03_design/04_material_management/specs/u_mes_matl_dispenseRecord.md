# u_mes_matl_dispenseRecord

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Weighing or counting of a material lot for an order, with target, tolerance, tare, gross and net weight and the second-person or system verification. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 42 (34 required, 8 may be null) |
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
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000014"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5G26091"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000015"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Paracetamol IP, active pharmaceutical ingredient"` |  |
| 10 | lotId | String | - | Yes | Reference to u_mes_plan_lot._id | `"1096000000000015"` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | - | Yes | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"R260904-API-011"` |  |
| 12 | dispenseMethod | String | - | Yes | How the quantity is determined | `"Gravimetric Weighing"` | Gravimetric Weighing; Count By Weight |
| 13 | targetWeight | Decimal128 | - | Yes | Target net weight | `NumberDecimal("250.000")` |  |
| 14 | tolerancePct | Decimal128 | - | Yes | Allowed deviation from the target (percent) | `NumberDecimal("0.50")` |  |
| 15 | tareWeight | Decimal128 | - | Yes | Tare weight of the container | `NumberDecimal("12.400")` |  |
| 16 | grossWeight | Decimal128 | - | Yes | Gross weight | `NumberDecimal("262.550")` |  |
| 17 | netWeight | Decimal128 | - | Yes | Net weight | `NumberDecimal("250.150")` |  |
| 18 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000012"` | Reference: u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Kilogram"` |  |
| 20 | pieceCount | Int32 | - | No (null allowed) | Pieces calculated by count-by-weight; null for bulk material | `null` |  |
| 21 | withinTolerance | Boolean | - | Yes | Net weight within tolerance | `true` |  |
| 22 | balanceGaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id: balance gauge | `"1189000000000011"` | Reference: u_mes_qual_gauge._id |
| 23 | balanceGaugeName | String | - | No (null allowed) | Display value of balanceGaugeId, copied from u_mes_qual_gauge.name | `"Platform balance 150 kg, d = 10 g"` |  |
| 24 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000014"` | Reference: u_mes_matl_storageLocation._id |
| 25 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Staging area, dispensing"` |  |
| 26 | dispensedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'dispensed' | `"1029000000000018"` | Reference: u_mes_mast_user._id |
| 27 | dispensedBy | String | - | Yes | Display name of the user in dispensedById, copied from u_mes_mast_user.fullName | `"Prakash Jagtap"` |  |
| 28 | dispensedAt | Date | Datetime | Yes | Time of dispensing | `ISODate("2026-09-17T06:05:00.000+0000")` |  |
| 29 | verificationMethod | String | - | Yes | How the dispense is verified | `"System Check"` | Second Person; System Check |
| 30 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `null` | Reference: u_mes_mast_user._id |
| 31 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `null` |  |
| 32 | verifiedAt | Date | Datetime | No (null allowed) | Time of verification | `ISODate("2026-09-17T06:05:20.000+0000")` |  |
| 33 | labelId | String | - | No (null allowed) | Reference to u_mes_matl_label._id | `null` | Reference: u_mes_matl_label._id |
| 34 | labelName | String | - | No (null allowed) | Display value of labelId, copied from u_mes_matl_label.recordNo | `null` |  |
| 35 | status | String | - | Yes | Primary lifecycle state of the document | `"Issued"` | Dispensed; Verified; Issued; Returned; Rejected |
| 36 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:05:00.000+0000")` |  |
| 38 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000018"` | Reference: u_mes_mast_user._id |
| 39 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Prakash Jagtap"` |  |
| 40 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:05:20.000+0000")` |  |
| 41 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000018"` | Reference: u_mes_mast_user._id |
| 42 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Prakash Jagtap"` |  |

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
