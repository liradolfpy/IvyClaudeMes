# u_mes_maint_sparePartUsedOnEquipment

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | Links one spare part to one used on equipment; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_maint_sparePart |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Relationship collection. A spare part can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. sparePartId and sparePartName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1225000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SP-004417-UOE01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | sparePartId | String | - | Yes | Reference to u_mes_maint_sparePart._id: the parent document this one belongs to | `"1224000000000001"` | Reference: u_mes_maint_sparePart._id |
| 7 | sparePartName | String | - | Yes | Display value of sparePartId, copied from u_mes_maint_sparePart.description | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | usedOnEquipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id: used on equipment | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 10 | usedOnEquipmentName | String | - | Yes | Display value of usedOnEquipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ sparePartId: 1, usedOnEquipmentId: 1 }` | Yes | One link per pair |
| 2 | `{ usedOnEquipmentId: 1, sparePartId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_sparePartUsedOnEquipment.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_sparePartUsedOnEquipment.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_sparePartUsedOnEquipment.js
