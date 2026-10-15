# u_mes_plan_setupVerificationItem

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | One document per item of a setup verification |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_setupVerification |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 26 (18 required, 8 may be null) |

## Structure

Child collection. The parent setup verification can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. setupVerificationId and setupVerificationName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1310000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SUV-20260915-00012-I01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | setupVerificationId | String | - | Yes | Reference to u_mes_plan_setupVerification._id: the parent document this one belongs to | `"1309000000000001"` | Reference: u_mes_plan_setupVerification._id |
| 7 | setupVerificationName | String | - | Yes | Display value of setupVerificationId, copied from u_mes_plan_setupVerification.recordNo | `"SUV-20260915-00012"` |  |
| 8 | itemNo | Int32 | - | Yes | Check number within the verification | `NumberInt(1)` |  |
| 9 | checkType | String | - | Yes | What is checked | `"Fixture"` | Variant; Fixture; Tool; Program; Parameter; Component; Gauge |
| 10 | relatedCollectionName | String | - | No (null allowed) | Name of the collection the related document is in | `"u_mes_maint_tool"` |  |
| 11 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1226000000000006"` | Reference: Any collection (see relatedCollectionName) |
| 12 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"Seal insertion sleeve 54 mm"` |  |
| 13 | scannedCode | String | - | No (null allowed) | Code scanned at the station | `"SLV-54-0008"` |  |
| 14 | expectedValue | Decimal128 | - | No (null allowed) | Expected numeric value for parameter checks | `null` |  |
| 15 | actualValue | Decimal128 | - | No (null allowed) | Actual numeric value | `null` |  |
| 16 | unitOfMeasureId | String | - | No (null allowed) | Reference to u_mes_mast_unitOfMeasure._id | `null` | Reference: u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - | No (null allowed) | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `null` |  |
| 18 | passed | Boolean | - | Yes | Check result | `true` |  |
| 19 | checkedAt | Date | Datetime | Yes | Time of the check | `ISODate("2026-09-15T05:45:00.000+0000")` |  |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 21 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:45:00.000+0000")` |  |
| 22 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 24 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:45:00.000+0000")` |  |
| 25 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 26 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ setupVerificationId: 1, itemNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ unitOfMeasureId: 1 }` | No | Look-up of lines by unit of measure |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_setupVerificationItem.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_setupVerificationItem.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_setupVerificationItem.js
