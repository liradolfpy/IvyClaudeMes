# u_mes_qual_productQualityReview

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Periodic product quality review of an item: lots made, released and rejected, deviations, complaints, CAPA, changes, recalls and capability over the review period, with conclusion and actions. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 33 (25 required, 8 may be null) |
| Estimated volume per year | about 20 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per product quality review, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1362000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PQR-5110-10-0100-2026-Q2"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | reviewPeriodFromDate | Date | Date | Yes | First day of the review period | `ISODate("2026-04-01T00:00:00.000+0000")` |  |
| 8 | reviewPeriodToDate | Date | Date | Yes | Last day of the review period | `ISODate("2026-06-30T00:00:00.000+0000")` |  |
| 9 | lotsProducedCount | Int32 | - | Yes | Lots or orders produced | `NumberInt(118)` |  |
| 10 | lotsReleasedCount | Int32 | - | Yes | Lots released | `NumberInt(117)` |  |
| 11 | lotsRejectedCount | Int32 | - | Yes | Lots rejected | `NumberInt(1)` |  |
| 12 | nonconformanceCount | Int32 | - | Yes | Nonconformances and deviations | `NumberInt(6)` |  |
| 13 | deviationPermitCount | Int32 | - | Yes | Deviation permits used | `NumberInt(1)` |  |
| 14 | customerComplaintCount | Int32 | - | Yes | Customer complaints | `NumberInt(3)` |  |
| 15 | capaCount | Int32 | - | Yes | CAPA opened | `NumberInt(2)` |  |
| 16 | engineeringChangeCount | Int32 | - | Yes | Changes implemented | `NumberInt(2)` |  |
| 17 | productRecallCount | Int32 | - | Yes | Recalls | `NumberInt(1)` |  |
| 18 | processCapabilityText | String | - | No (null allowed) | Capability of the critical characteristics | `"Bleed screw torque Cpk 1.92; pressure drop at 140 bar Cpk 2.10"` |  |
| 19 | conclusionText | String | - | No (null allowed) | Conclusion; null while in preparation | `"Process in a state of control; no change to the control strategy"` |  |
| 20 | actionsText | String | - | No (null allowed) | Actions decided | `"None"` |  |
| 21 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 22 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 23 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 24 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 25 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-07-15T11:00:00.000+0000")` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | In Preparation; In Review; Approved |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-07-15T11:00:00.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-07-15T11:00:00.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

In Preparation, In Review, Approved. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ reportControlledDocumentId: 1 }` | No | Look-up of documents by report controlled document |
| 5 | `{ siteId: 1, reviewPeriodFromDate: -1 }` | No | Time-ordered lists and reports by review period from date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_productQualityReview.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_productQualityReview.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_productQualityReview.js
