# u_mes_ehs_energyReading

| Property | Value |
|---|---|
| Module | Energy, safety and andon (ehs) |
| Purpose | Interval energy, compressed air and gas consumption per meter and equipment |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | ENR-<recordNo> |
| Display value used by references | recordNo |
| Keys | 34 (25 required, 9 may be null) |
| Estimated volume per year | ~3.5 million |
| Storage | time-series (recommended) |

## Structure

Flat entity collection: one document per energy reading, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ENR-<recordNo> | `"ENR-20260929-EM03-0031"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-EM03-0031"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | meterIotDeviceId | String | Yes | Reference to u_mes_sys_iotDevice._id: meter IoT device | `"IOT-EM-03"` | Reference: u_mes_sys_iotDevice._id |
| 6 | meterIotDeviceName | String | Yes | Display value of meterIotDeviceId, copied from u_mes_sys_iotDevice.name | `"Energy meter, assembly line 1"` |  |
| 7 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 8 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 9 | lineId | String | No (null allowed) | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 10 | lineName | String | No (null allowed) | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 11 | shiftId | String | No (null allowed) | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 12 | shiftName | String | No (null allowed) | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 13 | energyTypeId | String | Yes | Reference to u_mes_ehs_energyType._id | `"ENT-T-ELEC"` | Reference: u_mes_ehs_energyType._id |
| 14 | energyTypeName | String | Yes | Display value of energyTypeId, copied from u_mes_ehs_energyType.name | `"Electricity"` |  |
| 15 | intervalStartAt | Date | Yes | Interval start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | intervalEndAt | Date | Yes | Interval end date and time | `ISODate("2026-09-29T00:45:00.000+0000")` |  |
| 17 | consumption | Decimal128 | Yes | Quantity consumed in the interval, in the unit given by unitOfMeasureId | `NumberDecimal("41.6")` |  |
| 18 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-KWH"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Kilowatt hour"` |  |
| 20 | meterReadingStart | Decimal128 | Yes | Meter reading start | `NumberDecimal("184220.4")` |  |
| 21 | meterReadingEnd | Decimal128 | Yes | Meter reading end | `NumberDecimal("184262.0")` |  |
| 22 | demandKw | Decimal128 | No (null allowed) | Demand (kW) | `NumberDecimal("96.5")` |  |
| 23 | powerFactor | Double | No (null allowed) | Power factor | `Double(0.96)` |  |
| 24 | costInr | Decimal128 | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 25 | unitsProduced | Int32 | Yes | Units produced | `NumberInt(762)` |  |
| 26 | specificConsumption | Decimal128 | No (null allowed) | Consumption per unit produced | `NumberDecimal("0.0546")` |  |
| 27 | signalQuality | String | Yes | Signal quality | `"Good"` | Good; Uncertain; Bad |
| 28 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 29 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 30 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 31 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"MES System"` |  |
| 32 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:45:00.000+0000")` |  |
| 33 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 34 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"MES System"` |  |

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

- Validator: 03_design/10_energy_safety_andon/validators/u_mes_ehs_energyReading.json
- Indexes: 03_design/10_energy_safety_andon/indexes/u_mes_ehs_energyReading.js
- Sample document: 03_design/10_energy_safety_andon/samples/u_mes_ehs_energyReading.js
