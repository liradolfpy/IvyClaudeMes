# Query Control Instruction

Instruction version: 0.2 | 13 October 2026 | Model version 2.9 (369 collections) plus `u_int_mdict`
Status: working instruction, refined regularly. Every refinement raises the version, adds a row to the change log (section 17), moves answered questions to section 15 and adds new questions to section 14.
Location: `04_reference_data/ui_controls/query_control_instruction.md`, next to the control samples it governs (`04_reference_data/ui_controls/query/`).

## 1. Purpose

This instruction gives one repeatable method for deciding the **query controls** of every list screen in the MES React application: which controls appear, which type each one is, where its values come from, how each attribute is set, and what the page's backend code receives.

Apply it to every collection that has a list screen. The result for each collection is one `modalElements` array inside the page configuration document served by `/miscellaneous/pageconfig`.

It builds on two earlier project documents:

- `02_architecture/QueryKeySelectionStrategy.md`: which keys may be queried and indexed;
- the grouping strategy agreed on 12 October 2026: screens filter by groups (scope, period, status, category), not by individual documents. A single document is opened only by selecting a row from the list.

## 2. How the query form works

| Step | What happens |
|---|---|
| 1 | The screen loads and calls `GET /miscellaneous/pageconfig` for its page. |
| 2 | The response is a page configuration document (sample: `query/FormatQuery.json`). Its `dictData.config.modalElements` array lists the query controls in display order. |
| 3 | The React app renders each element by its `typ`, loads its values from the source given by `src` (`api` or `data`), adds `ALL` as the first value when `includeAll` is true, and applies the default. |
| 4 | The user changes the selections and submits. The app checks the controls with `required: true` and shows `errorMessage` for any that is empty. |
| 5 | The app builds the payload: every control writes its selected value under its `data_index`; dropdowns also write the display text under `p_din`; range pickers write the two dates under `din_from` and `din_to`. Controls hidden by RBAC (`visible: false`) still send their default value. |
| 6 | The page's own backend code (each page has its own code) turns the payload into a MongoDB filter, following section 9. A value of `all` means "do not filter on this key". |

## 3. Inputs

| Input | Location | Used for |
|---|---|---|
| Collection keys | `02_architecture/collection_keys.md` | Exact key names for `data_index` and `p_din` |
| Collection type matrix | `02_architecture/collection_type_matrix.md` | Master or Transaction, screen label |
| Collection inventory | `02_architecture/collection_inventory.md` | Kind and display key of each collection |
| Field lists and specifications | `02_architecture/field_lists`, `03_design/<module>/specs` | BSON type, allowed values, reference target of each key |
| Status values | `04_reference_data/code_lists/status_values.md` | Status dropdown values |
| Enumeration values | `04_reference_data/code_lists/enumeration_values.md` | Allowed values of category keys |
| Query key strategy | `02_architecture/QueryKeySelectionStrategy.md` | Which keys are query keys; index alignment |
| Control sample | `04_reference_data/ui_controls/query/FormatQuery.json` | Control syntax |
| Cropdown sample | `04_reference_data/ui_controls/query/cropdown.md` | Existing custom dropdown lists |
| Legacy mdict sample | `04_reference_data/ui_controls/query/mdict.json` | Format of the application's MasterDict (data belongs to another application; not used for MES) |
| MES MasterDict | `04_reference_data/ui_controls/query/u_int_mdict.json` | MES dictionaries served by `/mdict` (section 11) |
| `/dd` authorised list | Flask backend code (not in this repository) | Collections allowed for dynamic dropdowns |

## 4. Control catalogue

| Control | `typ` | `src` | Values come from | Use when |
|---|---|---|---|---|
| Date picker | `datePicker` | – | Calendar | One single date is needed (for example one shift report). Use only when a range makes no sense. |
| Range picker | `rangePicker` | – | Calendar | A period is needed. **Preferred over the date picker** and present on every transaction list screen. |
| Hard-coded dropdown | `dropDown` | `data` | The `data` object in the control | The values never change without a software release and there are 10 or fewer. Also used for an optional Boolean filter (section 5, step 3). |
| Cropdown (custom dropdown) | `dropDown` | `api`, `api: "/cropdown"` | One document of the `cropdown` collection, chosen by `params.name` | A small custom list that is not a collection of the data model, is shared by several pages and may be changed by an administrator without a release. **10 values or fewer per cropdown document**; a longer list becomes a proper collection. |
| Mdict (MasterDict) | `dropDown` | `api`, `api: "/mdict"` | The cache, filled from `u_int_mdict`, chosen by `params.typ` (the `dictName`) and `params.subTyp` (`idame`) | Master data listed in section 11: at most 200 documents in the source collection and frequently used. Only master data. |
| Dynamic dropdown | `dropDown` | `api`, `api: "/dd"` | The collection named in `params.dn`, which must be registered in the Flask code | Master data that is not in mdict and has 500 documents or fewer. |
| Dynamic search dropdown | `dropDown` | `api`, `api: "/dd"`, with `minSearchLength` and `maxSearchLength` | Same as dynamic dropdown, queried with `$regex` on the typed text | Data that exceeds 500 documents or is expected to grow past 500. |
| Radio | `radio` | `data` | The `data` object in the control | A mandatory choice between two to four exclusive options shown side by side, including a mandatory true / false choice. **Radio has no "All" option.** |

## 5. Procedure for one collection

### Step 1: Write the query profile

From `collection_keys.md` and the query key strategy, write down for the collection:

| Profile item | Question | Example for `u_mes_plan_andonEvent` |
|---|---|---|
| Time key | Which single date or datetime key places the record in time? | `raisedAt` [Datetime] |
| Scope keys | Which plant-hierarchy keys does it hold (area, line, work centre, equipment, storage location)? | `lineId`, `workCenterId`, `equipmentId` |
| Shift key | Does it hold `shiftId`? | `shiftId` |
| Status key | Does it hold `status` with a lifecycle? | `status`: Raised, Acknowledged, Resolved, Cancelled |
| Category keys | Which classification keys do users group by? | `andonTypeId`, `reasonCodeId`, `severityClass` |
| Boolean keys | Which flags do users filter on? | `lineStopped` |

### Step 2: Choose the controls

Take the profile items in this order and stop at **8 controls** (aim for 6):

| Order | Control | Rule |
|---|---|---|
| 1 | Period | Mandatory on Transaction, Reports, Telemetry and Audit Trail screens. Range picker on the time key. Not used on Master screens. |
| 2 | Scope | Mandatory on Transaction screens when the collection holds a scope key. Highest useful level first (Line), then the next level (Work Center). At most two scope levels. Scope dropdowns are independent: there is no cascading (choosing a line does not narrow the work-centre list). |
| 3 | Shift | When the collection holds `shiftId` and users read it per shift. |
| 4 | Status | When the collection has a lifecycle status. |
| 5 | Category | One or two category keys that users group by. |
| 6 | Boolean | Only flags that users filter on regularly. |
| – | Never a control | `siteId` (taken from the login session, see Q13), `_id`, `recordNo` (records are opened from the list), any `...Name` key, measured values, free text, audit stamps (`createdAt`, `updatedBy` and the like). |

Rules:

- A key becomes a control only if it is a query key under the query key strategy (it is in an index or is applied on top of an indexed filter).
- Do not add a control to select one transaction document (one production order, one lot, one serial number). Group filters are used instead. Searching by business number is open (Q15, Q16).

### Step 3: Choose the control type

| Key | Control type |
|---|---|
| Time key, period needed | `rangePicker` |
| Time key, one day only | `datePicker` |
| Reference key (`...Id`) | `dropDown` |
| Status or category text key with allowed values | `dropDown` |
| Boolean key, optional filter (user may want both values) | `dropDown`, `src: "data"`, `data: { "true": "Yes", "false": "No" }`, `includeAll: true` |
| Boolean key, the user must always choose one value | `radio`, `data: { "true": "Yes", "false": "No" }` |
| Mandatory choice between two to four exclusive options that the user should see at once | `radio` |

Boolean values are always sent as the strings `"true"` and `"false"`; the backend converts them to BSON Boolean.

### Step 4: Choose the source of a dropdown

Answer the questions in order; the first "yes" decides.

| # | Question | Source |
|---|---|---|
| 1 | Is the key a status, Boolean or allowed-value key whose values are fixed by the data model (`status_values.md`, `enumeration_values.md`) and are there 10 or fewer values? | `src: "data"` (hard-coded). The `data` keys are exactly the values stored in the collection. |
| 2 | Is it a small custom list (10 or fewer values) that is not a collection of the data model, is shared by several pages, and may be changed by an administrator without a release? | `/cropdown` |
| 3 | Does the key reference a master collection that has a dictionary in `u_int_mdict` (section 11)? | `/mdict` |
| 4 | Does the key reference a collection that holds 500 documents or fewer? | `/dd` (register the collection in the Flask code if it is not registered) |
| 5 | Does it hold more than 500 documents, or is it expected to grow past 500? | `/dd` with `minSearchLength` and `maxSearchLength` (search dropdown) |
| 6 | None of the above | Do not create the control; raise it as a question (section 14) |

Placement of model collections used in query controls:

