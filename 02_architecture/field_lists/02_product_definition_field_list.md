# Field list - Product Definition (prod)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/02_product_definition/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_prod_item

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | description | String | - |  |
| 6 | itemType | String | - |  |
| 7 | itemGroupId | String | - | u_mes_prod_itemGroup._id |
| 8 | itemGroupName | String | - |  |
| 9 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String | - |  |
| 11 | drawingNo | String | - |  |
| 12 | drawingRevision | String | - |  |
| 13 | revisionDate | Date | Date |  |
| 14 | materialSpecification | String | - |  |
| 15 | materialGrade | String | - |  |
| 16 | netWeightKg | Decimal128 | - |  |
| 17 | grossWeightKg | Decimal128 | - |  |
| 18 | procurementType | String | - |  |
| 19 | defaultSupplierId | String | - | u_mes_mast_supplier._id |
| 20 | defaultSupplierName | String | - |  |
| 21 | isSerialised | Boolean | - |  |
| 22 | isLotControlled | Boolean | - |  |
| 23 | serialNumberRangeId | String | - | u_mes_syst_numberRange._id |
| 24 | serialNumberRangeName | String | - |  |
| 25 | lotNumberRangeId | String | - | u_mes_syst_numberRange._id |
| 26 | lotNumberRangeName | String | - |  |
| 27 | shelfLifeDays | Int32 | - |  |
| 28 | safetyCharacteristic | Boolean | - |  |
| 29 | hsnCode | String | - |  |
| 30 | standardCostInr | Decimal128 | - |  |
| 31 | erpMaterialNo | String | - |  |
| 32 | defaultStorageLocationId | String | - | u_mes_matl_storageLocation._id |
| 33 | defaultStorageLocationName | String | - |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemRevision

Kind: child | Data class: master | Parent: u_mes_prod_item | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | revision | String | - |  |
| 9 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 10 | engineeringChangeName | String | - |  |
| 11 | effectiveFrom | Date | Date |  |
| 12 | description | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemCustomerPart

Kind: child | Data class: master | Parent: u_mes_prod_item | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | customerId | String | - | u_mes_mast_customer._id |
| 9 | customerName | String | - |  |
| 10 | customerPartNo | String | - |  |
| 11 | customerRevision | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_prod_productVariant

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | baseItemId | String | - | u_mes_prod_item._id |
| 7 | baseItemName | String | - |  |
| 8 | variantItemId | String | - | u_mes_prod_item._id |
| 9 | variantItemName | String | - |  |
| 10 | customerId | String | - | u_mes_mast_customer._id |
| 11 | customerName | String | - |  |
| 12 | optionsHand | String | - |  |
| 13 | optionsPistonDiameterMm | Decimal128 | - |  |
| 14 | optionsPadCompoundId | String | - | u_mes_prod_padCompound._id |
| 15 | optionsPadCompoundName | String | - |  |
| 16 | optionsMarketId | String | - | u_mes_prod_market._id |
| 17 | optionsMarketName | String | - |  |
| 18 | optionsSurfaceFinishId | String | - | u_mes_prod_surfaceFinish._id |
| 19 | optionsSurfaceFinishName | String | - |  |
| 20 | optionsColour | String | - |  |
| 21 | vehicleModelId | String | - | u_mes_prod_vehicleModel._id |
| 22 | vehicleModelName | String | - |  |
| 23 | modelYear | Int32 | - |  |
| 24 | labelSuffix | String | - |  |
| 25 | effectiveFrom | Date | Date |  |
| 26 | effectiveTo | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterial

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | itemRevision | String | - |  |
| 8 | bomVersion | Int32 | - |  |
| 9 | bomType | String | - |  |
| 10 | baseQuantity | Decimal128 | - |  |
| 11 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 12 | baseUnitOfMeasureName | String | - |  |
| 13 | effectiveFrom | Date | Date |  |
| 14 | effectiveTo | Date | Date |  |
| 15 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | - |  |
| 17 | approvedById | String | - | u_mes_mast_user._id |
| 18 | approvedBy | String | - |  |
| 19 | approvedAt | Date | Datetime |  |
| 20 | erpBomNo | String | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponent

Kind: child | Data class: master | Parent: u_mes_prod_billOfMaterial | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 6 | billOfMaterialName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | componentItemId | String | - | u_mes_prod_item._id |
| 9 | componentItemName | String | - |  |
| 10 | quantity | Decimal128 | - |  |
| 11 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 12 | unitOfMeasureName | String | - |  |
| 13 | scrapPct | Decimal128 | - |  |
| 14 | operationId | String | - | u_mes_prod_operation._id |
| 15 | operationName | String | - |  |
| 16 | isTraceable | Boolean | - |  |
| 17 | traceLevel | String | - |  |
| 18 | backflush | Boolean | - |  |
| 19 | referenceDesignator | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponentProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfMaterialComponent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfMaterialComponentId | String | - | u_mes_prod_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 9 | productVariantName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponentAlternateItem

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfMaterialComponent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfMaterialComponentId | String | - | u_mes_prod_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | alternateItemId | String | - | u_mes_prod_item._id |
| 9 | alternateItemName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_operation

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | operationType | String | - |  |
| 7 | description | String | - |  |
| 8 | defaultWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | defaultWorkCenterName | String | - |  |
| 10 | trackingGrain | String | - |  |
| 11 | standardCycleTimeSec | Decimal128 | - |  |
| 12 | standardSetupTimeMin | Int32 | - |  |
| 13 | standardManning | Int32 | - |  |
| 14 | isInspection | Boolean | - |  |
| 15 | isSpecialProcess | Boolean | - |  |
| 16 | specialProcessStandard | String | - |  |
| 17 | requiresFirstOffApproval | Boolean | - |  |
| 18 | erpControlKey | String | - |  |
| 19 | sequenceHint | Int32 | - |  |
| 20 | status | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_prod_operationRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prod_operation | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operationId | String | - | u_mes_prod_operation._id |
| 6 | operationName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 9 | requiredSkillName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_routing

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | itemRevision | String | - |  |
| 8 | routingVersion | Int32 | - |  |
| 9 | routingType | String | - |  |
| 10 | description | String | - |  |
| 11 | effectiveFrom | Date | Date |  |
| 12 | effectiveTo | Date | Date |  |
| 13 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 14 | engineeringChangeName | String | - |  |
| 15 | entryStepNo | Int32 | - |  |
| 16 | parentRoutingId | String | - | u_mes_prod_routing._id |
| 17 | parentRoutingName | String | - |  |
| 18 | approvedById | String | - | u_mes_mast_user._id |
| 19 | approvedBy | String | - |  |
| 20 | approvedAt | Date | Datetime |  |
| 21 | erpRoutingNo | String | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStep

Kind: child | Data class: master | Parent: u_mes_prod_routing | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | routingId | String | - | u_mes_prod_routing._id |
| 6 | routingName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | cycleTimeSec | Decimal128 | - |  |
| 13 | setupTimeMin | Int32 | - |  |
| 14 | isMilestone | Boolean | - |  |
| 15 | isOptional | Boolean | - |  |
| 16 | reworkReturnStepNo | Int32 | - |  |
| 17 | maxQueueTimeMin | Int32 | - |  |
| 18 | maxReworkCount | Int32 | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStepAlternateWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_prod_routingStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | routingStepId | String | - | u_mes_prod_routingStep._id |
| 6 | routingStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | alternateWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | alternateWorkCenterName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStepNextStep

Kind: child | Data class: master | Parent: u_mes_prod_routingStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | routingStepId | String | - | u_mes_prod_routingStep._id |
| 6 | routingStepName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | nextStepCondition | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcess

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | itemRevision | String | - |  |
| 8 | routingId | String | - | u_mes_prod_routing._id |
| 9 | routingName | String | - |  |
| 10 | bopVersion | Int32 | - |  |
| 11 | effectiveFrom | Date | Date |  |
| 12 | effectiveTo | Date | Date |  |
| 13 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 14 | billOfMaterialName | String | - |  |
| 15 | approvedById | String | - | u_mes_mast_user._id |
| 16 | approvedBy | String | - |  |
| 17 | approvedAt | Date | Datetime |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStep

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcess | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 6 | billOfProcessName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | recipeId | String | - | u_mes_prod_recipe._id |
| 11 | recipeName | String | - |  |
| 12 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 13 | workInstructionName | String | - |  |
| 14 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 15 | inspectionPlanName | String | - |  |
| 16 | cycleTimeSec | Decimal128 | - |  |
| 17 | manning | Int32 | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepEquipment

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepTool

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | toolId | String | - | u_mes_maint_tool._id |
| 9 | toolName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 9 | requiredSkillName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepConsumedComponent

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | quantity | Decimal128 | - |  |
| 11 | verifyByScan | Boolean | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepInterlock

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | interlockType | String | - |  |
| 9 | description | String | - |  |
| 10 | enforced | Boolean | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepProcessParameter

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 6 | billOfProcessStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | nominal | Decimal128 | - |  |
| 10 | lowerLimit | Decimal128 | - |  |
| 11 | upperLimit | Decimal128 | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstruction

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
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | version | Int32 | - |  |
| 11 | languageId | String | - | u_mes_mast_language._id |
| 12 | languageName | String | - |  |
| 13 | effectiveFrom | Date | Date |  |
| 14 | effectiveTo | Date | Date |  |
| 15 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | - |  |
| 17 | safetyNotes | String | - |  |
| 18 | authorUserId | String | - | u_mes_mast_user._id |
| 19 | authorUserName | String | - |  |
| 20 | approvedById | String | - | u_mes_mast_user._id |
| 21 | approvedBy | String | - |  |
| 22 | approvedAt | Date | Datetime |  |
| 23 | readAcknowledgementRequired | Boolean | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStep

Kind: child | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 6 | workInstructionName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | title | String | - |  |
| 9 | instructionText | String | - |  |
| 10 | inputType | String | - |  |
| 11 | expectedValue | Decimal128 | - |  |
| 12 | lowerLimit | Decimal128 | - |  |
| 13 | upperLimit | Decimal128 | - |  |
| 14 | isMandatory | Boolean | - |  |
| 15 | requiresScan | Boolean | - |  |
| 16 | caution | String | - |  |
| 17 | standardTimeSec | Decimal128 | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepMediaControlledDocument

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 6 | workInstructionStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | mediaControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 9 | mediaControlledDocumentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 6 | workInstructionStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 9 | productVariantName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepTool

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 6 | workInstructionStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | toolId | String | - | u_mes_maint_tool._id |
| 9 | toolName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepCharacteristic

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 6 | workInstructionStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionPpeItem

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 6 | workInstructionName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | ppeItemId | String | - | u_mes_prod_ppeItem._id |
| 9 | ppeItemName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionKeyPoint

Kind: valueList | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 6 | workInstructionName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | keyPoint | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipe

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | operationId | String | - | u_mes_prod_operation._id |
| 11 | operationName | String | - |  |
| 12 | version | Int32 | - |  |
| 13 | recipeType | String | - |  |
| 14 | programNo | String | - |  |
| 15 | effectiveFrom | Date | Date |  |
| 16 | effectiveTo | Date | Date |  |
| 17 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 18 | engineeringChangeName | String | - |  |
| 19 | checksum | String | - |  |
| 20 | approvedById | String | - | u_mes_mast_user._id |
| 21 | approvedBy | String | - |  |
| 22 | approvedAt | Date | Datetime |  |
| 23 | lastDownloadedAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeParameter

Kind: child | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | recipeId | String | - | u_mes_prod_recipe._id |
| 6 | recipeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | processTagId | String | - | u_mes_perf_processTag._id |
| 10 | processTagName | String | - |  |
| 11 | setPoint | Decimal128 | - |  |
| 12 | lowerLimit | Decimal128 | - |  |
| 13 | upperLimit | Decimal128 | - |  |
| 14 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - |  |
| 16 | isCritical | Boolean | - |  |
| 17 | downloadToController | Boolean | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeStage

Kind: child | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | recipeId | String | - | u_mes_prod_recipe._id |
| 6 | recipeName | String | - |  |
| 7 | stageNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | durationSec | Int32 | - |  |
| 10 | setPoint | Decimal128 | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_engineeringChange

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | description | String | - |  |
| 7 | changeType | String | - |  |
| 8 | reasonCodeText | String | - |  |
| 9 | originator | String | - |  |
| 10 | customerId | String | - | u_mes_mast_customer._id |
| 11 | customerName | String | - |  |
| 12 | customerChangeRef | String | - |  |
| 13 | raisedById | String | - | u_mes_mast_user._id |
| 14 | raisedBy | String | - |  |
| 15 | raisedAt | Date | Datetime |  |
| 16 | effectivityType | String | - |  |
| 17 | effectiveFrom | Date | Date |  |
| 18 | cutInSerialNo | String | - |  |
| 19 | stockDispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 20 | stockDispositionTypeName | String | - |  |
| 21 | ppapRequired | Boolean | - |  |
| 22 | implementedAt | Date | Datetime |  |
| 23 | closedAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeAffectedItem

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 6 | engineeringChangeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | fromRevision | String | - |  |
| 11 | toRevision | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 6 | engineeringChangeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | changeAction | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeApproval

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 6 | engineeringChangeName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | businessFunction | String | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | decision | String | - |  |
| 12 | decidedAt | Date | Datetime |  |
| 13 | comment | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 6 | engineeringChangeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 9 | controlledDocumentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_prod_itemGroup

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemFamily

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_ppeItem

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_market

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_padCompound

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_surfaceFinish

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_prod_vehicleModel

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | customerId | String | - | u_mes_mast_customer._id |
| 8 | customerName | String | - |  |
| 9 | modelYear | Int32 | - |  |
| 10 | platformCode | String | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
