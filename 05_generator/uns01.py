"""Requirement set UNS_01: Unified Namespace on Azure IoT Hub (design 02_architecture/data_flows/unified_namespace_design.md, D081, D082, D083).
3 new collections (numbered after GMP_Pharma_01 by their position: 1370-1372), 10 keys added to 10 existing collections, allowed-value additions.
Merged into ext_req01.NEW / ADD / ENUM_ADD, so every generator that reads ext_req01 picks the set up unchanged.
Same tuple format as ext_req01.py and gmp01.py: fields (key, BSON type, null allowed, referenced entity or None, description).
Keys holding a UNS message id end in 'Uuid', not 'Id', because a key ending in 'Id' is read as a reference by the generators."""

SRC = 'UNS_01'
TAG = 'uns01'

def _c(**kw):
    kw.setdefault('src', SRC); kw.setdefault('tag', TAG); return kw

NEW = [
 _c(no=1370, entity='unsMessageType', prefix='UMT', volume='about 30', storage='standard collection',
  module='syst', kind='entity', type='Master', label='UNS Message Types',
  purpose='Catalogue of the message types carried by the Unified Namespace on Azure IoT Hub: namespace, message type, payload schema and version, message class, the MES collection the ingestion service writes and the device twin property that holds the current state.',
  why='Small master list maintained by the MES team; the ingestion service validates every message against it, the data lake team reads it as the message catalogue, and a new message type is a data change instead of a code change.',
  bk='<namespace>.<message type>, e.g. edge.result.tightening', status=['Active', 'Inactive'], q='UNS design sections 4.3 and 7',
  idx='unique `recordNo`; unique (`unsNamespace`, `messageTypeCode`, `payloadSchemaVersion`)',
  fields=[
   ('name', 'String', False, None, 'Display name of the message type'),
   ('description', 'String', False, None, 'What the message carries and when it is sent'),
   ('unsNamespace', 'String', False, None, 'UNS namespace of the message; sent in lower case as the application property ns'),
   ('messageTypeCode', 'String', False, None, 'Message type within the namespace, sent as the application property msgType'),
   ('payloadSchemaName', 'String', False, None, 'Payload schema name carried in the envelope field schema'),
   ('payloadSchemaVersion', 'Int32', False, None, 'Major version of the payload schema'),
   ('messageClass', 'String', False, None, 'State, event or measurement'),
   ('hierarchyLevel', 'String', False, None, 'ISA-95 level of the node the message describes'),
   ('senderType', 'String', False, None, 'Kind of IoT Hub identity that sends the message'),
   ('targetCollectionName', 'String', True, None, 'MES collection the ingestion service writes; null when the MES does not store the message'),
   ('twinPropertyPath', 'String', True, None, 'Device twin property that holds the current state; null for events'),
   ('ingestedByMes', 'Boolean', False, None, 'True when the MES ingestion service stores the message'),
   ('routedToDataLake', 'Boolean', False, None, 'True when IoT Hub routing writes the message to the client data lake'),
  ],
  enums={
   'unsNamespace': ['Edge', 'MES', 'KPI'],
   'messageClass': ['State', 'Event', 'Measurement'],
   'hierarchyLevel': ['Site', 'Area', 'Line', 'Work Center', 'Equipment'],
   'senderType': ['IoT Edge Gateway', 'MES Publisher'],
  }),
 _c(no=1371, entity='iotHubIdentity', prefix='IHI', volume='about 20 per site', storage='standard collection',
  module='syst', kind='entity', type='Master', label='IoT Hub Identities',
  purpose='One Azure IoT Hub device identity: an equipment identity, an IoT Edge gateway or the MES publisher, with its parent gateway, authentication, certificate, provisioning state, last registry sync and last connection state.',
  why='The identity name and the ISA-95 path are derived from master data (design U3, U4), but whether an identity exists and is in sync in IoT Hub is real state that the registry sync service and maintenance must track.',
  bk='IoT Hub device identity name, e.g. PN1-TRQ-01-N1', status=['Active', 'Inactive'], q='UNS design sections 5.2, 8.6 and 10',
  idx='unique `recordNo`; (`equipmentId`); (`parentIotHubIdentityId`); (`provisioningStatus`)',
  fields=[
   ('name', 'String', False, None, 'Display name of the identity'),
   ('identityType', 'String', False, None, 'Equipment, IoT Edge gateway or MES publisher'),
   ('iotHubName', 'String', False, None, 'Azure IoT Hub the identity is registered in'),
   ('equipmentId', 'String', True, 'equipment', 'Equipment the identity represents; null for gateways and the MES publisher'),
   ('iotDeviceId', 'String', True, 'iotDevice', 'Controller or gateway device behind the identity; null while the device is not registered in the device list'),
   ('parentIotHubIdentityId', 'String', True, 'iotHubIdentity', 'IoT Edge gateway the identity connects through; null for gateways and the MES publisher'),
   ('authenticationMethod', 'String', False, None, 'How the identity authenticates to IoT Hub'),
   ('certificateThumbprint', 'String', True, None, 'SHA-1 thumbprint of the client certificate; null for symmetric key authentication'),
   ('certificateExpiresAt', 'Date', True, None, 'Expiry of the client certificate; null for symmetric key authentication'),
   ('provisioningStatus', 'String', False, None, 'State of the identity in IoT Hub'),
   ('lastRegistrySyncAt', 'Date', True, None, 'Last time the registry sync service wrote the identity and its twin tags; null before the first sync'),
   ('twinTagsVersion', 'Int32', False, None, 'Version of the twin tags last written; increases with each master data change that touches the identity'),
   ('lastSyncErrorText', 'String', True, None, 'Error of the last failed sync; null when the last sync succeeded'),
   ('connectionState', 'String', False, None, 'Last connection state reported by IoT Hub'),
   ('connectionStateAt', 'Date', True, None, 'Time of the last device connection state event; null when the identity never connected'),
  ],
  enums={
   'identityType': ['Equipment', 'IoT Edge Gateway', 'MES Publisher'],
   'authenticationMethod': ['X.509 CA Signed', 'X.509 Self Signed', 'Symmetric Key'],
   'provisioningStatus': ['Not Provisioned', 'Provisioned', 'Sync Failed', 'Disabled'],
   'connectionState': ['Connected', 'Disconnected', 'Never Connected'],
  }),
 _c(no=1372, entity='unsRejectedMessage', prefix='URM', volume='about 500 per year', storage='standard collection, archive after 1 year',
  module='syst', kind='entity', type='Transaction', label='UNS Rejected Messages',
  purpose='One UNS message that the MES ingestion service could not store, with the reason, the payload as received, the copy in the dead-letter container and how it was resolved (sent again after correction, or discarded).',
  why='Event record per rejected message; unbounded over time but low in volume; engineers work through the open ones from a list screen.',
  bk='URM-<yyyymmdd>-<nnnnn>, e.g. URM-20260915-00001', status=['Open', 'Resent', 'Discarded'], q='UNS design sections 7.16 and 8.5',
  idx='unique `recordNo`; unique (`messageUuid`); (`siteId`, `status`, `receivedAt`)',
  fields=[
   ('messageUuid', 'String', False, None, 'Envelope msgId and IoT Hub message-id of the rejected message'),
   ('iotHubIdentityId', 'String', False, 'iotHubIdentity', 'Identity that sent the message'),
   ('unsMessageTypeId', 'String', True, 'unsMessageType', 'Message type from the application properties; null when it cannot be read'),
   ('equipmentId', 'String', True, 'equipment', 'Equipment of the sending identity; null for gateways'),
   ('isa95Path', 'String', True, None, 'ISA-95 path stamped by IoT Hub message enrichment; null when missing'),
   ('payloadSchemaName', 'String', True, None, 'Schema named in the envelope; null when the envelope cannot be read'),
   ('messageTimestamp', 'Date', True, None, 'Envelope ts as plant time; null when missing or unreadable'),
   ('receivedAt', 'Date', False, None, 'Time the ingestion service read the message'),
   ('rejectionReason', 'String', False, None, 'Rule that rejected the message'),
   ('rejectionDetailText', 'String', False, None, 'Detail of the failed check'),
   ('payloadText', 'String', False, None, 'Message body as received (UTF-8 JSON text)'),
   ('deadLetterBlobPath', 'String', False, None, 'Path of the copy in the uns-deadletter blob container'),
   ('resolvedById', 'String', True, 'user', 'Engineer who sent the message again or discarded it'),
   ('resolvedAt', 'Date', True, None, 'Time of the resolution'),
   ('resolutionText', 'String', True, None, 'What was corrected, or why the message was discarded'),
   ('resentMessageUuid', 'String', True, None, 'msgId of the corrected message sent again; null when open or discarded'),
  ],
  enums={
   'rejectionReason': ['Invalid Envelope', 'Unknown Schema', 'Unresolved Master Reference', 'Clock Skew', 'Validator Failure'],
  }),
]

_SMU = 'UNS message id (envelope msgId) the document was created from; null for documents entered or calculated in the MES. Unique per site when present (design 8.3, M1)'
# (entity, key, BSON type, null allowed, referenced entity, allowed values, description)
ADD = [
 ("equipmentState", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("processReading", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("alarm", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("torqueResult", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("leakTestResult", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("energyReading", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("measurementCurve", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("inspectionResult", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("operationExecution", "sourceMessageUuid", "String", True, None, None, _SMU),
 ("iotDevice", "edgeGatewayIotDeviceId", "String", True, "iotDevice", None, "IoT Edge gateway the device reports through to Azure IoT Hub; null for gateways and devices not connected to the UNS (design M4)"),
]

ENUM_ADD = {
 ("integrationConnector", "connectorType"): ["Azure IoT Hub"],
}

# time-series candidates among the collections with sourceMessageUuid: no unique index there (MongoDB time-series collections do not allow one)
TIMESERIES_SMU = {"processReading", "energyReading"}
