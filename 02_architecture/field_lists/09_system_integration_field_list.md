# Field list - SystemAndIntegration (syst)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/09_system_integration/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_syst_erpMessage

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 7 | integrationConnectorName | String | - |  |
| 8 | direction | String | - |  |
| 9 | messageType | String | - |  |
| 10 | idempotencyKey | String | - |  |
| 11 | correlationNo | String | - |  |
| 12 | relatedCollectionName | String | - |  |
| 13 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 14 | relatedEntityName | String | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 18 | goodsReceiptName | String | - |  |
| 19 | shipmentId | String | - | u_mes_matl_shipment._id |
| 20 | shipmentName | String | - |  |
| 21 | payload | String | - |  |
| 22 | payloadFormat | String | - |  |
| 23 | payloadHash | String | - |  |
| 24 | attempts | Int32 | - |  |
| 25 | maxAttempts | Int32 | - |  |
| 26 | createdInSourceAt | Date | Datetime |  |
| 27 | receivedAt | Date | Datetime |  |
| 28 | processedAt | Date | Datetime |  |
| 29 | nextRetryAt | Date | Datetime |  |
| 30 | errorCode | String | - |  |
| 31 | errorText | String | - |  |
| 32 | erpDocumentNo | String | - |  |
| 33 | acknowledgedAt | Date | Datetime |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |

## u_mes_syst_integrationConnector

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | connectorType | String | - |  |
| 8 | targetSystem | String | - |  |
| 9 | protocol | String | - |  |
| 10 | endpoint | String | - |  |
| 11 | environment | String | - |  |
| 12 | authMethod | String | - |  |
| 13 | credentialRef | String | - |  |
| 14 | timeoutMs | Int32 | - |  |
| 15 | retryPolicyMaxAttempts | Int32 | - |  |
| 16 | retryPolicyBackoffSec | Int32 | - |  |
| 17 | lastSuccessAt | Date | Datetime |  |
| 18 | lastFailureAt | Date | Datetime |  |
| 19 | healthStatus | String | - |  |
| 20 | ownerUserId | String | - | u_mes_mast_user._id |
| 21 | ownerUserName | String | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_syst_integrationConnectorFunction

Kind: child | Data class: master | Parent: u_mes_syst_integrationConnector | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 7 | integrationConnectorName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | functionName | String | - |  |
| 10 | direction | String | - |  |
| 11 | messageType | String | - |  |
| 12 | endpointPath | String | - |  |
| 13 | scheduleExpression | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_syst_iotDevice

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | deviceTypeId | String | - | u_mes_syst_deviceType._id |
| 8 | deviceTypeName | String | - |  |
| 9 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 10 | manufacturerName | String | - |  |
| 11 | model | String | - |  |
| 12 | serialNo | String | - |  |
| 13 | firmwareVersion | String | - |  |
| 14 | equipmentId | String | - | u_mes_mast_equipment._id |
| 15 | equipmentName | String | - |  |
| 16 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 17 | workCenterName | String | - |  |
| 18 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 19 | integrationConnectorName | String | - |  |
| 20 | ipAddress | String | - |  |
| 21 | macAddress | String | - |  |
| 22 | port | Int32 | - |  |
| 23 | protocol | String | - |  |
| 24 | vlan | Int32 | - |  |
| 25 | opcNodeAddress | String | - |  |
| 26 | pollIntervalMs | Int32 | - |  |
| 27 | lastSeenAt | Date | Datetime |  |
| 28 | connectionStatus | String | - |  |
| 29 | certificateExpiresAt | Date | Date |  |
| 30 | installedAt | Date | Datetime |  |
| 31 | edgeGatewayIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 32 | edgeGatewayIotDeviceName | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorApp

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | appType | String | - |  |
| 8 | version | Int32 | - |  |
| 9 | publishedById | String | - | u_mes_mast_user._id |
| 10 | publishedBy | String | - |  |
| 11 | publishedAt | Date | Datetime |  |
| 12 | approvedById | String | - | u_mes_mast_user._id |
| 13 | approvedBy | String | - |  |
| 14 | approvedAt | Date | Datetime |  |
| 15 | previousVersionOperatorAppId | String | - | u_mes_syst_operatorApp._id |
| 16 | previousVersionOperatorAppName | String | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppOperation

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppStep

