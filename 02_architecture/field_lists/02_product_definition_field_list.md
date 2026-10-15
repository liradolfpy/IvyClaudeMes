# Field list - ProductDefinition (prod)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/02_product_definition/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_prod_item

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | description | String | - |  |
| 7 | itemType | String | - |  |
| 8 | itemGroupId | String | - | u_mes_prod_itemGroup._id |
| 9 | itemGroupName | String | - |  |
| 10 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 11 | baseUnitOfMeasureName | String | - |  |
| 12 | drawingNo | String | - |  |
| 13 | drawingRevision | String | - |  |
| 14 | revisionDate | Date | Date |  |
| 15 | materialSpecification | String | - |  |
| 16 | materialGrade | String | - |  |
| 17 | netWeightKg | Decimal128 | - |  |
| 18 | grossWeightKg | Decimal128 | - |  |
| 19 | procurementType | String | - |  |
| 20 | defaultSupplierId | String | - | u_mes_mast_supplier._id |
| 21 | defaultSupplierName | String | - |  |
| 22 | isSerialised | Boolean | - |  |
| 23 | isLotControlled | Boolean | - |  |
| 24 | serialNumberRangeId | String | - | u_mes_syst_numberRange._id |
| 25 | serialNumberRangeName | String | - |  |
| 26 | lotNumberRangeId | String | - | u_mes_syst_numberRange._id |
| 27 | lotNumberRangeName | String | - |  |
| 28 | shelfLifeDays | Int32 | - |  |
| 29 | safetyCharacteristic | Boolean | - |  |
| 30 | hsnCode | String | - |  |
| 31 | standardCostInr | Decimal128 | - |  |
| 32 | erpMaterialNo | String | - |  |
| 33 | defaultStorageLocationId | String | - | u_mes_matl_storageLocation._id |
| 34 | defaultStorageLocationName | String | - |  |
| 35 | fefoRequired | Boolean | - |  |
| 36 | exposureControlled | Boolean | - |  |
| 37 | openLifeMinutes | Int32 | - |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemRevision

Kind: child | Data class: master | Parent: u_mes_prod_item | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | revision | String | - |  |
| 10 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 11 | engineeringChangeName | String | - |  |
| 12 | effectiveFrom | Date | Date |  |
| 13 | description | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemCustomerPart

Kind: child | Data class: master | Parent: u_mes_prod_item | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | customerId | String | - | u_mes_mast_customer._id |
| 10 | customerName | String | - |  |
| 11 | customerPartNo | String | - |  |
| 12 | customerRevision | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_prod_productVariant

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | baseItemId | String | - | u_mes_prod_item._id |
| 8 | baseItemName | String | - |  |
| 9 | variantItemId | String | - | u_mes_prod_item._id |
| 10 | variantItemName | String | - |  |
| 11 | customerId | String | - | u_mes_mast_customer._id |
| 12 | customerName | String | - |  |
| 13 | optionsHand | String | - |  |
| 14 | optionsPistonDiameterMm | Decimal128 | - |  |
| 15 | optionsPadCompoundId | String | - | u_mes_prod_padCompound._id |
| 16 | optionsPadCompoundName | String | - |  |
| 17 | optionsMarketId | String | - | u_mes_prod_market._id |
| 18 | optionsMarketName | String | - |  |
| 19 | optionsSurfaceFinishId | String | - | u_mes_prod_surfaceFinish._id |
| 20 | optionsSurfaceFinishName | String | - |  |
| 21 | optionsColour | String | - |  |
| 22 | vehicleModelId | String | - | u_mes_prod_vehicleModel._id |
| 23 | vehicleModelName | String | - |  |
| 24 | modelYear | Int32 | - |  |
| 25 | labelSuffix | String | - |  |
| 26 | effectiveFrom | Date | Date |  |
| 27 | effectiveTo | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterial

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | itemRevision | String | - |  |
| 9 | bomVersion | Int32 | - |  |
| 10 | bomType | String | - |  |
| 11 | baseQuantity | Decimal128 | - |  |
| 12 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | baseUnitOfMeasureName | String | - |  |
| 14 | effectiveFrom | Date | Date |  |
| 15 | effectiveTo | Date | Date |  |
| 16 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - |  |
| 18 | approvedById | String | - | u_mes_mast_user._id |
| 19 | approvedBy | String | - |  |
| 20 | approvedAt | Date | Datetime |  |
| 21 | erpBomNo | String | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponent

Kind: child | Data class: master | Parent: u_mes_prod_billOfMaterial | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 7 | billOfMaterialName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | componentItemId | String | - | u_mes_prod_item._id |
| 10 | componentItemName | String | - |  |
| 11 | quantity | Decimal128 | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | scrapPct | Decimal128 | - |  |
| 15 | operationId | String | - | u_mes_prod_operation._id |
| 16 | operationName | String | - |  |
| 17 | isTraceable | Boolean | - |  |
| 18 | traceLevel | String | - |  |
| 19 | backflush | Boolean | - |  |
| 20 | referenceDesignator | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponentProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfMaterialComponent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfMaterialComponentId | String | - | u_mes_prod_billOfMaterialComponent._id |
| 7 | billOfMaterialComponentName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfMaterialComponentAlternateItem

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfMaterialComponent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfMaterialComponentId | String | - | u_mes_prod_billOfMaterialComponent._id |
| 7 | billOfMaterialComponentName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | alternateItemId | String | - | u_mes_prod_item._id |
| 10 | alternateItemName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_operation

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | operationType | String | - |  |
| 8 | description | String | - |  |
| 9 | defaultWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | defaultWorkCenterName | String | - |  |
| 11 | trackingGrain | String | - |  |
| 12 | standardCycleTimeSec | Decimal128 | - |  |
| 13 | standardSetupTimeMin | Int32 | - |  |
| 14 | standardManning | Int32 | - |  |
| 15 | isInspection | Boolean | - |  |
| 16 | isSpecialProcess | Boolean | - |  |
| 17 | specialProcessStandard | String | - |  |
| 18 | requiresFirstOffApproval | Boolean | - |  |
| 19 | erpControlKey | String | - |  |
| 20 | sequenceHint | Int32 | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_prod_operationRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prod_operation | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operationId | String | - | u_mes_prod_operation._id |
| 7 | operationName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 10 | requiredSkillName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_routing

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | itemRevision | String | - |  |
| 9 | routingVersion | Int32 | - |  |
| 10 | routingType | String | - |  |
| 11 | description | String | - |  |
| 12 | effectiveFrom | Date | Date |  |
| 13 | effectiveTo | Date | Date |  |
| 14 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 15 | engineeringChangeName | String | - |  |
| 16 | entryStepNo | Int32 | - |  |
| 17 | parentRoutingId | String | - | u_mes_prod_routing._id |
| 18 | parentRoutingName | String | - |  |
| 19 | approvedById | String | - | u_mes_mast_user._id |
| 20 | approvedBy | String | - |  |
| 21 | approvedAt | Date | Datetime |  |
| 22 | erpRoutingNo | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStep

Kind: child | Data class: master | Parent: u_mes_prod_routing | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | routingId | String | - | u_mes_prod_routing._id |
| 7 | routingName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | cycleTimeSec | Decimal128 | - |  |
| 14 | setupTimeMin | Int32 | - |  |
| 15 | isMilestone | Boolean | - |  |
| 16 | isOptional | Boolean | - |  |
| 17 | reworkReturnStepNo | Int32 | - |  |
| 18 | maxQueueTimeMin | Int32 | - |  |
| 19 | maxReworkCount | Int32 | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStepAlternateWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_prod_routingStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | routingStepId | String | - | u_mes_prod_routingStep._id |
| 7 | routingStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | alternateWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | alternateWorkCenterName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_routingStepNextStep

