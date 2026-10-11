# MongoDB output rules

Source: owner's requirements of 11 October 2026.

## 1. MongoDB shell output (sample documents, seed .js files)

| BSON type | Write as | Example |
|---|---|---|
| Date | `ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000")` | `ISODate("2026-09-28T00:30:00.000+0000")` |
| Int32 | `NumberInt(n)` | `NumberInt(240)` |
| Int64 | `NumberLong("n")` | `NumberLong("1250000")` |
| Double | `Double(n)`, also for whole numbers | `Double(18)`, `Double(18.5204)` |
| Decimal128 | `NumberDecimal("n")` with the value as a string, so no binary rounding occurs | `NumberDecimal("14.20")` |
| Boolean | `true` / `false` | `true` |
| String | double-quoted text | `"In Progress"` |
| null | `null` | `null` |

- Constructors are executable and are never placed inside quotes.
- IDs, booleans, nulls, text and dates match the collection specification exactly: type, requiredness, status values and reference rules.
- Dates are never written as strings.
- IST times are converted to UTC before writing (IST = UTC + 05:30).

## 2. Other output formats

- BSON files (`06_seed_data/bson`): native BSON types, written with the `bson` package; one file per collection named `<collection name>.bson`, concatenated documents (mongodump format).
- Extended JSON (`06_seed_data/extended_json`): canonical Extended JSON v2 (`$date`, `$numberInt`, `$numberLong`, `$numberDouble`, `$numberDecimal`).
- JSON Schema validators: `bsonType` names `string`, `date`, `int`, `long`, `double`, `decimal`, `bool`, `null`.

## 3. Sample documents

No sample document is produced for a collection until its field-level specification exists and has passed `schema_review_checklist.md`.
