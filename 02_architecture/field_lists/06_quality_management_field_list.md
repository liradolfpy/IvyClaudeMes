# Field list - Quality Management (qual)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/06_quality_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_qual_characteristic

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | characteristicType | String | - |  |
| 12 | classification | String | - |  |
| 13 | drawingZone | String | - |  |
| 14 | balloonNo | String | - |  |
| 15 | dataType | String | - |  |
| 16 | nominal | Decimal128 | - |  |
| 17 | lowerSpecLimit | Decimal128 | - |  |
| 18 | upperSpecLimit | Decimal128 | - |  |
| 19 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - |  |
| 21 | toleranceType | String | - |  |
| 22 | measurementMethod | String | - |  |
| 23 | gaugeId | String | - | u_mes_qual_gauge._id |
| 24 | gaugeName | String | - |  |
| 25 | gaugeTypeId | String | - | u_mes_qual_gaugeType._id |
| 26 | gaugeTypeName | String | - |  |
| 27 | attributeAcceptance | String | - |  |
| 28 | isSpc | Boolean | - |  |
| 29 | targetCpk | Decimal128 | - |  |
| 30 | reactionPlan | String | - |  |
| 31 | source | String | - |  |
| 32 | positionCount | Int32 | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlan

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
| 9 | phase | String | - |  |
| 10 | version | Int32 | - |  |
| 11 | routingId | String | - | u_mes_prod_routing._id |
| 12 | routingName | String | - |  |
| 13 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 14 | pfmeaName | String | - |  |
| 15 | customerApprovalDate | Date | Date |  |
| 16 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - |  |
| 18 | preparedById | String | - | u_mes_mast_user._id |
| 19 | preparedBy | String | - |  |
| 20 | approvedById | String | - | u_mes_mast_user._id |
| 21 | approvedBy | String | - |  |
| 22 | approvedAt | Date | Datetime |  |
| 23 | effectiveFrom | Date | Date |  |
| 24 | originalDate | Date | Date |  |
| 25 | revisionDate | Date | Date |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlanCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qual_controlPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 7 | controlPlanName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | coreTeamUserId | String | - | u_mes_mast_user._id |
| 10 | coreTeamUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_qual_controlPlanLine

Kind: child | Data class: master | Parent: u_mes_qual_controlPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 7 | controlPlanName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | processName | String | - |  |
| 12 | equipmentText | String | - |  |
| 13 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 14 | characteristicName | String | - |  |
| 15 | classification | String | - |  |
| 16 | specification | String | - |  |
| 17 | gaugeId | String | - | u_mes_qual_gauge._id |
| 18 | gaugeName | String | - |  |
| 19 | measurementTechnique | String | - |  |
| 20 | sampleSize | Int32 | - |  |
| 21 | sampleFrequency | String | - |  |
| 22 | controlMethod | String | - |  |
| 23 | reactionPlan | String | - |  |
| 24 | responsible | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 8 | controlPlanName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | operationId | String | - | u_mes_prod_operation._id |
| 12 | operationName | String | - |  |
| 13 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 14 | workCenterName | String | - |  |
| 15 | planType | String | - |  |
| 16 | version | Int32 | - |  |
| 17 | collectionTrigger | String | - |  |
| 18 | samplingPlanId | String | - | u_mes_qual_samplingPlan._id |
| 19 | samplingPlanName | String | - |  |
| 20 | blockOnFail | Boolean | - |  |
| 21 | effectiveFrom | Date | Date |  |
| 22 | effectiveTo | Date | Date |  |
| 23 | approvedById | String | - | u_mes_mast_user._id |
| 24 | approvedBy | String | - |  |
| 25 | approvedAt | Date | Datetime |  |
| 26 | itemRevision | String | - |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlanLine

Kind: child | Data class: master | Parent: u_mes_qual_inspectionPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 7 | inspectionPlanName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - |  |
| 11 | gaugeId | String | - | u_mes_qual_gauge._id |
| 12 | gaugeName | String | - |  |
| 13 | sampleSize | Int32 | - |  |
| 14 | frequencyType | String | - |  |
| 15 | frequencyValue | Decimal128 | - |  |
| 16 | recordType | String | - |  |
| 17 | autoNcOnFail | Boolean | - |  |
| 18 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 19 | defectCodeName | String | - |  |
| 20 | overrideAllowed | Boolean | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_qual_samplingPlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | samplingType | String | - |  |
| 8 | standard | String | - |  |
| 9 | inspectionLevel | String | - |  |
| 10 | aql | Decimal128 | - |  |
| 11 | frequencyType | String | - |  |
| 12 | frequencyEveryNUnits | Int32 | - |  |
| 13 | frequencyEveryMinutes | Int32 | - |  |
| 14 | skipLotEnabled | Boolean | - |  |
| 15 | skipLotConsecutiveAcceptedToSkip | Int32 | - |  |
| 16 | skipLotSkipFraction | Decimal128 | - |  |
| 17 | switchingRules | String | - |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_qual_samplingPlanSizeRow

Kind: child | Data class: master | Parent: u_mes_qual_samplingPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | samplingPlanId | String | - | u_mes_qual_samplingPlan._id |
| 7 | samplingPlanName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lotSizeFrom | Int32 | - |  |
| 10 | lotSizeTo | Int32 | - |  |
| 11 | sampleSize | Int32 | - |  |
| 12 | acceptNumber | Int32 | - |  |
| 13 | rejectNumber | Int32 | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheet

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | checkSheetType | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | operationId | String | - | u_mes_prod_operation._id |
| 13 | operationName | String | - |  |
| 14 | itemId | String | - | u_mes_prod_item._id |
| 15 | itemName | String | - |  |
| 16 | version | Int32 | - |  |
| 17 | frequency | String | - |  |
| 18 | masterSampleRequired | Boolean | - |  |
| 19 | estimatedMinutes | Int32 | - |  |
| 20 | effectiveFrom | Date | Date |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheetItem

Kind: child | Data class: master | Parent: u_mes_qual_checkSheet | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 7 | checkSheetName | String | - |  |
| 8 | itemNo | Int32 | - |  |
| 9 | question | String | - |  |
| 10 | answerType | String | - |  |
| 11 | expectedAnswer | String | - |  |
| 12 | lowerLimit | Decimal128 | - |  |
| 13 | upperLimit | Decimal128 | - |  |
| 14 | unitText | String | - |  |
| 15 | isCritical | Boolean | - |  |
| 16 | reactionOnFail | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_qual_checkSheetResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 7 | checkSheetName | String | - |  |
| 8 | checkSheetVersion | Int32 | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | equipmentId | String | - | u_mes_mast_equipment._id |
| 12 | equipmentName | String | - |  |
| 13 | shiftId | String | - | u_mes_mast_shift._id |
| 14 | shiftName | String | - |  |
| 15 | productionDate | Date | Date |  |
| 16 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 17 | productionOrderName | String | - |  |
| 18 | performedById | String | - | u_mes_mast_user._id |
| 19 | performedBy | String | - |  |
| 20 | startedAt | Date | Datetime |  |
| 21 | completedAt | Date | Datetime |  |
| 22 | overallResult | String | - |  |
| 23 | failedCount | Int32 | - |  |
| 24 | reactionTaken | String | - |  |
| 25 | verifiedById | String | - | u_mes_mast_user._id |
| 26 | verifiedBy | String | - |  |
| 27 | verifiedAt | Date | Datetime |  |
| 28 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 29 | nonconformanceName | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_qual_checkSheetResultAnswer

