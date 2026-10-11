# u_mes_perf_processReading

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | Tag values over time (die temperature, furnace zone temperature, spindle load, bath pH, current) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | PD-<recordNo> |
| Display value used by references | recordNo |
| Keys | 24 (19 required, 5 may be null) |
| Estimated volume per year | ~2 billion raw, down-sampled |
| Storage | time-series (recommended) |

## Structure

Flat entity collection: one document per process reading, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: PD-<recordNo> | `"PD-20260929-00417733"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-00417733"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | processTagId | String | Yes | Reference to u_mes_perf_processTag._id | `"TAG-PN1.GDC01.DIE_TEMP_UPPER"` | Reference: u_mes_perf_processTag._id |
| 6 | processTagName | String | Yes | Display value of processTagId, copied from u_mes_perf_processTag.description | `"Die temperature, upper half, casting machine 1"` |  |
| 7 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id | `"EQ-GDC-01"` | Reference: u_mes_mast_equipment._id |
| 8 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 9 | timestamp | Date | Yes | Timestamp (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 10 | tagValue | Double | Yes | Numeric value of the tag at the timestamp | `Double(402.6)` |  |
| 11 | tagValueText | String | No (null allowed) | Tag value text | `null` |  |
| 12 | signalQuality | String | Yes | Signal quality | `"Good"` | Good; Uncertain; Bad |
| 13 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 15 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 16 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 17 | inLimits | Boolean | Yes | True when: in limits | `true` |  |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 20 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 22 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 23 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ processTagId: 1 }` | No | Look-up of documents by process tag |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ siteId: 1, timestamp: -1 }` | No | Time-ordered lists and reports by timestamp |
| 7 | `{ processTagId: 1, timestamp: -1 }` | No | Trend of one tag over time |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_processReading.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_processReading.js
- Sample document: 03_design/07_performance_management/samples/u_mes_perf_processReading.js
