## u_mes_syst_alertRule - Alert Rules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_alertRule.json | _id: mes_syst_alertRuleStable | rel: CL20261018-23:51 | samples: 10 | columns: 18 | total width: 3530px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | name | Name | String | 54 | 300px | left |
| 3 | metric | Metric | String | 21 | 170px | left |
| 4 | lineName | Line | String | 35 | 270px | left |
| 5 | workCenterName | Work Center | String | 33 | 260px | left |
| 6 | equipmentName | Equipment | String | 29 | 230px | left |
| 7 | processTagName | Process Tag | String | 33 | 260px | left |
| 8 | itemName | Item | String | 33 | 260px | left |
| 9 | comparison | Comparison | String | 12 | 110px | left |
| 10 | thresholdValue | Threshold Value | Decimal128 | 5 | 150px | right |
| 11 | thresholdUpperValue | Threshold Upper Value | Decimal128 | 5 | 190px | right |
| 12 | evaluationWindowMinutes | Evaluation Window (min) | Int32 | 3 | 210px | right |
| 13 | severityClass | Severity Class | String | 6 | 140px | left |
| 14 | actionType | Action Type | String | 21 | 170px | left |
| 15 | notificationTypeName | Notification Type | String | 18 | 160px | left |
| 16 | escalationRuleName | Escalation Rule | String | 35 | 270px | left |
| 17 | falseAlertCount | False Alert Count | Int32 | 1 | 160px | right |
| 18 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); processTagId (reference key, shown through processTagName); itemId (reference key, shown through itemName); notificationTypeId (reference key, shown through notificationTypeName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_analyticsModel - Analytics Models (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_analyticsModel.json | _id: mes_syst_analyticsModelStable | rel: CL20261018-23:51 | samples: 10 | columns: 15 | total width: 2910px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | name | Name | String | 45 | 300px | left |
| 3 | modelType | Model Type | String | 25 | 200px | left |
| 4 | modelVersion | Model Version | String | 3 | 140px | left |
| 5 | framework | Framework | String | 37 | 280px | left |
| 6 | trainingDatasetRef | Training Dataset Ref | String | 44 | 300px | left |
| 7 | validationMetricName | Validation Metric Name | String | 21 | 200px | left |
| 8 | validationMetricValue | Validation Metric Value | Decimal128 | 5 | 210px | right |
| 9 | equipmentName | Equipment | String | 31 | 240px | left |
| 10 | modelControlledDocumentName | Model Controlled Document | String | 0 | 220px | left |
| 11 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 12 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 13 | approvedBy | Approved By | String | 15 | 130px | left |
| 14 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 14 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); modelControlledDocumentId (reference key, shown through modelControlledDocumentName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): modelControlledDocumentName

## u_mes_syst_auditTrail - Audit Trail (Audit Trail)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_auditTrail.json | _id: mes_syst_auditTrailStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | relatedCollectionName | Related Collection Name | String | 25 | 210px | left |
| 3 | relatedEntityName | Related Entity | String | 45 | 300px | left |
| 4 | changeAction | Change Action | String | 6 | 140px | left |
| 5 | changedAt | Changed At | Date/Datetime | 19 | 160px | center |
| 6 | changedBy | Changed By | String | 14 | 120px | left |
| 7 | reasonText | Reason Text | String | 43 | 300px | left |
| 8 | electronicSignatureName | Electronic Signature | String | 15 | 180px | left |
| 9 | clientIp | Client IP | String | 11 | 110px | left |
| 10 | application | Application | String | 25 | 200px | left |
| 11 | documentVersionBefore | Document Version Before | Int32 | 1 | 210px | right |
| 12 | documentVersionAfter | Document Version After | Int32 | 1 | 200px | right |
| 13 | previousHash | Previous Hash | String | 64 | 300px | left |
| 14 | entryHash | Entry Hash | String | 64 | 300px | left |
| 15 | gxpRelevant | Gxp Relevant | Boolean | 3 | 130px | center |
| 16 | auditTrailReviewName | Audit Trail Review | String | 16 | 170px | left |
| 17 | createdBy | Created By | String | 18 | 150px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 18 | 150px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); changedById (reference key, shown through changedBy); electronicSignatureId (reference key, shown through electronicSignatureName); auditTrailReviewId (reference key, shown through auditTrailReviewName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_auditTrailChange - Audit Trail Changes (Audit Trail)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_auditTrailChange.json | _id: mes_syst_auditTrailChangeStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1420px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | auditTrailName | Audit Trail | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | changedFieldName | Changed Field Name | String | 14 | 170px | left |
| 5 | oldValue | Old Value | String | 4 | 110px | left |
| 6 | newValue | New Value | String | 4 | 110px | left |
| 7 | createdBy | Created By | String | 18 | 150px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 18 | 150px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); auditTrailId (reference key, shown through auditTrailName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_auditTrailReview - Audit Trail Reviews (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_auditTrailReview.json | _id: mes_syst_auditTrailReviewStable | rel: CL20261018-23:51 | samples: 10 | columns: 20 | total width: 3730px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | reviewType | Review Type | String | 22 | 180px | left |
| 3 | computerisedSystemName | Computerised System | String | 53 | 300px | left |
| 4 | relatedCollectionName | Related Collection Name | String | 31 | 240px | left |
| 5 | relatedEntityName | Related Entity | String | 57 | 300px | left |
| 6 | reviewFromAt | Review From At | Date/Datetime | 19 | 160px | center |
| 7 | reviewToAt | Review to At | Date/Datetime | 19 | 160px | center |
| 8 | entriesReviewedCount | Entries Reviewed Count | Int32 | 4 | 200px | right |
| 9 | criticalEntriesCount | Critical Entries Count | Int32 | 3 | 200px | right |
| 10 | anomalyCount | Anomaly Count | Int32 | 1 | 140px | right |
| 11 | findingsText | Findings Text | String | 82 | 300px | left |
| 12 | nonconformanceName | Nonconformance | String | 49 | 300px | left |
| 13 | reviewedBy | Reviewed By | String | 14 | 120px | left |
| 14 | reviewedAt | Reviewed At | Date/Datetime | 19 | 160px | center |
| 15 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 16 | status | Status | String | 9 | 90px | left |
| 17 | createdBy | Created By | String | 14 | 120px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 14 | 120px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); computerisedSystemId (reference key, shown through computerisedSystemName); relatedEntityId (reference key, shown through relatedEntityName); nonconformanceId (reference key, shown through nonconformanceName); reviewedById (reference key, shown through reviewedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): electronicSignatureName

## u_mes_syst_backupRun - Backup and Restore Runs (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_backupRun.json | _id: mes_syst_backupRunStable | rel: CL20261018-23:51 | samples: 10 | columns: 15 | total width: 2390px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | runType | Run Type | String | 18 | 150px | left |
| 3 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 4 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 5 | sizeBytes | Size Bytes | Int64 | 12 | 110px | right |
| 6 | storageTarget | Storage Target | String | 47 | 300px | left |
| 7 | recoveryTimeMinutes | Recovery Time (min) | Int32 | 2 | 180px | right |
| 8 | recoveryPointMinutes | Recovery Point (min) | Int32 | 2 | 180px | right |
| 9 | evidenceControlledDocumentName | Evidence Controlled Document | String | 0 | 240px | left |
| 10 | performedBy | Performed By | String | 11 | 130px | left |
| 11 | status | Status | String | 9 | 90px | left |
| 12 | createdBy | Created By | String | 14 | 120px | left |
| 13 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 14 | updatedBy | Updated By | String | 14 | 120px | left |
| 15 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); evidenceControlledDocumentId (reference key, shown through evidenceControlledDocumentName); performedById (reference key, shown through performedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): evidenceControlledDocumentName