Kind: child | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | widgetType | String | - |  |
| 11 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 12 | workInstructionName | String | - |  |
| 13 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 14 | inspectionPlanName | String | - |  |
| 15 | nextStepNo | Int32 | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppStepTrigger

Kind: child | Data class: master | Parent: u_mes_syst_operatorAppStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppStepId | String | - | u_mes_syst_operatorAppStep._id |
| 7 | operatorAppStepName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | triggerEvent | String | - |  |
| 10 | triggerAction | String | - |  |
| 11 | triggerTarget | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppDeviceBinding

Kind: child | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | - |  |
| 11 | purpose | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppLanguage

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 7 | operatorAppName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | languageId | String | - | u_mes_mast_language._id |
| 10 | languageName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_businessEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | eventType | String | - |  |
| 7 | eventCategory | String | - |  |
| 8 | occurredAt | Date | Datetime |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | equipmentId | String | - | u_mes_mast_equipment._id |
| 15 | equipmentName | String | - |  |
| 16 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 17 | productionOrderName | String | - |  |
| 18 | userId | String | - | u_mes_mast_user._id |
| 19 | userName | String | - |  |
| 20 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 21 | iotDeviceName | String | - |  |
| 22 | severity | Int32 | - |  |
| 23 | messageText | String | - |  |
| 24 | eventPayloadText | String | - |  |
| 25 | correlationNo | String | - |  |
| 26 | source | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_syst_auditTrail

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | relatedCollectionName | String | - |  |
| 7 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 8 | relatedEntityName | String | - |  |
| 9 | changeAction | String | - |  |
| 10 | changedAt | Date | Datetime |  |
| 11 | changedById | String | - | u_mes_mast_user._id |
| 12 | changedBy | String | - |  |
| 13 | reasonText | String | - |  |
| 14 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 15 | electronicSignatureName | String | - |  |
| 16 | clientIp | String | - |  |
| 17 | application | String | - |  |
| 18 | documentVersionBefore | Int32 | - |  |
| 19 | documentVersionAfter | Int32 | - |  |
| 20 | previousHash | String | - |  |
| 21 | entryHash | String | - |  |
| 22 | gxpRelevant | Boolean | - |  |
| 23 | auditTrailReviewId | String | - | u_mes_syst_auditTrailReview._id |
| 24 | auditTrailReviewName | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_syst_auditTrailChange

Kind: child | Data class: transaction | Parent: u_mes_syst_auditTrail | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | auditTrailId | String | - | u_mes_syst_auditTrail._id |
| 7 | auditTrailName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | changedFieldName | String | - |  |
| 10 | oldValue | String | - |  |
| 11 | newValue | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_syst_electronicSignature

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | relatedCollectionName | String | - |  |
| 7 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 8 | relatedEntityName | String | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | roleId | String | - | u_mes_mast_role._id |
| 12 | roleName | String | - |  |
| 13 | signatureMeaningId | String | - | u_mes_mast_signatureMeaning._id |
| 14 | signatureMeaningName | String | - |  |
| 15 | signedAt | Date | Datetime |  |
| 16 | authenticationMethod | String | - |  |
| 17 | contentHash | String | - |  |
| 18 | comment | String | - |  |
| 19 | clientIp | String | - |  |
| 20 | workstation | String | - |  |
| 21 | isSecondSignature | Boolean | - |  |
| 22 | witnessUserId | String | - | u_mes_mast_user._id |
| 23 | witnessUserName | String | - |  |
| 24 | signatureManifestationText | String | - |  |
| 25 | signedRecordVersion | Int32 | - |  |
| 26 | isFirstSigningInSession | Boolean | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_syst_notification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 7 | notificationTypeName | String | - |  |
| 8 | severity | Int32 | - |  |
| 9 | title | String | - |  |
| 10 | bodyText | String | - |  |
| 11 | relatedCollectionName | String | - |  |
| 12 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 13 | relatedEntityName | String | - |  |
| 14 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 15 | andonEventName | String | - |  |
| 16 | alarmId | String | - | u_mes_perf_alarm._id |
| 17 | alarmName | String | - |  |
| 18 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 19 | nonconformanceName | String | - |  |
| 20 | escalationLevel | Int32 | - |  |
| 21 | raisedAt | Date | Datetime |  |
| 22 | acknowledgedById | String | - | u_mes_mast_user._id |
| 23 | acknowledgedBy | String | - |  |
| 24 | acknowledgedAt | Date | Datetime |  |
| 25 | expiresAt | Date | Datetime |  |
| 26 | alertRuleId | String | - | u_mes_syst_alertRule._id |
| 27 | alertRuleName | String | - |  |
| 28 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 29 | escalationRuleName | String | - |  |
| 30 | responseDueAt | Date | Datetime |  |
| 31 | resolvedAt | Date | Datetime |  |
| 32 | resolvedById | String | - | u_mes_mast_user._id |
| 33 | resolvedBy | String | - |  |
| 34 | interlockEventId | String | - | u_mes_plan_interlockEvent._id |
| 35 | interlockEventName | String | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_syst_notificationRecipient

