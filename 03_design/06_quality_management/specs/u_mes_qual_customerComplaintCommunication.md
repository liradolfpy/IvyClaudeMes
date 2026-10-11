# u_mes_qual_customerComplaintCommunication

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per communication of a customer complaint |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_customerComplaint |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent customer complaint can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. customerComplaintId and customerComplaintName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1202000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"CMP-2026-0004-C01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerComplaintId | String | Yes | Reference to u_mes_qual_customerComplaint._id: the parent document this one belongs to | `"1198000000000001"` | Reference: u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | Yes | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `"Porosity opened at customer machining of mounting face"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | communicatedAt | Date | Yes | Date and time when the record was communicated | `ISODate("2026-09-15T00:34:10.000+0000")` |  |
| 9 | direction | String | Yes | Direction of the customer complaint communication | `"Outbound"` | Inbound; Outbound |
| 10 | communicationSummary | String | Yes | Communication summary | `"Containment report with sorting result sent to customer SQA"` |  |
| 11 | authorUserId | String | Yes | Reference to u_mes_mast_user._id: author user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 12 | authorUserName | String | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:40.000+0000")` |  |
| 15 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 17 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:34:10.000+0000")` |  |
| 18 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ customerComplaintId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ authorUserId: 1 }` | No | Look-up of lines by author user |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_customerComplaintCommunication.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_customerComplaintCommunication.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_customerComplaintCommunication.js
