# Field list - Quality Management (qual)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/06_quality_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_qual_characteristic

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | characteristicType | String | - |  |
| 11 | classification | String | - |  |
| 12 | drawingZone | String | - |  |
| 13 | balloonNo | String | - |  |
| 14 | dataType | String | - |  |
| 15 | nominal | Decimal128 | - |  |
| 16 | lowerSpecLimit | Decimal128 | - |  |
| 17 | upperSpecLimit | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | toleranceType | String | - |  |
| 21 | measurementMethod | String | - |  |
| 22 | gaugeId | String | - | u_mes_qual_gauge._id |
| 23 | gaugeName | String | - |  |
| 24 | gaugeTypeId | String | - | u_mes_qual_gaugeType._id |
| 25 | gaugeTypeName | String | - |  |
| 26 | attributeAcceptance | String | - |  |
| 27 | isSpc | Boolean | - |  |
| 28 | targetCpk | Decimal128 | - |  |
| 29 | reactionPlan | String | - |  |
| 30 | source | String | - |  |
| 31 | positionCount | Int32 | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlan

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
| 8 | phase | String | - |  |
| 9 | version | Int32 | - |  |
| 10 | routingId | String | - | u_mes_prod_routing._id |
| 11 | routingName | String | - |  |
| 12 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 13 | pfmeaName | String | - |  |
| 14 | customerApprovalDate | Date | Date |  |
| 15 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | - |  |
| 17 | preparedById | String | - | u_mes_mast_user._id |
| 18 | preparedBy | String | - |  |
| 19 | approvedById | String | - | u_mes_mast_user._id |
| 20 | approvedBy | String | - |  |
| 21 | approvedAt | Date | Datetime |  |
| 22 | effectiveFrom | Date | Date |  |
| 23 | originalDate | Date | Date |  |
| 24 | revisionDate | Date | Date |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlanCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qual_controlPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 6 | controlPlanName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | coreTeamUserId | String | - | u_mes_mast_user._id |
| 9 | coreTeamUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlanLine

Kind: child | Data class: master | Parent: u_mes_qual_controlPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 6 | controlPlanName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | processName | String | - |  |
| 11 | equipmentText | String | - |  |
| 12 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 13 | characteristicName | String | - |  |
| 14 | classification | String | - |  |
| 15 | specification | String | - |  |
| 16 | gaugeId | String | - | u_mes_qual_gauge._id |
| 17 | gaugeName | String | - |  |
| 18 | measurementTechnique | String | - |  |
| 19 | sampleSize | Int32 | - |  |
| 20 | sampleFrequency | String | - |  |
| 21 | controlMethod | String | - |  |
| 22 | reactionPlan | String | - |  |
| 23 | responsible | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 7 | controlPlanName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | operationId | String | - | u_mes_prod_operation._id |
| 11 | operationName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | planType | String | - |  |
| 15 | version | Int32 | - |  |
| 16 | collectionTrigger | String | - |  |
| 17 | samplingPlanId | String | - | u_mes_qual_samplingPlan._id |
| 18 | samplingPlanName | String | - |  |
| 19 | blockOnFail | Boolean | - |  |
| 20 | effectiveFrom | Date | Date |  |
| 21 | effectiveTo | Date | Date |  |
| 22 | approvedById | String | - | u_mes_mast_user._id |
| 23 | approvedBy | String | - |  |
| 24 | approvedAt | Date | Datetime |  |
| 25 | itemRevision | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlanLine

Kind: child | Data class: master | Parent: u_mes_qual_inspectionPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 6 | inspectionPlanName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | gaugeId | String | - | u_mes_qual_gauge._id |
| 11 | gaugeName | String | - |  |
| 12 | sampleSize | Int32 | - |  |
| 13 | frequencyType | String | - |  |
| 14 | frequencyValue | Decimal128 | - |  |
| 15 | recordType | String | - |  |
| 16 | autoNcOnFail | Boolean | - |  |
| 17 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 18 | defectCodeName | String | - |  |
| 19 | overrideAllowed | Boolean | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_qual_samplingPlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | samplingType | String | - |  |
| 7 | standard | String | - |  |
| 8 | inspectionLevel | String | - |  |
| 9 | aql | Decimal128 | - |  |
| 10 | frequencyType | String | - |  |
| 11 | frequencyEveryNUnits | Int32 | - |  |
| 12 | frequencyEveryMinutes | Int32 | - |  |
| 13 | skipLotEnabled | Boolean | - |  |
| 14 | skipLotConsecutiveAcceptedToSkip | Int32 | - |  |
| 15 | skipLotSkipFraction | Decimal128 | - |  |
| 16 | switchingRules | String | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_qual_samplingPlanSizeRow

Kind: child | Data class: master | Parent: u_mes_qual_samplingPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | samplingPlanId | String | - | u_mes_qual_samplingPlan._id |
| 6 | samplingPlanName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | lotSizeFrom | Int32 | - |  |
| 9 | lotSizeTo | Int32 | - |  |
| 10 | sampleSize | Int32 | - |  |
| 11 | acceptNumber | Int32 | - |  |
| 12 | rejectNumber | Int32 | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheet

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | checkSheetType | String | - |  |
| 7 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | operationId | String | - | u_mes_prod_operation._id |
| 12 | operationName | String | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | version | Int32 | - |  |
| 16 | frequency | String | - |  |
| 17 | masterSampleRequired | Boolean | - |  |
| 18 | estimatedMinutes | Int32 | - |  |
| 19 | effectiveFrom | Date | Date |  |
| 20 | approvedById | String | - | u_mes_mast_user._id |
| 21 | approvedBy | String | - |  |
| 22 | approvedAt | Date | Datetime |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheetItem

Kind: child | Data class: master | Parent: u_mes_qual_checkSheet | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 6 | checkSheetName | String | - |  |
| 7 | itemNo | Int32 | - |  |
| 8 | question | String | - |  |
| 9 | answerType | String | - |  |
| 10 | expectedAnswer | String | - |  |
| 11 | lowerLimit | Decimal128 | - |  |
| 12 | upperLimit | Decimal128 | - |  |
| 13 | unitText | String | - |  |
| 14 | isCritical | Boolean | - |  |
| 15 | reactionOnFail | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheetResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 6 | checkSheetName | String | - |  |
| 7 | checkSheetVersion | Int32 | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | shiftId | String | - | u_mes_mast_shift._id |
| 13 | shiftName | String | - |  |
| 14 | productionDate | Date | Date |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | performedById | String | - | u_mes_mast_user._id |
| 18 | performedBy | String | - |  |
| 19 | startedAt | Date | Datetime |  |
| 20 | completedAt | Date | Datetime |  |
| 21 | overallResult | String | - |  |
| 22 | failedCount | Int32 | - |  |
| 23 | reactionTaken | String | - |  |
| 24 | verifiedById | String | - | u_mes_mast_user._id |
| 25 | verifiedBy | String | - |  |
| 26 | verifiedAt | Date | Datetime |  |
| 27 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 28 | nonconformanceName | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_qual_checkSheetResultAnswer

Kind: child | Data class: transaction | Parent: u_mes_qual_checkSheetResult | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | checkSheetResultId | String | - | u_mes_qual_checkSheetResult._id |
| 6 | checkSheetResultName | String | - |  |
| 7 | itemNo | Int32 | - |  |
| 8 | answerText | String | - |  |
| 9 | answerNumber | Decimal128 | - |  |
| 10 | passed | Boolean | - |  |
| 11 | comment | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_inspectionResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 6 | inspectionPlanName | String | - |  |
| 7 | planLineNo | Int32 | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 13 | wipUnitName | String | - |  |
| 14 | lotId | String | - | u_mes_plan_lot._id |
| 15 | lotName | String | - |  |
| 16 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 17 | goodsReceiptName | String | - |  |
| 18 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 19 | operationExecutionName | String | - |  |
| 20 | operationId | String | - | u_mes_prod_operation._id |
| 21 | operationName | String | - |  |
| 22 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 23 | workCenterName | String | - |  |
| 24 | inspectionType | String | - |  |
| 25 | sampleNo | Int32 | - |  |
| 26 | measuredValue | Decimal128 | - |  |
| 27 | attributeResult | String | - |  |
| 28 | nominal | Decimal128 | - |  |
| 29 | lowerSpecLimit | Decimal128 | - |  |
| 30 | upperSpecLimit | Decimal128 | - |  |
| 31 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 32 | unitOfMeasureName | String | - |  |
| 33 | deviation | Decimal128 | - |  |
| 34 | result | String | - |  |
| 35 | gaugeId | String | - | u_mes_qual_gauge._id |
| 36 | gaugeName | String | - |  |
| 37 | measuredById | String | - | u_mes_mast_user._id |
| 38 | measuredBy | String | - |  |
| 39 | measuredAt | Date | Datetime |  |
| 40 | source | String | - |  |
| 41 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 42 | defectCodeName | String | - |  |
| 43 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 44 | nonconformanceName | String | - |  |
| 45 | overridden | Boolean | - |  |
| 46 | remarks | String | - |  |
| 47 | positionNo | Int32 | - |  |
| 48 | positionName | String | - |  |
| 49 | imageControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 50 | imageControlledDocumentName | String | - |  |
| 51 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 52 | measurementCurveName | String | - |  |
| 53 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 54 | analyticsModelName | String | - |  |
| 55 | modelVersion | String | - |  |
| 56 | modelClass | String | - |  |
| 57 | modelConfidence | Decimal128 | - |  |
| 58 | status | String | - |  |
| 59 | schemaVersion | Int32 | - |  |
| 60 | createdAt | Date | Datetime |  |
| 61 | createdById | String | - | u_mes_mast_user._id |
| 62 | createdBy | String | - |  |
| 63 | updatedAt | Date | Datetime |  |
| 64 | updatedById | String | - | u_mes_mast_user._id |
| 65 | updatedBy | String | - |  |

## u_mes_qual_spcChart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | equipmentId | String | - | u_mes_mast_equipment._id |
| 13 | equipmentName | String | - |  |
| 14 | chartType | String | - |  |
| 15 | subgroupSize | Int32 | - |  |
| 16 | subgroupFrequency | String | - |  |
| 17 | lowerSpecLimit | Decimal128 | - |  |
| 18 | upperSpecLimit | Decimal128 | - |  |
| 19 | capabilityCp | Decimal128 | - |  |
| 20 | capabilityCpk | Decimal128 | - |  |
| 21 | capabilityPp | Decimal128 | - |  |
| 22 | capabilityPpk | Decimal128 | - |  |
| 23 | capabilityCalculatedAt | Date | Datetime |  |
| 24 | capabilitySampleCount | Int32 | - |  |
| 25 | ownerUserId | String | - | u_mes_mast_user._id |
| 26 | ownerUserName | String | - |  |
| 27 | reactionPlan | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcChartControlLimit

Kind: child | Data class: master | Parent: u_mes_qual_spcChart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 6 | spcChartName | String | - |  |
| 7 | revisionNo | Int32 | - |  |
| 8 | effectiveFrom | Date | Date |  |
| 9 | ucl | Decimal128 | - |  |
| 10 | centerLine | Decimal128 | - |  |
| 11 | lcl | Decimal128 | - |  |
| 12 | uclRange | Decimal128 | - |  |
| 13 | centerLineRange | Decimal128 | - |  |
| 14 | lclRange | Decimal128 | - |  |
| 15 | basedOnSubgroups | Int32 | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcChartRule

