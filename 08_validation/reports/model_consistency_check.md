# Model consistency check

Run: 11 October 2026 | Input: 05_generator/model/flat_model.json | Tool: 05_generator/flatten_model.py

| Check | Scope | Result |
|---|---|---|
| Collection name matches u_mes_<3-letter module>_<lowerCamelCase singular> | 257 | Pass |
| Collection names unique | 257 | Pass |
| Key is lower camelCase with no dot, bracket, space or hyphen | 5553 | Pass |
| No key ends in Ids (no pluralised references) | 5553 | Pass |
| Every key ending in Id resolves to a collection in the inventory or is the polymorphic relatedEntityId | 1362 | Pass |
| Every reference Id is paired with its display key | 1362 | Pass |
| No duplicate key inside a collection | 257 | Pass |
| Every key has a concrete BSON type | 5553 | Pass |
| Audit keys present on all transaction collections and absent on all master collections | 257 | Pass |
| _id and recordNo present in every collection | 257 | Pass |

## Keys by BSON type

| BSON type | Keys |
|---|---|
| String | 4027 |
| Int32 | 654 |
| Date | 549 |
| Decimal128 | 196 |
| Boolean | 110 |
| Int64 | 13 |
| Double | 4 |

## Not checked yet

Requiredness, allowed values, descriptions and examples are not defined in the model yet, so they are not checked. BSON types were assigned by naming rules (documented in flatten_model.py) and need a read-through per collection when its specification is written.
