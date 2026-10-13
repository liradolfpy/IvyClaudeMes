# Field list - Batch Manufacturing Record (bmr)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/11_batch_manufacturing_record/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_bmr_batchRecordReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | reviewScope | String | - |  |
| 12 | operationsCount | Int32 | - |  |
| 13 | exceptionCount | Int32 | - |  |
| 14 | openExceptionCount | Int32 | - |  |
| 15 | genealogyComplete | Boolean | - |  |
| 16 | yieldReconciliationId | String | - | u_mes_bmr_yieldReconciliation._id |
| 17 | yieldReconciliationName | String | - |  |
| 18 | auditTrailReviewId | String | - | u_mes_syst_auditTrailReview._id |
| 19 | auditTrailReviewName | String | - |  |
| 20 | productionReviewedById | String | - | u_mes_mast_user._id |
| 21 | productionReviewedBy | String | - |  |
| 22 | productionReviewedAt | Date | Datetime |  |
| 23 | qaReviewedById | String | - | u_mes_mast_user._id |
| 24 | qaReviewedBy | String | - |  |
| 25 | qaReviewedAt | Date | Datetime |  |
| 26 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 27 | electronicSignatureName | String | - |  |
| 28 | returnReasonText | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_bmr_batchRecordReviewException

Kind: child | Data class: transaction | Parent: u_mes_bmr_batchRecordReview | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 6 | batchRecordReviewName | String | - |  |
| 7 | lineNo | Int32 | - |  |
| 8 | exceptionType | String | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | description | String | - |  |
| 13 | assessment | String | - |  |
| 14 | assessedById | String | - | u_mes_mast_user._id |
| 15 | assessedBy | String | - |  |
| 16 | assessedAt | Date | Datetime |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_bmr_batchRelease

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | lotId | String | - | u_mes_plan_lot._id |
| 6 | lotName | String | - |  |
| 7 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 8 | productionOrderName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 12 | batchRecordReviewName | String | - |  |
| 13 | releaseQuantity | Int32 | - |  |
| 14 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - |  |
| 16 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 17 | deviationPermitName | String | - |  |
| 18 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 19 | qualityHoldName | String | - |  |
| 20 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 21 | certificateControlledDocumentName | String | - |  |
| 22 | releasedById | String | - | u_mes_mast_user._id |
| 23 | releasedBy | String | - |  |
| 24 | releasedAt | Date | Datetime |  |
| 25 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 26 | electronicSignatureName | String | - |  |
| 27 | decisionText | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_bmr_yieldReconciliation

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - |  |
| 7 | reconciliationType | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 11 | unitOfMeasureName | String | - |  |
| 12 | theoreticalQuantity | Decimal128 | - |  |
| 13 | issuedQuantity | Decimal128 | - |  |
| 14 | outputQuantity | Decimal128 | - |  |
| 15 | rejectedQuantity | Decimal128 | - |  |
| 16 | destroyedQuantity | Decimal128 | - |  |
| 17 | returnedQuantity | Decimal128 | - |  |
| 18 | unaccountedQuantity | Decimal128 | - |  |
| 19 | yieldPct | Decimal128 | - |  |
| 20 | lowerLimitPct | Decimal128 | - |  |
| 21 | upperLimitPct | Decimal128 | - |  |
| 22 | withinLimits | Boolean | - |  |
| 23 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 24 | nonconformanceName | String | - |  |
| 25 | calculatedAt | Date | Datetime |  |
| 26 | approvedById | String | - | u_mes_mast_user._id |
| 27 | approvedBy | String | - |  |
| 28 | approvedAt | Date | Datetime |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_bmr_batchManufacturingRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | masterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 12 | masterManufacturingRecordName | String | - |  |
| 13 | masterRecordVersion | Int32 | - |  |
| 14 | plannedQuantity | Int32 | - |  |
| 15 | lineClearanceId | String | - | u_mes_plan_lineClearance._id |
| 16 | lineClearanceName | String | - |  |
| 17 | yieldReconciliationId | String | - | u_mes_bmr_yieldReconciliation._id |
| 18 | yieldReconciliationName | String | - |  |
| 19 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 20 | batchRecordReviewName | String | - |  |
| 21 | batchReleaseId | String | - | u_mes_bmr_batchRelease._id |
| 22 | batchReleaseName | String | - |  |
| 23 | openedAt | Date | Datetime |  |
| 24 | compiledAt | Date | Datetime |  |
| 25 | exportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 26 | exportControlledDocumentName | String | - |  |
| 27 | checksumSha256 | String | - |  |
| 28 | pageCount | Int32 | - |  |
| 29 | exportedById | String | - | u_mes_mast_user._id |
| 30 | exportedBy | String | - |  |
| 31 | exportedAt | Date | Datetime |  |
| 32 | archivedAt | Date | Datetime |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |
