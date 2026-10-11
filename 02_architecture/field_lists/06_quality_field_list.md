# Field list - Quality (qlt)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/06_quality/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_qlt_characteristic

Kind: entity | Data class: master | Parent: - | _id pattern: CHR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | itemId | String | u_mes_prd_item._id |
| 7 | itemName | String |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | characteristicType | String |  |
| 11 | classification | String |  |
| 12 | drawingZone | String |  |
| 13 | balloonNo | String |  |
| 14 | dataType | String |  |
| 15 | nominal | Decimal128 |  |
| 16 | lowerSpecLimit | Decimal128 |  |
| 17 | upperSpecLimit | Decimal128 |  |
| 18 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 19 | unitOfMeasureName | String |  |
| 20 | toleranceType | String |  |
| 21 | measurementMethod | String |  |
| 22 | gaugeId | String | u_mes_qlt_gauge._id |
| 23 | gaugeName | String |  |
| 24 | gaugeType | String |  |
| 25 | attributeAcceptance | String |  |
| 26 | isSpc | Boolean |  |
| 27 | targetCpk | Decimal128 |  |
| 28 | reactionPlan | String |  |
| 29 | source | String |  |
| 30 | status | String |  |
| 31 | schemaVersion | Int32 |  |

## u_mes_qlt_controlPlan

Kind: entity | Data class: master | Parent: - | _id pattern: CP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | itemRevision | String |  |
| 8 | phase | String |  |
| 9 | version | Int32 |  |
| 10 | routingId | String | u_mes_prd_routing._id |
| 11 | routingName | String |  |
| 12 | pfmeaId | String | u_mes_qlt_pfmea._id |
| 13 | pfmeaName | String |  |
| 14 | customerApprovalDate | Date |  |
| 15 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 16 | engineeringChangeName | String |  |
| 17 | preparedById | String | u_mes_mdm_user._id |
| 18 | preparedBy | String |  |
| 19 | approvedById | String | u_mes_mdm_user._id |
| 20 | approvedBy | String |  |
| 21 | approvedAt | Date |  |
| 22 | effectiveFrom | Date |  |
| 23 | originalDate | Date |  |
| 24 | revisionDate | Date |  |
| 25 | status | String |  |
| 26 | schemaVersion | Int32 |  |

## u_mes_qlt_controlPlanCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qlt_controlPlan | _id pattern: <controlPlanId>-CTU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | controlPlanId | String | u_mes_qlt_controlPlan._id |
| 6 | controlPlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | coreTeamUserId | String | u_mes_mdm_user._id |
| 9 | coreTeamUserName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_qlt_controlPlanLine

Kind: child | Data class: master | Parent: u_mes_qlt_controlPlan | _id pattern: <controlPlanId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | controlPlanId | String | u_mes_qlt_controlPlan._id |
| 6 | controlPlanName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | processName | String |  |
| 11 | equipmentText | String |  |
| 12 | characteristicId | String | u_mes_qlt_characteristic._id |
| 13 | characteristicName | String |  |
| 14 | classification | String |  |
| 15 | specification | String |  |
| 16 | gaugeId | String | u_mes_qlt_gauge._id |
| 17 | gaugeName | String |  |
| 18 | measurementTechnique | String |  |
| 19 | sampleSize | Int32 |  |
| 20 | sampleFrequency | String |  |
| 21 | controlMethod | String |  |
| 22 | reactionPlan | String |  |
| 23 | responsible | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_qlt_inspectionPlan

Kind: entity | Data class: master | Parent: - | _id pattern: IP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | controlPlanId | String | u_mes_qlt_controlPlan._id |
| 7 | controlPlanName | String |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | operationId | String | u_mes_prd_operation._id |
| 11 | operationName | String |  |
| 12 | workCenterId | String | u_mes_mdm_workCenter._id |
| 13 | workCenterName | String |  |
| 14 | planType | String |  |
| 15 | version | Int32 |  |
| 16 | collectionTrigger | String |  |
| 17 | samplingPlanId | String | u_mes_qlt_samplingPlan._id |
| 18 | samplingPlanName | String |  |
| 19 | blockOnFail | Boolean |  |
| 20 | effectiveFrom | Date |  |
| 21 | effectiveTo | Date |  |
| 22 | approvedById | String | u_mes_mdm_user._id |
| 23 | approvedBy | String |  |
| 24 | approvedAt | Date |  |
| 25 | status | String |  |
| 26 | schemaVersion | Int32 |  |

## u_mes_qlt_inspectionPlanLine

Kind: child | Data class: master | Parent: u_mes_qlt_inspectionPlan | _id pattern: <inspectionPlanId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | inspectionPlanId | String | u_mes_qlt_inspectionPlan._id |
| 6 | inspectionPlanName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | characteristicId | String | u_mes_qlt_characteristic._id |
| 9 | characteristicName | String |  |
| 10 | gaugeId | String | u_mes_qlt_gauge._id |
| 11 | gaugeName | String |  |
| 12 | sampleSize | Int32 |  |
| 13 | frequencyType | String |  |
| 14 | frequencyValue | Decimal128 |  |
| 15 | recordType | String |  |
| 16 | autoNcOnFail | Boolean |  |
| 17 | defectCodeId | String | u_mes_qlt_defectCode._id |
| 18 | defectCodeName | String |  |
| 19 | overrideAllowed | Boolean |  |
| 20 | schemaVersion | Int32 |  |

## u_mes_qlt_samplingPlan

Kind: entity | Data class: master | Parent: - | _id pattern: SMP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | samplingType | String |  |
| 7 | standard | String |  |
| 8 | inspectionLevel | String |  |
| 9 | aql | Decimal128 |  |
| 10 | frequencyType | String |  |
| 11 | frequencyEveryNUnits | Int32 |  |
| 12 | frequencyEveryMinutes | Int32 |  |
| 13 | skipLotEnabled | Boolean |  |
| 14 | skipLotConsecutiveAcceptedToSkip | Int32 |  |
| 15 | skipLotSkipFraction | Decimal128 |  |
| 16 | switchingRules | String |  |
| 17 | status | String |  |
| 18 | schemaVersion | Int32 |  |

## u_mes_qlt_samplingPlanSizeRow

Kind: child | Data class: master | Parent: u_mes_qlt_samplingPlan | _id pattern: <samplingPlanId>-SR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | samplingPlanId | String | u_mes_qlt_samplingPlan._id |
| 6 | samplingPlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lotSizeFrom | Int32 |  |
| 9 | lotSizeTo | Int32 |  |
| 10 | sampleSize | Int32 |  |
| 11 | acceptNumber | Int32 |  |
| 12 | rejectNumber | Int32 |  |
| 13 | schemaVersion | Int32 |  |

