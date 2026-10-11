# u_mes_exe_labourBooking

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Clock-on / clock-off of people against orders, operations and indirect activities |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | LAB-<recordNo> |
| Display value used by references | recordNo |
| Keys | 36 (23 required, 13 may be null) |
| Estimated volume per year | ~350,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per labour booking, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: LAB-<recordNo> | `"LAB-20260929-10231-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-10231-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userId | String | Yes | Reference to u_mes_mdm_user._id | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 6 | userName | String | Yes | Display value of userId, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 7 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 8 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 9 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 10 | bookingType | String | Yes | Booking type | `"Direct"` | Direct; Indirect |
| 11 | productionOrderId | String | No (null allowed) | Reference to u_mes_exe_productionOrder._id | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 12 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 13 | operationId | String | No (null allowed) | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 14 | operationName | String | No (null allowed) | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 15 | workCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 16 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 17 | indirectActivityId | String | No (null allowed) | Reference to u_mes_exe_indirectActivity._id | `null` | Reference: u_mes_exe_indirectActivity._id |
| 18 | indirectActivityName | String | No (null allowed) | Display value of indirectActivityId, copied from u_mes_exe_indirectActivity.name | `null` |  |
| 19 | clockOnAt | Date | Yes | Clock on date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 20 | clockOffAt | Date | No (null allowed) | Clock off date and time | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 21 | durationMinutes | Int32 | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 22 | overtimeMinutes | Int32 | Yes | Overtime (minutes) | `NumberInt(0)` |  |
| 23 | quantityGood | Int32 | Yes | Quantity good | `NumberInt(1)` |  |
| 24 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 25 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 26 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 27 | erpConfirmationNo | String | No (null allowed) | ERP confirmation number | `"0000871245"` |  |
| 28 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 29 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Open; Closed; Approved |
| 30 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 32 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 33 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 34 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 35 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 36 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Closed, Approved. Initial state: Open. The values are maintained in u_mes_sys_statusDefinition.

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

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_labourBooking.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_labourBooking.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_labourBooking.js
