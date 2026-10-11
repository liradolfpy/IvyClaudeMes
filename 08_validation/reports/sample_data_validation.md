# Sample data validation

Run: 12 October 2026 | Tool: 05_generator/gen_samples.py | Collections: 299 | Documents: 2990

| # | Check | Scope | Result | Findings |
|---|---|---|---|---|
| 1 | Exactly 10 documents | all collections | Pass | 0 |
| 2 | Every document has a unique _id | all collections | Pass | 0 |
| 3 | _id is a 16-digit numeric string | all collections | Pass | 0 |
| 4 | No ObjectId | all collections | Pass | 0 |
| 5 | No nested documents or arrays | all collections | Pass | 0 |
| 6 | All schema keys present, no extra keys, same order | all collections | Pass | 0 |
| 7 | Data types match the schema | all collections | Pass | 0 |
| 8 | Required keys are not null | all collections | Pass | 0 |
| 9 | Values are in the allowed list | all collections | Pass | 0 |
| 10 | Status values are approved | all collections | Pass | 0 |
| 11 | ID and display pairs are complete | all collections | Pass | 0 |
| 12 | Every reference points to an existing document | all collections | Pass | 0 |
| 13 | Display value equals the referenced document's display value | all collections | Pass | 0 |
| 14 | Business numbers (recordNo) unique in the collection | all collections | Pass | 0 |
| 15 | Parent and line number unique in child collections | all collections | Pass | 0 |
| 16 | Audit keys valid (transaction collections only) | all collections | Pass | 0 |
| 17 | Dates in logical order | all collections | Pass | 0 |
| 18 | Dates inside 2018-2027 | all collections | Pass | 0 |
| 19 | Quantities not negative | all collections | Pass | 0 |

Shell format: every Int32 is written with NumberInt(), Int64 with NumberLong(), Decimal128 with NumberDecimal(), Double with Double(), dates with ISODate(); this is done by one formatting function for all files.

## Schema Observation

Nothing was added to or removed from any collection. These points were noticed while filling the documents and are reported only.

| # | Collection | Observation | What the samples do |
|---|---|---|---|
| 1 | u_mes_prod_recipe | recipeType has no allowed value for an assembly press program or a vision job | The recipes at those two positions are a second tightening program and a second laser marking layout; executions at the press and at final inspection carry no recipe |
| 2 | u_mes_plan_operationExecution | result is required, so an execution that is still running cannot be stored without a result | All ten executions are completed |
| 3 | u_mes_plan_container | ownerCustomerId is required, although in-plant trolleys and racks have no customer owner | All containers carry the customer of the part |
| 4 | u_mes_prod_operation, u_mes_prod_item | Exactly 10 documents: the eleventh operation (packing) and the items brake pad set and mounting bracket are not represented | Ten operations OP010 to OP100 and ten items |
| 5 | u_mes_prod_billOfMaterialComponent | The RH assembly BOM points to the LH body, because an RH body is not among the ten items | Left as is |
| 6 | all transaction collections | All documents belong to the Chakan plant; the other nine sites exist only in u_mes_mast_site | Plant is not varied in transactions, so that lines, work centers and equipment stay consistent with their site |

## How realistic the documents are

- Read through and corrected by hand: production orders, WIP units, operation executions, torque and leak results, lots, goods receipt lines, stock movements, inspection results, nonconformances, gauges, equipment, users, items, BOM components, routing steps, downtime events, serial numbers.
- Built by the same rules but not read line by line: the remaining collections. Their keys, types, references, allowed values and dates are checked by the table above; individual text or number combinations in them can still read oddly.
- Each collection has exactly ten documents, so stories are short: for example, ten leak tests are spread over four units.
