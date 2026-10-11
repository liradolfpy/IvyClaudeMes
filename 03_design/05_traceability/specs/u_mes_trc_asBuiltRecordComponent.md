# u_mes_trc_asBuiltRecordComponent

| Property | Value |
|---|---|
| Module | Traceability (trc) |
| Purpose | One document per component of a as built record |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_trc_asBuiltRecord |
| _id pattern | <asBuiltRecordId>-C<nnn> |
| Display value used by references | recordNo |
| Keys | 22 (18 required, 4 may be null) |

## Structure

Child collection. The parent as built record can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. asBuiltRecordId and asBuiltRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <asBuiltRecordId>-C<nnn> | `"ABR-VB26272A00184-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"VB26272A00184-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | asBuiltRecordId | String | Yes | Reference to u_mes_trc_asBuiltRecord._id: the parent document this one belongs to | `"ABR-VB26272A00184"` | Reference: u_mes_trc_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | Yes | Display value of asBuiltRecordId, copied from u_mes_trc_asBuiltRecord.recordNo | `"VB26272A00184"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 11 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 12 | serialNo | String | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 13 | quantity | Int32 | Yes | Quantity of the as built record component | `NumberInt(1)` |  |
| 14 | genealogyLinkId | String | No (null allowed) | Reference to u_mes_trc_genealogyLink._id | `"GEN-20260929-000551"` | Reference: u_mes_trc_genealogyLink._id |
| 15 | genealogyLinkName | String | No (null allowed) | Display value of genealogyLinkId, copied from u_mes_trc_genealogyLink.recordNo | `"20260929-000551"` |  |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 19 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 20 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 21 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 22 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ asBuiltRecordId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |
| 3 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 4 | `{ genealogyLinkId: 1 }` | No | Look-up of lines by genealogy link |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trc_asBuiltRecordComponent.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trc_asBuiltRecordComponent.js
- Sample document: 03_design/05_traceability/samples/u_mes_trc_asBuiltRecordComponent.js
