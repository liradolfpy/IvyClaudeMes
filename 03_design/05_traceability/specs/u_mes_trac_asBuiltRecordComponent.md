# u_mes_trac_asBuiltRecordComponent

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | One document per component of a as built record |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_trac_asBuiltRecord |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 22 (18 required, 4 may be null) |

## Structure

Child collection. The parent as built record can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. asBuiltRecordId and asBuiltRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1135000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ABR-VB26258A00184-C01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | asBuiltRecordId | String | - | Yes | Reference to u_mes_trac_asBuiltRecord._id: the parent document this one belongs to | `"1134000000000001"` | Reference: u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - | Yes | Display value of asBuiltRecordId, copied from u_mes_trac_asBuiltRecord.recordNo | `"ABR-VB26258A00184"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 12 | serialNo | String | - | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 13 | quantity | Int32 | - | Yes | Quantity of the as built record component | `NumberInt(1)` |  |
| 14 | genealogyLinkId | String | - | No (null allowed) | Reference to u_mes_trac_genealogyLink._id | `"1132000000000001"` | Reference: u_mes_trac_genealogyLink._id |
| 15 | genealogyLinkName | String | - | No (null allowed) | Display value of genealogyLinkId, copied from u_mes_trac_genealogyLink.recordNo | `"GEN-2026-000372"` |  |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 17 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:48.000+0000")` |  |
| 18 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 19 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 20 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:48.000+0000")` |  |
| 21 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 22 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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

- Validator: 03_design/05_traceability/validators/u_mes_trac_asBuiltRecordComponent.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_asBuiltRecordComponent.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_asBuiltRecordComponent.js
