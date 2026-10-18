## u_mes_bmr_batchManufacturingRecord - Batch Manufacturing Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_bmr_batchManufacturingRecord.json | _id: mes_bmr_batchManufacturingRecordStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 4040px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | lotName | Lot | String | 13 | 120px | left |
| 5 | masterManufacturingRecordName | Master Manufacturing Record | String | 84 | 300px | left |
| 6 | masterRecordVersion | Master Record Version | Int32 | 1 | 190px | right |
| 7 | plannedQuantity | Planned Quantity | Int32 | 6 | 160px | right |
| 8 | lineClearanceName | Line Clearance | String | 16 | 140px | left |
| 9 | yieldReconciliationName | Yield Reconciliation | String | 17 | 180px | left |
| 10 | batchRecordReviewName | Batch Record Review | String | 14 | 180px | left |
| 11 | batchReleaseName | Batch Release | String | 17 | 140px | left |
| 12 | openedAt | Opened At | Date/Datetime | 19 | 160px | center |
| 13 | compiledAt | Compiled At | Date/Datetime | 19 | 160px | center |
| 14 | exportControlledDocumentName | Export Controlled Document | String | 0 | 230px | left |
| 15 | checksumSha256 | Checksum Sha256 | String | 64 | 300px | left |
| 16 | pageCount | Page Count | Int32 | 2 | 110px | right |
| 17 | exportedBy | Exported By | String | 11 | 120px | left |
| 18 | exportedAt | Exported At | Date/Datetime | 19 | 160px | center |
| 19 | archivedAt | Archived At | Date/Datetime | 19 | 160px | center |
| 20 | status | Status | String | 12 | 110px | left |
| 21 | createdBy | Created By | String | 11 | 110px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 11 | 110px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); masterManufacturingRecordId (reference key, shown through masterManufacturingRecordName); lineClearanceId (reference key, shown through lineClearanceName); yieldReconciliationId (reference key, shown through yieldReconciliationName); batchRecordReviewId (reference key, shown through batchRecordReviewName); batchReleaseId (reference key, shown through batchReleaseName); exportControlledDocumentId (reference key, shown through exportControlledDocumentName); exportedById (reference key, shown through exportedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): exportControlledDocumentName

## u_mes_bmr_batchRecordReview - Batch Record Reviews (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_bmr_batchRecordReview.json | _id: mes_bmr_batchRecordReviewStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 3780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | lotName | Lot | String | 13 | 120px | left |
| 5 | reviewScope | Review Scope | String | 19 | 160px | left |
| 6 | operationsCount | Operations Count | Int32 | 3 | 160px | right |
| 7 | exceptionCount | Exception Count | Int32 | 1 | 150px | right |
| 8 | openExceptionCount | Open Exception Count | Int32 | 1 | 180px | right |
| 9 | genealogyComplete | Genealogy Complete | Boolean | 3 | 170px | center |
| 10 | yieldReconciliationName | Yield Reconciliation | String | 17 | 180px | left |
| 11 | auditTrailReviewName | Audit Trail Review | String | 16 | 170px | left |
| 12 | productionReviewedBy | Production Reviewed By | String | 13 | 200px | left |
| 13 | productionReviewedAt | Production Reviewed At | Date/Datetime | 19 | 200px | center |
| 14 | qaReviewedBy | Qa Reviewed By | String | 11 | 140px | left |
| 15 | qaReviewedAt | Qa Reviewed At | Date/Datetime | 19 | 160px | center |
| 16 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 17 | returnReasonText | Return Reason Text | String | 101 | 300px | left |
| 18 | status | Status | String | 23 | 190px | left |
| 19 | createdBy | Created By | String | 11 | 110px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 11 | 110px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); yieldReconciliationId (reference key, shown through yieldReconciliationName); auditTrailReviewId (reference key, shown through auditTrailReviewName); productionReviewedById (reference key, shown through productionReviewedBy); qaReviewedById (reference key, shown through qaReviewedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): electronicSignatureName