## u_mes_syst_businessEvent - Business Events (Audit Trail)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_businessEvent.json | _id: mes_syst_businessEventStable | rel: CL20261018-23:51 | samples: 10 | columns: 20 | total width: 3650px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | eventType | Event Type | String | 19 | 160px | left |
| 3 | eventCategory | Event Category | String | 11 | 140px | left |
| 4 | occurredAt | Occurred At | Date/Datetime | 19 | 160px | center |
| 5 | relatedCollectionName | Related Collection Name | String | 29 | 230px | left |
| 6 | relatedEntityName | Related Entity | String | 15 | 140px | left |
| 7 | workCenterName | Work Center | String | 33 | 260px | left |
| 8 | equipmentName | Equipment | String | 31 | 240px | left |
| 9 | productionOrderName | Production Order | String | 10 | 160px | left |
| 10 | userName | User | String | 14 | 120px | left |
| 11 | iotDeviceName | IoT Device | String | 38 | 290px | left |
| 12 | severity | Severity | Int32 | 2 | 100px | right |
| 13 | messageText | Message Text | String | 49 | 300px | left |
| 14 | eventPayloadText | Event Payload Text | String | 38 | 290px | left |
| 15 | correlationNo | Correlation No | String | 36 | 280px | left |
| 16 | source | Source | String | 12 | 110px | left |
| 17 | createdBy | Created By | String | 10 | 110px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 10 | 110px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); productionOrderId (reference key, shown through productionOrderName); userId (reference key, shown through userName); iotDeviceId (reference key, shown through iotDeviceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_computerisedSystem - Computerised Systems (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_computerisedSystem.json | _id: mes_syst_computerisedSystemStable | rel: CL20261018-23:51 | samples: 10 | columns: 19 | total width: 3590px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 57 | 300px | left |
| 3 | description | Description | String | 153 | 300px | left |
| 4 | systemCategory | System Category | String | 30 | 230px | left |
| 5 | gampCategory | Gamp Category | String | 10 | 140px | left |
| 6 | gxpImpact | Gxp Impact | String | 8 | 110px | left |
| 7 | dataCriticality | Data Criticality | String | 6 | 160px | left |
| 8 | holdsElectronicRecords | Holds Electronic Records | Boolean | 3 | 210px | center |
| 9 | usesElectronicSignatures | Uses Electronic Signatures | Boolean | 3 | 230px | center |
| 10 | systemOwnerUserName | System Owner User | String | 14 | 160px | left |
| 11 | processOwnerUserName | Process Owner User | String | 14 | 170px | left |
| 12 | supplierName | Supplier | String | 0 | 100px | left |
| 13 | equipmentName | Equipment | String | 36 | 280px | left |
| 14 | softwareVersion | Software Version | String | 18 | 160px | left |
| 15 | hostingModel | Hosting Model | String | 13 | 140px | left |
| 16 | lastValidatedDate | Last Validated Date | Date/Date | 10 | 180px | center |
| 17 | periodicReviewIntervalMonths | Periodic Review Interval Months | Int32 | 2 | 260px | right |
| 18 | nextPeriodicReviewDate | Next Periodic Review Date | Date/Date | 10 | 220px | center |
| 19 | status | Status | String | 13 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); systemOwnerUserId (reference key, shown through systemOwnerUserName); processOwnerUserId (reference key, shown through processOwnerUserName); supplierId (reference key, shown through supplierName); equipmentId (reference key, shown through equipmentName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): supplierName

## u_mes_syst_controlledDocument - Controlled Documents (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_controlledDocument.json | _id: mes_syst_controlledDocumentStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4470px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | title | Title | String | 78 | 300px | left |
| 3 | documentTypeName | Document Type | String | 28 | 220px | left |
| 4 | revision | Revision | String | 1 | 100px | left |
| 5 | itemName | Item | String | 61 | 300px | left |
| 6 | relatedCollectionName | Related Collection Name | String | 15 | 210px | left |
| 7 | relatedEntityName | Related Entity | String | 61 | 300px | left |
| 8 | fileName | File Name | String | 25 | 200px | left |
| 9 | mimeType | Mime Type | String | 15 | 130px | left |
| 10 | sizeBytes | Size Bytes | Int64 | 6 | 110px | right |
| 11 | storageProvider | Storage Provider | String | 2 | 160px | left |
| 12 | storageKey | Storage Key | String | 39 | 300px | left |
| 13 | checksumSha256 | Checksum Sha256 | String | 64 | 300px | left |
| 14 | languageName | Language | String | 7 | 100px | left |
| 15 | authorUserName | Author User | String | 14 | 120px | left |
| 16 | approvedBy | Approved By | String | 0 | 120px | left |
| 17 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 18 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 19 | expiresAt | Expires At | Date/Datetime | 19 | 160px | center |
| 20 | retentionYears | Retention Years | Int32 | 2 | 150px | right |
| 21 | isControlled | Controlled | Boolean | 3 | 110px | center |
| 22 | status | Status | String | 8 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); documentTypeId (reference key, shown through documentTypeName); itemId (reference key, shown through itemName); relatedEntityId (reference key, shown through relatedEntityName); languageId (reference key, shown through languageName); authorUserId (reference key, shown through authorUserName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_syst_controlledDocumentTag - Controlled Document Tags (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_controlledDocumentTag.json | _id: mes_syst_controlledDocumentTagStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1240px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | controlledDocumentName | Controlled Document | String | 57 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | tag | Tag | String | 7 | 80px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); controlledDocumentId (reference key, shown through controlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_deviceType - Device Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_deviceType.json | _id: mes_syst_deviceTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 24 | 190px | left |
| 3 | description | Description | String | 36 | 280px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_documentType - Document Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_documentType.json | _id: mes_syst_documentTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 28 | 220px | left |
| 3 | description | Description | String | 37 | 280px | left |
| 4 | retentionYears | Retention Years | Int32 | 2 | 150px | right |
| 5 | isControlled | Controlled | Boolean | 3 | 110px | center |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_electronicSignature - Electronic Signatures (Audit Trail)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_electronicSignature.json | _id: mes_syst_electronicSignatureStable | rel: CL20261018-23:51 | samples: 20 | columns: 21 | total width: 3920px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | relatedCollectionName | Related Collection Name | String | 17 | 210px | left |
| 3 | relatedEntityName | Related Entity | String | 56 | 300px | left |
| 4 | userName | User | String | 14 | 120px | left |
| 5 | roleName | Role | String | 35 | 270px | left |
| 6 | signatureMeaningName | Signature Meaning | String | 13 | 160px | left |
| 7 | signedAt | Signed At | Date/Datetime | 19 | 160px | center |
| 8 | authenticationMethod | Authentication Method | String | 8 | 190px | left |
| 9 | contentHash | Content Hash | String | 64 | 300px | left |
| 10 | comment | Comment | String | 58 | 300px | left |
| 11 | clientIp | Client IP | String | 11 | 110px | left |
| 12 | workstation | Workstation | String | 14 | 120px | left |
| 13 | isSecondSignature | Second Signature | Boolean | 3 | 160px | center |
| 14 | witnessUserName | Witness User | String | 0 | 130px | left |
| 15 | signatureManifestationText | Signature Manifestation Text | String | 52 | 300px | left |
| 16 | signedRecordVersion | Signed Record Version | Int32 | 1 | 190px | right |
| 17 | isFirstSigningInSession | First Signing in Session | Boolean | 3 | 210px | center |
| 18 | createdBy | Created By | String | 14 | 120px | left |
| 19 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 20 | updatedBy | Updated By | String | 14 | 120px | left |
| 21 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); userId (reference key, shown through userName); roleId (reference key, shown through roleName); signatureMeaningId (reference key, shown through signatureMeaningName); witnessUserId (reference key, shown through witnessUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): witnessUserName

## u_mes_syst_enumerationValue - Enumeration Values (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_enumerationValue.json | _id: mes_syst_enumerationValueStable | rel: CL20261018-23:51 | samples: 20 | columns: 9 | total width: 1580px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 42 | 300px | left |
| 2 | collectionName | Collection Name | String | 29 | 230px | left |
| 3 | fieldName | Field Name | String | 9 | 110px | left |
| 4 | valueCode | Value Code | String | 21 | 170px | left |
| 5 | valueName | Value Name | String | 21 | 170px | left |
| 6 | description | Description | String | 71 | 300px | left |
| 7 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 8 | isDefault | Default | Boolean | 3 | 90px | center |
| 9 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_erpMessage - ERP Messages (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_erpMessage.json | _id: mes_syst_erpMessageStable | rel: CL20261018-23:51 | samples: 10 | columns: 29 | total width: 4760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | integrationConnectorName | Integration Connector | String | 41 | 300px | left |
| 3 | direction | Direction | String | 8 | 110px | left |
| 4 | messageType | Message Type | String | 25 | 200px | left |
| 5 | idempotencyKey | Idempotency Key | String | 25 | 200px | left |
| 6 | correlationNo | Correlation No | String | 36 | 280px | left |
| 7 | relatedCollectionName | Related Collection Name | String | 26 | 210px | left |
| 8 | relatedEntityName | Related Entity | String | 10 | 140px | left |
| 9 | productionOrderName | Production Order | String | 10 | 160px | left |
| 10 | goodsReceiptName | Goods Receipt | String | 0 | 140px | left |
| 11 | shipmentName | Shipment | String | 0 | 100px | left |
| 12 | payload | Payload | String | 40 | 300px | left |
| 13 | payloadFormat | Payload Format | String | 4 | 140px | left |
| 14 | payloadHash | Payload Hash | String | 64 | 300px | left |
| 15 | attempts | Attempts | Int32 | 1 | 100px | right |
| 16 | maxAttempts | Max Attempts | Int32 | 1 | 130px | right |
| 17 | createdInSourceAt | Created in Source At | Date/Datetime | 19 | 180px | center |
| 18 | receivedAt | Received At | Date/Datetime | 19 | 160px | center |
| 19 | processedAt | Processed At | Date/Datetime | 19 | 160px | center |
| 20 | nextRetryAt | Next Retry At | Date/Datetime | 0 | 140px | center |
| 21 | errorCode | Error Code | String | 0 | 110px | left |
| 22 | errorText | Error Text | String | 0 | 110px | left |
| 23 | erpDocumentNo | ERP Document No | String | 10 | 150px | left |
| 24 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 25 | status | Status | String | 12 | 110px | left |
| 26 | createdBy | Created By | String | 10 | 110px | left |
| 27 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 28 | updatedBy | Updated By | String | 10 | 110px | left |
| 29 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); integrationConnectorId (reference key, shown through integrationConnectorName); relatedEntityId (reference key, shown through relatedEntityName); productionOrderId (reference key, shown through productionOrderName); goodsReceiptId (reference key, shown through goodsReceiptName); shipmentId (reference key, shown through shipmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): goodsReceiptName, shipmentName, nextRetryAt, errorCode, errorText

## u_mes_syst_escalationRule - Escalation Rules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_escalationRule.json | _id: mes_syst_escalationRuleStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 35 | 270px | left |
| 3 | sourceType | Source Type | String | 14 | 120px | left |
| 4 | severityClass | Severity Class | String | 8 | 140px | left |
| 5 | lineName | Line | String | 29 | 230px | left |
| 6 | firstResponderRoleName | First Responder Role | String | 22 | 180px | left |
| 7 | requiredSkillName | Required Skill | String | 0 | 140px | left |
| 8 | responseTargetMinutes | Response Target (min) | Int32 | 3 | 190px | right |
| 9 | resolutionTargetMinutes | Resolution Target (min) | Int32 | 4 | 210px | right |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); firstResponderRoleId (reference key, shown through firstResponderRoleName); requiredSkillId (reference key, shown through requiredSkillName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): requiredSkillName

