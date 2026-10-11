# u_mes_perf_productionCount

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Hourly good / reject / rework counts per work centre against target (hour-by-hour board) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | PC-<recordNo> |
| Display value used by references | recordNo |
| Keys | 34 (29 required, 5 may be null) |
| Estimated volume per year | ~250,000 |
| Storage | time-series candidate |

## Structure

Flat entity collection: one document per production count, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: PC-<recordNo> | `"PC-20260929-TRQ-01-08"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-TRQ-01-08"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"LN-ASY-01"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Caliper Assembly Line 1"` |  |
| 9 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 10 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 11 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 12 | hourStartAt | Date | Yes | Hour start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 13 | hourEndAt | Date | Yes | Hour end date and time | `ISODate("2026-09-29T01:30:00.000+0000")` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 16 | itemId | String | No (null allowed) | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 17 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 18 | targetQuantity | Int32 | Yes | Target quantity | `NumberInt(100)` |  |
| 19 | goodQuantity | Int32 | Yes | Good quantity | `NumberInt(474)` |  |
| 20 | rejectQuantity | Int32 | Yes | Reject quantity | `NumberInt(1)` |  |
| 21 | reworkQuantity | Int32 | Yes | Rework quantity | `NumberInt(4)` |  |
| 22 | cumulativeTarget | Int32 | Yes | Cumulative target | `NumberInt(300)` |  |
| 23 | cumulativeGood | Int32 | Yes | Cumulative good | `NumberInt(281)` |  |
| 24 | downtimeMinutes | Int32 | Yes | Downtime (minutes) | `NumberInt(18)` |  |
| 25 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 26 | gapReason | String | No (null allowed) | Gap reason | `"Nutrunner socket change 18 minutes"` |  |
| 27 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Open; Closed |
| 28 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 30 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 31 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 32 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T01:30:00.000+0000")` |  |
| 33 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 34 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Open, Closed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_productionCount.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_productionCount.js
- Sample document: 03_design/07_performance_management/samples/u_mes_perf_productionCount.js
