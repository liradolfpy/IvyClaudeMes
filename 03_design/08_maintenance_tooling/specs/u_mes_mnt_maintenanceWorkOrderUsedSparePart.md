# u_mes_mnt_maintenanceWorkOrderUsedSparePart

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | One document per used spare part of a maintenance work order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_mnt_maintenanceWorkOrder |
| _id pattern | <maintenanceWorkOrderId>-USP<nnn> |
| Display value used by references | recordNo |
| Keys | 18 (18 required, 0 may be null) |

## Structure

Child collection. The parent maintenance work order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenanceWorkOrderId and maintenanceWorkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <maintenanceWorkOrderId>-USP<nnn> | `"MWO-2026-000341-USP001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000341-USP001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenanceWorkOrderId | String | Yes | Reference to u_mes_mnt_maintenanceWorkOrder._id: the parent document this one belongs to | `"MWO-2026-000341"` | Reference: u_mes_mnt_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | Yes | Display value of maintenanceWorkOrderId, copied from u_mes_mnt_maintenanceWorkOrder.title | `"Nutrunner rundown fault, station 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | sparePartId | String | Yes | Reference to u_mes_mnt_sparePart._id | `"SPR-SP-004417"` | Reference: u_mes_mnt_sparePart._id |
| 9 | sparePartName | String | Yes | Display value of sparePartId, copied from u_mes_mnt_sparePart.description | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 10 | quantity | Decimal128 | Yes | Quantity of the maintenance work order used spare part | `NumberDecimal("1")` |  |
| 11 | costInr | Decimal128 | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10112"` | Reference: u_mes_mdm_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Imran Shaikh"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10112"` | Reference: u_mes_mdm_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Imran Shaikh"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenanceWorkOrderId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ sparePartId: 1 }` | No | Look-up of lines by spare part |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_maintenanceWorkOrderUsedSparePart.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_maintenanceWorkOrderUsedSparePart.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_maintenanceWorkOrderUsedSparePart.js
