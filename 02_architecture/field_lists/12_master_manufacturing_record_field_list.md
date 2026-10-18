# Field list - MasterManufacturingRecord (mmr)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/12_master_manufacturing_record/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_mmr_masterManufacturingRecord

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | itemRevisionId | String | - | u_mes_prod_itemRevision._id |
| 10 | itemRevisionName | String | - |  |
| 11 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - |  |
| 13 | version | Int32 | - |  |
| 14 | previousMasterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 15 | previousMasterManufacturingRecordName | String | - |  |
| 16 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 17 | billOfMaterialName | String | - |  |
| 18 | routingId | String | - | u_mes_prod_routing._id |
| 19 | routingName | String | - |  |
| 20 | billOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 21 | billOfProcessName | String | - |  |
| 22 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 23 | controlPlanName | String | - |  |
| 24 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 25 | inspectionPlanName | String | - |  |
| 26 | packagingSpecificationId | String | - | u_mes_matl_packagingSpecification._id |
| 27 | packagingSpecificationName | String | - |  |
| 28 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 29 | labelTemplateName | String | - |  |
| 30 | processValidationId | String | - | u_mes_qual_processValidation._id |
| 31 | processValidationName | String | - |  |
| 32 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 33 | controlledDocumentName | String | - |  |
| 34 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 35 | engineeringChangeName | String | - |  |
| 36 | changeReasonText | String | - |  |
| 37 | standardBatchSize | Int32 | - |  |
| 38 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 39 | unitOfMeasureName | String | - |  |
| 40 | theoreticalQuantity | Decimal128 | - |  |
| 41 | lowerLimitPct | Decimal128 | - |  |
| 42 | upperLimitPct | Decimal128 | - |  |
| 43 | effectiveFrom | Date | Date |  |
| 44 | effectiveTo | Date | Date |  |
| 45 | authoredById | String | - | u_mes_mast_user._id |
| 46 | authoredBy | String | - |  |
| 47 | reviewedById | String | - | u_mes_mast_user._id |
| 48 | reviewedBy | String | - |  |
| 49 | reviewedAt | Date | Datetime |  |
| 50 | approvedById | String | - | u_mes_mast_user._id |
| 51 | approvedBy | String | - |  |
| 52 | approvedAt | Date | Datetime |  |
| 53 | status | String | - |  |
| 54 | schemaVersion | Int32 | - |  |

## u_mes_mmr_masterManufacturingRecordRecipe

Kind: relationship | Data class: master | Parent: u_mes_mmr_masterManufacturingRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | masterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 7 | masterManufacturingRecordName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | recipeId | String | - | u_mes_prod_recipe._id |
| 10 | recipeName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
