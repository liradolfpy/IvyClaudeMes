# Query Control Instruction

Instruction version: 0.15 | 15 October 2026 | Model version 2.9 (369 collections, 8,614 keys including `app`) plus `u_int_mdict`
Status: working instruction, refined regularly. Every refinement raises the version, adds a row to the change log (section 17), moves answered questions to section 15 and adds new questions to section 14.
Location: `04_reference_data/ui_controls/query_control_instruction.md`, next to the control samples it governs (`04_reference_data/ui_controls/query/`).

## 1. Purpose

This instruction gives one repeatable method for deciding the **query controls** of every list screen in the MES React application: which controls appear, which type each one is, where its values come from, how each attribute is set, and what the page's backend code receives.

Apply it to every collection that has a list screen. The result for each collection is one `modalElements` array inside the page configuration document served by `/miscellaneous/pageconfig`. Page configuration documents are stored in the collection `PageConfig`. This instruction governs `dictData.config.modalElements` and the fixed document frame described in step 8; any other field is outside its scope.

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
| 5 | The app builds the payload: every control writes its selected value under its `data_index`; dropdowns and radios also write the display text under `p_din`; range pickers write the two dates as strings at the top level of the payload, under the key names given in `din_from` and `din_to`. Controls hidden by RBAC (`visible: false`) still send their default value. |
| 6 | The page's own backend code (each page has its own code) turns the payload into a MongoDB filter, following section 9. A value of `all` means "do not filter on this key". The site is the application default and is never part of the query. |

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
| Mdict (MasterDict) | `dropDown` | `api`, `api: "/mdict"` | The cache, filled from `u_int_mdict`, chosen by `params.typ` (the `dictName`) and `params.subTyp`, which is always the fixed value `idame` (a map combining id and name) | Master data listed in section 11: at most 200 documents in the source collection and frequently used. Only master data. |
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
| 1 | Period | Mandatory on Transaction, Reports, Telemetry and Audit Trail screens of **entity** collections. Range picker on the time key; the time key must be a required (non-null) date key where one exists. Not used on Master screens. Child and relationship collections have no period control: their first control is a search dropdown on the parent (`<parent>Id`), followed by their own reference and category keys. |
| 2 | Scope | Mandatory on Transaction screens when the collection holds a scope key. Highest useful level first (Line), then the next level (Work Center). At most two scope levels. Scope dropdowns are independent: there is no cascading (choosing a line does not narrow the work-centre list). |
| 3 | Shift | When the collection holds `shiftId` and users read it per shift. Source: cropdown `Shift`, never mdict. |
| 4 | Status | When the collection has a lifecycle status. |
| 5 | Category | One or two category keys that users group by. |
| 6 | Boolean | Only flags that users filter on regularly. |
| – | Never a control | `siteId` (site is not used in any query), `_id`, `recordNo` as a typed value (a business number is searched with the search dropdown, see the rule below), any `...Name` key, measured values, free text, audit stamps (`createdAt`, `updatedBy` and the like). |

Rules:

- A key becomes a control only if it is a query key under the query key strategy (it is in an index or is applied on top of an indexed filter).
- Group filters come first. A control that finds one transaction document by its business number (production order, lot, serial number, nonconformance) is allowed only as a **dynamic search dropdown** on that transaction collection: `params.dn` and `sourceParams_dynamic` = the transaction collection, `data_index` = the reference key held by the listed collection (for example `productionOrderId`), `p_din` = its name key (`productionOrderName`). The user types part of the number (`recordNo`) and picks it. At most one such control per screen, placed after the period control.

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
| 5 | Does it hold more than 500 documents, or is it expected to grow past 500, or is it a transaction collection searched by business number? | `/dd` with `minSearchLength` and `maxSearchLength` (search dropdown) |
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
| Shift | 4 values (A, B, C, G) | `/cropdown` | `{ name: "Shift" }`. The cropdown keys are the shift codes (`A`, `B`, `C`, `G`), and `shiftId` in transaction, report and telemetry collections stores the same code, so the filter is a direct match. The mdict `Shift` dictionary is not used in query controls. |

### Step 5: Set the attributes

Use section 6 for every attribute. The most important rules:

- `data_index` is the **exact key name in the collection** (`lineId`, `status`, `raisedAt`). Each page has its own backend code, so this is a naming standard rather than a technical need: it keeps page code, payload and indexes readable side by side.
- `p_din` is the **matching display key** of the model (`lineName` for `lineId`, following the Id/Name pairing of `collection_keys.md`). For a `data` or cropdown source on a text key, `p_din` is the key name followed by `Text` (for example `statusText`), because the model has no separate name key for it.
- `includeAll: true` and `default: "all"` on every dropdown filter; `multiSelect: false` unless there is a compelling reason (then `default: ["all"]` or the required values as an array).
- `required: true` makes the control mandatory and is set on **every control** unless a control is specifically required to be optional (then `required: false`, with the reason noted in the query profile).

