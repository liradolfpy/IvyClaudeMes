---
name: stable
description: Stable (StandardTable) - build the React table page configuration (typ PageConfigStable) that lists a MES collection's documents, from the collection's field list and sample documents.
---

# Stable (StandardTable) - table page configuration

Skill version: 0.5 | 17 October 2026 | Model version 2.9 (369 collections, 8,614 keys including `app`)
Sibling instruction: `04_reference_data/ui_controls/query_control_instruction.md` (query controls of the same list screens). Keep the two consistent.
Reference copy of this skill in the repository: `04_reference_data/ui_controls/table/stable_skill.md`.

## 1. Purpose

Every list screen of the MES React application shows the documents of one collection in a table. The table is rendered from a page configuration document stored in the collection `PageConfig` and served by `/miscellaneous/pageconfig`. This skill produces that document for one or more collections: which keys become columns, in what order, with which title, width, alignment and format, inside a fixed frame copied from the reference sample `04_reference_data/ui_controls/table/FormatTable.json` (version of 17 Oct 2026).

## 2. Inputs (all in the ClaudeMES repository, `E:\Ivy\Claude\ClaudeProjects\ClaudeMES`)

| Input | Location | Used for |
|---|---|---|
| Field lists | `02_architecture/field_lists/<nn>_<module>_field_list.md` | Keys in model order, BSON type, date tag (Date / Datetime), reference target |
| Collection type matrix | `02_architecture/collection_type_matrix.md` | Module code, screen type, screen label (table title) |
| Sample documents | `03_design/<module>/samples/<collection>.js` | Longest displayed text per key (column width); first document copied into `clmnDoc` |
| Specifications | `03_design/<module>/specs/<collection>.md` | Meaning, allowed values, nullability when a rule needs checking |
| Reference sample | `04_reference_data/ui_controls/table/FormatTable.json` | Frame and fixed styling values |
| Generator | `05_generator/gen_stable.py` | Applies every rule of this skill |

## 3. How to run

1. Work on the user's computer through the device shell (`$HOME/mnt/ClaudeMES`).
2. Run `python3 05_generator/gen_stable.py <collection> [<collection> ...]` from the repository root. Collection names are the full model names (`u_mes_perf_downtimeEvent`). For a whole module, take the collection names of that module from `collection_type_matrix.md` (match `| u_mes_<code>_...` only, not the module summary row).
3. The script writes `04_reference_data/ui_controls/table/PageConfigs/<collection>.json` (MongoDB shell style: `NumberInt`, `NumberLong`, `NumberDecimal`, `ISODate`) and prints a column report: data_index, title, type, longest sample text, width, alignment, the keys left out and why, and keys that had no sample value. For a module run, save the report as `PageConfigs/column_report_<code>.md`. Every file of one run carries the same `rel` (section 5).
4. Run the checklist (section 8) on the report and the files, and read the list of titles for words the title rules do not yet handle. Show the user the result and anything the checklist flagged.
5. If a rule must change, change it in this skill **and** in `gen_stable.py` together, raise the skill version, add a change-log row (section 10), update the reference copy `stable_skill.md`, and regenerate the configurations produced earlier so all share the same rules. Never change generated configurations before the skill is updated and agreed with the owner.
6. If the device shell or the script is not available, apply sections 4 to 7 by hand with the same inputs; never invent keys that are not in the field list.

## 4. Column rules

### 4.1 Which keys become columns (owner decision, 14 Oct 2026: display keys only)

| Key | Column? | Reason |
|---|---|---|
| `recordNo` | Yes, always first, `"fixed" : "left"` | Business key; stays visible while scrolling. If a collection has no `recordNo`, the first String key that is a column is fixed instead. |
| `_id`, `app`, `siteId`, `siteName`, `schemaVersion`, `createdById`, `updatedById` | No | Technical identifiers; site is the application default |
| Reference key `xId` whose display key `xName` (or `x`, for `reportedById` / `reportedBy`) exists | No; the display key is the column | Users read names, not 16-digit ids |
| Reference key `...Id` with a reference target but no display key | No; listed in the report for review | Would show a 16-digit id |
| `...Name` display keys | Yes, at the position of the name key in the field list | |
| All other business keys (text, numbers, dates, Booleans, `status`) | Yes, in field-list order | |
| `createdBy`, `createdAt`, `updatedBy`, `updatedAt` | Yes, moved to the end in this order, where the collection has them | Master collections have no audit keys in model 2.9, so their tables have none |

