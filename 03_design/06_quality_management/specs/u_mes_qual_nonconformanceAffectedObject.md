# u_mes_qual_nonconformanceAffectedObject

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per affected object of a nonconformance |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_nonconformance |
| _id pattern | <nonconformanceId>-AO<nnn> |
| Display value used by references | recordNo |
| Keys | 23 (18 required, 5 may be null) |

## Structure

Child collection. The parent nonconformance can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. nonconformanceId and nonconformanceName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <nonconformanceId>-AO<nnn> | `"NCR-2026-000118-AO001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000118-AO001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | Yes | Reference to u_mes_qual_nonconformance._id: the parent document this one belongs to | `"NCR-2026-000118"` | Reference: u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | Yes | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_plan_wipUnit"` |  |
| 9 | relatedEntityId | String | Yes | _id of the related document in the collection named by relatedCollectionName | `"WU-U260929A0184"` | Reference: Any collection (see relatedCollectionName) |
| 10 | relatedEntityName | String | Yes | Display value of the related document | `"U260929A0184"` |  |
| 11 | quantity | Int32 | Yes | Quantity of the nonconformance affected object | `NumberInt(1)` |  |
| 12 | dispositionTypeId | String | No (null allowed) | Reference to u_mes_qual_dispositionType._id | `"DSP-T-REWORK"` | Reference: u_mes_qual_dispositionType._id |
| 13 | dispositionTypeName | String | No (null allowed) | Display value of dispositionTypeId, copied from u_mes_qual_dispositionType.name | `"Rework"` |  |
| 14 | dispositionById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'disposition' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 15 | dispositionBy | String | No (null allowed) | Display name of the user in dispositionById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | dispositionAt | Date | No (null allowed) | Disposition date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 19 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 21 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 22 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_nonconformanceAffectedObject.js
