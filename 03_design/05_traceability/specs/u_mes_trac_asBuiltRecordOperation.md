# u_mes_trac_asBuiltRecordOperation

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | One document per operation of a as built record |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_trac_asBuiltRecord |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 28 (19 required, 9 may be null) |

## Structure

Child collection. The parent as built record can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. asBuiltRecordId and asBuiltRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1136000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ABR-VB26258A00184-O01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | asBuiltRecordId | String | - | Yes | Reference to u_mes_trac_asBuiltRecord._id: the parent document this one belongs to | `"1134000000000001"` | Reference: u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - | Yes | Display value of asBuiltRecordId, copied from u_mes_trac_asBuiltRecord.recordNo | `"ABR-VB26258A00184"` |  |
| 7 | stepNo | Int32 | - | Yes | Step number within the parent record | `NumberInt(10)` |  |
| 8 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 10 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 12 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 13 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 14 | operatorUserId | String | - | Yes | Reference to u_mes_mast_user._id: operator user | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 15 | operatorUserName | String | - | Yes | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 16 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:50.000+0000")` |  |
| 17 | result | String | - | Yes | Result of the as built record operation | `"OK"` | OK; Not OK |
| 18 | recipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id | `"1073000000000001"` | Reference: u_mes_prod_recipe._id |
| 19 | recipeName | String | - | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `"Caliper body LH casting parameters"` |  |
| 20 | recipeVersion | String | - | No (null allowed) | Version of the recipe / program | `"1"` |  |
| 21 | recipeChecksum | String | - | No (null allowed) | Checksum of the program | `"9f2c4a1be07d53c6"` |  |
| 22 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 23 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:20.000+0000")` |  |
| 24 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 25 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 26 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:50.000+0000")` |  |
| 27 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 28 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ asBuiltRecordId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ workCenterId: 1 }` | No | Look-up of lines by work center |
| 4 | `{ equipmentId: 1 }` | No | Look-up of lines by equipment |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_asBuiltRecordOperation.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_asBuiltRecordOperation.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_asBuiltRecordOperation.js