Kind: valueList | Data class: master | Parent: u_mes_qual_spcChart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 6 | spcChartName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | rule | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcSample

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 6 | spcChartName | String | - |  |
| 7 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | subgroupNo | Int32 | - |  |
| 12 | sampledAt | Date | Datetime |  |
| 13 | sampledById | String | - | u_mes_mast_user._id |
| 14 | sampledBy | String | - |  |
| 15 | shiftId | String | - | u_mes_mast_shift._id |
| 16 | shiftName | String | - |  |
| 17 | subgroupMean | Decimal128 | - |  |
| 18 | subgroupRange | Decimal128 | - |  |
| 19 | stdDev | Decimal128 | - |  |
| 20 | ucl | Decimal128 | - |  |
| 21 | lcl | Decimal128 | - |  |
| 22 | centerLine | Decimal128 | - |  |
| 23 | inControl | Boolean | - |  |
| 24 | assignableCause | String | - |  |
| 25 | correctiveAction | String | - |  |
| 26 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 27 | nonconformanceName | String | - |  |
| 28 | excludedFromLimits | Boolean | - |  |
| 29 | reactionType | String | - |  |
| 30 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 31 | qualityHoldName | String | - |  |
| 32 | notificationId | String | - | u_mes_syst_notification._id |
| 33 | notificationName | String | - |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |

## u_mes_qual_spcSampleReading

Kind: valueList | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 6 | spcSampleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | reading | Decimal128 | - |  |
| 9 | schemaVersion | Int32 | - |  |
| 10 | createdAt | Date | Datetime |  |
| 11 | createdById | String | - | u_mes_mast_user._id |
| 12 | createdBy | String | - |  |
| 13 | updatedAt | Date | Datetime |  |
| 14 | updatedById | String | - | u_mes_mast_user._id |
| 15 | updatedBy | String | - |  |

## u_mes_qual_spcSampleInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 6 | spcSampleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_spcSampleViolation

Kind: child | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 6 | spcSampleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | rule | String | - |  |
| 9 | description | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_defectCode

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | defectGroupId | String | - | u_mes_qual_defectGroup._id |
| 7 | defectGroupName | String | - |  |
| 8 | description | String | - |  |
| 9 | severity | Int32 | - |  |
| 10 | defaultDispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 11 | defaultDispositionTypeName | String | - |  |
| 12 | dispositionRoutingId | String | - | u_mes_prod_routing._id |
| 13 | dispositionRoutingName | String | - |  |
| 14 | isSafetyRelated | Boolean | - |  |
| 15 | requiresPhoto | Boolean | - |  |
| 16 | requiresHold | Boolean | - |  |
| 17 | scrapCostCategory | String | - |  |
| 18 | customerDefectCode | String | - |  |
| 19 | pfmeaFailureMode | String | - |  |
| 20 | status | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_qual_defectCodeApplicableOperation

Kind: relationship | Data class: master | Parent: u_mes_qual_defectCode | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 6 | defectCodeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | applicableOperationId | String | - | u_mes_prod_operation._id |
| 9 | applicableOperationName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_qual_nonconformance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | description | String | - |  |
| 7 | ncType | String | - |  |
| 8 | source | String | - |  |
| 9 | detectedAt | Date | Datetime |  |
| 10 | detectedById | String | - | u_mes_mast_user._id |
| 11 | detectedBy | String | - |  |
| 12 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 13 | detectedAtOperationName | String | - |  |
| 14 | detectedAtWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 15 | detectedAtWorkCenterName | String | - |  |
| 16 | originOperationId | String | - | u_mes_prod_operation._id |
| 17 | originOperationName | String | - |  |
| 18 | itemId | String | - | u_mes_prod_item._id |
| 19 | itemName | String | - |  |
| 20 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 21 | defectCodeName | String | - |  |
| 22 | supplierId | String | - | u_mes_mast_supplier._id |
| 23 | supplierName | String | - |  |
| 24 | customerId | String | - | u_mes_mast_customer._id |
| 25 | customerName | String | - |  |
| 26 | quantityAffected | Int32 | - |  |
| 27 | quantityRejected | Int32 | - |  |
| 28 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 29 | qualityHoldName | String | - |  |
| 30 | capaId | String | - | u_mes_qual_capa._id |
| 31 | capaName | String | - |  |
| 32 | rootCauseSummary | String | - |  |
| 33 | severity | Int32 | - |  |
| 34 | costInr | Decimal128 | - |  |
| 35 | closedAt | Date | Datetime |  |
| 36 | closedById | String | - | u_mes_mast_user._id |
| 37 | closedBy | String | - |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |
| 40 | createdAt | Date | Datetime |  |
| 41 | createdById | String | - | u_mes_mast_user._id |
| 42 | createdBy | String | - |  |
| 43 | updatedAt | Date | Datetime |  |
| 44 | updatedById | String | - | u_mes_mast_user._id |
| 45 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | quantity | Int32 | - |  |
| 12 | dispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 13 | dispositionTypeName | String | - |  |
| 14 | dispositionById | String | - | u_mes_mast_user._id |
| 15 | dispositionBy | String | - |  |
| 16 | dispositionAt | Date | Datetime |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | actionNo | Int32 | - |  |
| 8 | description | String | - |  |
| 9 | ownerUserId | String | - | u_mes_mast_user._id |
| 10 | ownerUserName | String | - |  |
| 11 | completedAt | Date | Datetime |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceReworkOrder

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 9 | reworkOrderName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceScrapRecord

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | scrapRecordId | String | - | u_mes_qual_scrapRecord._id |
| 9 | scrapRecordName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_nonconformancePhotoControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | photoControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 9 | photoControlledDocumentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceMrbUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | mrbUserId | String | - | u_mes_mast_user._id |
| 9 | mrbUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_reworkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | lotId | String | - | u_mes_plan_lot._id |
| 8 | lotName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | quantity | Int32 | - |  |
| 12 | reworkRoutingId | String | - | u_mes_prod_routing._id |
| 13 | reworkRoutingName | String | - |  |
| 14 | reworkType | String | - |  |
| 15 | instruction | String | - |  |
| 16 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 17 | workCenterName | String | - |  |
| 18 | issuedById | String | - | u_mes_mast_user._id |
| 19 | issuedBy | String | - |  |
| 20 | issuedAt | Date | Datetime |  |
| 21 | startedAt | Date | Datetime |  |
| 22 | completedAt | Date | Datetime |  |
| 23 | reinspectionResult | String | - |  |
| 24 | reinspectedById | String | - | u_mes_mast_user._id |
| 25 | reinspectedBy | String | - |  |
| 26 | reinspectedAt | Date | Datetime |  |
| 27 | quantityRecovered | Int32 | - |  |
| 28 | quantityScrapped | Int32 | - |  |
| 29 | reworkAttemptNo | Int32 | - |  |
| 30 | returnStepNo | Int32 | - |  |
| 31 | labourMinutes | Int32 | - |  |
| 32 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 33 | reasonCodeName | String | - |  |
| 34 | releasedById | String | - | u_mes_mast_user._id |
| 35 | releasedBy | String | - |  |
| 36 | releasedAt | Date | Datetime |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_qual_reworkOrderWipUnit

Kind: relationship | Data class: transaction | Parent: u_mes_qual_reworkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 6 | reworkOrderName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_reworkOrderStep

Kind: child | Data class: transaction | Parent: u_mes_qual_reworkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 6 | reworkOrderName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | description | String | - |  |
| 11 | completedAt | Date | Datetime |  |
| 12 | completedById | String | - | u_mes_mast_user._id |
| 13 | completedBy | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_scrapRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - |  |
| 7 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 8 | defectCodeName | String | - |  |
| 9 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 10 | wipUnitName | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | quantity | Int32 | - |  |
| 16 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - |  |
| 18 | weightKg | Decimal128 | - |  |
| 19 | originOperationId | String | - | u_mes_prod_operation._id |
| 20 | originOperationName | String | - |  |
| 21 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 22 | detectedAtOperationName | String | - |  |
| 23 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 24 | workCenterName | String | - |  |
| 25 | shiftId | String | - | u_mes_mast_shift._id |
| 26 | shiftName | String | - |  |
| 27 | scrapType | String | - |  |
| 28 | scrapCostInr | Decimal128 | - |  |
| 29 | declaredById | String | - | u_mes_mast_user._id |
| 30 | declaredBy | String | - |  |
| 31 | declaredAt | Date | Datetime |  |
| 32 | approvedById | String | - | u_mes_mast_user._id |
| 33 | approvedBy | String | - |  |
| 34 | approvedAt | Date | Datetime |  |
| 35 | scrapLocationId | String | - | u_mes_matl_storageLocation._id |
| 36 | scrapLocationName | String | - |  |
| 37 | disposalMethod | String | - |  |
| 38 | erpPosted | Boolean | - |  |
| 39 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 40 | serialNumberName | String | - |  |
| 41 | dispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 42 | dispositionTypeName | String | - |  |
| 43 | status | String | - |  |
| 44 | schemaVersion | Int32 | - |  |
| 45 | createdAt | Date | Datetime |  |
| 46 | createdById | String | - | u_mes_mast_user._id |
| 47 | createdBy | String | - |  |
| 48 | updatedAt | Date | Datetime |  |
| 49 | updatedById | String | - | u_mes_mast_user._id |
| 50 | updatedBy | String | - |  |

## u_mes_qual_qualityHold

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | holdType | String | - |  |
| 6 | reasonText | String | - |  |
| 7 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 8 | reasonCodeName | String | - |  |
| 9 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 10 | nonconformanceName | String | - |  |
| 11 | itemId | String | - | u_mes_prod_item._id |
| 12 | itemName | String | - |  |
| 13 | totalQuantity | Int32 | - |  |
| 14 | quarantineLocationId | String | - | u_mes_matl_storageLocation._id |
| 15 | quarantineLocationName | String | - |  |
| 16 | placedById | String | - | u_mes_mast_user._id |
| 17 | placedBy | String | - |  |
| 18 | placedAt | Date | Datetime |  |
| 19 | expectedReleaseAt | Date | Datetime |  |
| 20 | releasedById | String | - | u_mes_mast_user._id |
| 21 | releasedBy | String | - |  |
| 22 | releasedAt | Date | Datetime |  |
| 23 | releaseDecision | String | - |  |
| 24 | releaseComment | String | - |  |
| 25 | customerNotified | Boolean | - |  |
| 26 | releaseReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 27 | releaseReasonCodeName | String | - |  |
| 28 | releaseElectronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 29 | releaseElectronicSignatureName | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_qual_qualityHoldHeldObject

Kind: child | Data class: transaction | Parent: u_mes_qual_qualityHold | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 6 | qualityHoldName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | quantity | Int32 | - |  |
| 12 | releasedAt | Date | Datetime |  |
| 13 | releaseDecision | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_deviationPermit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | deviationType | String | - |  |
| 11 | description | String | - |  |
| 12 | requestedValue | Decimal128 | - |  |
| 13 | specifiedValue | Decimal128 | - |  |
| 14 | customerId | String | - | u_mes_mast_customer._id |
| 15 | customerName | String | - |  |
| 16 | customerApprovalRef | String | - |  |
| 17 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 18 | nonconformanceName | String | - |  |
| 19 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 20 | engineeringChangeName | String | - |  |
| 21 | limitType | String | - |  |
| 22 | quantityLimit | Int32 | - |  |
| 23 | quantityUsed | Int32 | - |  |
| 24 | validFrom | Date | Date |  |
| 25 | validTo | Date | Date |  |
| 26 | markingRequirement | String | - |  |
| 27 | requestedById | String | - | u_mes_mast_user._id |
| 28 | requestedBy | String | - |  |
| 29 | requestedAt | Date | Datetime |  |
| 30 | closedAt | Date | Datetime |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_qual_deviationPermitApproval

