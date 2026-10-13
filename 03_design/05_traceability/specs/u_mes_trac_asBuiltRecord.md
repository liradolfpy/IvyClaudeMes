# u_mes_trac_asBuiltRecord

| Property | Value |
|---|---|
| Module | Traceability (trac) |
| Purpose | Device-history summary per shipped unit: components, key results, operators, sign-off (digital birth certificate) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 54 (29 required, 25 may be null) |
| Estimated volume per year | ~720,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per as built record, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with asBuiltRecordId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_trac_asBuiltRecordComponent | Child | component |
| u_mes_trac_asBuiltRecordOperation | Child | operation |
| u_mes_trac_asBuiltRecordInspectionResult | Relationship | inspection result |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1134000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ABR-VB26258A00184"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | wipUnitId | String | - | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 7 | wipUnitName | String | - | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 8 | serialNumberId | String | - | Yes | Reference to u_mes_trac_serialNumber._id | `"1131000000000001"` | Reference: u_mes_trac_serialNumber._id |
| 9 | serialNumberName | String | - | Yes | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258A00184"` |  |
| 10 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 11 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 12 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 13 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 14 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 15 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 17 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 18 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 19 | builtAt | Date | Datetime | Yes | Date and time when the record was built. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:50.000+0000")` |  |
| 20 | torqueTorqueResultId | String | - | No (null allowed) | Reference to u_mes_perf_torqueResult._id: torque torque result | `null` | Reference: u_mes_perf_torqueResult._id |
| 21 | torqueTorqueResultName | String | - | No (null allowed) | Display value of torqueTorqueResultId, copied from u_mes_perf_torqueResult.recordNo | `null` |  |
| 22 | torqueFinalTorqueNm | Decimal128 | - | No (null allowed) | Torque final torque (N.m) | `NumberDecimal("14.2")` |  |
| 23 | torqueFinalAngleDeg | Decimal128 | - | No (null allowed) | Torque final angle (degrees) | `NumberDecimal("38.5")` |  |
| 24 | leakTestLeakTestResultId | String | - | No (null allowed) | Reference to u_mes_perf_leakTestResult._id: leak test leak test result | `null` | Reference: u_mes_perf_leakTestResult._id |
| 25 | leakTestLeakTestResultName | String | - | No (null allowed) | Display value of leakTestLeakTestResultId, copied from u_mes_perf_leakTestResult.recordNo | `null` |  |
| 26 | leakTestVerdict | String | - | No (null allowed) | Leak test verdict | `"Pass"` | Pass; Fail |
| 27 | leakTestLeakRate | Decimal128 | - | No (null allowed) | Measured leak rate at the high-pressure stage (sccm) | `NumberDecimal("0.21")` |  |
| 28 | bodyLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: body lot | `"1096000000000004"` | Reference: u_mes_plan_lot._id |
| 29 | bodyLotName | String | - | No (null allowed) | Display value of bodyLotId, copied from u_mes_plan_lot.recordNo | `"L260917-ANO-001"` |  |
| 30 | castingLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: casting lot | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 31 | castingLotName | String | - | No (null allowed) | Display value of castingLotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 32 | heatTreatmentLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: heat treatment lot | `"1096000000000002"` | Reference: u_mes_plan_lot._id |
| 33 | heatTreatmentLotName | String | - | No (null allowed) | Display value of heatTreatmentLotId, copied from u_mes_plan_lot.recordNo | `"L260915-HT-002"` |  |
| 34 | reworkCount | Int32 | - | Yes | Rework count | `NumberInt(0)` |  |
| 35 | deviationPermitId | String | - | No (null allowed) | Reference to u_mes_qual_deviationPermit._id | `null` | Reference: u_mes_qual_deviationPermit._id |
| 36 | deviationPermitName | String | - | No (null allowed) | Display value of deviationPermitId, copied from u_mes_qual_deviationPermit.title | `null` |  |
| 37 | containerId | String | - | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 38 | containerName | String | - | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 39 | shipmentId | String | - | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 40 | shipmentName | String | - | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 41 | finalReleaseById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'final release' | `null` | Reference: u_mes_mast_user._id |
| 42 | finalReleaseBy | String | - | No (null allowed) | Display name of the user in finalReleaseById, copied from u_mes_mast_user.fullName | `null` |  |
| 43 | finalReleaseAt | Date | Datetime | No (null allowed) | Final release date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 44 | recordHash | String | - | Yes | SHA-256 hash of the frozen record | `"c41d7be29a630f5e8b7a12d4f09c33aa71e5d60b2f8c94a1d3e7b65f0a2c4d18"` |  |
| 45 | genealogyComplete | Boolean | - | Yes | True when every traceable BOM component is linked | `false` |  |
| 46 | missingComponentCount | Int32 | - | Yes | Number of traceable BOM components not linked | `NumberInt(1)` |  |
| 47 | status | String | - | Yes | Primary lifecycle state of the document | `"Compiling"` | Compiling; Released |
| 48 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 49 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:20.000+0000")` |  |
| 50 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 51 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 52 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:01:50.000+0000")` |  |
| 53 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 54 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Compiling, Released. Initial state: Compiling. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 4 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 7 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 8 | `{ siteId: 1, builtAt: -1 }` | No | Time-ordered lists and reports by built at |

## Referenced by

u_mes_trac_asBuiltRecordComponent, u_mes_trac_asBuiltRecordOperation, u_mes_trac_asBuiltRecordInspectionResult.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trac_asBuiltRecord.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trac_asBuiltRecord.js
- Sample documents (10): 03_design/05_traceability/samples/u_mes_trac_asBuiltRecord.js