## u_mes_syst_escalationRuleLevel - Escalation Levels (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_escalationRuleLevel.json | _id: mes_syst_escalationRuleLevelStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1180px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | escalationRuleName | Escalation Rule | String | 33 | 260px | left |
| 3 | level | Level | Int32 | 1 | 80px | right |
| 4 | delayMinutes | Delay (min) | Int32 | 3 | 120px | right |
| 5 | basis | Basis | String | 16 | 140px | left |
| 6 | roleName | Role | String | 21 | 170px | left |
| 7 | notificationTypeName | Notification Type | String | 16 | 160px | left |
| 8 | channel | Channel | String | 11 | 100px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); escalationRuleId (reference key, shown through escalationRuleName); roleId (reference key, shown through roleName); notificationTypeId (reference key, shown through notificationTypeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_integrationConnector - Integration Connectors (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_integrationConnector.json | _id: mes_syst_integrationConnectorStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2870px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 8 | 110px | left |
| 2 | name | Name | String | 41 | 300px | left |
| 3 | connectorType | Connector Type | String | 22 | 180px | left |
| 4 | targetSystem | Target System | String | 11 | 140px | left |
| 5 | protocol | Protocol | String | 15 | 130px | left |
| 6 | endpoint | Endpoint | String | 47 | 300px | left |
| 7 | environment | Environment | String | 10 | 120px | left |
| 8 | authMethod | Auth Method | String | 25 | 200px | left |
| 9 | credentialRef | Credential Ref | String | 23 | 190px | left |
| 10 | timeoutMs | Timeout Ms | Int32 | 5 | 110px | right |
| 11 | retryPolicyMaxAttempts | Retry Policy Max Attempts | Int32 | 1 | 220px | right |
| 12 | retryPolicyBackoffSec | Retry Policy Backoff (s) | Int32 | 2 | 210px | right |
| 13 | lastSuccessAt | Last Success At | Date/Datetime | 19 | 160px | center |
| 14 | lastFailureAt | Last Failure At | Date/Datetime | 0 | 150px | center |
| 15 | healthStatus | Health Status | String | 8 | 140px | left |
| 16 | ownerUserName | Owner User | String | 14 | 120px | left |
| 17 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastFailureAt

## u_mes_syst_integrationConnectorFunction - Integration Connector Functions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_integrationConnectorFunction.json | _id: mes_syst_integrationConnectorFunctionStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1360px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | integrationConnectorName | Integration Connector | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | functionName | Function Name | String | 25 | 200px | left |
| 5 | direction | Direction | String | 8 | 110px | left |
| 6 | messageType | Message Type | String | 25 | 200px | left |
| 7 | endpointPath | Endpoint Path | String | 17 | 140px | left |
| 8 | scheduleExpression | Schedule Expression | String | 11 | 180px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); integrationConnectorId (reference key, shown through integrationConnectorName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_interlockRule - Interlock Rules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_interlockRule.json | _id: mes_syst_interlockRuleStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 3640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 51 | 300px | left |
| 3 | ruleType | Rule Type | String | 17 | 140px | left |
| 4 | transactionPoint | Transaction Point | String | 18 | 160px | left |
| 5 | lineName | Line | String | 35 | 270px | left |
| 6 | workCenterName | Work Center | String | 37 | 280px | left |
| 7 | operationName | Operation | String | 29 | 230px | left |
| 8 | itemName | Item | String | 46 | 300px | left |
| 9 | enforcementMode | Enforcement Mode | String | 7 | 160px | left |
| 10 | overrideAllowed | Override Allowed | Boolean | 3 | 160px | center |
| 11 | overrideRoleName | Override Role | String | 24 | 190px | left |
| 12 | overrideRequiresSignature | Override Requires Signature | Boolean | 3 | 230px | center |
| 13 | overrideRequiresReasonCode | Override Requires Reason Code | Boolean | 3 | 250px | center |
| 14 | escalationRuleName | Escalation Rule | String | 33 | 260px | left |
| 15 | messageText | Message Text | String | 93 | 300px | left |
| 16 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 17 | validTo | Valid to | Date/Date | 0 | 100px | center |
| 18 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); operationId (reference key, shown through operationName); itemId (reference key, shown through itemName); overrideRoleId (reference key, shown through overrideRoleName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): validTo

## u_mes_syst_iotDevice - IoT Devices (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_iotDevice.json | _id: mes_syst_iotDeviceStable | rel: CL20261019-12:24 | samples: 20 | columns: 23 | total width: 3950px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 47 | 300px | left |
| 3 | deviceTypeName | Device Type | String | 24 | 190px | left |
| 4 | manufacturerName | Manufacturer | String | 28 | 220px | left |
| 5 | model | Model | String | 21 | 170px | left |
| 6 | serialNo | Serial No | String | 14 | 120px | left |
| 7 | firmwareVersion | Firmware Version | String | 6 | 160px | left |
| 8 | equipmentName | Equipment | String | 54 | 300px | left |
| 9 | workCenterName | Work Center | String | 37 | 280px | left |
| 10 | integrationConnectorName | Integration Connector | String | 41 | 300px | left |
| 11 | ipAddress | IP Address | String | 10 | 110px | left |
| 12 | macAddress | Mac Address | String | 17 | 140px | left |
| 13 | port | Port | Int32 | 4 | 80px | right |
| 14 | protocol | Protocol | String | 13 | 120px | left |
| 15 | vlan | Vlan | Int32 | 3 | 80px | right |
| 16 | opcNodeAddress | Opc Node Address | String | 18 | 160px | left |
| 17 | pollIntervalMs | Poll Interval Ms | Int32 | 4 | 160px | right |
| 18 | lastSeenAt | Last Seen At | Date/Datetime | 0 | 130px | center |
| 19 | connectionStatus | Connection Status | String | 7 | 160px | left |
| 20 | certificateExpiresAt | Certificate Expires At | Date/Date | 10 | 200px | center |
| 21 | installedAt | Installed At | Date/Datetime | 19 | 160px | center |
| 22 | edgeGatewayIotDeviceName | Edge Gateway IoT Device | String | 0 | 210px | left |
| 23 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); deviceTypeId (reference key, shown through deviceTypeName); manufacturerId (reference key, shown through manufacturerName); equipmentId (reference key, shown through equipmentName); workCenterId (reference key, shown through workCenterName); integrationConnectorId (reference key, shown through integrationConnectorName); edgeGatewayIotDeviceId (reference key, shown through edgeGatewayIotDeviceName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastSeenAt, edgeGatewayIotDeviceName

## u_mes_syst_iotHubIdentity - IoT Hub Identities (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_iotHubIdentity.json | _id: mes_syst_iotHubIdentityStable | rel: CL20261019-12:24 | samples: 10 | columns: 17 | total width: 3350px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 46 | 300px | left |
| 3 | identityType | Identity Type | String | 16 | 140px | left |
| 4 | iotHubName | IoT Hub Name | String | 14 | 130px | left |
| 5 | equipmentName | Equipment | String | 31 | 240px | left |
| 6 | iotDeviceName | IoT Device | String | 38 | 290px | left |
| 7 | parentIotHubIdentityName | Parent IoT Hub Identity | String | 46 | 300px | left |
| 8 | authenticationMethod | Authentication Method | String | 15 | 190px | left |
| 9 | certificateThumbprint | Certificate Thumbprint | String | 40 | 300px | left |
| 10 | certificateExpiresAt | Certificate Expires At | Date/Date | 10 | 200px | center |
| 11 | provisioningStatus | Provisioning Status | String | 11 | 180px | left |
| 12 | lastRegistrySyncAt | Last Registry Sync At | Date/Datetime | 19 | 190px | center |
| 13 | twinTagsVersion | Twin Tags Version | Int32 | 1 | 160px | right |
| 14 | lastSyncErrorText | Last Sync Error Text | String | 0 | 180px | left |
| 15 | connectionState | Connection State | String | 12 | 160px | left |
| 16 | connectionStateAt | Connection State At | Date/Datetime | 19 | 180px | center |
| 17 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); iotDeviceId (reference key, shown through iotDeviceName); parentIotHubIdentityId (reference key, shown through parentIotHubIdentityName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastSyncErrorText

## u_mes_syst_modelPrediction - Model Predictions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_modelPrediction.json | _id: mes_syst_modelPredictionStable | rel: CL20261018-23:51 | samples: 10 | columns: 26 | total width: 4280px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | analyticsModelName | Analytics Model | String | 45 | 300px | left |
| 3 | modelVersion | Model Version | String | 3 | 140px | left |
| 4 | predictionType | Prediction Type | String | 21 | 170px | left |
| 5 | relatedCollectionName | Related Collection Name | String | 20 | 210px | left |
| 6 | relatedEntityName | Related Entity | String | 33 | 260px | left |
| 7 | workCenterName | Work Center | String | 33 | 260px | left |
| 8 | productVariantName | Product Variant | String | 26 | 210px | left |
| 9 | shiftName | Shift | String | 7 | 80px | left |
| 10 | predictedAt | Predicted At | Date/Datetime | 19 | 160px | center |
| 11 | horizonMinutes | Horizon (min) | Int32 | 3 | 140px | right |
| 12 | predictedClass | Predicted Class | String | 17 | 150px | left |
| 13 | predictedValue | Predicted Value | Decimal128 | 4 | 150px | right |
| 14 | confidence | Confidence | Decimal128 | 5 | 110px | right |
| 15 | recommendedAction | Recommended Action | String | 46 | 300px | left |
| 16 | actionStatus | Action Status | String | 12 | 140px | left |
| 17 | actionTakenBy | Action Taken By | String | 14 | 150px | left |
| 18 | actionTakenAt | Action Taken At | Date/Datetime | 19 | 160px | center |
| 19 | actualValue | Actual Value | Decimal128 | 4 | 130px | right |
| 20 | actualClass | Actual Class | String | 11 | 130px | left |
| 21 | notificationName | Notification | String | 0 | 130px | left |
| 22 | status | Status | String | 8 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); analyticsModelId (reference key, shown through analyticsModelName); relatedEntityId (reference key, shown through relatedEntityName); workCenterId (reference key, shown through workCenterName); productVariantId (reference key, shown through productVariantName); shiftId (reference key, shown through shiftName); actionTakenById (reference key, shown through actionTakenBy); notificationId (reference key, shown through notificationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): notificationName

