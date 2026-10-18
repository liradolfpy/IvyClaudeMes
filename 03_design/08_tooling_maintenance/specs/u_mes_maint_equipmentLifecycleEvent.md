# u_mes_maint_equipmentLifecycleEvent

| Property | Value |
|---|---|
| Module | ToolingAndMaintenance (maint) |
| Purpose | Lifecycle events of an equipment: commissioning, relocation, overhaul, refurbishment, upgrade, health assessment, replacement recommendation, decommissioning. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 31 (18 required, 13 may be null) |
| Estimated volume per year | about 300 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per equipment lifecycle event, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1331000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ELE-TRQ-01-N1-001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 7 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 8 | eventType | String | - | Yes | Event type | `"Commissioning"` | Commissioning; Relocation; Overhaul; Refurbishment; Upgrade; Health Assessment; Replacement Recommendation; Decommissioning |
| 9 | eventAt | Date | Datetime | Yes | Event time | `ISODate("2026-04-20T10:00:00.000+0000")` |  |
| 10 | description | String | - | Yes | Description | `"Commissioning of DC nutrunner station 1"` |  |
| 11 | costInr | Decimal128 | - | No (null allowed) | Cost in INR | `1850000.00` |  |
| 12 | healthScore | Decimal128 | - | No (null allowed) | Health score after the event (0 to 100) | `98` |  |
| 13 | lifetimeCyclesAtEvent | Int64 | - | No (null allowed) | Cycle counter at the event | `NumberLong("0")` |  |
| 14 | lifetimeRunHoursAtEvent | Decimal128 | - | No (null allowed) | Run hours at the event | `0.0` |  |
| 15 | maintenanceWorkOrderId | String | - | No (null allowed) | Reference to u_mes_maint_maintenanceWorkOrder._id | `null` | Reference: u_mes_maint_maintenanceWorkOrder._id |
| 16 | maintenanceWorkOrderName | String | - | No (null allowed) | Display value of maintenanceWorkOrderId, copied from u_mes_maint_maintenanceWorkOrder.title | `null` |  |
| 17 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 18 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 19 | modelPredictionId | String | - | No (null allowed) | Reference to u_mes_syst_modelPrediction._id | `null` | Reference: u_mes_syst_modelPrediction._id |
| 20 | modelPredictionName | String | - | No (null allowed) | Display value of modelPredictionId, copied from u_mes_syst_modelPrediction.recordNo | `null` |  |
| 21 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 22 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 23 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-04-20T14:00:00.000+0000")` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Recorded; Approved; Cancelled |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 27 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 28 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 29 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 30 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 31 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Recorded, Approved, Cancelled. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ maintenanceWorkOrderId: 1 }` | No | Look-up of documents by maintenance work order |
| 5 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 6 | `{ modelPredictionId: 1 }` | No | Look-up of documents by model prediction |
| 7 | `{ siteId: 1, eventAt: -1 }` | No | Time-ordered lists and reports by event at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_equipmentLifecycleEvent.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_equipmentLifecycleEvent.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_equipmentLifecycleEvent.js
