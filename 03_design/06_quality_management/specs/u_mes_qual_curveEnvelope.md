# u_mes_qual_curveEnvelope

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Approved golden-sample envelope for a force–displacement, torque–angle, pressure–time or signal curve. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 31 (23 required, 8 may be null) |
| Estimated volume per year | about 100 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per curve envelope, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with curveEnvelopeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_curveEnvelopeWindow | Child | window |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1317000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ENV-OP060-PST-PRESS-02"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Envelope name | `"Piston press-in force, front caliper LH"` |  |
| 6 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000006"` | Reference: u_mes_qual_characteristic._id |
| 7 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Dust boot seating height"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 12 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000006"` | Reference: u_mes_prod_operation._id |
| 13 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Piston and seal assembly"` |  |
| 14 | recipeId | String | - | No (null allowed) | Reference to u_mes_prod_recipe._id | `null` | Reference: u_mes_prod_recipe._id |
| 15 | recipeName | String | - | No (null allowed) | Display value of recipeId, copied from u_mes_prod_recipe.name | `null` |  |
| 16 | curveType | String | - | Yes | Curve type | `"Force Displacement"` | Force Displacement; Torque Angle; Pressure Time; Sound Spectrum; Vibration Acceleration |
| 17 | xQuantity | String | - | Yes | X-axis quantity, e.g. Displacement | `"Displacement"` |  |
| 18 | xUnitText | String | - | Yes | X-axis unit as delivered by the controller, e.g. mm, deg, ms | `"mm"` |  |
| 19 | yQuantity | String | - | Yes | Y-axis quantity, e.g. Force | `"Force"` |  |
| 20 | yUnitText | String | - | Yes | Y-axis unit as delivered by the controller, e.g. N, N.m, bar | `"N"` |  |
| 21 | version | Int32 | - | Yes | Envelope version number | `NumberInt(2)` |  |
| 22 | goldenSampleSerialNo | String | - | No (null allowed) | Serial of the golden sample used | `"VB26240A00012"` |  |
| 23 | referenceControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: reference controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 24 | referenceControlledDocumentName | String | - | No (null allowed) | Display value of referenceControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 25 | effectiveFrom | Date | Date | Yes | Effective from | `ISODate("2026-08-28T00:00:00.000+0000")` |  |
| 26 | effectiveTo | Date | Date | No (null allowed) | Effective to | `null` |  |
| 27 | approvedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 28 | approvedBy | String | - | Yes | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 29 | approvedAt | Date | Datetime | Yes | Approval time | `ISODate("2026-08-27T11:10:00.000+0000")` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 6 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 7 | `{ recipeId: 1 }` | No | Look-up of documents by recipe |

## Referenced by

u_mes_perf_torqueResult, u_mes_qual_characteristicPosition, u_mes_qual_curveEnvelopeWindow, u_mes_qual_measurementCurve.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_curveEnvelope.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_curveEnvelope.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_curveEnvelope.js