| Model collection | Expected documents per site | Source | `params` |
|---|---|---|---|
| Masters listed in section 11.3 | 200 or fewer | `/mdict` | `{ typ: "<dictName>", subTyp: "idame" }` |
| `u_mes_mast_user` (operators, supervisors, any `...ById` or `...UserId` key) | about 600 | `/dd` search | `{ dn: "u_mes_mast_user" }` |
| `u_mes_matl_storageLocation` | more than 200 bins | `/dd` search | `{ dn: "u_mes_matl_storageLocation" }` |
| `u_mes_maint_tool` | about 300 | `/dd` search | `{ dn: "u_mes_maint_tool" }` |
| `u_mes_qual_gauge` | about 250 | `/dd` search | `{ dn: "u_mes_qual_gauge" }` |
| `u_mes_qual_characteristic` | more than 200, grows with each item | `/dd` search | `{ dn: "u_mes_qual_characteristic" }` |
| `u_mes_maint_sparePart`, `u_mes_perf_processTag` | more than 500 | `/dd` search | `{ dn: "<collection>" }` |
| `u_mes_prod_recipe`, `u_mes_syst_iotDevice`, `u_mes_prod_routing`, `u_mes_qual_controlPlan`, `u_mes_qual_inspectionPlan`, `u_mes_qual_checkSheet`, `u_mes_maint_maintenancePlan` | 500 or fewer, not frequently used as a filter | `/dd` | `{ dn: "<collection>" }` |
| Status of any collection | 3 to 8 values | `data` | values from `status_values.md` |
| Shift | – | `/mdict` `Shift`, **not** the cropdown `Shift` document | – |

### Step 5: Set the attributes

Use section 6 for every attribute. The most important rules:

- `data_index` is the **exact key name in the collection** (`lineId`, `status`, `raisedAt`). Each page has its own backend code, so this is a naming standard rather than a technical need: it keeps page code, payload and indexes readable side by side.
- `p_din` is the **matching display key** of the model (`lineName` for `lineId`, following the Id/Name pairing of `collection_keys.md`). For a `data` or cropdown source on a text key, `p_din` is the key name followed by `Text` (for example `statusText`), because the model has no separate name key for it.
- `includeAll: true` and `default: "all"` (single) or `default: ["all"]` (multi) on every optional dropdown filter.
- `required: true` makes the control mandatory. Use it on the period control and on any control whose absence would make the query unbounded.

### Step 6: Check the payload and the filter

Write the example payload and the resulting MongoDB filter for the screen (section 9) and confirm that the filter is served by an index from the query key strategy.

### Step 7: Run the checklist

Section 12.

## 6. Attribute reference

| Attribute | Applies to | Meaning | Rule in this project |
|---|---|---|---|
| `typ` | all | Control type | One of `datePicker`, `rangePicker`, `dropDown`, `radio` |
| `label` | all | Text shown next to the control | Title Case, the business name of the key as used in the screen label of `collection_type_matrix.md`, singular, 25 characters or fewer (for example `Work Center`, `Andon Type`, `Raised Between`) |
| `placeHolder` | all except radio | Hint text inside the control | `Select <label>` for dropdowns and pickers; for the search dropdown `Type <maxSearchLength> characters of <label>` |
| `errorMessage` | all with `required: true` | Message when a mandatory control is empty at submit | `Please select <label>` |
| `required` | all | `true`: the control is mandatory; `false`: optional | `true` on the period control and on radios; `false` on optional dropdowns. A dropdown with `includeAll` and default `all` is always filled, so `required: true` on it only stops the user from clearing it. |
| `default` | dropDown, radio, datePicker | Value selected when the form opens | Dropdown single: `"all"`; multi: `["all"]`; status on work-list screens: the open statuses as an array; radio: one of its `data` keys; datePicker: day offset from today as `NumberInt` (`0` = today, `-1` = yesterday) |
| `defaultFrom`, `defaultTo` | rangePicker | Initial range | Day offsets from today as `NumberInt` (`0` = today, `-30` = 30 days ago). Standard: live screens `0` / `0`; operational lists `-7` / `0`; history and reports `-30` / `0` |
| `format` | datePicker, rangePicker | Display and payload date format | `YYYY-MM-DD` |
| `din_from`, `din_to` | rangePicker | Payload keys of the two dates | `from` and `to` (as in the sample); payload shape open (Q4) |
| `includeAll` | dropDown | The app adds `{ "all": "ALL" }` as the first value; `all` tells the backend not to filter on this key | `true` on every optional filter; `false` only when one value must always be chosen. Not available on radio. |
| `multiSelect` | dropDown | Several values can be selected | Exceptional. Allowed for status and for one scope or category key per screen. `default` must then be an array. |
| `readOnly` | all | Shown but not editable | Exceptional: a value fixed by the page or role, for example the line of a line-supervisor screen |
| `visible` | all | Whether the control is shown | `true` by default; `false` when RBAC must stop a role from changing the filter. A hidden control still sends its default value, so its default must be the value that role is allowed to see. |
| `colSize` | all | Width of the control on a 24-column grid | Standard `8` (three controls per row). Never above `8` except a single wide control on its own row. The sample's `12` (two per row) is not used for MES pages. |
| `labelColSpan` | all | Width of the label of the control | Standard `8`; never above `8` (meaning of the base open, Q2b) |
| `data_index` | all | Payload key that receives the selected value | Exact key name of the collection (`raisedAt`, `lineId`, `status`, `lineStopped`) |
| `p_din` | dropDown | Payload key that receives the display text of the selected value | Display key of the model (`lineName`); `<key>Text` for keys without a name key |
| `api` | dropDown with `src: "api"` | Endpoint | `/cropdown`, `/mdict` or `/dd` |
| `params` | dropDown with `src: "api"` | Selector of the list | `/cropdown`: `{ name }`; `/mdict`: `{ typ, subTyp }`; `/dd`: `{ dn }` where `dn` is the collection name |
| `sourceParams_dynamic` | `/dd` | Collection name (same value as `params.dn`) | The full collection name, for example `u_mes_maint_tool` |
| `maxSearchLength` | search dropdown | Number of characters typed after which the frontend calls the search API | `3` |
| `minSearchLength` | search dropdown | See Q6b | Same value as `maxSearchLength` (as in the sample) until clarified |
| `src` | dropDown, radio | Where the values come from | `api` or `data` |
| `data` | `src: "data"` | Value map: key = stored value, value = display text | Keys exactly as stored in the collection (Booleans as `"true"` / `"false"`); 10 entries or fewer |

