# u_mes_matl_exposureTimer

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Floor-life, pot-life or open-time clock for a lot or container of an exposure-controlled item. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (22 required, 10 may be null) |
| Estimated volume per year | about 2,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per exposure timer, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1311000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EXT-20260915-00003"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000006"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston Seal, square section, EPDM"` |  |
| 8 | lotId | String | - | Yes | Reference to u_mes_plan_lot._id | `"1096000000000010"` | Reference: u_mes_plan_lot._id |
| 9 | lotName | String | - | Yes | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260912-SEL-002"` |  |
| 10 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 11 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 12 | timerType | String | - | Yes | Timer type | `"Open Time"` | Floor Life; Pot Life; Open Time; Bake; Dirty Equipment Hold; Clean Equipment Hold; Process Hold Time |
| 13 | limitMinutes | Int32 | - | Yes | Allowed exposure in minutes | `NumberInt(480)` |  |
| 14 | startedAt | Date | Datetime | Yes | Clock start (container opened) | `ISODate("2026-09-15T05:40:00.000+0000")` |  |
| 15 | pausedAt | Date | Datetime | No (null allowed) | Last pause (container resealed / dry storage) | `null` |  |
| 16 | accumulatedMinutes | Int32 | - | Yes | Exposure accumulated so far | `NumberInt(455)` |  |
| 17 | expiresAt | Date | Datetime | Yes | Calculated expiry time while running | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 18 | storageLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 19 | storageLocationName | String | - | No (null allowed) | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 20 | resetReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: reset reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 21 | resetReasonCodeName | String | - | No (null allowed) | Display value of resetReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 22 | resetById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reset' | `null` | Reference: u_mes_mast_user._id |
| 23 | resetBy | String | - | No (null allowed) | Display name of the user in resetById, copied from u_mes_mast_user.fullName | `null` |  |
| 24 | resetAt | Date | Datetime | No (null allowed) | Reset time | `null` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Consumed"` | Running; Paused; Expired; Reset; Consumed |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:27:23.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:27:23.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Running, Paused, Expired, Reset, Consumed. Initial state: Running. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 5 | `{ containerId: 1 }` | No | Look-up of documents by container |
| 6 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 7 | `{ resetReasonCodeId: 1 }` | No | Look-up of documents by reset reason code |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_exposureTimer.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_exposureTimer.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_exposureTimer.js
