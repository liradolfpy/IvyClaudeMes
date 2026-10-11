# Field list - Integration and system (sys)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/09_integration_system/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_sys_erpMessage

Kind: entity | Data class: transaction | Parent: - | _id pattern: MSG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | integrationConnectorId | String | u_mes_sys_integrationConnector._id |
| 6 | integrationConnectorName | String |  |
| 7 | direction | String |  |
| 8 | messageType | String |  |
| 9 | idempotencyKey | String |  |
| 10 | correlationNo | String |  |
| 11 | relatedCollectionName | String |  |
| 12 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 13 | relatedEntityName | String |  |
| 14 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | goodsReceiptId | String | u_mes_mat_goodsReceipt._id |
| 17 | goodsReceiptName | String |  |
| 18 | shipmentId | String | u_mes_mat_shipment._id |
| 19 | shipmentName | String |  |
| 20 | payload | String |  |
| 21 | payloadFormat | String |  |
| 22 | payloadHash | String |  |
| 23 | attempts | Int32 |  |
| 24 | maxAttempts | Int32 |  |
| 25 | createdInSourceAt | Date |  |
| 26 | receivedAt | Date |  |
| 27 | processedAt | Date |  |
| 28 | nextRetryAt | Date |  |
| 29 | errorCode | String |  |
| 30 | errorText | String |  |
| 31 | erpDocumentNo | String |  |
| 32 | acknowledgedAt | Date |  |
| 33 | status | String |  |
| 34 | schemaVersion | Int32 |  |
| 35 | createdAt | Date |  |
| 36 | createdById | String | u_mes_mdm_user._id |
| 37 | createdBy | String |  |
| 38 | updatedAt | Date |  |
| 39 | updatedById | String | u_mes_mdm_user._id |
| 40 | updatedBy | String |  |

## u_mes_sys_integrationConnector

Kind: entity | Data class: master | Parent: - | _id pattern: ICN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | connectorType | String |  |
| 7 | targetSystem | String |  |
| 8 | protocol | String |  |
| 9 | endpoint | String |  |
| 10 | environment | String |  |
| 11 | authMethod | String |  |
| 12 | credentialRef | String |  |
| 13 | timeoutMs | Int32 |  |
| 14 | retryPolicyMaxAttempts | Int32 |  |
| 15 | retryPolicyBackoffSec | Int32 |  |
| 16 | lastSuccessAt | Date |  |
| 17 | lastFailureAt | Date |  |
| 18 | healthStatus | String |  |
| 19 | ownerUserId | String | u_mes_mdm_user._id |
| 20 | ownerUserName | String |  |
| 21 | status | String |  |
| 22 | schemaVersion | Int32 |  |

## u_mes_sys_integrationConnectorFunction

Kind: child | Data class: master | Parent: u_mes_sys_integrationConnector | _id pattern: <integrationConnectorId>-F<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | integrationConnectorId | String | u_mes_sys_integrationConnector._id |
| 6 | integrationConnectorName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | functionName | String |  |
| 9 | direction | String |  |
| 10 | messageType | String |  |
| 11 | endpointPath | String |  |
| 12 | scheduleExpression | String |  |
| 13 | schemaVersion | Int32 |  |

## u_mes_sys_iotDevice

Kind: entity | Data class: master | Parent: - | _id pattern: IOT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | deviceType | String |  |
| 7 | manufacturer | String |  |
| 8 | model | String |  |
| 9 | serialNo | String |  |
| 10 | firmwareVersion | String |  |
| 11 | equipmentId | String | u_mes_mdm_equipment._id |
| 12 | equipmentName | String |  |
| 13 | workCenterId | String | u_mes_mdm_workCenter._id |
| 14 | workCenterName | String |  |
| 15 | integrationConnectorId | String | u_mes_sys_integrationConnector._id |
| 16 | integrationConnectorName | String |  |
| 17 | ipAddress | String |  |
| 18 | macAddress | String |  |
| 19 | port | Int32 |  |
| 20 | protocol | String |  |
| 21 | vlan | Int32 |  |
| 22 | opcNodeAddress | String |  |
| 23 | pollIntervalMs | Int32 |  |
| 24 | lastSeenAt | Date |  |
| 25 | connectionStatus | String |  |
| 26 | certificateExpiresAt | Date |  |
| 27 | installedAt | Date |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |

## u_mes_sys_operatorApp