### Step 6: Check the payload and the filter

Write the example payload and the resulting MongoDB filter for the screen (section 9) and confirm that the filter is served by an index from the query key strategy.

### Step 7: Run the checklist

Section 13.

### Step 8: Build the page configuration document

Wrap the `modalElements` array in this frame. Values in angle brackets are filled per collection; all other values are fixed and copied exactly.

| Field | Value | Rule |
|---|---|---|
| `_id` | `<collection without the leading u_>Query` | `u_mes_maint_cleaningRecord` gives `mes_maint_cleaningRecordQuery` |
| `dictName` | Same as `_id` | `mes_maint_cleaningRecordQuery` |
| `typ` | `"PageConfigQuery"` | Fixed |
| `page` | Page name | Kept as set by the owner (the reviewed Downtime Events config uses `"Phantom"`) |
| `dictData.config.method` | `"GET"` | Fixed |
| `dictData.config.pageTitle` | Screen label | The label of the collection in `collection_type_matrix.md` (`Cleaning Records`) |
| `dictData.config.api` | `"/ivy/mes"` | Fixed |
| `dictData.config.params` | `{}` | Fixed, empty object |
| `dictData.config.footerButtons` | `{}` | Fixed, empty object |
| `dictData.config.modalElements` | The controls | Steps 1 to 6 |

`dictData` holds only `config`; `pageTitle`, `api`, `params` and `footerButtons` are inside `config`, never beside it.
| `ver` | `"<YYYYMMDD-HHmm>"` | Date and time (IST) the document is generated, as a string, for example `"20261013-1708"` |
| `rel` | `"<YYYYMMDD-HHmm>"` | Same value as `ver` |
| `unq` | `false` | Fixed |
| `subTyp` | `"PhantomQuery"` | Fixed |
| `act` | `false` | Fixed |
| `approve`, `delete`, `dynamicModal`, `edit`, `view` | `[]` | Fixed, empty arrays |
| `mint` | `"1"` | Fixed |
| `projid` | `""` | Fixed, empty string |

```js
{
    "_id" : "mes_maint_cleaningRecordQuery",
    "dictName" : "mes_maint_cleaningRecordQuery",
    "typ" : "PageConfigQuery",
    "page" : "Phantom",
    "dictData" : {
        "config" : {
            "method" : "GET",
            "pageTitle" : "Cleaning Records",
            "api" : "/ivy/mes",
            "params" : {},
            "footerButtons" : {},
            "modalElements" : [ /* controls */ ]
        }
    },
    "ver" : "20261013-1708",
    "unq" : false,
    "subTyp" : "PhantomQuery",
    "act" : false,
    "approve" : [],
    "delete" : [],
    "dynamicModal" : [],
    "edit" : [],
    "mint" : "1",
    "view" : [],
    "rel" : "20261013-1708",
    "projid" : ""
}
```

File name of a generated configuration: `04_reference_data/ui_controls/query/PageConfigs/<collection>.json` (for example `PageConfigs/u_mes_maint_cleaningRecord.json`).

### Step 9: Build or update the IvyConfig

Every time a query configuration is generated or changed, the IvyConfig of the same collection is generated or updated in the same step. IvyConfig is the configuration of the REST API: a generic backend code reads the payload from the UI, parses every value by its `din` and `typ`, and runs the query (`get`) or the write (`post`).

File: `04_reference_data/ui_controls/query/IvyConfig/<collection>Ivy.json` (for example `IvyConfig/u_mes_perf_downtimeEventIvy.json`).

Document frame:

| Field | Value | Rule |
|---|---|---|
| `_id` | `"<collection without the leading u_>Ivy"` | `u_mes_maint_cleaningRecord` gives `mes_maint_cleaningRecordIvy` |
| `code` | Module code | The module code in the collection name (`u_mes_perf_downtimeEvent` gives `perf`) |
| `moduleName` | Module name | From the module code in the collection name, using the module table of `collection_inventory.md` (`perf` gives `PerformanceManagement`) |
| `collection` | Collection name | `u_mes_perf_downtimeEvent` |
| `stableName` | `"<collection without the leading u_>Stable"` | `mes_perf_downtimeEventStable` |
| `typ` | `"IvyConfig"` | Fixed |
| `label` | `"EnterpriseIvy"` | Fixed |
| `dn` | Same as `_id` | `mes_maint_cleaningRecordIvy` |
| `proj` | `[]` | Empty for now |
| `get` | One entry per query control | See below |
| `post` | One entry per document key | See below |
| `staticPost` | `{ "act" : true }` | Fixed |
| `patch` | `[]` | Empty for now |

`get` list: every control of the page configuration's `modalElements`, in the same order, and nothing else. Only the filter key (`data_index`) is listed; `p_din` display keys are not.

