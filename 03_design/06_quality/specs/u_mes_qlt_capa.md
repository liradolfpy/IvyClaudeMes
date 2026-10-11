# u_mes_qlt_capa

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Corrective and preventive actions in 8D structure (D1-D8) with team, root cause, actions, verification |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | CAPA-<recordNo> |
| Display value used by references | title |
| Keys | 42 (22 required, 20 may be null) |
| Estimated volume per year | ~300 |
| Storage | standard |

## Structure

Flat entity collection: one document per CAPA, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with capaId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_capaNonconformance | Relationship | nonconformance |
| u_mes_qlt_capaTeamMember | Child | team member |
| u_mes_qlt_capaContainmentAction | Child | containment action |
| u_mes_qlt_capaCorrectiveAction | Child | corrective action |
| u_mes_qlt_capaImplementationAction | Child | implementation action |
| u_mes_qlt_capaControlledDocument | Relationship | controlled document |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CAPA-<recordNo> | `"CAPA-2026-0014"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0014"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the CAPA; used as its display value in other collections | `"8D - Leak at piston seal"` |  |
| 6 | capaType | String | Yes | CAPA type | `"Corrective"` | Corrective; Preventive |
| 7 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 8 | customerComplaintId | String | No (null allowed) | Reference to u_mes_qlt_customerComplaint._id | `"CMP-2026-0004"` | Reference: u_mes_qlt_customerComplaint._id |
| 9 | customerComplaintName | String | No (null allowed) | Display value of customerComplaintId, copied from u_mes_qlt_customerComplaint.description | `"Bleed screw cap missing on three calipers at customer line"` |  |
| 10 | auditId | String | No (null allowed) | Reference to u_mes_qlt_audit._id | `"AUD-LPA-2026-0931"` | Reference: u_mes_qlt_audit._id |
| 11 | auditName | String | No (null allowed) | Display value of auditId, copied from u_mes_qlt_audit.title | `"Layered process audit, Assembly line 1, week 40"` |  |
| 12 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 13 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 14 | customerId | String | No (null allowed) | Reference to u_mes_mdm_customer._id | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 15 | customerName | String | No (null allowed) | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 16 | openedAt | Date | Yes | Date and time when the record was opened | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | openedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'opened' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 18 | openedBy | String | Yes | Display name of the user in openedById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 19 | d2ProblemDescription | String | Yes | D2 problem description | `"Leak test failures at 140 bar stage on caliper LH, 6 of 480 units on 29 Sep 2026 shift A"` |  |
| 20 | d4RootCauseOccurrence | String | No (null allowed) | D4 root cause occurrence | `"Burr on seal groove edge after grooving insert exceeded tool life"` |  |
| 21 | d4RootCauseEscape | String | No (null allowed) | D4 root cause escape | `"Visual check of groove not in control plan; leak test detects only at end of line"` |  |
| 22 | d4RootCauseMethod | String | No (null allowed) | D4 root cause method | `"5 Why"` | 5 Why; Fishbone; Fault Tree; Is Is Not |
| 23 | d7PreventionPfmeaId | String | No (null allowed) | Reference to u_mes_qlt_pfmea._id: D7 prevention PFMEA | `"FMEA-5110-10-0100-PF"` | Reference: u_mes_qlt_pfmea._id |
| 24 | d7PreventionPfmeaName | String | No (null allowed) | Display value of d7PreventionPfmeaId, copied from u_mes_qlt_pfmea.title | `"Process FMEA, Front Brake Caliper Assembly LH"` |  |
| 25 | d7PreventionControlPlanId | String | No (null allowed) | Reference to u_mes_qlt_controlPlan._id: D7 prevention control plan | `"CP-5110-10-0100-PROD"` | Reference: u_mes_qlt_controlPlan._id |
| 26 | d7PreventionControlPlanName | String | No (null allowed) | Display value of d7PreventionControlPlanId, copied from u_mes_qlt_controlPlan.recordNo | `"5110-10-0100-PROD"` |  |
| 27 | d7PreventionLessonsLearned | String | No (null allowed) | D7 prevention lessons learned | `"Tool life interlock to be enforced on all grooving operations"` |  |
| 28 | d7PreventionHorizontalDeployment | String | No (null allowed) | D7 prevention horizontal deployment | `"Apply to rear caliper line LN-MC-02"` |  |
| 29 | d8ClosureClosedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'D8 closure closed' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 30 | d8ClosureClosedBy | String | No (null allowed) | Display name of the user in d8ClosureClosedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 31 | d8ClosureClosedAt | Date | No (null allowed) | D8 closure closed date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 32 | d8ClosureCustomerAccepted | Boolean | Yes | True when: D8 closure customer accepted | `true` |  |
| 33 | dueAt | Date | Yes | Due date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 34 | currentDiscipline | String | Yes | Current discipline | `"D5"` | D1; D2; D3; D4; D5; D6; D7; D8 |
| 35 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Open; Containment Done; Root Cause Identified; Actions Implemented; Verified; Closed |
| 36 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 37 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 38 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 39 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 40 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 41 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 42 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Open, Containment Done, Root Cause Identified, Actions Implemented, Verified, Closed. Initial state: Open. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_qlt_nonconformance, u_mes_qlt_capaNonconformance, u_mes_qlt_capaTeamMember, u_mes_qlt_capaContainmentAction, u_mes_qlt_capaCorrectiveAction, u_mes_qlt_capaImplementationAction, u_mes_qlt_capaControlledDocument, u_mes_qlt_auditFinding, u_mes_qlt_customerComplaint, u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_capa.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_capa.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_capa.js
