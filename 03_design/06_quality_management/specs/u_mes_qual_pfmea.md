# u_mes_qual_pfmea

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Process FMEA per item / process: failure modes, effects, causes, S-O-D, action priority |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 19 (14 required, 5 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per PFMEA, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with pfmeaId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_pfmeaCoreTeamUser | Relationship | core team user |
| u_mes_qual_pfmeaLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1183000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PF-5110-10-0100-R01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title of the PFMEA; used as its display value in other collections | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 9 | version | Int32 | - | Yes | Version of the PFMEA | `NumberInt(1)` |  |
| 10 | methodology | String | - | Yes | Methodology of the PFMEA | `"AIAG-VDA"` | AIAG-VDA; AIAG 4th Edition |
| 11 | controlPlanId | String | - | No (null allowed) | Reference to u_mes_qual_controlPlan._id | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 12 | controlPlanName | String | - | No (null allowed) | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 13 | originalDate | Date | Date | Yes | Original date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 14 | revisionDate | Date | Date | Yes | Revision date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 15 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 16 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 17 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ controlPlanId: 1 }` | No | Look-up of documents by control plan |

## Referenced by

u_mes_qual_controlPlan, u_mes_qual_capa, u_mes_qual_pfmeaCoreTeamUser, u_mes_qual_pfmeaLine, u_mes_qual_ppapSubmission, u_mes_qual_riskAssessment.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_pfmea.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_pfmea.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_pfmea.js
