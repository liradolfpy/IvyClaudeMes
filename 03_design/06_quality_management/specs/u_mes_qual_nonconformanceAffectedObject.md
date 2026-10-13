# u_mes_qual_nonconformanceAffectedObject

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per affected object of a nonconformance |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_nonconformance |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 24 (19 required, 5 may be null) |

## Structure

Child collection. The parent nonconformance can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. nonconformanceId and nonconformanceName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1161000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"NCR-2026-000118-AO01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | nonconformanceId | String | - | Yes | Reference to u_mes_qual_nonconformance._id: the parent document this one belongs to | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - | Yes | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_wipUnit"` |  |
| 10 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1094000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | Yes | Display value of the related document | `"U260915A0184"` |  |
| 12 | quantity | Int32 | - | Yes | Quantity of the nonconformance affected object | `NumberInt(1)` |  |
| 13 | dispositionTypeId | String | - | No (null allowed) | Reference to u_mes_qual_dispositionType._id | `"1284000000000001"` | Reference: u_mes_qual_dispositionType._id |
| 14 | dispositionTypeName | String | - | No (null allowed) | Display value of dispositionTypeId, copied from u_mes_qual_dispositionType.name | `"Use As Is"` |  |
| 15 | dispositionById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'disposition' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | dispositionBy | String | - | No (null allowed) | Display name of the user in dispositionById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | dispositionAt | Date | Datetime | No (null allowed) | Disposition date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 20 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 22 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 23 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ nonconformanceId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ dispositionTypeId: 1 }` | No | Look-up of lines by disposition type |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_nonconformanceAffectedObject.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_nonconformanceAffectedObject.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_nonconformanceAffectedObject.js
