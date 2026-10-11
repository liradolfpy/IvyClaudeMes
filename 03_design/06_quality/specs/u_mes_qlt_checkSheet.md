# u_mes_qlt_checkSheet

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Check sheet definitions: start-of-shift checks, poka-yoke verification, first-off, autonomous maintenance |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CKS-<recordNo> |
| Display value used by references | name |
| Keys | 24 (15 required, 9 may be null) |
| Estimated volume per year | 200-1,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per check sheet, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with checkSheetId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_checkSheetItem | Child | item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CKS-<recordNo> | `"CKS-TRQ-01-SOS"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01-SOS"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the check sheet; used as its display value in other collections | `"Start of shift check, torque station"` |  |
| 6 | checkSheetType | String | Yes | Check sheet type | `"Start Of Shift"` | Start Of Shift; Poka Yoke Verification; First Off Approval; Autonomous Maintenance; Layered Process Audit; Changeover |
| 7 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 8 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 9 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 10 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 11 | operationId | String | No (null allowed) | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 12 | operationName | String | No (null allowed) | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 13 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 14 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 15 | version | Int32 | Yes | Version of the check sheet | `NumberInt(3)` |  |
| 16 | frequency | String | Yes | Frequency of the check sheet | `"Per Shift"` | Per Shift; Daily; Weekly; Per Changeover; Per Lot |
| 17 | masterSampleRequired | Boolean | Yes | True when: master sample required | `true` |  |
| 18 | estimatedMinutes | Int32 | Yes | Estimated (minutes) | `NumberInt(8)` |  |
| 19 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 20 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 21 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 22 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 23 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_qlt_checkSheetItem, u_mes_qlt_checkSheetResult, u_mes_qlt_audit.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_checkSheet.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_checkSheet.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_checkSheet.js