Kind: entity | Data class: master | Parent: - | _id pattern: APP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | appType | String |  |
| 7 | version | Int32 |  |
| 8 | publishedById | String | u_mes_mdm_user._id |
| 9 | publishedBy | String |  |
| 10 | publishedAt | Date |  |
| 11 | approvedById | String | u_mes_mdm_user._id |
| 12 | approvedBy | String |  |
| 13 | approvedAt | Date |  |
| 14 | previousVersionOperatorAppId | String | u_mes_sys_operatorApp._id |
| 15 | previousVersionOperatorAppName | String |  |
| 16 | status | String |  |
| 17 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppWorkCenter

Kind: relationship | Data class: master | Parent: u_mes_sys_operatorApp | _id pattern: <operatorAppId>-WC<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppId | String | u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | workCenterId | String | u_mes_mdm_workCenter._id |
| 9 | workCenterName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppOperation

Kind: relationship | Data class: master | Parent: u_mes_sys_operatorApp | _id pattern: <operatorAppId>-O<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppId | String | u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppStep

Kind: child | Data class: master | Parent: u_mes_sys_operatorApp | _id pattern: <operatorAppId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppId | String | u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | name | String |  |
| 9 | widgetType | String |  |
| 10 | workInstructionId | String | u_mes_prd_workInstruction._id |
| 11 | workInstructionName | String |  |
| 12 | inspectionPlanId | String | u_mes_qlt_inspectionPlan._id |
| 13 | inspectionPlanName | String |  |
| 14 | nextStepNo | Int32 |  |
| 15 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppStepTrigger

Kind: child | Data class: master | Parent: u_mes_sys_operatorAppStep | _id pattern: <operatorAppStepId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppStepId | String | u_mes_sys_operatorAppStep._id |
| 6 | operatorAppStepName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | triggerEvent | String |  |
| 9 | triggerAction | String |  |
| 10 | triggerTarget | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppDeviceBinding

Kind: child | Data class: master | Parent: u_mes_sys_operatorApp | _id pattern: <operatorAppId>-DB<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppId | String | u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | iotDeviceId | String | u_mes_sys_iotDevice._id |
| 9 | iotDeviceName | String |  |
| 10 | purpose | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_sys_operatorAppLanguage

Kind: valueList | Data class: master | Parent: u_mes_sys_operatorApp | _id pattern: <operatorAppId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | operatorAppId | String | u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | language | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_sys_businessEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: EVT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | eventType | String |  |
| 6 | eventCategory | String |  |
| 7 | occurredAt | Date |  |
| 8 | relatedCollectionName | String |  |
| 9 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String |  |
| 11 | workCenterId | String | u_mes_mdm_workCenter._id |
| 12 | workCenterName | String |  |
| 13 | equipmentId | String | u_mes_mdm_equipment._id |
| 14 | equipmentName | String |  |
| 15 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 16 | productionOrderName | String |  |
| 17 | userId | String | u_mes_mdm_user._id |
| 18 | userName | String |  |
| 19 | iotDeviceId | String | u_mes_sys_iotDevice._id |
| 20 | iotDeviceName | String |  |
| 21 | severity | Int32 |  |
| 22 | messageText | String |  |
| 23 | eventPayloadText | String |  |
| 24 | correlationNo | String |  |
| 25 | source | String |  |
| 26 | schemaVersion | Int32 |  |
| 27 | createdAt | Date |  |
| 28 | createdById | String | u_mes_mdm_user._id |
| 29 | createdBy | String |  |
| 30 | updatedAt | Date |  |
| 31 | updatedById | String | u_mes_mdm_user._id |
| 32 | updatedBy | String |  |

## u_mes_sys_auditTrail

Kind: entity | Data class: transaction | Parent: - | _id pattern: ADT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | relatedCollectionName | String |  |
| 6 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 7 | relatedEntityName | String |  |
| 8 | changeAction | String |  |
| 9 | changedAt | Date |  |
| 10 | changedById | String | u_mes_mdm_user._id |
| 11 | changedBy | String |  |
| 12 | reasonText | String |  |
| 13 | electronicSignatureId | String | u_mes_sys_electronicSignature._id |
| 14 | electronicSignatureName | String |  |
| 15 | clientIp | String |  |
| 16 | application | String |  |
| 17 | documentVersionBefore | Int32 |  |
| 18 | documentVersionAfter | Int32 |  |
| 19 | previousHash | String |  |
| 20 | entryHash | String |  |
| 21 | schemaVersion | Int32 |  |
| 22 | createdAt | Date |  |
| 23 | createdById | String | u_mes_mdm_user._id |
| 24 | createdBy | String |  |
| 25 | updatedAt | Date |  |
| 26 | updatedById | String | u_mes_mdm_user._id |
| 27 | updatedBy | String |  |

## u_mes_sys_auditTrailChange

Kind: child | Data class: transaction | Parent: u_mes_sys_auditTrail | _id pattern: <auditTrailId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | auditTrailId | String | u_mes_sys_auditTrail._id |
| 6 | auditTrailName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | changedFieldName | String |  |
| 9 | oldValue | String |  |
| 10 | newValue | String |  |
| 11 | schemaVersion | Int32 |  |
| 12 | createdAt | Date |  |
| 13 | createdById | String | u_mes_mdm_user._id |
| 14 | createdBy | String |  |
| 15 | updatedAt | Date |  |
| 16 | updatedById | String | u_mes_mdm_user._id |
| 17 | updatedBy | String |  |

## u_mes_sys_electronicSignature

Kind: entity | Data class: transaction | Parent: - | _id pattern: SIG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | relatedCollectionName | String |  |
| 6 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 7 | relatedEntityName | String |  |
| 8 | userId | String | u_mes_mdm_user._id |
| 9 | userName | String |  |
| 10 | roleId | String | u_mes_mdm_role._id |
| 11 | roleName | String |  |
| 12 | meaning | String |  |
| 13 | signedAt | Date |  |
| 14 | authenticationMethod | String |  |
| 15 | contentHash | String |  |
| 16 | comment | String |  |
| 17 | clientIp | String |  |
| 18 | workstation | String |  |
| 19 | isSecondSignature | Boolean |  |
| 20 | witnessUserId | String | u_mes_mdm_user._id |
| 21 | witnessUserName | String |  |
| 22 | schemaVersion | Int32 |  |
| 23 | createdAt | Date |  |
| 24 | createdById | String | u_mes_mdm_user._id |
| 25 | createdBy | String |  |
| 26 | updatedAt | Date |  |
| 27 | updatedById | String | u_mes_mdm_user._id |
| 28 | updatedBy | String |  |

## u_mes_sys_notification

Kind: entity | Data class: transaction | Parent: - | _id pattern: NTF-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | notificationType | String |  |
| 6 | severity | Int32 |  |
| 7 | title | String |  |
| 8 | bodyText | String |  |
| 9 | relatedCollectionName | String |  |
| 10 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String |  |
| 12 | andonEventId | String | u_mes_ehs_andonEvent._id |
| 13 | andonEventName | String |  |
| 14 | alarmId | String | u_mes_eqp_alarm._id |
| 15 | alarmName | String |  |
| 16 | nonconformanceId | String | u_mes_qlt_nonconformance._id |
| 17 | nonconformanceName | String |  |
| 18 | escalationLevel | Int32 |  |
| 19 | raisedAt | Date |  |
| 20 | acknowledgedById | String | u_mes_mdm_user._id |
| 21 | acknowledgedBy | String |  |
| 22 | acknowledgedAt | Date |  |
| 23 | expiresAt | Date |  |
| 24 | status | String |  |
| 25 | schemaVersion | Int32 |  |
| 26 | createdAt | Date |  |
| 27 | createdById | String | u_mes_mdm_user._id |
| 28 | createdBy | String |  |
| 29 | updatedAt | Date |  |
| 30 | updatedById | String | u_mes_mdm_user._id |
| 31 | updatedBy | String |  |

## u_mes_sys_notificationRecipient

Kind: child | Data class: transaction | Parent: u_mes_sys_notification | _id pattern: <notificationId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | notificationId | String | u_mes_sys_notification._id |
| 6 | notificationName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | userId | String | u_mes_mdm_user._id |
| 9 | userName | String |  |
| 10 | roleId | String | u_mes_mdm_role._id |
| 11 | roleName | String |  |
| 12 | channel | String |  |
| 13 | sentAt | Date |  |
| 14 | deliveredAt | Date |  |
| 15 | readAt | Date |  |
| 16 | schemaVersion | Int32 |  |
| 17 | createdAt | Date |  |
| 18 | createdById | String | u_mes_mdm_user._id |
| 19 | createdBy | String |  |
| 20 | updatedAt | Date |  |
| 21 | updatedById | String | u_mes_mdm_user._id |
| 22 | updatedBy | String |  |

## u_mes_sys_controlledDocument

Kind: entity | Data class: transaction | Parent: - | _id pattern: DOC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | documentType | String |  |
| 7 | revision | String |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | relatedCollectionName | String |  |
| 11 | relatedEntityId | String | any collection, named in relatedCollectionName |
| 12 | relatedEntityName | String |  |
| 13 | fileName | String |  |
| 14 | mimeType | String |  |
| 15 | sizeBytes | Int64 |  |
| 16 | storageProvider | String |  |
| 17 | storageKey | String |  |
| 18 | checksumSha256 | String |  |
| 19 | language | String |  |
| 20 | authorUserId | String | u_mes_mdm_user._id |
| 21 | authorUserName | String |  |
| 22 | approvedById | String | u_mes_mdm_user._id |
| 23 | approvedBy | String |  |
| 24 | approvedAt | Date |  |
| 25 | effectiveFrom | Date |  |
| 26 | expiresAt | Date |  |
| 27 | retentionYears | Int32 |  |
| 28 | isControlled | Boolean |  |
| 29 | status | String |  |
| 30 | schemaVersion | Int32 |  |
| 31 | createdAt | Date |  |
| 32 | createdById | String | u_mes_mdm_user._id |
| 33 | createdBy | String |  |
| 34 | updatedAt | Date |  |
| 35 | updatedById | String | u_mes_mdm_user._id |
| 36 | updatedBy | String |  |

## u_mes_sys_controlledDocumentTag

Kind: valueList | Data class: transaction | Parent: u_mes_sys_controlledDocument | _id pattern: <controlledDocumentId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | controlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 6 | controlledDocumentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | tag | String |  |
| 9 | schemaVersion | Int32 |  |
| 10 | createdAt | Date |  |
| 11 | createdById | String | u_mes_mdm_user._id |
| 12 | createdBy | String |  |
| 13 | updatedAt | Date |  |
| 14 | updatedById | String | u_mes_mdm_user._id |
| 15 | updatedBy | String |  |

## u_mes_sys_numberRange

Kind: entity | Data class: master | Parent: - | _id pattern: NR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | rangeType | String |  |
| 7 | itemId | String | u_mes_prd_item._id |
| 8 | itemName | String |  |
| 9 | prefix | String |  |
| 10 | formatMask | String |  |
| 11 | currentValue | Int64 |  |
| 12 | minValue | Int64 |  |
| 13 | maxValue | Int64 |  |
| 14 | incrementById | String | u_mes_mdm_user._id |
| 15 | incrementBy | String |  |
| 16 | resetPolicy | String |  |
| 17 | lastResetAt | Date |  |
| 18 | checkDigitMethod | String |  |
| 19 | warnAtPct | Decimal128 |  |
| 20 | lastIssuedValue | Int64 |  |
| 21 | lastIssuedAt | Date |  |
| 22 | exampleValue | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_sys_systemConfiguration

Kind: entity | Data class: master | Parent: - | _id pattern: CFG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | module | String |  |
| 6 | description | String |  |
| 7 | valueType | String |  |
| 8 | configValueText | String |  |
| 9 | configValueNumber | Decimal128 |  |
| 10 | configValueFlag | Boolean |  |
| 11 | configValueJson | String |  |
| 12 | scope | String |  |
| 13 | isEditable | Boolean |  |
| 14 | isSecret | Boolean |  |
| 15 | validFrom | Date |  |
| 16 | lastChangedReason | String |  |
| 17 | status | String |  |
| 18 | schemaVersion | Int32 |  |

## u_mes_sys_statusDefinition

Kind: entity | Data class: master | Parent: - | _id pattern: STD-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | collectionName | String |  |
| 6 | fieldName | String |  |
| 7 | statusCode | String |  |
| 8 | statusName | String |  |
| 9 | description | String |  |
| 10 | sequenceNo | Int32 |  |
| 11 | isInitial | Boolean |  |
| 12 | isFinal | Boolean |  |
| 13 | colourCode | String |  |
| 14 | status | String |  |
| 15 | schemaVersion | Int32 |  |

## u_mes_sys_statusTransition

Kind: entity | Data class: master | Parent: - | _id pattern: STT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | collectionName | String |  |
| 6 | fromStatusDefinitionId | String | u_mes_sys_statusDefinition._id |
| 7 | fromStatusDefinitionName | String |  |
| 8 | toStatusDefinitionId | String | u_mes_sys_statusDefinition._id |
| 9 | toStatusDefinitionName | String |  |
| 10 | transitionName | String |  |
| 11 | requiresSignature | Boolean |  |
| 12 | requiresReason | Boolean |  |
| 13 | sequenceNo | Int32 |  |
| 14 | status | String |  |
| 15 | schemaVersion | Int32 |  |
