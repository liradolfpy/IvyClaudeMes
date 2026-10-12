# u_mes_prod_routing

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Sequence of operations per item, including rework / disposition routings and alternate paths |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 23 (15 required, 8 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per routing, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with routingId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_routingStep | Child | step |
| u_mes_prod_routingStepAlternateWorkCenter | Relationship | (below u_mes_prod_routingStep) alternate work center |
| u_mes_prod_routingStepNextStep | Child | (below u_mes_prod_routingStep) next step |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1053000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 8 | routingVersion | Int32 | - | Yes | Routing version | `NumberInt(1)` |  |
| 9 | routingType | String | - | Yes | Routing type | `"Standard"` | Standard; Rework; Alternate |
| 10 | description | String | - | Yes | Description of the routing | `"Front caliper LH, full process routing"` |  |
| 11 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 12 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 13 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000010"` | Reference: u_mes_prod_engineeringChange._id |
| 14 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Work instruction pictures updated for RH variant"` |  |
| 15 | entryStepNo | Int32 | - | Yes | Step at which material enters the routing | `NumberInt(10)` |  |
| 16 | parentRoutingId | String | - | No (null allowed) | Reference to u_mes_prod_routing._id: parent routing | `null` | Reference: u_mes_prod_routing._id |
| 17 | parentRoutingName | String | - | No (null allowed) | Display value of parentRoutingId, copied from u_mes_prod_routing.description | `null` |  |
| 18 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 19 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 20 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 21 | erpRoutingNo | String | - | Yes | ERP routing number | `"50001101-01"` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 5 | `{ parentRoutingId: 1 }` | No | Look-up of documents by parent routing |

## Referenced by

u_mes_prod_routing, u_mes_prod_routingStep, u_mes_prod_billOfProcess, u_mes_plan_productionOrder, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_qual_controlPlan, u_mes_qual_defectCode, u_mes_qual_reworkOrder.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_routing.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_routing.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_routing.js
