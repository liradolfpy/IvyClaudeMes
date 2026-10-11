# u_mes_trc_asBuiltRecordOperation

| Property | Value |
|---|---|
| Module | Traceability (trc) |
| Purpose | One document per operation of a as built record |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_trc_asBuiltRecord |
| _id pattern | <asBuiltRecordId>-O<nnn> |
| Display value used by references | recordNo |
| Keys | 24 (19 required, 5 may be null) |

## Structure

Child collection. The parent as built record can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. asBuiltRecordId and asBuiltRecordName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <asBuiltRecordId>-O<nnn> | `"ABR-VB26272A00184-O001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"VB26272A00184-O001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | asBuiltRecordId | String | Yes | Reference to u_mes_trc_asBuiltRecord._id: the parent document this one belongs to | `"ABR-VB26272A00184"` | Reference: u_mes_trc_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | Yes | Display value of asBuiltRecordId, copied from u_mes_trc_asBuiltRecord.recordNo | `"VB26272A00184"` |  |
| 7 | stepNo | Int32 | Yes | Step number within the parent record | `NumberInt(70)` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prd_operation._id | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 10 | workCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 11 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 12 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 13 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 14 | operatorUserId | String | Yes | Reference to u_mes_mdm_user._id: operator user | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 15 | operatorUserName | String | Yes | Display value of operatorUserId, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 16 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | result | String | Yes | Result of the as built record operation | `"OK"` | OK; Not OK |
| 18 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 20 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 21 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 22 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 23 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 24 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ asBuiltRecordId: 1, stepNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ operationId: 1 }` | No | Look-up of lines by operation |
| 3 | `{ workCenterId: 1 }` | No | Look-up of lines by work center |
| 4 | `{ equipmentId: 1 }` | No | Look-up of lines by equipment |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/05_traceability/validators/u_mes_trc_asBuiltRecordOperation.json
- Indexes: 03_design/05_traceability/indexes/u_mes_trc_asBuiltRecordOperation.js
- Sample document: 03_design/05_traceability/samples/u_mes_trc_asBuiltRecordOperation.js
