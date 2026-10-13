# Field list - Master Manufacturing Record (mmr)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/12_master_manufacturing_record/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mmr_masterManufacturingRecord

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | itemRevisionId | String | - | u_mes_prod_itemRevision._id |
| 9 | itemRevisionName | String | - |  |
| 10 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - |  |
| 12 | version | Int32 | - |  |
| 13 | previousMasterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 14 | previousMasterManufacturingRecordName | String | - |  |
| 15 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 16 | billOfMaterialName | String | - |  |
| 17 | routingId | String | - | u_mes_prod_routing._id |
| 18 | routingName | String | - |  |
| 19 | billOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 20 | billOfProcessName | String | - |  |
| 21 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 22 | controlPlanName | String | - |  |
| 23 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 24 | inspectionPlanName | String | - |  |
| 25 | packagingSpecificationId | String | - | u_mes_matl_packagingSpecification._id |
| 26 | packagingSpecificationName | String | - |  |
| 27 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 28 | labelTemplateName | String | - |  |
| 29 | processValidationId | String | - | u_mes_qual_processValidation._id |
| 30 | processValidationName | String | - |  |
| 31 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 32 | controlledDocumentName | String | - |  |
| 33 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 34 | engineeringChangeName | String | - |  |
| 35 | changeReasonText | String | - |  |
| 36 | standardBatchSize | Int32 | - |  |
| 37 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 38 | unitOfMeasureName | String | - |  |
| 39 | theoreticalQuantity | Decimal128 | - |  |
| 40 | lowerLimitPct | Decimal128 | - |  |
| 41 | upperLimitPct | Decimal128 | - |  |
| 42 | effectiveFrom | Date | Date |  |
| 43 | effectiveTo | Date | Date |  |
| 44 | authoredById | String | - | u_mes_mast_user._id |
| 45 | authoredBy | String | - |  |
| 46 | reviewedById | String | - | u_mes_mast_user._id |
| 47 | reviewedBy | String | - |  |
| 48 | reviewedAt | Date | Datetime |  |
| 49 | approvedById | String | - | u_mes_mast_user._id |
| 50 | approvedBy | String | - |  |
| 51 | approvedAt | Date | Datetime |  |
| 52 | status | String | - |  |
| 53 | schemaVersion | Int32 | - |  |

## u_mes_mmr_masterManufacturingRecordRecipe

Kind: relationship | Data class: master | Parent: u_mes_mmr_masterManufacturingRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | masterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 6 | masterManufacturingRecordName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | recipeId | String | - | u_mes_prod_recipe._id |
| 9 | recipeName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