Kind: child | Data class: transaction | Parent: u_mes_qual_checkSheetResult | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | checkSheetResultId | String | - | u_mes_qual_checkSheetResult._id |
| 7 | checkSheetResultName | String | - |  |
| 8 | itemNo | Int32 | - |  |
| 9 | answerText | String | - |  |
| 10 | answerNumber | Decimal128 | - |  |
| 11 | passed | Boolean | - |  |
| 12 | comment | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_inspectionResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 7 | inspectionPlanName | String | - |  |
| 8 | planLineNo | Int32 | - |  |
| 9 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - |  |
| 11 | itemId | String | - | u_mes_prod_item._id |
| 12 | itemName | String | - |  |
| 13 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 14 | wipUnitName | String | - |  |
| 15 | lotId | String | - | u_mes_plan_lot._id |
| 16 | lotName | String | - |  |
| 17 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 18 | goodsReceiptName | String | - |  |
| 19 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | - |  |
| 21 | operationId | String | - | u_mes_prod_operation._id |
| 22 | operationName | String | - |  |
| 23 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 24 | workCenterName | String | - |  |
| 25 | inspectionType | String | - |  |
| 26 | sampleNo | Int32 | - |  |
| 27 | measuredValue | Decimal128 | - |  |
| 28 | attributeResult | String | - |  |
| 29 | nominal | Decimal128 | - |  |
| 30 | lowerSpecLimit | Decimal128 | - |  |
| 31 | upperSpecLimit | Decimal128 | - |  |
| 32 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 33 | unitOfMeasureName | String | - |  |
| 34 | deviation | Decimal128 | - |  |
| 35 | result | String | - |  |
| 36 | gaugeId | String | - | u_mes_qual_gauge._id |
| 37 | gaugeName | String | - |  |
| 38 | measuredById | String | - | u_mes_mast_user._id |
| 39 | measuredBy | String | - |  |
| 40 | measuredAt | Date | Datetime |  |
| 41 | source | String | - |  |
| 42 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 43 | defectCodeName | String | - |  |
| 44 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 45 | nonconformanceName | String | - |  |
| 46 | overridden | Boolean | - |  |
| 47 | remarks | String | - |  |
| 48 | positionNo | Int32 | - |  |
| 49 | positionName | String | - |  |
| 50 | imageControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 51 | imageControlledDocumentName | String | - |  |
| 52 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 53 | measurementCurveName | String | - |  |
| 54 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 55 | analyticsModelName | String | - |  |
| 56 | modelVersion | String | - |  |
| 57 | modelClass | String | - |  |
| 58 | modelConfidence | Decimal128 | - |  |
| 59 | status | String | - |  |
| 60 | schemaVersion | Int32 | - |  |
| 61 | createdAt | Date | Datetime |  |
| 62 | createdById | String | - | u_mes_mast_user._id |
| 63 | createdBy | String | - |  |
| 64 | updatedAt | Date | Datetime |  |
| 65 | updatedById | String | - | u_mes_mast_user._id |
| 66 | updatedBy | String | - |  |

## u_mes_qual_spcChart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | chartType | String | - |  |
| 16 | subgroupSize | Int32 | - |  |
| 17 | subgroupFrequency | String | - |  |
| 18 | lowerSpecLimit | Decimal128 | - |  |
| 19 | upperSpecLimit | Decimal128 | - |  |
| 20 | capabilityCp | Decimal128 | - |  |
| 21 | capabilityCpk | Decimal128 | - |  |
| 22 | capabilityPp | Decimal128 | - |  |
| 23 | capabilityPpk | Decimal128 | - |  |
| 24 | capabilityCalculatedAt | Date | Datetime |  |
| 25 | capabilitySampleCount | Int32 | - |  |
| 26 | ownerUserId | String | - | u_mes_mast_user._id |
| 27 | ownerUserName | String | - |  |
| 28 | reactionPlan | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcChartControlLimit

Kind: child | Data class: master | Parent: u_mes_qual_spcChart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 7 | spcChartName | String | - |  |
| 8 | revisionNo | Int32 | - |  |
| 9 | effectiveFrom | Date | Date |  |
| 10 | ucl | Decimal128 | - |  |
| 11 | centerLine | Decimal128 | - |  |
| 12 | lcl | Decimal128 | - |  |
| 13 | uclRange | Decimal128 | - |  |
| 14 | centerLineRange | Decimal128 | - |  |
| 15 | lclRange | Decimal128 | - |  |
| 16 | basedOnSubgroups | Int32 | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcChartRule

Kind: valueList | Data class: master | Parent: u_mes_qual_spcChart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 7 | spcChartName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | rule | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_qual_spcSample

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcChartId | String | - | u_mes_qual_spcChart._id |
| 7 | spcChartName | String | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | subgroupNo | Int32 | - |  |
| 13 | sampledAt | Date | Datetime |  |
| 14 | sampledById | String | - | u_mes_mast_user._id |
| 15 | sampledBy | String | - |  |
| 16 | shiftId | String | - | u_mes_mast_shift._id |
| 17 | shiftName | String | - |  |
| 18 | subgroupMean | Decimal128 | - |  |
| 19 | subgroupRange | Decimal128 | - |  |
| 20 | stdDev | Decimal128 | - |  |
| 21 | ucl | Decimal128 | - |  |
| 22 | lcl | Decimal128 | - |  |
| 23 | centerLine | Decimal128 | - |  |
| 24 | inControl | Boolean | - |  |
| 25 | assignableCause | String | - |  |
| 26 | correctiveAction | String | - |  |
| 27 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 28 | nonconformanceName | String | - |  |
| 29 | excludedFromLimits | Boolean | - |  |
| 30 | reactionType | String | - |  |
| 31 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 32 | qualityHoldName | String | - |  |
| 33 | notificationId | String | - | u_mes_syst_notification._id |
| 34 | notificationName | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_qual_spcSampleReading

Kind: valueList | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 7 | spcSampleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | reading | Decimal128 | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_qual_spcSampleInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 7 | spcSampleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 10 | inspectionResultName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_spcSampleViolation

Kind: child | Data class: transaction | Parent: u_mes_qual_spcSample | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | spcSampleId | String | - | u_mes_qual_spcSample._id |
| 7 | spcSampleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | rule | String | - |  |
| 10 | description | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_defectCode

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | defectGroupId | String | - | u_mes_qual_defectGroup._id |
| 8 | defectGroupName | String | - |  |
| 9 | description | String | - |  |
| 10 | severity | Int32 | - |  |
| 11 | defaultDispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 12 | defaultDispositionTypeName | String | - |  |
| 13 | dispositionRoutingId | String | - | u_mes_prod_routing._id |
| 14 | dispositionRoutingName | String | - |  |
| 15 | isSafetyRelated | Boolean | - |  |
| 16 | requiresPhoto | Boolean | - |  |
| 17 | requiresHold | Boolean | - |  |
| 18 | scrapCostCategory | String | - |  |
| 19 | customerDefectCode | String | - |  |
| 20 | pfmeaFailureMode | String | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_qual_defectCodeApplicableOperation

