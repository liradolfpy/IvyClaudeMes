# u_mes_syst_controlledDocumentTag

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per tag value of a controlled document |
| Kind | Value list |
| Data class | Transaction |
| Parent collection | u_mes_syst_controlledDocument |
| _id pattern | <controlledDocumentId>-T<nnn> |
| Display value used by references | recordNo |
| Keys | 15 (15 required, 0 may be null) |

## Structure

Value-list collection. A controlled document can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. controlledDocumentId and controlledDocumentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <controlledDocumentId>-T<nnn> | `"DOC-DRW-5110-10-0100-D-T001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"DRW-5110-10-0100-D-T001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | controlledDocumentId | String | Yes | Reference to u_mes_syst_controlledDocument._id: the parent document this one belongs to | `"DOC-DRW-5110-10-0100-D"` | Reference: u_mes_syst_controlledDocument._id |
| 6 | controlledDocumentName | String | Yes | Display value of controlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | tag | String | Yes | Tag of the controlled document tag | `"caliper"` |  |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 10 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 11 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 12 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 13 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 15 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ controlledDocumentId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_controlledDocumentTag.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_controlledDocumentTag.js
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_controlledDocumentTag.js
