# u_mes_qual_deviationPermit

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Temporary deviations / concessions approved by the customer with quantity or date limit |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 38 (27 required, 11 may be null) |
| Estimated volume per year | ~100 |
| Storage | standard |

## Structure

Flat entity collection: one document per deviation permit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with deviationPermitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_deviationPermitApproval | Child | approval |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1174000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DEV-2026-0006"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title of the deviation permit; used as its display value in other collections | `"Wall thickness 7.4 mm accepted on 500 castings"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 8 | characteristicId | String | - | No (null allowed) | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - | No (null allowed) | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 10 | deviationType | String | - | Yes | Deviation type | `"Product"` | Product; Process; Material |
| 11 | description | String | - | Yes | Description of the deviation permit | `"Temporary deviation on 'casting wall thickness at bridge' at gravity die casting; all affected containers carry a deviation tag"` |  |
| 12 | requestedValue | Decimal128 | - | Yes | Requested value | `NumberDecimal("16.5")` |  |
| 13 | specifiedValue | Decimal128 | - | Yes | Specified value | `NumberDecimal("16.0")` |  |
| 14 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 15 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 16 | customerApprovalRef | String | - | No (null allowed) | Customer approval ref | `"SML/DEV/2026/044"` |  |
| 17 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 18 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 19 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 20 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 21 | limitType | String | - | Yes | Limit type | `"Quantity"` | Quantity; Date |
| 22 | quantityLimit | Int32 | - | No (null allowed) | Quantity limit | `NumberInt(2000)` |  |
| 23 | quantityUsed | Int32 | - | Yes | Quantity used | `NumberInt(480)` |  |
| 24 | validFrom | Date | Date | Yes | Valid from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 25 | validTo | Date | Date | No (null allowed) | Valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 26 | markingRequirement | String | - | No (null allowed) | Marking requirement | `"Green dot on bin label"` |  |
| 27 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 28 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 29 | requestedAt | Date | Datetime | Yes | Date and time when the record was requested. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:10.000+0000")` |  |
| 30 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Requested"` | Requested; Approved; Expired; Closed; Rejected |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 34 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 36 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:10.000+0000")` |  |
| 37 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Requested, Approved, Expired, Closed, Rejected. Initial state: Requested. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_trac_asBuiltRecord, u_mes_qual_deviationPermitApproval, u_mes_bmr_batchRelease.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_deviationPermit.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_deviationPermit.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_deviationPermit.js
