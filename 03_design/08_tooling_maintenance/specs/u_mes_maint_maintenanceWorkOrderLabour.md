# u_mes_maint_maintenanceWorkOrderLabour

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | One document per labour of a maintenance work order |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_maint_maintenanceWorkOrder |
| _id pattern | <maintenanceWorkOrderId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Child collection. The parent maintenance work order can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. maintenanceWorkOrderId and maintenanceWorkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <maintenanceWorkOrderId>-L<nnn> | `"MWO-2026-000341-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000341-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenanceWorkOrderId | String | Yes | Reference to u_mes_maint_maintenanceWorkOrder._id: the parent document this one belongs to | `"MWO-2026-000341"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | Yes | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Nutrunner rundown fault, station 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | userId | String | Yes | Reference to u_mes_mast_user._id | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 9 | userName | String | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 10 | labourMinutes | Int32 | Yes | Labour (minutes) | `NumberInt(35)` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 13 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 14 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 15 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 17 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenanceWorkOrderId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ userId: 1 }` | No | Look-up of lines by user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrderLabour.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrderLabour.js
- Sample document: 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrderLabour.js
