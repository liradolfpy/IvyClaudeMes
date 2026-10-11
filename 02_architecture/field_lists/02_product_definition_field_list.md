# Field list - Product definition (prd)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/02_product_definition/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_prd_item

Kind: entity | Data class: master | Parent: - | _id pattern: ITM-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | description | String |  |
| 6 | itemType | String |  |
| 7 | itemGroup | String |  |
| 8 | baseUnitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 9 | baseUnitOfMeasureName | String |  |
| 10 | drawingNo | String |  |
| 11 | drawingRevision | String |  |
| 12 | revisionDate | Date |  |
| 13 | materialSpecification | String |  |
| 14 | materialGrade | String |  |
| 15 | netWeightKg | Decimal128 |  |
| 16 | grossWeightKg | Decimal128 |  |
| 17 | procurementType | String |  |
| 18 | defaultSupplierId | String | u_mes_mdm_supplier._id |
| 19 | defaultSupplierName | String |  |
| 20 | isSerialised | Boolean |  |
| 21 | isLotControlled | Boolean |  |
| 22 | serialNumberRangeId | String | u_mes_sys_numberRange._id |
| 23 | serialNumberRangeName | String |  |
| 24 | lotNumberRangeId | String | u_mes_sys_numberRange._id |
| 25 | lotNumberRangeName | String |  |
| 26 | shelfLifeDays | Int32 |  |
| 27 | safetyCharacteristic | Boolean |  |
| 28 | hsnCode | String |  |
| 29 | standardCostInr | Decimal128 |  |
| 30 | erpMaterialNo | String |  |
| 31 | defaultStorageLocationId | String | u_mes_mat_storageLocation._id |
| 32 | defaultStorageLocationName | String |  |
| 33 | status | String |  |
| 34 | schemaVersion | Int32 |  |

## u_mes_prd_itemRevision

Kind: child | Data class: master | Parent: u_mes_prd_item | _id pattern: <itemId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | revision | String |  |
| 9 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 10 | engineeringChangeName | String |  |
| 11 | effectiveFrom | Date |  |
| 12 | description | String |  |
| 13 | schemaVersion | Int32 |  |

## u_mes_prd_itemCustomerPart

Kind: child | Data class: master | Parent: u_mes_prd_item | _id pattern: <itemId>-CP<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | customerId | String | u_mes_mdm_customer._id |
| 9 | customerName | String |  |
| 10 | customerPartNo | String |  |
| 11 | customerRevision | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_prd_productVariant

Kind: entity | Data class: master | Parent: - | _id pattern: VAR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | baseItemId | String | u_mes_prd_item._id |
| 7 | baseItemName | String |  |
| 8 | variantItemId | String | u_mes_prd_item._id |
| 9 | variantItemName | String |  |
| 10 | customerId | String | u_mes_mdm_customer._id |
| 11 | customerName | String |  |
| 12 | optionsHand | String |  |
| 13 | optionsPistonDiameterMm | Decimal128 |  |
| 14 | optionsPadCompound | String |  |
| 15 | optionsMarket | String |  |
| 16 | optionsSurfaceFinish | String |  |
| 17 | optionsColour | String |  |
| 18 | modelCode | String |  |
| 19 | modelYear | Int32 |  |
| 20 | labelSuffix | String |  |
| 21 | effectiveFrom | Date |  |
| 22 | effectiveTo | Date |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_prd_billOfMaterial

Kind: entity | Data class: master | Parent: - | _id pattern: BOM-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | itemRevision | String |  |
| 8 | bomVersion | Int32 |  |
| 9 | bomType | String |  |
| 10 | baseQuantity | Decimal128 |  |
| 11 | baseUnitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 12 | baseUnitOfMeasureName | String |  |
| 13 | effectiveFrom | Date |  |
| 14 | effectiveTo | Date |  |
| 15 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 16 | engineeringChangeName | String |  |
| 17 | approvedById | String | u_mes_mdm_user._id |
| 18 | approvedBy | String |  |
| 19 | approvedAt | Date |  |
| 20 | erpBomNo | String |  |
| 21 | status | String |  |
| 22 | schemaVersion | Int32 |  |

## u_mes_prd_billOfMaterialComponent

Kind: child | Data class: master | Parent: u_mes_prd_billOfMaterial | _id pattern: <billOfMaterialId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfMaterialId | String | u_mes_prd_billOfMaterial._id |
| 6 | billOfMaterialName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | componentItemId | String | u_mes_prd_item._id |
| 9 | componentItemName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 12 | unitOfMeasureName | String |  |
| 13 | scrapPct | Decimal128 |  |
| 14 | operationId | String | u_mes_prd_operation._id |
| 15 | operationName | String |  |
| 16 | isTraceable | Boolean |  |
| 17 | traceLevel | String |  |
| 18 | backflush | Boolean |  |
| 19 | referenceDesignator | String |  |
| 20 | schemaVersion | Int32 |  |