## 7. Layout rules

1. Control order in `modalElements`: Period, Scope (higher level first), Shift, Status, Category, Boolean.
2. Standard `colSize: 8`, `labelColSpan: 8` on the 24-column grid: three controls per row, so eight controls fill three rows.
3. Labels never repeat the page name (on the Andon Events page, `Status`, not `Andon Status`).
4. Range picker label: `<Verb> Between` from the time key (`raisedAt` gives `Raised Between`, `measuredAt` gives `Measured Between`).

## 8. Payload contract

| Control | Payload written |
|---|---|
| rangePicker | `"<din_from>": "YYYY-MM-DD"`, `"<din_to>": "YYYY-MM-DD"`; whether they are nested under `data_index` is open (Q4). The examples in this instruction show them nested. |
| datePicker | `"<data_index>": "YYYY-MM-DD"` |
| dropDown, single | `"<data_index>": "<value>", "<p_din>": "<display text>"` |
| dropDown, multi | `"<data_index>": ["<value>", ...], "<p_din>": ["<display text>", ...]` |
| dropDown with ALL | `"<data_index>": "all"` (or `["all"]`), `"<p_din>": "ALL"` |
| radio | `"<data_index>": "<value>"`; Booleans as `"true"` / `"false"` |
| Hidden control (`visible: false`) | Its `default` value, as for a visible control |

## 9. Backend translation (rules for each page's code)

| Payload | MongoDB filter |
|---|---|
| No value, or `all`, or `["all"]` | Key left out of the filter |
| Single value | `{ <data_index>: <value> }` |
| Several values | `{ <data_index>: { $in: [ ... ] } }` |
| `"true"` / `"false"` | `{ <data_index>: true }` / `false` (converted to BSON Boolean) |
| Range on a [Datetime] key | `{ <key>: { $gte: <from 00:00 IST as UTC>, $lt: <day after to, 00:00 IST as UTC> } }`; whether the day starts at midnight or at the first shift is open (Q3b) |
| Range on a [Date] key (`productionDate`) | `{ <key>: { $gte: <from>, $lte: <to> } }` |
| Always added | `siteId` from the user's session (Q13) |
| Never used for filtering | Any `p_din` value; it is kept for display (report header, export file name) |

## 10. Standard control templates

Copy these and change only the marked values.

Period:

```js
{
    "typ" : "rangePicker",
    "label" : "Raised Between",                // <Verb> Between from the time key
    "defaultFrom" : NumberInt(-7),
    "defaultTo" : NumberInt(0),
    "required" : true,
    "placeHolder" : "Select Raised Between",
    "errorMessage" : "Please select Raised Between",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "format" : "YYYY-MM-DD",
    "din_from" : "from",
    "din_to" : "to",
    "data_index" : "raisedAt"                  // time key of the collection
}
```

Master reference from the cache (mdict):

```js
{
    "typ" : "dropDown",
    "label" : "Line",
    "default" : "all",
    "includeAll" : true,
    "multiSelect" : false,
    "required" : false,
    "placeHolder" : "Select Line",
    "errorMessage" : "Please select Line",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "data_index" : "lineId",
    "p_din" : "lineName",
    "api" : "/mdict",
    "params" : { "typ" : "Line", "subTyp" : "idame" },
    "src" : "api"
}
```

Status (hard-coded from `status_values.md`):

