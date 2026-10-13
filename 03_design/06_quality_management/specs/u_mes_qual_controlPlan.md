# u_mes_qual_controlPlan

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | AIAG control plan per item and phase (prototype, pre-launch, production) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
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

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1139000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CP-5110-10-0100-PROD"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 8 | phase | String | - | Yes | Phase of the control plan | `"Prototype"` | Prototype; Pre Launch; Production |
| 9 | version | Int32 | - | Yes | Version of the control plan | `NumberInt(1)` |  |
| 10 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 11 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 12 | pfmeaId | String | - | No (null allowed) | Reference to u_mes_qual_pfmea._id | `"1183000000000001"` | Reference: u_mes_qual_pfmea._id |
| 13 | pfmeaName | String | - | No (null allowed) | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 14 | customerApprovalDate | Date | Date | No (null allowed) | Customer approval date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `null` |  |
| 15 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000010"` | Reference: u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Work instruction pictures updated for RH variant"` |  |
| 17 | preparedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'prepared' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | preparedBy | String | - | Yes | Display name of the user in preparedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 20 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 21 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 22 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 23 | originalDate | Date | Date | Yes | Original date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 24 | revisionDate | Date | Date | Yes | Revision date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_qual_controlPlanCoreTeamUser, u_mes_qual_controlPlanLine, u_mes_qual_inspectionPlan, u_mes_qual_capa, u_mes_qual_pfmea, u_mes_qual_ppapSubmission, u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_controlPlan.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_controlPlan.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_controlPlan.js
