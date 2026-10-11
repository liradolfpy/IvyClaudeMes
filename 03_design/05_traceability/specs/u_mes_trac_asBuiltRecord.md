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
| Keys | 51 (34 required, 17 may be null) |
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

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1134000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ABR-VB26258A00184"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | wipUnitId | String | Yes | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | Yes | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 7 | serialNumberId | String | Yes | Reference to u_mes_trac_serialNumber._id | `"1131000000000001"` | Reference: u_mes_trac_serialNumber._id |
| 8 | serialNumberName | String | Yes | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258A00184"` |  |
| 9 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 12 | productVariantId | String | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 13 | productVariantName | String | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 14 | productionOrderId | String | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 16 | customerId | String | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 17 | customerName | String | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 18 | builtAt | Date | Yes | Date and time when the record was built | `ISODate("2026-09-15T00:31:50.000+0000")` |  |
| 19 | torqueTorqueResultId | String | Yes | Reference to u_mes_perf_torqueResult._id: torque torque result | `"1213000000000001"` | Reference: u_mes_perf_torqueResult._id |
| 20 | torqueTorqueResultName | String | Yes | Display value of torqueTorqueResultId, copied from u_mes_perf_torqueResult.recordNo | `"TRQ-2026-000478"` |  |
| 21 | torqueFinalTorqueNm | Decimal128 | Yes | Torque final torque (N.m) | `NumberDecimal("14.2")` |  |
| 22 | torqueFinalAngleDeg | Decimal128 | Yes | Torque final angle (degrees) | `NumberDecimal("38.5")` |  |
| 23 | leakTestLeakTestResultId | String | Yes | Reference to u_mes_perf_leakTestResult._id: leak test leak test result | `"1214000000000001"` | Reference: u_mes_perf_leakTestResult._id |
| 24 | leakTestLeakTestResultName | String | Yes | Display value of leakTestLeakTestResultId, copied from u_mes_perf_leakTestResult.recordNo | `"LKT-2026-000377"` |  |
| 25 | leakTestVerdict | String | Yes | Leak test verdict | `"Pass"` | Pass; Fail |
| 26 | leakTestLeakRate | Decimal128 | Yes | Measured leak rate at the high-pressure stage (sccm) | `NumberDecimal("0.21")` |  |
| 27 | bodyLotId | String | No (null allowed) | Reference to u_mes_plan_lot._id: body lot | `"1096000000000004"` | Reference: u_mes_plan_lot._id |
| 28 | bodyLotName | String | No (null allowed) | Display value of bodyLotId, copied from u_mes_plan_lot.recordNo | `"L260917-ANO-001"` |  |
| 29 | castingLotId | String | No (null allowed) | Reference to u_mes_plan_lot._id: casting lot | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 30 | castingLotName | String | No (null allowed) | Display value of castingLotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 31 | heatTreatmentLotId | String | No (null allowed) | Reference to u_mes_plan_lot._id: heat treatment lot | `"1096000000000002"` | Reference: u_mes_plan_lot._id |
| 32 | heatTreatmentLotName | String | No (null allowed) | Display value of heatTreatmentLotId, copied from u_mes_plan_lot.recordNo | `"L260915-HT-002"` |  |
| 33 | reworkCount | Int32 | Yes | Rework count | `NumberInt(0)` |  |
| 34 | deviationPermitId | String | No (null allowed) | Reference to u_mes_qual_deviationPermit._id | `null` | Reference: u_mes_qual_deviationPermit._id |
| 35 | deviationPermitName | String | No (null allowed) | Display value of deviationPermitId, copied from u_mes_qual_deviationPermit.title | `null` |  |
| 36 | containerId | String | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 37 | containerName | String | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 38 | shipmentId | String | No (null allowed) | Reference to u_mes_matl_shipment._id | `null` | Reference: u_mes_matl_shipment._id |
| 39 | shipmentName | String | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `null` |  |
| 40 | finalReleaseById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'final release' | `null` | Reference: u_mes_mast_user._id |
| 41 | finalReleaseBy | String | No (null allowed) | Display name of the user in finalReleaseById, copied from u_mes_mast_user.fullName | `null` |  |
| 42 | finalReleaseAt | Date | No (null allowed) | Final release date and time | `null` |  |
| 43 | recordHash | String | Yes | SHA-256 hash of the frozen record | `"c41d7be29a630f5e8b7a12d4f09c33aa71e5d60b2f8c94a1d3e7b65f0a2c4d18"` |  |
| 44 | status | String | Yes | Primary lifecycle state of the document | `"Compiling"` | Compiling; Released |
| 45 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 46 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:31:20.000+0000")` |  |
| 47 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 48 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 49 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:31:50.000+0000")` |  |
| 50 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 51 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
