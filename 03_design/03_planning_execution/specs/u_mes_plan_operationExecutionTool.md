# u_mes_plan_operationExecutionTool

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Links one operation execution to one tool; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_plan_operationExecution |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 17 (17 required, 0 may be null) |

## Structure

Relationship collection. A operation execution can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. operationExecutionId and operationExecutionName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1092000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OPX-2026-000376-T01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id: the parent document this one belongs to | `"1090000000000001"` | Reference: u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000376"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | toolId | String | - | Yes | Reference to u_mes_maint_tool._id | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 10 | toolName | String | - | Yes | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 12 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:54:40.000+0000")` |  |
| 13 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 14 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 15 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:54:40.000+0000")` |  |
| 16 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 17 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ operationExecutionId: 1, toolId: 1 }` | Yes | One link per pair |
| 2 | `{ toolId: 1, operationExecutionId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_operationExecutionTool.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_operationExecutionTool.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_operationExecutionTool.js