Kind: child | Data class: transaction | Parent: u_mes_qual_deviationPermit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 6 | deviationPermitName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | businessFunction | String | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | decision | String | - |  |
| 12 | decidedAt | Date | Datetime |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_capa

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | capaType | String | - |  |
| 7 | source | String | - |  |
| 8 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 9 | customerComplaintName | String | - |  |
| 10 | auditId | String | - | u_mes_qual_audit._id |
| 11 | auditName | String | - |  |
| 12 | itemId | String | - | u_mes_prod_item._id |
| 13 | itemName | String | - |  |
| 14 | customerId | String | - | u_mes_mast_customer._id |
| 15 | customerName | String | - |  |
| 16 | openedAt | Date | Datetime |  |
| 17 | openedById | String | - | u_mes_mast_user._id |
| 18 | openedBy | String | - |  |
| 19 | d2ProblemDescription | String | - |  |
| 20 | d4RootCauseOccurrence | String | - |  |
| 21 | d4RootCauseEscape | String | - |  |
| 22 | d4RootCauseMethod | String | - |  |
| 23 | d7PreventionPfmeaId | String | - | u_mes_qual_pfmea._id |
| 24 | d7PreventionPfmeaName | String | - |  |
| 25 | d7PreventionControlPlanId | String | - | u_mes_qual_controlPlan._id |
| 26 | d7PreventionControlPlanName | String | - |  |
| 27 | d7PreventionLessonsLearned | String | - |  |
| 28 | d7PreventionHorizontalDeployment | String | - |  |
| 29 | d8ClosureClosedById | String | - | u_mes_mast_user._id |
| 30 | d8ClosureClosedBy | String | - |  |
| 31 | d8ClosureClosedAt | Date | Datetime |  |
| 32 | d8ClosureCustomerAccepted | Boolean | - |  |
| 33 | dueAt | Date | Datetime |  |
| 34 | currentDiscipline | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_qual_capaNonconformance

Kind: relationship | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 9 | nonconformanceName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_capaTeamMember

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | userId | String | - | u_mes_mast_user._id |
| 9 | userName | String | - |  |
| 10 | roleInTeam | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_capaContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | description | String | - |  |
| 9 | ownerUserId | String | - | u_mes_mast_user._id |
| 10 | ownerUserName | String | - |  |
| 11 | completedAt | Date | Datetime |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_capaCorrectiveAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | description | String | - |  |
| 9 | ownerUserId | String | - | u_mes_mast_user._id |
| 10 | ownerUserName | String | - |  |
| 11 | dueAt | Date | Datetime |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_capaImplementationAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | description | String | - |  |
| 9 | completedAt | Date | Datetime |  |
| 10 | verifiedById | String | - | u_mes_mast_user._id |
| 11 | verifiedBy | String | - |  |
| 12 | effective | Boolean | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_capaControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | capaId | String | - | u_mes_qual_capa._id |
| 6 | capaName | String | - |  |
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

## u_mes_qual_pfmea

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
| 8 | itemRevision | String | - |  |
| 9 | version | Int32 | - |  |
| 10 | methodology | String | - |  |
| 11 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 12 | controlPlanName | String | - |  |
| 13 | originalDate | Date | Date |  |
| 14 | revisionDate | Date | Date |  |
| 15 | approvedById | String | - | u_mes_mast_user._id |
| 16 | approvedBy | String | - |  |
| 17 | approvedAt | Date | Datetime |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_qual_pfmeaCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qual_pfmea | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 6 | pfmeaName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | coreTeamUserId | String | - | u_mes_mast_user._id |
| 9 | coreTeamUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_qual_pfmeaLine

Kind: child | Data class: master | Parent: u_mes_qual_pfmea | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 6 | pfmeaName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | processFunction | String | - |  |
| 11 | failureMode | String | - |  |
| 12 | failureEffect | String | - |  |
| 13 | severity | Int32 | - |  |
| 14 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 15 | characteristicName | String | - |  |
| 16 | classification | String | - |  |
| 17 | failureCause | String | - |  |
| 18 | preventionControl | String | - |  |
| 19 | occurrence | Int32 | - |  |
| 20 | detectionControl | String | - |  |
| 21 | detection | Int32 | - |  |
| 22 | rpn | Int32 | - |  |
| 23 | actionPriority | String | - |  |
| 24 | recommendedAction | String | - |  |
| 25 | ownerUserId | String | - | u_mes_mast_user._id |
| 26 | ownerUserName | String | - |  |
| 27 | targetDate | Date | Date |  |
| 28 | actionTaken | String | - |  |
| 29 | revisedSeverity | Int32 | - |  |
| 30 | revisedOccurrence | Int32 | - |  |
| 31 | revisedDetection | Int32 | - |  |
| 32 | schemaVersion | Int32 | - |  |

## u_mes_qual_ppapSubmission

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | itemRevision | String | - |  |
| 8 | customerId | String | - | u_mes_mast_customer._id |
| 9 | customerName | String | - |  |
| 10 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 11 | engineeringChangeName | String | - |  |
| 12 | submissionLevel | Int32 | - |  |
| 13 | submissionReason | String | - |  |
| 14 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 15 | controlPlanName | String | - |  |
| 16 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 17 | pfmeaName | String | - |  |
| 18 | sampleQuantity | Int32 | - |  |
| 19 | significantProductionRunQuantity | Int32 | - |  |
| 20 | pswSignedById | String | - | u_mes_mast_user._id |
| 21 | pswSignedBy | String | - |  |
| 22 | pswSignedAt | Date | Datetime |  |
| 23 | submittedAt | Date | Datetime |  |
| 24 | customerDecision | String | - |  |
| 25 | customerDecisionAt | Date | Datetime |  |
| 26 | customerRemarks | String | - |  |
| 27 | interimApprovalValidTo | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_qual_ppapSubmissionElement

