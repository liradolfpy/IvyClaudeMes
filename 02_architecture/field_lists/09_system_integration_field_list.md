# Field list - System and Integration (syst)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/09_system_integration/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_syst_erpMessage

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 6 | integrationConnectorName | String | - |  |
| 7 | direction | String | - |  |
| 8 | messageType | String | - |  |
| 9 | idempotencyKey | String | - |  |
| 10 | correlationNo | String | - |  |
| 11 | relatedCollectionName | String | - |  |
| 12 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 13 | relatedEntityName | String | - |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 17 | goodsReceiptName | String | - |  |
| 18 | shipmentId | String | - | u_mes_matl_shipment._id |
| 19 | shipmentName | String | - |  |
| 20 | payload | String | - |  |
| 21 | payloadFormat | String | - |  |
| 22 | payloadHash | String | - |  |
| 23 | attempts | Int32 | - |  |
| 24 | maxAttempts | Int32 | - |  |
| 25 | createdInSourceAt | Date | Datetime |  |
| 26 | receivedAt | Date | Datetime |  |
| 27 | processedAt | Date | Datetime |  |
| 28 | nextRetryAt | Date | Datetime |  |
| 29 | errorCode | String | - |  |
| 30 | errorText | String | - |  |
| 31 | erpDocumentNo | String | - |  |
| 32 | acknowledgedAt | Date | Datetime |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_syst_integrationConnector

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | connectorType | String | - |  |
| 7 | targetSystem | String | - |  |
| 8 | protocol | String | - |  |
| 9 | endpoint | String | - |  |
| 10 | environment | String | - |  |
| 11 | authMethod | String | - |  |
| 12 | credentialRef | String | - |  |
| 13 | timeoutMs | Int32 | - |  |
| 14 | retryPolicyMaxAttempts | Int32 | - |  |
| 15 | retryPolicyBackoffSec | Int32 | - |  |
| 16 | lastSuccessAt | Date | Datetime |  |
| 17 | lastFailureAt | Date | Datetime |  |
| 18 | healthStatus | String | - |  |
| 19 | ownerUserId | String | - | u_mes_mast_user._id |
| 20 | ownerUserName | String | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_syst_integrationConnectorFunction

Kind: child | Data class: master | Parent: u_mes_syst_integrationConnector | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 6 | integrationConnectorName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | functionName | String | - |  |
| 9 | direction | String | - |  |
| 10 | messageType | String | - |  |
| 11 | endpointPath | String | - |  |
| 12 | scheduleExpression | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_syst_iotDevice

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | deviceTypeId | String | - | u_mes_syst_deviceType._id |
| 7 | deviceTypeName | String | - |  |
| 8 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | - |  |
| 10 | model | String | - |  |
| 11 | serialNo | String | - |  |
| 12 | firmwareVersion | String | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 16 | workCenterName | String | - |  |
| 17 | integrationConnectorId | String | - | u_mes_syst_integrationConnector._id |
| 18 | integrationConnectorName | String | - |  |
| 19 | ipAddress | String | - |  |
| 20 | macAddress | String | - |  |
| 21 | port | Int32 | - |  |
| 22 | protocol | String | - |  |
| 23 | vlan | Int32 | - |  |
| 24 | opcNodeAddress | String | - |  |
| 25 | pollIntervalMs | Int32 | - |  |
| 26 | lastSeenAt | Date | Datetime |  |
| 27 | connectionStatus | String | - |  |
| 28 | certificateExpiresAt | Date | Date |  |
| 29 | installedAt | Date | Datetime |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorApp

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | appType | String | - |  |
| 7 | version | Int32 | - |  |
| 8 | publishedById | String | - | u_mes_mast_user._id |
| 9 | publishedBy | String | - |  |
| 10 | publishedAt | Date | Datetime |  |
| 11 | approvedById | String | - | u_mes_mast_user._id |
| 12 | approvedBy | String | - |  |
| 13 | approvedAt | Date | Datetime |  |
| 14 | previousVersionOperatorAppId | String | - | u_mes_syst_operatorApp._id |
| 15 | previousVersionOperatorAppName | String | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppOperation

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppStep

Kind: child | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | widgetType | String | - |  |
| 10 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 11 | workInstructionName | String | - |  |
| 12 | inspectionPlanId | String | - | u_mes_qual_inspectionPlan._id |
| 13 | inspectionPlanName | String | - |  |
| 14 | nextStepNo | Int32 | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppStepTrigger

Kind: child | Data class: master | Parent: u_mes_syst_operatorAppStep | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppStepId | String | - | u_mes_syst_operatorAppStep._id |
| 6 | operatorAppStepName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | triggerEvent | String | - |  |
| 9 | triggerAction | String | - |  |
| 10 | triggerTarget | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppDeviceBinding

Kind: child | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 9 | iotDeviceName | String | - |  |
| 10 | purpose | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_operatorAppLanguage

Kind: relationship | Data class: master | Parent: u_mes_syst_operatorApp | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | operatorAppId | String | - | u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | languageId | String | - | u_mes_mast_language._id |
| 9 | languageName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_syst_businessEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | eventType | String | - |  |
| 6 | eventCategory | String | - |  |
| 7 | occurredAt | Date | Datetime |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | userId | String | - | u_mes_mast_user._id |
| 18 | userName | String | - |  |
| 19 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 20 | iotDeviceName | String | - |  |
| 21 | severity | Int32 | - |  |
| 22 | messageText | String | - |  |
| 23 | eventPayloadText | String | - |  |
| 24 | correlationNo | String | - |  |
| 25 | source | String | - |  |
| 26 | schemaVersion | Int32 | - |  |
| 27 | createdAt | Date | Datetime |  |
| 28 | createdById | String | - | u_mes_mast_user._id |
| 29 | createdBy | String | - |  |
| 30 | updatedAt | Date | Datetime |  |
| 31 | updatedById | String | - | u_mes_mast_user._id |
| 32 | updatedBy | String | - |  |

## u_mes_syst_auditTrail

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | relatedCollectionName | String | - |  |
| 6 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 7 | relatedEntityName | String | - |  |
| 8 | changeAction | String | - |  |
| 9 | changedAt | Date | Datetime |  |
| 10 | changedById | String | - | u_mes_mast_user._id |
| 11 | changedBy | String | - |  |
| 12 | reasonText | String | - |  |
| 13 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 14 | electronicSignatureName | String | - |  |
| 15 | clientIp | String | - |  |
| 16 | application | String | - |  |
| 17 | documentVersionBefore | Int32 | - |  |
| 18 | documentVersionAfter | Int32 | - |  |
| 19 | previousHash | String | - |  |
| 20 | entryHash | String | - |  |
| 21 | schemaVersion | Int32 | - |  |
| 22 | createdAt | Date | Datetime |  |
| 23 | createdById | String | - | u_mes_mast_user._id |
| 24 | createdBy | String | - |  |
| 25 | updatedAt | Date | Datetime |  |
| 26 | updatedById | String | - | u_mes_mast_user._id |
| 27 | updatedBy | String | - |  |

## u_mes_syst_auditTrailChange

Kind: child | Data class: transaction | Parent: u_mes_syst_auditTrail | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | auditTrailId | String | - | u_mes_syst_auditTrail._id |
| 6 | auditTrailName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | changedFieldName | String | - |  |
| 9 | oldValue | String | - |  |
| 10 | newValue | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_syst_electronicSignature

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | relatedCollectionName | String | - |  |
| 6 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 7 | relatedEntityName | String | - |  |
| 8 | userId | String | - | u_mes_mast_user._id |
| 9 | userName | String | - |  |
| 10 | roleId | String | - | u_mes_mast_role._id |
| 11 | roleName | String | - |  |
| 12 | signatureMeaningId | String | - | u_mes_mast_signatureMeaning._id |
| 13 | signatureMeaningName | String | - |  |
| 14 | signedAt | Date | Datetime |  |
| 15 | authenticationMethod | String | - |  |
| 16 | contentHash | String | - |  |
| 17 | comment | String | - |  |
| 18 | clientIp | String | - |  |
| 19 | workstation | String | - |  |
| 20 | isSecondSignature | Boolean | - |  |
| 21 | witnessUserId | String | - | u_mes_mast_user._id |
| 22 | witnessUserName | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_syst_notification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 6 | notificationTypeName | String | - |  |
| 7 | severity | Int32 | - |  |
| 8 | title | String | - |  |
| 9 | bodyText | String | - |  |
| 10 | relatedCollectionName | String | - |  |
| 11 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 12 | relatedEntityName | String | - |  |
| 13 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 14 | andonEventName | String | - |  |
| 15 | alarmId | String | - | u_mes_perf_alarm._id |
| 16 | alarmName | String | - |  |
| 17 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 18 | nonconformanceName | String | - |  |
| 19 | escalationLevel | Int32 | - |  |
| 20 | raisedAt | Date | Datetime |  |
| 21 | acknowledgedById | String | - | u_mes_mast_user._id |
| 22 | acknowledgedBy | String | - |  |
| 23 | acknowledgedAt | Date | Datetime |  |
| 24 | expiresAt | Date | Datetime |  |
| 25 | alertRuleId | String | - | u_mes_syst_alertRule._id |
| 26 | alertRuleName | String | - |  |
| 27 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 28 | escalationRuleName | String | - |  |
| 29 | responseDueAt | Date | Datetime |  |
| 30 | resolvedAt | Date | Datetime |  |
| 31 | resolvedById | String | - | u_mes_mast_user._id |
| 32 | resolvedBy | String | - |  |
| 33 | interlockEventId | String | - | u_mes_plan_interlockEvent._id |
| 34 | interlockEventName | String | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_syst_notificationRecipient

Kind: child | Data class: transaction | Parent: u_mes_syst_notification | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | notificationId | String | - | u_mes_syst_notification._id |
| 6 | notificationName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | userId | String | - | u_mes_mast_user._id |
| 9 | userName | String | - |  |
| 10 | roleId | String | - | u_mes_mast_role._id |
| 11 | roleName | String | - |  |
| 12 | channel | String | - |  |
| 13 | sentAt | Date | Datetime |  |
| 14 | deliveredAt | Date | Datetime |  |
| 15 | readAt | Date | Datetime |  |
| 16 | schemaVersion | Int32 | - |  |
| 17 | createdAt | Date | Datetime |  |
| 18 | createdById | String | - | u_mes_mast_user._id |
| 19 | createdBy | String | - |  |
| 20 | updatedAt | Date | Datetime |  |
| 21 | updatedById | String | - | u_mes_mast_user._id |
| 22 | updatedBy | String | - |  |

## u_mes_syst_controlledDocument

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | documentTypeId | String | - | u_mes_syst_documentType._id |
| 7 | documentTypeName | String | - |  |
| 8 | revision | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | relatedCollectionName | String | - |  |
| 12 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 13 | relatedEntityName | String | - |  |
| 14 | fileName | String | - |  |
| 15 | mimeType | String | - |  |
| 16 | sizeBytes | Int64 | - |  |
| 17 | storageProvider | String | - |  |
| 18 | storageKey | String | - |  |
| 19 | checksumSha256 | String | - |  |
| 20 | languageId | String | - | u_mes_mast_language._id |
| 21 | languageName | String | - |  |
| 22 | authorUserId | String | - | u_mes_mast_user._id |
| 23 | authorUserName | String | - |  |
| 24 | approvedById | String | - | u_mes_mast_user._id |
| 25 | approvedBy | String | - |  |
| 26 | approvedAt | Date | Datetime |  |
| 27 | effectiveFrom | Date | Date |  |
| 28 | expiresAt | Date | Datetime |  |
| 29 | retentionYears | Int32 | - |  |
| 30 | isControlled | Boolean | - |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_syst_controlledDocumentTag

Kind: valueList | Data class: transaction | Parent: u_mes_syst_controlledDocument | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | controlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 6 | controlledDocumentName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | tag | String | - |  |
| 9 | schemaVersion | Int32 | - |  |
| 10 | createdAt | Date | Datetime |  |
| 11 | createdById | String | - | u_mes_mast_user._id |
| 12 | createdBy | String | - |  |
| 13 | updatedAt | Date | Datetime |  |
| 14 | updatedById | String | - | u_mes_mast_user._id |
| 15 | updatedBy | String | - |  |

## u_mes_syst_numberRange

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | rangeType | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | prefix | String | - |  |
| 10 | formatMask | String | - |  |
| 11 | currentValue | Int64 | - |  |
| 12 | minValue | Int64 | - |  |
| 13 | maxValue | Int64 | - |  |
| 14 | incrementById | String | - | u_mes_mast_user._id |
| 15 | incrementBy | String | - |  |
| 16 | resetPolicy | String | - |  |
| 17 | lastResetAt | Date | Datetime |  |
| 18 | checkDigitMethod | String | - |  |
| 19 | warnAtPct | Decimal128 | - |  |
| 20 | lastIssuedValue | Int64 | - |  |
| 21 | lastIssuedAt | Date | Datetime |  |
| 22 | exampleValue | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_syst_systemConfiguration

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | module | String | - |  |
| 6 | description | String | - |  |
| 7 | valueType | String | - |  |
| 8 | configValueText | String | - |  |
| 9 | configValueNumber | Decimal128 | - |  |
| 10 | configValueFlag | Boolean | - |  |
| 11 | configValueJson | String | - |  |
| 12 | scope | String | - |  |
| 13 | isEditable | Boolean | - |  |
| 14 | isSecret | Boolean | - |  |
| 15 | validFrom | Date | Date |  |
| 16 | lastChangedReason | String | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_syst_documentType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | retentionYears | Int32 | - |  |
| 8 | isControlled | Boolean | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_syst_deviceType

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

