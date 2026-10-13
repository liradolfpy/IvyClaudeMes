# u_mes_qual_checkSheet

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Check sheet definitions: start-of-shift checks, poka-yoke verification, first-off, autonomous maintenance |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 25 (16 required, 9 may be null) |
| Estimated volume per year | 200-1,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per check sheet, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with checkSheetId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_checkSheetItem | Child | item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1146000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SOS-GDC-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the check sheet; used as its display value in other collections | `"Start of shift check, Gravity Die Casting Cell 1"` |  |
| 7 | checkSheetType | String | - | Yes | Check sheet type | `"Start Of Shift"` | Start Of Shift; Poka Yoke Verification; First Off Approval; Autonomous Maintenance; Layered Process Audit; Changeover |
| 8 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 10 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 11 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 12 | operationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 13 | operationName | String | - | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 14 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 15 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 16 | version | Int32 | - | Yes | Version of the check sheet | `NumberInt(1)` |  |
| 17 | frequency | String | - | Yes | Frequency of the check sheet | `"Per Shift"` | Per Shift; Daily; Weekly; Per Changeover; Per Lot |
| 18 | masterSampleRequired | Boolean | - | Yes | True when: master sample required | `true` |  |
| 19 | estimatedMinutes | Int32 | - | Yes | Estimated (minutes) | `NumberInt(8)` |  |
| 20 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 21 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 22 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 5 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |

## Referenced by

u_mes_qual_checkSheetItem, u_mes_qual_checkSheetResult, u_mes_qual_audit, u_mes_qual_auditSchedule.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_checkSheet.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_checkSheet.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_checkSheet.js
