# u_mes_qual_capaCorrectiveAction

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per corrective action of a CAPA |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_capa |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent CAPA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. capaId and capaName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1180000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CAPA-2026-0014-CA201"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | capaId | String | - | Yes | Reference to u_mes_qual_capa._id: the parent document this one belongs to | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 7 | capaName | String | - | Yes | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | description | String | - | Yes | Description of the CAPA corrective action | `"Ejector pin polished and die coat thickness corrected"` |  |
| 10 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 11 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 12 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ capaId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capaCorrectiveAction.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capaCorrectiveAction.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_capaCorrectiveAction.js