Kind: relationship | Data class: master | Parent: u_mes_qual_defectCode | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 7 | defectCodeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | applicableOperationId | String | - | u_mes_prod_operation._id |
| 10 | applicableOperationName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_qual_nonconformance

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
| 8 | ncType | String | - |  |
| 9 | source | String | - |  |
| 10 | detectedAt | Date | Datetime |  |
| 11 | detectedById | String | - | u_mes_mast_user._id |
| 12 | detectedBy | String | - |  |
| 13 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 14 | detectedAtOperationName | String | - |  |
| 15 | detectedAtWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 16 | detectedAtWorkCenterName | String | - |  |
| 17 | originOperationId | String | - | u_mes_prod_operation._id |
| 18 | originOperationName | String | - |  |
| 19 | itemId | String | - | u_mes_prod_item._id |
| 20 | itemName | String | - |  |
| 21 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 22 | defectCodeName | String | - |  |
| 23 | supplierId | String | - | u_mes_mast_supplier._id |
| 24 | supplierName | String | - |  |
| 25 | customerId | String | - | u_mes_mast_customer._id |
| 26 | customerName | String | - |  |
| 27 | quantityAffected | Int32 | - |  |
| 28 | quantityRejected | Int32 | - |  |
| 29 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 30 | qualityHoldName | String | - |  |
| 31 | capaId | String | - | u_mes_qual_capa._id |
| 32 | capaName | String | - |  |
| 33 | rootCauseSummary | String | - |  |
| 34 | severity | Int32 | - |  |
| 35 | costInr | Decimal128 | - |  |
| 36 | closedAt | Date | Datetime |  |
| 37 | closedById | String | - | u_mes_mast_user._id |
| 38 | closedBy | String | - |  |
| 39 | deviationClass | String | - |  |
| 40 | productImpactText | String | - |  |
| 41 | investigationDueDate | Date | Date |  |
| 42 | qaApprovedById | String | - | u_mes_mast_user._id |
| 43 | qaApprovedBy | String | - |  |
| 44 | qaApprovedAt | Date | Datetime |  |
| 45 | riskAssessmentId | String | - | u_mes_qual_riskAssessment._id |
| 46 | riskAssessmentName | String | - |  |
| 47 | status | String | - |  |
| 48 | schemaVersion | Int32 | - |  |
| 49 | createdAt | Date | Datetime |  |
| 50 | createdById | String | - | u_mes_mast_user._id |
| 51 | createdBy | String | - |  |
| 52 | updatedAt | Date | Datetime |  |
| 53 | updatedById | String | - | u_mes_mast_user._id |
| 54 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | quantity | Int32 | - |  |
| 13 | dispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 14 | dispositionTypeName | String | - |  |
| 15 | dispositionById | String | - | u_mes_mast_user._id |
| 16 | dispositionBy | String | - |  |
| 17 | dispositionAt | Date | Datetime |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | actionNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | completedAt | Date | Datetime |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 10 | inspectionResultName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceReworkOrder

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 10 | reworkOrderName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceScrapRecord

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | scrapRecordId | String | - | u_mes_qual_scrapRecord._id |
| 10 | scrapRecordName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_nonconformancePhotoControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | photoControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 10 | photoControlledDocumentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_nonconformanceMrbUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_nonconformance | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | mrbUserId | String | - | u_mes_mast_user._id |
| 10 | mrbUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_reworkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | lotId | String | - | u_mes_plan_lot._id |
| 9 | lotName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | quantity | Int32 | - |  |
| 13 | reworkRoutingId | String | - | u_mes_prod_routing._id |
| 14 | reworkRoutingName | String | - |  |
| 15 | reworkType | String | - |  |
| 16 | instruction | String | - |  |
| 17 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 18 | workCenterName | String | - |  |
| 19 | issuedById | String | - | u_mes_mast_user._id |
| 20 | issuedBy | String | - |  |
| 21 | issuedAt | Date | Datetime |  |
| 22 | startedAt | Date | Datetime |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | reinspectionResult | String | - |  |
| 25 | reinspectedById | String | - | u_mes_mast_user._id |
| 26 | reinspectedBy | String | - |  |
| 27 | reinspectedAt | Date | Datetime |  |
| 28 | quantityRecovered | Int32 | - |  |
| 29 | quantityScrapped | Int32 | - |  |
| 30 | reworkAttemptNo | Int32 | - |  |
| 31 | returnStepNo | Int32 | - |  |
| 32 | labourMinutes | Int32 | - |  |
| 33 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 34 | reasonCodeName | String | - |  |
| 35 | releasedById | String | - | u_mes_mast_user._id |
| 36 | releasedBy | String | - |  |
| 37 | releasedAt | Date | Datetime |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |
| 40 | createdAt | Date | Datetime |  |
| 41 | createdById | String | - | u_mes_mast_user._id |
| 42 | createdBy | String | - |  |
| 43 | updatedAt | Date | Datetime |  |
| 44 | updatedById | String | - | u_mes_mast_user._id |
| 45 | updatedBy | String | - |  |

## u_mes_qual_reworkOrderWipUnit

Kind: relationship | Data class: transaction | Parent: u_mes_qual_reworkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 7 | reworkOrderName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 10 | wipUnitName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_reworkOrderStep

Kind: child | Data class: transaction | Parent: u_mes_qual_reworkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 7 | reworkOrderName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | description | String | - |  |
| 12 | completedAt | Date | Datetime |  |
| 13 | completedById | String | - | u_mes_mast_user._id |
| 14 | completedBy | String | - |  |
| 15 | schemaVersion | Int32 | - |  |
| 16 | createdAt | Date | Datetime |  |
| 17 | createdById | String | - | u_mes_mast_user._id |
| 18 | createdBy | String | - |  |
| 19 | updatedAt | Date | Datetime |  |
| 20 | updatedById | String | - | u_mes_mast_user._id |
| 21 | updatedBy | String | - |  |

## u_mes_qual_scrapRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 7 | nonconformanceName | String | - |  |
| 8 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 9 | defectCodeName | String | - |  |
| 10 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - |  |
| 12 | lotId | String | - | u_mes_plan_lot._id |
| 13 | lotName | String | - |  |
| 14 | itemId | String | - | u_mes_prod_item._id |
| 15 | itemName | String | - |  |
| 16 | quantity | Int32 | - |  |
| 17 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | - |  |
| 19 | weightKg | Decimal128 | - |  |
| 20 | originOperationId | String | - | u_mes_prod_operation._id |
| 21 | originOperationName | String | - |  |
| 22 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 23 | detectedAtOperationName | String | - |  |
| 24 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 25 | workCenterName | String | - |  |
| 26 | shiftId | String | - | u_mes_mast_shift._id |
| 27 | shiftName | String | - |  |
| 28 | scrapType | String | - |  |
| 29 | scrapCostInr | Decimal128 | - |  |
| 30 | declaredById | String | - | u_mes_mast_user._id |
| 31 | declaredBy | String | - |  |
| 32 | declaredAt | Date | Datetime |  |
| 33 | approvedById | String | - | u_mes_mast_user._id |
| 34 | approvedBy | String | - |  |
| 35 | approvedAt | Date | Datetime |  |
| 36 | scrapLocationId | String | - | u_mes_matl_storageLocation._id |
| 37 | scrapLocationName | String | - |  |
| 38 | disposalMethod | String | - |  |
| 39 | erpPosted | Boolean | - |  |
| 40 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 41 | serialNumberName | String | - |  |
| 42 | dispositionTypeId | String | - | u_mes_qual_dispositionType._id |
| 43 | dispositionTypeName | String | - |  |
| 44 | status | String | - |  |
| 45 | schemaVersion | Int32 | - |  |
| 46 | createdAt | Date | Datetime |  |
| 47 | createdById | String | - | u_mes_mast_user._id |
| 48 | createdBy | String | - |  |
| 49 | updatedAt | Date | Datetime |  |
| 50 | updatedById | String | - | u_mes_mast_user._id |
| 51 | updatedBy | String | - |  |

## u_mes_qual_qualityHold

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | holdType | String | - |  |
| 7 | reasonText | String | - |  |
| 8 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 9 | reasonCodeName | String | - |  |
| 10 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 11 | nonconformanceName | String | - |  |
| 12 | itemId | String | - | u_mes_prod_item._id |
| 13 | itemName | String | - |  |
| 14 | totalQuantity | Int32 | - |  |
| 15 | quarantineLocationId | String | - | u_mes_matl_storageLocation._id |
| 16 | quarantineLocationName | String | - |  |
| 17 | placedById | String | - | u_mes_mast_user._id |
| 18 | placedBy | String | - |  |
| 19 | placedAt | Date | Datetime |  |
| 20 | expectedReleaseAt | Date | Datetime |  |
| 21 | releasedById | String | - | u_mes_mast_user._id |
| 22 | releasedBy | String | - |  |
| 23 | releasedAt | Date | Datetime |  |
| 24 | releaseDecision | String | - |  |
| 25 | releaseComment | String | - |  |
| 26 | customerNotified | Boolean | - |  |
| 27 | releaseReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 28 | releaseReasonCodeName | String | - |  |
| 29 | releaseElectronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 30 | releaseElectronicSignatureName | String | - |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_qual_qualityHoldHeldObject

Kind: child | Data class: transaction | Parent: u_mes_qual_qualityHold | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 7 | qualityHoldName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | quantity | Int32 | - |  |
| 13 | releasedAt | Date | Datetime |  |
| 14 | releaseDecision | String | - |  |
| 15 | schemaVersion | Int32 | - |  |
| 16 | createdAt | Date | Datetime |  |
| 17 | createdById | String | - | u_mes_mast_user._id |
| 18 | createdBy | String | - |  |
| 19 | updatedAt | Date | Datetime |  |
| 20 | updatedById | String | - | u_mes_mast_user._id |
| 21 | updatedBy | String | - |  |

## u_mes_qual_deviationPermit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

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
| 9 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - |  |
| 11 | deviationType | String | - |  |
| 12 | description | String | - |  |
| 13 | requestedValue | Decimal128 | - |  |
| 14 | specifiedValue | Decimal128 | - |  |
| 15 | customerId | String | - | u_mes_mast_customer._id |
| 16 | customerName | String | - |  |
| 17 | customerApprovalRef | String | - |  |
| 18 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 19 | nonconformanceName | String | - |  |
| 20 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 21 | engineeringChangeName | String | - |  |
| 22 | limitType | String | - |  |
| 23 | quantityLimit | Int32 | - |  |
| 24 | quantityUsed | Int32 | - |  |
| 25 | validFrom | Date | Date |  |
| 26 | validTo | Date | Date |  |
| 27 | markingRequirement | String | - |  |
| 28 | requestedById | String | - | u_mes_mast_user._id |
| 29 | requestedBy | String | - |  |
| 30 | requestedAt | Date | Datetime |  |
| 31 | closedAt | Date | Datetime |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_qual_deviationPermitApproval

Kind: child | Data class: transaction | Parent: u_mes_qual_deviationPermit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 7 | deviationPermitName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | businessFunction | String | - |  |
| 10 | userId | String | - | u_mes_mast_user._id |
| 11 | userName | String | - |  |
| 12 | decision | String | - |  |
| 13 | decidedAt | Date | Datetime |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_capa

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | capaType | String | - |  |
| 8 | source | String | - |  |
| 9 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 10 | customerComplaintName | String | - |  |
| 11 | auditId | String | - | u_mes_qual_audit._id |
| 12 | auditName | String | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | customerId | String | - | u_mes_mast_customer._id |
| 16 | customerName | String | - |  |
| 17 | openedAt | Date | Datetime |  |
| 18 | openedById | String | - | u_mes_mast_user._id |
| 19 | openedBy | String | - |  |
| 20 | d2ProblemDescription | String | - |  |
| 21 | d4RootCauseOccurrence | String | - |  |
| 22 | d4RootCauseEscape | String | - |  |
| 23 | d4RootCauseMethod | String | - |  |
| 24 | d7PreventionPfmeaId | String | - | u_mes_qual_pfmea._id |
| 25 | d7PreventionPfmeaName | String | - |  |
| 26 | d7PreventionControlPlanId | String | - | u_mes_qual_controlPlan._id |
| 27 | d7PreventionControlPlanName | String | - |  |
| 28 | d7PreventionLessonsLearned | String | - |  |
| 29 | d7PreventionHorizontalDeployment | String | - |  |
| 30 | d8ClosureClosedById | String | - | u_mes_mast_user._id |
| 31 | d8ClosureClosedBy | String | - |  |
| 32 | d8ClosureClosedAt | Date | Datetime |  |
| 33 | d8ClosureCustomerAccepted | Boolean | - |  |
| 34 | dueAt | Date | Datetime |  |
| 35 | currentDiscipline | String | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_qual_capaNonconformance

Kind: relationship | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 10 | nonconformanceName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_capaTeamMember

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | roleInTeam | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_capaContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | completedAt | Date | Datetime |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_capaCorrectiveAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | dueAt | Date | Datetime |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_capaImplementationAction

Kind: child | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | completedAt | Date | Datetime |  |
| 11 | verifiedById | String | - | u_mes_mast_user._id |
| 12 | verifiedBy | String | - |  |
| 13 | effective | Boolean | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_capaControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qual_capa | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | capaId | String | - | u_mes_qual_capa._id |
| 7 | capaName | String | - |  |
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

## u_mes_qual_pfmea

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
| 9 | itemRevision | String | - |  |
| 10 | version | Int32 | - |  |
| 11 | methodology | String | - |  |
| 12 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 13 | controlPlanName | String | - |  |
| 14 | originalDate | Date | Date |  |
| 15 | revisionDate | Date | Date |  |
| 16 | approvedById | String | - | u_mes_mast_user._id |
| 17 | approvedBy | String | - |  |
| 18 | approvedAt | Date | Datetime |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_qual_pfmeaCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qual_pfmea | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 7 | pfmeaName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | coreTeamUserId | String | - | u_mes_mast_user._id |
| 10 | coreTeamUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_qual_pfmeaLine