## u_mes_qlt_checkSheet

Kind: entity | Data class: master | Parent: - | _id pattern: CKS-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | checkSheetType | String |  |
| 7 | workCenterId | String | u_mes_mdm_workCenter._id |
| 8 | workCenterName | String |  |
| 9 | equipmentId | String | u_mes_mdm_equipment._id |
| 10 | equipmentName | String |  |
| 11 | operationId | String | u_mes_prd_operation._id |
| 12 | operationName | String |  |
| 13 | itemId | String | u_mes_prd_item._id |
| 14 | itemName | String |  |
| 15 | version | Int32 |  |
| 16 | frequency | String |  |
| 17 | masterSampleRequired | Boolean |  |
| 18 | estimatedMinutes | Int32 |  |
| 19 | effectiveFrom | Date |  |
| 20 | approvedById | String | u_mes_mdm_user._id |
| 21 | approvedBy | String |  |
| 22 | approvedAt | Date |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_qlt_checkSheetItem

Kind: child | Data class: master | Parent: u_mes_qlt_checkSheet | _id pattern: <checkSheetId>-I<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | checkSheetId | String | u_mes_qlt_checkSheet._id |
| 6 | checkSheetName | String |  |
| 7 | itemNo | Int32 |  |
| 8 | question | String |  |
| 9 | answerType | String |  |
| 10 | expectedAnswer | String |  |
| 11 | lowerLimit | Decimal128 |  |
| 12 | upperLimit | Decimal128 |  |
| 13 | unitText | String |  |
| 14 | isCritical | Boolean |  |
| 15 | reactionOnFail | Boolean |  |
| 16 | schemaVersion | Int32 |  |

## u_mes_qlt_checkSheetResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: CKR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | checkSheetId | String | u_mes_qlt_checkSheet._id |
| 6 | checkSheetName | String |  |
| 7 | checkSheetVersion | Int32 |  |
| 8 | workCenterId | String | u_mes_mdm_workCenter._id |
| 9 | workCenterName | String |  |
| 10 | equipmentId | String | u_mes_mdm_equipment._id |
| 11 | equipmentName | String |  |
| 12 | shiftId | String | u_mes_mdm_shift._id |
| 13 | shiftName | String |  |
| 14 | productionDate | Date |  |
| 15 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 16 | productionOrderName | String |  |
| 17 | performedById | String | u_mes_mdm_user._id |
| 18 | performedBy | String |  |
| 19 | startedAt | Date |  |
| 20 | completedAt | Date |  |
| 21 | overallResult | String |  |
| 22 | failedCount | Int32 |  |
| 23 | reactionTaken | String |  |
| 24 | verifiedById | String | u_mes_mdm_user._id |
| 25 | verifiedBy | String |  |
| 26 | verifiedAt | Date |  |
| 27 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 28 | nonconformanceName | String |  |
| 29 | status | String |  |
| 30 | schemaVersion | Int32 |  |
| 31 | createdAt | Date |  |
| 32 | createdById | String | u_mes_mdm_user._id |
| 33 | createdBy | String |  |
| 34 | updatedAt | Date |  |
| 35 | updatedById | String | u_mes_mdm_user._id |
| 36 | updatedBy | String |  |

## u_mes_qlt_checkSheetResultAnswer

Kind: child | Data class: transaction | Parent: u_mes_qlt_checkSheetResult | _id pattern: <checkSheetResultId>-A<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | checkSheetResultId | String | u_mes_qlt_checkSheetResult._id |
| 6 | checkSheetResultName | String |  |
| 7 | itemNo | Int32 |  |
| 8 | answerText | String |  |
| 9 | answerNumber | Decimal128 |  |
| 10 | passed | Boolean |  |
| 11 | comment | String |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_qlt_inspectionResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: IR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | inspectionPlanId | String | u_mes_qlt_inspectionPlan._id |
| 6 | inspectionPlanName | String |  |
| 7 | planLineNo | Int32 |  |
| 8 | characteristicId | String | u_mes_qlt_characteristic._id |
| 9 | characteristicName | String |  |
| 10 | itemId | String | u_mes_prd_item._id |
| 11 | itemName | String |  |
| 12 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 13 | wipUnitName | String |  |
| 14 | lotId | String | u_mes_exe_lot._id |
| 15 | lotName | String |  |
| 16 | goodsReceiptId | String | u_mes_mat_goodsReceipt._id |
| 17 | goodsReceiptName | String |  |
| 18 | operationExecutionId | String | u_mes_exe_operationExecution._id |
| 19 | operationExecutionName | String |  |
| 20 | operationId | String | u_mes_prd_operation._id |
| 21 | operationName | String |  |
| 22 | workCenterId | String | u_mes_mdm_workCenter._id |
| 23 | workCenterName | String |  |
| 24 | inspectionType | String |  |
| 25 | sampleNo | Int32 |  |
| 26 | measuredValue | Decimal128 |  |
| 27 | attributeResult | String |  |
| 28 | nominal | Decimal128 |  |
| 29 | lowerSpecLimit | Decimal128 |  |
| 30 | upperSpecLimit | Decimal128 |  |
| 31 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 32 | unitOfMeasureName | String |  |
| 33 | deviation | Decimal128 |  |
| 34 | result | String |  |
| 35 | gaugeId | String | u_mes_qlt_gauge._id |
| 36 | gaugeName | String |  |
| 37 | measuredById | String | u_mes_mdm_user._id |
| 38 | measuredBy | String |  |
| 39 | measuredAt | Date |  |
| 40 | source | String |  |
| 41 | defectCodeId | String | u_mes_qlt_defectCode._id |
| 42 | defectCodeName | String |  |
| 43 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 44 | nonconformanceName | String |  |
| 45 | overridden | Boolean |  |
| 46 | remarks | String |  |
| 47 | status | String |  |
| 48 | schemaVersion | Int32 |  |
| 49 | createdAt | Date |  |
| 50 | createdById | String | u_mes_mdm_user._id |
| 51 | createdBy | String |  |
| 52 | updatedAt | Date |  |
| 53 | updatedById | String | u_mes_mdm_user._id |
| 54 | updatedBy | String |  |

## u_mes_qlt_spcChart

