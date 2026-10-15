# u_mes_plan_labourBooking

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Clock-on / clock-off of people against orders, operations and indirect activities |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 43 (24 required, 19 may be null) |
| Estimated volume per year | ~350,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per labour booking, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1101000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LAB-2026-000407"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 7 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 8 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 9 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 10 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 11 | bookingType | String | - | Yes | Booking type | `"Direct"` | Direct; Indirect |
| 12 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 13 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 14 | operationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 15 | operationName | String | - | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 16 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 17 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 18 | indirectActivityId | String | - | No (null allowed) | Reference to u_mes_plan_indirectActivity._id | `null` | Reference: u_mes_plan_indirectActivity._id |
| 19 | indirectActivityName | String | - | No (null allowed) | Display value of indirectActivityId, copied from u_mes_plan_indirectActivity.name | `null` |  |
| 20 | clockOnAt | Date | Datetime | Yes | Clock on date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 21 | clockOffAt | Date | Datetime | No (null allowed) | Clock off date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 22 | durationMinutes | Int32 | - | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 23 | overtimeMinutes | Int32 | - | Yes | Overtime (minutes) | `NumberInt(0)` |  |
| 24 | quantityGood | Int32 | - | Yes | Quantity good | `NumberInt(1)` |  |
| 25 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 26 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 27 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 28 | erpConfirmationNo | String | - | No (null allowed) | ERP confirmation number | `"0000871245"` |  |
| 29 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 30 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `null` | Reference: u_mes_plan_operationExecution._id |
| 31 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `null` |  |
| 32 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `null` | Reference: u_mes_prod_productVariant._id |
| 33 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `null` |  |
| 34 | operatorSessionId | String | - | No (null allowed) | Reference to u_mes_plan_operatorSession._id | `null` | Reference: u_mes_plan_operatorSession._id |
| 35 | operatorSessionName | String | - | No (null allowed) | Display value of operatorSessionId, copied from u_mes_plan_operatorSession.recordNo | `null` |  |
| 36 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Closed; Approved |
| 37 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 38 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T00:00:00.000+0000")` |  |
| 39 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 40 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 41 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 42 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 43 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Closed, Approved. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ userId: 1 }` | No | Look-up of documents by user |
| 4 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 5 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 6 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 7 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_labourBooking.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_labourBooking.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_labourBooking.js