```js
{
    "typ" : "dropDown",
    "label" : "Status",
    "default" : [ "Raised", "Acknowledged" ],
    "includeAll" : true,
    "multiSelect" : true,
    "required" : false,
    "placeHolder" : "Select Status",
    "errorMessage" : "Please select Status",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "data_index" : "status",
    "p_din" : "statusText",
    "data" : {
        "Raised" : "Raised",
        "Acknowledged" : "Acknowledged",
        "Resolved" : "Resolved",
        "Cancelled" : "Cancelled"
    },
    "src" : "data"
}
```

Optional Boolean filter (dropdown, because radio has no "All"):

```js
{
    "typ" : "dropDown",
    "label" : "Line Stopped",
    "default" : "all",
    "includeAll" : true,
    "multiSelect" : false,
    "required" : false,
    "placeHolder" : "Select Line Stopped",
    "errorMessage" : "Please select Line Stopped",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "data_index" : "lineStopped",
    "p_din" : "lineStoppedText",
    "data" : { "true" : "Yes", "false" : "No" },
    "src" : "data"
}
```

Mandatory choice (radio):

```js
{
    "typ" : "radio",
    "label" : "Period Type",
    "default" : "Day",
    "required" : true,
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "data_index" : "periodType",
    "data" : { "Shift" : "Shift", "Day" : "Day", "Week" : "Week", "Month" : "Month" },
    "src" : "data"
}
```

(Reliability Summary screen, `u_mes_maint_reliabilitySummary.periodType`: each document belongs to exactly one period type, so the user must choose one.)

Search dropdown (more than 500 documents, or users):

```js
{
    "typ" : "dropDown",
    "label" : "Operator",
    "default" : "all",
    "includeAll" : true,
    "multiSelect" : false,
    "required" : false,
    "placeHolder" : "Type 3 characters of Operator",
    "errorMessage" : "Please select Operator",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "minSearchLength" : NumberInt(3),
    "maxSearchLength" : NumberInt(3),
    "data_index" : "operatorUserId",
    "p_din" : "operatorUserName",
    "api" : "/dd",
    "params" : { "dn" : "u_mes_mast_user" },
    "sourceParams_dynamic" : "u_mes_mast_user",
    "src" : "api"
}
```

## 11. MES MasterDict: collection `u_int_mdict`

### 11.1 Purpose

`u_int_mdict` holds one dictionary per frequently used small master collection and per site. The `/mdict` API serves the dictionaries from the cache; `u_int_mdict` is the reference copy and the stage between the master collections and the cache. When a master document is created or changed, its dictionary in `u_int_mdict` and the cache are refreshed. It replaces the legacy `mdict.json` content, which belongs to another application.

### 11.2 Document structure

| Key | BSON type | Description |
|---|---|---|
| `_id` | String | 16-digit numeric string with collection number 1370 (next free number after 1369) |
| `recordNo` | String | Business key: `MD-<site recordNo>-<dictName>`, for example `MD-PN1-Line` |
| `siteId`, `siteName` | String | Site of the dictionary; the cache key is `siteId` + `dictName` |
| `dictName` | String | Dictionary name used as `params.typ`; the entity name in PascalCase from the collection name (`u_mes_mast_workCenter` gives `WorkCenter`) |
| `sourceCollection` | String | Master collection the dictionary is built from |
| `displayKey` | String | Key of the source document used as display text (`name`, `description`) |
| `entryCount` | Int32 | Number of entries in `idame`; must stay at 200 or fewer |
| `idame` | Embedded document | Map of source `_id` to display text. Holds all documents of the source collection for the site, including inactive ones, so historic records can still be filtered. The display text equals the value stored in the `...Name` keys of transaction collections, so `p_din` matches stored data. |
| `refreshedAt` | Date [Datetime] | Last rebuild of the dictionary |
| `status` | String | Active, Inactive |
| `schemaVersion` | Int32 | 1 |
| `createdAt`, `createdById`, `createdBy`, `updatedAt`, `updatedById`, `updatedBy` | Date / String | Audit stamps |

Embed versus reference: `idame` is embedded because it is bounded (200 entries or fewer by rule), always read as a whole and rebuilt as a whole. Indexes: `{ siteId: 1, dictName: 1 }` unique (the cache lookup); `{ siteId: 1, recordNo: 1 }` unique.

### 11.3 Selection rule and resulting dictionaries

A master entity collection gets a dictionary when all three hold:

1. it is expected to hold **200 documents or fewer per site** in production;
2. it is **frequently used**: referenced by at least two transaction, report or telemetry collections, or it is the category key of a frequently used list screen;
3. it is used as a **query control** (scope, shift or category), not only displayed.

Reference counts were taken from `02_architecture/field_lists` (references from non-master collections, `siteId` excluded).