Kind: child | Data class: master | Parent: u_mes_qual_pfmea | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 7 | pfmeaName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | processFunction | String | - |  |
| 12 | failureMode | String | - |  |
| 13 | failureEffect | String | - |  |
| 14 | severity | Int32 | - |  |
| 15 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 16 | characteristicName | String | - |  |
| 17 | classification | String | - |  |
| 18 | failureCause | String | - |  |
| 19 | preventionControl | String | - |  |
| 20 | occurrence | Int32 | - |  |
| 21 | detectionControl | String | - |  |
| 22 | detection | Int32 | - |  |
| 23 | rpn | Int32 | - |  |
| 24 | actionPriority | String | - |  |
| 25 | recommendedAction | String | - |  |
| 26 | ownerUserId | String | - | u_mes_mast_user._id |
| 27 | ownerUserName | String | - |  |
| 28 | targetDate | Date | Date |  |
| 29 | actionTaken | String | - |  |
| 30 | revisedSeverity | Int32 | - |  |
| 31 | revisedOccurrence | Int32 | - |  |
| 32 | revisedDetection | Int32 | - |  |
| 33 | schemaVersion | Int32 | - |  |

## u_mes_qual_ppapSubmission

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

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
| 9 | customerId | String | - | u_mes_mast_customer._id |
| 10 | customerName | String | - |  |
| 11 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 12 | engineeringChangeName | String | - |  |
| 13 | submissionLevel | Int32 | - |  |
| 14 | submissionReason | String | - |  |
| 15 | controlPlanId | String | - | u_mes_qual_controlPlan._id |
| 16 | controlPlanName | String | - |  |
| 17 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 18 | pfmeaName | String | - |  |
| 19 | sampleQuantity | Int32 | - |  |
| 20 | significantProductionRunQuantity | Int32 | - |  |
| 21 | pswSignedById | String | - | u_mes_mast_user._id |
| 22 | pswSignedBy | String | - |  |
| 23 | pswSignedAt | Date | Datetime |  |
| 24 | submittedAt | Date | Datetime |  |
| 25 | customerDecision | String | - |  |
| 26 | customerDecisionAt | Date | Datetime |  |
| 27 | customerRemarks | String | - |  |
| 28 | interimApprovalValidTo | Date | Date |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_qual_ppapSubmissionElement

Kind: child | Data class: transaction | Parent: u_mes_qual_ppapSubmission | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | ppapSubmissionId | String | - | u_mes_qual_ppapSubmission._id |
| 7 | ppapSubmissionName | String | - |  |
| 8 | elementNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | required | Boolean | - |  |
| 11 | status | String | - |  |
| 12 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 13 | controlledDocumentName | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_ppapSubmissionMsaStudy

Kind: relationship | Data class: transaction | Parent: u_mes_qual_ppapSubmission | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | ppapSubmissionId | String | - | u_mes_qual_ppapSubmission._id |
| 7 | ppapSubmissionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 10 | msaStudyName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_gauge

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | gaugeTypeId | String | - | u_mes_qual_gaugeType._id |
| 8 | gaugeTypeName | String | - |  |
| 9 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 10 | manufacturerName | String | - |  |
| 11 | model | String | - |  |
| 12 | serialNo | String | - |  |
| 13 | rangeMin | Decimal128 | - |  |
| 14 | rangeMax | Decimal128 | - |  |
| 15 | rangeUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 16 | rangeUnitOfMeasureName | String | - |  |
| 17 | resolution | Decimal128 | - |  |
| 18 | accuracy | Decimal128 | - |  |
| 19 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 20 | storageLocationName | String | - |  |
| 21 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 22 | workCenterName | String | - |  |
| 23 | ownerUserId | String | - | u_mes_mast_user._id |
| 24 | ownerUserName | String | - |  |
| 25 | calibrationIntervalDays | Int32 | - |  |
| 26 | calibrationSource | String | - |  |
| 27 | calibrationSupplierId | String | - | u_mes_mast_supplier._id |
| 28 | calibrationSupplierName | String | - |  |
| 29 | lastCalibratedAt | Date | Datetime |  |
| 30 | nextCalibrationDueAt | Date | Date |  |
| 31 | lastGaugeCalibrationId | String | - | u_mes_qual_gaugeCalibration._id |
| 32 | lastGaugeCalibrationName | String | - |  |
| 33 | usageCount | Int32 | - |  |
| 34 | purchasedAt | Date | Datetime |  |
| 35 | isMasterGauge | Boolean | - |  |
| 36 | blockedForUse | Boolean | - |  |
| 37 | equipmentId | String | - | u_mes_mast_equipment._id |
| 38 | equipmentName | String | - |  |
| 39 | status | String | - |  |
| 40 | schemaVersion | Int32 | - |  |

## u_mes_qual_gaugeCalibration

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | gaugeId | String | - | u_mes_qual_gauge._id |
| 7 | gaugeName | String | - |  |
| 8 | calibrationType | String | - |  |
| 9 | calibratedAt | Date | Datetime |  |
| 10 | calibratedById | String | - | u_mes_mast_user._id |
| 11 | calibratedBy | String | - |  |
| 12 | calibrationSupplierId | String | - | u_mes_mast_supplier._id |
| 13 | calibrationSupplierName | String | - |  |
| 14 | masterStandardRef | String | - |  |
| 15 | traceability | String | - |  |
| 16 | temperatureC | Decimal128 | - |  |
| 17 | humidityPct | Decimal128 | - |  |
| 18 | asFoundResult | String | - |  |
| 19 | asLeftResult | String | - |  |
| 20 | overallResult | String | - |  |
| 21 | uncertainty | Decimal128 | - |  |
| 22 | adjustmentMade | Boolean | - |  |
| 23 | certificateNo | String | - |  |
| 24 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 25 | certificateControlledDocumentName | String | - |  |
| 26 | nextDueAt | Date | Date |  |
| 27 | impactAssessmentRequired | Boolean | - |  |
| 28 | remarks | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_qual_gaugeCalibrationReading

Kind: child | Data class: transaction | Parent: u_mes_qual_gaugeCalibration | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | gaugeCalibrationId | String | - | u_mes_qual_gaugeCalibration._id |
| 7 | gaugeCalibrationName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | nominal | Decimal128 | - |  |
| 10 | asFound | Decimal128 | - |  |
| 11 | asLeft | Decimal128 | - |  |
| 12 | tolerance | Decimal128 | - |  |
| 13 | withinTolerance | Boolean | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_msaStudy

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | gaugeId | String | - | u_mes_qual_gauge._id |
| 7 | gaugeName | String | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | studyType | String | - |  |
| 13 | studyMethod | String | - |  |
| 14 | studyDate | Date | Date |  |
| 15 | partsCount | Int32 | - |  |
| 16 | trialsCount | Int32 | - |  |
| 17 | resultsEquipmentVariation | Decimal128 | - |  |
| 18 | resultsAppraiserVariation | Decimal128 | - |  |
| 19 | resultsGrr | Decimal128 | - |  |
| 20 | resultsPartVariation | Decimal128 | - |  |
| 21 | resultsTotalVariation | Decimal128 | - |  |
| 22 | resultsGrrPctTolerance | Decimal128 | - |  |
| 23 | resultsGrrPctStudyVariation | Decimal128 | - |  |
| 24 | resultsNdc | Decimal128 | - |  |
| 25 | resultsBiasValue | Decimal128 | - |  |
| 26 | resultsKappa | Decimal128 | - |  |
| 27 | conclusion | String | - |  |
| 28 | actionRequired | Boolean | - |  |
| 29 | conductedById | String | - | u_mes_mast_user._id |
| 30 | conductedBy | String | - |  |
| 31 | approvedById | String | - | u_mes_mast_user._id |
| 32 | approvedBy | String | - |  |
| 33 | approvedAt | Date | Datetime |  |
| 34 | nextStudyDueAt | Date | Date |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_qual_msaStudyAppraiserUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_msaStudy | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 7 | msaStudyName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | appraiserUserId | String | - | u_mes_mast_user._id |
| 10 | appraiserUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_msaStudyTrial

Kind: child | Data class: transaction | Parent: u_mes_qual_msaStudy | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | msaStudyId | String | - | u_mes_qual_msaStudy._id |
| 7 | msaStudyName | String | - |  |
| 8 | appraiserUserId | String | - | u_mes_mast_user._id |
| 9 | appraiserUserName | String | - |  |
| 10 | partNo | Int32 | - |  |
| 11 | trialNo | Int32 | - |  |
| 12 | measuredValue | Decimal128 | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_qual_audit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | auditType | String | - |  |
| 8 | standard | String | - |  |
| 9 | scopeText | String | - |  |
| 10 | areaId | String | - | u_mes_mast_area._id |
| 11 | areaName | String | - |  |
| 12 | lineId | String | - | u_mes_mast_line._id |
| 13 | lineName | String | - |  |
| 14 | customerId | String | - | u_mes_mast_customer._id |
| 15 | customerName | String | - |  |
| 16 | layer | Int32 | - |  |
| 17 | leadAuditorUserId | String | - | u_mes_mast_user._id |
| 18 | leadAuditorUserName | String | - |  |
| 19 | auditeeUserId | String | - | u_mes_mast_user._id |
| 20 | auditeeUserName | String | - |  |
| 21 | plannedDate | Date | Date |  |
| 22 | startedAt | Date | Datetime |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 25 | checkSheetName | String | - |  |
| 26 | questionsCount | Int32 | - |  |
| 27 | conformingCount | Int32 | - |  |
| 28 | scorePct | Decimal128 | - |  |
| 29 | overallRating | String | - |  |
| 30 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 31 | reportControlledDocumentName | String | - |  |
| 32 | nextAuditDueAt | Date | Date |  |
| 33 | auditScheduleId | String | - | u_mes_qual_auditSchedule._id |
| 34 | auditScheduleName | String | - |  |
| 35 | dueDate | Date | Date |  |
| 36 | isMissed | Boolean | - |  |
| 37 | escalationLevel | Int32 | - |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |
| 40 | createdAt | Date | Datetime |  |
| 41 | createdById | String | - | u_mes_mast_user._id |
| 42 | createdBy | String | - |  |
| 43 | updatedAt | Date | Datetime |  |
| 44 | updatedById | String | - | u_mes_mast_user._id |
| 45 | updatedBy | String | - |  |

## u_mes_qual_auditAuditorUser

Kind: relationship | Data class: transaction | Parent: u_mes_qual_audit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | auditId | String | - | u_mes_qual_audit._id |
| 7 | auditName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | auditorUserId | String | - | u_mes_mast_user._id |
| 10 | auditorUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_auditFinding

Kind: child | Data class: transaction | Parent: u_mes_qual_audit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | auditId | String | - | u_mes_qual_audit._id |
| 7 | auditName | String | - |  |
| 8 | findingNo | Int32 | - |  |
| 9 | clause | String | - |  |
| 10 | description | String | - |  |
| 11 | grade | String | - |  |
| 12 | ownerUserId | String | - | u_mes_mast_user._id |
| 13 | ownerUserName | String | - |  |
| 14 | dueAt | Date | Datetime |  |
| 15 | closedAt | Date | Datetime |  |
| 16 | capaId | String | - | u_mes_qual_capa._id |
| 17 | capaName | String | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_qual_customerComplaint

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerId | String | - | u_mes_mast_customer._id |
| 7 | customerName | String | - |  |
| 8 | customerRefNo | String | - |  |
| 9 | complaintTypeId | String | - | u_mes_qual_complaintType._id |
| 10 | complaintTypeName | String | - |  |
| 11 | itemId | String | - | u_mes_prod_item._id |
| 12 | itemName | String | - |  |
| 13 | description | String | - |  |
| 14 | defectDescription | String | - |  |
| 15 | reportedAt | Date | Datetime |  |
| 16 | receivedById | String | - | u_mes_mast_user._id |
| 17 | receivedBy | String | - |  |
| 18 | occurredAt | Date | Datetime |  |
| 19 | customerLocation | String | - |  |
| 20 | quantityComplained | Int32 | - |  |
| 21 | quantityConfirmed | Int32 | - |  |
| 22 | vehicleModelId | String | - | u_mes_prod_vehicleModel._id |
| 23 | vehicleModelName | String | - |  |
| 24 | mileageKm | Decimal128 | - |  |
| 25 | severity | Int32 | - |  |
| 26 | isSafetyRelated | Boolean | - |  |
| 27 | containmentDueAt | Date | Datetime |  |
| 28 | containmentSentAt | Date | Datetime |  |
| 29 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 30 | nonconformanceName | String | - |  |
| 31 | capaId | String | - | u_mes_qual_capa._id |
| 32 | capaName | String | - |  |
| 33 | debitNoteInr | Decimal128 | - |  |
| 34 | ppmImpact | Int32 | - |  |
| 35 | sortingCostInr | Decimal128 | - |  |
| 36 | customerClosedAt | Date | Datetime |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintSerialNumber

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 7 | customerComplaintName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 10 | serialNumberName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintShipment

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 7 | customerComplaintName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | shipmentId | String | - | u_mes_matl_shipment._id |
| 10 | shipmentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintSuspectLot

Kind: relationship | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 7 | customerComplaintName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | suspectLotId | String | - | u_mes_plan_lot._id |
| 10 | suspectLotName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_qual_customerComplaintCommunication

Kind: child | Data class: transaction | Parent: u_mes_qual_customerComplaint | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 7 | customerComplaintName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | communicatedAt | Date | Datetime |  |
| 10 | direction | String | - |  |
| 11 | communicationSummary | String | - |  |
| 12 | authorUserId | String | - | u_mes_mast_user._id |
| 13 | authorUserName | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_qual_defectGroup

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

## u_mes_qual_gaugeType

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

## u_mes_qual_dispositionType

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
| 8 | requiresRework | Boolean | - |  |
| 9 | requiresScrap | Boolean | - |  |
| 10 | requiresCustomerApproval | Boolean | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_qual_complaintType

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

## u_mes_qual_characteristicPosition

