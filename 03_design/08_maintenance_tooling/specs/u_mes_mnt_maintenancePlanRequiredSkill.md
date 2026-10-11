# u_mes_mnt_maintenancePlanRequiredSkill

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | Links one maintenance plan to one required skill; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mnt_maintenancePlan |
| _id pattern | <maintenancePlanId>-RS<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A maintenance plan can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. maintenancePlanId and maintenancePlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <maintenancePlanId>-RS<nnn> | `"MP-PM-LKT-01-M-RS001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PM-LKT-01-M-RS001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | maintenancePlanId | String | Yes | Reference to u_mes_mnt_maintenancePlan._id: the parent document this one belongs to | `"MP-PM-LKT-01-M"` | Reference: u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String | Yes | Display value of maintenancePlanId, copied from u_mes_mnt_maintenancePlan.name | `"Leak tester monthly preventive maintenance"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | requiredSkillId | String | Yes | Reference to u_mes_mdm_skill._id: required skill | `"SKL-LEAK-TEST-OP"` | Reference: u_mes_mdm_skill._id |
| 9 | requiredSkillName | String | Yes | Display value of requiredSkillId, copied from u_mes_mdm_skill.name | `"Leak Test Operation"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ maintenancePlanId: 1, requiredSkillId: 1 }` | Yes | One link per pair |
| 2 | `{ requiredSkillId: 1, maintenancePlanId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_maintenancePlanRequiredSkill.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_maintenancePlanRequiredSkill.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_maintenancePlanRequiredSkill.js
