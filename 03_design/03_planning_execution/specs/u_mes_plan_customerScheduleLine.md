# u_mes_plan_customerScheduleLine

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per line of a customer schedule |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_customerSchedule |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (23 required, 0 may be null) |

## Structure

Child collection. The parent customer schedule can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. customerScheduleId and customerScheduleName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1082000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CSR-SML-DS-2026-36-L01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerScheduleId | String | - | Yes | Reference to u_mes_plan_customerSchedule._id: the parent document this one belongs to | `"1081000000000001"` | Reference: u_mes_plan_customerSchedule._id |
| 6 | customerScheduleName | String | - | Yes | Display value of customerScheduleId, copied from u_mes_plan_customerSchedule.recordNo | `"CSR-SML-DS-2026-36"` |  |
| 7 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | customerPartNo | String | - | Yes | Customer part number | `"SM-3501-0421-LH"` |  |
| 11 | dueDate | Date | Date | Yes | Due date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 12 | quantity | Int32 | - | Yes | Quantity of the customer schedule line | `NumberInt(480)` |  |
| 13 | cumulativeRequired | Int32 | - | Yes | Cumulative quantity required by the customer since the start of the schedule year | `NumberInt(18240)` |  |
| 14 | cumulativeShipped | Int32 | - | Yes | Cumulative shipped | `NumberInt(17760)` |  |
| 15 | firmness | String | - | Yes | Firmness of the customer schedule line | `"Firm"` | Firm; Forecast |
| 16 | shippedQuantity | Int32 | - | Yes | Shipped quantity | `NumberInt(480)` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerScheduleId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_customerScheduleLine.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_customerScheduleLine.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_customerScheduleLine.js
