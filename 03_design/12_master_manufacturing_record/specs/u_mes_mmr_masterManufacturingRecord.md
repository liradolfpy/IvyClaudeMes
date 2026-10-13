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
| Keys | 54 (29 required, 25 may be null) |
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
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MMR-PCM500-B10-03"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the master record | `"Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 3"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000011"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Paracetamol Tablets IP 500 mg, blister 10 x 10"` |  |
| 9 | itemRevisionId | String | - | Yes | Reference to u_mes_prod_itemRevision._id | `"1044000000000012"` | Reference: u_mes_prod_itemRevision._id |
| 10 | itemRevisionName | String | - | Yes | Display value of itemRevisionId, copied from u_mes_prod_itemRevision.recordNo | `"FG-PCM500-B10-R02"` |  |
| 11 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000011"` | Reference: u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Paracetamol 500 mg 10 x 10 blister, domestic"` |  |
| 13 | version | Int32 | - | Yes | Version of the master record | `NumberInt(3)` |  |
| 14 | previousMasterManufacturingRecordId | String | - | No (null allowed) | Reference to u_mes_mmr_masterManufacturingRecord._id: previous master manufacturing record | `"1367000000000002"` | Reference: u_mes_mmr_masterManufacturingRecord._id |
| 15 | previousMasterManufacturingRecordName | String | - | No (null allowed) | Display value of previousMasterManufacturingRecordId, copied from u_mes_mmr_masterManufacturingRecord.title | `"Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 2"` |  |
| 16 | billOfMaterialId | String | - | Yes | Reference to u_mes_prod_billOfMaterial._id | `"1047000000000019"` | Reference: u_mes_prod_billOfMaterial._id |
| 17 | billOfMaterialName | String | - | Yes | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-FG-PCM500-B10-03"` |  |
| 18 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000011"` | Reference: u_mes_prod_routing._id |
| 19 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Paracetamol 500 mg blister, full process routing"` |  |
| 20 | billOfProcessId | String | - | Yes | Reference to u_mes_prod_billOfProcess._id | `"1057000000000011"` | Reference: u_mes_prod_billOfProcess._id |
| 21 | billOfProcessName | String | - | Yes | Display value of billOfProcessId, copied from u_mes_prod_billOfProcess.recordNo | `"BOP-FG-PCM500-B10-R01"` |  |
| 22 | controlPlanId | String | - | Yes | Reference to u_mes_qual_controlPlan._id | `"1139000000000011"` | Reference: u_mes_qual_controlPlan._id |
| 23 | controlPlanName | String | - | Yes | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-FG-PCM500-B10-PROD"` |  |
| 24 | inspectionPlanId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"1142000000000020"` | Reference: u_mes_qual_inspectionPlan._id |
| 25 | inspectionPlanName | String | - | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, cartoning and final inspection"` |  |
| 26 | packagingSpecificationId | String | - | No (null allowed) | Reference to u_mes_matl_packagingSpecification._id | `"1122000000000015"` | Reference: u_mes_matl_packagingSpecification._id |
| 27 | packagingSpecificationName | String | - | No (null allowed) | Display value of packagingSpecificationId, copied from u_mes_matl_packagingSpecification.recordNo | `"PKS-FG-PCM500-B10-MCH-03"` |  |
| 28 | labelTemplateId | String | - | No (null allowed) | Reference to u_mes_matl_labelTemplate._id | `"1124000000000011"` | Reference: u_mes_matl_labelTemplate._id |
| 29 | labelTemplateName | String | - | No (null allowed) | Display value of labelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Medicura Healthcare shipper label A5"` |  |
| 30 | processValidationId | String | - | No (null allowed) | Reference to u_mes_qual_processValidation._id | `"1365000000000001"` | Reference: u_mes_qual_processValidation._id |
| 31 | processValidationName | String | - | No (null allowed) | Display value of processValidationId, copied from u_mes_qual_processValidation.title | `"Paracetamol 500 mg tablets, process performance qualification, three batches"` |  |
| 32 | controlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id | `"1246000000000020"` | Reference: u_mes_syst_controlledDocument._id |
| 33 | controlledDocumentName | String | - | No (null allowed) | Display value of controlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"SOP dispensing of raw materials SOP-WH-007 revision 9"` |  |
| 34 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000014"` | Reference: u_mes_prod_engineeringChange._id |
| 35 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Blister foil supplier changed"` |  |
| 36 | changeReasonText | String | - | No (null allowed) | Reason for the change from the previous version | `"Blister foil supplier changed and leak test program revised (ECN-2026-0030)"` |  |
| 37 | standardBatchSize | Int32 | - | Yes | Standard batch size in pieces | `NumberInt(4800)` |  |
| 38 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000011"` | Reference: u_mes_mast_unitOfMeasure._id |
| 39 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 40 | theoreticalQuantity | Decimal128 | - | Yes | Theoretical output of a standard batch | `NumberDecimal("4800")` |  |
| 41 | lowerLimitPct | Decimal128 | - | Yes | Lower yield limit (percent) | `NumberDecimal("98.00")` |  |
| 42 | upperLimitPct | Decimal128 | - | Yes | Upper yield limit (percent) | `NumberDecimal("100.00")` |  |
| 43 | effectiveFrom | Date | Date | No (null allowed) | First day the version may be used; null while in preparation | `ISODate("2026-05-25T00:00:00.000+0000")` |  |
| 44 | effectiveTo | Date | Date | No (null allowed) | Last day the version may be used; null while effective | `null` |  |
| 45 | authoredById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'authored' | `"1029000000000019"` | Reference: u_mes_mast_user._id |
| 46 | authoredBy | String | - | Yes | Display name of the user in authoredById, copied from u_mes_mast_user.fullName | `"Tejas Bapat"` |  |
| 47 | reviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'reviewed' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 48 | reviewedBy | String | - | No (null allowed) | Display name of the user in reviewedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 49 | reviewedAt | Date | Datetime | No (null allowed) | Review time | `ISODate("2026-05-22T15:00:00.000+0000")` |  |
| 50 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000017"` | Reference: u_mes_mast_user._id |
| 51 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Vandana Iyer"` |  |
| 52 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-05-23T11:00:00.000+0000")` |  |
| 53 | status | String | - | Yes | Primary lifecycle state of the document | `"Effective"` | In Preparation; In Review; Approved; Effective; Superseded |
| 54 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