## u_mes_prd_billOfMaterialComponentProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prd_billOfMaterialComponent | _id pattern: <billOfMaterialComponentId>-PV<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfMaterialComponentId | String | u_mes_prd_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | productVariantId | String | u_mes_prd_productVariant._id |
| 9 | productVariantName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_billOfMaterialComponentAlternateItem

Kind: relationship | Data class: master | Parent: u_mes_prd_billOfMaterialComponent | _id pattern: <billOfMaterialComponentId>-AI<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfMaterialComponentId | String | u_mes_prd_billOfMaterialComponent._id |
| 6 | billOfMaterialComponentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | alternateItemId | String | u_mes_prd_item._id |
| 9 | alternateItemName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_operation

Kind: entity | Data class: master | Parent: - | _id pattern: OPN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | operationType | String |  |
| 7 | description | String |  |
| 8 | defaultWorkCenterId | String | u_mes_mdm_workCenter._id |
| 9 | defaultWorkCenterName | String |  |
| 10 | trackingGrain | String |  |
| 11 | standardCycleTimeSec | Decimal128 |  |
| 12 | standardSetupTimeMin | Int32 |  |
| 13 | standardManning | Int32 |  |
| 14 | isInspection | Boolean |  |
| 15 | isSpecialProcess | Boolean |  |
| 16 | specialProcessStandard | String |  |
| 17 | requiresFirstOffApproval | Boolean |  |
| 18 | erpControlKey | String |  |
| 19 | sequenceHint | Int32 |  |
| 20 | status | String |  |
| 21 | schemaVersion | Int32 |  |

## u_mes_prd_operationRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prd_operation | _id pattern: <operationId>-RS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operationId | String | u_mes_prd_operation._id |
| 6 | operationName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | requiredSkillId | String | u_mes_mdm_skill._id |
| 9 | requiredSkillName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_routing

Kind: entity | Data class: master | Parent: - | _id pattern: RTG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | itemRevision | String |  |
| 8 | routingVersion | Int32 |  |
| 9 | routingType | String |  |
| 10 | description | String |  |
| 11 | effectiveFrom | Date |  |
| 12 | effectiveTo | Date |  |
| 13 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 14 | engineeringChangeName | String |  |
| 15 | entryStepNo | Int32 |  |
| 16 | parentRoutingId | String | u_mes_prd_routing._id |
| 17 | parentRoutingName | String |  |
| 18 | approvedById | String | u_mes_mdm_user._id |
| 19 | approvedBy | String |  |
| 20 | approvedAt | Date |  |
| 21 | erpRoutingNo | String |  |
| 22 | status | String |  |
| 23 | schemaVersion | Int32 |  |

## u_mes_prd_routingStep

Kind: child | Data class: master | Parent: u_mes_prd_routing | _id pattern: <routingId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | routingId | String | u_mes_prd_routing._id |
| 6 | routingName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | workCenterId | String | u_mes_mdm_workCenter._id |
| 11 | workCenterName | String |  |
| 12 | cycleTimeSec | Decimal128 |  |
| 13 | setupTimeMin | Int32 |  |
| 14 | isMilestone | Boolean |  |
| 15 | isOptional | Boolean |  |
| 16 | reworkReturnStepNo | Int32 |  |
| 17 | maxQueueTimeMin | Int32 |  |
| 18 | maxReworkCount | Int32 |  |
| 19 | schemaVersion | Int32 |  |

## u_mes_prd_routingStepAlternateWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_prd_routingStep | _id pattern: <routingStepId>-AWC<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | routingStepId | String | u_mes_prd_routingStep._id |
| 6 | routingStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | alternateWorkCenterId | String | u_mes_mdm_workCenter._id |
| 9 | alternateWorkCenterName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_routingStepNextStep

Kind: child | Data class: master | Parent: u_mes_prd_routingStep | _id pattern: <routingStepId>-NS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | routingStepId | String | u_mes_prd_routingStep._id |
| 6 | routingStepName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | nextStepCondition | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcess

Kind: entity | Data class: master | Parent: - | _id pattern: BOP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | itemRevision | String |  |
| 8 | routingId | String | u_mes_prd_routing._id |
| 9 | routingName | String |  |
| 10 | bopVersion | Int32 |  |
| 11 | effectiveFrom | Date |  |
| 12 | effectiveTo | Date |  |
| 13 | billOfMaterialId | String | u_mes_prd_billOfMaterial._id |
| 14 | billOfMaterialName | String |  |
| 15 | approvedById | String | u_mes_mdm_user._id |
| 16 | approvedBy | String |  |
| 17 | approvedAt | Date |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStep

Kind: child | Data class: master | Parent: u_mes_prd_billOfProcess | _id pattern: <billOfProcessId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessId | String | u_mes_prd_billOfProcess._id |
| 6 | billOfProcessName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | recipeId | String | u_mes_prd_recipe._id |
| 11 | recipeName | String |  |
| 12 | workInstructionId | String | u_mes_prd_workInstruction._id |
| 13 | workInstructionName | String |  |
| 14 | inspectionPlanId | String | u_mes_qlt_inspectionPlan._id |
| 15 | inspectionPlanName | String |  |
| 16 | cycleTimeSec | Decimal128 |  |
| 17 | manning | Int32 |  |
| 18 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepEquipment

Kind: relationship | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | equipmentId | String | u_mes_mdm_equipment._id |
| 9 | equipmentName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepTool

Kind: relationship | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | toolId | String | u_mes_mnt_tool._id |
| 9 | toolName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-RS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | requiredSkillId | String | u_mes_mdm_skill._id |
| 9 | requiredSkillName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepConsumedComponent

Kind: child | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-CC<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | verifyByScan | Boolean |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepInterlock

Kind: child | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-I<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | interlockType | String |  |
| 9 | description | String |  |
| 10 | enforced | Boolean |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_prd_billOfProcessStepProcessParameter

Kind: child | Data class: master | Parent: u_mes_prd_billOfProcessStep | _id pattern: <billOfProcessStepId>-PP<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | billOfProcessStepId | String | u_mes_prd_billOfProcessStep._id |
| 6 | billOfProcessStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | nominal | Decimal128 |  |
| 10 | lowerLimit | Decimal128 |  |
| 11 | upperLimit | Decimal128 |  |
| 12 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 13 | unitOfMeasureName | String |  |
| 14 | schemaVersion | Int32 |  |

## u_mes_prd_workInstruction

Kind: entity | Data class: master | Parent: - | _id pattern: WI-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | itemId | String | u_mes_prd_item._id |
| 7 | itemName | String |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | version | Int32 |  |
| 11 | language | String |  |
| 12 | effectiveFrom | Date |  |
| 13 | effectiveTo | Date |  |
| 14 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 15 | engineeringChangeName | String |  |
| 16 | safetyNotes | String |  |
| 17 | authorUserId | String | u_mes_mdm_user._id |
| 18 | authorUserName | String |  |
| 19 | approvedById | String | u_mes_mdm_user._id |
| 20 | approvedBy | String |  |
| 21 | approvedAt | Date |  |
| 22 | readAcknowledgementRequired | Boolean |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionStep

Kind: child | Data class: master | Parent: u_mes_prd_workInstruction | _id pattern: <workInstructionId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionId | String | u_mes_prd_workInstruction._id |
| 6 | workInstructionName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | title | String |  |
| 9 | instructionText | String |  |
| 10 | inputType | String |  |
| 11 | expectedValue | Decimal128 |  |
| 12 | lowerLimit | Decimal128 |  |
| 13 | upperLimit | Decimal128 |  |
| 14 | isMandatory | Boolean |  |
| 15 | requiresScan | Boolean |  |
| 16 | caution | String |  |
| 17 | standardTimeSec | Decimal128 |  |
| 18 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionStepMediaControlledDocument

Kind: relationship | Data class: master | Parent: u_mes_prd_workInstructionStep | _id pattern: <workInstructionStepId>-MCD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionStepId | String | u_mes_prd_workInstructionStep._id |
| 6 | workInstructionStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | mediaControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 9 | mediaControlledDocumentName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionStepProductVariant

Kind: relationship | Data class: master | Parent: u_mes_prd_workInstructionStep | _id pattern: <workInstructionStepId>-PV<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionStepId | String | u_mes_prd_workInstructionStep._id |
| 6 | workInstructionStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | productVariantId | String | u_mes_prd_productVariant._id |
| 9 | productVariantName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionStepTool

Kind: relationship | Data class: master | Parent: u_mes_prd_workInstructionStep | _id pattern: <workInstructionStepId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionStepId | String | u_mes_prd_workInstructionStep._id |
| 6 | workInstructionStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | toolId | String | u_mes_mnt_tool._id |
| 9 | toolName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionStepCharacteristic

Kind: relationship | Data class: master | Parent: u_mes_prd_workInstructionStep | _id pattern: <workInstructionStepId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionStepId | String | u_mes_prd_workInstructionStep._id |
| 6 | workInstructionStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | characteristicId | String | u_mes_qlt_characteristic._id |
| 9 | characteristicName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionPpeItem

Kind: valueList | Data class: master | Parent: u_mes_prd_workInstruction | _id pattern: <workInstructionId>-PI<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionId | String | u_mes_prd_workInstruction._id |
| 6 | workInstructionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | ppeItem | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_prd_workInstructionKeyPoint

