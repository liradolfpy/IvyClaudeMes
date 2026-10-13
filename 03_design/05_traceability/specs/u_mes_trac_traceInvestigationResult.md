# u_mes_trac_traceInvestigationResult

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | One document per result of a trace investigation |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_trac_traceInvestigation |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 29 (23 required, 6 may be null) |

## Structure

Child collection. The parent trace investigation can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. traceInvestigationId and traceInvestigationName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1315000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"TRC-20260919-011-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | traceInvestigationId | String | - | Yes | Reference to u_mes_trac_traceInvestigation._id: the parent document this one belongs to | `"1314000000000001"` | Reference: u_mes_trac_traceInvestigation._id |
| 7 | traceInvestigationName | String | - | Yes | Display value of traceInvestigationId, copied from u_mes_trac_traceInvestigation.title | `"Forward trace, seal lot L260905-SEL-011 after seal cut at assembly"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_wipUnit"` | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| 10 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1094000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | Yes | Display value of the related document | `"U260915A0184"` |  |
| 12 | genealogyDepth | Int32 | - | Yes | Genealogy distance from the start object (1 = direct parent or child) | `NumberInt(1)` |  |
| 13 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 15 | statusAtRun | String | - | Yes | Status of the object at the time of the run | `"On Hold"` |  |
| 16 | storageLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id | `"1112000000000007"` | Reference: u_mes_matl_storageLocation._id |
| 17 | storageLocationName | String | - | No (null allowed) | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Quarantine cage, quality"` |  |
| 18 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 19 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 20 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `null` | Reference: u_mes_mast_customer._id |
| 21 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `null` |  |
| 22 | quantity | Decimal128 | - | Yes | Quantity concerned | `NumberDecimal("1")` |  |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 24 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:28:40.000+0000")` |  |
| 25 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 26 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 27 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T23:28:40.000+0000")` |  |
| 28 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ traceInvestigationId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |
| 3 | `{ storageLocationId: 1 }` | No | Look-up of lines by storage location |
| 4 | `{ shipmentId: 1 }` | No | Look-up of lines by shipment |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_traceInvestigationResult.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_traceInvestigationResult.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_traceInvestigationResult.js
