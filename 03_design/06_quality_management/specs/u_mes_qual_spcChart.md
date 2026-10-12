# u_mes_qual_spcChart

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Chart definition per characteristic and work centre: chart type, subgroup size, control limits, rules |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 29 (20 required, 9 may be null) |
| Estimated volume per year | 500-2,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per SPC chart, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with spcChartId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_spcChartControlLimit | Child | control limit |
| u_mes_qual_spcChartRule | Value list | rule |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1151000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SPC-OP010-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the SPC chart; used as its display value in other collections | `"Casting wall thickness at bridge, X-bar R chart"` |  |
| 6 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 10 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 12 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 13 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 14 | chartType | String | - | Yes | Chart type | `"X-bar R"` | X-bar R; X-bar S; I-MR; p; np; c; u |
| 15 | subgroupSize | Int32 | - | Yes | Subgroup size | `NumberInt(5)` |  |
| 16 | subgroupFrequency | String | - | Yes | Subgroup frequency | `"Every 2 hours"` |  |
| 17 | lowerSpecLimit | Decimal128 | - | No (null allowed) | Lower spec limit | `NumberDecimal("7.50")` |  |
| 18 | upperSpecLimit | Decimal128 | - | No (null allowed) | Upper spec limit | `NumberDecimal("8.50")` |  |
| 19 | capabilityCp | Decimal128 | - | No (null allowed) | CAPAbility cp | `NumberDecimal("1.92")` |  |
| 20 | capabilityCpk | Decimal128 | - | No (null allowed) | CAPAbility cpk | `NumberDecimal("1.71")` |  |
| 21 | capabilityPp | Decimal128 | - | No (null allowed) | CAPAbility pp | `NumberDecimal("1.84")` |  |
| 22 | capabilityPpk | Decimal128 | - | No (null allowed) | CAPAbility ppk | `NumberDecimal("1.66")` |  |
| 23 | capabilityCalculatedAt | Date | Datetime | No (null allowed) | Capability calculated date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | capabilitySampleCount | Int32 | - | Yes | CAPAbility sample count | `NumberInt(125)` |  |
| 25 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 26 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 27 | reactionPlan | String | - | Yes | Reaction plan | `"Stop, segregate parts since last good check, inform line leader, raise NCR"` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Inactive |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Suspended, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 7 | `{ ownerUserId: 1 }` | No | Look-up of documents by owner user |

## Referenced by

u_mes_qual_spcChartControlLimit, u_mes_qual_spcChartRule, u_mes_qual_spcSample.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_spcChart.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_spcChart.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_spcChart.js
