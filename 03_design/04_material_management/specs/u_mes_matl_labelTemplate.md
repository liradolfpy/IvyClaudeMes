# u_mes_matl_labelTemplate

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Label layouts (unit 2D code, bin label, customer shipping label, hold tag) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 19 (17 required, 2 may be null) |
| Estimated volume per year | 20-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per label template, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with labelTemplateId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_labelTemplateField | Child | field |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1124000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SML-BIN-A5"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the label template; used as its display value in other collections | `"Sahyadri Motors bin label A5"` |  |
| 6 | labelType | String | - | Yes | Label type | `"Container Label"` | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| 7 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 8 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 9 | standard | String | - | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 10 | widthMm | Decimal128 | - | Yes | Width (mm) | `NumberDecimal("400.0")` |  |
| 11 | heightMm | Decimal128 | - | Yes | Height (mm) | `NumberDecimal("280.0")` |  |
| 12 | printerLanguage | String | - | Yes | Printer language | `"ZPL"` | ZPL; EPL; PDF |
| 13 | symbology | String | - | Yes | Symbology of the label template | `"Data Matrix ECC200"` | Data Matrix ECC200; QR Code; Code 128; Code 39; PDF417 |
| 14 | payloadPattern | String | - | Yes | Payload pattern | `"[)>{RS}06{GS}P{customerPartNo}{GS}Q{quantity}{GS}1T{lotNo}{RS}{EOT}"` |  |
| 15 | version | Int32 | - | Yes | Version of the label template | `NumberInt(1)` |  |
| 16 | copies | Int32 | - | Yes | Copies of the label template | `NumberInt(1)` |  |
| 17 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 18 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |

## Referenced by

u_mes_mast_customer, u_mes_matl_packagingSpecification, u_mes_matl_labelTemplateField, u_mes_matl_label.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_labelTemplate.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_labelTemplate.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_labelTemplate.js
