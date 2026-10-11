# u_mes_qlt_defectCode

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Defect / NC code catalogue with group, default disposition routing and severity |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | DEF-<recordNo> |
| Display value used by references | name |
| Keys | 21 (19 required, 2 may be null) |
| Estimated volume per year | 100-400 |
| Storage | standard |

## Structure

Flat entity collection: one document per defect code, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with defectCodeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_defectCodeApplicableOperation | Relationship | applicable operation |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DEF-<recordNo> | `"DEF-LK01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LK01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the defect code; used as its display value in other collections | `"Leak at piston seal"` |  |
| 6 | defectGroupId | String | Yes | Reference to u_mes_qlt_defectGroup._id | `"DGR-LEAK"` | Reference: u_mes_qlt_defectGroup._id |
| 7 | defectGroupName | String | Yes | Display value of defectGroupId, copied from u_mes_qlt_defectGroup.name | `"Leak"` |  |
| 8 | description | String | Yes | Description of the defect code | `"Pressure decay above limit traced to the piston seal"` |  |
| 9 | severity | Int32 | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 10 | defaultDispositionTypeId | String | Yes | Reference to u_mes_qlt_dispositionType._id: default disposition type | `"DSP-T-REWORK"` | Reference: u_mes_qlt_dispositionType._id |
| 11 | defaultDispositionTypeName | String | Yes | Display value of defaultDispositionTypeId, copied from u_mes_qlt_dispositionType.name | `"Rework"` |  |
| 12 | dispositionRoutingId | String | Yes | Reference to u_mes_prd_routing._id: disposition routing | `"RTG-5110-10-0100-R01"` | Reference: u_mes_prd_routing._id |
| 13 | dispositionRoutingName | String | Yes | Display value of dispositionRoutingId, copied from u_mes_prd_routing.description | `"Front caliper LH assembly routing"` |  |
| 14 | isSafetyRelated | Boolean | Yes | True when the record is safety related | `false` |  |
| 15 | requiresPhoto | Boolean | Yes | True when photo is required | `false` |  |
| 16 | requiresHold | Boolean | Yes | True when hold is required | `false` |  |
| 17 | scrapCostCategory | String | Yes | Scrap cost category | `"Assembly Scrap"` | Casting Scrap; Machining Scrap; Assembly Scrap; Supplier Chargeable |
| 18 | customerDefectCode | String | No (null allowed) | Customer defect code | `"SM-Q-0417"` |  |
| 19 | pfmeaFailureMode | String | No (null allowed) | PFMEA failure mode | `"Fluid leak past piston seal"` |  |
| 20 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 21 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ defectGroupId: 1 }` | No | Look-up of documents by defect group |
| 4 | `{ defaultDispositionTypeId: 1 }` | No | Look-up of documents by default disposition type |
| 5 | `{ dispositionRoutingId: 1 }` | No | Look-up of documents by disposition routing |

## Referenced by

u_mes_exe_operationExecutionDefectCode, u_mes_qlt_inspectionPlanLine, u_mes_qlt_inspectionResult, u_mes_qlt_defectCodeApplicableOperation, u_mes_qlt_nonconformance, u_mes_qlt_scrapRecord.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_defectCode.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_defectCode.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_defectCode.js
