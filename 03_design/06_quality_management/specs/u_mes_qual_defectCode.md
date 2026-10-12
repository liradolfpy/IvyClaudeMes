# u_mes_qual_defectCode

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Defect / NC code catalogue with group, default disposition routing and severity |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 21 (19 required, 2 may be null) |
| Estimated volume per year | 100-400 |
| Storage | standard |

## Structure

Flat entity collection: one document per defect code, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with defectCodeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_defectCodeApplicableOperation | Relationship | applicable operation |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1158000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CS01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the defect code; used as its display value in other collections | `"Shrinkage porosity"` |  |
| 6 | defectGroupId | String | - | Yes | Reference to u_mes_qual_defectGroup._id | `"1282000000000001"` | Reference: u_mes_qual_defectGroup._id |
| 7 | defectGroupName | String | - | Yes | Display value of defectGroupId, copied from u_mes_qual_defectGroup.name | `"Casting"` |  |
| 8 | description | String | - | Yes | Description of the defect code | `"Porosity visible on machined face or found by X-ray sampling"` |  |
| 9 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 10 | defaultDispositionTypeId | String | - | Yes | Reference to u_mes_qual_dispositionType._id: default disposition type | `"1284000000000001"` | Reference: u_mes_qual_dispositionType._id |
| 11 | defaultDispositionTypeName | String | - | Yes | Display value of defaultDispositionTypeId, copied from u_mes_qual_dispositionType.name | `"Use As Is"` |  |
| 12 | dispositionRoutingId | String | - | Yes | Reference to u_mes_prod_routing._id: disposition routing | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 13 | dispositionRoutingName | String | - | Yes | Display value of dispositionRoutingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 14 | isSafetyRelated | Boolean | - | Yes | True when the record is safety related | `false` |  |
| 15 | requiresPhoto | Boolean | - | Yes | True when photo is required | `false` |  |
| 16 | requiresHold | Boolean | - | Yes | True when hold is required | `false` |  |
| 17 | scrapCostCategory | String | - | Yes | Scrap cost category | `"Machining Scrap"` | Casting Scrap; Machining Scrap; Assembly Scrap; Supplier Chargeable |
| 18 | customerDefectCode | String | - | No (null allowed) | Customer defect code | `"SM-Q-0417"` |  |
| 19 | pfmeaFailureMode | String | - | No (null allowed) | PFMEA failure mode | `"Shrinkage porosity in the bridge section"` |  |
| 20 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ defectGroupId: 1 }` | No | Look-up of documents by defect group |
| 4 | `{ defaultDispositionTypeId: 1 }` | No | Look-up of documents by default disposition type |
| 5 | `{ dispositionRoutingId: 1 }` | No | Look-up of documents by disposition routing |

## Referenced by

u_mes_plan_operationExecutionDefectCode, u_mes_qual_inspectionPlanLine, u_mes_qual_inspectionResult, u_mes_qual_defectCodeApplicableOperation, u_mes_qual_nonconformance, u_mes_qual_scrapRecord, u_mes_qual_defectRecord.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_defectCode.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_defectCode.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_defectCode.js
