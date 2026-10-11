# u_mes_qual_reworkOrder

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Rework instruction and execution on the rework routing with re-inspection result |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | RWK-<recordNo> |
| Display value used by references | recordNo |
| Keys | 39 (32 required, 7 may be null) |
| Estimated volume per year | ~5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per rework order, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with reworkOrderId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_reworkOrderWipUnit | Relationship | wip unit |
| u_mes_qual_reworkOrderStep | Child | step |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: RWK-<recordNo> | `"RWK-2026-000052"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000052"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | Yes | Reference to u_mes_qual_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | Yes | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 7 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 8 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 9 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | quantity | Int32 | Yes | Quantity of the rework order | `NumberInt(1)` |  |
| 12 | reworkRoutingId | String | Yes | Reference to u_mes_prod_routing._id: rework routing | `"RTG-5110-10-0100-RW1"` | Reference: u_mes_prod_routing._id |
| 13 | reworkRoutingName | String | Yes | Display value of reworkRoutingId, copied from u_mes_prod_routing.description | `"Front caliper LH rework routing"` |  |
| 14 | reworkType | String | Yes | Rework type | `"Replace Component"` | Replace Component; Retighten; Re-machine; Re-anodise; Re-mark; Clean |
| 15 | instruction | String | Yes | Instruction of the rework order | `"Dismantle piston, replace seal with new lot, reassemble and repeat leak test"` |  |
| 16 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 17 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 18 | issuedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'issued' | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 19 | issuedBy | String | Yes | Display name of the user in issuedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 20 | issuedAt | Date | Yes | Date and time when the record was issued | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 21 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 22 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 23 | reinspectionResult | String | No (null allowed) | Reinspection result | `"Pass"` | Pass; Fail |
| 24 | reinspectedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reinspected' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 25 | reinspectedBy | String | No (null allowed) | Display name of the user in reinspectedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 26 | reinspectedAt | Date | No (null allowed) | Date and time when the record was reinspected | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 27 | quantityRecovered | Int32 | Yes | Quantity recovered | `NumberInt(4)` |  |
| 28 | quantityScrapped | Int32 | Yes | Quantity scrapped | `NumberInt(2)` |  |
| 29 | reworkAttemptNo | Int32 | Yes | Rework attempt number | `NumberInt(1)` |  |
| 30 | returnStepNo | Int32 | Yes | Return step number | `NumberInt(80)` |  |
| 31 | labourMinutes | Int32 | Yes | Labour (minutes) | `NumberInt(35)` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Issued; In Progress; Awaiting Reinspection; Completed; Scrapped |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 35 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 37 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 38 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Issued, In Progress, Awaiting Reinspection, Completed, Scrapped. Initial state: Issued. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 4 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ reworkRoutingId: 1 }` | No | Look-up of documents by rework routing |
| 7 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 8 | `{ siteId: 1, issuedAt: -1 }` | No | Time-ordered lists and reports by issued at |

## Referenced by

u_mes_qual_nonconformanceReworkOrder, u_mes_qual_reworkOrderWipUnit, u_mes_qual_reworkOrderStep.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_reworkOrder.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_reworkOrder.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_reworkOrder.js
