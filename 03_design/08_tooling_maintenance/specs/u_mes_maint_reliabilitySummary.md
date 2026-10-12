# u_mes_maint_reliabilitySummary

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | MTBF and MTTR per equipment, line and period. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 28 (24 required, 4 may be null) |
| Estimated volume per year | about 2,000 |
| Storage | standard collection (report table) |

## Structure

Flat entity collection: one document per reliability summary, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1330000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"REL-202609-GDC-01-M1"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | - | Yes | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | - | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 7 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 9 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `null` | Reference: u_mes_mast_shift._id |
| 10 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `null` |  |
| 11 | periodType | String | - | Yes | Period type | `"Month"` | Shift; Day; Week; Month |
| 12 | periodStartAt | Date | Datetime | Yes | Period start | `ISODate("2026-09-01T00:00:00.000+0000")` |  |
| 13 | periodEndAt | Date | Datetime | Yes | Period end | `ISODate("2026-09-30T23:59:00.000+0000")` |  |
| 14 | operatingHours | Decimal128 | - | Yes | Run hours | `NumberDecimal("498.5")` |  |
| 15 | failureCount | Int32 | - | Yes | Breakdowns | `NumberInt(2)` |  |
| 16 | repairMinutes | Int32 | - | Yes | Total repair minutes | `NumberInt(190)` |  |
| 17 | mtbfHours | Decimal128 | - | No (null allowed) | Mean time between failures; null when no failure | `NumberDecimal("249.3")` |  |
| 18 | mttrMinutes | Decimal128 | - | No (null allowed) | Mean time to repair; null when no failure | `NumberDecimal("95.0")` |  |
| 19 | availabilityPct | Decimal128 | - | Yes | Technical availability | `NumberDecimal("99.4")` |  |
| 20 | calculatedAt | Date | Datetime | Yes | Calculation time | `ISODate("2026-09-30T23:59:00.000+0000")` |  |
| 21 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Recalculated |
| 22 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 23 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 24 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 25 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 26 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-30T23:59:00.000+0000")` |  |
| 27 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000006"` | Reference: u_mes_mast_user._id |
| 28 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |

## Status values

Calculated, Recalculated. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ siteId: 1, periodStartAt: -1 }` | No | Time-ordered lists and reports by period start at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_reliabilitySummary.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_reliabilitySummary.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_reliabilitySummary.js