Kind: entity | Data class: master | Parent: - | _id pattern: SPC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | characteristicId | String | u_mes_qlt_characteristic._id |
| 7 | characteristicName | String |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | workCenterId | String | u_mes_mdm_workCenter._id |
| 11 | workCenterName | String |  |
| 12 | equipmentId | String | u_mes_mdm_equipment._id |
| 13 | equipmentName | String |  |
| 14 | chartType | String |  |
| 15 | subgroupSize | Int32 |  |
| 16 | subgroupFrequency | String |  |
| 17 | lowerSpecLimit | Decimal128 |  |
| 18 | upperSpecLimit | Decimal128 |  |
| 19 | capabilityCp | Decimal128 |  |
| 20 | capabilityCpk | Decimal128 |  |
| 21 | capabilityPp | Decimal128 |  |
| 22 | capabilityPpk | Decimal128 |  |
| 23 | capabilityCalculatedAt | Date |  |
| 24 | capabilitySampleCount | Int32 |  |
| 25 | ownerUserId | String | u_mes_mdm_user._id |
| 26 | ownerUserName | String |  |
| 27 | reactionPlan | String |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |

## u_mes_qlt_spcChartControlLimit

Kind: child | Data class: master | Parent: u_mes_qlt_spcChart | _id pattern: <spcChartId>-CL<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcChartId | String | u_mes_qlt_spcChart._id |
| 6 | spcChartName | String |  |
| 7 | revisionNo | Int32 |  |
| 8 | effectiveFrom | Date |  |
| 9 | ucl | Decimal128 |  |
| 10 | centerLine | Decimal128 |  |
| 11 | lcl | Decimal128 |  |
| 12 | uclRange | Decimal128 |  |
| 13 | centerLineRange | Decimal128 |  |
| 14 | lclRange | Decimal128 |  |
| 15 | basedOnSubgroups | Int32 |  |
| 16 | schemaVersion | Int32 |  |

## u_mes_qlt_spcChartRule

Kind: valueList | Data class: master | Parent: u_mes_qlt_spcChart | _id pattern: <spcChartId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcChartId | String | u_mes_qlt_spcChart._id |
| 6 | spcChartName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | rule | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_qlt_spcSample

Kind: entity | Data class: transaction | Parent: - | _id pattern: SPS-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcChartId | String | u_mes_qlt_spcChart._id |
| 6 | spcChartName | String |  |
| 7 | characteristicId | String | u_mes_qlt_characteristic._id |
| 8 | characteristicName | String |  |
| 9 | workCenterId | String | u_mes_mdm_workCenter._id |
| 10 | workCenterName | String |  |
| 11 | subgroupNo | Int32 |  |
| 12 | sampledAt | Date |  |
| 13 | sampledById | String | u_mes_mdm_user._id |
| 14 | sampledBy | String |  |
| 15 | shiftId | String | u_mes_mdm_shift._id |
| 16 | shiftName | String |  |
| 17 | subgroupMean | Decimal128 |  |
| 18 | subgroupRange | Decimal128 |  |
| 19 | stdDev | Decimal128 |  |
| 20 | ucl | Decimal128 |  |
| 21 | lcl | Decimal128 |  |
| 22 | centerLine | Decimal128 |  |
| 23 | inControl | Boolean |  |
| 24 | assignableCause | String |  |
| 25 | correctiveAction | String |  |
| 26 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 27 | nonconformanceName | String |  |
| 28 | excludedFromLimits | Boolean |  |
| 29 | status | String |  |
| 30 | schemaVersion | Int32 |  |
| 31 | createdAt | Date |  |
| 32 | createdById | String | u_mes_mdm_user._id |
| 33 | createdBy | String |  |
| 34 | updatedAt | Date |  |
| 35 | updatedById | String | u_mes_mdm_user._id |
| 36 | updatedBy | String |  |

## u_mes_qlt_spcSampleReading

Kind: valueList | Data class: transaction | Parent: u_mes_qlt_spcSample | _id pattern: <spcSampleId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcSampleId | String | u_mes_qlt_spcSample._id |
| 6 | spcSampleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | reading | Decimal128 |  |
| 9 | schemaVersion | Int32 |  |
| 10 | createdAt | Date |  |
| 11 | createdById | String | u_mes_mdm_user._id |
| 12 | createdBy | String |  |
| 13 | updatedAt | Date |  |
| 14 | updatedById | String | u_mes_mdm_user._id |
| 15 | updatedBy | String |  |

## u_mes_qlt_spcSampleInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_spcSample | _id pattern: <spcSampleId>-IR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcSampleId | String | u_mes_qlt_spcSample._id |
| 6 | spcSampleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | inspectionResultId | String | u_mes_qlt_inspectionResult._id |
| 9 | inspectionResultName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_spcSampleViolation

Kind: child | Data class: transaction | Parent: u_mes_qlt_spcSample | _id pattern: <spcSampleId>-V<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | spcSampleId | String | u_mes_qlt_spcSample._id |
| 6 | spcSampleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | rule | String |  |
| 9 | description | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_defectCode

Kind: entity | Data class: master | Parent: - | _id pattern: DEF-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | defectGroup | String |  |
| 7 | description | String |  |
| 8 | severity | Int32 |  |
| 9 | defaultDisposition | String |  |
| 10 | dispositionRoutingId | String | u_mes_prd_routing._id |
| 11 | dispositionRoutingName | String |  |
| 12 | isSafetyRelated | Boolean |  |
| 13 | requiresPhoto | Boolean |  |
| 14 | requiresHold | Boolean |  |
| 15 | scrapCostCategory | String |  |
| 16 | customerDefectCode | String |  |
| 17 | pfmeaFailureMode | String |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |

## u_mes_qlt_defectCodeApplicableOperation

Kind: relationship | Data class: master | Parent: u_mes_qlt_defectCode | _id pattern: <defectCodeId>-AO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | defectCodeId | String | u_mes_qlt_defectCode._id |
| 6 | defectCodeName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | applicableOperationId | String | u_mes_prd_operation._id |
| 9 | applicableOperationName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_qlt_nonconformance

