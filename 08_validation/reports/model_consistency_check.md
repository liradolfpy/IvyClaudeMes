# Model consistency check

Run: 11 October 2026 | Input: 05_generator/model/flat_model.json | Tool: 05_generator/flatten_model.py

| Check | Scope | Result |
|---|---|---|
| Collection name matches u_mes_<3-letter module>_<lowerCamelCase singular> | 369 | Pass |
| Collection names unique | 369 | Pass |
| Key is lower camelCase with no dot, bracket, space or hyphen | 8245 | Pass |
| No key ends in Ids (no pluralised references) | 8245 | Pass |
| Every key ending in Id resolves to a collection in the inventory or is the polymorphic relatedEntityId | 2086 | Pass |
| Every reference Id is paired with its display key | 2086 | Pass |
| No duplicate key inside a collection | 369 | Pass |
| Every key has a concrete BSON type | 8245 | Pass |
| Audit keys present on all transaction collections and absent on all master collections | 369 | Pass |
| _id and recordNo present in every collection | 369 | Pass |

## Keys by BSON type

| BSON type | Keys |
|---|---|
| String | 6041 |
| Int32 | 927 |
| Date | 795 |
| Decimal128 | 281 |
| Boolean | 182 |
| Int64 | 15 |
| Double | 4 |

## Not checked yet

Requiredness, allowed values, descriptions and examples are not defined in the model yet, so they are not checked. BSON types were assigned by naming rules (documented in flatten_model.py) and need a read-through per collection when its specification is written.
