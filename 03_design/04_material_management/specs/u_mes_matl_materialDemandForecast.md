# u_mes_matl_materialDemandForecast

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Short-term component demand and projected line-side shortage per item, line and time bucket. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 31 (28 required, 3 may be null) |
| Estimated volume per year | about 200,000 (recalculated hourly, superseded rows archived) |
| Storage | standard collection, archive after 90 days |

## Structure

Flat entity collection: one document per material demand forecast, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1313000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"MDF-20260924-ASY-01-5110-30-0020-08"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000006"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston Seal, square section, EPDM"` |  |
| 8 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 10 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-24T00:00:00.000+0000")` |  |
| 11 | bucketStartAt | Date | Datetime | Yes | Bucket start | `ISODate("2026-09-24T08:00:00.000+0000")` |  |
| 12 | bucketEndAt | Date | Datetime | Yes | Bucket end | `ISODate("2026-09-24T09:00:00.000+0000")` |  |
| 13 | scheduledDemand | Decimal128 | - | Yes | Demand from the schedule and BOM | `100` |  |
| 14 | consumptionRatePerHour | Decimal128 | - | Yes | Actual consumption rate | `96` |  |
| 15 | onHandQuantity | Decimal128 | - | Yes | Line-side and supermarket stock at calculation | `150` |  |
| 16 | projectedOnHand | Decimal128 | - | Yes | Projected stock at bucket end | `54` |  |
| 17 | projectedShortageAt | Date | Datetime | No (null allowed) | Projected time the line starves | `null` |  |
| 18 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 20 | method | String | - | Yes | Calculation method | `"Model"` | Schedule; Consumption Rate; Model |
| 21 | analyticsModelId | String | - | No (null allowed) | Reference to u_mes_syst_analyticsModel._id | `"1337000000000007"` | Reference: u_mes_syst_analyticsModel._id |
| 22 | analyticsModelName | String | - | No (null allowed) | Display value of analyticsModelId, copied from u_mes_syst_analyticsModel.name | `"Line-side component demand forecast"` |  |
| 23 | calculatedAt | Date | Datetime | Yes | Calculation time | `ISODate("2026-09-24T07:55:00.000+0000")` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Calculated"` | Calculated; Superseded |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 27 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 28 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 29 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-24T09:00:00.000+0000")` |  |
| 30 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 31 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Calculated, Superseded. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 6 | `{ analyticsModelId: 1 }` | No | Look-up of documents by analytics model |
| 7 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_materialDemandForecast.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_materialDemandForecast.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_materialDemandForecast.js
