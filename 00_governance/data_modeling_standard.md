# Data modeling standard

Source: owner's requirements of 11 October 2026, with the project's own choices marked "Project choice" (each is recorded in `decision_log.md`). Rule identifiers DATA-001 and DATA-002 are the ones named in the requirements.

## 1. Collection names

- Format: `[Application]_[Module]_[Collection]` = `u_mes_<moduleCode>_<singularCollectionName>`.
- Application code (project prefix): `u_mes`.
- Module code: three lowercase letters. Project choice: mdm, prd, exe, mat, trc, qlt, eqp, mnt, sys, ehs (see `Folder_Guide.md` section 4).
- Collection part: lower camelCase, singular noun (`workOrder`, `workCenter`, `operation`), no spaces, hyphens or special characters.
- The name states the domain context and purpose. Vague names such as `data1` or `logs` are not used.
- Each business concept is one collection, even when several functional sections use it.

## 2. DATA-001 Flat documents

- The database is MongoDB but every collection is treated like a SQL table.
- Every value has its own top-level key. No embedded documents. No arrays. No nesting inside any value.
- A repeated value or a repeated association is stored as separate documents in its own collection, one document per occurrence. Project choice, three kinds:

| Kind | Used when | Name | Carries |
|---|---|---|---|
| Child | The parent has repeating lines with several attributes (order lines, routing steps) | parent entity + singular line noun, e.g. `u_mes_prd_routingStep` | parent reference pair, a line number, the line's keys |
| Relationship | One document must refer to several documents of another collection (many-to-many) | parent entity + role or target entity, e.g. `u_mes_mdm_workCenterEquipment` | parent reference pair, `sequenceNo`, one singular reference pair |
| Value list | The parent has several plain values of the same meaning | parent entity + singular value noun, e.g. `u_mes_mdm_rolePermission` | parent reference pair, `sequenceNo`, one value key |

- Multiplicity is never expressed by pluralising a scalar key. A key ending in `Ids` or `Names` is not allowed.
- Each key holds one value and has one purpose. No two keys with slightly different names hold the same information.

## 3. Key names

- Lower camelCase: first letter lowercase, each following word capitalised (`recordNo`, `relatedEntityName`, `createdAt`). The only exception is `_id`.
- No spaces, hyphens, punctuation or special characters.
- Clear, descriptive, established business terms, used the same way across the application.
- Singular nouns for a key that holds one value.
- One stable name per concept across all documents of a collection and across collections. Synonyms such as `recordNo`, `recordNumber`, `documentNo` for the same concept are not mixed.
- Vague names (`data`, `value`, `info`, `misc`) are not used unless the purpose is explicit from context and documented.
- Where a conventional name does not fit, use a clear descriptor (`relatedEntityDescription`, `salesOrderNo`).

## 4. Identifiers

- `_id`: unique identifier. Project choice: String, never ObjectId; entity collections use `<PREFIX>-<recordNo>`, child, relationship and value-list collections use `<parent _id>-<TAG><nnn>`. Patterns are in the register.
- `recordNo`: the separate business identifier. Project choice: present in every collection under this one name; what it holds for each collection is stated in the register.

## 5. References

- A reference is a pair of top-level keys: `<entity>Id` and `<entity>Name`. The entity stem is grammatically singular (`workOrderId` + `workOrderName`, `traceableEntityId`, never `workOrdersId`).
- `<entity>Name` holds the display value of the referenced document. Project choice: the target's `name`, else `title`, else `description`, else `recordNo`; the source key per collection is in `collection_inventory.md`.
- A role may prefix the stem (`fromStorageLocationId` + `fromStorageLocationName`).
- A reference to a user that records who did something uses `<action>ById` + `<action>By` (`approvedById` + `approvedBy`), the same pattern as the audit keys.
- A reference that may point to different collections uses three keys: `relatedCollectionName`, `relatedEntityId`, `relatedEntityName`.
- Display values that refer to the same entity are identical wherever they appear.
- `siteId` + `siteName` are in every collection except `u_mes_mdm_site`.

## 6. Status

- `status` is the document's primary lifecycle state, used only when the collection has one.
- Each collection defines its own values. Values are readable words in Title Case with spaces (`In Progress`), one spelling per state; forms such as `InProgress`, `in_progress`, `In-Progress` are not mixed.
- Status values are mapped in a separate collection: `u_mes_sys_statusDefinition` (one document per collection and value) and `u_mes_sys_statusTransition` (allowed moves). The values are listed in `04_reference_data/code_lists/status_values.md`.
- A second state that is not the lifecycle keeps its own descriptive key (`qualityStatus`, `stockStatus`, `connectionStatus`).

## 7. Dates and times

- Event timestamps end in `At` (`createdAt`, `approvedAt`, `completedAt`). Calendar dates end in `Date` or use `validFrom`, `validTo`, `effectiveFrom`, `effectiveTo`.
- All are BSON dates, stored in UTC. Never strings.

## 8. DATA-002 Numeric and other types

Every numeric key has one concrete BSON type, stated in the field lists.

| BSON type | Used for |
|---|---|
| Int32 | Ordinary counts, piece quantities, line and step numbers, durations in minutes or seconds, versions |
| Int64 | Lifetime counters, number-range values, file sizes |
| Decimal128 | Measurements, tolerances, material quantities with fractions, percentages, money (project choice, from the original brief) |
| Double | Only keys specified as Double: `geoLatitude`, `geoLongitude`, `tagValue`, `powerFactor` |
| String | Names, descriptions, status values, business numbers, IDs |
| Boolean | True/false attributes |
| Date | All dates and timestamps |
| null | Only when a value is genuinely unavailable |

Numeric quantities are never stored as strings.

## 9. Audit keys - transaction collections only

| Key | Meaning |
|---|---|
| createdAt | Date and time the document was created |
| createdById | ID of the user or process that created it |
| createdBy | Display name of the creator |
| updatedAt | Date and time of the most recent update |
| updatedById | ID of the user or process that last updated it |
| updatedBy | Display name of the updater |

Master collections do not carry these keys; their change history is in `u_mes_sys_auditTrail`. The data class of each collection (master or transaction) is in `collection_inventory.md`. A child, relationship or value-list collection has the data class of its parent.

## 10. Optional keys

An optional key is handled the same way in every document of a collection: either always present with `null` when unavailable, or defined as optional in the collection specification. Project choice: always present, `null` when unavailable, so that every document of a collection has the same keys.
