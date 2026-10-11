# Schema review and naming checklist

Run before accepting a document or generating sample or seed data. Record the result in `08_validation/reports`.

## A. Schema review

| # | Check |
|---|---|
| A1 | All documents in the collection use the same key spelling and casing for the same concept |
| A2 | `_id` is unique and matches the pattern in the register; `recordNo` is present as the separate business identifier |
| A3 | Every reference ID has its paired display key, including the audit references |
| A4 | Display values that refer to the same entity are identical everywhere |
| A5 | Date, numeric, string, Boolean and null values use the BSON type in the field list |
| A6 | The document is flat: no embedded objects, no arrays |
| A7 | Optional keys are handled the same way across documents (present, `null` when unavailable) |
| A8 | `status`, when present, holds a value listed for that collection in `status_values.md` |
| A9 | Audit keys are present on transaction collections and absent on master collections |
| A10 | Every reference ID points to an `_id` that exists in the target collection |
| A11 | Dates fall inside the production timeline and are in a possible order |
| A12 | No classification is held as free text: each one is either a master reference (ID plus display key) or a fixed enumeration with its values in `enumeration_values.md` |

## B. Naming checklist for every new key

| # | Question |
|---|---|
| B1 | Is the name clear and lower camelCase? |
| B2 | Does it use the collection's established terminology? |
| B3 | If it is a reference ID, is the corresponding name or description key also present? |
| B4 | Does the BSON type match the value being stored? |
| B5 | Is the key consistent with the same concept in other documents and collections? |
| B6 | Is the key necessary and limited to one clear purpose? |
| B7 | If the key classifies the document, has DATA-003 been applied: master collection (rule A) or fixed enumeration (rule B)? |

## C. Naming checklist for every new collection

| # | Question |
|---|---|
| C1 | Does the name follow `u_mes_<moduleCode>_<singularCollectionName>`? |
| C2 | Is the business concept not already held by another collection? |
| C3 | Is the data class (master or transaction) decided and recorded in the inventory? |
| C4 | If it has a lifecycle, are its status values defined in `status_values.md`? |
| C5 | Does every master list the collection uses exist as its own collection in the inventory? |