| Control | Entry |
|---|---|
| Range picker | `{ "dinFrom" : "from", "dinTo" : "to", "din" : "<data_index>", "typ" : "range", "format" : "YYYY-MM-DD" }` |
| Any other control | `{ "din" : "<data_index>", "typ" : "<type of the key>" }` |

`post` list: every key of the collection in field-list order (`app` included) (`02_architecture/field_lists`), as `{ "din" : "<key>", "typ" : "<type>" }`, with these rules:

- `_id` is left out (created by the server);
- the audit keys `createdAt`, `createdById`, `createdBy`, `updatedAt`, `updatedById`, `updatedBy` are left out;
- `app` (application context: `Auto`, `Gamp` or `Common`) is a model key placed directly after `recordNo` in every collection, so it comes from the field list like any other key;
- `...Name` display keys and `siteId` / `siteName` are included like any other key.

Type names (`typ`):

| BSON type | `typ` |
|---|---|
| String | `string` |
| Boolean | `bool` |
| Int32, Int64 | `int` |
| Decimal128 | `decimal` |
| Double | `double` |
| Date (both [Date] and [Datetime] keys) | `Date` |
| Range picker control | `range` |

## 6. Attribute reference

| Attribute | Applies to | Meaning | Rule in this project |
|---|---|---|---|
| `typ` | all | Control type | One of `datePicker`, `rangePicker`, `dropDown`, `radio` |
| `label` | all | Text shown next to the control | Title Case, the business name of the key as used in the screen label of `collection_type_matrix.md`, singular, 25 characters or fewer (for example `Work Center`, `Andon Type`, `Raised Date Range`) |
| `placeHolder` | all except radio | Hint text inside the control | `Select <label>` for dropdowns and pickers; for the search dropdown `Type <maxSearchLength> characters of <label>` |
| `errorMessage` | all with `required: true` | Message when a mandatory control is empty at submit | `Please select <label>` |
| `required` | all | `true`: the control is mandatory; `false`: optional | `true` on every control unless the control is specifically required to be optional. A dropdown with `includeAll` and default `"all"` is always filled, so `required: true` on it only stops the user from clearing it. |
| `default` | dropDown, radio, datePicker | Value selected when the form opens | Dropdown: `"all"` (an array such as `["all"]` only when `multiSelect` is true); radio: one of its `data` keys; datePicker: day offset from today as `NumberInt` (`0` = today, `-1` = yesterday) |
| `defaultFrom`, `defaultTo` | rangePicker | Initial range | Day offsets from today as `NumberInt` (`0` = today, `-30` = 30 days ago). Standard: live screens `0` / `0`; operational lists `-7` / `0`; history and reports `-10` / `0` |
| `format` | datePicker, rangePicker | Display and payload date format | `YYYY-MM-DD` |
| `din_from`, `din_to` | rangePicker | Names of the two top-level payload keys that receive the from-date and to-date as strings | Always exactly `"din_from" : "from"` and `"din_to" : "to"`. A query form has only one range picker, so the names never collide. `data_index` is the time key, so the page code knows which key the range applies to. |
| `includeAll` | dropDown | The app adds `{ "all": "ALL" }` as the first value; `all` tells the backend not to filter on this key | `true` on every optional filter; `false` only when one value must always be chosen. Not available on radio. |
| `multiSelect` | dropDown | Several values can be selected | `false` under normal conditions. `true` only when there is a compelling reason, written in the query profile (for example an open-calls board that must show Raised and Acknowledged together). `default` is an array exactly when `multiSelect` is true. |
| `readOnly` | all | Shown but not editable | Exceptional: a value fixed by the page or role, for example the line of a line-supervisor screen |
| `visible` | all | Whether the control is shown | `true` by default; `false` when RBAC must stop a role from changing the filter. A hidden control still sends its default value, so its default must be the value that role is allowed to see. |
| `colSize` | all | Width of the control on a 24-column grid | Standard `8` (three controls per row). Never above `8` except a single wide control on its own row. The sample's `12` (two per row) is not used for MES pages. |
| `labelColSpan` | all | Column span of the label, on a 24-column scale (maximum `24`) | Standard `8`; never above `24` |
| `data_index` | all | Payload key that receives the selected value | Exact key name of the collection (`raisedAt`, `lineId`, `status`, `lineStopped`) |
| `p_din` | dropDown, radio | Payload key that receives the display text of the selected value | Display key of the model (`lineName`); `<key>Text` for keys without a name key (for example `periodTypeText`) |
| `api` | dropDown with `src: "api"` | Endpoint | `/cropdown`, `/mdict` or `/dd` |
| `params` | dropDown with `src: "api"` | Selector of the list | `/cropdown`: `{ name }`; `/mdict`: `{ typ, subTyp }`; `/dd`: `{ dn }` where `dn` is the collection name |
| `sourceParams_dynamic` | `/dd` | Collection name (same value as `params.dn`) | The full collection name, for example `u_mes_maint_tool` |
| `maxSearchLength` | search dropdown | Number of characters typed after which the frontend calls the search API | `3` |
| `minSearchLength` | search dropdown | Minimum number of characters the user must type before the `$regex` search API is called | `3`; set `maxSearchLength` to the same value |
| `src` | dropDown, radio | Where the values come from | `api` or `data` |
| `data` | `src: "data"` | Value map: key = stored value, value = display text | Keys exactly as stored in the collection (Booleans as `"true"` / `"false"`); 10 entries or fewer |