The model is flat (DATA-001): every key is a top-level scalar, so there are no array or embedded columns. The order of the columns in the `column` array is the order above; only the keys inside each column object are sorted (section 7).

### 4.2 Attributes per column

Attributes of a column object (written in alphanumeric key order, section 7): `align`, `data_index`, `dtFormat`, `fixed` (first column only), `isBool`, `isIST`, `title`, `width`.

| BSON type (date tag) | `align` | Extra attributes |
|---|---|---|
| String | `left` | - |
| Int32, Int64, Decimal128, Double | `right` | - (decimal formatting: open question S5) |
| Date (Date) | `center` | `"dtFormat" : "YYYY-MM-DD"`, `"isIST" : true` |
| Date (Datetime) | `center` | `"dtFormat" : "YYYY-MM-DD HH:mm:SS"`, `"isIST" : true` |
| Boolean | `center` | `"isBool" : true` |

- `data_index` is the exact key name of the collection.
- `isIST: true` means the value is shown as stored (owner answer, 14 Oct 2026). Specifications store dates as IST wall-clock with the `+0000` suffix, so no shift is applied.
- Datetime format is `YYYY-MM-DD HH:mm:SS`, exactly as in the reference sample (owner answer, 17 Oct 2026).
- Text is aligned left, numbers right, dates and Booleans centre (owner confirmed 17 Oct 2026: no change to the column rules).

### 4.3 Title

