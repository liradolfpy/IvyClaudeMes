# u_mes_perf_leakTestResultStage

| Property | Value |
|---|---|
| Module | PerformanceManagement (perf) |
| Purpose | One document per stage of a leak test result |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_perf_leakTestResult |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 25 (25 required, 0 may be null) |

## Structure

Child collection. The parent leak test result can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. leakTestResultId and leakTestResultName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1215000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LKT-2026-000377-S01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | leakTestResultId | String | - | Yes | Reference to u_mes_perf_leakTestResult._id: the parent document this one belongs to | `"1214000000000001"` | Reference: u_mes_perf_leakTestResult._id |
| 7 | leakTestResultName | String | - | Yes | Display value of leakTestResultId, copied from u_mes_perf_leakTestResult.recordNo | `"LKT-2026-000377"` |  |
| 8 | stageNo | Int32 | - | Yes | Stage number | `NumberInt(1)` |  |
| 9 | stageName | String | - | Yes | Stage name | `"Low Pressure"` | Low Pressure; High Pressure; Gross Leak; Fine Leak |
| 10 | testPressureBar | Decimal128 | - | Yes | Test pressure (bar) | `5.0` |  |
| 11 | fillTimeSec | Decimal128 | - | Yes | Fill time (seconds) | `2.0` |  |
| 12 | stabiliseTimeSec | Decimal128 | - | Yes | Stabilise time (seconds) | `3.0` |  |
| 13 | testTimeSec | Decimal128 | - | Yes | Test time (seconds) | `4.0` |  |
| 14 | pressureDropPa | Decimal128 | - | Yes | Pressure drop (pascal) | `8.0` |  |
| 15 | leakRateSccm | Decimal128 | - | Yes | Leak rate (standard cubic centimetres per minute) | `0.09` |  |
| 16 | limitPressureDropPa | Decimal128 | - | Yes | Limit pressure drop (pascal) | `30.0` |  |
| 17 | limitLeakRateSccm | Decimal128 | - | Yes | Limit leak rate (standard cubic centimetres per minute) | `0.30` |  |
| 18 | stageResult | String | - | Yes | Stage result | `"Pass"` | Pass; Fail |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 20 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:14:03.000+0000")` |  |
| 21 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 22 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 23 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:14:03.000+0000")` |  |
| 24 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 25 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ leakTestResultId: 1, stageNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/07_performance_management/validators/u_mes_perf_leakTestResultStage.json
- Indexes: 03_design/07_performance_management/indexes/u_mes_perf_leakTestResultStage.js
- Sample documents (10): 03_design/07_performance_management/samples/u_mes_perf_leakTestResultStage.js