| dictName | Source collection | Display key | References from non-master collections | Expected documents per site |
|---|---|---|---|---|
| Area | `u_mes_mast_area` | name | 3 | 10 |
| Line | `u_mes_mast_line` | name | 18 | 12 |
| WorkCenter | `u_mes_mast_workCenter` | name | 37 | 60 |
| Equipment | `u_mes_mast_equipment` | name | 29 | 150 |
| Shift | `u_mes_mast_shift` | name | 27 | 4 |
| Customer | `u_mes_mast_customer` | name | 14 | 15 |
| Supplier | `u_mes_mast_supplier` | name | 4 | 60 |
| Item | `u_mes_prod_item` | description | 52 | 180 (review at go-live; above 200 it moves to `/dd` search) |
| ProductVariant | `u_mes_prod_productVariant` | name | 14 | 20 |
| Operation | `u_mes_prod_operation` | name | 16 | 40 |
| AndonType | `u_mes_plan_andonType` | name | 1 (category of Andon Events) | 6 |
| ContainerType | `u_mes_plan_containerType` | name | 1 (category of Containers) | 15 |
| IndirectActivity | `u_mes_plan_indirectActivity` | name | 1 (category of Labour Bookings) | 15 |
| StockStatus | `u_mes_matl_stockStatus` | name | 3 | 6 |
| MovementType | `u_mes_matl_movementType` | name | 1 (category of Material Movements) | 25 |
| DefectCode | `u_mes_qual_defectCode` | name | 5 | 80 |
| DispositionType | `u_mes_qual_dispositionType` | name | 3 | 6 |
| ComplaintType | `u_mes_qual_complaintType` | name | 1 (category of Customer Complaints) | 8 |
| ReasonCode | `u_mes_perf_reasonCode` | name | 14 | 150 |
| LossCategory | `u_mes_perf_lossCategory` | name | 2 | 8 |
| EnergyType | `u_mes_perf_energyType` | name | 1 (category of Energy Readings) | 5 |
| DocumentType | `u_mes_syst_documentType` | name | 1 (category of Controlled Documents) | 30 |
| NotificationType | `u_mes_syst_notificationType` | name | 1 (category of Notifications) | 15 |
| IncidentType | `u_mes_ehs_incidentType` | name | 1 (category of Safety Incidents) | 8 |

Not given a dictionary:

| Collection | Reason | Source used instead |
|---|---|---|
| `u_mes_mast_user` (518 references) | About 600 documents per site | `/dd` search |
| `u_mes_matl_storageLocation`, `u_mes_maint_tool`, `u_mes_qual_gauge`, `u_mes_qual_characteristic`, `u_mes_maint_sparePart`, `u_mes_perf_processTag` | More than 200 documents, or growing | `/dd` search |
| `u_mes_prod_recipe`, `u_mes_syst_iotDevice`, `u_mes_prod_routing`, `u_mes_qual_controlPlan`, `u_mes_qual_pfmea`, `u_mes_prod_billOfMaterial` and other definition masters | Versioned or rarely used as a filter | `/dd` |
| `u_mes_mast_unitOfMeasure` (20 references) | Displayed only, never a query control | – |
| Value-list masters without transaction references (country, currency, language, item group, defect group and similar) | Not used in query controls of transaction screens | `/dd` on their own admin screen |

### 11.4 Sample file

`04_reference_data/ui_controls/query/u_int_mdict.json`: 43 documents in MongoDB shell style, one per dictionary per site, built from the sample documents in `03_design/<module>/samples`. The sample universe holds two sites: Chakan Plant, Pune (`PN1`, `1003000000000001`) and Ranjangaon OSD Plant, Pune (`RJ1`, `1003000000000011`). Dictionaries whose source has samples for one site only (AndonType, IndirectActivity, EnergyType, NotificationType, IncidentType) exist for that site only. Every `idame` key is an `_id` present in the source sample file.

## 12. Worked example: `u_mes_plan_andonEvent` (Andon Events)

Profile: time key `raisedAt`; scope `lineId`, `workCenterId`; shift `shiftId`; status Raised, Acknowledged, Resolved, Cancelled; category `andonTypeId`; Boolean `lineStopped`.

| # | Control | Type and source | `data_index` / `p_din` | Default |
|---|---|---|---|---|
| 1 | Raised Between | rangePicker | `raisedAt` | `-7` to `0` |
| 2 | Line | dropDown, mdict `Line` | `lineId` / `lineName` | `all` |
| 3 | Work Center | dropDown, mdict `WorkCenter`, multiSelect | `workCenterId` / `workCenterName` | `["all"]` |
| 4 | Shift | dropDown, mdict `Shift` | `shiftId` / `shiftName` | `all` |
| 5 | Status | dropDown, data, multiSelect | `status` / `statusText` | `["Raised", "Acknowledged"]` |
| 6 | Andon Type | dropDown, mdict `AndonType` | `andonTypeId` / `andonTypeName` | `all` |
| 7 | Line Stopped | dropDown, data (optional Boolean) | `lineStopped` / `lineStoppedText` | `all` |

