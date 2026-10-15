# u_mes_qual_productRecall

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Recall or field action for product already shipped: class, scope, reason, linked complaint, investigation and trace, quantities shipped and recovered, authority notification and effectiveness check. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 38 (26 required, 12 may be null) |
| Estimated volume per year | a few per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per product recall, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with productRecallId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_productRecallLot | Child | lot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1363000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RCL-2026-001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title | `"Recall of 120 cartons of batch PCM5B26091 with unreadable 2D code at Medicura Healthcare Kenya"` |  |
| 7 | recallClass | String | - | Yes | Recall class by health or safety risk | `"Class III"` | Class I; Class II; Class III |
| 8 | recallScope | String | - | Yes | How far the product has gone | `"Distributor"` | Customer Plant; Distributor; Field |
| 9 | reasonText | String | - | Yes | Reason for the recall | `"2D code not readable at the importer scanner"` |  |
| 10 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000015"` | Reference: u_mes_mast_customer._id |
| 11 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Medicura Healthcare Kenya Ltd."` |  |
| 12 | customerComplaintId | String | - | No (null allowed) | Reference to u_mes_qual_customerComplaint._id | `"1198000000000019"` | Reference: u_mes_qual_customerComplaint._id |
| 13 | customerComplaintName | String | - | No (null allowed) | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `"2D code not readable at the distributor scan"` |  |
| 14 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000019"` | Reference: u_mes_qual_nonconformance._id |
| 15 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"2D code grade D on cartons after print head contamination"` |  |
| 16 | traceInvestigationId | String | - | No (null allowed) | Reference to u_mes_trac_traceInvestigation._id | `null` | Reference: u_mes_trac_traceInvestigation._id |
| 17 | traceInvestigationName | String | - | No (null allowed) | Display value of traceInvestigationId, copied from u_mes_trac_traceInvestigation.title | `null` |  |
| 18 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `"1176000000000019"` | Reference: u_mes_qual_capa._id |
| 19 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `"CAPA - Unreadable carton codes"` |  |
| 20 | initiatedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'initiated' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 21 | initiatedBy | String | - | Yes | Display name of the user in initiatedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 22 | initiatedAt | Date | Datetime | Yes | Time the recall was initiated | `ISODate("2026-09-24T13:00:00.000+0000")` |  |
| 23 | authorityNotified | Boolean | - | Yes | True when the regulator was notified | `false` |  |
| 24 | authorityNotifiedAt | Date | Datetime | No (null allowed) | Time of the notification | `null` |  |
| 25 | quantityShipped | Int32 | - | Yes | Quantity shipped in the recalled lots | `NumberInt(120)` |  |
| 26 | quantityRecovered | Int32 | - | Yes | Quantity recovered so far | `NumberInt(120)` |  |
| 27 | effectivenessCheckCompleted | Boolean | - | Yes | Recall effectiveness check completed | `true` |  |
| 28 | closedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closed' | `"1029000000000017"` | Reference: u_mes_mast_user._id |
| 29 | closedBy | String | - | No (null allowed) | Display name of the user in closedById, copied from u_mes_mast_user.fullName | `"Vandana Iyer"` |  |
| 30 | closedAt | Date | Datetime | No (null allowed) | Closing time | `ISODate("2026-09-25T00:00:00.000+0000")` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Closed"` | Initiated; In Progress; Completed; Closed; Cancelled |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T13:00:00.000+0000")` |  |
| 34 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 36 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-25T00:00:00.000+0000")` |  |
| 37 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Status values

Initiated, In Progress, Completed, Closed, Cancelled. Initial state: Initiated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ customerComplaintId: 1 }` | No | Look-up of documents by customer complaint |
| 5 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 6 | `{ traceInvestigationId: 1 }` | No | Look-up of documents by trace investigation |
| 7 | `{ capaId: 1 }` | No | Look-up of documents by CAPA |
| 8 | `{ siteId: 1, initiatedAt: -1 }` | No | Time-ordered lists and reports by initiated at |

## Referenced by

u_mes_qual_productRecallLot.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_productRecall.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_productRecall.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_productRecall.js
