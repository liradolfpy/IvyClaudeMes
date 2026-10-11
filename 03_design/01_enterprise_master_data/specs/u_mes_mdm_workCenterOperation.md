# u_mes_mdm_workCenterOperation

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Links one work center to one operation; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mdm_workCenter |
| _id pattern | <workCenterId>-O<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A work center can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. workCenterId and workCenterName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workCenterId>-O<nnn> | `"WC-TRQ-01-O001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01-O001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id: the parent document this one belongs to | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 6 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workCenterId: 1, operationId: 1 }` | Yes | One link per pair |
| 2 | `{ operationId: 1, workCenterId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_workCenterOperation.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_workCenterOperation.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_workCenterOperation.js
