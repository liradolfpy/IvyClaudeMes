# u_mes_mast_equipmentIotDevice

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Links one equipment to one IoT device; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_equipment |
| _id pattern | <equipmentId>-ID<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A equipment can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. equipmentId and equipmentName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <equipmentId>-ID<nnn> | `"EQ-TRQ-01-NR1-ID001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01-NR1-ID001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | equipmentId | String | Yes | Reference to u_mes_mast_equipment._id: the parent document this one belongs to | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 6 | equipmentName | String | Yes | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | iotDeviceId | String | Yes | Reference to u_mes_syst_iotDevice._id | `"IOT-NR-CTRL-01"` | Reference: u_mes_syst_iotDevice._id |
| 9 | iotDeviceName | String | Yes | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `"Nutrunner controller, torque station 1"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ equipmentId: 1, iotDeviceId: 1 }` | Yes | One link per pair |
| 2 | `{ iotDeviceId: 1, equipmentId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_equipmentIotDevice.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_equipmentIotDevice.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_equipmentIotDevice.js