Kind: valueList | Data class: master | Parent: u_mes_prd_workInstruction | _id pattern: <workInstructionId>-KP<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workInstructionId | String | u_mes_prd_workInstruction._id |
| 6 | workInstructionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | keyPoint | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_prd_recipe

Kind: entity | Data class: master | Parent: - | _id pattern: RCP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | equipmentId | String | u_mes_mdm_equipment._id |
| 7 | equipmentName | String |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | operationId | String | u_mes_prd_operation._id |
| 11 | operationName | String |  |
| 12 | version | Int32 |  |
| 13 | recipeType | String |  |
| 14 | programNo | String |  |
| 15 | effectiveFrom | Date |  |
| 16 | effectiveTo | Date |  |
| 17 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 18 | engineeringChangeName | String |  |
| 19 | checksum | String |  |
| 20 | approvedById | String | u_mes_mdm_user._id |
| 21 | approvedBy | String |  |
| 22 | approvedAt | Date |  |
| 23 | lastDownloadedAt | Date |  |
| 24 | status | String |  |
| 25 | schemaVersion | Int32 |  |

## u_mes_prd_recipeParameter

Kind: child | Data class: master | Parent: u_mes_prd_recipe | _id pattern: <recipeId>-P<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | recipeId | String | u_mes_prd_recipe._id |
| 6 | recipeName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | processTagId | String | u_mes_eqp_processTag._id |
| 10 | processTagName | String |  |
| 11 | setPoint | Decimal128 |  |
| 12 | lowerLimit | Decimal128 |  |
| 13 | upperLimit | Decimal128 |  |
| 14 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 15 | unitOfMeasureName | String |  |
| 16 | isCritical | Boolean |  |
| 17 | downloadToController | Boolean |  |
| 18 | schemaVersion | Int32 |  |

## u_mes_prd_recipeStage

Kind: child | Data class: master | Parent: u_mes_prd_recipe | _id pattern: <recipeId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | recipeId | String | u_mes_prd_recipe._id |
| 6 | recipeName | String |  |
| 7 | stageNo | Int32 |  |
| 8 | name | String |  |
| 9 | durationSec | Int32 |  |
| 10 | setPoint | Decimal128 |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_prd_engineeringChange

Kind: entity | Data class: transaction | Parent: - | _id pattern: ECN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | description | String |  |
| 7 | changeType | String |  |
| 8 | reasonCodeText | String |  |
| 9 | originator | String |  |
| 10 | customerId | String | u_mes_mdm_customer._id |
| 11 | customerName | String |  |
| 12 | customerChangeRef | String |  |
| 13 | raisedById | String | u_mes_mdm_user._id |
| 14 | raisedBy | String |  |
| 15 | raisedAt | Date |  |
| 16 | effectivityType | String |  |
| 17 | effectiveFrom | Date |  |
| 18 | cutInSerialNo | String |  |
| 19 | stockDisposition | String |  |
| 20 | ppapRequired | Boolean |  |
| 21 | implementedAt | Date |  |
| 22 | closedAt | Date |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |
| 25 | createdAt | Date |  |
| 26 | createdById | String | u_mes_mdm_user._id |
| 27 | createdBy | String |  |
| 28 | updatedAt | Date |  |
| 29 | updatedById | String | u_mes_mdm_user._id |
| 30 | updatedBy | String |  |

## u_mes_prd_engineeringChangeAffectedItem

Kind: child | Data class: transaction | Parent: u_mes_prd_engineeringChange | _id pattern: <engineeringChangeId>-AI<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | fromRevision | String |  |
| 11 | toRevision | String |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_prd_engineeringChangeAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_prd_engineeringChange | _id pattern: <engineeringChangeId>-AO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | relatedCollectionName | String |  |
| 9 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String |  |
| 11 | changeAction | String |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_prd_engineeringChangeApproval

Kind: child | Data class: transaction | Parent: u_mes_prd_engineeringChange | _id pattern: <engineeringChangeId>-A<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | businessFunction | String |  |
| 9 | userId | String | u_mes_mdm_user._id |
| 10 | userName | String |  |
| 11 | decision | String |  |
| 12 | decidedAt | Date |  |
| 13 | comment | String |  |
| 14 | schemaVersion | Int32 |  |
| 15 | createdAt | Date |  |
| 16 | createdById | String | u_mes_mdm_user._id |
| 17 | createdBy | String |  |
| 18 | updatedAt | Date |  |
| 19 | updatedById | String | u_mes_mdm_user._id |
| 20 | updatedBy | String |  |

## u_mes_prd_engineeringChangeControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_prd_engineeringChange | _id pattern: <engineeringChangeId>-CD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 6 | engineeringChangeName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | controlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 9 | controlledDocumentName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |
