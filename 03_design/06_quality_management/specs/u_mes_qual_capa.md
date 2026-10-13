# u_mes_qual_capa

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Corrective and preventive actions in 8D structure (D1-D8) with team, root cause, actions, verification |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 42 (22 required, 20 may be null) |
| Estimated volume per year | ~300 |
| Storage | standard |

## Structure

Flat entity collection: one document per CAPA, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with capaId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_capaNonconformance | Relationship | nonconformance |
| u_mes_qual_capaTeamMember | Child | team member |
| u_mes_qual_capaContainmentAction | Child | containment action |
| u_mes_qual_capaCorrectiveAction | Child | corrective action |
| u_mes_qual_capaImplementationAction | Child | implementation action |
| u_mes_qual_capaControlledDocument | Relationship | controlled document |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1176000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CAPA-2026-0014"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title of the CAPA; used as its display value in other collections | `"8D - Shrinkage porosity in bridge section"` |  |
| 6 | capaType | String | - | Yes | CAPA type | `"Corrective"` | Corrective; Preventive |
| 7 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 8 | customerComplaintId | String | - | No (null allowed) | Reference to u_mes_qual_customerComplaint._id | `null` | Reference: u_mes_qual_customerComplaint._id |
| 9 | customerComplaintName | String | - | No (null allowed) | Display value of customerComplaintId, copied from u_mes_qual_customerComplaint.description | `null` |  |
| 10 | auditId | String | - | No (null allowed) | Reference to u_mes_qual_audit._id | `null` | Reference: u_mes_qual_audit._id |
| 11 | auditName | String | - | No (null allowed) | Display value of auditId, copied from u_mes_qual_audit.title | `null` |  |
| 12 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 13 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 14 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 15 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 16 | openedAt | Date | Datetime | Yes | Date and time when the record was opened. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 17 | openedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'opened' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | openedBy | String | - | Yes | Display name of the user in openedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | d2ProblemDescription | String | - | Yes | D2 problem description | `"Porosity visible on machined face or found by X-ray sampling"` |  |
| 20 | d4RootCauseOccurrence | String | - | No (null allowed) | D4 root cause occurrence | `"Die temperature too low at pour"` |  |
| 21 | d4RootCauseEscape | String | - | No (null allowed) | D4 root cause escape | `"Visual check of groove not in control plan; leak test detects only at end of line"` |  |
| 22 | d4RootCauseMethod | String | - | No (null allowed) | D4 root cause method | `null` | 5 Why; Fishbone; Fault Tree; Is Is Not |
| 23 | d7PreventionPfmeaId | String | - | No (null allowed) | Reference to u_mes_qual_pfmea._id: D7 prevention PFMEA | `"1183000000000001"` | Reference: u_mes_qual_pfmea._id |
| 24 | d7PreventionPfmeaName | String | - | No (null allowed) | Display value of d7PreventionPfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 25 | d7PreventionControlPlanId | String | - | No (null allowed) | Reference to u_mes_qual_controlPlan._id: D7 prevention control plan | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 26 | d7PreventionControlPlanName | String | - | No (null allowed) | Display value of d7PreventionControlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 27 | d7PreventionLessonsLearned | String | - | No (null allowed) | D7 prevention lessons learned | `"Tool life interlock to be enforced on all grooving operations"` |  |
| 28 | d7PreventionHorizontalDeployment | String | - | No (null allowed) | D7 prevention horizontal deployment | `"Apply to rear caliper line LN-MC-02"` |  |
| 29 | d8ClosureClosedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'D8 closure closed' | `null` | Reference: u_mes_mast_user._id |
| 30 | d8ClosureClosedBy | String | - | No (null allowed) | Display name of the user in d8ClosureClosedById, copied from u_mes_mast_user.fullName | `null` |  |
| 31 | d8ClosureClosedAt | Date | Datetime | No (null allowed) | D8 closure closed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 32 | d8ClosureCustomerAccepted | Boolean | - | Yes | True when: D8 closure customer accepted | `true` |  |
| 33 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:00.000+0000")` |  |
| 34 | currentDiscipline | String | - | Yes | Current discipline | `"D8"` | D1; D2; D3; D4; D5; D6; D7; D8 |
| 35 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Containment Done; Root Cause Identified; Actions Implemented; Verified; Closed |
| 36 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 38 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 39 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 40 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:00.000+0000")` |  |
| 41 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 42 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Open, Containment Done, Root Cause Identified, Actions Implemented, Verified, Closed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerComplaintId: 1 }` | No | Look-up of documents by customer complaint |
| 4 | `{ auditId: 1 }` | No | Look-up of documents by audit |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 7 | `{ d7PreventionPfmeaId: 1 }` | No | Look-up of documents by D7 prevention PFMEA |
| 8 | `{ siteId: 1, openedAt: -1 }` | No | Time-ordered lists and reports by opened at |

## Referenced by

u_mes_qual_nonconformance, u_mes_qual_capaNonconformance, u_mes_qual_capaTeamMember, u_mes_qual_capaContainmentAction, u_mes_qual_capaCorrectiveAction, u_mes_qual_capaImplementationAction, u_mes_qual_capaControlledDocument, u_mes_qual_auditFinding, u_mes_qual_customerComplaint, u_mes_perf_downtimeEvent, u_mes_ehs_safetyIncident, u_mes_qual_productRecall.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_capa.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_capa.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_capa.js
