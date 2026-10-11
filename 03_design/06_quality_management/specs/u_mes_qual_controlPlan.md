# u_mes_qual_controlPlan

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | AIAG control plan per item and phase (prototype, pre-launch, production) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CP-<recordNo> |
| Display value used by references | recordNo |
| Keys | 26 (18 required, 8 may be null) |
| Estimated volume per year | 200-1,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per control plan, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with controlPlanId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_controlPlanCoreTeamUser | Relationship | core team user |
| u_mes_qual_controlPlanLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CP-<recordNo> | `"CP-5110-10-0100-PROD"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-PROD"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 8 | phase | String | Yes | Phase of the control plan | `"Production"` | Prototype; Pre Launch; Production |
| 9 | version | Int32 | Yes | Version of the control plan | `NumberInt(3)` |  |
| 10 | routingId | String | Yes | Reference to u_mes_prod_routing._id | `"RTG-5110-10-0100-R01"` | Reference: u_mes_prod_routing._id |
| 11 | routingName | String | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH assembly routing"` |  |
| 12 | pfmeaId | String | No (null allowed) | Reference to u_mes_qual_pfmea._id | `"FMEA-5110-10-0100-PF"` | Reference: u_mes_qual_pfmea._id |
| 13 | pfmeaName | String | No (null allowed) | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front Brake Caliper Assembly LH"` |  |
| 14 | customerApprovalDate | Date | No (null allowed) | Customer approval date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 15 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 17 | preparedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'prepared' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 18 | preparedBy | String | Yes | Display name of the user in preparedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | approvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 20 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 21 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 22 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 23 | originalDate | Date | Yes | Original date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 24 | revisionDate | Date | Yes | Revision date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 25 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 26 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ routingId: 1 }` | No | Look-up of documents by routing |
| 5 | `{ pfmeaId: 1 }` | No | Look-up of documents by PFMEA |
| 6 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |

## Referenced by

u_mes_qual_controlPlanCoreTeamUser, u_mes_qual_controlPlanLine, u_mes_qual_inspectionPlan, u_mes_qual_capa, u_mes_qual_pfmea, u_mes_qual_ppapSubmission.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_controlPlan.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_controlPlan.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_controlPlan.js