## u_mes_bmr_batchRecordReviewException - Batch Record Review Exceptions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_bmr_batchRecordReviewException.json | _id: mes_bmr_batchRecordReviewExceptionStable | rel: CL20261018-23:51 | samples: 10 | columns: 14 | total width: 2490px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | batchRecordReviewName | Batch Record Review | String | 14 | 180px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | exceptionType | Exception Type | String | 27 | 210px | left |
| 5 | relatedCollectionName | Related Collection Name | String | 29 | 230px | left |
| 6 | relatedEntityName | Related Entity | String | 58 | 300px | left |
| 7 | description | Description | String | 122 | 300px | left |
| 8 | assessment | Assessment | String | 26 | 210px | left |
| 9 | assessedBy | Assessed By | String | 11 | 120px | left |
| 10 | assessedAt | Assessed At | Date/Datetime | 19 | 160px | center |
| 11 | createdBy | Created By | String | 11 | 110px | left |
| 12 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 13 | updatedBy | Updated By | String | 11 | 110px | left |
| 14 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); batchRecordReviewId (reference key, shown through batchRecordReviewName); relatedEntityId (reference key, shown through relatedEntityName); assessedById (reference key, shown through assessedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_bmr_batchRelease - Batch Releases (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_bmr_batchRelease.json | _id: mes_bmr_batchReleaseStable | rel: CL20261018-23:51 | samples: 10 | columns: 19 | total width: 3400px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | lotName | Lot | String | 13 | 120px | left |
| 3 | productionOrderName | Production Order | String | 10 | 160px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | batchRecordReviewName | Batch Record Review | String | 14 | 180px | left |
| 6 | releaseQuantity | Release Quantity | Int32 | 6 | 160px | right |
| 7 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 8 | deviationPermitName | Deviation Permit | String | 57 | 300px | left |
| 9 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 10 | certificateControlledDocumentName | Certificate Controlled Document | String | 0 | 260px | left |
| 11 | releasedBy | Released By | String | 0 | 120px | left |
| 12 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 13 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 14 | decisionText | Decision Text | String | 127 | 300px | left |
| 15 | status | Status | String | 22 | 180px | left |
| 16 | createdBy | Created By | String | 11 | 110px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 11 | 110px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lotId (reference key, shown through lotName); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); batchRecordReviewId (reference key, shown through batchRecordReviewName); unitOfMeasureId (reference key, shown through unitOfMeasureName); deviationPermitId (reference key, shown through deviationPermitName); qualityHoldId (reference key, shown through qualityHoldName); certificateControlledDocumentId (reference key, shown through certificateControlledDocumentName); releasedById (reference key, shown through releasedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): certificateControlledDocumentName, releasedBy, electronicSignatureName

## u_mes_bmr_yieldReconciliation - Yield and Reconciliation (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_bmr_yieldReconciliation.json | _id: mes_bmr_yieldReconciliationStable | rel: CL20261018-23:51 | samples: 10 | columns: 25 | total width: 4080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | reconciliationType | Reconciliation Type | String | 24 | 190px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 6 | theoreticalQuantity | Theoretical Quantity | Decimal128 | 6 | 180px | right |
| 7 | issuedQuantity | Issued Quantity | Decimal128 | 6 | 150px | right |
| 8 | outputQuantity | Output Quantity | Decimal128 | 6 | 150px | right |
| 9 | rejectedQuantity | Rejected Quantity | Decimal128 | 4 | 160px | right |
| 10 | destroyedQuantity | Destroyed Quantity | Decimal128 | 4 | 170px | right |
| 11 | returnedQuantity | Returned Quantity | Decimal128 | 4 | 160px | right |
| 12 | unaccountedQuantity | Unaccounted Quantity | Decimal128 | 3 | 180px | right |
| 13 | yieldPct | Yield (%) | Decimal128 | 5 | 110px | right |
| 14 | lowerLimitPct | Lower Limit (%) | Decimal128 | 5 | 150px | right |
| 15 | upperLimitPct | Upper Limit (%) | Decimal128 | 5 | 150px | right |
| 16 | withinLimits | Within Limits | Boolean | 3 | 140px | center |
| 17 | nonconformanceName | Nonconformance | String | 49 | 300px | left |
| 18 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 19 | approvedBy | Approved By | String | 11 | 120px | left |
| 20 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 21 | status | Status | String | 19 | 160px | left |
| 22 | createdBy | Created By | String | 11 | 110px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 11 | 110px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); unitOfMeasureId (reference key, shown through unitOfMeasureName); nonconformanceId (reference key, shown through nonconformanceName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