Kind: entity | Data class: transaction | Parent: - | _id pattern: NCR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | description | String |  |
| 7 | ncType | String |  |
| 8 | source | String |  |
| 9 | detectedAt | Date |  |
| 10 | detectedById | String | u_mes_mdm_user._id |
| 11 | detectedBy | String |  |
| 12 | detectedAtOperationId | String | u_mes_prd_operation._id |
| 13 | detectedAtOperationName | String |  |
| 14 | detectedAtWorkCenterId | String | u_mes_mdm_workCenter._id |
| 15 | detectedAtWorkCenterName | String |  |
| 16 | originOperationId | String | u_mes_prd_operation._id |
| 17 | originOperationName | String |  |
| 18 | itemId | String | u_mes_prd_item._id |
| 19 | itemName | String |  |
| 20 | defectCodeId | String | u_mes_qlt_defectCode._id |
| 21 | defectCodeName | String |  |
| 22 | supplierId | String | u_mes_mdm_supplier._id |
| 23 | supplierName | String |  |
| 24 | customerId | String | u_mes_mdm_customer._id |
| 25 | customerName | String |  |
| 26 | quantityAffected | Int32 |  |
| 27 | quantityRejected | Int32 |  |
| 28 | qualityHoldId | String | u_mes_qlt_qualityHold._id |
| 29 | qualityHoldName | String |  |
| 30 | capaId | String | u_mes_qlt_capa._id |
| 31 | capaName | String |  |
| 32 | rootCauseSummary | String |  |
| 33 | severity | Int32 |  |
| 34 | costInr | Decimal128 |  |
| 35 | closedAt | Date |  |
| 36 | closedById | String | u_mes_mdm_user._id |
| 37 | closedBy | String |  |
| 38 | status | String |  |
| 39 | schemaVersion | Int32 |  |
| 40 | createdAt | Date |  |
| 41 | createdById | String | u_mes_mdm_user._id |
| 42 | createdBy | String |  |
| 43 | updatedAt | Date |  |
| 44 | updatedById | String | u_mes_mdm_user._id |
| 45 | updatedBy | String |  |

## u_mes_qlt_nonconformanceAffectedObject

Kind: child | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-AO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | relatedCollectionName | String |  |
| 9 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String |  |
| 11 | quantity | Int32 |  |
| 12 | disposition | String |  |
| 13 | dispositionById | String | u_mes_mdm_user._id |
| 14 | dispositionBy | String |  |
| 15 | dispositionAt | Date |  |
| 16 | schemaVersion | Int32 |  |
| 17 | createdAt | Date |  |
| 18 | createdById | String | u_mes_mdm_user._id |
| 19 | createdBy | String |  |
| 20 | updatedAt | Date |  |
| 21 | updatedById | String | u_mes_mdm_user._id |
| 22 | updatedBy | String |  |

## u_mes_qlt_nonconformanceContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-CA<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | actionNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mdm_user._id |
| 10 | ownerUserName | String |  |
| 11 | completedAt | Date |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_qlt_nonconformanceInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-IR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | inspectionResultId | String | u_mes_qlt_inspectionResult._id |
| 9 | inspectionResultName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_nonconformanceReworkOrder

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-RO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | reworkOrderId | String | u_mes_qlt_reworkOrder._id |
| 9 | reworkOrderName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_nonconformanceScrapRecord

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-SR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | scrapRecordId | String | u_mes_qlt_scrapRecord._id |
| 9 | scrapRecordName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_nonconformancePhotoControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-PCD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | photoControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 9 | photoControlledDocumentName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_nonconformanceMrbUser

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_nonconformance | _id pattern: <nonconformanceId>-MU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | mrbUserId | String | u_mes_mdm_user._id |
| 9 | mrbUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_reworkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: RWK-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | lotId | String | u_mes_exe_lot._id |
| 8 | lotName | String |  |
| 9 | itemId | String | u_mes_prd_item._id |
| 10 | itemName | String |  |
| 11 | quantity | Int32 |  |
| 12 | reworkRoutingId | String | u_mes_prd_routing._id |
| 13 | reworkRoutingName | String |  |
| 14 | reworkType | String |  |
| 15 | instruction | String |  |
| 16 | workCenterId | String | u_mes_mdm_workCenter._id |
| 17 | workCenterName | String |  |
| 18 | issuedById | String | u_mes_mdm_user._id |
| 19 | issuedBy | String |  |
| 20 | issuedAt | Date |  |
| 21 | startedAt | Date |  |
| 22 | completedAt | Date |  |
| 23 | reinspectionResult | String |  |
| 24 | reinspectedById | String | u_mes_mdm_user._id |
| 25 | reinspectedBy | String |  |
| 26 | reinspectedAt | Date |  |
| 27 | quantityRecovered | Int32 |  |
| 28 | quantityScrapped | Int32 |  |
| 29 | reworkAttemptNo | Int32 |  |
| 30 | returnStepNo | Int32 |  |
| 31 | labourMinutes | Int32 |  |
| 32 | status | String |  |
| 33 | schemaVersion | Int32 |  |
| 34 | createdAt | Date |  |
| 35 | createdById | String | u_mes_mdm_user._id |
| 36 | createdBy | String |  |
| 37 | updatedAt | Date |  |
| 38 | updatedById | String | u_mes_mdm_user._id |
| 39 | updatedBy | String |  |

## u_mes_qlt_reworkOrderWipUnit

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_reworkOrder | _id pattern: <reworkOrderId>-WU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | reworkOrderId | String | u_mes_qlt_reworkOrder._id |
| 6 | reworkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 9 | wipUnitName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_reworkOrderStep

Kind: child | Data class: transaction | Parent: u_mes_qlt_reworkOrder | _id pattern: <reworkOrderId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | reworkOrderId | String | u_mes_qlt_reworkOrder._id |
| 6 | reworkOrderName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | description | String |  |
| 11 | completedAt | Date |  |
| 12 | completedById | String | u_mes_mdm_user._id |
| 13 | completedBy | String |  |
| 14 | schemaVersion | Int32 |  |
| 15 | createdAt | Date |  |
| 16 | createdById | String | u_mes_mdm_user._id |
| 17 | createdBy | String |  |
| 18 | updatedAt | Date |  |
| 19 | updatedById | String | u_mes_mdm_user._id |
| 20 | updatedBy | String |  |

