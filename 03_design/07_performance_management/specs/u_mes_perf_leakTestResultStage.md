# u_mes_perf_leakTestResultStage

| Property | Value |
|---|---|
| Module | Performance Management (perf) |
| Purpose | One document per stage of a leak test result |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_perf_leakTestResult |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 24 (24 required, 0 may be null) |

## Structure

Child collection. The parent leak test result can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. leakTestResultId and leakTestResultName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1215000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LKT-2026-000377-S01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | leakTestResultId | String | - | Yes | Reference to u_mes_perf_leakTestResult._id: the parent document this one belongs to | `"1214000000000001"` | Reference: u_mes_perf_leakTestResult._id |
| 6 | leakTestResultName | String | - | Yes | Display value of leakTestResultId, copied from u_mes_perf_leakTestResult.recordNo | `"LKT-2026-000377"` |  |
| 7 | stageNo | Int32 | - | Yes | Stage number | `NumberInt(1)` |  |
| 8 | stageName | String | - | Yes | Stage name | `"Low Pressure"` | Low Pressure; High Pressure |
| 9 | testPressureBar | Decimal128 | - | Yes | Test pressure (bar) | `NumberDecimal("5.0")` |  |
| 10 | fillTimeSec | Decimal128 | - | Yes | Fill time (seconds) | `NumberDecimal("2.0")` |  |
| 11 | stabiliseTimeSec | Decimal128 | - | Yes | Stabilise time (seconds) | `NumberDecimal("3.0")` |  |
| 12 | testTimeSec | Decimal128 | - | Yes | Test time (seconds) | `NumberDecimal("4.0")` |  |
| 13 | pressureDropPa | Decimal128 | - | Yes | Pressure drop (pascal) | `NumberDecimal("8.0")` |  |
| 14 | leakRateSccm | Decimal128 | - | Yes | Leak rate (standard cubic centimetres per minute) | `NumberDecimal("0.09")` |  |
| 15 | limitPressureDropPa | Decimal128 | - | Yes | Limit pressure drop (pascal) | `NumberDecimal("30.0")` |  |
| 16 | limitLeakRateSccm | Decimal128 | - | Yes | Limit leak rate (standard cubic centimetres per minute) | `NumberDecimal("0.30")` |  |
| 17 | stageResult | String | - | Yes | Stage result | `"Pass"` | Pass; Fail |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:14:03.000+0000")` |  |
| 20 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 22 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T15:14:03.000+0000")` |  |
| 23 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

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
