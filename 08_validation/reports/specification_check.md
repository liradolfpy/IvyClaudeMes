# Specification check

Run: 11 October 2026 | Tool: 05_generator/gen_specs.py

| Item | Count |
|---|---|
| Collections specified | 299 |
| Keys specified | 6058 |
| Required (non-null) keys | 5011 |
| Keys that may be null | 1047 |
| Keys with allowed values | 350 |
| Indexes defined | 1078 |
| Files written (spec, validator, index script, sample per collection, plus 10 module summaries) | 1206 |

## Sample documents checked against their own specification

Checks: every key present; value type equals the BSON type; a null only where null is allowed; a value from the allowed list where one is defined.

Result: all 299 sample documents pass.

## Not covered by this check

- Reference values in sample documents are illustrative. That every reference points to an existing _id is checked on the seed data, where all collections are generated together.
- Requiredness, allowed values and descriptions were produced from rules and dictionaries in 05_generator (keydict_text.py, keydict_num.py, gen_specs.py); they have not been reviewed collection by collection by a person.
- Validators have not been loaded into a MongoDB server in this run.