## u_mes_syst_notificationType

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

## u_mes_syst_statusDefinition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | collectionName | String | - |  |
| 6 | fieldName | String | - |  |
| 7 | statusCode | String | - |  |
| 8 | statusName | String | - |  |
| 9 | description | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | isInitial | Boolean | - |  |
| 12 | isFinal | Boolean | - |  |
| 13 | colourCode | String | - |  |
| 14 | status | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_syst_enumerationValue

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | collectionName | String | - |  |
| 6 | fieldName | String | - |  |
| 7 | valueCode | String | - |  |
| 8 | valueName | String | - |  |
| 9 | description | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | isDefault | Boolean | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_syst_statusTransition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | collectionName | String | - |  |
| 6 | fromStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 7 | fromStatusDefinitionName | String | - |  |
| 8 | toStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 9 | toStatusDefinitionName | String | - |  |
| 10 | transitionName | String | - |  |
| 11 | requiresSignature | Boolean | - |  |
| 12 | requiresReason | Boolean | - |  |
| 13 | sequenceNo | Int32 | - |  |
| 14 | status | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_syst_interlockRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | ruleType | String | - |  |
| 7 | transactionPoint | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | operationId | String | - | u_mes_prod_operation._id |
| 13 | operationName | String | - |  |
| 14 | itemId | String | - | u_mes_prod_item._id |
| 15 | itemName | String | - |  |
| 16 | enforcementMode | String | - |  |
| 17 | overrideAllowed | Boolean | - |  |
| 18 | overrideRoleId | String | - | u_mes_mast_role._id |
| 19 | overrideRoleName | String | - |  |
| 20 | overrideRequiresSignature | Boolean | - |  |
| 21 | overrideRequiresReasonCode | Boolean | - |  |
| 22 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 23 | escalationRuleName | String | - |  |
| 24 | messageText | String | - |  |
| 25 | validFrom | Date | Date |  |
| 26 | validTo | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |

## u_mes_syst_statusTransitionRole

Kind: relationship | Data class: master | Parent: u_mes_syst_statusTransition | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | statusTransitionId | String | - | u_mes_syst_statusTransition._id |
| 6 | statusTransitionName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | roleId | String | - | u_mes_mast_role._id |
| 9 | roleName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_syst_escalationRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | sourceType | String | - |  |
| 7 | severityClass | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | firstResponderRoleId | String | - | u_mes_mast_role._id |
| 11 | firstResponderRoleName | String | - |  |
| 12 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 13 | requiredSkillName | String | - |  |
| 14 | responseTargetMinutes | Int32 | - |  |
| 15 | resolutionTargetMinutes | Int32 | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_syst_escalationRuleLevel

Kind: child | Data class: master | Parent: u_mes_syst_escalationRule | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 6 | escalationRuleName | String | - |  |
| 7 | level | Int32 | - |  |
| 8 | delayMinutes | Int32 | - |  |
| 9 | basis | String | - |  |
| 10 | roleId | String | - | u_mes_mast_role._id |
| 11 | roleName | String | - |  |
| 12 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 13 | notificationTypeName | String | - |  |
| 14 | channel | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_syst_alertRule

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | metric | String | - |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | equipmentId | String | - | u_mes_mast_equipment._id |
| 12 | equipmentName | String | - |  |
| 13 | processTagId | String | - | u_mes_perf_processTag._id |
| 14 | processTagName | String | - |  |
| 15 | itemId | String | - | u_mes_prod_item._id |
| 16 | itemName | String | - |  |
| 17 | comparison | String | - |  |
| 18 | thresholdValue | Decimal128 | - |  |
| 19 | thresholdUpperValue | Decimal128 | - |  |
| 20 | evaluationWindowMinutes | Int32 | - |  |
| 21 | severityClass | String | - |  |
| 22 | actionType | String | - |  |
| 23 | notificationTypeId | String | - | u_mes_syst_notificationType._id |
| 24 | notificationTypeName | String | - |  |
| 25 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 26 | escalationRuleName | String | - |  |
| 27 | falseAlertCount | Int32 | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |

## u_mes_syst_analyticsModel

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | modelType | String | - |  |
| 7 | modelVersion | String | - |  |
| 8 | framework | String | - |  |
| 9 | trainingDatasetRef | String | - |  |
| 10 | validationMetricName | String | - |  |
| 11 | validationMetricValue | Decimal128 | - |  |
| 12 | equipmentId | String | - | u_mes_mast_equipment._id |
| 13 | equipmentName | String | - |  |
| 14 | modelControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 15 | modelControlledDocumentName | String | - |  |
| 16 | effectiveFrom | Date | Date |  |
| 17 | effectiveTo | Date | Date |  |
| 18 | approvedById | String | - | u_mes_mast_user._id |
| 19 | approvedBy | String | - |  |
| 20 | approvedAt | Date | Datetime |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_syst_modelPrediction

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | analyticsModelId | String | - | u_mes_syst_analyticsModel._id |
| 6 | analyticsModelName | String | - |  |
| 7 | modelVersion | String | - |  |
| 8 | predictionType | String | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 15 | productVariantName | String | - |  |
| 16 | shiftId | String | - | u_mes_mast_shift._id |
| 17 | shiftName | String | - |  |
| 18 | predictedAt | Date | Datetime |  |
| 19 | horizonMinutes | Int32 | - |  |
| 20 | predictedClass | String | - |  |
| 21 | predictedValue | Decimal128 | - |  |
| 22 | confidence | Decimal128 | - |  |
| 23 | recommendedAction | String | - |  |
| 24 | actionStatus | String | - |  |
| 25 | actionTakenById | String | - | u_mes_mast_user._id |
| 26 | actionTakenBy | String | - |  |
| 27 | actionTakenAt | Date | Datetime |  |
| 28 | actualValue | Decimal128 | - |  |
| 29 | actualClass | String | - |  |
| 30 | notificationId | String | - | u_mes_syst_notification._id |
| 31 | notificationName | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_syst_simulationStudy

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | studyType | String | - |  |
| 7 | relatedCollectionName | String | - |  |
| 8 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 9 | relatedEntityName | String | - |  |
| 10 | scenarioText | String | - |  |
| 11 | inputSnapshotAt | Date | Datetime |  |
| 12 | resultText | String | - |  |
| 13 | predictedValue | Decimal128 | - |  |
| 14 | predictedKpi | String | - |  |
| 15 | recommendedRecipeId | String | - | u_mes_prod_recipe._id |
| 16 | recommendedRecipeName | String | - |  |
| 17 | rolloutProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 18 | rolloutProductionOrderName | String | - |  |
| 19 | actualValue | Decimal128 | - |  |
| 20 | comparisonResult | String | - |  |
| 21 | resultControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 22 | resultControlledDocumentName | String | - |  |
| 23 | approvedById | String | - | u_mes_mast_user._id |
| 24 | approvedBy | String | - |  |
| 25 | approvedAt | Date | Datetime |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_syst_recordPolicy

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | collectionName | String | - |  |
| 6 | editPolicy | String | - |  |
| 7 | lockOnStatusDefinitionId | String | - | u_mes_syst_statusDefinition._id |
| 8 | lockOnStatusDefinitionName | String | - |  |
| 9 | requiresReasonForEdit | Boolean | - |  |
| 10 | requiresSignatureForEdit | Boolean | - |  |
| 11 | editRoleId | String | - | u_mes_mast_role._id |
| 12 | editRoleName | String | - |  |
| 13 | deleteAllowed | Boolean | - |  |
| 14 | retentionYears | Int32 | - |  |
| 15 | archiveAfterMonths | Int32 | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_syst_savedView

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | viewType | String | - |  |
| 7 | collectionName | String | - |  |
| 8 | filterJson | String | - |  |
| 9 | sortJson | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | roleId | String | - | u_mes_mast_role._id |
| 13 | roleName | String | - |  |
| 14 | isShared | Boolean | - |  |
| 15 | status | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_syst_backupRun

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | runType | String | - |  |
| 6 | startedAt | Date | Datetime |  |
| 7 | completedAt | Date | Datetime |  |
| 8 | sizeBytes | Int64 | - |  |
| 9 | storageTarget | String | - |  |
| 10 | recoveryTimeMinutes | Int32 | - |  |
| 11 | recoveryPointMinutes | Int32 | - |  |
| 12 | evidenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 13 | evidenceControlledDocumentName | String | - |  |
| 14 | performedById | String | - | u_mes_mast_user._id |
| 15 | performedBy | String | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |
