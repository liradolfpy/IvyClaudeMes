# u_mes_plan_containerType

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Types of container with dimensions and tare weight |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 14 (14 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per container type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1278000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RB-6040"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the container type; used as its display value in other collections | `"Returnable Bin 600 x 400"` |  |
| 6 | description | String | - | Yes | Description of the container type | `"Returnable Bin 600 x 400 (RB-6040)"` |  |
| 7 | lengthMm | Decimal128 | - | Yes | Length (mm) | `NumberDecimal("600.0")` |  |
| 8 | widthMm | Decimal128 | - | Yes | Width (mm) | `NumberDecimal("400.0")` |  |
| 9 | heightMm | Decimal128 | - | Yes | Height (mm) | `NumberDecimal("280.0")` |  |
| 10 | tareWeightKg | Decimal128 | - | Yes | Tare weight (kg) | `NumberDecimal("2.100")` |  |
| 11 | isReturnable | Boolean | - | Yes | True when the record is returnable | `false` |  |
| 12 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 13 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_plan_container, u_mes_matl_packagingSpecification, u_mes_matl_replenishmentRule.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_containerType.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_containerType.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_containerType.js
