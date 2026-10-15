# u_mes_qual_deviationPermit

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Temporary deviations / concessions approved by the customer with quantity or date limit |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 39 (28 required, 11 may be null) |
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
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the deviation permit; used as its display value in other collections | `"Wall thickness 7.4 mm accepted on 500 castings"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 9 | characteristicId | String | - | No (null allowed) | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - | No (null allowed) | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 11 | deviationType | String | - | Yes | Deviation type | `"Product"` | Product; Process; Material |
| 12 | description | String | - | Yes | Description of the deviation permit | `"Temporary deviation on 'casting wall thickness at bridge' at gravity die casting; all affected containers carry a deviation tag"` |  |
| 13 | requestedValue | Decimal128 | - | Yes | Requested value | `NumberDecimal("16.5")` |  |
| 14 | specifiedValue | Decimal128 | - | Yes | Specified value | `NumberDecimal("16.0")` |  |
| 15 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 16 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 17 | customerApprovalRef | String | - | No (null allowed) | Customer approval ref | `"SML/DEV/2026/044"` |  |
| 18 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 19 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 20 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `null` | Reference: u_mes_prod_engineeringChange._id |
| 21 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `null` |  |
| 22 | limitType | String | - | Yes | Limit type | `"Quantity"` | Quantity; Date |
| 23 | quantityLimit | Int32 | - | No (null allowed) | Quantity limit | `NumberInt(2000)` |  |
| 24 | quantityUsed | Int32 | - | Yes | Quantity used | `NumberInt(480)` |  |
| 25 | validFrom | Date | Date | Yes | Valid from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 26 | validTo | Date | Date | No (null allowed) | Valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 27 | markingRequirement | String | - | No (null allowed) | Marking requirement | `"Green dot on bin label"` |  |
| 28 | requestedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'requested' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 29 | requestedBy | String | - | Yes | Display name of the user in requestedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 30 | requestedAt | Date | Datetime | Yes | Date and time when the record was requested. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:10.000+0000")` |  |
| 31 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 32 | status | String | - | Yes | Primary lifecycle state of the document | `"Requested"` | Requested; Approved; Expired; Closed; Rejected |
| 33 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 35 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 37 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:10.000+0000")` |  |
| 38 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