## u_mes_qlt_scrapRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: SCR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String |  |
| 7 | defectCodeId | String | u_mes_qlt_defectCode._id |
| 8 | defectCodeName | String |  |
| 9 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 10 | wipUnitName | String |  |
| 11 | lotId | String | u_mes_exe_lot._id |
| 12 | lotName | String |  |
| 13 | itemId | String | u_mes_prd_item._id |
| 14 | itemName | String |  |
| 15 | quantity | Int32 |  |
| 16 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 17 | unitOfMeasureName | String |  |
| 18 | weightKg | Decimal128 |  |
| 19 | originOperationId | String | u_mes_prd_operation._id |
| 20 | originOperationName | String |  |
| 21 | detectedAtOperationId | String | u_mes_prd_operation._id |
| 22 | detectedAtOperationName | String |  |
| 23 | workCenterId | String | u_mes_mdm_workCenter._id |
| 24 | workCenterName | String |  |
| 25 | shiftId | String | u_mes_mdm_shift._id |
| 26 | shiftName | String |  |
| 27 | scrapType | String |  |
| 28 | scrapCostInr | Decimal128 |  |
| 29 | declaredById | String | u_mes_mdm_user._id |
| 30 | declaredBy | String |  |
| 31 | declaredAt | Date |  |
| 32 | approvedById | String | u_mes_mdm_user._id |
| 33 | approvedBy | String |  |
| 34 | approvedAt | Date |  |
| 35 | scrapLocationId | String | u_mes_mat_storageLocation._id |
| 36 | scrapLocationName | String |  |
| 37 | disposalMethod | String |  |
| 38 | erpPosted | Boolean |  |
| 39 | status | String |  |
| 40 | schemaVersion | Int32 |  |
| 41 | createdAt | Date |  |
| 42 | createdById | String | u_mes_mdm_user._id |
| 43 | createdBy | String |  |
| 44 | updatedAt | Date |  |
| 45 | updatedById | String | u_mes_mdm_user._id |
| 46 | updatedBy | String |  |

## u_mes_qlt_qualityHold

Kind: entity | Data class: transaction | Parent: - | _id pattern: HLD-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | holdType | String |  |
| 6 | reasonText | String |  |
| 7 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 8 | reasonCodeName | String |  |
| 9 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 10 | nonconformanceName | String |  |
| 11 | itemId | String | u_mes_prd_item._id |
| 12 | itemName | String |  |
| 13 | totalQuantity | Int32 |  |
| 14 | quarantineLocationId | String | u_mes_mat_storageLocation._id |
| 15 | quarantineLocationName | String |  |
| 16 | placedById | String | u_mes_mdm_user._id |
| 17 | placedBy | String |  |
| 18 | placedAt | Date |  |
| 19 | expectedReleaseAt | Date |  |
| 20 | releasedById | String | u_mes_mdm_user._id |
| 21 | releasedBy | String |  |
| 22 | releasedAt | Date |  |
| 23 | releaseDecision | String |  |
| 24 | releaseComment | String |  |
| 25 | customerNotified | Boolean |  |
| 26 | status | String |  |
| 27 | schemaVersion | Int32 |  |
| 28 | createdAt | Date |  |
| 29 | createdById | String | u_mes_mdm_user._id |
| 30 | createdBy | String |  |
| 31 | updatedAt | Date |  |
| 32 | updatedById | String | u_mes_mdm_user._id |
| 33 | updatedBy | String |  |

## u_mes_qlt_qualityHoldHeldObject

Kind: child | Data class: transaction | Parent: u_mes_qlt_qualityHold | _id pattern: <qualityHoldId>-HO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | qualityHoldId | String | u_mes_qlt_qualityHold._id |
| 6 | qualityHoldName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | relatedCollectionName | String |  |
| 9 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String |  |
| 11 | quantity | Int32 |  |
| 12 | releasedAt | Date |  |
| 13 | releaseDecision | String |  |
| 14 | schemaVersion | Int32 |  |
| 15 | createdAt | Date |  |
| 16 | createdById | String | u_mes_mdm_user._id |
| 17 | createdBy | String |  |
| 18 | updatedAt | Date |  |
| 19 | updatedById | String | u_mes_mdm_user._id |
| 20 | updatedBy | String |  |

## u_mes_qlt_deviationPermit

Kind: entity | Data class: transaction | Parent: - | _id pattern: DEV-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | itemId | String | u_mes_prd_item._id |
| 7 | itemName | String |  |
| 8 | characteristicId | String | u_mes_qlt_characteristic._id |
| 9 | characteristicName | String |  |
| 10 | deviationType | String |  |
| 11 | description | String |  |
| 12 | requestedValue | Decimal128 |  |
| 13 | specifiedValue | Decimal128 |  |
| 14 | customerId | String | u_mes_mdm_customer._id |
| 15 | customerName | String |  |
| 16 | customerApprovalRef | String |  |
| 17 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 18 | nonconformanceName | String |  |
| 19 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 20 | engineeringChangeName | String |  |
| 21 | limitType | String |  |
| 22 | quantityLimit | Int32 |  |
| 23 | quantityUsed | Int32 |  |
| 24 | validFrom | Date |  |
| 25 | validTo | Date |  |
| 26 | markingRequirement | String |  |
| 27 | requestedById | String | u_mes_mdm_user._id |
| 28 | requestedBy | String |  |
| 29 | requestedAt | Date |  |
| 30 | closedAt | Date |  |
| 31 | status | String |  |
| 32 | schemaVersion | Int32 |  |
| 33 | createdAt | Date |  |
| 34 | createdById | String | u_mes_mdm_user._id |
| 35 | createdBy | String |  |
| 36 | updatedAt | Date |  |
| 37 | updatedById | String | u_mes_mdm_user._id |
| 38 | updatedBy | String |  |

## u_mes_qlt_deviationPermitApproval

Kind: child | Data class: transaction | Parent: u_mes_qlt_deviationPermit | _id pattern: <deviationPermitId>-A<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | deviationPermitId | String | u_mes_qlt_deviationPermit._id |
| 6 | deviationPermitName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | businessFunction | String |  |
| 9 | userId | String | u_mes_mdm_user._id |
| 10 | userName | String |  |
| 11 | decision | String |  |
| 12 | decidedAt | Date |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_qlt_capa

Kind: entity | Data class: transaction | Parent: - | _id pattern: CAPA-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | capaType | String |  |
| 7 | source | String |  |
| 8 | customerComplaintId | String | u_mes_qlt_customerComplaint._id |
| 9 | customerComplaintName | String |  |
| 10 | auditId | String | u_mes_qlt_audit._id |
| 11 | auditName | String |  |
| 12 | itemId | String | u_mes_prd_item._id |
| 13 | itemName | String |  |
| 14 | customerId | String | u_mes_mdm_customer._id |
| 15 | customerName | String |  |
| 16 | openedAt | Date |  |
| 17 | openedById | String | u_mes_mdm_user._id |
| 18 | openedBy | String |  |
| 19 | d2ProblemDescription | String |  |
| 20 | d4RootCauseOccurrence | String |  |
| 21 | d4RootCauseEscape | String |  |
| 22 | d4RootCauseMethod | String |  |
| 23 | d7PreventionPfmeaId | String | u_mes_qlt_pfmea._id |
| 24 | d7PreventionPfmeaName | String |  |
| 25 | d7PreventionControlPlanId | String | u_mes_qlt_controlPlan._id |
| 26 | d7PreventionControlPlanName | String |  |
| 27 | d7PreventionLessonsLearned | String |  |
| 28 | d7PreventionHorizontalDeployment | String |  |
| 29 | d8ClosureClosedById | String | u_mes_mdm_user._id |
| 30 | d8ClosureClosedBy | String |  |
| 31 | d8ClosureClosedAt | Date |  |
| 32 | d8ClosureCustomerAccepted | Boolean |  |
| 33 | dueAt | Date |  |
| 34 | currentDiscipline | String |  |
| 35 | status | String |  |
| 36 | schemaVersion | Int32 |  |
| 37 | createdAt | Date |  |
| 38 | createdById | String | u_mes_mdm_user._id |
| 39 | createdBy | String |  |
| 40 | updatedAt | Date |  |
| 41 | updatedById | String | u_mes_mdm_user._id |
| 42 | updatedBy | String |  |

