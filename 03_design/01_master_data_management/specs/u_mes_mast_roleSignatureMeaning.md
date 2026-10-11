# u_mes_mast_roleSignatureMeaning

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Links one role to one signature meaning; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_role |
| _id pattern | <roleId>-SM<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A role can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. roleId and roleName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <roleId>-SM<nnn> | `"ROLE-OPERATOR-SM001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"OPERATOR-SM001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | roleId | String | Yes | Reference to u_mes_mast_role._id: the parent document this one belongs to | `"ROLE-OPERATOR"` | Reference: u_mes_mast_role._id |
| 6 | roleName | String | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | signatureMeaningId | String | Yes | Reference to u_mes_mast_signatureMeaning._id | `"SGM-APPROVED"` | Reference: u_mes_mast_signatureMeaning._id |
| 9 | signatureMeaningName | String | Yes | Display value of signatureMeaningId, copied from u_mes_mast_signatureMeaning.name | `"Approved"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ roleId: 1, signatureMeaningId: 1 }` | Yes | One link per pair |
| 2 | `{ signatureMeaningId: 1, roleId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_roleSignatureMeaning.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_roleSignatureMeaning.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_roleSignatureMeaning.js
