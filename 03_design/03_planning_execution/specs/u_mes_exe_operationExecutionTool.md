# u_mes_exe_operationExecutionTool

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | Links one operation execution to one tool; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_exe_operationExecution |
| _id pattern | <operationExecutionId>-T<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A operation execution can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. operationExecutionId and operationExecutionName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <operationExecutionId>-T<nnn> | `"OPX-20260929-000184-T001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000184-T001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | operationExecutionId | String | Yes | Reference to u_mes_exe_operationExecution._id: the parent document this one belongs to | `"OPX-20260929-000184"` | Reference: u_mes_exe_operationExecution._id |
| 6 | operationExecutionName | String | Yes | Display value of operationExecutionId, copied from u_mes_exe_operationExecution.recordNo | `"20260929-000184"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | toolId | String | Yes | Reference to u_mes_mnt_tool._id | `"TL-SKT-10-0007"` | Reference: u_mes_mnt_tool._id |
| 9 | toolName | String | Yes | Display value of toolId, copied from u_mes_mnt_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operationExecutionId: 1, toolId: 1 }` | Yes | One link per pair |
| 2 | `{ toolId: 1, operationExecutionId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_operationExecutionTool.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_operationExecutionTool.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_operationExecutionTool.js