## u_mes_qlt_capaNonconformance

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-N<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 9 | nonconformanceName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_capaTeamMember

Kind: child | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-TM<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | userId | String | u_mes_mdm_user._id |
| 9 | userName | String |  |
| 10 | roleInTeam | String |  |
| 11 | schemaVersion | Int32 |  |
| 12 | createdAt | Date |  |
| 13 | createdById | String | u_mes_mdm_user._id |
| 14 | createdBy | String |  |
| 15 | updatedAt | Date |  |
| 16 | updatedById | String | u_mes_mdm_user._id |
| 17 | updatedBy | String |  |

## u_mes_qlt_capaContainmentAction

Kind: child | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-CA<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mdm_user._id |
| 10 | ownerUserName | String |  |
| 11 | completedAt | Date |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_qlt_capaCorrectiveAction

Kind: child | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-CA2<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mdm_user._id |
| 10 | ownerUserName | String |  |
| 11 | dueAt | Date |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_qlt_capaImplementationAction

Kind: child | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-IA<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | description | String |  |
| 9 | completedAt | Date |  |
| 10 | verifiedById | String | u_mes_mdm_user._id |
| 11 | verifiedBy | String |  |
| 12 | effective | Boolean |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_qlt_capaControlledDocument

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_capa | _id pattern: <capaId>-CD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | capaId | String | u_mes_qlt_capa._id |
| 6 | capaName | String |  |
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

## u_mes_qlt_pfmea

Kind: entity | Data class: master | Parent: - | _id pattern: FMEA-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | itemId | String | u_mes_prd_item._id |
| 7 | itemName | String |  |
| 8 | itemRevision | String |  |
| 9 | version | Int32 |  |
| 10 | methodology | String |  |
| 11 | controlPlanId | String | u_mes_qlt_controlPlan._id |
| 12 | controlPlanName | String |  |
| 13 | originalDate | Date |  |
| 14 | revisionDate | Date |  |
| 15 | approvedById | String | u_mes_mdm_user._id |
| 16 | approvedBy | String |  |
| 17 | approvedAt | Date |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |

## u_mes_qlt_pfmeaCoreTeamUser

Kind: relationship | Data class: master | Parent: u_mes_qlt_pfmea | _id pattern: <pfmeaId>-CTU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | pfmeaId | String | u_mes_qlt_pfmea._id |
| 6 | pfmeaName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | coreTeamUserId | String | u_mes_mdm_user._id |
| 9 | coreTeamUserName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_qlt_pfmeaLine

Kind: child | Data class: master | Parent: u_mes_qlt_pfmea | _id pattern: <pfmeaId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | pfmeaId | String | u_mes_qlt_pfmea._id |
| 6 | pfmeaName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | processFunction | String |  |
| 11 | failureMode | String |  |
| 12 | failureEffect | String |  |
| 13 | severity | Int32 |  |
| 14 | characteristicId | String | u_mes_qlt_characteristic._id |
| 15 | characteristicName | String |  |
| 16 | classification | String |  |
| 17 | failureCause | String |  |
| 18 | preventionControl | String |  |
| 19 | occurrence | Int32 |  |
| 20 | detectionControl | String |  |
| 21 | detection | Int32 |  |
| 22 | rpn | Int32 |  |
| 23 | actionPriority | String |  |
| 24 | recommendedAction | String |  |
| 25 | ownerUserId | String | u_mes_mdm_user._id |
| 26 | ownerUserName | String |  |
| 27 | targetDate | Date |  |
| 28 | actionTaken | String |  |
| 29 | revisedSeverity | Int32 |  |
| 30 | revisedOccurrence | Int32 |  |
| 31 | revisedDetection | Int32 |  |
| 32 | schemaVersion | Int32 |  |

## u_mes_qlt_ppapSubmission

Kind: entity | Data class: transaction | Parent: - | _id pattern: PPAP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prd_item._id |
| 6 | itemName | String |  |
| 7 | itemRevision | String |  |
| 8 | customerId | String | u_mes_mdm_customer._id |
| 9 | customerName | String |  |
| 10 | engineeringChangeId | String | u_mes_prd_engineeringChange._id |
| 11 | engineeringChangeName | String |  |
| 12 | submissionLevel | Int32 |  |
| 13 | submissionReason | String |  |
| 14 | controlPlanId | String | u_mes_qlt_controlPlan._id |
| 15 | controlPlanName | String |  |
| 16 | pfmeaId | String | u_mes_qlt_pfmea._id |
| 17 | pfmeaName | String |  |
| 18 | sampleQuantity | Int32 |  |
| 19 | significantProductionRunQuantity | Int32 |  |
| 20 | pswSignedById | String | u_mes_mdm_user._id |
| 21 | pswSignedBy | String |  |
| 22 | pswSignedAt | Date |  |
| 23 | submittedAt | Date |  |
| 24 | customerDecision | String |  |
| 25 | customerDecisionAt | Date |  |
| 26 | customerRemarks | String |  |
| 27 | interimApprovalValidTo | Date |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |
| 30 | createdAt | Date |  |
| 31 | createdById | String | u_mes_mdm_user._id |
| 32 | createdBy | String |  |
| 33 | updatedAt | Date |  |
| 34 | updatedById | String | u_mes_mdm_user._id |
| 35 | updatedBy | String |  |

## u_mes_qlt_ppapSubmissionElement

