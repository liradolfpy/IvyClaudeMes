# u_mes_mmr_masterManufacturingRecord

| Property | Value |
|---|---|
| Module | Master Manufacturing Record (mmr) |
| Purpose | One approved, versioned master manufacturing record per item revision: the bill of material, routing, bill of process, recipes, control plan, inspection plan, packaging specification and label template that together define how a batch is made, with standard batch size, theoretical yield, yield limits, effective dates and approvals. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 53 (28 required, 25 may be null) |
| Estimated volume per year | about 40 versions per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per master manufacturing record, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with masterManufacturingRecordId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mmr_masterManufacturingRecordRecipe | Relationship | recipe |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1367000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MMR-5110-10-0100-03"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title of the master record | `"Front brake caliper assembly LH, master manufacturing record version 3"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevisionId | String | - | Yes | Reference to u_mes_prod_itemRevision._id | `"1044000000000002"` | Reference: u_mes_prod_itemRevision._id |
| 9 | itemRevisionName | String | - | Yes | Display value of itemRevisionId, copied from u_mes_prod_itemRevision.recordNo | `"5110-10-0100-R02"` |  |
| 10 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 12 | version | Int32 | - | Yes | Version of the master record | `NumberInt(3)` |  |
| 13 | previousMasterManufacturingRecordId | String | - | No (null allowed) | Reference to u_mes_mmr_masterManufacturingRecord._id: previous master manufacturing record | `"1367000000000002"` | Reference: u_mes_mmr_masterManufacturingRecord._id |
| 14 | previousMasterManufacturingRecordName | String | - | No (null allowed) | Display value of previousMasterManufacturingRecordId, copied from u_mes_mmr_masterManufacturingRecord.title | `"Front brake caliper assembly LH, master manufacturing record version 2"` |  |
| 15 | billOfMaterialId | String | - | Yes | Reference to u_mes_prod_billOfMaterial._id | `"1047000000000009"` | Reference: u_mes_prod_billOfMaterial._id |
| 16 | billOfMaterialName | String | - | Yes | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-5110-10-0100-03"` |  |
| 17 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 18 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 19 | billOfProcessId | String | - | Yes | Reference to u_mes_prod_billOfProcess._id | `"1057000000000001"` | Reference: u_mes_prod_billOfProcess._id |
| 20 | billOfProcessName | String | - | Yes | Display value of billOfProcessId, copied from u_mes_prod_billOfProcess.recordNo | `"BOP-5110-10-0100-R01"` |  |
| 21 | controlPlanId | String | - | Yes | Reference to u_mes_qual_controlPlan._id | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 22 | controlPlanName | String | - | Yes | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 23 | inspectionPlanId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"1142000000000010"` | Reference: u_mes_qual_inspectionPlan._id |
| 24 | inspectionPlanName | String | - | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, final inspection"` |  |
| 25 | packagingSpecificationId | String | - | No (null allowed) | Reference to u_mes_matl_packagingSpecification._id | `"1122000000000005"` | Reference: u_mes_matl_packagingSpecification._id |
| 26 | packagingSpecificationName | String | - | No (null allowed) | Display value of packagingSpecificationId, copied from u_mes_matl_packagingSpecification.recordNo | `"PKS-5110-10-0100-SML-03"` |  |
| 27 | labelTemplateId | String | - | No (null allowed) | Reference to u_mes_matl_labelTemplate._id | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 28 | labelTemplateName | String | - | No (null allowed) | Display value of labelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 29 | processValidationId | String | - | No (null allowed) | Reference to u_mes_qual_processValidation._id | `"1365000000000001"` | Reference: u_mes_qual_processValidation._id |
| 30 | processValidationName | String | - | No (null allowed) | Display value of processValidationId, copied from u_mes_qual_processValidation.title | `"Front caliper LH, assembly line 1, process qualification"` |  |
| 31 | controlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id | `"1246000000000010"` | Reference: u_mes_syst_controlledDocument._id |
| 32 | controlledDocumentName | String | - | No (null allowed) | Display value of controlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 33 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000001"` | Reference: u_mes_prod_engineeringChange._id |
| 34 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 35 | changeReasonText | String | - | No (null allowed) | Reason for the change from the previous version | `"Bleed screw torque window revised to 14 +/- 2 N.m with angle monitoring (ECN-2026-0027)"` |  |
| 36 | standardBatchSize | Int32 | - | Yes | Standard batch size in pieces | `NumberInt(480)` |  |
| 37 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 38 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 39 | theoreticalQuantity | Decimal128 | - | Yes | Theoretical output of a standard batch | `NumberDecimal("480")` |  |
| 40 | lowerLimitPct | Decimal128 | - | Yes | Lower yield limit (percent) | `NumberDecimal("98.00")` |  |
| 41 | upperLimitPct | Decimal128 | - | Yes | Upper yield limit (percent) | `NumberDecimal("100.00")` |  |
| 42 | effectiveFrom | Date | Date | No (null allowed) | First day the version may be used; null while in preparation | `ISODate("2026-05-25T00:00:00.000+0000")` |  |
| 43 | effectiveTo | Date | Date | No (null allowed) | Last day the version may be used; null while effective | `null` |  |
| 44 | authoredById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'authored' | `"1029000000000009"` | Reference: u_mes_mast_user._id |
| 45 | authoredBy | String | - | Yes | Display name of the user in authoredById, copied from u_mes_mast_user.fullName | `"Sneha Joshi"` |  |
| 46 | reviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 47 | reviewedBy | String | - | No (null allowed) | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 48 | reviewedAt | Date | Datetime | No (null allowed) | Review time | `ISODate("2026-05-22T15:00:00.000+0000")` |  |
| 49 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 50 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 51 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-05-23T11:00:00.000+0000")` |  |
| 52 | status | String | - | Yes | Primary lifecycle state of the document | `"Effective"` | In Preparation; In Review; Approved; Effective; Superseded |
| 53 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, In Review, Approved, Effective, Superseded. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ itemRevisionId: 1 }` | No | Look-up of documents by item revision |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ previousMasterManufacturingRecordId: 1 }` | No | Look-up of documents by previous master manufacturing record |
| 7 | `{ billOfMaterialId: 1 }` | No | Look-up of documents by bill of material |

## Referenced by

u_mes_mmr_masterManufacturingRecord, u_mes_mmr_masterManufacturingRecordRecipe, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/12_master_manufacturing_record/validators/u_mes_mmr_masterManufacturingRecord.json
- Indexes: 03_design/12_master_manufacturing_record/indexes/u_mes_mmr_masterManufacturingRecord.js
- Sample documents (10): 03_design/12_master_manufacturing_record/samples/u_mes_mmr_masterManufacturingRecord.js