Kind: child | Data class: transaction | Parent: u_mes_syst_notification | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | notificationId | String | - | u_mes_syst_notification._id |
| 7 | notificationName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | roleId | String | - | u_mes_mast_role._id |
| 12 | roleName | String | - |  |
| 13 | channel | String | - |  |
| 14 | sentAt | Date | Datetime |  |
| 15 | deliveredAt | Date | Datetime |  |
| 16 | readAt | Date | Datetime |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_syst_controlledDocument

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | documentTypeId | String | - | u_mes_syst_documentType._id |
| 8 | documentTypeName | String | - |  |
| 9 | revision | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | relatedCollectionName | String | - |  |
| 13 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 14 | relatedEntityName | String | - |  |
| 15 | fileName | String | - |  |
| 16 | mimeType | String | - |  |
| 17 | sizeBytes | Int64 | - |  |
| 18 | storageProvider | String | - |  |
| 19 | storageKey | String | - |  |
| 20 | checksumSha256 | String | - |  |
| 21 | languageId | String | - | u_mes_mast_language._id |
| 22 | languageName | String | - |  |
| 23 | authorUserId | String | - | u_mes_mast_user._id |
| 24 | authorUserName | String | - |  |
| 25 | approvedById | String | - | u_mes_mast_user._id |
| 26 | approvedBy | String | - |  |
| 27 | approvedAt | Date | Datetime |  |
| 28 | effectiveFrom | Date | Date |  |
| 29 | expiresAt | Date | Datetime |  |
| 30 | retentionYears | Int32 | - |  |
| 31 | isControlled | Boolean | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_syst_controlledDocumentTag

Kind: valueList | Data class: transaction | Parent: u_mes_syst_controlledDocument | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 7 | controlledDocumentName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | tag | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_syst_numberRange

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | rangeType | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | prefix | String | - |  |
| 11 | formatMask | String | - |  |
| 12 | currentValue | Int64 | - |  |
| 13 | minValue | Int64 | - |  |
| 14 | maxValue | Int64 | - |  |
| 15 | incrementById | String | - | u_mes_mast_user._id |
| 16 | incrementBy | String | - |  |
| 17 | resetPolicy | String | - |  |
| 18 | lastResetAt | Date | Datetime |  |
| 19 | checkDigitMethod | String | - |  |
| 20 | warnAtPct | Decimal128 | - |  |
| 21 | lastIssuedValue | Int64 | - |  |
| 22 | lastIssuedAt | Date | Datetime |  |
| 23 | exampleValue | String | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_syst_systemConfiguration

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | module | String | - |  |
| 7 | description | String | - |  |
| 8 | valueType | String | - |  |
| 9 | configValueText | String | - |  |
| 10 | configValueNumber | Decimal128 | - |  |
| 11 | configValueFlag | Boolean | - |  |
| 12 | configValueJson | String | - |  |
| 13 | scope | String | - |  |
| 14 | isEditable | Boolean | - |  |
| 15 | isSecret | Boolean | - |  |
| 16 | validFrom | Date | Date |  |
| 17 | lastChangedReason | String | - |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_syst_documentType

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
| 8 | retentionYears | Int32 | - |  |
| 9 | isControlled | Boolean | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_syst_deviceType

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

## u_mes_syst_notificationType

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

