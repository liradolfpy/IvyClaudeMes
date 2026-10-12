# Specification check

Run: 11 October 2026 | Tool: 05_generator/gen_specs.py

| Item | Count |
|---|---|
| Collections specified | 343 |
| Keys specified | 7383 |
| Required (non-null) keys | 5837 |
| Keys that may be null | 1546 |
| Keys with allowed values | 439 |
| Indexes defined | 1324 |
| Files written (spec, validator, index script per collection, plus 10 module summaries) | 1039 |

## Example document (first sample document) checked against its own specification

The full check of all ten documents per collection is in sample_data_validation.md. Checks: every key present; value type equals the BSON type; a null only where null is allowed; a value from the allowed list where one is defined.

Result: all 343 sample documents pass.

## Not covered by this check

- Requiredness, allowed values and descriptions were produced from rules and dictionaries in 05_generator (keydict_text.py, keydict_num.py, gen_specs.py); they have not been reviewed collection by collection by a person.
- Validators have not been loaded into a MongoDB server in this run.
