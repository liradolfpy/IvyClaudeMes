# Product Definition (prod) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prod_item | Entity | master | 39 | 27 | 4 | 7 |
| 2 | u_mes_prod_itemRevision | Child | master | 14 | 14 | 1 | 2 |
| 3 | u_mes_prod_itemCustomerPart | Child | master | 13 | 13 | 1 | 2 |
| 4 | u_mes_prod_productVariant | Entity | master | 29 | 13 | 3 | 7 |
| 5 | u_mes_prod_billOfMaterial | Entity | master | 23 | 17 | 3 | 5 |
| 6 | u_mes_prod_billOfMaterialComponent | Child | master | 21 | 16 | 2 | 4 |
| 7 | u_mes_prod_billOfMaterialComponentProductVariant | Relationship | master | 11 | 11 | 1 | 2 |
| 8 | u_mes_prod_billOfMaterialComponentAlternateItem | Relationship | master | 11 | 11 | 1 | 2 |
| 9 | u_mes_prod_operation | Entity | master | 22 | 21 | 4 | 3 |
| 10 | u_mes_prod_operationRequiredSkill | Relationship | master | 11 | 11 | 1 | 2 |
| 11 | u_mes_prod_routing | Entity | master | 24 | 16 | 3 | 5 |
| 12 | u_mes_prod_routingStep | Child | master | 20 | 16 | 1 | 3 |
| 13 | u_mes_prod_routingStepAlternateWorkCenter | Relationship | master | 11 | 11 | 1 | 2 |
| 14 | u_mes_prod_routingStepNextStep | Child | master | 10 | 10 | 2 | 1 |
| 15 | u_mes_prod_billOfProcess | Entity | master | 20 | 14 | 2 | 5 |
| 16 | u_mes_prod_billOfProcessStep | Child | master | 19 | 13 | 1 | 4 |
| 17 | u_mes_prod_billOfProcessStepEquipment | Relationship | master | 11 | 11 | 1 | 2 |
| 18 | u_mes_prod_billOfProcessStepTool | Relationship | master | 11 | 11 | 1 | 2 |
| 19 | u_mes_prod_billOfProcessStepRequiredSkill | Relationship | master | 11 | 11 | 1 | 2 |
| 20 | u_mes_prod_billOfProcessStepConsumedComponent | Child | master | 13 | 13 | 1 | 2 |
| 21 | u_mes_prod_billOfProcessStepInterlock | Child | master | 12 | 12 | 2 | 1 |
| 22 | u_mes_prod_billOfProcessStepProcessParameter | Child | master | 15 | 13 | 1 | 2 |
| 23 | u_mes_prod_workInstruction | Entity | master | 30 | 21 | 3 | 7 |
| 24 | u_mes_prod_workInstructionStep | Child | master | 22 | 15 | 2 | 2 |
| 25 | u_mes_prod_workInstructionStepMediaControlledDocument | Relationship | master | 11 | 11 | 1 | 2 |
| 26 | u_mes_prod_workInstructionStepProductVariant | Relationship | master | 11 | 11 | 1 | 2 |
| 27 | u_mes_prod_workInstructionStepTool | Relationship | master | 11 | 11 | 1 | 2 |
| 28 | u_mes_prod_workInstructionStepCharacteristic | Relationship | master | 11 | 11 | 1 | 2 |
| 29 | u_mes_prod_workInstructionPpeItem | Relationship | master | 11 | 11 | 1 | 2 |
| 30 | u_mes_prod_workInstructionKeyPoint | Value list | master | 10 | 10 | 1 | 1 |
| 31 | u_mes_prod_recipe | Entity | master | 37 | 19 | 4 | 7 |
| 32 | u_mes_prod_recipeParameter | Child | master | 19 | 15 | 1 | 3 |
| 33 | u_mes_prod_recipeStage | Child | master | 12 | 12 | 1 | 1 |
| 34 | u_mes_prod_engineeringChange | Entity | transaction | 37 | 27 | 6 | 6 |
| 35 | u_mes_prod_engineeringChangeAffectedItem | Child | transaction | 19 | 19 | 1 | 2 |
| 36 | u_mes_prod_engineeringChangeAffectedObject | Child | transaction | 19 | 19 | 2 | 1 |
| 37 | u_mes_prod_engineeringChangeApproval | Child | transaction | 21 | 19 | 3 | 2 |
| 38 | u_mes_prod_engineeringChangeControlledDocument | Relationship | transaction | 17 | 17 | 1 | 2 |
| 39 | u_mes_prod_itemGroup | Entity | master | 10 | 10 | 2 | 2 |
| 40 | u_mes_prod_itemFamily | Entity | master | 10 | 10 | 2 | 2 |
| 41 | u_mes_prod_ppeItem | Entity | master | 10 | 10 | 2 | 2 |
| 42 | u_mes_prod_market | Entity | master | 10 | 10 | 2 | 2 |
| 43 | u_mes_prod_padCompound | Entity | master | 10 | 10 | 2 | 2 |
| 44 | u_mes_prod_surfaceFinish | Entity | master | 10 | 10 | 2 | 2 |
| 45 | u_mes_prod_vehicleModel | Entity | master | 14 | 11 | 2 | 3 |
| 46 | u_mes_prod_recipeProductVariant | Relationship | master | 11 | 11 | 1 | 2 |
| 47 | u_mes_prod_recipeControlledDocument | Relationship | master | 12 | 12 | 2 | 2 |
| 48 | u_mes_prod_workInstructionWorkCenter | Relationship | master | 11 | 11 | 1 | 2 |
| 49 | u_mes_prod_workInstructionProductVariant | Relationship | master | 11 | 11 | 1 | 2 |
