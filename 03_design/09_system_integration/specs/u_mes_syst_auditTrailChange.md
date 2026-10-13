# u_mes_syst_auditTrailChange

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | One document per change of a audit trail |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_syst_auditTrail |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (16 required, 2 may be null) |

## Structure

Child collection. The parent audit trail can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. auditTrailId and auditTrailName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1242000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ADT-2026-000202-C01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | auditTrailId | String | - | Yes | Reference to u_mes_syst_auditTrail._id: the parent document this one belongs to | `"1241000000000001"` | Reference: u_mes_syst_auditTrail._id |
| 7 | auditTrailName | String | - | Yes | Display value of auditTrailId, copied from u_mes_syst_auditTrail.recordNo | `"ADT-2026-000202"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | changedFieldName | String | - | Yes | Changed field name | `"upperSpecLimit"` |  |
| 10 | oldValue | String | - | No (null allowed) | Old value | `"15.5"` |  |
| 11 | newValue | String | - | No (null allowed) | New value | `"16.0"` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 14 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 16 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 17 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ auditTrailId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_auditTrailChange.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_auditTrailChange.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_auditTrailChange.js
