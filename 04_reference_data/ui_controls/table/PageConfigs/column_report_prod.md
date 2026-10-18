## u_mes_prod_billOfMaterial - Bills of Material (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfMaterial.json | _id: mes_prod_billOfMaterialStable | rel: CL20261018-23:51 | samples: 20 | columns: 14 | total width: 2160px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | bomVersion | BOM Version | Int32 | 1 | 120px | right |
| 5 | bomType | BOM Type | String | 10 | 100px | left |
| 6 | baseQuantity | Base Quantity | Decimal128 | 1 | 140px | right |
| 7 | baseUnitOfMeasureName | Base Unit of Measure | String | 4 | 180px | left |
| 8 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 9 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 10 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 11 | approvedBy | Approved By | String | 0 | 120px | left |
| 12 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 13 | erpBomNo | ERP BOM No | String | 11 | 110px | left |
| 14 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); baseUnitOfMeasureId (reference key, shown through baseUnitOfMeasureName); engineeringChangeId (reference key, shown through engineeringChangeName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_prod_billOfMaterialComponent - BOM Components (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfMaterialComponent.json | _id: mes_prod_billOfMaterialComponentStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 1880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | billOfMaterialName | Bill of Material | String | 21 | 170px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | componentItemName | Component Item | String | 61 | 300px | left |
| 5 | quantity | Quantity | Decimal128 | 7 | 100px | right |
| 6 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 7 | scrapPct | Scrap (%) | Decimal128 | 3 | 110px | right |
| 8 | operationName | Operation | String | 31 | 240px | left |
| 9 | isTraceable | Traceable | Boolean | 3 | 110px | center |
| 10 | traceLevel | Trace Level | String | 3 | 120px | left |
| 11 | backflush | Backflush | Boolean | 3 | 110px | center |
| 12 | referenceDesignator | Reference Designator | String | 2 | 180px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfMaterialId (reference key, shown through billOfMaterialName); componentItemId (reference key, shown through componentItemName); unitOfMeasureId (reference key, shown through unitOfMeasureName); operationId (reference key, shown through operationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfMaterialComponentAlternateItem - BOM Component Alternate Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfMaterialComponentAlternateItem.json | _id: mes_prod_billOfMaterialComponentAlternateItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 30 | 230px | left |
| 2 | billOfMaterialComponentName | Bill of Material Component | String | 25 | 230px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | alternateItemName | Alternate Item | String | 61 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfMaterialComponentId (reference key, shown through billOfMaterialComponentName); alternateItemId (reference key, shown through alternateItemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfMaterialComponentProductVariant - BOM Component Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfMaterialComponentProductVariant.json | _id: mes_prod_billOfMaterialComponentProductVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 30 | 230px | left |
| 2 | billOfMaterialComponentName | Bill of Material Component | String | 25 | 230px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productVariantName | Product Variant | String | 44 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfMaterialComponentId (reference key, shown through billOfMaterialComponentName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcess - Bills of Process (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcess.json | _id: mes_prod_billOfProcessStable | rel: CL20261018-23:51 | samples: 20 | columns: 11 | total width: 1810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | routingName | Routing | String | 64 | 300px | left |
| 5 | bopVersion | Bop Version | Int32 | 1 | 120px | right |
| 6 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 7 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 8 | billOfMaterialName | Bill of Material | String | 21 | 170px | left |
| 9 | approvedBy | Approved By | String | 0 | 120px | left |
| 10 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 11 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); routingId (reference key, shown through routingName); billOfMaterialId (reference key, shown through billOfMaterialName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_prod_billOfProcessStep - BOP Steps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStep.json | _id: mes_prod_billOfProcessStepStable | rel: CL20261018-23:51 | samples: 20 | columns: 9 | total width: 1830px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | billOfProcessName | Bill of Process | String | 21 | 170px | left |
| 3 | stepNo | Step No | Int32 | 3 | 90px | right |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | recipeName | Recipe | String | 56 | 300px | left |
| 6 | workInstructionName | Work Instruction | String | 65 | 300px | left |
| 7 | inspectionPlanName | Inspection Plan | String | 54 | 300px | left |
| 8 | cycleTimeSec | Cycle Time (s) | Decimal128 | 7 | 140px | right |
| 9 | manning | Manning | Int32 | 1 | 90px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessId (reference key, shown through billOfProcessName); operationId (reference key, shown through operationName); recipeId (reference key, shown through recipeName); workInstructionId (reference key, shown through workInstructionName); inspectionPlanId (reference key, shown through inspectionPlanName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepConsumedComponent - BOP Step Consumed Components (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepConsumedComponent.json | _id: mes_prod_billOfProcessStepConsumedComponentStable | rel: CL20261018-23:51 | samples: 20 | columns: 6 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 30 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 6 | verifyByScan | Verify By Scan | Boolean | 3 | 140px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepEquipment - BOP Step Equipment (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepEquipment.json | _id: mes_prod_billOfProcessStepEquipmentStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 29 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | equipmentName | Equipment | String | 54 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); equipmentId (reference key, shown through equipmentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepInterlock - BOP Step Interlocks (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepInterlock.json | _id: mes_prod_billOfProcessStepInterlockStable | rel: CL20261018-23:51 | samples: 20 | columns: 6 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 29 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | interlockType | Interlock Type | String | 17 | 140px | left |
| 5 | description | Description | String | 77 | 300px | left |
| 6 | enforced | Enforced | Boolean | 3 | 100px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepProcessParameter - BOP Step Process Parameters (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepProcessParameter.json | _id: mes_prod_billOfProcessStepProcessParameterStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1330px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 30 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 46 | 300px | left |
| 5 | nominal | Nominal | Decimal128 | 7 | 90px | right |
| 6 | lowerLimit | Lower Limit | Decimal128 | 7 | 120px | right |
| 7 | upperLimit | Upper Limit | Decimal128 | 7 | 120px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 14 | 150px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepRequiredSkill - BOP Step Required Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepRequiredSkill.json | _id: mes_prod_billOfProcessStepRequiredSkillStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 30 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | requiredSkillName | Required Skill | String | 45 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); requiredSkillId (reference key, shown through requiredSkillName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_billOfProcessStepTool - BOP Step Tools (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_billOfProcessStepTool.json | _id: mes_prod_billOfProcessStepToolStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 29 | 230px | left |
| 2 | billOfProcessStepName | Bill of Process Step | String | 25 | 200px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | toolName | Tool | String | 46 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billOfProcessStepId (reference key, shown through billOfProcessStepName); toolId (reference key, shown through toolName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_engineeringChange - Engineering Changes (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_engineeringChange.json | _id: mes_prod_engineeringChangeStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4600px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | title | Title | String | 61 | 300px | left |
| 3 | description | Description | String | 134 | 300px | left |
| 4 | changeType | Change Type | String | 15 | 130px | left |
| 5 | reasonCodeText | Reason Code Text | String | 57 | 300px | left |
| 6 | originator | Originator | String | 8 | 110px | left |
| 7 | customerName | Customer | String | 42 | 300px | left |
| 8 | customerChangeRef | Customer Change Ref | String | 16 | 180px | left |
| 9 | raisedBy | Raised By | String | 14 | 120px | left |
| 10 | raisedAt | Raised At | Date/Datetime | 19 | 160px | center |
| 11 | effectivityType | Effectivity Type | String | 4 | 160px | left |
| 12 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 13 | cutInSerialNo | Cut in Serial No | String | 13 | 160px | left |
| 14 | stockDispositionTypeName | Stock Disposition Type | String | 24 | 200px | left |
| 15 | ppapRequired | Ppap Required | Boolean | 3 | 140px | center |
| 16 | implementedAt | Implemented At | Date/Datetime | 19 | 160px | center |
| 17 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 18 | gmpImpact | GMP Impact | Boolean | 3 | 110px | center |
| 19 | validationRequired | Validation Required | Boolean | 3 | 180px | center |
| 20 | regulatoryImpact | Regulatory Impact | String | 21 | 170px | left |
| 21 | riskAssessmentName | Risk Assessment | String | 62 | 300px | left |
| 22 | status | Status | String | 16 | 140px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); raisedById (reference key, shown through raisedBy); stockDispositionTypeId (reference key, shown through stockDispositionTypeName); riskAssessmentId (reference key, shown through riskAssessmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_prod_engineeringChangeAffectedItem - Engineering Change Affected Items (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_engineeringChangeAffectedItem.json | _id: mes_prod_engineeringChangeAffectedItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | fromRevision | From Revision | String | 1 | 140px | left |
| 6 | toRevision | To Revision | String | 1 | 120px | left |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); engineeringChangeId (reference key, shown through engineeringChangeName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_prod_engineeringChangeAffectedObject - Engineering Change Affected Objects (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_engineeringChangeAffectedObject.json | _id: mes_prod_engineeringChangeAffectedObjectStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | relatedCollectionName | Related Collection Name | String | 18 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 64 | 300px | left |
| 6 | changeAction | Change Action | String | 6 | 140px | left |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); engineeringChangeId (reference key, shown through engineeringChangeName); relatedEntityId (reference key, shown through relatedEntityName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_prod_engineeringChangeApproval - Engineering Change Approvals (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_engineeringChangeApproval.json | _id: mes_prod_engineeringChangeApprovalStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 2020px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | engineeringChangeName | Engineering Change | String | 49 | 300px | left |
| 3 | stepNo | Step No | Int32 | 3 | 90px | right |
| 4 | businessFunction | Business Function | String | 7 | 160px | left |
| 5 | userName | User | String | 14 | 120px | left |
| 6 | decision | Decision | String | 24 | 190px | left |
| 7 | decidedAt | Decided At | Date/Datetime | 19 | 160px | center |
| 8 | comment | Comment | String | 58 | 300px | left |
| 9 | createdBy | Created By | String | 14 | 120px | left |
| 10 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 11 | updatedBy | Updated By | String | 14 | 120px | left |
| 12 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); engineeringChangeId (reference key, shown through engineeringChangeName); userId (reference key, shown through userName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_prod_engineeringChangeControlledDocument - Engineering Change Documents (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_engineeringChangeControlledDocument.json | _id: mes_prod_engineeringChangeControlledDocumentStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1430px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | controlledDocumentName | Controlled Document | String | 78 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); engineeringChangeId (reference key, shown through engineeringChangeName); controlledDocumentId (reference key, shown through controlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_prod_item - Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_item.json | _id: mes_prod_itemStable | rel: CL20261018-23:51 | samples: 20 | columns: 28 | total width: 5000px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | description | Description | String | 61 | 300px | left |
| 3 | itemType | Item Type | String | 19 | 160px | left |
| 4 | itemGroupName | Item Group | String | 22 | 180px | left |
| 5 | baseUnitOfMeasureName | Base Unit of Measure | String | 8 | 180px | left |
| 6 | drawingNo | Drawing No | String | 19 | 160px | left |
| 7 | drawingRevision | Drawing Revision | String | 1 | 160px | left |
| 8 | revisionDate | Revision Date | Date/Date | 10 | 140px | center |
| 9 | materialSpecification | Material Specification | String | 46 | 300px | left |
| 10 | materialGrade | Material Grade | String | 23 | 190px | left |
| 11 | netWeightKg | Net Weight Kg | Decimal128 | 5 | 140px | right |
| 12 | grossWeightKg | Gross Weight Kg | Decimal128 | 5 | 150px | right |
| 13 | procurementType | Procurement Type | String | 9 | 160px | left |
| 14 | defaultSupplierName | Default Supplier | String | 44 | 300px | left |
| 15 | isSerialised | Serialised | Boolean | 3 | 110px | center |
| 16 | isLotControlled | Lot Controlled | Boolean | 3 | 140px | center |
| 17 | serialNumberRangeName | Serial Number Range | String | 33 | 260px | left |
| 18 | lotNumberRangeName | Lot Number Range | String | 33 | 260px | left |
| 19 | shelfLifeDays | Shelf Life (days) | Int32 | 4 | 160px | right |
| 20 | safetyCharacteristic | Safety Characteristic | Boolean | 3 | 190px | center |
| 21 | hsnCode | Hsn Code | String | 8 | 100px | left |
| 22 | standardCostInr | Standard Cost (INR) | Decimal128 | 6 | 180px | right |
| 23 | erpMaterialNo | ERP Material No | String | 18 | 150px | left |
| 24 | defaultStorageLocationName | Default Storage Location | String | 32 | 250px | left |
| 25 | fefoRequired | Fefo Required | Boolean | 3 | 140px | center |
| 26 | exposureControlled | Exposure Controlled | Boolean | 3 | 180px | center |
| 27 | openLifeMinutes | Open Life (min) | Int32 | 3 | 150px | right |
| 28 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemGroupId (reference key, shown through itemGroupName); baseUnitOfMeasureId (reference key, shown through baseUnitOfMeasureName); defaultSupplierId (reference key, shown through defaultSupplierName); serialNumberRangeId (reference key, shown through serialNumberRangeName); lotNumberRangeId (reference key, shown through lotNumberRangeName); defaultStorageLocationId (reference key, shown through defaultStorageLocationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_itemCustomerPart - Item Customer Parts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_itemCustomerPart.json | _id: mes_prod_itemCustomerPartStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 1070px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | itemName | Item | String | 39 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | customerName | Customer | String | 23 | 190px | left |
| 5 | customerPartNo | Customer Part No | String | 15 | 160px | left |
| 6 | customerRevision | Customer Revision | String | 2 | 160px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_itemFamily - Item Families (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_itemFamily.json | _id: mes_prod_itemFamilyStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 30 | 230px | left |
| 3 | description | Description | String | 46 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_itemGroup - Item Groups (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_itemGroup.json | _id: mes_prod_itemGroupStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 750px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 22 | 180px | left |
| 3 | description | Description | String | 32 | 250px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_itemRevision - Item Revisions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_itemRevision.json | _id: mes_prod_itemRevisionStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1360px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | revision | Revision | String | 1 | 100px | left |
| 5 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 6 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 7 | description | Description | String | 32 | 250px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); engineeringChangeId (reference key, shown through engineeringChangeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_market - Markets (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_market.json | _id: mes_prod_marketStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 29 | 230px | left |
| 3 | description | Description | String | 39 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_operation - Operations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_operation.json | _id: mes_prod_operationStable | rel: CL20261018-23:51 | samples: 20 | columns: 16 | total width: 2870px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 5 | 110px | left |
| 2 | name | Name | String | 31 | 240px | left |
| 3 | operationType | Operation Type | String | 17 | 140px | left |
| 4 | description | Description | String | 55 | 300px | left |
| 5 | defaultWorkCenterName | Default Work Center | String | 37 | 280px | left |
| 6 | trackingGrain | Tracking Grain | String | 4 | 140px | left |
| 7 | standardCycleTimeSec | Standard Cycle Time (s) | Decimal128 | 7 | 210px | right |
| 8 | standardSetupTimeMin | Standard Setup Time Min | Int32 | 2 | 210px | right |
| 9 | standardManning | Standard Manning | Int32 | 1 | 160px | right |
| 10 | isInspection | Inspection | Boolean | 3 | 110px | center |
| 11 | isSpecialProcess | Special Process | Boolean | 3 | 150px | center |
| 12 | specialProcessStandard | Special Process Standard | String | 6 | 210px | left |
| 13 | requiresFirstOffApproval | Requires First Off Approval | Boolean | 3 | 230px | center |
| 14 | erpControlKey | ERP Control Key | String | 4 | 150px | left |
| 15 | sequenceHint | Sequence Hint | Int32 | 3 | 140px | right |
| 16 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); defaultWorkCenterId (reference key, shown through defaultWorkCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_operationRequiredSkill - Operation Required Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_operationRequiredSkill.json | _id: mes_prod_operationRequiredSkillStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 670px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | operationName | Operation | String | 24 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | requiredSkillName | Required Skill | String | 32 | 250px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operationId (reference key, shown through operationName); requiredSkillId (reference key, shown through requiredSkillName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_padCompound - Pad Compounds (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_padCompound.json | _id: mes_prod_padCompoundStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 24 | 190px | left |
| 3 | description | Description | String | 34 | 260px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_ppeItem - PPE Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_ppeItem.json | _id: mes_prod_ppeItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | name | Name | String | 32 | 250px | left |
| 3 | description | Description | String | 39 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_productVariant - Product Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_productVariant.json | _id: mes_prod_productVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 3240px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | name | Name | String | 52 | 300px | left |
| 3 | baseItemName | Base Item | String | 49 | 300px | left |
| 4 | variantItemName | Variant Item | String | 49 | 300px | left |
| 5 | customerName | Customer | String | 42 | 300px | left |
| 6 | optionsHand | Options Hand | String | 2 | 130px | left |
| 7 | optionsPistonDiameterMm | Options Piston Diameter (mm) | Decimal128 | 4 | 240px | right |
| 8 | optionsPadCompoundName | Options Pad Compound | String | 24 | 190px | left |
| 9 | optionsMarketName | Options Market | String | 29 | 230px | left |
| 10 | optionsSurfaceFinishName | Options Surface Finish | String | 20 | 200px | left |
| 11 | optionsColour | Options Colour | String | 6 | 140px | left |
| 12 | vehicleModelName | Vehicle Model | String | 22 | 180px | left |
| 13 | modelYear | Model Year | Int32 | 4 | 110px | right |
| 14 | labelSuffix | Label Suffix | String | 1 | 130px | left |
| 15 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 16 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 17 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); baseItemId (reference key, shown through baseItemName); variantItemId (reference key, shown through variantItemName); customerId (reference key, shown through customerName); optionsPadCompoundId (reference key, shown through optionsPadCompoundName); optionsMarketId (reference key, shown through optionsMarketName); optionsSurfaceFinishId (reference key, shown through optionsSurfaceFinishName); vehicleModelId (reference key, shown through vehicleModelName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_recipe - Recipes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_recipe.json | _id: mes_prod_recipeStable | rel: CL20261018-23:51 | samples: 20 | columns: 24 | total width: 4470px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | name | Name | String | 56 | 300px | left |
| 3 | equipmentName | Equipment | String | 54 | 300px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | operationName | Operation | String | 31 | 240px | left |
| 6 | version | Version | Int32 | 1 | 90px | right |
| 7 | recipeType | Recipe Type | String | 22 | 180px | left |
| 8 | programNo | Program No | String | 12 | 110px | left |
| 9 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 10 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 11 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 12 | checksum | Checksum | String | 16 | 140px | left |
| 13 | approvedBy | Approved By | String | 0 | 120px | left |
| 14 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 15 | lastDownloadedAt | Last Downloaded At | Date/Datetime | 0 | 170px | center |
| 16 | previousVersionRecipeName | Previous Version Recipe | String | 0 | 210px | left |
| 17 | changeReasonText | Change Reason Text | String | 82 | 300px | left |
| 18 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 19 | isGoldenRecipe | Golden Recipe | Boolean | 3 | 140px | center |
| 20 | goldenDesignatedAt | Golden Designated At | Date/Datetime | 19 | 180px | center |
| 21 | goldenDesignatedBy | Golden Designated By | String | 15 | 180px | left |
| 22 | origin | Origin | String | 18 | 150px | left |
| 23 | analyticsModelName | Analytics Model | String | 35 | 270px | left |
| 24 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); itemId (reference key, shown through itemName); operationId (reference key, shown through operationName); engineeringChangeId (reference key, shown through engineeringChangeName); approvedById (reference key, shown through approvedBy); previousVersionRecipeId (reference key, shown through previousVersionRecipeName); goldenDesignatedById (reference key, shown through goldenDesignatedBy); analyticsModelId (reference key, shown through analyticsModelName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt, lastDownloadedAt, previousVersionRecipeName

## u_mes_prod_recipeControlledDocument - Recipe Reference Files (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_recipeControlledDocument.json | _id: mes_prod_recipeControlledDocumentStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 1080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | recipeName | Recipe | String | 56 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | controlledDocumentName | Controlled Document | String | 78 | 300px | left |
| 5 | fileRole | File Role | String | 21 | 170px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); recipeId (reference key, shown through recipeName); controlledDocumentId (reference key, shown through controlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_recipeParameter - Recipe Parameters (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_recipeParameter.json | _id: mes_prod_recipeParameterStable | rel: CL20261018-23:51 | samples: 20 | columns: 11 | total width: 2000px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | recipeName | Recipe | String | 51 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 46 | 300px | left |
| 5 | processTagName | Process Tag | String | 46 | 300px | left |
| 6 | setPoint | Set Point | Decimal128 | 7 | 110px | right |
| 7 | lowerLimit | Lower Limit | Decimal128 | 7 | 120px | right |
| 8 | upperLimit | Upper Limit | Decimal128 | 7 | 120px | right |
| 9 | unitOfMeasureName | Unit of Measure | String | 14 | 150px | left |
| 10 | isCritical | Critical | Boolean | 3 | 100px | center |
| 11 | downloadToController | Download to Controller | Boolean | 3 | 200px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); recipeId (reference key, shown through recipeName); processTagId (reference key, shown through processTagName); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_recipeProductVariant - Recipe Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_recipeProductVariant.json | _id: mes_prod_recipeProductVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | recipeName | Recipe | String | 56 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productVariantName | Product Variant | String | 49 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); recipeId (reference key, shown through recipeName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_recipeStage - Recipe Stages (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_recipeStage.json | _id: mes_prod_recipeStageStable | rel: CL20261018-23:51 | samples: 20 | columns: 6 | total width: 900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | recipeName | Recipe | String | 51 | 300px | left |
| 3 | stageNo | Stage No | Int32 | 1 | 100px | right |
| 4 | name | Name | String | 8 | 80px | left |
| 5 | durationSec | Duration (s) | Int32 | 2 | 130px | right |
| 6 | setPoint | Set Point | Decimal128 | 7 | 110px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); recipeId (reference key, shown through recipeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_routing - Routings (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_routing.json | _id: mes_prod_routingStable | rel: CL20261018-23:51 | samples: 20 | columns: 15 | total width: 2520px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | routingVersion | Routing Version | Int32 | 1 | 150px | right |
| 5 | routingType | Routing Type | String | 9 | 130px | left |
| 6 | description | Description | String | 64 | 300px | left |
| 7 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 8 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 9 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 10 | entryStepNo | Entry Step No | Int32 | 2 | 140px | right |
| 11 | parentRoutingName | Parent Routing | String | 0 | 140px | left |
| 12 | approvedBy | Approved By | String | 0 | 120px | left |
| 13 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 14 | erpRoutingNo | ERP Routing No | String | 11 | 140px | left |
| 15 | status | Status | String | 14 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); engineeringChangeId (reference key, shown through engineeringChangeName); parentRoutingId (reference key, shown through parentRoutingName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentRoutingName, approvedBy, approvedAt

## u_mes_prod_routingStep - Routing Steps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_routingStep.json | _id: mes_prod_routingStepStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 2090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | routingName | Routing | String | 48 | 300px | left |
| 3 | stepNo | Step No | Int32 | 3 | 90px | right |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | workCenterName | Work Center | String | 37 | 280px | left |
| 6 | cycleTimeSec | Cycle Time (s) | Decimal128 | 7 | 140px | right |
| 7 | setupTimeMin | Setup Time Min | Int32 | 2 | 140px | right |
| 8 | isMilestone | Milestone | Boolean | 3 | 110px | center |
| 9 | isOptional | Optional | Boolean | 3 | 100px | center |
| 10 | reworkReturnStepNo | Rework Return Step No | Int32 | 2 | 190px | right |
| 11 | maxQueueTimeMin | Max Queue Time Min | Int32 | 3 | 170px | right |
| 12 | maxReworkCount | Max Rework Count | Int32 | 1 | 160px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); routingId (reference key, shown through routingName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_routingStepAlternateWorkCenter - Routing Step Alternate Work Centers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_routingStepAlternateWorkCenter.json | _id: mes_prod_routingStepAlternateWorkCenterStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | routingStepName | Routing Step | String | 21 | 170px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | alternateWorkCenterName | Alternate Work Center | String | 37 | 280px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); routingStepId (reference key, shown through routingStepName); alternateWorkCenterId (reference key, shown through alternateWorkCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_routingStepNextStep - Routing Step Next Steps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_routingStepNextStep.json | _id: mes_prod_routingStepNextStepStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 650px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | routingStepName | Routing Step | String | 21 | 170px | left |
| 3 | stepNo | Step No | Int32 | 2 | 90px | right |
| 4 | nextStepCondition | Next Step Condition | String | 9 | 180px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); routingStepId (reference key, shown through routingStepName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_surfaceFinish - Surface Finishes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_surfaceFinish.json | _id: mes_prod_surfaceFinishStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 20 | 160px | left |
| 3 | description | Description | String | 33 | 260px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_vehicleModel - Vehicle Models (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_vehicleModel.json | _id: mes_prod_vehicleModelStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1180px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 6 | 110px | left |
| 2 | name | Name | String | 22 | 180px | left |
| 3 | description | Description | String | 31 | 240px | left |
| 4 | customerName | Customer | String | 23 | 190px | left |
| 5 | modelYear | Model Year | Int32 | 4 | 110px | right |
| 6 | platformCode | Platform Code | String | 2 | 140px | left |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstruction - Work Instructions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstruction.json | _id: mes_prod_workInstructionStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 3360px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | title | Title | String | 65 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | version | Version | Int32 | 1 | 90px | right |
| 6 | languageName | Language | String | 7 | 100px | left |
| 7 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 8 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 9 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 10 | safetyNotes | Safety Notes | String | 64 | 300px | left |
| 11 | authorUserName | Author User | String | 14 | 120px | left |
| 12 | approvedBy | Approved By | String | 0 | 120px | left |
| 13 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 14 | readAcknowledgementRequired | Read Acknowledgement Required | Boolean | 3 | 250px | center |
| 15 | reacknowledgeOnRevision | Reacknowledge on Revision | Boolean | 3 | 220px | center |
| 16 | generationSource | Generation Source | String | 30 | 230px | left |
| 17 | sourceBillOfProcessName | Source Bill of Process | String | 21 | 200px | left |
| 18 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); operationId (reference key, shown through operationName); languageId (reference key, shown through languageName); engineeringChangeId (reference key, shown through engineeringChangeName); authorUserId (reference key, shown through authorUserName); approvedById (reference key, shown through approvedBy); sourceBillOfProcessId (reference key, shown through sourceBillOfProcessName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_prod_workInstructionKeyPoint - Work Instruction Key Points (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionKeyPoint.json | _id: mes_prod_workInstructionKeyPointStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | workInstructionName | Work Instruction | String | 64 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | keyPoint | Key Point | String | 77 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionId (reference key, shown through workInstructionName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionPpeItem - Work Instruction PPE Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionPpeItem.json | _id: mes_prod_workInstructionPpeItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | workInstructionName | Work Instruction | String | 65 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | ppeItemName | PPE Item | String | 32 | 250px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionId (reference key, shown through workInstructionName); ppeItemId (reference key, shown through ppeItemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionProductVariant - Work Instruction Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionProductVariant.json | _id: mes_prod_workInstructionProductVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | workInstructionName | Work Instruction | String | 65 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productVariantName | Product Variant | String | 49 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionId (reference key, shown through workInstructionName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionStep - Work Instruction Steps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionStep.json | _id: mes_prod_workInstructionStepStable | rel: CL20261018-23:51 | samples: 20 | columns: 15 | total width: 2720px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | workInstructionName | Work Instruction | String | 64 | 300px | left |
| 3 | stepNo | Step No | Int32 | 2 | 90px | right |
| 4 | title | Title | String | 129 | 300px | left |
| 5 | instructionText | Instruction Text | String | 129 | 300px | left |
| 6 | inputType | Input Type | String | 4 | 110px | left |
| 7 | expectedValue | Expected Value | Decimal128 | 7 | 140px | right |
| 8 | lowerLimit | Lower Limit | Decimal128 | 7 | 120px | right |
| 9 | upperLimit | Upper Limit | Decimal128 | 7 | 120px | right |
| 10 | isMandatory | Mandatory | Boolean | 3 | 110px | center |
| 11 | requiresScan | Requires Scan | Boolean | 3 | 140px | center |
| 12 | caution | Caution | String | 67 | 300px | left |
| 13 | standardTimeSec | Standard Time (s) | Decimal128 | 4 | 160px | right |
| 14 | arContentControlledDocumentName | Ar Content Controlled Document | String | 0 | 250px | left |
| 15 | arAnchorRef | Ar Anchor Ref | String | 0 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionId (reference key, shown through workInstructionName); arContentControlledDocumentId (reference key, shown through arContentControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): arContentControlledDocumentName, arAnchorRef

## u_mes_prod_workInstructionStepCharacteristic - Work Instruction Step Characteristics (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionStepCharacteristic.json | _id: mes_prod_workInstructionStepCharacteristicStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | workInstructionStepName | Work Instruction Step | String | 16 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | characteristicName | Characteristic | String | 45 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionStepId (reference key, shown through workInstructionStepName); characteristicId (reference key, shown through characteristicName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionStepMediaControlledDocument - Work Instruction Step Media (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionStepMediaControlledDocument.json | _id: mes_prod_workInstructionStepMediaControlledDocumentStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | workInstructionStepName | Work Instruction Step | String | 16 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | mediaControlledDocumentName | Media Controlled Document | String | 78 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionStepId (reference key, shown through workInstructionStepName); mediaControlledDocumentId (reference key, shown through mediaControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionStepProductVariant - Work Instruction Step Product Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionStepProductVariant.json | _id: mes_prod_workInstructionStepProductVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | workInstructionStepName | Work Instruction Step | String | 16 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productVariantName | Product Variant | String | 44 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionStepId (reference key, shown through workInstructionStepName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionStepTool - Work Instruction Step Tools (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionStepTool.json | _id: mes_prod_workInstructionStepToolStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | workInstructionStepName | Work Instruction Step | String | 16 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | toolName | Tool | String | 43 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionStepId (reference key, shown through workInstructionStepName); toolId (reference key, shown through toolName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_prod_workInstructionWorkCenter - Work Instruction Stations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_prod_workInstructionWorkCenter.json | _id: mes_prod_workInstructionWorkCenterStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 840px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | workInstructionName | Work Instruction | String | 65 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | workCenterName | Work Center | String | 37 | 280px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workInstructionId (reference key, shown through workInstructionName); workCenterId (reference key, shown through workCenterName); schemaVersion (excluded key (identifier, site, app or schema))