## 7. Layout rules

1. Control order in `modalElements`: Period, Search by business number (if any), Scope (higher level first), Shift, Status, Category, Boolean.
2. Standard `colSize: 8`, `labelColSpan: 8` on the 24-column grid: three controls per row, so eight controls fill three rows.
3. Labels never repeat the page name (on the Andon Events page, `Status`, not `Andon Status`).
4. Range picker label: `<business name of the time key> Range`; for a datetime key ending in `At`, the `At` becomes `Date` (`productionDate` gives `Production Date Range`, `raisedAt` gives `Raised Date Range`, `measuredAt` gives `Measured Date Range`).
5. Exactly one range picker per query form.

## 8. Payload contract

| Control | Payload written |
|---|---|
| rangePicker | `"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"` at the top level of the payload, both as strings |
| datePicker | `"<data_index>": "YYYY-MM-DD"` |
| dropDown, single | `"<data_index>": "<value>", "<p_din>": "<display text>"` |
| dropDown, multi | `"<data_index>": ["<value>", ...], "<p_din>": ["<display text>", ...]` |
| dropDown with ALL | `"<data_index>": "all"` (or `["all"]`), `"<p_din>": "ALL"` |
| radio | `"<data_index>": "<value>", "<p_din>": "<display text>"`; Booleans as `"true"` / `"false"` |
| Hidden control (`visible: false`) | Its `default` value, as for a visible control |

## 9. Backend translation (rules for each page's code)

| Payload | MongoDB filter |
|---|---|
| No value, or `all`, or `["all"]` | Key left out of the filter |
| Single value | `{ <data_index>: <value> }` |
| Several values | `{ <data_index>: { $in: [ ... ] } }` |
| `"true"` / `"false"` | `{ <data_index>: true }` / `false` (converted to BSON Boolean) |
| Range on a [Datetime] key | `{ <key>: { $gte: <start of from-date>, $lt: <start of the day after to-date> } }`. Where a day starts (calendar midnight or production day) is decided in the backend code of the page; this instruction does not fix it. |
| Range on a [Date] key (`productionDate`) | `{ <key>: { $gte: <from>, $lte: <to> } }` |
| Never added | `siteId`: the site is the application default and is not used in any query |
| Never used for filtering | Any `p_din` value; it is kept for display (report header, export file name) |

## 10. Standard control templates

Copy these and change only the marked values.

Period:

