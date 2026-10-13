# Field list - Batch Manufacturing Record (bmr)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/11_batch_manufacturing_record/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_bmr_batchRecordReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | reviewScope | String | - |  |
| 13 | operationsCount | Int32 | - |  |
| 14 | exceptionCount | Int32 | - |  |
| 15 | openExceptionCount | Int32 | - |  |
| 16 | genealogyComplete | Boolean | - |  |
| 17 | yieldReconciliationId | String | - | u_mes_bmr_yieldReconciliation._id |
| 18 | yieldReconciliationName | String | - |  |
| 19 | auditTrailReviewId | String | - | u_mes_syst_auditTrailReview._id |
| 20 | auditTrailReviewName | String | - |  |
| 21 | productionReviewedById | String | - | u_mes_mast_user._id |
| 22 | productionReviewedBy | String | - |  |
| 23 | productionReviewedAt | Date | Datetime |  |
| 24 | qaReviewedById | String | - | u_mes_mast_user._id |
| 25 | qaReviewedBy | String | - |  |
| 26 | qaReviewedAt | Date | Datetime |  |
| 27 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 28 | electronicSignatureName | String | - |  |
| 29 | returnReasonText | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_bmr_batchRecordReviewException

Kind: child | Data class: transaction | Parent: u_mes_bmr_batchRecordReview | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 7 | batchRecordReviewName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | exceptionType | String | - |  |
| 10 | relatedCollectionName | String | - |  |
| 11 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 12 | relatedEntityName | String | - |  |
| 13 | description | String | - |  |
| 14 | assessment | String | - |  |
| 15 | assessedById | String | - | u_mes_mast_user._id |
| 16 | assessedBy | String | - |  |
| 17 | assessedAt | Date | Datetime |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_bmr_batchRelease

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lotId | String | - | u_mes_plan_lot._id |
| 7 | lotName | String | - |  |
| 8 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 13 | batchRecordReviewName | String | - |  |
| 14 | releaseQuantity | Int32 | - |  |
| 15 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - |  |
| 17 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 18 | deviationPermitName | String | - |  |
| 19 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 20 | qualityHoldName | String | - |  |
| 21 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 22 | certificateControlledDocumentName | String | - |  |
| 23 | releasedById | String | - | u_mes_mast_user._id |
| 24 | releasedBy | String | - |  |
| 25 | releasedAt | Date | Datetime |  |
| 26 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 27 | electronicSignatureName | String | - |  |
| 28 | decisionText | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_bmr_yieldReconciliation

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | reconciliationType | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 12 | unitOfMeasureName | String | - |  |
| 13 | theoreticalQuantity | Decimal128 | - |  |
| 14 | issuedQuantity | Decimal128 | - |  |
| 15 | outputQuantity | Decimal128 | - |  |
| 16 | rejectedQuantity | Decimal128 | - |  |
| 17 | destroyedQuantity | Decimal128 | - |  |
| 18 | returnedQuantity | Decimal128 | - |  |
| 19 | unaccountedQuantity | Decimal128 | - |  |
| 20 | yieldPct | Decimal128 | - |  |
| 21 | lowerLimitPct | Decimal128 | - |  |
| 22 | upperLimitPct | Decimal128 | - |  |
| 23 | withinLimits | Boolean | - |  |
| 24 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 25 | nonconformanceName | String | - |  |
| 26 | calculatedAt | Date | Datetime |  |
| 27 | approvedById | String | - | u_mes_mast_user._id |
| 28 | approvedBy | String | - |  |
| 29 | approvedAt | Date | Datetime |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_bmr_batchManufacturingRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | masterManufacturingRecordId | String | - | u_mes_mmr_masterManufacturingRecord._id |
| 13 | masterManufacturingRecordName | String | - |  |
| 14 | masterRecordVersion | Int32 | - |  |
| 15 | plannedQuantity | Int32 | - |  |
| 16 | lineClearanceId | String | - | u_mes_plan_lineClearance._id |
| 17 | lineClearanceName | String | - |  |
| 18 | yieldReconciliationId | String | - | u_mes_bmr_yieldReconciliation._id |
| 19 | yieldReconciliationName | String | - |  |
| 20 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 21 | batchRecordReviewName | String | - |  |
| 22 | batchReleaseId | String | - | u_mes_bmr_batchRelease._id |
| 23 | batchReleaseName | String | - |  |
| 24 | openedAt | Date | Datetime |  |
| 25 | compiledAt | Date | Datetime |  |
| 26 | exportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 27 | exportControlledDocumentName | String | - |  |
| 28 | checksumSha256 | String | - |  |
| 29 | pageCount | Int32 | - |  |
| 30 | exportedById | String | - | u_mes_mast_user._id |
| 31 | exportedBy | String | - |  |
| 32 | exportedAt | Date | Datetime |  |
| 33 | archivedAt | Date | Datetime |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |
