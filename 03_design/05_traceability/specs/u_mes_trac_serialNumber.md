# u_mes_trac_serialNumber

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | Registry of every serial / 2D code issued: status, mark grade, unit and shipment linkage |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 44 (20 required, 24 may be null) |
| Estimated volume per year | ~720,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per serial number, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1131000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"VB26258A00184"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 9 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 11 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 13 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 15 | numberRangeId | String | - | Yes | Reference to u_mes_syst_numberRange._id | `"1248000000000001"` | Reference: u_mes_syst_numberRange._id |
| 16 | numberRangeName | String | - | Yes | Display value of numberRangeId, copied from u_mes_syst_numberRange.name | `"Serial numbers, front caliper LH"` |  |
| 17 | dataMatrixPayload | String | - | Yes | Data matrix payload | `"SM-3501-0421-LH#VB26258A00184"` |  |
| 18 | issuedAt | Date | Datetime | Yes | Date and time when the record was issued. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:50.000+0000")` |  |
| 19 | markedAt | Date | Datetime | No (null allowed) | Date and time when the record was marked. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 20 | markedAtEquipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id: marked at equipment | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 21 | markedAtEquipmentName | String | - | No (null allowed) | Display value of markedAtEquipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 22 | markGrade | String | - | No (null allowed) | Mark grade | `null` | A; B; C; D; F |
| 23 | markVerifiedAt | Date | Datetime | No (null allowed) | Mark verified date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | labelId | String | - | No (null allowed) | Reference to u_mes_matl_label._id | `null` | Reference: u_mes_matl_label._id |
| 25 | labelName | String | - | No (null allowed) | Display value of labelId, copied from u_mes_matl_label.recordNo | `null` |  |
| 26 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 27 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 28 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 29 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 30 | shippedAt | Date | Datetime | No (null allowed) | Date and time when the record was shipped. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 31 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 32 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 33 | voidReason | String | - | No (null allowed) | Void reason | `null` |  |
| 34 | markingRecipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id: marking recipe | `null` | Reference: u_mes_prod_recipe._id |
| 35 | markingRecipeName | String | - | No (null allowed) | Display value of markingRecipeId, copied from u_mes_prod_recipe.name | `null` |  |
| 36 | markingRecipeVersion | String | - | No (null allowed) | Version of the marking program | `null` |  |
| 37 | status | String | - | Yes | Primary lifecycle state of the document | `"Issued"` | Reserved; Issued; Marked; Shipped; Voided; Scrapped |
| 38 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 39 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:20.000+0000")` |  |
| 40 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 41 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 42 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:50.000+0000")` |  |
| 43 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Reserved, Issued, Marked, Shipped, Voided, Scrapped. Initial state: Reserved. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 5 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ numberRangeId: 1 }` | No | Look-up of documents by number range |
| 8 | `{ siteId: 1, issuedAt: -1 }` | No | Time-ordered lists and reports by issued at |
| 9 | `{ dataMatrixPayload: 1 }` | Yes | A marked code is never issued twice |

## Referenced by

u_mes_plan_wipUnit, u_mes_trac_genealogyLink, u_mes_trac_asBuiltRecord, u_mes_qual_scrapRecord, u_mes_qual_customerComplaintSerialNumber, u_mes_qual_measurementCurve, u_mes_qual_defectRecord, u_mes_qual_retentionSample.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_serialNumber.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_serialNumber.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_serialNumber.js
