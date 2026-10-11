# u_mes_maint_sparePart

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Maintenance spares with stock, minimum, location, where-used |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | SPR-<recordNo> |
| Display value used by references | description |
| Keys | 26 (20 required, 6 may be null) |
| Estimated volume per year | 2,000-8,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per spare part, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with sparePartId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_maint_sparePartUsedOnEquipment | Relationship | used on equipment |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SPR-<recordNo> | `"SPR-SP-004417"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SP-004417"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | description | String | Yes | Description of the spare part | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 6 | category | String | Yes | Category of the spare part | `"Mechanical"` | Mechanical; Electrical; Process; Material; Quality; Organisation; Planned |
| 7 | manufacturerId | String | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"MFR-ATLAS-COPCO"` | Reference: u_mes_mast_manufacturer._id |
| 8 | manufacturerName | String | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"Atlas Copco"` |  |
| 9 | manufacturerPartNo | String | Yes | Manufacturer part number | `"4220 3311 10"` |  |
| 10 | supplierId | String | No (null allowed) | Reference to u_mes_mast_supplier._id | `"SUP-S1042"` | Reference: u_mes_mast_supplier._id |
| 11 | supplierName | String | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 12 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"UOM-EA"` | Reference: u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 14 | storageLocationId | String | Yes | Reference to u_mes_matl_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_matl_storageLocation._id |
| 15 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 16 | stockQuantity | Decimal128 | Yes | Stock quantity | `NumberDecimal("6")` |  |
| 17 | minimumQuantity | Decimal128 | Yes | Minimum quantity | `NumberDecimal("2")` |  |
| 18 | reorderQuantity | Decimal128 | Yes | Reorder quantity | `NumberDecimal("4")` |  |
| 19 | leadTimeDays | Int32 | Yes | Lead time (days) | `NumberInt(21)` |  |
| 20 | unitCostInr | Decimal128 | Yes | Unit cost (Indian rupees) | `NumberDecimal("4320.00")` |  |
| 21 | criticality | String | Yes | A = failure stops the line or affects safety, B = reduced output, C = no immediate effect | `"A"` | A; B; C |
| 22 | lastIssuedAt | Date | No (null allowed) | Last issued date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 23 | lastReceivedAt | Date | No (null allowed) | Last received date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 24 | isInsuranceSpare | Boolean | Yes | True when the record is insurance spare | `false` |  |
| 25 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Obsolete |
| 26 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_maint_maintenancePlanRequiredSparePart, u_mes_maint_maintenanceWorkOrderUsedSparePart, u_mes_maint_sparePartUsedOnEquipment.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_sparePart.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_sparePart.js
- Sample document: 03_design/08_tooling_maintenance/samples/u_mes_maint_sparePart.js
