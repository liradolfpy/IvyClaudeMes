# u_mes_qual_defectCodeApplicableOperation

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Links one defect code to one applicable operation; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_qual_defectCode |
| _id pattern | <defectCodeId>-AO<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A defect code can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. defectCodeId and defectCodeName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <defectCodeId>-AO<nnn> | `"DEF-LK01-AO001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LK01-AO001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | defectCodeId | String | Yes | Reference to u_mes_qual_defectCode._id: the parent document this one belongs to | `"DEF-LK01"` | Reference: u_mes_qual_defectCode._id |
| 6 | defectCodeName | String | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Leak at piston seal"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | applicableOperationId | String | Yes | Reference to u_mes_prod_operation._id: applicable operation | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 9 | applicableOperationName | String | Yes | Display value of applicableOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ defectCodeId: 1, applicableOperationId: 1 }` | Yes | One link per pair |
| 2 | `{ applicableOperationId: 1, defectCodeId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_defectCodeApplicableOperation.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_defectCodeApplicableOperation.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_defectCodeApplicableOperation.js
