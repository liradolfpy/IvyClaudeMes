# Product Definition (prod) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prod_item | Entity | master | 38 | 26 | 3 | 7 |
| 2 | u_mes_prod_itemRevision | Child | master | 13 | 13 | 0 | 2 |
| 3 | u_mes_prod_itemCustomerPart | Child | master | 12 | 12 | 0 | 2 |
| 4 | u_mes_prod_productVariant | Entity | master | 28 | 14 | 2 | 7 |
| 5 | u_mes_prod_billOfMaterial | Entity | master | 22 | 16 | 2 | 5 |
| 6 | u_mes_prod_billOfMaterialComponent | Child | master | 20 | 15 | 1 | 4 |
| 7 | u_mes_prod_billOfMaterialComponentProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
| 8 | u_mes_prod_billOfMaterialComponentAlternateItem | Relationship | master | 10 | 10 | 0 | 2 |
| 9 | u_mes_prod_operation | Entity | master | 21 | 20 | 3 | 3 |
| 10 | u_mes_prod_operationRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 11 | u_mes_prod_routing | Entity | master | 23 | 15 | 2 | 5 |
| 12 | u_mes_prod_routingStep | Child | master | 19 | 15 | 0 | 3 |
| 13 | u_mes_prod_routingStepAlternateWorkCenter | Relationship | master | 10 | 10 | 0 | 2 |
| 14 | u_mes_prod_routingStepNextStep | Child | master | 9 | 9 | 1 | 1 |
| 15 | u_mes_prod_billOfProcess | Entity | master | 19 | 13 | 1 | 5 |
| 16 | u_mes_prod_billOfProcessStep | Child | master | 18 | 12 | 0 | 4 |
| 17 | u_mes_prod_billOfProcessStepEquipment | Relationship | master | 10 | 10 | 0 | 2 |
| 18 | u_mes_prod_billOfProcessStepTool | Relationship | master | 10 | 10 | 0 | 2 |
| 19 | u_mes_prod_billOfProcessStepRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 20 | u_mes_prod_billOfProcessStepConsumedComponent | Child | master | 12 | 12 | 0 | 2 |
| 21 | u_mes_prod_billOfProcessStepInterlock | Child | master | 11 | 11 | 1 | 1 |
| 22 | u_mes_prod_billOfProcessStepProcessParameter | Child | master | 14 | 12 | 0 | 2 |
| 23 | u_mes_prod_workInstruction | Entity | master | 29 | 20 | 2 | 7 |
| 24 | u_mes_prod_workInstructionStep | Child | master | 21 | 14 | 1 | 2 |
| 25 | u_mes_prod_workInstructionStepMediaControlledDocument | Relationship | master | 10 | 10 | 0 | 2 |
| 26 | u_mes_prod_workInstructionStepProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
| 27 | u_mes_prod_workInstructionStepTool | Relationship | master | 10 | 10 | 0 | 2 |
| 28 | u_mes_prod_workInstructionStepCharacteristic | Relationship | master | 10 | 10 | 0 | 2 |
| 29 | u_mes_prod_workInstructionPpeItem | Relationship | master | 10 | 10 | 0 | 2 |
| 30 | u_mes_prod_workInstructionKeyPoint | Value list | master | 9 | 9 | 0 | 1 |
| 31 | u_mes_prod_recipe | Entity | master | 36 | 18 | 3 | 7 |
| 32 | u_mes_prod_recipeParameter | Child | master | 18 | 14 | 0 | 3 |
| 33 | u_mes_prod_recipeStage | Child | master | 11 | 11 | 0 | 1 |
| 34 | u_mes_prod_engineeringChange | Entity | transaction | 36 | 26 | 5 | 6 |
| 35 | u_mes_prod_engineeringChangeAffectedItem | Child | transaction | 18 | 18 | 0 | 2 |
| 36 | u_mes_prod_engineeringChangeAffectedObject | Child | transaction | 18 | 18 | 1 | 1 |
| 37 | u_mes_prod_engineeringChangeApproval | Child | transaction | 20 | 18 | 2 | 2 |
| 38 | u_mes_prod_engineeringChangeControlledDocument | Relationship | transaction | 16 | 16 | 0 | 2 |
| 39 | u_mes_prod_itemGroup | Entity | master | 9 | 9 | 1 | 2 |
| 40 | u_mes_prod_itemFamily | Entity | master | 9 | 9 | 1 | 2 |
| 41 | u_mes_prod_ppeItem | Entity | master | 9 | 9 | 1 | 2 |
| 42 | u_mes_prod_market | Entity | master | 9 | 9 | 1 | 2 |
| 43 | u_mes_prod_padCompound | Entity | master | 9 | 9 | 1 | 2 |
| 44 | u_mes_prod_surfaceFinish | Entity | master | 9 | 9 | 1 | 2 |
| 45 | u_mes_prod_vehicleModel | Entity | master | 13 | 10 | 1 | 3 |
| 46 | u_mes_prod_recipeProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
| 47 | u_mes_prod_recipeControlledDocument | Relationship | master | 11 | 11 | 1 | 2 |
| 48 | u_mes_prod_workInstructionWorkCenter | Relationship | master | 10 | 10 | 0 | 2 |
| 49 | u_mes_prod_workInstructionProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
