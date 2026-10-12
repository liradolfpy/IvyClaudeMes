# u_mes_syst_savedView

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Saved dashboard and comparison filters per user or role. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 16 (13 required, 3 may be null) |
| Estimated volume per year | about 500 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per saved view, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1341000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"VIEW-10045-001"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | View name | `"OEE by shift, assembly line 1, last 7 days"` |  |
| 6 | viewType | String | - | Yes | View type | `"Comparison"` | Dashboard; Comparison; Pareto; Trend; List |
| 7 | collectionName | String | - | Yes | Main collection queried | `"u_mes_perf_oeeRecord"` |  |
| 8 | filterJson | String | - | Yes | Filter as JSON text | `"{\"lineName\":\"Front Caliper Assembly Line 1\",\"periodStartAt\":{\"$gte\":\"-7d\"}}"` |  |
| 9 | sortJson | String | - | No (null allowed) | Sort as JSON text | `"{\"oeePct\":-1}"` |  |
| 10 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 11 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 12 | roleId | String | - | No (null allowed) | Reference to u_mes_mast_role._id | `"1026000000000004"` | Reference: u_mes_mast_role._id |
| 13 | roleName | String | - | No (null allowed) | Display value of roleId, copied from u_mes_mast_role.name | `"Production Supervisor"` |  |
| 14 | isShared | Boolean | - | Yes | Visible to the role | `true` |  |
| 15 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ ownerUserId: 1 }` | No | Look-up of documents by owner user |
| 4 | `{ roleId: 1 }` | No | Look-up of documents by role |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_savedView.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_savedView.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_savedView.js
