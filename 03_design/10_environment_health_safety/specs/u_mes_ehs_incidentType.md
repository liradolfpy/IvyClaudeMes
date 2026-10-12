# u_mes_ehs_incidentType

| Property | Value |
|---|---|
| Module | Environment Health and Safety (ehs) |
| Purpose | Types of safety incident |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per incident type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1293000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"NEAR-MISS"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the incident type; used as its display value in other collections | `"Near Miss"` |  |
| 6 | description | String | - | Yes | Description of the incident type | `"Near Miss (NEAR-MISS)"` |  |
| 7 | isInjury | Boolean | - | Yes | True when the record is injury | `false` |  |
| 8 | reportableToAuthority | Boolean | - | Yes | True when: reportable to authority | `false` |  |
| 9 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 10 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/10_environment_health_safety/validators/u_mes_ehs_incidentType.json
- Indexes: 03_design/10_environment_health_safety/indexes/u_mes_ehs_incidentType.js
- Sample documents (10): 03_design/10_environment_health_safety/samples/u_mes_ehs_incidentType.js
