# u_mes_syst_interlockRule

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Configured check that the application must pass before a transaction is allowed, with its scope and override policy. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 28 (15 required, 13 may be null) |
| Estimated volume per year | about 400 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per interlock rule, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1332000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ILR-HOLD-001"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Rule name | `"Hold check at operation start"` |  |
| 6 | ruleType | String | - | Yes | Check type | `"Hold Check"` | Hold Check; Sequence Check; Mandatory Scan; Duplicate Serial; Wrong Order; Wrong Station; Variant Check; Component Lot Capture; Lot Release Check; Expiry Check; Kit Completeness; Genealogy Completeness; Recipe Release Check; Program Version Check; Work Instruction Release Check; Acknowledgement Check; Mandatory Inspection; NOK Result; Skill Check; Login Check; Equipment Readiness; Tool Life; Calibration Check; Environment Check; Setup Check; Alarm Restart |
| 7 | transactionPoint | String | - | Yes | Where the check runs | `"Operation Start"` | Operation Start; Operation Complete; Material Issue; Kit Release; Pack Out; Dispatch; Order Close; Login; Inspection Accept |
| 8 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `null` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `null` |  |
| 10 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `null` | Reference: u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `null` |  |
| 12 | operationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id | `null` | Reference: u_mes_prod_operation._id |
| 13 | operationName | String | - | No (null allowed) | Display value of operationId, copied from u_mes_prod_operation.name | `null` |  |
| 14 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `null` | Reference: u_mes_prod_item._id |
| 15 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `null` |  |
| 16 | enforcementMode | String | - | Yes | Warning only, or block the transaction | `"Block"` | Warning; Block |
| 17 | overrideAllowed | Boolean | - | Yes | Override permitted | `false` |  |
| 18 | overrideRoleId | String | - | No (null allowed) | Reference to u_mes_mast_role._id: override role | `null` | Reference: u_mes_mast_role._id |
| 19 | overrideRoleName | String | - | No (null allowed) | Display value of overrideRoleId, copied from u_mes_mast_role.name | `null` |  |
| 20 | overrideRequiresSignature | Boolean | - | Yes | Override needs an electronic signature | `false` |  |
| 21 | overrideRequiresReasonCode | Boolean | - | Yes | Override needs a reason code | `false` |  |
| 22 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000004"` | Reference: u_mes_syst_escalationRule._id |
| 23 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Interlock block not cleared"` |  |
| 24 | messageText | String | - | Yes | Operator message | `"Unit, lot or order is on quality hold; operation not allowed"` |  |
| 25 | validFrom | Date | Date | Yes | Valid from | `ISODate("2026-04-01T00:00:00.000+0000")` |  |
| 26 | validTo | Date | Date | No (null allowed) | Valid to | `null` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 7 | `{ overrideRoleId: 1 }` | No | Look-up of documents by override role |

## Referenced by

u_mes_plan_interlockEvent.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_interlockRule.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_interlockRule.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_interlockRule.js
