# Product definition (prd) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prd_item | Entity | master | 35 | 24 | 3 | 7 |
| 2 | u_mes_prd_itemRevision | Child | master | 13 | 13 | 0 | 2 |
| 3 | u_mes_prd_itemCustomerPart | Child | master | 12 | 12 | 0 | 2 |
| 4 | u_mes_prd_productVariant | Entity | master | 28 | 14 | 2 | 7 |
| 5 | u_mes_prd_billOfMaterial | Entity | master | 22 | 16 | 2 | 5 |
| 6 | u_mes_prd_billOfMaterialComponent | Child | master | 20 | 15 | 1 | 4 |
| 7 | u_mes_prd_billOfMaterialComponentProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
| 8 | u_mes_prd_billOfMaterialComponentAlternateItem | Relationship | master | 10 | 10 | 0 | 2 |
| 9 | u_mes_prd_operation | Entity | master | 21 | 20 | 3 | 3 |
| 10 | u_mes_prd_operationRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 11 | u_mes_prd_routing | Entity | master | 23 | 15 | 2 | 5 |
| 12 | u_mes_prd_routingStep | Child | master | 19 | 15 | 0 | 3 |
| 13 | u_mes_prd_routingStepAlternateWorkCenter | Relationship | master | 10 | 10 | 0 | 2 |
| 14 | u_mes_prd_routingStepNextStep | Child | master | 9 | 9 | 1 | 1 |
| 15 | u_mes_prd_billOfProcess | Entity | master | 19 | 13 | 1 | 5 |
| 16 | u_mes_prd_billOfProcessStep | Child | master | 18 | 12 | 0 | 4 |
| 17 | u_mes_prd_billOfProcessStepEquipment | Relationship | master | 10 | 10 | 0 | 2 |
| 18 | u_mes_prd_billOfProcessStepTool | Relationship | master | 10 | 10 | 0 | 2 |
| 19 | u_mes_prd_billOfProcessStepRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 20 | u_mes_prd_billOfProcessStepConsumedComponent | Child | master | 12 | 12 | 0 | 2 |
| 21 | u_mes_prd_billOfProcessStepInterlock | Child | master | 11 | 11 | 1 | 1 |
| 22 | u_mes_prd_billOfProcessStepProcessParameter | Child | master | 14 | 12 | 0 | 2 |
| 23 | u_mes_prd_workInstruction | Entity | master | 25 | 18 | 1 | 7 |
| 24 | u_mes_prd_workInstructionStep | Child | master | 18 | 14 | 1 | 1 |
| 25 | u_mes_prd_workInstructionStepMediaControlledDocument | Relationship | master | 10 | 10 | 0 | 2 |
| 26 | u_mes_prd_workInstructionStepProductVariant | Relationship | master | 10 | 10 | 0 | 2 |
| 27 | u_mes_prd_workInstructionStepTool | Relationship | master | 10 | 10 | 0 | 2 |
| 28 | u_mes_prd_workInstructionStepCharacteristic | Relationship | master | 10 | 10 | 0 | 2 |
| 29 | u_mes_prd_workInstructionPpeItem | Relationship | master | 10 | 10 | 0 | 2 |
| 30 | u_mes_prd_workInstructionKeyPoint | Value list | master | 9 | 9 | 0 | 1 |
| 31 | u_mes_prd_recipe | Entity | master | 25 | 16 | 2 | 6 |
| 32 | u_mes_prd_recipeParameter | Child | master | 18 | 14 | 0 | 3 |
| 33 | u_mes_prd_recipeStage | Child | master | 11 | 11 | 0 | 1 |
| 34 | u_mes_prd_engineeringChange | Entity | transaction | 31 | 23 | 4 | 5 |
| 35 | u_mes_prd_engineeringChangeAffectedItem | Child | transaction | 18 | 18 | 0 | 2 |
| 36 | u_mes_prd_engineeringChangeAffectedObject | Child | transaction | 18 | 18 | 1 | 1 |
| 37 | u_mes_prd_engineeringChangeApproval | Child | transaction | 20 | 18 | 2 | 2 |
| 38 | u_mes_prd_engineeringChangeControlledDocument | Relationship | transaction | 16 | 16 | 0 | 2 |
| 39 | u_mes_prd_itemGroup | Entity | master | 9 | 9 | 1 | 2 |
| 40 | u_mes_prd_itemFamily | Entity | master | 9 | 9 | 1 | 2 |
| 41 | u_mes_prd_ppeItem | Entity | master | 9 | 9 | 1 | 2 |
| 42 | u_mes_prd_market | Entity | master | 9 | 9 | 1 | 2 |
| 43 | u_mes_prd_padCompound | Entity | master | 9 | 9 | 1 | 2 |
| 44 | u_mes_prd_surfaceFinish | Entity | master | 9 | 9 | 1 | 2 |
| 45 | u_mes_prd_vehicleModel | Entity | master | 13 | 10 | 1 | 3 |
