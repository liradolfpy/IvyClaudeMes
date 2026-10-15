# u_mes_qual_capaImplementationAction

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | One document per implementation action of a CAPA |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_capa |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (17 required, 3 may be null) |

## Structure

Child collection. The parent CAPA can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. capaId and capaName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1181000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CAPA-2026-0014-IA01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | capaId | String | - | Yes | Reference to u_mes_qual_capa._id: the parent document this one belongs to | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 7 | capaName | String | - | Yes | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | description | String | - | Yes | Description of the CAPA implementation action | `"Ejector pin polished and die coat thickness corrected; effectiveness verified over the next 2,000 pieces"` |  |
| 10 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 11 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 12 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 13 | effective | Boolean | - | Yes | True when: effective | `true` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 16 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 18 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 19 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ capaId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capaImplementationAction.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capaImplementationAction.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_capaImplementationAction.js
