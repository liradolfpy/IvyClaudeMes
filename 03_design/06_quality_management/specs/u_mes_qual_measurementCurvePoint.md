# u_mes_qual_measurementCurvePoint

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Points of a measurement curve. Created as a MongoDB time-series collection: timeField `sampledAt`, metaField `measurementCurveId`, granularity seconds. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (18 required, 0 may be null) |
| Estimated volume per year | about 300 million |
| Storage | time-series collection (timeField sampledAt, metaField measurementCurveId, granularity seconds) |

## Structure

Flat entity collection: one document per measurement curve point, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1320000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CRV-20260915-01840-0001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | measurementCurveId | String | - | Yes | Reference to u_mes_qual_measurementCurve._id | `"1319000000000001"` | Reference: u_mes_qual_measurementCurve._id |
| 7 | measurementCurveName | String | - | Yes | Display value of measurementCurveId, copied from u_mes_qual_measurementCurve.recordNo | `"CRV-20260915-01840"` |  |
| 8 | pointNo | Int32 | - | Yes | Point number | `NumberInt(1)` |  |
| 9 | sampledAt | Date | Datetime | Yes | Sample time | `ISODate("2026-09-15T06:01:30.000+0000")` |  |
| 10 | xValue | Decimal128 | - | Yes | X value | `NumberDecimal("0.0")` |  |
| 11 | yValue | Decimal128 | - | Yes | Y value | `NumberDecimal("0")` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 14 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 16 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:30.000+0000")` |  |
| 17 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ measurementCurveId: 1 }` | No | Look-up of documents by measurement curve |
| 3 | `{ siteId: 1, sampledAt: -1 }` | No | Time-ordered lists and reports by sampled at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_measurementCurvePoint.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_measurementCurvePoint.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_measurementCurvePoint.js
