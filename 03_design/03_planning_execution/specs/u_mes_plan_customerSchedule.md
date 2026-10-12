# u_mes_plan_customerSchedule

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | OEM delivery schedules / releases (demand that drives production orders and shipments) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (20 required, 3 may be null) |
| Estimated volume per year | 5,000-20,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per customer schedule, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with customerScheduleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_customerScheduleLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1081000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CSR-SML-DS-2026-36"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 6 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 7 | shipToCode | String | - | Yes | Ship to code | `"SML-TLG-D4"` |  |
| 8 | scheduleType | String | - | Yes | Schedule type | `"Delivery Schedule"` | Forecast; Delivery Schedule; Just In Time Call Off |
| 9 | customerOrderNo | String | - | Yes | Customer order number | `"4500218734"` |  |
| 10 | receivedAt | Date | Datetime | No (null allowed) | Date and time when the record was received. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 11 | horizonFrom | Date | Date | Yes | Horizon from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 12 | horizonTo | Date | Date | Yes | Horizon to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-13T00:00:00.000+0000")` |  |
| 13 | supersedesCustomerScheduleId | String | - | No (null allowed) | Reference to u_mes_plan_customerSchedule._id: supersedes customer schedule | `null` | Reference: u_mes_plan_customerSchedule._id |
| 14 | supersedesCustomerScheduleName | String | - | No (null allowed) | Display value of supersedesCustomerScheduleId, copied from u_mes_plan_customerSchedule.recordNo | `null` |  |
| 15 | erpSalesOrderNo | String | - | Yes | ERP sales order number | `"0020041877"` |  |
| 16 | status | String | - | Yes | Primary lifecycle state of the document | `"Received"` | Received; Confirmed; Partially Shipped; Completed; Replaced |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Received, Confirmed, Partially Shipped, Completed, Replaced. Initial state: Received. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ supersedesCustomerScheduleId: 1 }` | No | Look-up of documents by supersedes customer schedule |
| 5 | `{ siteId: 1, receivedAt: -1 }` | No | Time-ordered lists and reports by received at |

## Referenced by

u_mes_plan_customerSchedule, u_mes_plan_customerScheduleLine, u_mes_plan_productionOrder, u_mes_matl_shipment.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_customerSchedule.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_customerSchedule.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_customerSchedule.js
