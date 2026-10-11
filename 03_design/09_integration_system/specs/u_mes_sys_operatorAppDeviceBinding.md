# u_mes_sys_operatorAppDeviceBinding

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | One document per device binding of a operator app |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_sys_operatorApp |
| _id pattern | <operatorAppId>-DB<nnn> |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Child collection. The parent operator app can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppId and operatorAppName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <operatorAppId>-DB<nnn> | `"APP-APP-TRQ-01-DB001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-TRQ-01-DB001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operatorAppId | String | Yes | Reference to u_mes_sys_operatorApp._id: the parent document this one belongs to | `"APP-APP-TRQ-01"` | Reference: u_mes_sys_operatorApp._id |
| 6 | operatorAppName | String | Yes | Display value of operatorAppId, copied from u_mes_sys_operatorApp.name | `"Torque station operator app"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | iotDeviceId | String | Yes | Reference to u_mes_sys_iotDevice._id | `"IOT-NR-CTRL-01"` | Reference: u_mes_sys_iotDevice._id |
| 9 | iotDeviceName | String | Yes | Display value of iotDeviceId, copied from u_mes_sys_iotDevice.name | `"Nutrunner controller, torque station 1"` |  |
| 10 | purpose | String | Yes | Purpose of the operator app device binding | `"Tightening result"` | Tightening result; Leak test result; Component scan; Label print; Measurement |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operatorAppId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ iotDeviceId: 1 }` | No | Look-up of lines by IoT device |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_operatorAppDeviceBinding.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_operatorAppDeviceBinding.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_operatorAppDeviceBinding.js
