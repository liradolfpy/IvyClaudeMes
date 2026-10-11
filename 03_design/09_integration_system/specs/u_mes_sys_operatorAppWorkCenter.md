# u_mes_sys_operatorAppWorkCenter

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | Links one operator app to one work center; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_sys_operatorApp |
| _id pattern | <operatorAppId>-WC<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A operator app can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. operatorAppId and operatorAppName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <operatorAppId>-WC<nnn> | `"APP-APP-TRQ-01-WC001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-TRQ-01-WC001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operatorAppId | String | Yes | Reference to u_mes_sys_operatorApp._id: the parent document this one belongs to | `"APP-APP-TRQ-01"` | Reference: u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String | Yes | Display value of operatorAppId, copied from u_mes_sys_operatorApp.name | `"Torque station operator app"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 9 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operatorAppId: 1, workCenterId: 1 }` | Yes | One link per pair |
| 2 | `{ workCenterId: 1, operatorAppId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_operatorAppWorkCenter.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_operatorAppWorkCenter.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_operatorAppWorkCenter.js