## u_mes_syst_notification - Notifications (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_notification.json | _id: mes_syst_notificationStable | rel: CL20261018-23:51 | samples: 10 | columns: 26 | total width: 4770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | notificationTypeName | Notification Type | String | 22 | 180px | left |
| 3 | severity | Severity | Int32 | 2 | 100px | right |
| 4 | title | Title | String | 50 | 300px | left |
| 5 | bodyText | Body Text | String | 60 | 300px | left |
| 6 | relatedCollectionName | Related Collection Name | String | 21 | 210px | left |
| 7 | relatedEntityName | Related Entity | String | 60 | 300px | left |
| 8 | andonEventName | Andon Event | String | 42 | 300px | left |
| 9 | alarmName | Alarm | String | 15 | 130px | left |
| 10 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 11 | escalationLevel | Escalation Level | Int32 | 1 | 160px | right |
| 12 | raisedAt | Raised At | Date/Datetime | 19 | 160px | center |
| 13 | acknowledgedBy | Acknowledged By | String | 12 | 150px | left |
| 14 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 15 | expiresAt | Expires At | Date/Datetime | 19 | 160px | center |
| 16 | alertRuleName | Alert Rule | String | 40 | 300px | left |
| 17 | escalationRuleName | Escalation Rule | String | 30 | 230px | left |
| 18 | responseDueAt | Response Due At | Date/Datetime | 19 | 160px | center |
| 19 | resolvedAt | Resolved At | Date/Datetime | 0 | 120px | center |
| 20 | resolvedBy | Resolved By | String | 0 | 120px | left |
| 21 | interlockEventName | Interlock Event | String | 18 | 150px | left |
| 22 | status | Status | String | 12 | 110px | left |
| 23 | createdBy | Created By | String | 10 | 110px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 10 | 110px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); notificationTypeId (reference key, shown through notificationTypeName); relatedEntityId (reference key, shown through relatedEntityName); andonEventId (reference key, shown through andonEventName); alarmId (reference key, shown through alarmName); nonconformanceId (reference key, shown through nonconformanceName); acknowledgedById (reference key, shown through acknowledgedBy); alertRuleId (reference key, shown through alertRuleName); escalationRuleId (reference key, shown through escalationRuleName); resolvedById (reference key, shown through resolvedBy); interlockEventId (reference key, shown through interlockEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): resolvedAt, resolvedBy

