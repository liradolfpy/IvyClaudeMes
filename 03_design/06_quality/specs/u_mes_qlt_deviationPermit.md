# u_mes_qlt_deviationPermit

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Temporary deviations / concessions approved by the customer with quantity or date limit |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | DEV-<recordNo> |
| Display value used by references | title |
| Keys | 38 (27 required, 11 may be null) |
| Estimated volume per year | ~100 |
| Storage | standard |

## Structure

Flat entity collection: one document per deviation permit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with deviationPermitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_deviationPermitApproval | Child | approval |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DEV-<recordNo> | `"DEV-2026-0006"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0006"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the deviation permit; used as its display value in other collections | `"Anodising thickness upper limit deviation"` |  |
| 6 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 7 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | characteristicId | String | No (null allowed) | Reference to u_mes_qlt_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qlt_characteristic._id |
| 9 | characteristicName | String | No (null allowed) | Display value of characteristicId, copied from u_mes_qlt_characteristic.name | `"Piston bore diameter"` |  |
| 10 | deviationType | String | Yes | Deviation type | `"Product"` | Product; Process; Material |
| 11 | description | String | Yes | Description of the deviation permit | `"Coating thickness up to 16.5 um accepted against 16.0 um maximum for 2,000 pieces"` |  |
| 12 | requestedValue | Decimal128 | Yes | Requested value | `NumberDecimal("16.5")` |  |
| 13 | specifiedValue | Decimal128 | Yes | Specified value | `NumberDecimal("16.0")` |  |
| 14 | customerId | String | Yes | Reference to u_mes_mdm_customer._id | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 15 | customerName | String | Yes | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 16 | customerApprovalRef | String | No (null allowed) | Customer approval ref | `"SML/DEV/2026/044"` |  |
| 17 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qlt_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 18 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 19 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prd_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 20 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 21 | limitType | String | Yes | Limit type | `"Quantity"` | Quantity; Date |
| 22 | quantityLimit | Int32 | No (null allowed) | Quantity limit | `NumberInt(2000)` |  |
| 23 | quantityUsed | Int32 | Yes | Quantity used | `NumberInt(480)` |  |
| 24 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 25 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 26 | markingRequirement | String | No (null allowed) | Marking requirement | `"Green dot on bin label"` |  |
| 27 | requestedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'requested' | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 28 | requestedBy | String | Yes | Display name of the user in requestedById, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 29 | requestedAt | Date | Yes | Date and time when the record was requested | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 30 | closedAt | Date | No (null allowed) | Date and time when the record was closed | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Requested; Approved; Expired; Closed; Rejected |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 34 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 35 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 36 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 37 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 38 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Requested, Approved, Expired, Closed, Rejected. Initial state: Requested. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 5 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 6 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 7 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 8 | `{ siteId: 1, validFrom: -1 }` | No | Time-ordered lists and reports by valid from |

## Referenced by

u_mes_trc_asBuiltRecord, u_mes_qlt_deviationPermitApproval.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_deviationPermit.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_deviationPermit.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_deviationPermit.js