Kind: child | Data class: transaction | Parent: u_mes_qlt_ppapSubmission | _id pattern: <ppapSubmissionId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | ppapSubmissionId | String | u_mes_qlt_ppapSubmission._id |
| 6 | ppapSubmissionName | String |  |
| 7 | elementNo | Int32 |  |
| 8 | name | String |  |
| 9 | required | Boolean |  |
| 10 | status | String |  |
| 11 | controlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 12 | controlledDocumentName | String |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_qlt_ppapSubmissionMsaStudy

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_ppapSubmission | _id pattern: <ppapSubmissionId>-MS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | ppapSubmissionId | String | u_mes_qlt_ppapSubmission._id |
| 6 | ppapSubmissionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | msaStudyId | String | u_mes_qlt_msaStudy._id |
| 9 | msaStudyName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_gauge

Kind: entity | Data class: master | Parent: - | _id pattern: GAU-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | gaugeType | String |  |
| 7 | manufacturer | String |  |
| 8 | model | String |  |
| 9 | serialNo | String |  |
| 10 | rangeMin | Decimal128 |  |
| 11 | rangeMax | Decimal128 |  |
| 12 | rangeUnitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 13 | rangeUnitOfMeasureName | String |  |
| 14 | resolution | Decimal128 |  |
| 15 | accuracy | Decimal128 |  |
| 16 | storageLocationId | String | u_mes_mat_storageLocation._id |
| 17 | storageLocationName | String |  |
| 18 | workCenterId | String | u_mes_mdm_workCenter._id |
| 19 | workCenterName | String |  |
| 20 | ownerUserId | String | u_mes_mdm_user._id |
| 21 | ownerUserName | String |  |
| 22 | calibrationIntervalDays | Int32 |  |
| 23 | calibrationSource | String |  |
| 24 | calibrationSupplierId | String | u_mes_mdm_supplier._id |
| 25 | calibrationSupplierName | String |  |
| 26 | lastCalibratedAt | Date |  |
| 27 | nextCalibrationDueAt | Date |  |
| 28 | lastGaugeCalibrationId | String | u_mes_qlt_gaugeCalibration._id |
| 29 | lastGaugeCalibrationName | String |  |
| 30 | usageCount | Int32 |  |
| 31 | purchasedAt | Date |  |
| 32 | isMasterGauge | Boolean |  |
| 33 | blockedForUse | Boolean |  |
| 34 | status | String |  |
| 35 | schemaVersion | Int32 |  |

## u_mes_qlt_gaugeCalibration

Kind: entity | Data class: transaction | Parent: - | _id pattern: GCAL-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | gaugeId | String | u_mes_qlt_gauge._id |
| 6 | gaugeName | String |  |
| 7 | calibrationType | String |  |
| 8 | calibratedAt | Date |  |
| 9 | calibratedById | String | u_mes_mdm_user._id |
| 10 | calibratedBy | String |  |
| 11 | calibrationSupplierId | String | u_mes_mdm_supplier._id |
| 12 | calibrationSupplierName | String |  |
| 13 | masterStandardRef | String |  |
| 14 | traceability | String |  |
| 15 | temperatureC | Decimal128 |  |
| 16 | humidityPct | Decimal128 |  |
| 17 | asFoundResult | String |  |
| 18 | asLeftResult | String |  |
| 19 | overallResult | String |  |
| 20 | uncertainty | Decimal128 |  |
| 21 | adjustmentMade | Boolean |  |
| 22 | certificateNo | String |  |
| 23 | certificateControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 24 | certificateControlledDocumentName | String |  |
| 25 | nextDueAt | Date |  |
| 26 | impactAssessmentRequired | Boolean |  |
| 27 | remarks | String |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |
| 30 | createdAt | Date |  |
| 31 | createdById | String | u_mes_mdm_user._id |
| 32 | createdBy | String |  |
| 33 | updatedAt | Date |  |
| 34 | updatedById | String | u_mes_mdm_user._id |
| 35 | updatedBy | String |  |

## u_mes_qlt_gaugeCalibrationReading

Kind: child | Data class: transaction | Parent: u_mes_qlt_gaugeCalibration | _id pattern: <gaugeCalibrationId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | gaugeCalibrationId | String | u_mes_qlt_gaugeCalibration._id |
| 6 | gaugeCalibrationName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | nominal | Decimal128 |  |
| 9 | asFound | Decimal128 |  |
| 10 | asLeft | Decimal128 |  |
| 11 | tolerance | Decimal128 |  |
| 12 | withinTolerance | Boolean |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_qlt_msaStudy

Kind: entity | Data class: transaction | Parent: - | _id pattern: MSA-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | gaugeId | String | u_mes_qlt_gauge._id |
| 6 | gaugeName | String |  |
| 7 | characteristicId | String | u_mes_qlt_characteristic._id |
| 8 | characteristicName | String |  |
| 9 | itemId | String | u_mes_prd_item._id |
| 10 | itemName | String |  |
| 11 | studyType | String |  |
| 12 | studyMethod | String |  |
| 13 | studyDate | Date |  |
| 14 | partsCount | Int32 |  |
| 15 | trialsCount | Int32 |  |
| 16 | resultsEquipmentVariation | Decimal128 |  |
| 17 | resultsAppraiserVariation | Decimal128 |  |
| 18 | resultsGrr | Decimal128 |  |
| 19 | resultsPartVariation | Decimal128 |  |
| 20 | resultsTotalVariation | Decimal128 |  |
| 21 | resultsGrrPctTolerance | Decimal128 |  |
| 22 | resultsGrrPctStudyVariation | Decimal128 |  |
| 23 | resultsNdc | Decimal128 |  |
| 24 | resultsBiasValue | Decimal128 |  |
| 25 | resultsKappa | Decimal128 |  |
| 26 | conclusion | String |  |
| 27 | actionRequired | Boolean |  |
| 28 | conductedById | String | u_mes_mdm_user._id |
| 29 | conductedBy | String |  |
| 30 | approvedById | String | u_mes_mdm_user._id |
| 31 | approvedBy | String |  |
| 32 | approvedAt | Date |  |
| 33 | nextStudyDueAt | Date |  |
| 34 | status | String |  |
| 35 | schemaVersion | Int32 |  |
| 36 | createdAt | Date |  |
| 37 | createdById | String | u_mes_mdm_user._id |
| 38 | createdBy | String |  |
| 39 | updatedAt | Date |  |
| 40 | updatedById | String | u_mes_mdm_user._id |
| 41 | updatedBy | String |  |

## u_mes_qlt_msaStudyAppraiserUser

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_msaStudy | _id pattern: <msaStudyId>-AU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | msaStudyId | String | u_mes_qlt_msaStudy._id |
| 6 | msaStudyName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | appraiserUserId | String | u_mes_mdm_user._id |
| 9 | appraiserUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_msaStudyTrial

