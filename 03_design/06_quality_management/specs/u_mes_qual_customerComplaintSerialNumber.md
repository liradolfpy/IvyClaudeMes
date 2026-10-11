# u_mes_qual_customerComplaintSerialNumber

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one customer complaint to one serial number; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_qual_customerComplaint |
| _id pattern | <customerComplaintId>-SN<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A customer complaint can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. customerComplaintId and customerComplaintName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <customerComplaintId>-SN<nnn> | `"CMP-2026-0004-SN001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0004-SN001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerComplaintId | String | Yes | Reference to u_mes_qual_customerComplaint._id: the parent document this one belongs to | `"CMP-2026-0004"` | Reference: u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | Yes | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `"Bleed screw cap missing on three calipers at customer line"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | serialNumberId | String | Yes | Reference to u_mes_trac_serialNumber._id | `"SN-VB26272A00184"` | Reference: u_mes_trac_serialNumber._id |
| 9 | serialNumberName | String | Yes | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26272A00184"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerComplaintId: 1, serialNumberId: 1 }` | Yes | One link per pair |
| 2 | `{ serialNumberId: 1, customerComplaintId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_customerComplaintSerialNumber.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_customerComplaintSerialNumber.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_customerComplaintSerialNumber.js
