# u_mes_qual_customerComplaint

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Customer complaints / line rejections / warranty returns with affected serials and PPM impact |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 43 (32 required, 11 may be null) |
| Estimated volume per year | ~80 |
| Storage | standard |

## Structure

Flat entity collection: one document per customer complaint, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with customerComplaintId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_customerComplaintSerialNumber | Relationship | serial number |
| u_mes_qual_customerComplaintShipment | Relationship | shipment |
| u_mes_qual_customerComplaintSuspectLot | Relationship | suspect lot |
| u_mes_qual_customerComplaintCommunication | Child | communication |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1198000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CMP-2026-0004"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 6 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 7 | customerRefNo | String | - | Yes | Customer ref number | `"SML-QN-2026-0932"` |  |
| 8 | complaintTypeId | String | - | Yes | Reference to u_mes_qual_complaintType._id | `"1285000000000001"` | Reference: u_mes_qual_complaintType._id |
| 9 | complaintTypeName | String | - | Yes | Display value of complaintTypeId, copied from u_mes_qual_complaintType.name | `"Line Rejection"` |  |
| 10 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 11 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 12 | description | String | - | Yes | Description of the customer complaint | `"Porosity opened at customer machining of mounting face"` |  |
| 13 | defectDescription | String | - | Yes | Defect description | `"Porosity visible on machined face or found by X-ray sampling"` |  |
| 14 | reportedAt | Date | Datetime | Yes | Date and time when the record was reported. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 15 | receivedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'received' | `null` | Reference: u_mes_mast_user._id |
| 16 | receivedBy | String | - | No (null allowed) | Display name of the user in receivedById, copied from u_mes_mast_user.fullName | `null` |  |
| 17 | occurredAt | Date | Datetime | Yes | Date and time when the record was occurred. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 18 | customerLocation | String | - | Yes | Customer location | `"Sahyadri Motors, Talegaon, Chassis Assembly Shop"` |  |
| 19 | quantityComplained | Int32 | - | Yes | Quantity complained | `NumberInt(3)` |  |
| 20 | quantityConfirmed | Int32 | - | Yes | Quantity confirmed | `NumberInt(3)` |  |
| 21 | vehicleModelId | String | - | No (null allowed) | Reference to u_mes_prod_vehicleModel._id | `"1276000000000001"` | Reference: u_mes_prod_vehicleModel._id |
| 22 | vehicleModelName | String | - | No (null allowed) | Display value of vehicleModelId, copied from u_mes_prod_vehicleModel.name | `"Sahyadri X42 Hatchback"` |  |
| 23 | mileageKm | Decimal128 | - | No (null allowed) | Mileage (km) | `null` |  |
| 24 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 25 | isSafetyRelated | Boolean | - | Yes | True when the record is safety related | `false` |  |
| 26 | containmentDueAt | Date | Datetime | Yes | Containment due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:40.000+0000")` |  |
| 27 | containmentSentAt | Date | Datetime | No (null allowed) | Containment sent date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 28 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 29 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 30 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 31 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 32 | debitNoteInr | Decimal128 | - | Yes | Debit note (Indian rupees) | `NumberDecimal("0.00")` |  |
| 33 | ppmImpact | Int32 | - | Yes | Ppm impact | `NumberInt(41)` |  |
| 34 | sortingCostInr | Decimal128 | - | Yes | Sorting cost (Indian rupees) | `NumberDecimal("14500.00")` |  |
| 35 | customerClosedAt | Date | Datetime | No (null allowed) | Customer closed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 36 | status | String | - | Yes | Primary lifecycle state of the document | `"Received"` | Received; Containment Sent; Under Analysis; Closed; Rejected |
| 37 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 38 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 39 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 40 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 41 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:40.000+0000")` |  |
| 42 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 43 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Received, Containment Sent, Under Analysis, Closed, Rejected. Initial state: Received. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ complaintTypeId: 1 }` | No | Look-up of documents by complaint type |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ vehicleModelId: 1 }` | No | Look-up of documents by vehicle model |
| 7 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 8 | `{ siteId: 1, reportedAt: -1 }` | No | Time-ordered lists and reports by reported at |

## Referenced by

u_mes_qual_capa, u_mes_qual_customerComplaintSerialNumber, u_mes_qual_customerComplaintShipment, u_mes_qual_customerComplaintSuspectLot, u_mes_qual_customerComplaintCommunication, u_mes_trac_traceInvestigation.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_customerComplaint.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_customerComplaint.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_customerComplaint.js
