# u_mes_qual_qualityHold

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Hold / quarantine on units, lots, containers or locations with reason and release decision |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 38 (21 required, 17 may be null) |
| Estimated volume per year | ~2,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per quality hold, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with qualityHoldId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_qualityHoldHeldObject | Child | held object |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1172000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"HLD-2026-000021"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | holdType | String | - | Yes | Hold type | `"Supplier"` | Quality; Customer; Engineering; Supplier |
| 7 | reasonText | String | - | No (null allowed) | Reason text | `"Hold pending disposition of nonconformance: Seal cut at piston insertion, supplier lot ES-260905-11"` |  |
| 8 | reasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000006"` | Reference: u_mes_perf_reasonCode._id |
| 9 | reasonCodeName | String | - | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Seal feeder jam"` |  |
| 10 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000006"` | Reference: u_mes_qual_nonconformance._id |
| 11 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Seal cut at piston insertion, supplier lot ES-260905-11"` |  |
| 12 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 13 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 14 | totalQuantity | Int32 | - | Yes | Total quantity | `NumberInt(480)` |  |
| 15 | quarantineLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: quarantine location | `"1112000000000007"` | Reference: u_mes_matl_storageLocation._id |
| 16 | quarantineLocationName | String | - | No (null allowed) | Display value of quarantineLocationId, copied from u_mes_matl_storageLocation.name | `"Quarantine cage, quality"` |  |
| 17 | placedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'placed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | placedBy | String | - | Yes | Display name of the user in placedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | placedAt | Date | Datetime | Yes | Date and time when the record was placed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:26:10.000+0000")` |  |
| 20 | expectedReleaseAt | Date | Datetime | No (null allowed) | Expected release date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 21 | releasedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'released' | `null` | Reference: u_mes_mast_user._id |
| 22 | releasedBy | String | - | No (null allowed) | Display name of the user in releasedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | releasedAt | Date | Datetime | No (null allowed) | Date and time when the record was released. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | releaseDecision | String | - | No (null allowed) | Release decision | `null` | Released; Rework; Scrap; Return To Supplier |
| 25 | releaseComment | String | - | No (null allowed) | Release comment | `"100 percent leak retest completed, 2 units reworked"` |  |
| 26 | customerNotified | Boolean | - | Yes | True when: customer notified | `true` |  |
| 27 | releaseReasonCodeId | String | - | No (null allowed) | Reference to u_mes_perf_reasonCode._id: release reason code | `null` | Reference: u_mes_perf_reasonCode._id |
| 28 | releaseReasonCodeName | String | - | No (null allowed) | Display value of releaseReasonCodeId, copied from u_mes_perf_reasonCode.name | `null` |  |
| 29 | releaseElectronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id: release electronic signature | `null` | Reference: u_mes_syst_electronicSignature._id |
| 30 | releaseElectronicSignatureName | String | - | No (null allowed) | Display value of releaseElectronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Partially Released; Released |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:25:40.000+0000")` |  |
| 34 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 36 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:26:10.000+0000")` |  |
| 37 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Active, Partially Released, Released. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 4 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ quarantineLocationId: 1 }` | No | Look-up of documents by quarantine location |
| 7 | `{ releaseReasonCodeId: 1 }` | No | Look-up of documents by release reason code |
| 8 | `{ siteId: 1, placedAt: -1 }` | No | Time-ordered lists and reports by placed at |

## Referenced by

u_mes_plan_productionOrder, u_mes_plan_wipUnit, u_mes_plan_lot, u_mes_qual_spcSample, u_mes_qual_nonconformance, u_mes_qual_qualityHoldHeldObject, u_mes_trac_traceInvestigation, u_mes_bmr_batchRelease.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_qualityHold.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_qualityHold.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_qualityHold.js
