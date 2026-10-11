# u_mes_sys_auditTrailChange

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | One document per change of a audit trail |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_sys_auditTrail |
| _id pattern | <auditTrailId>-C<nnn> |
| Display value used by references | recordNo |
| Keys | 17 (15 required, 2 may be null) |

## Structure

Child collection. The parent audit trail can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. auditTrailId and auditTrailName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <auditTrailId>-C<nnn> | `"ADT-20260929-00004412-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-00004412-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | auditTrailId | String | Yes | Reference to u_mes_sys_auditTrail._id: the parent document this one belongs to | `"ADT-20260929-00004412"` | Reference: u_mes_sys_auditTrail._id |
| 6 | auditTrailName | String | Yes | Display value of auditTrailId, copied from u_mes_sys_auditTrail.recordNo | `"20260929-00004412"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | changedFieldName | String | Yes | Changed field name | `"upperSpecLimit"` |  |
| 9 | oldValue | String | No (null allowed) | Old value | `"15.5"` |  |
| 10 | newValue | String | No (null allowed) | New value | `"16.0"` |  |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 13 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 14 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"MES System"` |  |
| 15 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-SYSTEM"` | Reference: u_mes_mdm_user._id |
| 17 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ auditTrailId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_auditTrailChange.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_auditTrailChange.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_auditTrailChange.js
