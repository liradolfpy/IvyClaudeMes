# u_mes_maint_maintenanceWorkOrderAssignedToUser

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Links one maintenance work order to one assigned to user; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_maint_maintenanceWorkOrder |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Relationship collection. A maintenance work order can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. maintenanceWorkOrderId and maintenanceWorkOrderName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1221000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MWO-2026-000341-ATU01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | maintenanceWorkOrderId | String | - | Yes | Reference to u_mes_maint_maintenanceWorkOrder._id: the parent document this one belongs to | `"1220000000000001"` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - | Yes | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `"Ejector pin sticking, casting machine 1, die 2"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | assignedToUserId | String | - | Yes | Reference to u_mes_mast_user._id: assigned to user | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 10 | assignedToUserName | String | - | Yes | Display value of assignedToUserId, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 13 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 14 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 15 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 16 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 17 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenanceWorkOrderId: 1, assignedToUserId: 1 }` | Yes | One link per pair |
| 2 | `{ assignedToUserId: 1, maintenanceWorkOrderId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenanceWorkOrderAssignedToUser.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenanceWorkOrderAssignedToUser.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenanceWorkOrderAssignedToUser.js
