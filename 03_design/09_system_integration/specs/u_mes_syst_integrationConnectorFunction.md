# u_mes_syst_integrationConnectorFunction

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per function of a integration connector |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_integrationConnector |
| _id pattern | <integrationConnectorId>-F<nnn> |
| Display value used by references | recordNo |
| Keys | 13 (12 required, 1 may be null) |

## Structure

Child collection. The parent integration connector can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. integrationConnectorId and integrationConnectorName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <integrationConnectorId>-F<nnn> | `"ICN-ERP-PRD-F001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ERP-PRD-F001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | integrationConnectorId | String | Yes | Reference to u_mes_syst_integrationConnector._id: the parent document this one belongs to | `"ICN-ERP-PRD"` | Reference: u_mes_syst_integrationConnector._id |
| 6 | integrationConnectorName | String | Yes | Display value of integrationConnectorId, copied from u_mes_syst_integrationConnector.name | `"ERP production interface"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | functionName | String | Yes | Function name | `"postOperationConfirmation"` |  |
| 9 | direction | String | Yes | Direction of the integration connector function | `"Inbound"` | Inbound; Outbound |
| 10 | messageType | String | Yes | Message type | `"Production Order Download"` | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| 11 | endpointPath | String | Yes | Endpoint path | `"/v1/confirmations"` |  |
| 12 | scheduleExpression | String | No (null allowed) | Cron expression for scheduled functions | `"*/5 * * * *"` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ integrationConnectorId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_integrationConnectorFunction.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_integrationConnectorFunction.js
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_integrationConnectorFunction.js
