# u_mes_syst_erpMessage

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Inbound and outbound interface messages (order download, confirmation, goods movement) with payload, status, retries |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | MSG-<recordNo> |
| Display value used by references | recordNo |
| Keys | 40 (25 required, 15 may be null) |
| Estimated volume per year | ~2 million |
| Storage | standard, TTL archive |

## Structure

Flat entity collection: one document per ERP message, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: MSG-<recordNo> | `"MSG-20260929-000871"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000871"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | integrationConnectorId | String | Yes | Reference to u_mes_syst_integrationConnector._id | `"ICN-ERP-PRD"` | Reference: u_mes_syst_integrationConnector._id |
| 6 | integrationConnectorName | String | Yes | Display value of integrationConnectorId, copied from u_mes_syst_integrationConnector.name | `"ERP production interface"` |  |
| 7 | direction | String | Yes | Direction of the ERP message | `"Inbound"` | Inbound; Outbound |
| 8 | messageType | String | Yes | Message type | `"Production Order Download"` | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| 9 | idempotencyKey | String | Yes | Key that makes repeated delivery of the same message harmless | `"ERP-PRD-000100041200-0001"` |  |
| 10 | correlationNo | String | Yes | Identifier shared by records that belong to the same business transaction | `"c7a41e06-2d1f-4b7e-9a52-0c5f3e8b1d44"` |  |
| 11 | relatedCollectionName | String | Yes | Name of the collection the related document is in | `"u_mes_plan_wipUnit"` |  |
| 12 | relatedEntityId | String | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"WU-U260929A0184"` | Reference: Any collection (see relatedCollectionName) |
| 13 | relatedEntityName | String | No (null allowed) | Display value of the related document | `"U260929A0184"` |  |
| 14 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 16 | goodsReceiptId | String | No (null allowed) | Reference to u_mes_matl_goodsReceipt._id | `"GRN-2026-000918"` | Reference: u_mes_matl_goodsReceipt._id |
| 17 | goodsReceiptName | String | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_matl_goodsReceipt.recordNo | `"2026-000918"` |  |
| 18 | shipmentId | String | No (null allowed) | Reference to u_mes_matl_shipment._id | `"SHP-2026-000377"` | Reference: u_mes_matl_shipment._id |
| 19 | shipmentName | String | No (null allowed) | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `"2026-000377"` |  |
| 20 | payload | String | Yes | Payload of the ERP message | `"[)>06PSM-3501-0421-LHQ241TL260929-FG-002"` |  |
| 21 | payloadFormat | String | Yes | Payload format | `"JSON"` | JSON; XML; IDoc |
| 22 | payloadHash | String | Yes | Payload hash | `"5e1b0a7c9d3f42e8a6b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9"` |  |
| 23 | attempts | Int32 | Yes | Attempts of the ERP message | `NumberInt(1)` |  |
| 24 | maxAttempts | Int32 | Yes | Maximum attempts | `NumberInt(5)` |  |
| 25 | createdInSourceAt | Date | Yes | Created in source date and time | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 26 | receivedAt | Date | No (null allowed) | Date and time when the record was received | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 27 | processedAt | Date | No (null allowed) | Date and time when the record was processed | `ISODate("2026-09-29T00:31:14.000+0000")` |  |
| 28 | nextRetryAt | Date | No (null allowed) | Next retry date and time | `null` |  |
| 29 | errorCode | String | No (null allowed) | Error code | `null` |  |
| 30 | errorText | String | No (null allowed) | Error text | `null` |  |
| 31 | erpDocumentNo | String | No (null allowed) | ERP document number | `"4900318842"` |  |
| 32 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `ISODate("2026-09-29T00:31:34.000+0000")` |  |
| 33 | status | String | Yes | Primary lifecycle state of the document | `"Acknowledged"` | Queued; Sent; Acknowledged; Failed; Dead Letter |
| 34 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 36 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 38 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:31:34.000+0000")` |  |
| 39 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Status values

Queued, Sent, Acknowledged, Failed, Dead Letter. Initial state: Queued. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ integrationConnectorId: 1 }` | No | Look-up of documents by integration connector |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ goodsReceiptId: 1 }` | No | Look-up of documents by goods receipt |
| 6 | `{ shipmentId: 1 }` | No | Look-up of documents by shipment |
| 7 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 8 | `{ siteId: 1, createdInSourceAt: -1 }` | No | Time-ordered lists and reports by created in source at |
| 9 | `{ idempotencyKey: 1 }` | Yes | A repeated delivery of the same message is rejected |

## Referenced by

u_mes_plan_productionOrder, u_mes_matl_materialConsumption.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_erpMessage.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_erpMessage.js
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_erpMessage.js
