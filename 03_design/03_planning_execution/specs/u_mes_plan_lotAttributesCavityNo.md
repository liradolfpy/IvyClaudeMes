# u_mes_plan_lotAttributesCavityNo

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per attributes cavity number value of a lot |
| Kind | Value list |
| Data class | Transaction |
| Parent collection | u_mes_plan_lot |
| _id pattern | <lotId>-ACN<nnn> |
| Display value used by references | recordNo |
| Keys | 15 (15 required, 0 may be null) |

## Structure

Value-list collection. A lot can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. lotId and lotName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <lotId>-ACN<nnn> | `"LOT-L260928-GDC-014-ACN001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"L260928-GDC-014-ACN001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lotId | String | Yes | Reference to u_mes_plan_lot._id: the parent document this one belongs to | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 6 | lotName | String | Yes | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | attributesCavityNo | String | Yes | Attributes cavity number | `"1"` |  |
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
| 1 | `{ lotId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_lotAttributesCavityNo.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_lotAttributesCavityNo.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_lotAttributesCavityNo.js
