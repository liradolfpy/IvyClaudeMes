# u_mes_prod_engineeringChange

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Engineering change notices with affected objects, approvals and effectivity (cut-in serial / date) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 31 (23 required, 8 may be null) |
| Estimated volume per year | 200-1,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per engineering change, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with engineeringChangeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_engineeringChangeAffectedItem | Child | affected item |
| u_mes_prod_engineeringChangeAffectedObject | Child | affected object |
| u_mes_prod_engineeringChangeApproval | Child | approval |
| u_mes_prod_engineeringChangeControlledDocument | Relationship | controlled document |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1076000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ECN-2026-0027"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the engineering change; used as its display value in other collections | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 6 | description | String | Yes | Description of the engineering change | `"Change request: bleed screw torque window revised to 14 +/- 2 n.m. Affected process step: gravity die casting"` |  |
| 7 | changeType | String | Yes | Change type | `"Process Change"` | Design Change; Process Change; Material Change; Supplier Change; Tooling Change; Document Change |
| 8 | reasonCodeText | String | Yes | Reason code text | `"Customer request after field study of bleed screw seepage"` |  |
| 9 | originator | String | Yes | Originator of the engineering change | `"Customer"` | Customer; Internal; Supplier |
| 10 | customerId | String | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 11 | customerName | String | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 12 | customerChangeRef | String | No (null allowed) | Customer change ref | `"SML-ECR-2026-118"` |  |
| 13 | raisedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'raised' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 14 | raisedBy | String | Yes | Display name of the user in raisedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 15 | raisedAt | Date | Yes | Date and time when the record was raised | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 16 | effectivityType | String | Yes | Effectivity type | `"Date"` | Date; Serial Number; Lot; Stock Run Out |
| 17 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 18 | cutInSerialNo | String | No (null allowed) | Cut in serial number | `"VB26272A00001"` |  |
| 19 | stockDispositionTypeId | String | No (null allowed) | Reference to u_mes_qual_dispositionType._id: stock disposition type | `"1284000000000001"` | Reference: u_mes_qual_dispositionType._id |
| 20 | stockDispositionTypeName | String | No (null allowed) | Display value of stockDispositionTypeId, copied from u_mes_qual_dispositionType.name | `"Use As Is"` |  |
| 21 | ppapRequired | Boolean | Yes | True when: PPAP required | `false` |  |
| 22 | implementedAt | Date | No (null allowed) | Date and time when the record was implemented | `null` |  |
| 23 | closedAt | Date | No (null allowed) | Date and time when the record was closed | `null` |  |
| 24 | status | String | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Under Evaluation; Approved; Implemented; Closed; Rejected |
| 25 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 27 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 28 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 29 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 30 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 31 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Raised, Under Evaluation, Approved, Implemented, Closed, Rejected. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ stockDispositionTypeId: 1 }` | No | Look-up of documents by stock disposition type |
| 5 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_prod_itemRevision, u_mes_prod_billOfMaterial, u_mes_prod_routing, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_prod_engineeringChangeAffectedItem, u_mes_prod_engineeringChangeAffectedObject, u_mes_prod_engineeringChangeApproval, u_mes_prod_engineeringChangeControlledDocument, u_mes_qual_controlPlan, u_mes_qual_deviationPermit, u_mes_qual_ppapSubmission.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_engineeringChange.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_engineeringChange.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_engineeringChange.js
