# u_mes_syst_operatorAppDeviceBinding

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per device binding of a operator app |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_syst_operatorApp |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Child collection. The parent operator app can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. operatorAppId and operatorAppName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1238000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-GDC-01-DB01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operatorAppId | String | Yes | Reference to u_mes_syst_operatorApp._id: the parent document this one belongs to | `"1233000000000001"` | Reference: u_mes_syst_operatorApp._id |
| 6 | operatorAppName | String | Yes | Display value of operatorAppId, copied from u_mes_syst_operatorApp.name | `"Operator app, Gravity Die Casting Cell 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | iotDeviceId | String | Yes | Reference to u_mes_syst_iotDevice._id | `"1232000000000001"` | Reference: u_mes_syst_iotDevice._id |
| 9 | iotDeviceName | String | Yes | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `"PLC, casting machine 1"` |  |
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

- Validator: 03_design/09_system_integration/validators/u_mes_syst_operatorAppDeviceBinding.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_operatorAppDeviceBinding.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_operatorAppDeviceBinding.js
