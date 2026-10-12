# Data modeling standard

Source: owner's requirements of 11 October 2026, with the project's own choices marked "Project choice" (each is recorded in `decision_log.md`). Rule identifiers DATA-001 and DATA-002 are the ones named in the requirements.

## 1. Collection names

- Format: `[Application]_[Module]_[Collection]` = `u_mes_<moduleCode>_<singularCollectionName>`.
- Application code (project prefix): `u_mes`.
- Module code: four or five lowercase letters, fixed by the owner on 11 October 2026: mast (Master Data Management), prod (Product Definition), plan (Planning and Execution), matl (Material Management), trac (Traceability), qual (Quality Management), perf (Performance Management), maint (Tooling & Maintenance), syst (System and Integration), ehs (Environment Health and Safety). See `Folder_Guide.md` section 4.
- Collection part: lower camelCase, singular noun (`workOrder`, `workCenter`, `operation`), no spaces, hyphens or special characters.
- The name states the domain context and purpose. Vague names such as `data1` or `logs` are not used.
- Each business concept is one collection, even when several functional sections use it.

## 2. DATA-001 Flat documents

- The database is MongoDB but every collection is treated like a SQL table.
- Every value has its own top-level key. No embedded documents. No arrays. No nesting inside any value.
- A repeated value or a repeated association is stored as separate documents in its own collection, one document per occurrence. Project choice, three kinds:

| Kind | Used when | Name | Carries |
|---|---|---|---|
| Child | The parent has repeating lines with several attributes (order lines, routing steps) | parent entity + singular line noun, e.g. `u_mes_prod_routingStep` | parent reference pair, a line number, the line's keys |
| Relationship | One document must refer to several documents of another collection (many-to-many) | parent entity + role or target entity, e.g. `u_mes_mast_workCenterEquipment` | parent reference pair, `sequenceNo`, one singular reference pair |
| Value list | The parent has several plain values of the same meaning | parent entity + singular value noun, e.g. `u_mes_mast_rolePermission` | parent reference pair, `sequenceNo`, one value key |

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

- `_id`: unique system identifier. A String of exactly 16 digits (for example `1090000000000003`), never ObjectId and never a UUID. The first four digits are the collection number, the last twelve a running number. An external system's identifier is never used as `_id`; it is kept in its own key (for example `erpOrderNo`, `erpMaterialNo`).
- `recordNo`: the separate business identifier. Project choice: present in every collection under this one name; what it holds for each collection is stated in the register.

## 5. References

- A reference is a pair of top-level keys: `<entity>Id` and `<entity>Name`. The entity stem is grammatically singular (`workOrderId` + `workOrderName`, `traceableEntityId`, never `workOrdersId`).
- `<entity>Name` holds the display value of the referenced document. Project choice: the target's `name`, else `title`, else `description`, else `recordNo`; the source key per collection is in `collection_inventory.md`.
- A role may prefix the stem (`fromStorageLocationId` + `fromStorageLocationName`).
- A reference to a user that records who did something uses `<action>ById` + `<action>By` (`approvedById` + `approvedBy`), the same pattern as the audit keys.
- A reference that may point to different collections uses three keys: `relatedCollectionName`, `relatedEntityId`, `relatedEntityName`.
- Display values that refer to the same entity are identical wherever they appear.
- `siteId` + `siteName` are in every collection except `u_mes_mast_site`.

## 6. Status

- `status` is the document's primary lifecycle state, used only when the collection has one.
- Each collection defines its own values. Values are readable words in Title Case with spaces (`In Progress`), one spelling per state; forms such as `InProgress`, `in_progress`, `In-Progress` are not mixed.
- Status values are mapped in a separate collection: `u_mes_syst_statusDefinition` (one document per collection and value) and `u_mes_syst_statusTransition` (allowed moves). The values are listed in `04_reference_data/code_lists/status_values.md`.
- A second state that is not the lifecycle keeps its own descriptive key (`qualityStatus`, `stockStatus`, `connectionStatus`).

## 7. DATA-004 Dates and times (local plant time)

Source: owner's instruction of 12 October 2026.

- Every date and time is stored as a BSON date, never as a string.
- The value is the **local plant time (IST)**, written with the `+0000` suffix, **without converting to UTC**. The stored digits are what the clock on the shop floor showed. Example: 8 October 2026, 00:00 IST is stored as `ISODate("2026-10-08T00:00:00.000+0000")`, not as `2026-10-07T18:30:00.000+0000`. A shift starting at 06:00 IST is stored as `T06:00:00.000+0000`.
- Every date key carries a tag in the key design (field lists, collection keys and specifications):

| Tag | Holds | Stored as | Key name |
|---|---|---|---|
| Date | A calendar date with no time of day (due dates, validity dates, holidays, production dates) | 00:00:00.000 of that day | Ends in `Date`, or is one of `validFrom`, `validTo`, `effectiveFrom`, `effectiveTo`, `horizonFrom`, `horizonTo` |
| Datetime | A moment at which something happened or is planned to happen | The local time to the second (milliseconds .000 unless measured) | Ends in `At` |

