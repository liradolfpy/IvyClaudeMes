# u_mes_prd_engineeringChangeControlledDocument

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Links one engineering change to one controlled document; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_prd_engineeringChange |
| _id pattern | <engineeringChangeId>-CD<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A engineering change can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. engineeringChangeId and engineeringChangeName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <engineeringChangeId>-CD<nnn> | `"ECN-2026-0031-CD001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0031-CD001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | engineeringChangeId | String | Yes | Reference to u_mes_prd_engineeringChange._id: the parent document this one belongs to | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String | Yes | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | controlledDocumentId | String | Yes | Reference to u_mes_sys_controlledDocument._id | `"DOC-DRW-5110-10-0100-D"` | Reference: u_mes_sys_controlledDocument._id |
| 9 | controlledDocumentName | String | Yes | Display value of controlledDocumentId, copied from u_mes_sys_controlledDocument.title | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ engineeringChangeId: 1, controlledDocumentId: 1 }` | Yes | One link per pair |
| 2 | `{ controlledDocumentId: 1, engineeringChangeId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_engineeringChangeControlledDocument.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_engineeringChangeControlledDocument.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_engineeringChangeControlledDocument.js
