# u_mes_maint_sparePart

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Maintenance spares with stock, minimum, location, where-used |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 27 (21 required, 6 may be null) |
| Estimated volume per year | 2,000-8,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per spare part, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with sparePartId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_maint_sparePartUsedOnEquipment | Relationship | used on equipment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1224000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SP-004417"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | description | String | - | Yes | Description of the spare part | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 7 | category | String | - | Yes | Category of the spare part | `"Electrical"` | Mechanical; Electrical; Process; Material; Quality; Organisation; Planned |
| 8 | manufacturerId | String | - | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"1260000000000007"` | Reference: u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | - | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"Atlas Copco"` |  |
| 10 | manufacturerPartNo | String | - | Yes | Manufacturer part number | `"4220 3311 10"` |  |
| 11 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `"1038000000000003"` | Reference: u_mes_mast_supplier._id |
| 12 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Bharat Fasteners and Fittings Ltd."` |  |
| 13 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 15 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 16 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 17 | stockQuantity | Decimal128 | - | Yes | Stock quantity | `NumberDecimal("6")` |  |
| 18 | minimumQuantity | Decimal128 | - | Yes | Minimum quantity | `NumberDecimal("2")` |  |
| 19 | reorderQuantity | Decimal128 | - | Yes | Reorder quantity | `NumberDecimal("4")` |  |
| 20 | leadTimeDays | Int32 | - | Yes | Lead time (days) | `NumberInt(21)` |  |
| 21 | unitCostInr | Decimal128 | - | Yes | Unit cost (Indian rupees) | `NumberDecimal("4320.00")` |  |
| 22 | criticality | String | - | Yes | A = failure stops the line or affects safety, B = reduced output, C = no immediate effect | `"A"` | A; B; C |
| 23 | lastIssuedAt | Date | Datetime | No (null allowed) | Last issued date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | lastReceivedAt | Date | Datetime | No (null allowed) | Last received date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 25 | isInsuranceSpare | Boolean | - | Yes | True when the record is insurance spare | `false` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Obsolete |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Obsolete. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ manufacturerId: 1 }` | No | Look-up of documents by manufacturer |
| 4 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 6 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |

## Referenced by

u_mes_maint_maintenancePlanRequiredSparePart, u_mes_maint_maintenanceWorkOrderUsedSparePart, u_mes_maint_sparePartUsedOnEquipment, u_mes_maint_sparePartTransaction.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_sparePart.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_sparePart.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_sparePart.js