Kind: child | Data class: master | Parent: u_mes_prod_routingStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | routingStepId | String | - | u_mes_prod_routingStep._id |
| 7 | routingStepName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | nextStepCondition | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcess

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | itemRevision | String | - |  |
| 9 | routingId | String | - | u_mes_prod_routing._id |
| 10 | routingName | String | - |  |
| 11 | bopVersion | Int32 | - |  |
| 12 | effectiveFrom | Date | Date |  |
| 13 | effectiveTo | Date | Date |  |
| 14 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 15 | billOfMaterialName | String | - |  |
| 16 | approvedById | String | - | u_mes_mast_user._id |
| 17 | approvedBy | String | - |  |
| 18 | approvedAt | Date | Datetime |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStep

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcess | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 7 | billOfProcessName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | recipeId | String | - | u_mes_prod_recipe._id |
| 12 | recipeName | String | - |  |
| 13 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 14 | workInstructionName | String | - |  |
| 15 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 16 | inspectionPlanName | String | - |  |
| 17 | cycleTimeSec | Decimal128 | - |  |
| 18 | manning | Int32 | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepEquipment

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepTool

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | toolId | String | - | u_mes_maint_tool._id |
| 10 | toolName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 10 | requiredSkillName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepConsumedComponent

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | quantity | Decimal128 | - |  |
| 12 | verifyByScan | Boolean | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepInterlock

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | interlockType | String | - |  |
| 10 | description | String | - |  |
| 11 | enforced | Boolean | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_prod_billOfProcessStepProcessParameter

Kind: child | Data class: master | Parent: u_mes_prod_billOfProcessStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | billOfProcessStepId | String | - | u_mes_prod_billOfProcessStep._id |
| 7 | billOfProcessStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | nominal | Decimal128 | - |  |
| 11 | lowerLimit | Decimal128 | - |  |
| 12 | upperLimit | Decimal128 | - |  |
| 13 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstruction

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
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | version | Int32 | - |  |
| 12 | languageId | String | - | u_mes_mast_language._id |
| 13 | languageName | String | - |  |
| 14 | effectiveFrom | Date | Date |  |
| 15 | effectiveTo | Date | Date |  |
| 16 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - |  |
| 18 | safetyNotes | String | - |  |
| 19 | authorUserId | String | - | u_mes_mast_user._id |
| 20 | authorUserName | String | - |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | readAcknowledgementRequired | Boolean | - |  |
| 25 | reacknowledgeOnRevision | Boolean | - |  |
| 26 | generationSource | String | - |  |
| 27 | sourceBillOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 28 | sourceBillOfProcessName | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStep

Kind: child | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | title | String | - |  |
| 10 | instructionText | String | - |  |
| 11 | inputType | String | - |  |
| 12 | expectedValue | Decimal128 | - |  |
| 13 | lowerLimit | Decimal128 | - |  |
| 14 | upperLimit | Decimal128 | - |  |
| 15 | isMandatory | Boolean | - |  |
| 16 | requiresScan | Boolean | - |  |
| 17 | caution | String | - |  |
| 18 | standardTimeSec | Decimal128 | - |  |
| 19 | arContentControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 20 | arContentControlledDocumentName | String | - |  |
| 21 | arAnchorRef | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepMediaControlledDocument

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 7 | workInstructionStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | mediaControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 10 | mediaControlledDocumentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 7 | workInstructionStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepTool

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 7 | workInstructionStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | toolId | String | - | u_mes_maint_tool._id |
| 10 | toolName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionStepCharacteristic

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstructionStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionStepId | String | - | u_mes_prod_workInstructionStep._id |
| 7 | workInstructionStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionPpeItem

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | ppeItemId | String | - | u_mes_prod_ppeItem._id |
| 10 | ppeItemName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionKeyPoint

Kind: valueList | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | keyPoint | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipe

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | operationId | String | - | u_mes_prod_operation._id |
| 12 | operationName | String | - |  |
| 13 | version | Int32 | - |  |
| 14 | recipeType | String | - |  |
| 15 | programNo | String | - |  |
| 16 | effectiveFrom | Date | Date |  |
| 17 | effectiveTo | Date | Date |  |
| 18 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 19 | engineeringChangeName | String | - |  |
| 20 | checksum | String | - |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | lastDownloadedAt | Date | Datetime |  |
| 25 | previousVersionRecipeId | String | - | u_mes_prod_recipe._id |
| 26 | previousVersionRecipeName | String | - |  |
| 27 | changeReasonText | String | - |  |
| 28 | releasedAt | Date | Datetime |  |
| 29 | isGoldenRecipe | Boolean | - |  |
| 30 | goldenDesignatedAt | Date | Datetime |  |
| 31 | goldenDesignatedById | String | - | u_mes_mast_user._id |
| 32 | goldenDesignatedBy | String | - |  |
| 33 | origin | String | - |  |
| 34 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 35 | analyticsModelName | String | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeParameter

