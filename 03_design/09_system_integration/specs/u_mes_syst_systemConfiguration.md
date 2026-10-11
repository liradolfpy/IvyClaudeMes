# u_mes_syst_systemConfiguration

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Site and module settings (OEE basis, SPC rules, retention, label printer mapping) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CFG-<recordNo> |
| Display value used by references | description |
| Keys | 18 (14 required, 4 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per system configuration, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CFG-<recordNo> | `"CFG-oee.plannedTimeBasis"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"oee.plannedTimeBasis"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | module | String | Yes | Module of the system configuration | `"Performance"` | Master Data; Product Definition; Execution; Materials; Traceability; Quality; Performance; Maintenance; Integration; Safety |
| 6 | description | String | Yes | Description of the system configuration | `"Time basis used as the denominator of availability"` |  |
| 7 | valueType | String | Yes | Value type | `"Text"` | Text; Number; Flag; JSON |
| 8 | configValueText | String | No (null allowed) | Config value text | `"Planned Production Time"` |  |
| 9 | configValueNumber | Decimal128 | No (null allowed) | Config value number | `null` |  |
| 10 | configValueFlag | Boolean | Yes | True when: config value flag | `false` |  |
| 11 | configValueJson | String | No (null allowed) | Config value json | `null` |  |
| 12 | scope | String | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 13 | isEditable | Boolean | Yes | True when the record is editable | `true` |  |
| 14 | isSecret | Boolean | Yes | True when the record is secret | `false` |  |
| 15 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 16 | lastChangedReason | String | No (null allowed) | Last changed reason | `"Aligned with corporate OEE definition"` |  |
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

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_systemConfiguration.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_systemConfiguration.js
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_systemConfiguration.js