Not controls: `reasonCodeId`, `severityClass` (grid columns), `equipmentId` (third scope level), `siteId` (session).

Example payload when the user selects Front Caliper Assembly Line 1, the last 7 days and the open statuses:

```js
{
    "raisedAt" : { "from" : "2026-10-06", "to" : "2026-10-12" },
    "lineId" : "1006000000000006",
    "lineName" : "Front Caliper Assembly Line 1",
    "workCenterId" : [ "all" ],
    "workCenterName" : [ "ALL" ],
    "shiftId" : "all",
    "shiftName" : "ALL",
    "status" : [ "Raised", "Acknowledged" ],
    "statusText" : [ "Raised", "Acknowledged" ],
    "andonTypeId" : "all",
    "andonTypeName" : "ALL",
    "lineStopped" : "true",
    "lineStoppedText" : "Yes"
}
```

Resulting filter (IST midnight is 18:30 UTC of the previous day):

```js
{
    "siteId" : "1003000000000001",
    "raisedAt" : { "$gte" : ISODate("2026-10-05T18:30:00.000Z"), "$lt" : ISODate("2026-10-12T18:30:00.000Z") },
    "lineId" : "1006000000000006",
    "status" : { "$in" : [ "Raised", "Acknowledged" ] },
    "lineStopped" : true
}
```

The filter is served by the open-calls partial index `{ siteId, status, raisedAt }` and the line history index `{ lineId, raisedAt }` described for this collection on 12 October 2026.

## 13. Checklist per screen

| # | Check |
|---|---|
| 1 | Transaction, Reports, Telemetry and Audit Trail screens have a range picker on the time key with `required: true` |
| 2 | 8 controls or fewer, in the order of section 7 |
| 3 | Every `data_index` is an existing key of the collection in `collection_keys.md` |
| 4 | Every `p_din` is the matching display key, or `<key>Text` |
| 5 | Every dropdown source follows the decision table of step 4; master data never comes from `data` or cropdown; `/mdict` only for dictionaries of section 11.3 |
| 6 | `data` maps and cropdown documents have 10 values or fewer, and `data` keys equal the stored values |
| 7 | Every optional dropdown has `includeAll: true` and default `all` or `["all"]`; `default` is an array exactly when `multiSelect` is true |
| 8 | Radios are mandatory choices with two to four options and a default; optional Boolean filters are dropdowns |
| 9 | No control selects a single transaction document, `siteId`, `_id`, `recordNo` or a `...Name` key |
| 10 | `colSize` and `labelColSpan` are 8 or below |
| 11 | Label, placeholder and error message follow section 6 |
| 12 | Hidden controls have a default the role is allowed to see |
| 13 | The resulting filter is served by an index of the query key strategy |
| 14 | Every new cropdown document, `u_int_mdict` dictionary or `/dd` registration the screen needs is listed for creation |

## 14. Open questions

| No. | Question | Why it matters |
|---|---|---|
| Q2b | Is `labelColSpan` measured on the same 24-column grid as the whole row, or as a share of the control's own width (the sample uses `colSize` 12 with `labelColSpan` 10)? | Label width standard |
| Q3b | Should a date range follow the plant production day, starting with the first shift (for example 06:00 IST), rather than calendar midnight? If yes, a night-shift record raised at 02:00 on 13 October belongs to production day 12 October. | Correct period filter for night shifts |
| Q4 | For a range picker, is the payload `{ "raisedAt": { "from": "...", "to": "..." } }` (nested under `data_index`) or `{ "from": "...", "to": "..." }` at the top level? (The answer received repeated the day-offset answer.) | Payload contract |
| Q6b | `maxSearchLength` is the number of characters after which the search API is called. What does `minSearchLength` control? | Search dropdown standard |
| Q10 | Does `/mdict` support `subTyp` values other than `idame` (for example a map of active entries only)? `u_int_mdict` uses only `idame`. | Mdict parameters |
| Q13 | The sample universe has two sites. Is the site always taken from the login session, or can one user query several sites (Site control needed)? | Site handling and the cache key of `u_int_mdict` |
| Q15 | The updated `FormatQuery.json` has no text input control. How should a user find records by a business number (production order, lot, serial number, NC number): a new text control type, a `/dd` search on the transaction collection, or only through the list after group filters? | Search by number |
| Q16 | May `/dd` serve transaction collections (open production orders, lots), or only master data? | Production order and lot filters |
| Q17 | The cropdown `ShiftZone` (Current Shift, Today, Yesterday) suggests a period preset. Should live screens use a preset dropdown instead of the range picker? | Period control on live boards |
| Q18 | What do the page configuration fields `lid`, `page`, `subTyp`, `ver`, `unq`, `act`, `countList`, `q`, `projid`, `rel`, `resp`, `origId`, `mint` and `footerButtons` mean, and must any of them follow a rule for MES pages? | A complete page configuration standard |
| Q19 | Is the page configuration document stored in a MongoDB collection of the MES database? If so, under which collection name (for example `u_int_pageConfig`) and `_id` format? | Consistency with the data model |
| Q20 | How does `/dd` know which keys of a registered collection are the value and the display text? MES collections use `_id` with `name`, `description` or `fullName`. Is this set per collection in the Flask registration? | Registering MES collections in `/dd` |
| Q21 | `u_int_mdict` introduces the prefix `u_int_` outside the `u_mes_<module>_` naming of `collection_inventory.md`. Should `int` be registered as a module (with `u_int_mdict` and later `u_int_pageConfig`) in the data model register and the generator? This task did not change those files. | Model register completeness |
| Q22 | Is the `/mdict` API able to read the extra keys of `u_int_mdict` (`siteId`, `recordNo`, audit keys) while selecting by `dictName`, or does it expect only `_id`, `dictName` and `idame` as in the legacy sample? | Compatibility with the existing API |

