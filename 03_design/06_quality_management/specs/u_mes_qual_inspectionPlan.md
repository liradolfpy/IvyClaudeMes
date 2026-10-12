# u_mes_qual_inspectionPlan

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Executable data-collection group per operation: which characteristics, sample size, frequency, reaction |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 27 (16 required, 11 may be null) |
| Estimated volume per year | 1,000-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per inspection plan, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with inspectionPlanId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_inspectionPlanLine | Child | line |
| u_mes_qual_inspectionPlanProductVariant | Relationship | product variant |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1142000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"INP-OP010"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the inspection plan; used as its display value in other collections | `"In-process inspection, gravity die casting"` |  |
| 6 | controlPlanId | String | - | No (null allowed) | Reference to u_mes_qual_controlPlan._id | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 7 | controlPlanName | String | - | No (null allowed) | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 10 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 11 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 12 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 14 | planType | String | - | Yes | Plan type | `"In Process"` | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| 15 | version | Int32 | - | Yes | Version of the inspection plan | `NumberInt(1)` |  |
| 16 | collectionTrigger | String | - | Yes | Collection trigger | `"Operation Start"` | Operation Start; Operation Complete; Time Interval; Unit Count; Goods Receipt; Changeover |
| 17 | samplingPlanId | String | - | No (null allowed) | Reference to u_mes_qual_samplingPlan._id | `"1144000000000001"` | Reference: u_mes_qual_samplingPlan._id |
| 18 | samplingPlanName | String | - | No (null allowed) | Display value of samplingPlanId, copied from u_mes_qual_samplingPlan.name | `"AQL 1.0, general inspection level II"` |  |
| 19 | blockOnFail | Boolean | - | Yes | True when: block on fail | `true` |  |
| 20 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 21 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 22 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 23 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 24 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 25 | itemRevision | String | - | No (null allowed) | Item revision the plan applies to; null = all revisions | `null` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ controlPlanId: 1 }` | No | Look-up of documents by control plan |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 6 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 7 | `{ samplingPlanId: 1 }` | No | Look-up of documents by sampling plan |

## Referenced by

u_mes_prod_billOfProcessStep, u_mes_qual_inspectionPlanLine, u_mes_qual_inspectionResult, u_mes_syst_operatorAppStep, u_mes_qual_inspectionPlanProductVariant.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_inspectionPlan.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_inspectionPlan.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_inspectionPlan.js
