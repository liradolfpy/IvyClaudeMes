# u_mes_matl_shipment

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Dispatch to customer: invoice / ASN, vehicle, containers shipped, proof of delivery |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | SHP-<recordNo> |
| Display value used by references | recordNo |
| Keys | 39 (30 required, 9 may be null) |
| Estimated volume per year | ~3,500 |
| Storage | standard |

## Structure

Flat entity collection: one document per shipment, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with shipmentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_shipmentLine | Child | line |
| u_mes_matl_shipmentLineContainer | Relationship | (below u_mes_matl_shipmentLine) container |
| u_mes_matl_shipmentLineLot | Relationship | (below u_mes_matl_shipmentLine) lot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SHP-<recordNo> | `"SHP-2026-000377"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000377"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerId | String | Yes | Reference to u_mes_mast_customer._id | `"CUS-SML"` | Reference: u_mes_mast_customer._id |
| 6 | customerName | String | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 7 | shipToCode | String | Yes | Ship to code | `"SML-TLG-D4"` |  |
| 8 | customerScheduleId | String | No (null allowed) | Reference to u_mes_plan_customerSchedule._id | `"CSR-SML-DS-2026-40"` | Reference: u_mes_plan_customerSchedule._id |
| 9 | customerScheduleName | String | No (null allowed) | Display value of customerScheduleId, copied from u_mes_plan_customerSchedule.recordNo | `"SML-DS-2026-40"` |  |
| 10 | invoiceNo | String | Yes | Invoice number | `"VBS/26-27/004128"` |  |
| 11 | invoiceDate | Date | Yes | Invoice date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 12 | asnNo | String | No (null allowed) | ASN number | `"ASN-260930-0071"` |  |
| 13 | asnSentAt | Date | No (null allowed) | Asn sent date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 14 | eWayBillNo | String | Yes | E way bill number | `"271004417732"` |  |
| 15 | transporterId | String | Yes | Reference to u_mes_mast_transporter._id | `"TRP-DRC"` | Reference: u_mes_mast_transporter._id |
| 16 | transporterName | String | Yes | Display value of transporterId, copied from u_mes_mast_transporter.name | `"Deccan Road Carriers"` |  |
| 17 | vehicleNo | String | Yes | Vehicle number | `"MH14 GT 4471"` |  |
| 18 | driverName | String | Yes | Driver name | `"Ganesh More"` |  |
| 19 | lrNo | String | Yes | Lorry receipt number | `"DRC-771204"` |  |
| 20 | totalQuantity | Int32 | Yes | Total quantity | `NumberInt(480)` |  |
| 21 | totalContainers | Int32 | Yes | Total containers | `NumberInt(20)` |  |
| 22 | grossWeightKg | Decimal128 | Yes | Gross weight (kg) | `NumberDecimal("3.480")` |  |
| 23 | invoiceValueInr | Decimal128 | Yes | Invoice value (Indian rupees) | `NumberDecimal("1322880.00")` |  |
| 24 | dockLocationId | String | No (null allowed) | Reference to u_mes_matl_storageLocation._id: dock location | `"LOC-LS-ASY-01"` | Reference: u_mes_matl_storageLocation._id |
| 25 | dockLocationName | String | No (null allowed) | Display value of dockLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 26 | loadedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'loaded' | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 27 | loadedBy | String | Yes | Display name of the user in loadedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 28 | plannedDispatchAt | Date | Yes | Planned dispatch date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 29 | dispatchedAt | Date | No (null allowed) | Date and time when the record was dispatched | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 30 | deliveredAt | Date | No (null allowed) | Date and time when the record was delivered | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 31 | podReceivedAt | Date | No (null allowed) | Pod received date and time | `ISODate("2026-09-29T05:20:00.000+0000")` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Delivered"` | Planned; Loading; Dispatched; Delivered; Cancelled |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 35 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 37 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 38 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Planned, Loading, Dispatched, Delivered, Cancelled. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ customerScheduleId: 1 }` | No | Look-up of documents by customer schedule |
| 5 | `{ transporterId: 1 }` | No | Look-up of documents by transporter |
| 6 | `{ dockLocationId: 1 }` | No | Look-up of documents by dock location |
| 7 | `{ siteId: 1, invoiceDate: -1 }` | No | Time-ordered lists and reports by invoice date |

## Referenced by

u_mes_plan_container, u_mes_matl_materialMovement, u_mes_matl_label, u_mes_matl_shipmentLine, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecord, u_mes_qual_customerComplaintShipment, u_mes_syst_erpMessage.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_shipment.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_shipment.js
- Sample document: 03_design/04_material_management/samples/u_mes_matl_shipment.js
