# u_mes_qual_samplingPlan

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Sampling rules: AQL tables, skip-lot, time or counter based frequency |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 18 (12 required, 6 may be null) |
| Estimated volume per year | 20-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per sampling plan, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with samplingPlanId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_samplingPlanSizeRow | Child | size row |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1144000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"AQL-1.0-II"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the sampling plan; used as its display value in other collections | `"AQL 1.0, general inspection level II"` |  |
| 6 | samplingType | String | Yes | Sampling type | `"Attribute AQL"` | Attribute AQL; Fixed Sample; Hundred Percent; Skip Lot |
| 7 | standard | String | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 8 | inspectionLevel | String | Yes | Inspection level | `"S-1"` | S-1; S-2; S-3; S-4; I; II; III |
| 9 | aql | Decimal128 | No (null allowed) | Acceptance quality limit in percent | `NumberDecimal("1.0")` |  |
| 10 | frequencyType | String | Yes | Frequency type | `"Per Lot"` | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| 11 | frequencyEveryNUnits | Int32 | No (null allowed) | Frequency every nunits | `NumberInt(50)` |  |
| 12 | frequencyEveryMinutes | Int32 | No (null allowed) | Frequency every (minutes) | `NumberInt(120)` |  |
| 13 | skipLotEnabled | Boolean | Yes | True when: skip lot enabled | `false` |  |
| 14 | skipLotConsecutiveAcceptedToSkip | Int32 | No (null allowed) | Skip lot consecutive accepted to skip | `NumberInt(10)` |  |
| 15 | skipLotSkipFraction | Decimal128 | No (null allowed) | Skip lot skip fraction | `NumberDecimal("0.5")` |  |
| 16 | switchingRules | String | No (null allowed) | Switching rules | `"Tightened after 2 of 5 lots rejected; normal after 5 consecutive accepted"` |  |
| 17 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_qual_inspectionPlan, u_mes_qual_samplingPlanSizeRow.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_samplingPlan.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_samplingPlan.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_samplingPlan.js
