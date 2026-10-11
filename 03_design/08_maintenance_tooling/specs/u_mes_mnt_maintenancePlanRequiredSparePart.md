# u_mes_mnt_maintenancePlanRequiredSparePart

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | One document per required spare part of a maintenance plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mnt_maintenancePlan |
| _id pattern | <maintenancePlanId>-RSP<nnn> |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Child collection. The parent maintenance plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <maintenancePlanId>-RSP<nnn> | `"MP-PM-LKT-01-M-RSP001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-LKT-01-M-RSP001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenancePlanId | String | Yes | Reference to u_mes_mnt_maintenancePlan._id: the parent document this one belongs to | `"MP-PM-LKT-01-M"` | Reference: u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String | Yes | Display value of maintenancePlanId, copied from u_mes_mnt_maintenancePlan.name | `"Leak tester monthly preventive maintenance"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | sparePartId | String | Yes | Reference to u_mes_mnt_sparePart._id | `"SPR-SP-004417"` | Reference: u_mes_mnt_sparePart._id |
| 9 | sparePartName | String | Yes | Display value of sparePartId, copied from u_mes_mnt_sparePart.description | `"Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner"` |  |
| 10 | quantity | Decimal128 | Yes | Quantity of the maintenance plan required spare part | `NumberDecimal("1")` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ sparePartId: 1 }` | No | Look-up of lines by spare part |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_maintenancePlanRequiredSparePart.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_maintenancePlanRequiredSparePart.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_maintenancePlanRequiredSparePart.js