## 15. Resolved questions

| No. | Question | Answer (13 Oct 2026) | Effect in this version |
|---|---|---|---|
| Q1 | Does `required: true` mean mandatory? | Yes | Sections 5 and 6 |
| Q2 | Is `colSize` on a 24-column grid? | Yes | Standard `colSize: 8`, three controls per row |
| Q3 | Are date defaults day offsets from today? | Yes (0 = today, -30 = 30 days ago) | Section 6 |
| Q5 | Generic backend or page code? | Each page has its own code | `data_index` = collection key kept as a naming standard; section 9 written as rules for page code |
| Q6 | What does `maxSearchLength` control? | Number of characters after which the frontend calls the search API | Section 6; Q6b opened for `minSearchLength` |
| Q7 | Naming of `dn` and the authorised list | `dn` is the collection name; it is registered in the Flask code | `params.dn` and `sourceParams_dynamic` = collection name |
| Q8 | Which masters go to mdict; size limit | Claude decides; at most 200 documents per collection and frequently used | Section 11 and collection `u_int_mdict` |
| Q9 | Cascading dropdowns | Not applicable | Scope dropdowns are independent; `Line_<Child>` dictionaries are not used |
| Q11 | Radio use, Boolean values, "All" on radio | Two to four options allowed; Booleans sent as `"true"` / `"false"` strings and corrected by the backend; no "All" on radio | Optional Boolean filters use a hard-coded dropdown; radio for mandatory choices |
| Q12 | Hidden control sends its default? | Yes | Sections 2, 6 and 8 |
| Q14 | Cropdown limit | 10 values per document | Sections 4 and 5 |
| – | `FormatQuery.json` | Corrected by the owner | Cropdown example now writes `st` / `status` |
| – | Cropdown `Shift` | Corrected by the owner | `B` is now "Shift B" |
| – | Mdict file name | `mdict.json` | Section 3 |
| – | Mdict content from another application | Create `u_int_mdict` | Section 11, sample file `u_int_mdict.json` |

## 16. Observations on the sample files (not changed)

| File | Observation |
|---|---|
| `FormatQuery.json` | After the correction the control content is consistent, but the file still does not parse as one document: after the radio element there is a trailing comma, and the closing `]` of `modalElements` and `}` of `config` are missing before `"ver"`. Uses MongoDB shell types (`NumberInt`), so it is shell style rather than JSON. |
| `FormatQuery.json` | All controls use `colSize: 12` and `labelColSpan: 10`; MES pages use 8 and 8 (section 6). |
| `cropdown.md` | 18 documents, each with 10 values or fewer. Shift and financial year are master-type data; MES pages use `/mdict` `Shift` instead. Document `X016` has a space in its name (`Task Status`). |
| `mdict.json` | Legacy content of another application (watch dials, two-wheeler customers, other plants); kept as a format reference only. |

## 17. Change log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 13 Oct 2026 | First issue: control catalogue, seven-step procedure, source decision table, attribute reference, payload and backend translation, templates, Andon Events example, checklist, assumptions, open questions Q1 to Q19 | Claude |
| 0.2 | 13 Oct 2026 | Owner answers to Q1 to Q3, Q5 to Q9, Q11, Q12, Q14 applied; 24-column grid; Boolean values as strings; optional Boolean filters as dropdowns, radio only for mandatory choices; no cascading; `dn` = collection name; MasterDict selection rule and new collection `u_int_mdict` (section 11, sample file with 43 documents); users and large masters moved to `/dd` search; resolved-questions table added; new questions Q2b, Q3b, Q6b, Q13 expanded, Q15 restated, Q20 to Q22; assumptions table replaced by the resolved and open question tables | Claude |