## u_mes_syst_statusDefinition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | collectionName | String | - |  |
| 7 | fieldName | String | - |  |
| 8 | statusCode | String | - |  |
| 9 | statusName | String | - |  |
| 10 | description | String | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | isInitial | Boolean | - |  |
| 13 | isFinal | Boolean | - |  |
| 14 | colourCode | String | - |  |
| 15 | status | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_syst_enumerationValue

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | collectionName | String | - |  |
| 7 | fieldName | String | - |  |
| 8 | valueCode | String | - |  |
| 9 | valueName | String | - |  |
| 10 | description | String | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | isDefault | Boolean | - |  |
| 13 | status | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_syst_statusTransition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | collectionName | String | - |  |
| 7 | fromStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 8 | fromStatusDefinitionName | String | - |  |
| 9 | toStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 10 | toStatusDefinitionName | String | - |  |
| 11 | transitionName | String | - |  |
| 12 | requiresSignature | Boolean | - |  |
| 13 | requiresReason | Boolean | - |  |
| 14 | sequenceNo | Int32 | - |  |
| 15 | status | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_syst_interlockRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | ruleType | String | - |  |
| 8 | transactionPoint | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | operationId | String | - | u_mes_prod_operation._id |
| 14 | operationName | String | - |  |
| 15 | itemId | String | - | u_mes_prod_item._id |
| 16 | itemName | String | - |  |
| 17 | enforcementMode | String | - |  |
| 18 | overrideAllowed | Boolean | - |  |
| 19 | overrideRoleId | String | - | u_mes_mast_role._id |
| 20 | overrideRoleName | String | - |  |
| 21 | overrideRequiresSignature | Boolean | - |  |
| 22 | overrideRequiresReasonCode | Boolean | - |  |
| 23 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 24 | escalationRuleName | String | - |  |
| 25 | messageText | String | - |  |
| 26 | validFrom | Date | Date |  |
| 27 | validTo | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_syst_statusTransitionRole

Kind: relationship | Data class: master | Parent: u_mes_syst_statusTransition | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | statusTransitionId | String | - | u_mes_syst_statusTransition._id |
| 7 | statusTransitionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | roleId | String | - | u_mes_mast_role._id |
| 10 | roleName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_escalationRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | sourceType | String | - |  |
| 8 | severityClass | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | firstResponderRoleId | String | - | u_mes_mast_role._id |
| 12 | firstResponderRoleName | String | - |  |
| 13 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 14 | requiredSkillName | String | - |  |
| 15 | responseTargetMinutes | Int32 | - |  |
| 16 | resolutionTargetMinutes | Int32 | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_syst_escalationRuleLevel

Kind: child | Data class: master | Parent: u_mes_syst_escalationRule | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 7 | escalationRuleName | String | - |  |
| 8 | level | Int32 | - |  |
| 9 | delayMinutes | Int32 | - |  |
| 10 | basis | String | - |  |
| 11 | roleId | String | - | u_mes_mast_role._id |
| 12 | roleName | String | - |  |
| 13 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 14 | notificationTypeName | String | - |  |
| 15 | channel | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_syst_alertRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | metric | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | equipmentId | String | - | u_mes_mast_equipment._id |
| 13 | equipmentName | String | - |  |
| 14 | processTagId | String | - | u_mes_perf_processTag._id |
| 15 | processTagName | String | - |  |
| 16 | itemId | String | - | u_mes_prod_item._id |
| 17 | itemName | String | - |  |
| 18 | comparison | String | - |  |
| 19 | thresholdValue | Decimal128 | - |  |
| 20 | thresholdUpperValue | Decimal128 | - |  |
| 21 | evaluationWindowMinutes | Int32 | - |  |
| 22 | severityClass | String | - |  |
| 23 | actionType | String | - |  |
| 24 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 25 | notificationTypeName | String | - |  |
| 26 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 27 | escalationRuleName | String | - |  |
| 28 | falseAlertCount | Int32 | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |

## u_mes_syst_analyticsModel

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | modelType | String | - |  |
| 8 | modelVersion | String | - |  |
| 9 | framework | String | - |  |
| 10 | trainingDatasetRef | String | - |  |
| 11 | validationMetricName | String | - |  |
| 12 | validationMetricValue | Decimal128 | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | modelControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 16 | modelControlledDocumentName | String | - |  |
| 17 | effectiveFrom | Date | Date |  |
| 18 | effectiveTo | Date | Date |  |
| 19 | approvedById | String | - | u_mes_mast_user._id |
| 20 | approvedBy | String | - |  |
| 21 | approvedAt | Date | Datetime |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_syst_modelPrediction

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 7 | analyticsModelName | String | - |  |
| 8 | modelVersion | String | - |  |
| 9 | predictionType | String | - |  |
| 10 | relatedCollectionName | String | - |  |
| 11 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 12 | relatedEntityName | String | - |  |
| 13 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 14 | workCenterName | String | - |  |
| 15 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - |  |
| 17 | shiftId | String | - | u_mes_mast_shift._id |
| 18 | shiftName | String | - |  |
| 19 | predictedAt | Date | Datetime |  |
| 20 | horizonMinutes | Int32 | - |  |
| 21 | predictedClass | String | - |  |
| 22 | predictedValue | Decimal128 | - |  |
| 23 | confidence | Decimal128 | - |  |
| 24 | recommendedAction | String | - |  |
| 25 | actionStatus | String | - |  |
| 26 | actionTakenById | String | - | u_mes_mast_user._id |
| 27 | actionTakenBy | String | - |  |
| 28 | actionTakenAt | Date | Datetime |  |
| 29 | actualValue | Decimal128 | - |  |
| 30 | actualClass | String | - |  |
| 31 | notificationId | String | - | u_mes_syst_notification._id |
| 32 | notificationName | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_syst_simulationStudy

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | studyType | String | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | scenarioText | String | - |  |
| 12 | inputSnapshotAt | Date | Datetime |  |
| 13 | resultText | String | - |  |
| 14 | predictedValue | Decimal128 | - |  |
| 15 | predictedKpi | String | - |  |
| 16 | recommendedRecipeId | String | - | u_mes_prod_recipe._id |
| 17 | recommendedRecipeName | String | - |  |
| 18 | rolloutProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 19 | rolloutProductionOrderName | String | - |  |
| 20 | actualValue | Decimal128 | - |  |
| 21 | comparisonResult | String | - |  |
| 22 | resultControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 23 | resultControlledDocumentName | String | - |  |
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

## u_mes_syst_recordPolicy

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | collectionName | String | - |  |
| 7 | editPolicy | String | - |  |
| 8 | lockOnStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 9 | lockOnStatusDefinitionName | String | - |  |
| 10 | requiresReasonForEdit | Boolean | - |  |
| 11 | requiresSignatureForEdit | Boolean | - |  |
| 12 | editRoleId | String | - | u_mes_mast_role._id |
| 13 | editRoleName | String | - |  |
| 14 | deleteAllowed | Boolean | - |  |
| 15 | retentionYears | Int32 | - |  |
| 16 | archiveAfterMonths | Int32 | - |  |
| 17 | gxpRelevant | Boolean | - |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |

## u_mes_syst_savedView

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | viewType | String | - |  |
| 8 | collectionName | String | - |  |
| 9 | filterJson | String | - |  |
| 10 | sortJson | String | - |  |
| 11 | ownerUserId | String | - | u_mes_mast_user._id |
| 12 | ownerUserName | String | - |  |
| 13 | roleId | String | - | u_mes_mast_role._id |
| 14 | roleName | String | - |  |
| 15 | isShared | Boolean | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_syst_backupRun

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | runType | String | - |  |
| 7 | startedAt | Date | Datetime |  |
| 8 | completedAt | Date | Datetime |  |
| 9 | sizeBytes | Int64 | - |  |
| 10 | storageTarget | String | - |  |
| 11 | recoveryTimeMinutes | Int32 | - |  |
| 12 | recoveryPointMinutes | Int32 | - |  |
| 13 | evidenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 14 | evidenceControlledDocumentName | String | - |  |
| 15 | performedById | String | - | u_mes_mast_user._id |
| 16 | performedBy | String | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_syst_computerisedSystem

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
| 8 | systemCategory | String | - |  |
| 9 | gampCategory | String | - |  |
| 10 | gxpImpact | String | - |  |
| 11 | dataCriticality | String | - |  |
| 12 | holdsElectronicRecords | Boolean | - |  |
| 13 | usesElectronicSignatures | Boolean | - |  |
| 14 | systemOwnerUserId | String | - | u_mes_mast_user._id |
| 15 | systemOwnerUserName | String | - |  |
| 16 | processOwnerUserId | String | - | u_mes_mast_user._id |
| 17 | processOwnerUserName | String | - |  |
| 18 | supplierId | String | - | u_mes_mast_supplier._id |
| 19 | supplierName | String | - |  |
| 20 | equipmentId | String | - | u_mes_mast_equipment._id |
| 21 | equipmentName | String | - |  |
| 22 | softwareVersion | String | - |  |
| 23 | hostingModel | String | - |  |
| 24 | lastValidatedDate | Date | Date |  |
| 25 | periodicReviewIntervalMonths | Int32 | - |  |
| 26 | nextPeriodicReviewDate | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_syst_systemValidation

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | computerisedSystemId | String | - | u_mes_syst_computerisedSystem._id |
| 7 | computerisedSystemName | String | - |  |
| 8 | title | String | - |  |
| 9 | validationType | String | - |  |
| 10 | assuranceApproach | String | - |  |
| 11 | releaseVersion | String | - |  |
| 12 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 13 | engineeringChangeName | String | - |  |
| 14 | riskAssessmentId | String | - | u_mes_qual_riskAssessment._id |
| 15 | riskAssessmentName | String | - |  |
| 16 | protocolControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 17 | protocolControlledDocumentName | String | - |  |
| 18 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 19 | reportControlledDocumentName | String | - |  |
| 20 | testCaseCount | Int32 | - |  |
| 21 | testFailedCount | Int32 | - |  |
| 22 | openDeviationCount | Int32 | - |  |
| 23 | plannedStartDate | Date | Date |  |
| 24 | startedAt | Date | Datetime |  |
| 25 | completedAt | Date | Datetime |  |
| 26 | approvedById | String | - | u_mes_mast_user._id |
| 27 | approvedBy | String | - |  |
| 28 | approvedAt | Date | Datetime |  |
| 29 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 30 | electronicSignatureName | String | - |  |
| 31 | conclusionText | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_syst_systemPeriodicReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | computerisedSystemId | String | - | u_mes_syst_computerisedSystem._id |
| 7 | computerisedSystemName | String | - |  |
| 8 | reviewPeriodFromDate | Date | Date |  |
| 9 | reviewPeriodToDate | Date | Date |  |
| 10 | changesReviewedCount | Int32 | - |  |
| 11 | incidentsReviewedCount | Int32 | - |  |
| 12 | deviationsReviewedCount | Int32 | - |  |
| 13 | auditTrailReviewed | Boolean | - |  |
| 14 | accessReviewed | Boolean | - |  |
| 15 | backupRestoreVerified | Boolean | - |  |
| 16 | validatedStateConfirmed | Boolean | - |  |
| 17 | findingsText | String | - |  |
| 18 | reviewedById | String | - | u_mes_mast_user._id |
| 19 | reviewedBy | String | - |  |
| 20 | reviewedAt | Date | Datetime |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | nextReviewDate | Date | Date |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |
| 27 | createdAt | Date | Datetime |  |
| 28 | createdById | String | - | u_mes_mast_user._id |
| 29 | createdBy | String | - |  |
| 30 | updatedAt | Date | Datetime |  |
| 31 | updatedById | String | - | u_mes_mast_user._id |
| 32 | updatedBy | String | - |  |

## u_mes_syst_auditTrailReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | reviewType | String | - |  |
| 7 | computerisedSystemId | String | - | u_mes_syst_computerisedSystem._id |
| 8 | computerisedSystemName | String | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | reviewFromAt | Date | Datetime |  |
| 13 | reviewToAt | Date | Datetime |  |
| 14 | entriesReviewedCount | Int32 | - |  |
| 15 | criticalEntriesCount | Int32 | - |  |
| 16 | anomalyCount | Int32 | - |  |
| 17 | findingsText | String | - |  |
| 18 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 19 | nonconformanceName | String | - |  |
| 20 | reviewedById | String | - | u_mes_mast_user._id |
| 21 | reviewedBy | String | - |  |
| 22 | reviewedAt | Date | Datetime |  |
| 23 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 24 | electronicSignatureName | String | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |
| 27 | createdAt | Date | Datetime |  |
| 28 | createdById | String | - | u_mes_mast_user._id |
| 29 | createdBy | String | - |  |
| 30 | updatedAt | Date | Datetime |  |
| 31 | updatedById | String | - | u_mes_mast_user._id |
| 32 | updatedBy | String | - |  |