1. `recordNo` gives `Record No`.
2. A display key `xName` whose `xId` exists loses `Name`: `equipmentName` gives `Equipment`, `capaName` gives `CAPA`.
3. A leading `is` is dropped: `isPlanned` gives `Planned`.
4. A unit suffix becomes a bracket: `Minutes` gives `(min)`, `Seconds` / `Sec` give `(s)`, `Hours` give `(h)`, `Days` give `(days)`, `Inr` gives `(INR)`, `Mm` gives `(mm)`, `Percent` / `Pct` give `(%)`: `durationMinutes` gives `Duration (min)`, `taktTimeSec` gives `Takt Time (s)`, `unitCostInr` gives `Unit Cost (INR)`.
5. camelCase is split into Title Case words; known acronyms are upper case (OEE, CAPA, WIP, PFMEA, SLA, IoT, MTBF, MTTR, FPY, PPM, RPN, SPC and the others in the `ACRONYMS` table of the script). The small words of, on, in, per, and, or, to, for stay lower case except as the first word (`Unit of Measure`, `Used on Equipment`); `At` stays capitalised (`Started At`).
6. Titles do not repeat the page name (the line master's `name` column is `Name`, not `Line Name`).

### 4.4 Width (owner decision: computed value goes directly into `width`, to be finalised later)

```
content px = longest displayed sample text (characters) x 7 + 20
header  px = title length (characters) x 8 + 20 (sort icon) + 20
width      = max(content, header, 80), rounded up to the next 10, capped at 300  ->  "<n>px"
```

- Displayed length: Date 10 characters (`2026-09-17`), Datetime 19 (`2026-09-17 06:51:40`), Boolean 3 (`Yes`), numbers and text as their string length; `null` values are ignored.
- 300px is the current standard maximum; long free text (fault text, action text) is capped at 300.
- Sample files hold 10 to 20 documents, so widths are a first estimate. A key with no non-null sample value gets its width from the title only and is listed in the report.
- 7 px and 8 px per character are estimates for Roboto Condensed at 12px (row) and 14px (header) (assumption A2).

## 5. Document frame (top-level keys)

Written in alphanumeric key order (section 7), except `clmnDoc`, which is always the **last** key of the document (owner, 17 Oct 2026). The table lists the keys in the order they are written.

| Key | Value | Rule |
|---|---|---|
| `_id` | `<collection without the leading u_>Stable` | `u_mes_maint_cleaningRecord` gives `mes_maint_cleaningRecordStable`. Equals `stableName` of the collection's IvyConfig |
| `act` | `true` | Fixed |
| `app` | `"mes"` | Fixed |
| `dictData` | `{ "config" : ... }` | Section 6 |
| `dictName` | Same as `_id` | `mes_maint_cleaningRecordStable` |
| `lid` | `"lid_999"` | Fixed, from the reference sample |
| `module` | Module code | From the collection name (`u_mes_maint_...` gives `maint`) |
| `page` | Same as `_id` | Owner answer, 17 Oct 2026 (S3 closed) |
| `projid` | `""` | Fixed, empty |
| `rel` | `"CL<YYYYMMDD>-<HH:mm>"` | `resp` code followed by the date and time (IST) of the generation run, for example `"CL20261017-14:05"`. One value per run, shared by every file of the run. Owner answer, 17 Oct 2026 |
| `resp` | `"CL"` | Fixed: CL = generated by Claude |
| `subTyp` | `""` | Fixed, empty (was `"PhantomStable"` up to v0.3) |
| `typ` | `"PageConfigStable"` | Fixed |
| `ver` | `""` | Fixed, empty |
| `clmnDoc` | Array with one document: the **first document** of `03_design/<module>/samples/<collection>.js`, copied as it is | Every key of the sample document in field-list order, including `_id`, site, `app` and audit keys and `null` values, with the BSON types of the sample (`ISODate`, `NumberInt`, `NumberLong`, `NumberDecimal`). Owner answer, 17 Oct 2026 |

File: `04_reference_data/ui_controls/table/PageConfigs/<collection>.json`.

## 6. `dictData.config` - fixed blocks

Every block except `column` and `tableSubTitle.title-label` is copied from the reference sample. Blocks and keys inside them are written in alphanumeric key order (section 7); the table lists the blocks in that order.

| Block | Content |
|---|---|
| `action` | `{}` (an object). Contents to be defined later by the owner |
| `column` | Section 4 |
| `footer` | `background-color` blue gradient, `display-pagination-control` true, `font-color` `#D0E2FF`, `font-family` Roboto Condensed, `font-size` 12px, `font-weight` bold, `noOfRows-visible` true, `pageNo-visible` true, `pagination-background-color` `#0d3070`, `pagination-border` `1px solid #314f85`, `pagination-color` `#E5F6FF`, `pagination-visible` true, `row-padding` 0px, `visible` true |
| `footerButtons` | `{}` |
| `footerMultiline` | `background-color` `#B9C6DF`; `multiCol` with one row: a `dataElement` (`colSize` 6.0, `key` text `From` in Roboto Condensed 300 18px `#ecf0f1` left, margin `1px 1px 1px 1px`; `val` text empty in weight 600) and a `blankSpace` (`colSize` 1.0). Inner keys sorted too |
| `header` | `background-color` `#4a4f59`, `font-color` `#125FCC`, `font-family` Roboto Condensed, `font-size` 14px, `font-weight` 100, `row-padding` `0px 0px 0px 2px`, `visible` true |
| `headerMultiline` | `{}` (was `null`) |
| `row` | `alternateRows` `stable-row-1` / `stable-row-2`, `background-color` `#FFFFFF`, `border-bottom` none, `border-bottom-color` `#DCD5D5`, `border-top-color` `#E74C3C`, `font-color` `#000000`, `font-family` Roboto Condensed, `font-size` 12px, `font-weight` 400, `row-padding` `0px 0px 0px 5px` |
| `rowAction` | `[]`. Contents to be defined later by the owner |
| `tableConfig` | `divAlignment` left, `divBackgroundColor` transparent / transparent, `exportToCsv` true, `exportToPdf` false, `innerLeftPadding` 15px, `innerRightPadding` 15px, `interval` `NumberInt(3000000)`, `isCheckable` **false** (default for every table), `isSearchable` true, `isSortable` true, `leftMargin` 0px, `line-color` `#2ECC71`, `noOfRows` **`NumberInt(10)`**, `pagination` **`NumberInt(8)`**, `tableWidth` 80%, `visible` true |
| `tableSubTitle` | `background` blue gradient, `display-download-icon` true, `display-search-control` true, `download-icon-color` `#0F62FE`, `font-color` `#FFFFFF`, `font-family` Roboto Condensed, `font-size` 16px, `font-weight` 400, `search-border-color` `0px solid #0d3070`, `search-inner-color` `#B9C6DF`, `title-icon` fa-list, `title-icon-color` `#FFFFFF`, `title-icon-size` 16px, `title-label` = screen label from `collection_type_matrix.md` (`Cleaning Records`), `visible` true |
| `tableTitle` | `font-color` `#B1B1B5`, `font-family` Roboto Condensed, `font-size` 30px, `font-weight` 600, `title-label` empty, `visible` false |
| `zenFuncs` | `dynamicActionBtn` **true**, `footerButtons` true, `footerMultiline` **true**, `headerMultiline` false |
| `zenPop` | `{}` |

Blue gradient: `linear-gradient(90deg, hsla(211, 100%, 28%, 1) 30%, hsla(236, 100%, 8%, 1) 100%)`.

No longer written (removed in the 17 Oct 2026 sample): `headerRoute` (block and `zenFuncs.headerRoute`).

## 7. Key order (owner answer, 17 Oct 2026: alphanumeric)

- Every object of the configuration is written with its keys in alphanumeric order: the top level (except `clmnDoc`, always last), `dictData`, `config`, every block inside `config`, nested objects (`footerMultiline.multiCol` elements, their `key` / `val` / `style`), and every column object.
- Sorting is by plain character code (as `sort_keys` in JSON tools): `_id` comes first at the top level; `-` sorts before letters, so `noOfRows` comes before `noOfRows-visible`, and `title-icon` before `title-icon-color`.
- Arrays keep their order: the `column` array keeps the column order of section 4.1, `alternateRows`, `divBackgroundColor` and `multiCol` keep the sample order.
- Exception 1: `clmnDoc` is the last top-level key, after `ver` (owner, 17 Oct 2026).
- Exception 2: the sample document inside `clmnDoc` keeps its own key order (field-list order), because it is a copy of a real document (open question S8).

## 8. Checklist per table

| # | Check |
|---|---|
| 1 | `_id` = `dictName` = `page` = `<collection without u_>Stable` = IvyConfig `stableName`; `typ` = `PageConfigStable`; `subTyp`, `ver`, `projid` = `""`; `resp` = `"CL"`; `rel` = `CL<YYYYMMDD>-<HH:mm>` of the run; `act` true; `app` `mes`; `module` = module code |
| 2 | `clmnDoc` is an array with exactly one document, equal to the first document of the collection's sample file (same keys, values and BSON types) |
| 3 | First column is `recordNo` with `fixed: "left"`; no other column is fixed |
| 4 | Every `data_index` is a key of the collection in the field list; none is `_id`, `app`, `siteId`, `siteName`, `schemaVersion`, `createdById`, `updatedById`, or an `...Id` key with a display key |
| 5 | Audit columns, where present, are the last four in the order createdBy, createdAt, updatedBy, updatedAt |
| 6 | Date columns have `YYYY-MM-DD`, Datetime columns `YYYY-MM-DD HH:mm:SS`, both with `isIST: true`; Boolean columns have `isBool: true` |
| 7 | Text left, numbers right, dates and Booleans centre |
| 8 | Every width is between 80px and 300px and a multiple of 10 |
| 9 | `tableSubTitle.title-label` is the screen label of `collection_type_matrix.md` |
| 10 | `zenFuncs` = `dynamicActionBtn` true, `footerButtons` true, `footerMultiline` true, `headerMultiline` false; no `headerRoute` anywhere; `headerMultiline` `{}`; `action` `{}`; `rowAction` `[]` |
| 11 | `tableConfig.pagination` = `NumberInt(8)`, `noOfRows` = `NumberInt(10)`, `isCheckable` false |
| 12 | Keys of every object (except the `clmnDoc` document) are in alphanumeric order, and `clmnDoc` is the last top-level key |
| 13 | The file parses as JSON once the shell constructors (`NumberInt`, `NumberLong`, `NumberDecimal`, `ISODate`) are read as values (the script checks this) |
| 14 | Keys with no sample value and reference keys without a display key are reported to the user |

## 9. Assumptions and open questions

### 9.1 Assumptions

| No. | Assumption |
|---|---|
| A1 | Alignment: text left, numbers right, dates and Booleans centre (owner confirmed 17 Oct 2026). |
| A2 | Glyph widths of 7 px (row, 12px) and 8 px (header, 14px) and 20 px for the sort icon. |
| A3 | Fixed blocks are copied from the sample as a valid document; the 17 Oct 2026 sample still has one trailing comma (after `"isIST" : true,` in the `dt` example column). |
| A4 | Audit columns `createdBy`, `createdAt`, `updatedBy`, `updatedAt` are shown at the end where the collection has them. |
| A5 | Keys inside `clmnDoc` are written with double quotes like the rest of the file (the owner's example used unquoted shell keys); values and types are unchanged. |

### 9.2 Open questions

| No. | Question |
|---|---|
| S5 | Is there a column attribute for decimal places or number format (for Decimal128 values such as `oeeTarget`, `taktTimeSec`)? How does the backend serialise Decimal128 for the table? |
| S7 | `tableWidth` `80%`: tables have 4 to 39 columns (800 to 7,550 px); confirm horizontal scrolling is expected. |
| S8 | Alphanumeric key order: confirm it also applies to the column objects (`align` first, `width` last) and that the `clmnDoc` document keeps field-list order. |

### 9.3 Closed questions

| No. | Answer |
|---|---|
| S1 | `_id` = collection without `u_` + `Stable`, equal to IvyConfig `stableName` (15 Oct 2026) |
| S2 | Datetime format `YYYY-MM-DD HH:mm:SS` as in the sample (17 Oct 2026) |
| S3 | `page` = `_id` (17 Oct 2026) |
| S4 | `pagination` `NumberInt(8)`, `noOfRows` `NumberInt(10)` (17 Oct 2026) |
| S6 | `footerMultiline` kept as in the sample and switched on (`zenFuncs.footerMultiline` true) (17 Oct 2026) |

## 10. Change log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 14 Oct 2026 | First issue: column selection (display keys only), attribute and title rules, computed widths capped at 300px, frame (`<collectionSuffix>Stable`, `PageConfigStable`), fixed blocks from FormatTable.json, generator `05_generator/gen_stable.py`, checklist, assumptions A1 to A4, open questions S1 to S7. Samples produced for Downtime Events, Alarms, Station Performance, Lines, Defect Codes | Claude |
| 0.2 | 15 Oct 2026 | Title rules extended (units Days, Inr, Mm; acronym SLA; small words lower case). Table configurations generated for all 21 Maintenance (`maint`) collections, column report `PageConfigs/column_report_maint.md`; the five 0.1 samples regenerated with the new title rules | Claude |
| 0.3 | 15 Oct 2026 | Owner changes: column attribute `DtFormat` renamed `dtFormat`; `_id` / `dictName` / `page` = collection name without `u_` + `Stable` (`mes_maint_cleaningRecordStable`), matching IvyConfig `stableName` (S1 closed); file name `PageConfigs/<collection>.json`; `rat` / `ratConfig` renamed `rowAction` / `action` (updated FormatTable.json). All 26 configurations renamed and regenerated | Claude |
| 0.4 | 17 Oct 2026 | Updated FormatTable.json (17 Oct 2026) and owner answers: new top-level keys `ver`, `projid` (empty), `rel` (`CL` + IST run time `YYYYMMDD-HH:mm`), `resp` (`CL` = generated by Claude), `clmnDoc` (first sample document); `subTyp` empty; `headerRoute` removed; `headerMultiline` `{}`; `zenFuncs.dynamicActionBtn` true, `footerMultiline` true; `action` `{}`; `tableConfig.isCheckable` false, `pagination` `NumberInt(8)`, `noOfRows` `NumberInt(10)`; datetime format `HH:mm:SS`; all keys in alphanumeric order (new section 7); column rules unchanged; S2, S3, S4, S6 closed; S8 opened. Configurations not yet regenerated | Claude |
| 0.5 | 17 Oct 2026 | `clmnDoc` moved to the end of the document (last top-level key, exception to the alphanumeric order); frame table, section 7 and checklist 12 updated. Generator updated; no configuration regenerated | Claude |