Kind: child | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | recipeId | String | - | u_mes_prod_recipe._id |
| 7 | recipeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | processTagId | String | - | u_mes_perf_processTag._id |
| 11 | processTagName | String | - |  |
| 12 | setPoint | Decimal128 | - |  |
| 13 | lowerLimit | Decimal128 | - |  |
| 14 | upperLimit | Decimal128 | - |  |
| 15 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - |  |
| 17 | isCritical | Boolean | - |  |
| 18 | downloadToController | Boolean | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeStage

Kind: child | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | recipeId | String | - | u_mes_prod_recipe._id |
| 7 | recipeName | String | - |  |
| 8 | stageNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | durationSec | Int32 | - |  |
| 11 | setPoint | Decimal128 | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_prod_engineeringChange

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | description | String | - |  |
| 8 | changeType | String | - |  |
| 9 | reasonCodeText | String | - |  |
| 10 | originator | String | - |  |
| 11 | customerId | String | - | u_mes_mast_customer._id |
| 12 | customerName | String | - |  |
| 13 | customerChangeRef | String | - |  |
| 14 | raisedById | String | - | u_mes_mast_user._id |
| 15 | raisedBy | String | - |  |
| 16 | raisedAt | Date | Datetime |  |
| 17 | effectivityType | String | - |  |
| 18 | effectiveFrom | Date | Date |  |
| 19 | cutInSerialNo | String | - |  |
| 20 | stockDispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 21 | stockDispositionTypeName | String | - |  |
| 22 | ppapRequired | Boolean | - |  |
| 23 | implementedAt | Date | Datetime |  |
| 24 | closedAt | Date | Datetime |  |
| 25 | gmpImpact | Boolean | - |  |
| 26 | validationRequired | Boolean | - |  |
| 27 | regulatoryImpact | String | - |  |
| 28 | riskAssessmentId | String | - | u_mes_qual_riskAssessment._id |
| 29 | riskAssessmentName | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeAffectedItem

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 7 | engineeringChangeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | fromRevision | String | - |  |
| 12 | toRevision | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 7 | engineeringChangeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | changeAction | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeApproval

Kind: child | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 7 | engineeringChangeName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | businessFunction | String | - |  |
| 10 | userId | String | - | u_mes_mast_user._id |
| 11 | userName | String | - |  |
| 12 | decision | String | - |  |
| 13 | decidedAt | Date | Datetime |  |
| 14 | comment | String | - |  |
| 15 | schemaVersion | Int32 | - |  |
| 16 | createdAt | Date | Datetime |  |
| 17 | createdById | String | - | u_mes_mast_user._id |
| 18 | createdBy | String | - |  |
| 19 | updatedAt | Date | Datetime |  |
| 20 | updatedById | String | - | u_mes_mast_user._id |
| 21 | updatedBy | String | - |  |

## u_mes_prod_engineeringChangeControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_prod_engineeringChange | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 7 | engineeringChangeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 10 | controlledDocumentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_prod_itemGroup

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_itemFamily

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_ppeItem

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_market

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_padCompound

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_surfaceFinish

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_prod_vehicleModel

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | customerId | String | - | u_mes_mast_customer._id |
| 9 | customerName | String | - |  |
| 10 | modelYear | Int32 | - |  |
| 11 | platformCode | String | - |  |
| 12 | sequenceNo | Int32 | - |  |
| 13 | status | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | recipeId | String | - | u_mes_prod_recipe._id |
| 7 | recipeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_recipeControlledDocument

Kind: relationship | Data class: master | Parent: u_mes_prod_recipe | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | recipeId | String | - | u_mes_prod_recipe._id |
| 7 | recipeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 10 | controlledDocumentName | String | - |  |
| 11 | fileRole | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_prod_workInstructionProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prod_workInstruction | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 7 | workInstructionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