- A new date key is tagged when it is created; the tag is part of its specification and decides how sample data and application code fill it.
- An end-of-validity date (`validTo`, `effectiveTo`) is the last day on which the record is valid, stored as 00:00:00 of that day.
- Keys that are named with `At` but hold a calendar date (for example `nextDueAt`, `nextCalibrationDueAt`, `expiryAt`) are tagged Date. They are listed in `decision_log.md` (D035) as candidates for renaming to `…Date`; until then the tag, not the name, decides the format.
- If the plant time zone ever has to be shown in UTC, the application converts on display; the stored value stays local.

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

Master collections do not carry these keys; their change history is in `u_mes_syst_auditTrail`. The data class of each collection (master or transaction) is in `collection_inventory.md`. A child, relationship or value-list collection has the data class of its parent.

## 10. Optional keys

An optional key is handled the same way in every document of a collection: either always present with `null` when unavailable, or defined as optional in the collection specification. Project choice: always present, `null` when unavailable, so that every document of a collection has the same keys.

## 11. DATA-003 Classification values and master data

Source: owner's review of 11 October 2026 (the user document held department, designation and employmentType as plain text with no ID and no master collection).

A text key that classifies a document is never left as free text. It is handled by one of two rules.

| Rule | Applies when | Modelled as | Example |
|---|---|---|---|
| A. Master collection | The plant defines and maintains the list, the list can grow, or a value has attributes of its own | Its own master collection `u_mes_<moduleCode>_<singularName>` with `_id`, `recordNo` (the code), `name`, `description`, `sequenceNo`, `status`; referenced by `<entity>Id` + `<entity>Name` | `departmentId` + `departmentName` pointing to `u_mes_mast_department` |
| B. Fixed enumeration | The values are fixed by the application logic and the plant cannot add one without a software change | The key stays coded text; its allowed values are in the validator, listed in `04_reference_data/code_lists/enumeration_values.md`, and stored as data in `u_mes_syst_enumerationValue` (one document per collection, key and value) | `result` with OK, Not OK |

How to decide: if a plant administrator could reasonably need to add, rename or retire a value, it is rule A. If the software branches on the value, it is rule B.

Further rules:

- The same list is one master collection, however many keys use it. A role may prefix the reference (`responsibleDepartmentId`, `fromStockStatusId`, `defaultDispositionTypeId`).
- Where one document needs several values from a master list, the link is a relationship collection (`u_mes_mast_rolePermission` links a role to `u_mes_mast_permission`).
- A master collection of this kind is data class master: no audit keys, change history in `u_mes_syst_auditTrail`.
- Text that describes one person or thing outside the plant's lists stays text under a name that cannot be mistaken for a reference (`jobTitle` of a customer contact, not `designation`).
- Free text is allowed only for names, descriptions, notes, numbers issued by other parties, and technical addresses.
- `status` follows section 6 and is mapped in `u_mes_syst_statusDefinition`.

## 12. Enforcement, evidence and analytics records

Source: MES_ExternalRequirement_01 (owner decision of 12 October 2026, D036-D042).

- A rule that the application enforces is configured in a master collection and every execution of the rule leaves a transaction record. Interlocks: `u_mes_syst_interlockRule` and `u_mes_plan_interlockEvent`. Escalation: `u_mes_syst_escalationRule` with `u_mes_syst_escalationRuleLevel`. Threshold alerts: `u_mes_syst_alertRule`, raising `u_mes_syst_notification`. Role authorisation of status changes: `u_mes_syst_statusTransitionRole`.
- An override of an interlock carries a reason code (`u_mes_perf_reasonCode`, reasonType Interlock Override), the user (`overrideById` + `overrideBy`), the time and, when the rule requires it, an electronic signature.
- Station evidence is recorded as its own transaction: operator login (`u_mes_plan_operatorSession`), document acknowledgement (`u_mes_plan_documentAcknowledgement`), program load (`u_mes_plan_recipeDownload`), set-up verification (`u_mes_plan_setupVerification` + `u_mes_plan_setupVerificationItem`).
- Curve data: one document per captured curve in `u_mes_qual_measurementCurve` with the envelope verdict; the points go to the time-series collection `u_mes_qual_measurementCurvePoint` (timeField `sampledAt`, metaField `measurementCurveId`). Like the other time-series collections, it cannot carry a JSON Schema validator; its validator file is the rule the application enforces.
- AI / ML and rule models are registered with their version in `u_mes_syst_analyticsModel`; every prediction, classification or recommendation is stored in `u_mes_syst_modelPrediction` with the model version used.
- Edit, lock and retention behaviour per collection is configured in `u_mes_syst_recordPolicy`. Transaction data is not physically deleted.
- New collections are numbered after the last existing collection; existing numbers never change.

## 13. One key name, one BSON type

A key name has the same BSON type in every collection where it appears. flatten_model.py lists any key with more than one type. Documented exception: `quantity` is Int32 for countable units and Decimal128 for material quantities. A new key that would clash takes a more specific name (for example `severityClass` for a Low-Critical scale, because `severity` is an Int32 rating).