Kind: child | Data class: transaction | Parent: u_mes_qual_ppapSubmission | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | ppapSubmissionId | String | - | u_mes_qual_ppapSubmission._id |
| 6 | ppapSubmissionName | String | - |  |
| 7 | elementNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | required | Boolean | - |  |
| 10 | status | String | - |  |
| 11 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 12 | controlledDocumentName | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_ppapSubmissionMsaStudy

Kind: relationship | Data class: transaction | Parent: u_mes_qual_ppapSubmission | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | ppapSubmissionId | String | - | u_mes_qual_ppapSubmission._id |
| 6 | ppapSubmissionName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 9 | msaStudyName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_gauge

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | gaugeTypeId | String | - | u_mes_qual_gaugeType._id |
| 7 | gaugeTypeName | String | - |  |
| 8 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | - |  |
| 10 | model | String | - |  |
| 11 | serialNo | String | - |  |
| 12 | rangeMin | Decimal128 | - |  |
| 13 | rangeMax | Decimal128 | - |  |
| 14 | rangeUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 15 | rangeUnitOfMeasureName | String | - |  |
| 16 | resolution | Decimal128 | - |  |
| 17 | accuracy | Decimal128 | - |  |
| 18 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | storageLocationName | String | - |  |
| 20 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 21 | workCenterName | String | - |  |
| 22 | ownerUserId | String | - | u_mes_mast_user._id |
| 23 | ownerUserName | String | - |  |
| 24 | calibrationIntervalDays | Int32 | - |  |
| 25 | calibrationSource | String | - |  |
| 26 | calibrationSupplierId | String | - | u_mes_mast_supplier._id |
| 27 | calibrationSupplierName | String | - |  |
| 28 | lastCalibratedAt | Date | Datetime |  |
| 29 | nextCalibrationDueAt | Date | Date |  |
| 30 | lastGaugeCalibrationId | String | - | u_mes_qual_gaugeCalibration._id |
| 31 | lastGaugeCalibrationName | String | - |  |
| 32 | usageCount | Int32 | - |  |
| 33 | purchasedAt | Date | Datetime |  |
| 34 | isMasterGauge | Boolean | - |  |
| 35 | blockedForUse | Boolean | - |  |
| 36 | equipmentId | String | - | u_mes_mast_equipment._id |
| 37 | equipmentName | String | - |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |

## u_mes_qual_gaugeCalibration

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | gaugeId | String | - | u_mes_qual_gauge._id |
| 6 | gaugeName | String | - |  |
| 7 | calibrationType | String | - |  |
| 8 | calibratedAt | Date | Datetime |  |
| 9 | calibratedById | String | - | u_mes_mast_user._id |
| 10 | calibratedBy | String | - |  |
| 11 | calibrationSupplierId | String | - | u_mes_mast_supplier._id |
| 12 | calibrationSupplierName | String | - |  |
| 13 | masterStandardRef | String | - |  |
| 14 | traceability | String | - |  |
| 15 | temperatureC | Decimal128 | - |  |
| 16 | humidityPct | Decimal128 | - |  |
| 17 | asFoundResult | String | - |  |
| 18 | asLeftResult | String | - |  |
| 19 | overallResult | String | - |  |
| 20 | uncertainty | Decimal128 | - |  |
| 21 | adjustmentMade | Boolean | - |  |
| 22 | certificateNo | String | - |  |
| 23 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 24 | certificateControlledDocumentName | String | - |  |
| 25 | nextDueAt | Date | Date |  |
| 26 | impactAssessmentRequired | Boolean | - |  |
| 27 | remarks | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_qual_gaugeCalibrationReading

Kind: child | Data class: transaction | Parent: u_mes_qual_gaugeCalibration | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | gaugeCalibrationId | String | - | u_mes_qual_gaugeCalibration._id |
| 6 | gaugeCalibrationName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | nominal | Decimal128 | - |  |
| 9 | asFound | Decimal128 | - |  |
| 10 | asLeft | Decimal128 | - |  |
| 11 | tolerance | Decimal128 | - |  |
| 12 | withinTolerance | Boolean | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_msaStudy

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | gaugeId | String | - | u_mes_qual_gauge._id |
| 6 | gaugeName | String | - |  |
| 7 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | studyType | String | - |  |
| 12 | studyMethod | String | - |  |
| 13 | studyDate | Date | Date |  |
| 14 | partsCount | Int32 | - |  |
| 15 | trialsCount | Int32 | - |  |
| 16 | resultsEquipmentVariation | Decimal128 | - |  |
| 17 | resultsAppraiserVariation | Decimal128 | - |  |
| 18 | resultsGrr | Decimal128 | - |  |
| 19 | resultsPartVariation | Decimal128 | - |  |
| 20 | resultsTotalVariation | Decimal128 | - |  |
| 21 | resultsGrrPctTolerance | Decimal128 | - |  |
| 22 | resultsGrrPctStudyVariation | Decimal128 | - |  |
| 23 | resultsNdc | Decimal128 | - |  |
| 24 | resultsBiasValue | Decimal128 | - |  |
| 25 | resultsKappa | Decimal128 | - |  |
| 26 | conclusion | String | - |  |
| 27 | actionRequired | Boolean | - |  |
| 28 | conductedById | String | - | u_mes_mast_user._id |
| 29 | conductedBy | String | - |  |
| 30 | approvedById | String | - | u_mes_mast_user._id |
| 31 | approvedBy | String | - |  |
| 32 | approvedAt | Date | Datetime |  |
| 33 | nextStudyDueAt | Date | Date |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |

## u_mes_qual_msaStudyAppraiserUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_msaStudy | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 6 | msaStudyName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | appraiserUserId | String | - | u_mes_mast_user._id |
| 9 | appraiserUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_msaStudyTrial

Kind: child | Data class: transaction | Parent: u_mes_qual_msaStudy | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 6 | msaStudyName | String | - |  |
| 7 | appraiserUserId | String | - | u_mes_mast_user._id |
| 8 | appraiserUserName | String | - |  |
| 9 | partNo | Int32 | - |  |
| 10 | trialNo | Int32 | - |  |
| 11 | measuredValue | Decimal128 | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_audit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | auditType | String | - |  |
| 7 | standard | String | - |  |
| 8 | scopeText | String | - |  |
| 9 | areaId | String | - | u_mes_mast_area._id |
| 10 | areaName | String | - |  |
| 11 | lineId | String | - | u_mes_mast_line._id |
| 12 | lineName | String | - |  |
| 13 | customerId | String | - | u_mes_mast_customer._id |
| 14 | customerName | String | - |  |
| 15 | layer | Int32 | - |  |
| 16 | leadAuditorUserId | String | - | u_mes_mast_user._id |
| 17 | leadAuditorUserName | String | - |  |
| 18 | auditeeUserId | String | - | u_mes_mast_user._id |
| 19 | auditeeUserName | String | - |  |
| 20 | plannedDate | Date | Date |  |
| 21 | startedAt | Date | Datetime |  |
| 22 | completedAt | Date | Datetime |  |
| 23 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 24 | checkSheetName | String | - |  |
| 25 | questionsCount | Int32 | - |  |
| 26 | conformingCount | Int32 | - |  |
| 27 | scorePct | Decimal128 | - |  |
| 28 | overallRating | String | - |  |
| 29 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 30 | reportControlledDocumentName | String | - |  |
| 31 | nextAuditDueAt | Date | Date |  |
| 32 | auditScheduleId | String | - | u_mes_qual_auditSchedule._id |
| 33 | auditScheduleName | String | - |  |
| 34 | dueDate | Date | Date |  |
| 35 | isMissed | Boolean | - |  |
| 36 | escalationLevel | Int32 | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_qual_auditAuditorUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_audit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | auditId | String | - | u_mes_qual_audit._id |
| 6 | auditName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | auditorUserId | String | - | u_mes_mast_user._id |
| 9 | auditorUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_auditFinding

Kind: child | Data class: transaction | Parent: u_mes_qual_audit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | auditId | String | - | u_mes_qual_audit._id |
| 6 | auditName | String | - |  |
| 7 | findingNo | Int32 | - |  |
| 8 | clause | String | - |  |
| 9 | description | String | - |  |
| 10 | grade | String | - |  |
| 11 | ownerUserId | String | - | u_mes_mast_user._id |
| 12 | ownerUserName | String | - |  |
| 13 | dueAt | Date | Datetime |  |
| 14 | closedAt | Date | Datetime |  |
| 15 | capaId | String | - | u_mes_qual_capa._id |
| 16 | capaName | String | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_qual_customerComplaint

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerId | String | - | u_mes_mast_customer._id |
| 6 | customerName | String | - |  |
| 7 | customerRefNo | String | - |  |
| 8 | complaintTypeId | String | - | u_mes_qual_complaintType._id |
| 9 | complaintTypeName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | description | String | - |  |
| 13 | defectDescription | String | - |  |
| 14 | reportedAt | Date | Datetime |  |
| 15 | receivedById | String | - | u_mes_mast_user._id |
| 16 | receivedBy | String | - |  |
| 17 | occurredAt | Date | Datetime |  |
| 18 | customerLocation | String | - |  |
| 19 | quantityComplained | Int32 | - |  |
| 20 | quantityConfirmed | Int32 | - |  |
| 21 | vehicleModelId | String | - | u_mes_prod_vehicleModel._id |
| 22 | vehicleModelName | String | - |  |
| 23 | mileageKm | Decimal128 | - |  |
| 24 | severity | Int32 | - |  |
| 25 | isSafetyRelated | Boolean | - |  |
| 26 | containmentDueAt | Date | Datetime |  |
| 27 | containmentSentAt | Date | Datetime |  |
| 28 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 29 | nonconformanceName | String | - |  |
| 30 | capaId | String | - | u_mes_qual_capa._id |
| 31 | capaName | String | - |  |
| 32 | debitNoteInr | Decimal128 | - |  |
| 33 | ppmImpact | Int32 | - |  |
| 34 | sortingCostInr | Decimal128 | - |  |
| 35 | customerClosedAt | Date | Datetime |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintSerialNumber

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 9 | serialNumberName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintShipment

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | shipmentId | String | - | u_mes_matl_shipment._id |
| 9 | shipmentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintSuspectLot

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | suspectLotId | String | - | u_mes_plan_lot._id |
| 9 | suspectLotName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintCommunication

Kind: child | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 6 | customerComplaintName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | communicatedAt | Date | Datetime |  |
| 9 | direction | String | - |  |
| 10 | communicationSummary | String | - |  |
| 11 | authorUserId | String | - | u_mes_mast_user._id |
| 12 | authorUserName | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_defectGroup

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

## u_mes_qual_gaugeType

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

## u_mes_qual_dispositionType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | requiresRework | Boolean | - |  |
| 8 | requiresScrap | Boolean | - |  |
| 9 | requiresCustomerApproval | Boolean | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_qual_complaintType

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

## u_mes_qual_characteristicPosition

Kind: child | Data class: master | Parent: u_mes_qual_characteristic | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 6 | characteristicName | String | - |  |
| 7 | positionNo | Int32 | - |  |
| 8 | positionName | String | - |  |
| 9 | nominal | Decimal128 | - |  |
| 10 | lowerSpecLimit | Decimal128 | - |  |
| 11 | upperSpecLimit | Decimal128 | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 15 | curveEnvelopeName | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_qual_curveEnvelope

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - |  |
| 12 | operationId | String | - | u_mes_prod_operation._id |
| 13 | operationName | String | - |  |
| 14 | recipeId | String | - | u_mes_prod_recipe._id |
| 15 | recipeName | String | - |  |
| 16 | curveType | String | - |  |
| 17 | xQuantity | String | - |  |
| 18 | xUnitText | String | - |  |
| 19 | yQuantity | String | - |  |
| 20 | yUnitText | String | - |  |
| 21 | version | Int32 | - |  |
| 22 | goldenSampleSerialNo | String | - |  |
| 23 | referenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 24 | referenceControlledDocumentName | String | - |  |
| 25 | effectiveFrom | Date | Date |  |
| 26 | effectiveTo | Date | Date |  |
| 27 | approvedById | String | - | u_mes_mast_user._id |
| 28 | approvedBy | String | - |  |
| 29 | approvedAt | Date | Datetime |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |

## u_mes_qual_curveEnvelopeWindow

Kind: child | Data class: master | Parent: u_mes_qual_curveEnvelope | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 6 | curveEnvelopeName | String | - |  |
| 7 | windowNo | Int32 | - |  |
| 8 | windowType | String | - |  |
| 9 | xMin | Decimal128 | - |  |
| 10 | xMax | Decimal128 | - |  |
| 11 | yMin | Decimal128 | - |  |
| 12 | yMax | Decimal128 | - |  |
| 13 | entrySide | String | - |  |
| 14 | exitSide | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_qual_measurementCurve

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 6 | curveEnvelopeName | String | - |  |
| 7 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - |  |
| 9 | positionNo | Int32 | - |  |
| 10 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - |  |
| 12 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String | - |  |
| 14 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 15 | operationExecutionName | String | - |  |
| 16 | equipmentId | String | - | u_mes_mast_equipment._id |
| 17 | equipmentName | String | - |  |
| 18 | recipeVersion | String | - |  |
| 19 | capturedAt | Date | Datetime |  |
| 20 | pointCount | Int32 | - |  |
| 21 | peakX | Decimal128 | - |  |
| 22 | peakY | Decimal128 | - |  |
| 23 | finalX | Decimal128 | - |  |
| 24 | finalY | Decimal128 | - |  |
| 25 | result | String | - |  |
| 26 | failedWindowNo | Int32 | - |  |
| 27 | rawControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 28 | rawControlledDocumentName | String | - |  |
| 29 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 30 | inspectionResultName | String | - |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_qual_measurementCurvePoint

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 6 | measurementCurveName | String | - |  |
| 7 | pointNo | Int32 | - |  |
| 8 | sampledAt | Date | Datetime |  |
| 9 | xValue | Decimal128 | - |  |
| 10 | yValue | Decimal128 | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_defectRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 6 | defectCodeName | String | - |  |
| 7 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 8 | wipUnitName | String | - |  |
| 9 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 10 | serialNumberName | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - |  |
| 17 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 18 | productionOrderName | String | - |  |
| 19 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 20 | detectedAtOperationName | String | - |  |
| 21 | detectedAtWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 22 | detectedAtWorkCenterName | String | - |  |
| 23 | originOperationId | String | - | u_mes_prod_operation._id |
| 24 | originOperationName | String | - |  |
| 25 | isFirstFail | Boolean | - |  |
| 26 | positionNo | Int32 | - |  |
| 27 | defectLocationText | String | - |  |
| 28 | quantity | Int32 | - |  |
| 29 | fourMCategory | String | - |  |
| 30 | operatorUserId | String | - | u_mes_mast_user._id |
| 31 | operatorUserName | String | - |  |
| 32 | equipmentId | String | - | u_mes_mast_equipment._id |
| 33 | equipmentName | String | - |  |
| 34 | componentLotId | String | - | u_mes_plan_lot._id |
| 35 | componentLotName | String | - |  |
| 36 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 37 | operationExecutionName | String | - |  |
| 38 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 39 | inspectionResultName | String | - |  |
| 40 | shiftId | String | - | u_mes_mast_shift._id |
| 41 | shiftName | String | - |  |
| 42 | productionDate | Date | Date |  |
| 43 | detectedAt | Date | Datetime |  |
| 44 | detectedById | String | - | u_mes_mast_user._id |
| 45 | detectedBy | String | - |  |
| 46 | imageControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 47 | imageControlledDocumentName | String | - |  |
| 48 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 49 | nonconformanceName | String | - |  |
| 50 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 51 | reworkOrderName | String | - |  |
| 52 | scrapRecordId | String | - | u_mes_qual_scrapRecord._id |
| 53 | scrapRecordName | String | - |  |
| 54 | status | String | - |  |
| 55 | schemaVersion | Int32 | - |  |
| 56 | createdAt | Date | Datetime |  |
| 57 | createdById | String | - | u_mes_mast_user._id |
| 58 | createdBy | String | - |  |
| 59 | updatedAt | Date | Datetime |  |
| 60 | updatedById | String | - | u_mes_mast_user._id |
| 61 | updatedBy | String | - |  |

## u_mes_qual_auditSchedule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | auditType | String | - |  |
| 7 | layer | Int32 | - |  |
| 8 | areaId | String | - | u_mes_mast_area._id |
| 9 | areaName | String | - |  |
| 10 | lineId | String | - | u_mes_mast_line._id |
| 11 | lineName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 15 | checkSheetName | String | - |  |
| 16 | frequencyType | String | - |  |
| 17 | frequencyValue | Decimal128 | - |  |
| 18 | auditorRoleId | String | - | u_mes_mast_role._id |
| 19 | auditorRoleName | String | - |  |
| 20 | auditorUserId | String | - | u_mes_mast_user._id |
| 21 | auditorUserName | String | - |  |
| 22 | toleranceHours | Int32 | - |  |
| 23 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 24 | escalationRuleName | String | - |  |
| 25 | nextDueDate | Date | Date |  |
| 26 | validFrom | Date | Date |  |
| 27 | validTo | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlanProductVariant

Kind: relationship | Data class: master | Parent: u_mes_qual_inspectionPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 6 | inspectionPlanName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 9 | productVariantName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