Kind: child | Data class: master | Parent: u_mes_qual_characteristic | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - |  |
| 8 | positionNo | Int32 | - |  |
| 9 | positionName | String | - |  |
| 10 | nominal | Decimal128 | - |  |
| 11 | lowerSpecLimit | Decimal128 | - |  |
| 12 | upperSpecLimit | Decimal128 | - |  |
| 13 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - |  |
| 15 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 16 | curveEnvelopeName | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_qual_curveEnvelope

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 8 | characteristicName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - |  |
| 13 | operationId | String | - | u_mes_prod_operation._id |
| 14 | operationName | String | - |  |
| 15 | recipeId | String | - | u_mes_prod_recipe._id |
| 16 | recipeName | String | - |  |
| 17 | curveType | String | - |  |
| 18 | xQuantity | String | - |  |
| 19 | xUnitText | String | - |  |
| 20 | yQuantity | String | - |  |
| 21 | yUnitText | String | - |  |
| 22 | version | Int32 | - |  |
| 23 | goldenSampleSerialNo | String | - |  |
| 24 | referenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 25 | referenceControlledDocumentName | String | - |  |
| 26 | effectiveFrom | Date | Date |  |
| 27 | effectiveTo | Date | Date |  |
| 28 | approvedById | String | - | u_mes_mast_user._id |
| 29 | approvedBy | String | - |  |
| 30 | approvedAt | Date | Datetime |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |

## u_mes_qual_curveEnvelopeWindow

Kind: child | Data class: master | Parent: u_mes_qual_curveEnvelope | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 7 | curveEnvelopeName | String | - |  |
| 8 | windowNo | Int32 | - |  |
| 9 | windowType | String | - |  |
| 10 | xMin | Decimal128 | - |  |
| 11 | xMax | Decimal128 | - |  |
| 12 | yMin | Decimal128 | - |  |
| 13 | yMax | Decimal128 | - |  |
| 14 | entrySide | String | - |  |
| 15 | exitSide | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_qual_measurementCurve

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 7 | curveEnvelopeName | String | - |  |
| 8 | characteristicId | String | - | u_mes_qual_characteristic._id |
| 9 | characteristicName | String | - |  |
| 10 | positionNo | Int32 | - |  |
| 11 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String | - |  |
| 13 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 14 | serialNumberName | String | - |  |
| 15 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 16 | operationExecutionName | String | - |  |
| 17 | equipmentId | String | - | u_mes_mast_equipment._id |
| 18 | equipmentName | String | - |  |
| 19 | recipeVersion | String | - |  |
| 20 | capturedAt | Date | Datetime |  |
| 21 | pointCount | Int32 | - |  |
| 22 | peakX | Decimal128 | - |  |
| 23 | peakY | Decimal128 | - |  |
| 24 | finalX | Decimal128 | - |  |
| 25 | finalY | Decimal128 | - |  |
| 26 | result | String | - |  |
| 27 | failedWindowNo | Int32 | - |  |
| 28 | rawControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 29 | rawControlledDocumentName | String | - |  |
| 30 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 31 | inspectionResultName | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_qual_measurementCurvePoint

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 7 | measurementCurveName | String | - |  |
| 8 | pointNo | Int32 | - |  |
| 9 | sampledAt | Date | Datetime |  |
| 10 | xValue | Decimal128 | - |  |
| 11 | yValue | Decimal128 | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_qual_defectRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 7 | defectCodeName | String | - |  |
| 8 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | - |  |
| 10 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 11 | serialNumberName | String | - |  |
| 12 | lotId | String | - | u_mes_plan_lot._id |
| 13 | lotName | String | - |  |
| 14 | itemId | String | - | u_mes_prod_item._id |
| 15 | itemName | String | - |  |
| 16 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 17 | productVariantName | String | - |  |
| 18 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 19 | productionOrderName | String | - |  |
| 20 | detectedAtOperationId | String | - | u_mes_prod_operation._id |
| 21 | detectedAtOperationName | String | - |  |
| 22 | detectedAtWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 23 | detectedAtWorkCenterName | String | - |  |
| 24 | originOperationId | String | - | u_mes_prod_operation._id |
| 25 | originOperationName | String | - |  |
| 26 | isFirstFail | Boolean | - |  |
| 27 | positionNo | Int32 | - |  |
| 28 | defectLocationText | String | - |  |
| 29 | quantity | Int32 | - |  |
| 30 | fourMCategory | String | - |  |
| 31 | operatorUserId | String | - | u_mes_mast_user._id |
| 32 | operatorUserName | String | - |  |
| 33 | equipmentId | String | - | u_mes_mast_equipment._id |
| 34 | equipmentName | String | - |  |
| 35 | componentLotId | String | - | u_mes_plan_lot._id |
| 36 | componentLotName | String | - |  |
| 37 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 38 | operationExecutionName | String | - |  |
| 39 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 40 | inspectionResultName | String | - |  |
| 41 | shiftId | String | - | u_mes_mast_shift._id |
| 42 | shiftName | String | - |  |
| 43 | productionDate | Date | Date |  |
| 44 | detectedAt | Date | Datetime |  |
| 45 | detectedById | String | - | u_mes_mast_user._id |
| 46 | detectedBy | String | - |  |
| 47 | imageControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 48 | imageControlledDocumentName | String | - |  |
| 49 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 50 | nonconformanceName | String | - |  |
| 51 | reworkOrderId | String | - | u_mes_qual_reworkOrder._id |
| 52 | reworkOrderName | String | - |  |
| 53 | scrapRecordId | String | - | u_mes_qual_scrapRecord._id |
| 54 | scrapRecordName | String | - |  |
| 55 | status | String | - |  |
| 56 | schemaVersion | Int32 | - |  |
| 57 | createdAt | Date | Datetime |  |
| 58 | createdById | String | - | u_mes_mast_user._id |
| 59 | createdBy | String | - |  |
| 60 | updatedAt | Date | Datetime |  |
| 61 | updatedById | String | - | u_mes_mast_user._id |
| 62 | updatedBy | String | - |  |

## u_mes_qual_auditSchedule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | auditType | String | - |  |
| 8 | layer | Int32 | - |  |
| 9 | areaId | String | - | u_mes_mast_area._id |
| 10 | areaName | String | - |  |
| 11 | lineId | String | - | u_mes_mast_line._id |
| 12 | lineName | String | - |  |
| 13 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 14 | workCenterName | String | - |  |
| 15 | checkSheetId | String | - | u_mes_qual_checkSheet._id |
| 16 | checkSheetName | String | - |  |
| 17 | frequencyType | String | - |  |
| 18 | frequencyValue | Decimal128 | - |  |
| 19 | auditorRoleId | String | - | u_mes_mast_role._id |
| 20 | auditorRoleName | String | - |  |
| 21 | auditorUserId | String | - | u_mes_mast_user._id |
| 22 | auditorUserName | String | - |  |
| 23 | toleranceHours | Int32 | - |  |
| 24 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 25 | escalationRuleName | String | - |  |
| 26 | nextDueDate | Date | Date |  |
| 27 | validFrom | Date | Date |  |
| 28 | validTo | Date | Date |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |

