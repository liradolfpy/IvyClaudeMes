# u_mes_maint_maintenancePlanRequiredSkill

| Property | Value |
|---|---|
| Module | Tooling & Maintenance (maint) |
| Purpose | Links one maintenance plan to one required skill; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_maint_maintenancePlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A maintenance plan can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1218000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-GDC-01-M1-RS01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenancePlanId | String | - | Yes | Reference to u_mes_maint_maintenancePlan._id: the parent document this one belongs to | `"1216000000000001"` | Reference: u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String | - | Yes | Display value of maintenancePlanId, copied from u_mes_maint_maintenancePlan.name | `"Preventive maintenance, Gravity Die Casting Machine 1"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | requiredSkillId | String | - | Yes | Reference to u_mes_mast_skill._id: required skill | `"1031000000000001"` | Reference: u_mes_mast_skill._id |
| 9 | requiredSkillName | String | - | Yes | Display value of requiredSkillId, copied from u_mes_mast_skill.name | `"Gravity die casting operation"` |  |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, requiredSkillId: 1 }` | Yes | One link per pair |
| 2 | `{ requiredSkillId: 1, maintenancePlanId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_maintenancePlanRequiredSkill.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_maintenancePlanRequiredSkill.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_maintenancePlanRequiredSkill.js