## u_mes_syst_userAccessReview

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | computerisedSystemId | String | - | u_mes_syst_computerisedSystem._id |
| 7 | computerisedSystemName | String | - |  |
| 8 | reviewPeriodFromDate | Date | Date |  |
| 9 | reviewPeriodToDate | Date | Date |  |
| 10 | usersReviewedCount | Int32 | - |  |
| 11 | accessRemovedCount | Int32 | - |  |
| 12 | accessChangedCount | Int32 | - |  |
| 13 | reviewedById | String | - | u_mes_mast_user._id |
| 14 | reviewedBy | String | - |  |
| 15 | reviewedAt | Date | Datetime |  |
| 16 | approvedById | String | - | u_mes_mast_user._id |
| 17 | approvedBy | String | - |  |
| 18 | approvedAt | Date | Datetime |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_syst_userAccessReviewLine

Kind: child | Data class: transaction | Parent: u_mes_syst_userAccessReview | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userAccessReviewId | String | - | u_mes_syst_userAccessReview._id |
| 7 | userAccessReviewName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | roleId | String | - | u_mes_mast_role._id |
| 12 | roleName | String | - |  |
| 13 | accessStillRequired | Boolean | - |  |
| 14 | reviewAction | String | - |  |
| 15 | actionCompletedAt | Date | Datetime |  |
| 16 | comment | String | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_syst_unsMessageType

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
| 8 | unsNamespace | String | - |  |
| 9 | messageTypeCode | String | - |  |
| 10 | payloadSchemaName | String | - |  |
| 11 | payloadSchemaVersion | Int32 | - |  |
| 12 | messageClass | String | - |  |
| 13 | hierarchyLevel | String | - |  |
| 14 | senderType | String | - |  |
| 15 | targetCollectionName | String | - |  |
| 16 | twinPropertyPath | String | - |  |
| 17 | ingestedByMes | Boolean | - |  |
| 18 | routedToDataLake | Boolean | - |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_syst_iotHubIdentity

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | identityType | String | - |  |
| 8 | iotHubName | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 12 | iotDeviceName | String | - |  |
| 13 | parentIotHubIdentityId | String | - | u_mes_syst_iotHubIdentity._id |
| 14 | parentIotHubIdentityName | String | - |  |
| 15 | authenticationMethod | String | - |  |
| 16 | certificateThumbprint | String | - |  |
| 17 | certificateExpiresAt | Date | Date |  |
| 18 | provisioningStatus | String | - |  |
| 19 | lastRegistrySyncAt | Date | Datetime |  |
| 20 | twinTagsVersion | Int32 | - |  |
| 21 | lastSyncErrorText | String | - |  |
| 22 | connectionState | String | - |  |
| 23 | connectionStateAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_syst_unsRejectedMessage

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | messageUuid | String | - |  |
| 7 | iotHubIdentityId | String | - | u_mes_syst_iotHubIdentity._id |
| 8 | iotHubIdentityName | String | - |  |
| 9 | unsMessageTypeId | String | - | u_mes_syst_unsMessageType._id |
| 10 | unsMessageTypeName | String | - |  |
| 11 | equipmentId | String | - | u_mes_mast_equipment._id |
| 12 | equipmentName | String | - |  |
| 13 | isa95Path | String | - |  |
| 14 | payloadSchemaName | String | - |  |
| 15 | messageTimestamp | Date | Datetime |  |
| 16 | receivedAt | Date | Datetime |  |
| 17 | rejectionReason | String | - |  |
| 18 | rejectionDetailText | String | - |  |
| 19 | payloadText | String | - |  |
| 20 | deadLetterBlobPath | String | - |  |
| 21 | resolvedById | String | - | u_mes_mast_user._id |
| 22 | resolvedBy | String | - |  |
| 23 | resolvedAt | Date | Datetime |  |
| 24 | resolutionText | String | - |  |
| 25 | resentMessageUuid | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |
