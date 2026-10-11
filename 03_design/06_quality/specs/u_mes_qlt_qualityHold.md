# u_mes_qlt_qualityHold

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Hold / quarantine on units, lots, containers or locations with reason and release decision |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | HLD-<recordNo> |
| Display value used by references | recordNo |
| Keys | 33 (20 required, 13 may be null) |
| Estimated volume per year | ~2,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per quality hold, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with qualityHoldId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_qualityHoldHeldObject | Child | held object |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: HLD-<recordNo> | `"HLD-2026-000021"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000021"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | holdType | String | Yes | Hold type | `"Quality"` | Quality; Customer; Engineering; Supplier |
| 6 | reasonText | String | No (null allowed) | Reason text | `"Replenishment against kanban call"` |  |
| 7 | reasonCodeId | String | No (null allowed) | Reference to u_mes_eqp_reasonCode._id | `"RSN-MECH-NR-02"` | Reference: u_mes_eqp_reasonCode._id |
| 8 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_eqp_reasonCode.name | `"Nutrunner socket worn"` |  |
| 9 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qlt_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 10 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 11 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 12 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 13 | totalQuantity | Int32 | Yes | Total quantity | `NumberInt(480)` |  |
| 14 | quarantineLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: quarantine location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 15 | quarantineLocationName | String | No (null allowed) | Display value of quarantineLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 16 | placedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'placed' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 17 | placedBy | String | Yes | Display name of the user in placedById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 18 | placedAt | Date | Yes | Date and time when the record was placed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 19 | expectedReleaseAt | Date | No (null allowed) | Expected release date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 20 | releasedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'released' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 21 | releasedBy | String | No (null allowed) | Display name of the user in releasedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 22 | releasedAt | Date | No (null allowed) | Date and time when the record was released | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 23 | releaseDecision | String | No (null allowed) | Release decision | `"Released"` | Released; Rework; Scrap; Return To Supplier |
| 24 | releaseComment | String | No (null allowed) | Release comment | `"100 percent leak retest completed, 2 units reworked"` |  |
| 25 | customerNotified | Boolean | Yes | True when: customer notified | `true` |  |
| 26 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | Active; Partially Released; Released |
| 27 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 29 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 30 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 31 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 32 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 33 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Active, Partially Released, Released. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 4 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ quarantineLocationId: 1 }` | No | Look-up of documents by quarantine location |
| 7 | `{ siteId: 1, placedAt: -1 }` | No | Time-ordered lists and reports by placed at |

## Referenced by

u_mes_exe_wipUnit, u_mes_exe_lot, u_mes_qlt_nonconformance, u_mes_qlt_qualityHoldHeldObject.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_qualityHold.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_qualityHold.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_qualityHold.js
