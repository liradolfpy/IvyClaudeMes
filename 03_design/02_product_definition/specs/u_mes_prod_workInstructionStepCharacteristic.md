# u_mes_prod_workInstructionStepCharacteristic

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Links one work instruction step to one characteristic; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_prod_workInstructionStep |
| _id pattern | <workInstructionStepId>-C<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A work instruction step can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. workInstructionStepId and workInstructionStepName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workInstructionStepId>-C<nnn> | `"WI-WI-OP070-001-S001-C001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP070-001-S001-C001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workInstructionStepId | String | Yes | Reference to u_mes_prod_workInstructionStep._id: the parent document this one belongs to | `"WI-WI-OP070-001-S001"` | Reference: u_mes_prod_workInstructionStep._id |
| 6 | workInstructionStepName | String | Yes | Display value of workInstructionStepId, copied from u_mes_prod_workInstructionStep.title | `"WI-OP070-001-S001"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | characteristicId | String | Yes | Reference to u_mes_qual_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qual_characteristic._id |
| 9 | characteristicName | String | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Piston bore diameter"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workInstructionStepId: 1, characteristicId: 1 }` | Yes | One link per pair |
| 2 | `{ characteristicId: 1, workInstructionStepId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstructionStepCharacteristic.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstructionStepCharacteristic.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_workInstructionStepCharacteristic.js
