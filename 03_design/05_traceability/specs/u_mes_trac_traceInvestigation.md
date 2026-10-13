# u_mes_trac_traceInvestigation

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | A saved forward or reverse trace run, its starting object and the containment it fed. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 33 (24 required, 9 may be null) |
| Estimated volume per year | about 200 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per trace investigation, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with traceInvestigationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_trac_traceInvestigationResult | Child | result |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1314000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"TRC-20260919-011"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Short title | `"Forward trace, seal lot L260905-SEL-011 after seal cut at assembly"` |  |
| 7 | direction | String | - | Yes | Trace direction | `"Forward"` | Forward; Reverse; Both |
| 8 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_lot"` | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| 9 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1096000000000006"` | Reference: Any collection (see relatedCollectionName) |
| 10 | relatedEntityName | String | - | Yes | Display value of the related document | `"L260905-SEL-011"` |  |
| 11 | depthLimit | Int32 | - | Yes | Maximum genealogy levels followed | `NumberInt(3)` |  |
| 12 | resultCount | Int32 | - | Yes | Rows found | `NumberInt(3)` |  |
| 13 | shippedCount | Int32 | - | Yes | Rows already shipped | `NumberInt(0)` |  |
| 14 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `"1172000000000001"` | Reference: u_mes_qual_qualityHold._id |
| 15 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000021"` |  |
| 16 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000006"` | Reference: u_mes_qual_nonconformance._id |
| 17 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Seal cut at piston insertion, supplier lot ES-260905-11"` |  |
| 18 | customerComplaintId | String | - | No (null allowed) | Reference to u_mes_qual_customerComplaint._id | `null` | Reference: u_mes_qual_customerComplaint._id |
| 19 | customerComplaintName | String | - | No (null allowed) | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `null` |  |
| 20 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 22 | requestedAt | Date | Datetime | Yes | Run start | `ISODate("2026-09-19T23:50:00.000+0000")` |  |
| 23 | completedAt | Date | Datetime | No (null allowed) | Run end | `ISODate("2026-09-19T23:52:00.000+0000")` |  |
| 24 | exportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: export controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 25 | exportControlledDocumentName | String | - | No (null allowed) | Display value of exportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Closed"` | Running; Completed; Closed |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:25:40.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:52:00.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Running, Completed, Closed. Initial state: Running. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ qualityHoldId: 1 }` | No | Look-up of documents by quality hold |
| 4 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 5 | `{ customerComplaintId: 1 }` | No | Look-up of documents by customer complaint |
| 6 | `{ exportControlledDocumentId: 1 }` | No | Look-up of documents by export controlled document |
| 7 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 8 | `{ siteId: 1, requestedAt: -1 }` | No | Time-ordered lists and reports by requested at |

## Referenced by

u_mes_trac_traceInvestigationResult, u_mes_qual_productRecall.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_traceInvestigation.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_traceInvestigation.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_traceInvestigation.js