## u_mes_qual_inspectionPlanProductVariant

Kind: relationship | Data class: master | Parent: u_mes_qual_inspectionPlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 7 | inspectionPlanName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_qual_environmentalMonitoringPoint

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | areaId | String | - | u_mes_mast_area._id |
| 8 | areaName | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | monitoredParameter | String | - |  |
| 12 | parameterUnitText | String | - |  |
| 13 | limitDirection | String | - |  |
| 14 | alertLimit | Decimal128 | - |  |
| 15 | actionLimit | Decimal128 | - |  |
| 16 | lowerActionLimit | Decimal128 | - |  |
| 17 | samplingFrequency | String | - |  |
| 18 | processTagId | String | - | u_mes_perf_processTag._id |
| 19 | processTagName | String | - |  |
| 20 | status | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_qual_environmentalMonitoringResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | environmentalMonitoringPointId | String | - | u_mes_qual_environmentalMonitoringPoint._id |
| 7 | environmentalMonitoringPointName | String | - |  |
| 8 | sampledAt | Date | Datetime |  |
| 9 | measuredValue | Decimal128 | - |  |
| 10 | limitEvaluation | String | - |  |
| 11 | sampledById | String | - | u_mes_mast_user._id |
| 12 | sampledBy | String | - |  |
| 13 | gaugeId | String | - | u_mes_qual_gauge._id |
| 14 | gaugeName | String | - |  |
| 15 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 16 | nonconformanceName | String | - |  |
| 17 | productImpactText | String | - |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |
| 20 | createdAt | Date | Datetime |  |
| 21 | createdById | String | - | u_mes_mast_user._id |
| 22 | createdBy | String | - |  |
| 23 | updatedAt | Date | Datetime |  |
| 24 | updatedById | String | - | u_mes_mast_user._id |
| 25 | updatedBy | String | - |  |

## u_mes_qual_retentionSample

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | lotId | String | - | u_mes_plan_lot._id |
| 9 | lotName | String | - |  |
| 10 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - |  |
| 12 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String | - |  |
| 14 | sampleType | String | - |  |
| 15 | sampleQuantity | Int32 | - |  |
| 16 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - |  |
| 18 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | storageLocationName | String | - |  |
| 20 | collectedById | String | - | u_mes_mast_user._id |
| 21 | collectedBy | String | - |  |
| 22 | collectedAt | Date | Datetime |  |
| 23 | retainUntilDate | Date | Date |  |
| 24 | withdrawnAt | Date | Datetime |  |
| 25 | withdrawalReason | String | - |  |
| 26 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 27 | customerComplaintName | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_qual_riskAssessment

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | relatedCollectionName | String | - |  |
| 8 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 9 | relatedEntityName | String | - |  |
| 10 | assessmentMethod | String | - |  |
| 11 | scopeText | String | - |  |
| 12 | initialRiskLevel | String | - |  |
| 13 | residualRiskLevel | String | - |  |
| 14 | riskControlsText | String | - |  |
| 15 | pfmeaId | String | - | u_mes_qual_pfmea._id |
| 16 | pfmeaName | String | - |  |
| 17 | acceptanceDecision | String | - |  |
| 18 | approvedById | String | - | u_mes_mast_user._id |
| 19 | approvedBy | String | - |  |
| 20 | approvedAt | Date | Datetime |  |
| 21 | nextReviewDate | Date | Date |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_qual_productQualityReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | reviewPeriodFromDate | Date | Date |  |
| 9 | reviewPeriodToDate | Date | Date |  |
| 10 | lotsProducedCount | Int32 | - |  |
| 11 | lotsReleasedCount | Int32 | - |  |
| 12 | lotsRejectedCount | Int32 | - |  |
| 13 | nonconformanceCount | Int32 | - |  |
| 14 | deviationPermitCount | Int32 | - |  |
| 15 | customerComplaintCount | Int32 | - |  |
| 16 | capaCount | Int32 | - |  |
| 17 | engineeringChangeCount | Int32 | - |  |
| 18 | productRecallCount | Int32 | - |  |
| 19 | processCapabilityText | String | - |  |
| 20 | conclusionText | String | - |  |
| 21 | actionsText | String | - |  |
| 22 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 23 | reportControlledDocumentName | String | - |  |
| 24 | approvedById | String | - | u_mes_mast_user._id |
| 25 | approvedBy | String | - |  |
| 26 | approvedAt | Date | Datetime |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_qual_productRecall

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | recallClass | String | - |  |
| 8 | recallScope | String | - |  |
| 9 | reasonText | String | - |  |
| 10 | customerId | String | - | u_mes_mast_customer._id |
| 11 | customerName | String | - |  |
| 12 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 13 | customerComplaintName | String | - |  |
| 14 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 15 | nonconformanceName | String | - |  |
| 16 | traceInvestigationId | String | - | u_mes_trac_traceInvestigation._id |
| 17 | traceInvestigationName | String | - |  |
| 18 | capaId | String | - | u_mes_qual_capa._id |
| 19 | capaName | String | - |  |
| 20 | initiatedById | String | - | u_mes_mast_user._id |
| 21 | initiatedBy | String | - |  |
| 22 | initiatedAt | Date | Datetime |  |
| 23 | authorityNotified | Boolean | - |  |
| 24 | authorityNotifiedAt | Date | Datetime |  |
| 25 | quantityShipped | Int32 | - |  |
| 26 | quantityRecovered | Int32 | - |  |
| 27 | effectivenessCheckCompleted | Boolean | - |  |
| 28 | closedById | String | - | u_mes_mast_user._id |
| 29 | closedBy | String | - |  |
| 30 | closedAt | Date | Datetime |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_qual_productRecallLot

Kind: child | Data class: transaction | Parent: u_mes_qual_productRecall | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productRecallId | String | - | u_mes_qual_productRecall._id |
| 7 | productRecallName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | shipmentId | String | - | u_mes_matl_shipment._id |
| 12 | shipmentName | String | - |  |
| 13 | quantityShipped | Int32 | - |  |
| 14 | quantityRecovered | Int32 | - |  |
| 15 | schemaVersion | Int32 | - |  |
| 16 | createdAt | Date | Datetime |  |
| 17 | createdById | String | - | u_mes_mast_user._id |
| 18 | createdBy | String | - |  |
| 19 | updatedAt | Date | Datetime |  |
| 20 | updatedById | String | - | u_mes_mast_user._id |
| 21 | updatedBy | String | - |  |

## u_mes_qual_processValidation

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

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
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | validationStage | String | - |  |
| 12 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 13 | engineeringChangeName | String | - |  |
| 14 | protocolControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 15 | protocolControlledDocumentName | String | - |  |
| 16 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 17 | reportControlledDocumentName | String | - |  |
| 18 | plannedLotCount | Int32 | - |  |
| 19 | executedLotCount | Int32 | - |  |
| 20 | acceptanceCriteriaText | String | - |  |
| 21 | resultText | String | - |  |
| 22 | plannedStartDate | Date | Date |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | approvedById | String | - | u_mes_mast_user._id |
| 25 | approvedBy | String | - |  |
| 26 | approvedAt | Date | Datetime |  |
| 27 | nextReviewDate | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |
