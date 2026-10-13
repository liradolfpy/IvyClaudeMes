# u_mes_matl_label

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Printed label instances with payload, printer, reprint count |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 42 (27 required, 15 may be null) |
| Estimated volume per year | ~1 million |
| Storage | standard |

## Structure

Flat entity collection: one document per label, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1126000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LBL-2026-000485"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | labelTemplateId | String | - | Yes | Reference to u_mes_matl_labelTemplate._id | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 7 | labelTemplateName | String | - | Yes | Display value of labelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 8 | labelType | String | - | Yes | Label type | `"Container Label"` | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| 9 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_container"` |  |
| 10 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1099000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 11 | relatedEntityName | String | - | Yes | Display value of the related document | `"TRL-00031"` |  |
| 12 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000009"` | Reference: u_mes_plan_wipUnit._id |
| 13 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260924A0288"` |  |
| 14 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `"1099000000000005"` | Reference: u_mes_plan_container._id |
| 15 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `"BIN-000099"` |  |
| 16 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 17 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 18 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `"1127000000000001"` | Reference: u_mes_matl_shipment._id |
| 19 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `"SHP-2026-000377"` |  |
| 20 | payload | String | - | Yes | Payload of the label | `"[)>06PSM-3501-0421-LHQ241TL260929-FG-002"` |  |
| 21 | humanReadable | String | - | Yes | Human readable | `"SM-3501-0421-LH  QTY 24  LOT L260929-FG-002"` |  |
| 22 | printerIotDeviceId | String | - | No (null allowed) | Reference to u_mes_syst_iotDevice._id: printer IoT device | `"1232000000000010"` | Reference: u_mes_syst_iotDevice._id |
| 23 | printerIotDeviceName | String | - | No (null allowed) | Display value of printerIotDeviceId, copied from u_mes_syst_iotDevice.name | `"Label printer, packing station"` |  |
| 24 | printedAt | Date | Datetime | Yes | Date and time when the record was printed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T08:35:46.000+0000")` |  |
| 25 | printedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'printed' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 26 | printedBy | String | - | Yes | Display name of the user in printedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 27 | copies | Int32 | - | Yes | Copies of the label | `NumberInt(1)` |  |
| 28 | reprintCount | Int32 | - | Yes | Reprint count | `NumberInt(0)` |  |
| 29 | reprintReason | String | - | No (null allowed) | Reprint reason | `null` |  |
| 30 | verified | Boolean | - | Yes | True when: verified | `false` |  |
| 31 | verificationGrade | String | - | No (null allowed) | ISO/IEC 15415 or 29158 overall symbol grade | `"A"` | A; B; C; D; F |
| 32 | voidedAt | Date | Datetime | No (null allowed) | Date and time when the record was voided. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 33 | voidedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'voided' | `null` | Reference: u_mes_mast_user._id |
| 34 | voidedBy | String | - | No (null allowed) | Display name of the user in voidedById, copied from u_mes_mast_user.fullName | `null` |  |
| 35 | status | String | - | Yes | Primary lifecycle state of the document | `"Printed"` | Printed; Verified; Reprinted; Voided |
| 36 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T08:35:16.000+0000")` |  |
| 38 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 39 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 40 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T08:35:46.000+0000")` |  |
| 41 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 42 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Printed, Verified, Reprinted, Voided. Initial state: Printed. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ labelTemplateId: 1 }` | No | Look-up of documents by label template |
| 4 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 5 | `{ containerId: 1 }` | No | Look-up of documents by container |
| 6 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 7 | `{ shipmentId: 1 }` | No | Look-up of documents by shipment |
| 8 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 9 | `{ siteId: 1, printedAt: -1 }` | No | Time-ordered lists and reports by printed at |

## Referenced by

u_mes_plan_container, u_mes_trac_serialNumber, u_mes_matl_dispenseRecord.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_label.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_label.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_label.js
