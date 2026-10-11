# u_mes_eqp_processTag

| Property | Value |
|---|---|
| Module | Equipment and performance (eqp) |
| Purpose | Tag definitions: source address, unit, deadband, limits, equipment |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | TAG-<recordNo> |
| Display value used by references | description |
| Keys | 28 (24 required, 4 may be null) |
| Estimated volume per year | 5,000-20,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per process tag, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: TAG-<recordNo> | `"TAG-PN1.GDC01.DIE_TEMP_UPPER"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1.GDC01.DIE_TEMP_UPPER"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | description | String | Yes | Description of the process tag | `"Die temperature, upper half, casting machine 1"` |  |
| 6 | equipmentId | String | Yes | Reference to u_mes_mdm_equipment._id | `"EQ-GDC-01"` | Reference: u_mes_mdm_equipment._id |
| 7 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 8 | iotDeviceId | String | Yes | Reference to u_mes_sys_iotDevice._id | `"IOT-PLC-GDC-01"` | Reference: u_mes_sys_iotDevice._id |
| 9 | iotDeviceName | String | Yes | Display value of iotDeviceId, copied from u_mes_sys_iotDevice.name | `"PLC, casting machine 1"` |  |
| 10 | sourceAddress | String | Yes | Source address | `"ns=3;s=\"DB_Process\".\"DieTempUpper\""` |  |
| 11 | dataType | String | Yes | Data type | `"Variable"` | Variable; Attribute |
| 12 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-DEGC"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Degree Celsius"` |  |
| 14 | tagClass | String | Yes | Tag class | `"Process Value"` | Process Value; Setpoint; Counter; State; Alarm Bit; Energy |
| 15 | scanRateMs | Int32 | Yes | Scan rate (milliseconds) | `NumberInt(1000)` |  |
| 16 | deadband | Decimal128 | Yes | Deadband of the process tag | `NumberDecimal("0.5")` |  |
| 17 | lowLimit | Decimal128 | No (null allowed) | Low limit | `NumberDecimal("380.0")` |  |
| 18 | highLimit | Decimal128 | No (null allowed) | High limit | `NumberDecimal("420.0")` |  |
| 19 | lowLowLimit | Decimal128 | No (null allowed) | Low low limit | `NumberDecimal("360.0")` |  |
| 20 | highHighLimit | Decimal128 | No (null allowed) | High high limit | `NumberDecimal("440.0")` |  |
| 21 | engineeringMin | Decimal128 | Yes | Engineering (minutes) | `NumberDecimal("0.0")` |  |
| 22 | engineeringMax | Decimal128 | Yes | Engineering max | `NumberDecimal("600.0")` |  |
| 23 | isCritical | Boolean | Yes | True when the record is critical | `true` |  |
| 24 | historise | Boolean | Yes | True when: historise | `true` |  |
| 25 | retentionDays | Int32 | Yes | Retention (days) | `NumberInt(730)` |  |
| 26 | aggregation | String | Yes | Aggregation of the process tag | `"Average"` | None; Average; Minimum; Maximum; Last; Sum |
| 27 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 28 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ iotDeviceId: 1 }` | No | Look-up of documents by IoT device |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |

## Referenced by

u_mes_prd_recipeParameter, u_mes_eqp_processReading, u_mes_eqp_alarm.

## Files

- Validator: 03_design/07_equipment_performance/validators/u_mes_eqp_processTag.json
- Indexes: 03_design/07_equipment_performance/indexes/u_mes_eqp_processTag.js
- Sample document: 03_design/07_equipment_performance/samples/u_mes_eqp_processTag.js