## u_mes_syst_notificationRecipient - Notification Recipients (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_notificationRecipient.json | _id: mes_syst_notificationRecipientStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 2000px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | notificationName | Notification | String | 50 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | userName | User | String | 14 | 120px | left |
| 5 | roleName | Role | String | 22 | 180px | left |
| 6 | channel | Channel | String | 11 | 100px | left |
| 7 | sentAt | Sent At | Date/Datetime | 19 | 160px | center |
| 8 | deliveredAt | Delivered At | Date/Datetime | 19 | 160px | center |
| 9 | readAt | Read At | Date/Datetime | 19 | 160px | center |
| 10 | createdBy | Created By | String | 10 | 110px | left |
| 11 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 12 | updatedBy | Updated By | String | 10 | 110px | left |
| 13 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); notificationId (reference key, shown through notificationName); userId (reference key, shown through userName); roleId (reference key, shown through roleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_notificationType - Notification Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_notificationType.json | _id: mes_syst_notificationTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 22 | 180px | left |
| 3 | description | Description | String | 33 | 260px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_numberRange - Number Ranges (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_numberRange.json | _id: mes_syst_numberRangeStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 2670px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 33 | 260px | left |
| 3 | rangeType | Range Type | String | 13 | 120px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | prefix | Prefix | String | 4 | 90px | left |
| 6 | formatMask | Format Mask | String | 25 | 200px | left |
| 7 | currentValue | Current Value | Int64 | 3 | 140px | right |
| 8 | minValue | Min Value | Int64 | 1 | 110px | right |
| 9 | maxValue | Max Value | Int64 | 5 | 110px | right |
| 10 | incrementBy | Increment By | String | 14 | 130px | left |
| 11 | resetPolicy | Reset Policy | String | 5 | 130px | left |
| 12 | lastResetAt | Last Reset At | Date/Datetime | 0 | 140px | center |
| 13 | checkDigitMethod | Check Digit Method | String | 0 | 170px | left |
| 14 | warnAtPct | Warn At (%) | Decimal128 | 4 | 120px | right |
| 15 | lastIssuedValue | Last Issued Value | Int64 | 3 | 160px | right |
| 16 | lastIssuedAt | Last Issued At | Date/Datetime | 0 | 140px | center |
| 17 | exampleValue | Example Value | String | 13 | 140px | left |
| 18 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); incrementById (reference key, shown through incrementBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastResetAt, checkDigitMethod, lastIssuedAt

## u_mes_syst_operatorApp - Operator Apps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorApp.json | _id: mes_syst_operatorAppStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1480px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 47 | 300px | left |
| 3 | appType | App Type | String | 16 | 140px | left |
| 4 | version | Version | Int32 | 1 | 90px | right |
| 5 | publishedBy | Published By | String | 0 | 130px | left |
| 6 | publishedAt | Published At | Date/Datetime | 0 | 130px | center |
| 7 | approvedBy | Approved By | String | 0 | 120px | left |
| 8 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 9 | previousVersionOperatorAppName | Previous Version Operator App | String | 0 | 250px | left |
| 10 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); publishedById (reference key, shown through publishedBy); approvedById (reference key, shown through approvedBy); previousVersionOperatorAppId (reference key, shown through previousVersionOperatorAppName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): publishedBy, publishedAt, approvedBy, approvedAt, previousVersionOperatorAppName

## u_mes_syst_operatorAppDeviceBinding - Operator App Device Bindings (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppDeviceBinding.json | _id: mes_syst_operatorAppDeviceBindingStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 970px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | operatorAppName | Operator App | String | 40 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | iotDeviceName | IoT Device | String | 36 | 280px | left |
| 5 | purpose | Purpose | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppId (reference key, shown through operatorAppName); iotDeviceId (reference key, shown through iotDeviceName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_operatorAppLanguage - Operator App Languages (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppLanguage.json | _id: mes_syst_operatorAppLanguageStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | operatorAppName | Operator App | String | 47 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | languageName | Language | String | 7 | 100px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppId (reference key, shown through operatorAppName); languageId (reference key, shown through languageName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_operatorAppOperation - Operator App Operations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppOperation.json | _id: mes_syst_operatorAppOperationStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 730px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | operatorAppName | Operator App | String | 47 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | operationName | Operation | String | 24 | 190px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppId (reference key, shown through operatorAppName); operationId (reference key, shown through operationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_operatorAppStep - Operator App Steps (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppStep.json | _id: mes_syst_operatorAppStepStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1560px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | operatorAppName | Operator App | String | 40 | 300px | left |
| 3 | stepNo | Step No | Int32 | 2 | 90px | right |
| 4 | name | Name | String | 22 | 180px | left |
| 5 | widgetType | Widget Type | String | 16 | 140px | left |
| 6 | workInstructionName | Work Instruction | String | 44 | 300px | left |
| 7 | inspectionPlanName | Inspection Plan | String | 42 | 300px | left |
| 8 | nextStepNo | Next Step No | Int32 | 2 | 130px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppId (reference key, shown through operatorAppName); workInstructionId (reference key, shown through workInstructionName); inspectionPlanId (reference key, shown through inspectionPlanName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_operatorAppStepTrigger - Operator App Step Triggers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppStepTrigger.json | _id: mes_syst_operatorAppStepTriggerStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | operatorAppStepName | Operator App Step | String | 14 | 160px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | triggerEvent | Trigger Event | String | 11 | 140px | left |
| 5 | triggerAction | Trigger Action | String | 10 | 140px | left |
| 6 | triggerTarget | Trigger Target | String | 2 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppStepId (reference key, shown through operatorAppStepName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_operatorAppWorkCenter - Operator App Work Centers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_operatorAppWorkCenter.json | _id: mes_syst_operatorAppWorkCenterStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | operatorAppName | Operator App | String | 47 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | workCenterName | Work Center | String | 33 | 260px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operatorAppId (reference key, shown through operatorAppName); workCenterId (reference key, shown through workCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_recordPolicy - Record Policies (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_recordPolicy.json | _id: mes_syst_recordPolicyStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 2260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 33 | 260px | left |
| 2 | collectionName | Collection Name | String | 29 | 230px | left |
| 3 | editPolicy | Edit Policy | String | 18 | 150px | left |
| 4 | lockOnStatusDefinitionName | Lock on Status Definition | String | 0 | 220px | left |
| 5 | requiresReasonForEdit | Requires Reason for Edit | Boolean | 3 | 210px | center |
| 6 | requiresSignatureForEdit | Requires Signature for Edit | Boolean | 3 | 230px | center |
| 7 | editRoleName | Edit Role | String | 35 | 270px | left |
| 8 | deleteAllowed | Delete Allowed | Boolean | 3 | 140px | center |
| 9 | retentionYears | Retention Years | Int32 | 2 | 150px | right |
| 10 | archiveAfterMonths | Archive After Months | Int32 | 2 | 180px | right |
| 11 | gxpRelevant | Gxp Relevant | Boolean | 3 | 130px | center |
| 12 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lockOnStatusDefinitionId (reference key, shown through lockOnStatusDefinitionName); editRoleId (reference key, shown through editRoleName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lockOnStatusDefinitionName

## u_mes_syst_savedView - Saved Views (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_savedView.json | _id: mes_syst_savedViewStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 45 | 300px | left |
| 3 | viewType | View Type | String | 10 | 110px | left |
| 4 | collectionName | Collection Name | String | 33 | 260px | left |
| 5 | filterJson | Filter Json | String | 81 | 300px | left |
| 6 | sortJson | Sort Json | String | 25 | 200px | left |
| 7 | ownerUserName | Owner User | String | 15 | 130px | left |
| 8 | roleName | Role | String | 22 | 180px | left |
| 9 | isShared | Shared | Boolean | 3 | 90px | center |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); ownerUserId (reference key, shown through ownerUserName); roleId (reference key, shown through roleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_simulationStudy - Simulation Studies (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_simulationStudy.json | _id: mes_syst_simulationStudyStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 4190px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | title | Title | String | 82 | 300px | left |
| 3 | studyType | Study Type | String | 20 | 160px | left |
| 4 | relatedCollectionName | Related Collection Name | String | 26 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 40 | 300px | left |
| 6 | scenarioText | Scenario Text | String | 77 | 300px | left |
| 7 | inputSnapshotAt | Input Snapshot At | Date/Datetime | 19 | 160px | center |
| 8 | resultText | Result Text | String | 76 | 300px | left |
| 9 | predictedValue | Predicted Value | Decimal128 | 4 | 150px | right |
| 10 | predictedKpi | Predicted Kpi | String | 30 | 230px | left |
| 11 | recommendedRecipeName | Recommended Recipe | String | 40 | 300px | left |
| 12 | rolloutProductionOrderName | Rollout Production Order | String | 10 | 210px | left |
| 13 | actualValue | Actual Value | Decimal128 | 4 | 130px | right |
| 14 | comparisonResult | Comparison Result | String | 6 | 160px | left |
| 15 | resultControlledDocumentName | Result Controlled Document | String | 0 | 230px | left |
| 16 | approvedBy | Approved By | String | 15 | 130px | left |
| 17 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 18 | status | Status | String | 10 | 90px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); recommendedRecipeId (reference key, shown through recommendedRecipeName); rolloutProductionOrderId (reference key, shown through rolloutProductionOrderName); resultControlledDocumentId (reference key, shown through resultControlledDocumentName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): resultControlledDocumentName

## u_mes_syst_statusDefinition - Status Definitions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_statusDefinition.json | _id: mes_syst_statusDefinitionStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | collectionName | Collection Name | String | 26 | 210px | left |
| 3 | fieldName | Field Name | String | 6 | 110px | left |
| 4 | statusCode | Status Code | String | 11 | 120px | left |
| 5 | statusName | Status Name | String | 11 | 120px | left |
| 6 | description | Description | String | 44 | 300px | left |
| 7 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 8 | isInitial | Initial | Boolean | 3 | 90px | center |
| 9 | isFinal | Final | Boolean | 3 | 80px | center |
| 10 | colourCode | Colour Code | String | 7 | 120px | left |
| 11 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_statusTransition - Status Transitions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_statusTransition.json | _id: mes_syst_statusTransitionStable | rel: CL20261018-23:51 | samples: 10 | columns: 9 | total width: 1570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 37 | 280px | left |
| 2 | collectionName | Collection Name | String | 26 | 210px | left |
| 3 | fromStatusDefinitionName | From Status Definition | String | 11 | 200px | left |
| 4 | toStatusDefinitionName | To Status Definition | String | 11 | 180px | left |
| 5 | transitionName | Transition Name | String | 21 | 170px | left |
| 6 | requiresSignature | Requires Signature | Boolean | 3 | 170px | center |
| 7 | requiresReason | Requires Reason | Boolean | 3 | 150px | center |
| 8 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 9 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); fromStatusDefinitionId (reference key, shown through fromStatusDefinitionName); toStatusDefinitionId (reference key, shown through toStatusDefinitionName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_statusTransitionRole - Status Transition Roles (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_statusTransitionRole.json | _id: mes_syst_statusTransitionRoleStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 41 | 300px | left |
| 2 | statusTransitionName | Status Transition | String | 21 | 170px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | roleName | Role | String | 21 | 170px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); statusTransitionId (reference key, shown through statusTransitionName); roleId (reference key, shown through roleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_systemConfiguration - System Configurations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_systemConfiguration.json | _id: mes_syst_systemConfigurationStable | rel: CL20261018-23:51 | samples: 10 | columns: 14 | total width: 2050px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 24 | 190px | left |
| 2 | module | Module | String | 11 | 100px | left |
| 3 | description | Description | String | 82 | 300px | left |
| 4 | valueType | Value Type | String | 4 | 110px | left |
| 5 | configValueText | Config Value Text | String | 23 | 190px | left |
| 6 | configValueNumber | Config Value Number | Decimal128 | 0 | 180px | right |
| 7 | configValueFlag | Config Value Flag | Boolean | 3 | 160px | center |
| 8 | configValueJson | Config Value Json | String | 0 | 160px | left |
| 9 | scope | Scope | String | 10 | 90px | left |
| 10 | isEditable | Editable | Boolean | 3 | 100px | center |
| 11 | isSecret | Secret | Boolean | 3 | 90px | center |
| 12 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 13 | lastChangedReason | Last Changed Reason | String | 0 | 180px | left |
| 14 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): configValueNumber, configValueJson, lastChangedReason

## u_mes_syst_systemPeriodicReview - System Periodic Reviews (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_systemPeriodicReview.json | _id: mes_syst_systemPeriodicReviewStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 3940px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | computerisedSystemName | Computerised System | String | 57 | 300px | left |
| 3 | reviewPeriodFromDate | Review Period From Date | Date/Date | 10 | 210px | center |
| 4 | reviewPeriodToDate | Review Period to Date | Date/Date | 10 | 190px | center |
| 5 | changesReviewedCount | Changes Reviewed Count | Int32 | 1 | 200px | right |
| 6 | incidentsReviewedCount | Incidents Reviewed Count | Int32 | 1 | 210px | right |
| 7 | deviationsReviewedCount | Deviations Reviewed Count | Int32 | 1 | 220px | right |
| 8 | auditTrailReviewed | Audit Trail Reviewed | Boolean | 3 | 180px | center |
| 9 | accessReviewed | Access Reviewed | Boolean | 3 | 150px | center |
| 10 | backupRestoreVerified | Backup Restore Verified | Boolean | 3 | 210px | center |
| 11 | validatedStateConfirmed | Validated State Confirmed | Boolean | 3 | 220px | center |
| 12 | findingsText | Findings Text | String | 93 | 300px | left |
| 13 | reviewedBy | Reviewed By | String | 14 | 120px | left |
| 14 | reviewedAt | Reviewed At | Date/Datetime | 19 | 160px | center |
| 15 | approvedBy | Approved By | String | 11 | 120px | left |
| 16 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 17 | nextReviewDate | Next Review Date | Date/Date | 10 | 160px | center |
| 18 | status | Status | String | 9 | 90px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); computerisedSystemId (reference key, shown through computerisedSystemName); reviewedById (reference key, shown through reviewedBy); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_systemValidation - System Validations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_systemValidation.json | _id: mes_syst_systemValidationStable | rel: CL20261018-23:51 | samples: 10 | columns: 25 | total width: 4670px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | computerisedSystemName | Computerised System | String | 53 | 300px | left |
| 3 | title | Title | String | 82 | 300px | left |
| 4 | validationType | Validation Type | String | 19 | 160px | left |
| 5 | assuranceApproach | Assurance Approach | String | 18 | 170px | left |
| 6 | releaseVersion | Release Version | String | 18 | 150px | left |
| 7 | engineeringChangeName | Engineering Change | String | 61 | 300px | left |
| 8 | riskAssessmentName | Risk Assessment | String | 62 | 300px | left |
| 9 | protocolControlledDocumentName | Protocol Controlled Document | String | 0 | 240px | left |
| 10 | reportControlledDocumentName | Report Controlled Document | String | 0 | 230px | left |
| 11 | testCaseCount | Test Case Count | Int32 | 3 | 150px | right |
| 12 | testFailedCount | Test Failed Count | Int32 | 1 | 160px | right |
| 13 | openDeviationCount | Open Deviation Count | Int32 | 1 | 180px | right |
| 14 | plannedStartDate | Planned Start Date | Date/Date | 10 | 170px | center |
| 15 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 16 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 17 | approvedBy | Approved By | String | 11 | 120px | left |
| 18 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 19 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 20 | conclusionText | Conclusion Text | String | 121 | 300px | left |
| 21 | status | Status | String | 12 | 110px | left |
| 22 | createdBy | Created By | String | 14 | 120px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 14 | 120px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); computerisedSystemId (reference key, shown through computerisedSystemName); engineeringChangeId (reference key, shown through engineeringChangeName); riskAssessmentId (reference key, shown through riskAssessmentName); protocolControlledDocumentId (reference key, shown through protocolControlledDocumentName); reportControlledDocumentId (reference key, shown through reportControlledDocumentName); approvedById (reference key, shown through approvedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): protocolControlledDocumentName, reportControlledDocumentName, electronicSignatureName

## u_mes_syst_unsMessageType - UNS Message Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_unsMessageType.json | _id: mes_syst_unsMessageTypeStable | rel: CL20261019-12:24 | samples: 10 | columns: 15 | total width: 2660px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | name | Name | String | 19 | 160px | left |
| 3 | description | Description | String | 117 | 300px | left |
| 4 | unsNamespace | Uns Namespace | String | 4 | 140px | left |
| 5 | messageTypeCode | Message Type Code | String | 18 | 160px | left |
| 6 | payloadSchemaName | Payload Schema Name | String | 26 | 210px | left |
| 7 | payloadSchemaVersion | Payload Schema Version | Int32 | 1 | 200px | right |
| 8 | messageClass | Message Class | String | 11 | 140px | left |
| 9 | hierarchyLevel | Hierarchy Level | String | 11 | 150px | left |
| 10 | senderType | Sender Type | String | 16 | 140px | left |
| 11 | targetCollectionName | Target Collection Name | String | 27 | 210px | left |
| 12 | twinPropertyPath | Twin Property Path | String | 32 | 250px | left |
| 13 | ingestedByMes | Ingested By Mes | Boolean | 3 | 150px | center |
| 14 | routedToDataLake | Routed to Data Lake | Boolean | 3 | 180px | center |
| 15 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_syst_unsRejectedMessage - UNS Rejected Messages (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_unsRejectedMessage.json | _id: mes_syst_unsRejectedMessageStable | rel: CL20261019-12:24 | samples: 10 | columns: 22 | total width: 4480px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | messageUuid | Message Uuid | String | 36 | 280px | left |
| 3 | iotHubIdentityName | IoT Hub Identity | String | 31 | 240px | left |
| 4 | unsMessageTypeName | Uns Message Type | String | 17 | 160px | left |
| 5 | equipmentName | Equipment | String | 31 | 240px | left |
| 6 | isa95Path | Isa95 Path | String | 35 | 270px | left |
| 7 | payloadSchemaName | Payload Schema Name | String | 28 | 220px | left |
| 8 | messageTimestamp | Message Timestamp | Date/Datetime | 19 | 160px | center |
| 9 | receivedAt | Received At | Date/Datetime | 19 | 160px | center |
| 10 | rejectionReason | Rejection Reason | String | 27 | 210px | left |
| 11 | rejectionDetailText | Rejection Detail Text | String | 150 | 300px | left |
| 12 | payloadText | Payload Text | String | 592 | 300px | left |
| 13 | deadLetterBlobPath | Dead Letter Blob Path | String | 67 | 300px | left |
| 14 | resolvedBy | Resolved By | String | 12 | 120px | left |
| 15 | resolvedAt | Resolved At | Date/Datetime | 19 | 160px | center |
| 16 | resolutionText | Resolution Text | String | 174 | 300px | left |
| 17 | resentMessageUuid | Resent Message Uuid | String | 36 | 280px | left |
| 18 | status | Status | String | 9 | 90px | left |
| 19 | createdBy | Created By | String | 10 | 110px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 12 | 110px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); iotHubIdentityId (reference key, shown through iotHubIdentityName); unsMessageTypeId (reference key, shown through unsMessageTypeName); equipmentId (reference key, shown through equipmentName); resolvedById (reference key, shown through resolvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_userAccessReview - User Access Reviews (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_userAccessReview.json | _id: mes_syst_userAccessReviewStable | rel: CL20261018-23:51 | samples: 10 | columns: 16 | total width: 2630px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | computerisedSystemName | Computerised System | String | 57 | 300px | left |
| 3 | reviewPeriodFromDate | Review Period From Date | Date/Date | 10 | 210px | center |
| 4 | reviewPeriodToDate | Review Period to Date | Date/Date | 10 | 190px | center |
| 5 | usersReviewedCount | Users Reviewed Count | Int32 | 3 | 180px | right |
| 6 | accessRemovedCount | Access Removed Count | Int32 | 1 | 180px | right |
| 7 | accessChangedCount | Access Changed Count | Int32 | 1 | 180px | right |
| 8 | reviewedBy | Reviewed By | String | 14 | 120px | left |
| 9 | reviewedAt | Reviewed At | Date/Datetime | 19 | 160px | center |
| 10 | approvedBy | Approved By | String | 11 | 120px | left |
| 11 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 12 | status | Status | String | 9 | 90px | left |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); computerisedSystemId (reference key, shown through computerisedSystemName); reviewedById (reference key, shown through reviewedBy); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_syst_userAccessReviewLine - User Access Review Lines (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_syst_userAccessReviewLine.json | _id: mes_syst_userAccessReviewLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 2190px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | userAccessReviewName | User Access Review | String | 22 | 180px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | userName | User | String | 14 | 120px | left |
| 5 | roleName | Role | String | 28 | 220px | left |
| 6 | accessStillRequired | Access Still Required | Boolean | 3 | 190px | center |
| 7 | reviewAction | Review Action | String | 12 | 140px | left |
| 8 | actionCompletedAt | Action Completed At | Date/Datetime | 19 | 180px | center |
| 9 | comment | Comment | String | 97 | 300px | left |
| 10 | createdBy | Created By | String | 14 | 120px | left |
| 11 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 12 | updatedBy | Updated By | String | 14 | 120px | left |
| 13 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userAccessReviewId (reference key, shown through userAccessReviewName); userId (reference key, shown through userName); roleId (reference key, shown through roleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
