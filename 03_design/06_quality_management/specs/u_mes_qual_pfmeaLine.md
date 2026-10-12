# u_mes_qual_pfmeaLine

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per line of a PFMEA |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_pfmea |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (22 required, 10 may be null) |

## Structure

Child collection. The parent PFMEA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. pfmeaId and pfmeaName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1185000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PF-5110-10-0100-R01-L01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | pfmeaId | String | - | Yes | Reference to u_mes_qual_pfmea._id: the parent document this one belongs to | `"1183000000000001"` | Reference: u_mes_qual_pfmea._id |
| 6 | pfmeaName | String | - | Yes | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 7 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 10 | processFunction | String | - | Yes | Process function | `"Fill the die cavity completely with sound metal"` |  |
| 11 | failureMode | String | - | Yes | Failure mode | `"Shrinkage porosity in the bridge section"` |  |
| 12 | failureEffect | String | - | Yes | Failure effect | `"Reduced strength of caliper body, possible fluid seepage"` |  |
| 13 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 14 | characteristicId | String | - | No (null allowed) | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 15 | characteristicName | String | - | No (null allowed) | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 16 | classification | String | - | Yes | Special characteristic class from the drawing or PFMEA | `"Significant"` | Critical; Significant; Standard |
| 17 | failureCause | String | - | Yes | Failure cause | `"Die temperature too low at pour"` |  |
| 18 | preventionControl | String | - | Yes | Prevention control | `"Die temperature interlock on pour release"` |  |
| 19 | occurrence | Int32 | - | Yes | Occurrence rating 1 to 10 | `NumberInt(4)` |  |
| 20 | detectionControl | String | - | Yes | Detection control | `"X-ray sampling, 1 per 50 castings"` |  |
| 21 | detection | Int32 | - | Yes | Detection rating 1 to 10 | `NumberInt(5)` |  |
| 22 | rpn | Int32 | - | Yes | Severity x occurrence x detection | `NumberInt(160)` |  |
| 23 | actionPriority | String | - | Yes | Action priority | `"Medium"` | High; Medium; Low |
| 24 | recommendedAction | String | - | No (null allowed) | Recommended action | `"Add groove edge vision check after machining"` |  |
| 25 | ownerUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 26 | ownerUserName | String | - | No (null allowed) | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 27 | targetDate | Date | Date | No (null allowed) | Target date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 28 | actionTaken | String | - | No (null allowed) | Action taken | `"Ejector pin polished and die coat thickness corrected"` |  |
| 29 | revisedSeverity | Int32 | - | No (null allowed) | Revised severity | `NumberInt(8)` |  |
| 30 | revisedOccurrence | Int32 | - | No (null allowed) | Revised occurrence | `NumberInt(3)` |  |
| 31 | revisedDetection | Int32 | - | No (null allowed) | Revised detection | `NumberInt(4)` |  |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ pfmeaId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ characteristicId: 1 }` | No | Look-up of lines by characteristic |
| 4 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_pfmeaLine.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_pfmeaLine.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_pfmeaLine.js