```js
{
    "typ" : "rangePicker",
    "label" : "Raised Date Range",             // <business name of the time key> Range
    "defaultFrom" : NumberInt(-7),
    "defaultTo" : NumberInt(0),
    "required" : true,
    "placeHolder" : "Select Raised Date Range",
    "errorMessage" : "Please select Raised Date Range",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "format" : "YYYY-MM-DD",
    "din_from" : "from",                       // always "from"
    "din_to" : "to",                           // always "to"
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
    "required" : true,
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
    "default" : "all",
    "includeAll" : true,
    "multiSelect" : false,
    "required" : true,
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
    "required" : true,
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
    "p_din" : "periodTypeText",
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
    "required" : true,
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

Search by business number (transaction collection):

```js
{
    "typ" : "dropDown",
    "label" : "Production Order",
    "default" : "all",
    "includeAll" : true,
    "multiSelect" : false,
    "required" : true,
    "placeHolder" : "Type 3 characters of Production Order",
    "errorMessage" : "Please select Production Order",
    "readOnly" : false,
    "visible" : true,
    "colSize" : NumberInt(8),
    "labelColSpan" : NumberInt(8),
    "minSearchLength" : NumberInt(3),
    "maxSearchLength" : NumberInt(3),
    "data_index" : "productionOrderId",
    "p_din" : "productionOrderName",
    "api" : "/dd",
    "params" : { "dn" : "u_mes_plan_productionOrder" },
    "sourceParams_dynamic" : "u_mes_plan_productionOrder",
    "src" : "api"
}
```

## 11. MES MasterDict: collection `u_int_mdict`

### 11.1 Purpose

`u_int_mdict` holds one dictionary per frequently used small master collection and per site. Because the site is the application default and is not used in queries, `/mdict` serves the dictionaries of the default site; how `/mdict` handles MES dictionaries is deferred (section 14.1). The `/mdict` API serves the dictionaries from the cache; `u_int_mdict` is the reference copy and the stage between the master collections and the cache. When a master document is created or changed, its dictionary in `u_int_mdict` and the cache are refreshed. It replaces the legacy `mdict.json` content, which belongs to another application.

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
| Shift | `u_mes_mast_shift` | name | 27 | 4 (kept in `u_int_mdict` for other uses; query controls use cropdown `Shift`) |
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
| 1 | Raised Date Range | rangePicker | `raisedAt` | `-7` to `0` |
| 2 | Line | dropDown, mdict `Line` | `lineId` / `lineName` | `all` |
| 3 | Work Center | dropDown, mdict `WorkCenter` | `workCenterId` / `workCenterName` | `all` |
| 4 | Shift | dropDown, cropdown `Shift` | `shiftId` / `shiftName` | `all` |
| 5 | Status | dropDown, data, multiSelect (compelling reason: the open-calls board must show Raised and Acknowledged together) | `status` / `statusText` | `["Raised", "Acknowledged"]` |
| 6 | Andon Type | dropDown, mdict `AndonType` | `andonTypeId` / `andonTypeName` | `all` |
| 7 | Line Stopped | dropDown, data (optional Boolean) | `lineStopped` / `lineStoppedText` | `all` |

Not controls: `reasonCodeId`, `severityClass` (grid columns), `equipmentId` (third scope level), `siteId` (not used in queries).

Example payload when the user selects Front Caliper Assembly Line 1, the last 7 days and the open statuses:

```js
{
    "from" : "2026-10-06",
    "to" : "2026-10-12",
    "lineId" : "1006000000000006",
    "lineName" : "Front Caliper Assembly Line 1",
    "workCenterId" : "all",
    "workCenterName" : "ALL",
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

Resulting filter, with calendar-day boundaries as one possible backend choice (IST midnight is 18:30 UTC of the previous day):

```js
{
    "raisedAt" : { "$gte" : ISODate("2026-10-05T18:30:00.000Z"), "$lt" : ISODate("2026-10-12T18:30:00.000Z") },
    "lineId" : "1006000000000006",
    "status" : { "$in" : [ "Raised", "Acknowledged" ] },
    "lineStopped" : true
}
```

The filter is served by the line history index `{ lineId, raisedAt }` described for this collection on 12 October 2026. Because queries never carry `siteId`, indexes that start with `siteId` (for example the open-calls index `{ siteId, status, raisedAt }` and the D020 defaults) cannot serve these screens; they must start with the first query key instead (open calls: `{ status, raisedAt }`). See section 14.1.

## 13. Checklist per screen

| # | Check |
|---|---|
| 1 | Transaction, Reports, Telemetry and Audit Trail screens have exactly one range picker, on the time key, with `required: true`, `din_from: "from"`, `din_to: "to"` and the label `<time key> Range` |
| 2 | 8 controls or fewer, in the order of section 7 |
| 3 | Every `data_index` is an existing key of the collection in `collection_keys.md` |
| 4 | Every dropdown and radio has a `p_din`, and it is the matching display key or `<key>Text` |
| 5 | Every dropdown source follows the decision table of step 4; master data never comes from `data` or cropdown; `/mdict` only for dictionaries of section 11.3 |
| 6 | `data` maps and cropdown documents have 10 values or fewer, and `data` keys equal the stored values |
| 7 | Every dropdown has `includeAll: true` and default `all`; `multiSelect` is `false` unless a compelling reason is written in the query profile; `default` is an array exactly when `multiSelect` is true |
| 8 | Radios are mandatory choices with two to four options and a default; optional Boolean filters are dropdowns |
| 9 | No control on `siteId`, `_id` or a `...Name` key; a single transaction document is selected only through one search dropdown on its business number; the filter never contains `siteId` |
| 10 | `colSize` is 8 or below (a single wide control on its own row excepted); `labelColSpan` is 24 or below, standard 8 |
| 11 | Label, placeholder and error message follow section 6 |
| 12 | Hidden controls have a default the role is allowed to see |
| 13 | The resulting filter is served by an index of the query key strategy |
| 14 | Every new cropdown document, `u_int_mdict` dictionary or `/dd` registration the screen needs is listed for creation |
| 15 | Every control has `required: true` unless it is specifically required to be optional |
| 16 | The document frame follows step 8: `_id` = `dictName` = `<collection without u_>Query`; `typ` = `PageConfigQuery`; `dictData` holds only `config`, and `config` holds `method`, `pageTitle`, `api` (`/ivy/mes`), `params` (`{}`), `footerButtons` (`{}`) and `modalElements`; fixed fields copied exactly; `ver` = `rel` = generation time; file named `<collection>.json` |
| 17 | Shift controls use cropdown `Shift`, not mdict |
| 18 | The IvyConfig `<collection>Ivy.json` exists and was updated in the same step; its `get` list has exactly one entry per query control (same `din` and order, range entry with `from` / `to` and `YYYY-MM-DD`) |
| 19 | The IvyConfig `post` list has every collection key except `_id` and the six audit keys, including `app` after `recordNo`, each with the type of section 5, step 9; `code` is the module code |

## 14. Open questions

None at version 0.10. New questions are added here with the next free number (Q24 onwards).

### 14.1 Deferred items (to be worked later)

| No. | Item | Note |
|---|---|---|
| Q20 | How `/dd` identifies the value and display keys of a registered MES collection | Deferred by the owner on 13 Oct 2026 |
| Q21 | Registering the `u_int_` prefix (`u_int_mdict`; page configurations stay in the application collection `PageConfig`) in the data model register and generator | Deferred by the owner on 13 Oct 2026 |
| Q22 | Whether `/mdict` reads the extra keys of `u_int_mdict` (`siteId`, `recordNo`, audit keys), and how it treats the per-site dictionaries now that site is not used in queries | Deferred by the owner on 13 Oct 2026 |
| F1 | Index alignment: the query key strategy (`02_architecture/QueryKeySelectionStrategy.md`) and the generated index scripts put `siteId` first in several indexes (`{ siteId, recordNo }`, `{ siteId, status }`, `{ siteId, <date> }`). UI queries never carry `siteId`, so those indexes need `siteId` removed from the front, or a version without it, for list screens. Not changed by this instruction. | Follow-up on the query key strategy |
| F2 | `shiftId` now stores the shift code (`A`, `B`, `C`) in the sample documents (owner instruction, 13 Oct 2026; applied in `05_generator/gen_samples.py`). The model (`05_generator/model/flat_model.json`), `02_architecture/field_lists`, the collection specifications and their examples still describe `shiftId` as a reference to `u_mes_mast_shift._id`. They need the reference changed to the shift code (`u_mes_mast_shift.recordNo`) and a decision log entry. Child collections of the shift master (`shiftBreak`, `shiftWorkingDay`) keep the parent `_id`. | Follow-up on the model and specifications |
| F4 | Maintenance module check (15 Oct 2026): the allowed values of `u_mes_maint_maintenancePlan.planType` (Incoming, In Process, First Off ...) and `strategy` (Torque Control ...) belong to inspection plans and tightening, not maintenance plans; they are not used as query controls until corrected in the model. `u_mes_maint_equipmentQualification` has no required date key; its period control uses `startedAt`, so records in status Planned (no start yet) are found only after they start. | Follow-up on the model |

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
| – | Does `p_din` apply to radio? | Yes | Sections 2, 6, 8, 10 and checklist item 4 |
| – | `config.api` / `config.params` in the page configuration | Hard-coded per page as needed; ignore | Out of scope (section 16) |
| – | Mdict content from another application | Create `u_int_mdict` | Section 11, sample file `u_int_mdict.json` |
| Q4 | How is the range sent in the payload? | `din_from` and `din_to` name two top-level payload keys holding the from-date and to-date as strings | Sections 2, 6, 8, 10, 12; key names `<timeKey>From` / `<timeKey>To` |
| Q3b | Production day or calendar midnight? | Depends on the page; handled in the backend; ignore here | Section 9 leaves the day boundary to the page code |
| Q13 | How is the site chosen? | Default; site is not used in any query | No site control; `siteId` never in the filter (sections 2, 5, 9, 12, checklist 9); index follow-up F1 |
| Q15 / Q16 | Searching by production order, lot or serial number | With the dynamic search dropdown | Rule in step 2, step 4 row 5, template in section 10 |
| Q20 to Q22 | `/dd` and `/mdict` handling of MES collections | Ignore for now; to be worked later | Moved to section 14.1 |
| Q2b | What is `labelColSpan` measured against? | Column span on a 24-column scale, maximum 24 | Section 6, checklist 10 |
| Q6b | What does `minSearchLength` control? | Minimum number of characters typed before the `$regex` search API is called | Section 6 |
| Q10 | Other `subTyp` values for `/mdict`? | None: `subTyp` is always the hard-coded `idame` (id and name) | Sections 4 and 5 |
| Q17 | Preset period control for live screens? | No; the cropdown `ShiftZone` was deleted | Range picker stays the period control on every screen |
| Q18 | Meaning of the other page configuration fields | Ignore them | Section 1: only `modalElements` is in scope |
| Q19 | Where are page configurations stored? | In the collection `PageConfig` | Section 1; Q21 note in section 14.1 |
| – | Range picker label and payload keys (review of the Downtime Events config, 13 Oct 2026) | Label `Production Date Range`, not `Production Date Between`; only one range picker per query, so `din_from` / `din_to` stay permanently `from` / `to` | Sections 6, 7, 8, 10, 12, checklist 1; supersedes the `<timeKey>From` / `<timeKey>To` rule of version 0.4 |
| – | Page configuration frame and `required` on "all" dropdowns (review of the Downtime Events config, 13 Oct 2026) | `_id` and `dictName` = `<collectionSuffix>Query`; `typ` = `PageConfigQuery`; fixed `ver`, `rel` (`YYYYMMDD-HHmm`), `unq`, `subTyp`, `act`, `approve`, `delete`, `dynamicModal`, `edit`, `mint`, `view`, `projid`; `dictData.pageTitle` and `dictData.api` = `/ivy/mes`; every dropdown with default `all` has `required: true` | Step 8 added; sections 1, 5, 6, 10 and checklist 15 and 16; supersedes the Q18 answer "ignore the other fields" for the fields listed |
| – | Attribute name, Shift source, multi-select (13 Oct 2026) | All controls use `"isRequired": true` unless specifically required otherwise; Shift uses cropdown `name: "Shift"`, not mdict; `multiSelect: true` only with a compelling reason | Sections 5, 6, 10, 11.3, 12, checklist 7, 15, 17; new question Q23 |
| – | Attribute name (13 Oct 2026, later the same day) | Keep the key name `required`, not `isRequired`; the value stays `true` on every control unless specifically optional | Sections 2, 5, 6, 10, checklist 1 and 15; supersedes the `isRequired` name of version 0.8 |
| Q23 | Shift code versus `shiftId` | All `shiftId` values in the documents are the shift code (`A`, `B`, `C`); the cropdown `Shift` keys match directly | Step 4 placement table; sample documents regenerated; follow-up F2 |
| – | IvyConfig (13 Oct 2026) | Generated with every query: `_id` / `dn` = `<collection>Ivy`; `code` `mast`; `moduleName` = module name; `typ` `IvyConfig`; `label` `EnterpriseIvy`; `stableName` = collection without `u_` + `Stable`; `get` = every query control (filter keys only, range format `YYYY-MM-DD`); `post` = every key except `_id` and audit keys, plus `app`; types `string`, `bool`, `int` (Int32 and Int64), `decimal`, `double`, `Date`, `range`; `proj` and `patch` empty, `staticPost` `{ act: true }`; page configurations in `query/PageConfigs/`, IvyConfigs in `query/IvyConfig/` | Step 9; step 8 file location; checklist 18 and 19; follow-up F3 |
| – | IvyConfig `code`; key `app` (13 Oct 2026) | `code` is the module code. `app` is part of the data model with the standard values Auto / Gamp / Common (D060 rule in `flatten_model.py`); the field lists, collection keys, specifications, validators, register and reports were regenerated with `gen_docs.py` and `gen_specs.py` (8,614 keys) | Step 9; checklist 19; F3 closed |
| – | Page configuration layout (15 Oct 2026) | `pageTitle`, `api`, `params: {}` and `footerButtons: {}` inside `dictData.config`; `_id` / `dictName` = collection without `u_` + `Query` (`mes_maint_cleaningRecordQuery`); file name `<collection>.json` | Step 8, checklist 16; all 24 page configurations converted |
| – | IvyConfig identifier (15 Oct 2026) | `_id` and `dn` = collection without `u_` + `Ivy` (`mes_maint_cleaningRecordIvy`); `collection` keeps the full name; file name unchanged (`<collection>Ivy.json`) | Step 9; all 24 IvyConfigs updated |

## 16. Observations on the sample files (not changed)

| File | Observation |
|---|---|
| `FormatQuery.json` | Corrected by the owner on 13 Oct 2026 and reviewed again the same day: parses (9 controls) once read as MongoDB shell style (`NumberInt`); labels, placeholders and error messages match their controls; every hard-coded default is one of its values; no double or trailing spaces. Cosmetic only: one error message reads "Please Select Direction" (capital S) and indentation mixes tabs and spaces. |
| `FormatQuery.json` | `config.api` (`/stdtools/phantomzen`) and `config.params` (`op`) are the page's submit endpoint, hard-coded per page as needed; they are outside the scope of this instruction. |
| `cropdown.md` | 16 documents (after `ShiftZone` was deleted by the owner on 13 Oct 2026), each with 10 values or fewer. Shift and financial year are master-type data; MES pages use `/mdict` `Shift` instead. Document `X016` has a space in its name (`Task Status`). |
| `mdict.json` | Legacy content of another application (watch dials, two-wheeler customers, other plants); kept as a format reference only. |

## 17. Change log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 13 Oct 2026 | First issue: control catalogue, seven-step procedure, source decision table, attribute reference, payload and backend translation, templates, Andon Events example, checklist, assumptions, open questions Q1 to Q19 | Claude |
| 0.2 | 13 Oct 2026 | Owner answers to Q1 to Q3, Q5 to Q9, Q11, Q12, Q14 applied; 24-column grid; Boolean values as strings; optional Boolean filters as dropdowns, radio only for mandatory choices; no cascading; `dn` = collection name; MasterDict selection rule and new collection `u_int_mdict` (section 11, sample file with 43 documents); users and large masters moved to `/dd` search; resolved-questions table added; new questions Q2b, Q3b, Q6b, Q13 expanded, Q15 restated, Q20 to Q22; assumptions table replaced by the resolved and open question tables | Claude |
| 0.3 | 13 Oct 2026 | `p_din` applies to radio as well (attribute table, payload contract, radio template, checklist); `config.api` / `config.params` declared out of scope; observations on `FormatQuery.json` updated after the owner's correction and the spacing clean-up; final review of the corrected `FormatQuery.json` recorded in section 16 | Claude |
| 0.4 | 13 Oct 2026 | Owner answers to Q3b, Q4, Q13, Q15, Q16 applied: range dates as top-level string keys named `<timeKey>From` / `<timeKey>To`; day boundary left to page code; site never used in queries; search by business number through the dynamic search dropdown on the transaction collection (rule, template); Q20 to Q22 deferred to new section 14.1 with index follow-up F1; Andon Events example updated | Claude |
| 0.5 | 13 Oct 2026 | Owner answers to Q2b, Q6b, Q10, Q17, Q18 and Q19 applied: `labelColSpan` on a 24-column scale (max 24, standard 8); `minSearchLength` = minimum characters before the `$regex` search; `subTyp` always `idame`; no period preset (cropdown `ShiftZone` deleted); page configurations stored in `PageConfig`, only `modalElements` in scope. No open questions left; deferred items in section 14.1 remain | Claude |
| 0.6 | 13 Oct 2026 | Owner review of the Downtime Events config: range picker label `<time key> Range`; exactly one range picker per query form; `din_from` / `din_to` fixed to `from` / `to` (replaces `<timeKey>From` / `<timeKey>To`); template, Andon Events example and checklist updated | Claude |
| 0.7 | 13 Oct 2026 | Owner review of the Downtime Events config: new step 8 (page configuration frame: `_id` / `dictName` = `<collectionSuffix>Query`, `typ` = `PageConfigQuery`, `dictData.pageTitle`, `dictData.api` = `/ivy/mes`, fixed fields, `ver` / `rel` = `YYYYMMDD-HHmm`, file naming); `required: true` on every dropdown with default `all` (rules, templates, checklist 15); checklist 16 added; step 7 reference corrected to section 13 | Claude |
| 0.8 | 13 Oct 2026 | Attribute renamed to `isRequired`, `true` on every control unless specifically optional; Shift source changed to cropdown `Shift`; `multiSelect` false by default, true only with a written compelling reason; Status template made single-select; Andon Events example updated; checklist 7 and 15 revised, 17 added; Q23 opened on shift code versus `shiftId` | Claude |
| 0.9 | 13 Oct 2026 | Attribute name reverted from `isRequired` to `required` (rules, templates, checklist); value rule of 0.8 unchanged: `required: true` on every control unless specifically optional | Claude |
| 0.10 | 13 Oct 2026 | Q23 resolved: `shiftId` stores the shift code, matching the cropdown `Shift` (sample documents regenerated through `gen_samples.py`); follow-up F2 on model and specifications; second sample configuration `PageConfig_u_mes_perf_alarm.json` produced with this instruction | Claude |
| 0.11 | 13 Oct 2026 | Step 9 added: IvyConfig generated or updated with every query (frame, `get` and `post` rules, type names, file location); page configurations moved to `query/PageConfigs/`; checklist 18 and 19; follow-up F3 on the key `app`; IvyConfigs produced for Downtime Events, Alarms and Station Performance | Claude |
| 0.12 | 13 Oct 2026 | IvyConfig `code` = module code; `app` now listed in the data model (field lists, specifications, validators regenerated), so the `post` list takes it from the field list; follow-up F3 closed; three IvyConfigs regenerated | Claude |
| 0.13 | 15 Oct 2026 | Step 2: child and relationship collections have no period control and start with a parent search dropdown; time key must be a required date key where one exists. Follow-up F4 (maintenance plan allowed values, equipment qualification time key). Query and IvyConfigs produced for all 21 collections of the ToolingAndMaintenance module | Claude |
| 0.14 | 15 Oct 2026 | Page configuration layout: `pageTitle`, `api`, `params`, `footerButtons` moved inside `dictData.config`; `_id` / `dictName` = `<collection without u_>Query`; file name `<collection>.json`; all 24 existing page configurations converted (old files moved to `_to_delete/PageConfigs_old_names`) | Claude |
| 0.15 | 15 Oct 2026 | IvyConfig `_id` and `dn` = `<collection without u_>Ivy`; all 24 IvyConfigs updated | Claude |
