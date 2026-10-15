# u_mes_syst_systemConfiguration

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Site and module settings (OEE basis, SPC rules, retention, label printer mapping) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 19 (15 required, 4 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per system configuration, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1249000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"oee.plannedTimeBasis"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | module | String | - | Yes | Module of the system configuration | `"Master Data"` | Master Data; ProductDefinition; Execution; Materials; Traceability; Quality; Performance; Maintenance; Integration; Safety |
| 7 | description | String | - | Yes | Description of the system configuration | `"Time basis used as the denominator of availability (oee.plannedTimeBasis)"` |  |
| 8 | valueType | String | - | Yes | Value type | `"Text"` | Text; Number; Flag; JSON |
| 9 | configValueText | String | - | No (null allowed) | Config value text | `"Planned Production Time"` |  |
| 10 | configValueNumber | Decimal128 | - | No (null allowed) | Config value number | `null` |  |
| 11 | configValueFlag | Boolean | - | Yes | True when: config value flag | `false` |  |
| 12 | configValueJson | String | - | No (null allowed) | Config value json | `null` |  |
| 13 | scope | String | - | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 14 | isEditable | Boolean | - | Yes | True when the record is editable | `true` |  |
| 15 | isSecret | Boolean | - | Yes | True when the record is secret | `false` |  |
| 16 | validFrom | Date | Date | Yes | Valid from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 17 | lastChangedReason | String | - | No (null allowed) | Last changed reason | `null` |  |
| 18 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_systemConfiguration.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_systemConfiguration.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_systemConfiguration.js