Kind: child | Data class: transaction | Parent: u_mes_qlt_msaStudy | _id pattern: <msaStudyId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | msaStudyId | String | u_mes_qlt_msaStudy._id |
| 6 | msaStudyName | String |  |
| 7 | appraiserUserId | String | u_mes_mdm_user._id |
| 8 | appraiserUserName | String |  |
| 9 | partNo | Int32 |  |
| 10 | trialNo | Int32 |  |
| 11 | measuredValue | Decimal128 |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_qlt_audit

Kind: entity | Data class: transaction | Parent: - | _id pattern: AUD-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | auditType | String |  |
| 7 | standard | String |  |
| 8 | scopeText | String |  |
| 9 | areaId | String | u_mes_mdm_area._id |
| 10 | areaName | String |  |
| 11 | lineId | String | u_mes_mdm_line._id |
| 12 | lineName | String |  |
| 13 | customerId | String | u_mes_mdm_customer._id |
| 14 | customerName | String |  |
| 15 | layer | Int32 |  |
| 16 | leadAuditorUserId | String | u_mes_mdm_user._id |
| 17 | leadAuditorUserName | String |  |
| 18 | auditeeUserId | String | u_mes_mdm_user._id |
| 19 | auditeeUserName | String |  |
| 20 | plannedDate | Date |  |
| 21 | startedAt | Date |  |
| 22 | completedAt | Date |  |
| 23 | checkSheetId | String | u_mes_qlt_checkSheet._id |
| 24 | checkSheetName | String |  |
| 25 | questionsCount | Int32 |  |
| 26 | conformingCount | Int32 |  |
| 27 | scorePct | Decimal128 |  |
| 28 | overallRating | String |  |
| 29 | reportControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 30 | reportControlledDocumentName | String |  |
| 31 | nextAuditDueAt | Date |  |
| 32 | status | String |  |
| 33 | schemaVersion | Int32 |  |
| 34 | createdAt | Date |  |
| 35 | createdById | String | u_mes_mdm_user._id |
| 36 | createdBy | String |  |
| 37 | updatedAt | Date |  |
| 38 | updatedById | String | u_mes_mdm_user._id |
| 39 | updatedBy | String |  |

## u_mes_qlt_auditAuditorUser

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_audit | _id pattern: <auditId>-AU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | auditId | String | u_mes_qlt_audit._id |
| 6 | auditName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | auditorUserId | String | u_mes_mdm_user._id |
| 9 | auditorUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_auditFinding

Kind: child | Data class: transaction | Parent: u_mes_qlt_audit | _id pattern: <auditId>-F<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | auditId | String | u_mes_qlt_audit._id |
| 6 | auditName | String |  |
| 7 | findingNo | Int32 |  |
| 8 | clause | String |  |
| 9 | description | String |  |
| 10 | grade | String |  |
| 11 | ownerUserId | String | u_mes_mdm_user._id |
| 12 | ownerUserName | String |  |
| 13 | dueAt | Date |  |
| 14 | closedAt | Date |  |
| 15 | capaId | String | u_mes_qlt_capa._id |
| 16 | capaName | String |  |
| 17 | schemaVersion | Int32 |  |
| 18 | createdAt | Date |  |
| 19 | createdById | String | u_mes_mdm_user._id |
| 20 | createdBy | String |  |
| 21 | updatedAt | Date |  |
| 22 | updatedById | String | u_mes_mdm_user._id |
| 23 | updatedBy | String |  |

## u_mes_qlt_customerComplaint

Kind: entity | Data class: transaction | Parent: - | _id pattern: CMP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerId | String | u_mes_mdm_customer._id |
| 6 | customerName | String |  |
| 7 | customerRefNo | String |  |
| 8 | complaintType | String |  |
| 9 | itemId | String | u_mes_prd_item._id |
| 10 | itemName | String |  |
| 11 | description | String |  |
| 12 | defectDescription | String |  |
| 13 | reportedAt | Date |  |
| 14 | receivedById | String | u_mes_mdm_user._id |
| 15 | receivedBy | String |  |
| 16 | occurredAt | Date |  |
| 17 | customerLocation | String |  |
| 18 | quantityComplained | Int32 |  |
| 19 | quantityConfirmed | Int32 |  |
| 20 | vehicleModel | String |  |
| 21 | mileageKm | Decimal128 |  |
| 22 | severity | Int32 |  |
| 23 | isSafetyRelated | Boolean |  |
| 24 | containmentDueAt | Date |  |
| 25 | containmentSentAt | Date |  |
| 26 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 27 | nonconformanceName | String |  |
| 28 | capaId | String | u_mes_qlt_capa._id |
| 29 | capaName | String |  |
| 30 | debitNoteInr | Decimal128 |  |
| 31 | ppmImpact | Int32 |  |
| 32 | sortingCostInr | Decimal128 |  |
| 33 | customerClosedAt | Date |  |
| 34 | status | String |  |
| 35 | schemaVersion | Int32 |  |
| 36 | createdAt | Date |  |
| 37 | createdById | String | u_mes_mdm_user._id |
| 38 | createdBy | String |  |
| 39 | updatedAt | Date |  |
| 40 | updatedById | String | u_mes_mdm_user._id |
| 41 | updatedBy | String |  |

## u_mes_qlt_customerComplaintSerialNumber

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_customerComplaint | _id pattern: <customerComplaintId>-SN<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerComplaintId | String | u_mes_qlt_customerComplaint._id |
| 6 | customerComplaintName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | serialNumberId | String | u_mes_trc_serialNumber._id |
| 9 | serialNumberName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_customerComplaintShipment

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_customerComplaint | _id pattern: <customerComplaintId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerComplaintId | String | u_mes_qlt_customerComplaint._id |
| 6 | customerComplaintName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | shipmentId | String | u_mes_mat_shipment._id |
| 9 | shipmentName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_customerComplaintSuspectLot

Kind: relationship | Data class: transaction | Parent: u_mes_qlt_customerComplaint | _id pattern: <customerComplaintId>-SL<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerComplaintId | String | u_mes_qlt_customerComplaint._id |
| 6 | customerComplaintName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | suspectLotId | String | u_mes_exe_lot._id |
| 9 | suspectLotName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_qlt_customerComplaintCommunication

Kind: child | Data class: transaction | Parent: u_mes_qlt_customerComplaint | _id pattern: <customerComplaintId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerComplaintId | String | u_mes_qlt_customerComplaint._id |
| 6 | customerComplaintName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | communicatedAt | Date |  |
| 9 | direction | String |  |
| 10 | communicationSummary | String |  |
| 11 | authorUserId | String | u_mes_mdm_user._id |
| 12 | authorUserName | String |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |
