# u_mes_qlt_pfmea

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Process FMEA per item / process: failure modes, effects, causes, S-O-D, action priority |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | FMEA-<recordNo> |
| Display value used by references | title |
| Keys | 19 (14 required, 5 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per PFMEA, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with pfmeaId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_pfmeaCoreTeamUser | Relationship | core team user |
| u_mes_qlt_pfmeaLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: FMEA-<recordNo> | `"FMEA-5110-10-0100-PF"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-PF"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the PFMEA; used as its display value in other collections | `"Process FMEA, Front Brake Caliper Assembly LH"` |  |
| 6 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 7 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 9 | version | Int32 | Yes | Version of the PFMEA | `NumberInt(3)` |  |
| 10 | methodology | String | Yes | Methodology of the PFMEA | `"AIAG-VDA"` | AIAG-VDA; AIAG 4th Edition |
| 11 | controlPlanId | String | No (null allowed) | Reference to u_mes_qlt_controlPlan._id | `"CP-5110-10-0100-PROD"` | Reference: u_mes_qlt_controlPlan._id |
| 12 | controlPlanName | String | No (null allowed) | Display value of controlPlanId, copied from u_mes_qlt_controlPlan.recordNo | `"5110-10-0100-PROD"` |  |
| 13 | originalDate | Date | Yes | Original date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 14 | revisionDate | Date | Yes | Revision date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 15 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 16 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 17 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 18 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 19 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ controlPlanId: 1 }` | No | Look-up of documents by control plan |

## Referenced by

u_mes_qlt_controlPlan, u_mes_qlt_capa, u_mes_qlt_pfmeaCoreTeamUser, u_mes_qlt_pfmeaLine, u_mes_qlt_ppapSubmission.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_pfmea.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_pfmea.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_pfmea.js
