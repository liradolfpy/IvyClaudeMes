# u_mes_qual_productRecallLot

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per lot of a product recall |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_productRecall |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 20 (18 required, 2 may be null) |

## Structure

Child collection. The parent product recall can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. productRecallId and productRecallName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1364000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RCL-2026-001-L01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productRecallId | String | - | Yes | Reference to u_mes_qual_productRecall._id: the parent document this one belongs to | `"1363000000000001"` | Reference: u_mes_qual_productRecall._id |
| 6 | productRecallName | String | - | Yes | Display value of productRecallId, copied from u_mes_qual_productRecall.title | `"Containment of 12 calipers with unreadable 2D code at Sahyadri Motors Exports"` |  |
| 7 | lineNo | Int32 | - | Yes | Line number | `NumberInt(10)` |  |
| 8 | lotId | String | - | Yes | Reference to u_mes_plan_lot._id | `"1096000000000004"` | Reference: u_mes_plan_lot._id |
| 9 | lotName | String | - | Yes | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260917-ANO-001"` |  |
| 10 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `"1127000000000009"` | Reference: u_mes_matl_shipment._id |
| 11 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `"SHP-2026-000409"` |  |
| 12 | quantityShipped | Int32 | - | Yes | Quantity of the lot shipped | `NumberInt(12)` |  |
| 13 | quantityRecovered | Int32 | - | Yes | Quantity of the lot recovered | `NumberInt(12)` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 15 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T22:35:41.000+0000")` |  |
| 16 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 18 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T22:35:41.000+0000")` |  |
| 19 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ productRecallId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 3 | `{ shipmentId: 1 }` | No | Look-up of lines by shipment |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_productRecallLot.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_productRecallLot.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_productRecallLot.js
