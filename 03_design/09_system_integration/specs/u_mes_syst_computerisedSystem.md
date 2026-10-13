# u_mes_syst_computerisedSystem

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Inventory of the computerised systems that create, hold or process GMP records, with their GxP impact, GAMP category, owners and periodic review cycle. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 27 (21 required, 6 may be null) |
| Estimated volume per year | about 60 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per computerised system, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1344000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CSY-MES-PN1"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | System name | `"Manufacturing execution system, Chakan plant"` |  |
| 6 | description | String | - | Yes | What the system does and which GMP records it holds | `"Production orders, operation executions, genealogy, batch record review, release, reconciliation and electronic signatures for all lines"` |  |
| 7 | systemCategory | String | - | Yes | Kind of system | `"Manufacturing Execution System"` | Manufacturing Execution System; Equipment Controller; Laboratory System; ERP Interface; Label Printing; Data Historian; Infrastructure |
| 8 | gampCategory | String | - | Yes | GAMP 5 software category | `"Category 4"` | Category 1; Category 3; Category 4; Category 5 |
| 9 | gxpImpact | String | - | Yes | Impact of the system on product quality and GMP records | `"Direct"` | Direct; Indirect; None |
| 10 | dataCriticality | String | - | Yes | Criticality of the data the system holds | `"High"` | High; Medium; Low |
| 11 | holdsElectronicRecords | Boolean | - | Yes | True when GMP records are kept in electronic form (21 CFR Part 11 scope) | `true` |  |
| 12 | usesElectronicSignatures | Boolean | - | Yes | True when electronic signatures are applied in the system | `true` |  |
| 13 | systemOwnerUserId | String | - | Yes | Reference to u_mes_mast_user._id: system owner user | `"1029000000000009"` | Reference: u_mes_mast_user._id |
| 14 | systemOwnerUserName | String | - | Yes | Display value of systemOwnerUserId, copied from u_mes_mast_user.fullName | `"Sneha Joshi"` |  |
| 15 | processOwnerUserId | String | - | Yes | Reference to u_mes_mast_user._id: process owner user | `"1029000000000007"` | Reference: u_mes_mast_user._id |
| 16 | processOwnerUserName | String | - | Yes | Display value of processOwnerUserId, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 17 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 18 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 19 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `null` | Reference: u_mes_mast_equipment._id |
| 20 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 21 | softwareVersion | String | - | Yes | Installed software version | `"2.7.0"` |  |
| 22 | hostingModel | String | - | Yes | Where the system runs | `"Private Cloud"` | On Premise; Private Cloud; Supplier Hosted; Embedded |
| 23 | lastValidatedDate | Date | Date | No (null allowed) | Date of the last approved validation; null before the first one | `ISODate("2026-09-05T00:00:00.000+0000")` |  |
| 24 | periodicReviewIntervalMonths | Int32 | - | Yes | Interval between periodic reviews (months) | `NumberInt(12)` |  |
| 25 | nextPeriodicReviewDate | Date | Date | No (null allowed) | Date the next periodic review is due | `ISODate("2027-09-15T00:00:00.000+0000")` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Validated"` | In Validation; Validated; Retired |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Validation, Validated, Retired. Initial state: In Validation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ systemOwnerUserId: 1 }` | No | Look-up of documents by system owner user |
| 4 | `{ processOwnerUserId: 1 }` | No | Look-up of documents by process owner user |
| 5 | `{ supplierId: 1 }` | No | Look-up of documents by supplier |
| 6 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |

## Referenced by

u_mes_syst_systemValidation, u_mes_syst_systemPeriodicReview, u_mes_syst_auditTrailReview, u_mes_syst_userAccessReview.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_computerisedSystem.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_computerisedSystem.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_computerisedSystem.js
