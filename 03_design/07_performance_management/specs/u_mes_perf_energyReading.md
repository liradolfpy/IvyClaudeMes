# u_mes_perf_energyReading

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | Interval energy, compressed air and gas consumption per meter and equipment |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 35 (26 required, 9 may be null) |
| Estimated volume per year | ~3.5 million |
| Storage | time-series (recommended) |

## Structure

Flat entity collection: one document per energy reading, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1250000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ENR-2026-000337"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | meterIotDeviceId | String | - | Yes | Reference to u_mes_syst_iotDevice._id: meter IoT device | `"1232000000000004"` | Reference: u_mes_syst_iotDevice._id |
| 7 | meterIotDeviceName | String | - | Yes | Display value of meterIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Energy meter, surface treatment line"` |  |
| 8 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 9 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 10 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 11 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 12 | shiftId | String | - | No (null allowed) | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 13 | shiftName | String | - | No (null allowed) | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 14 | energyTypeId | String | - | Yes | Reference to u_mes_perf_energyType._id | `"1294000000000001"` | Reference: u_mes_perf_energyType._id |
| 15 | energyTypeName | String | - | Yes | Display value of energyTypeId, copied from u_mes_perf_energyType.name | `"Electricity"` |  |
| 16 | intervalStartAt | Date | Datetime | Yes | Interval start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 17 | intervalEndAt | Date | Datetime | Yes | Interval end date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:15:00.000+0000")` |  |
| 18 | consumption | Decimal128 | - | Yes | Quantity consumed in the interval, in the unit given by unitOfMeasureId | `NumberDecimal("41.6")` |  |
| 19 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000010"` | Reference: u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Kilowatt hour"` |  |
| 21 | meterReadingStart | Decimal128 | - | Yes | Meter reading start | `NumberDecimal("184220.4")` |  |
| 22 | meterReadingEnd | Decimal128 | - | Yes | Meter reading end | `NumberDecimal("184262.0")` |  |
| 23 | demandKw | Decimal128 | - | No (null allowed) | Demand (kW) | `NumberDecimal("96.5")` |  |
| 24 | powerFactor | Double | - | No (null allowed) | Power factor | `Double(0.96)` |  |
| 25 | costInr | Decimal128 | - | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 26 | unitsProduced | Int32 | - | Yes | Units produced | `NumberInt(38)` |  |
| 27 | specificConsumption | Decimal128 | - | No (null allowed) | Consumption per unit produced | `NumberDecimal("0.0546")` |  |
| 28 | signalQuality | String | - | Yes | Signal quality | `"Good"` | Good; Uncertain; Bad |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 31 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 33 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:15:00.000+0000")` |  |
| 34 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ meterIotDeviceId: 1 }` | No | Look-up of documents by meter IoT device |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ energyTypeId: 1 }` | No | Look-up of documents by energy type |
| 7 | `{ siteId: 1, intervalStartAt: -1 }` | No | Time-ordered lists and reports by interval start at |
| 8 | `{ meterIotDeviceId: 1, intervalStartAt: -1 }` | No | Consumption of one meter over time |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_energyReading.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_energyReading.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_energyReading.js
