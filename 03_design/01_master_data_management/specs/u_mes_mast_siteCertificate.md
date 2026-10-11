# u_mes_mast_siteCertificate

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per certificate of a site |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_site |
| _id pattern | <siteId>-C<nnn> |
| Display value used by references | recordNo |
| Keys | 12 (11 required, 1 may be null) |

## Structure

Child collection. The parent site can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. siteId and siteName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <siteId>-C<nnn> | `"SITE-PN1-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 6 | standard | String | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 7 | certificateNo | String | Yes | Certificate number | `"IATF-0412877"` |  |
| 8 | issuedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'issued' | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 9 | issuedBy | String | Yes | Display name of the user in issuedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 10 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 11 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_siteCertificate.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_siteCertificate.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_siteCertificate.js
