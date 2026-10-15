---
name: stable
description: Stable (StandardTable) - build the React table page configuration (typ PageConfigStable) that lists a MES collection's documents, from the collection's field list and sample documents.
---

# Stable (StandardTable) - table page configuration

Skill version: 0.1 | 14 October 2026 | Model version 2.9 (369 collections, 8,614 keys including `app`)
Sibling instruction: `04_reference_data/ui_controls/query_control_instruction.md` (query controls of the same list screens). Keep the two consistent.
Reference copy of this skill in the repository: `04_reference_data/ui_controls/table/stable_skill.md`.

## 1. Purpose

Every list screen of the MES React application shows the documents of one collection in a table. The table is rendered from a page configuration document stored in the collection `PageConfig` and served by `/miscellaneous/pageconfig`. This skill produces that document for one or more collections: which keys become columns, in what order, with which title, width, alignment and format, inside a fixed frame copied from the reference sample `04_reference_data/ui_controls/table/FormatTable.json`.

## 2. Inputs (all in the ClaudeMES repository, `E:\Ivy\Claude\ClaudeProjects\ClaudeMES`)

| Input | Location | Used for |
|---|---|---|
| Field lists | `02_architecture/field_lists/<nn>_<module>_field_list.md` | Keys in model order, BSON type, date tag (Date / Datetime), reference target |
| Collection type matrix | `02_architecture/collection_type_matrix.md` | Module code, screen type, screen label (table title) |
| Sample documents | `03_design/<module>/samples/<collection>.js` | Longest displayed text per key (column width) |
| Specifications | `03_design/<module>/specs/<collection>.md` | Meaning, allowed values, nullability when a rule needs checking |
| Reference sample | `04_reference_data/ui_controls/table/FormatTable.json` | Frame and fixed styling values |
| Generator | `05_generator/gen_stable.py` | Applies every rule of this skill |

## 3. How to run

1. Work on the user's computer through the device shell (`$HOME/mnt/ClaudeMES`).
2. Run `python3 05_generator/gen_stable.py <collection> [<collection> ...]` from the repository root. Collection names are the full model names (`u_mes_perf_downtimeEvent`).
3. The script writes `04_reference_data/ui_controls/table/PageConfigs/PageConfig_<collection>.json` (MongoDB shell style, `NumberInt`) and prints a column report: data_index, title, type, longest sample text, width, alignment, the keys left out and why, and keys that had no sample value.
4. Run the checklist (section 7) on the report and the file. Show the user the column report, and list anything the checklist flagged.
5. If a rule must change, change it in this skill **and** in `gen_stable.py` together, raise the skill version, add a change-log row (section 9) and update the reference copy `stable_skill.md`.
6. If the device shell or the script is not available, apply sections 4 to 6 by hand with the same inputs; never invent keys that are not in the field list.

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

The model is flat (DATA-001): every key is a top-level scalar, so there are no array or embedded columns.

### 4.2 Attributes per column

Attribute order inside each column object: `title`, `fixed` (first column only), `width`, `align`, `DtFormat`, `isIST`, `isBool`, `data_index`.

| BSON type (date tag) | `align` | Extra attributes |
|---|---|---|
| String | `left` | - |
| Int32, Int64, Decimal128, Double | `right` | - (decimal formatting: open question S5) |
| Date (Date) | `center` | `"DtFormat" : "YYYY-MM-DD"`, `"isIST" : true` |
| Date (Datetime) | `center` | `"DtFormat" : "YYYY-MM-DD HH:mm:ss"`, `"isIST" : true` |
| Boolean | `center` | `"isBool" : true` |

- `data_index` is the exact key name of the collection.
- `isIST: true` means the value is shown as stored (owner answer, 14 Oct 2026). Specifications store dates as IST wall-clock with the `+0000` suffix, so no shift is applied.
- Date format uses lower-case `ss` for seconds. The reference sample writes `HH:mm:SS`; in moment / dayjs `SS` means fractions of a second (open question S2).
- The reference sample centres every column; this skill aligns text left and numbers right (assumption A1).

### 4.3 Title

1. `recordNo` gives `Record No`.
2. A display key `xName` whose `xId` exists loses `Name`: `equipmentName` gives `Equipment`, `capaName` gives `CAPA`.
3. A leading `is` is dropped: `isPlanned` gives `Planned`.
4. A unit suffix becomes a bracket: `Minutes` gives `(min)`, `Seconds` / `Sec` give `(s)`, `Hours` give `(h)`, `Percent` / `Pct` give `(%)`: `durationMinutes` gives `Duration (min)`, `taktTimeSec` gives `Takt Time (s)`.
5. camelCase is split into Title Case words; known acronyms are upper case (OEE, CAPA, WIP, PFMEA, IoT, MTBF, MTTR, FPY, PPM, RPN, SPC and the others in the `ACRONYMS` table of the script).
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

## 5. Document frame

| Field | Value | Rule |
|---|---|---|
| `_id` | `<collectionSuffix>Stable` | Collection name without `u_<app>_<module>_`, followed by `Stable`: `u_mes_perf_downtimeEvent` gives `downtimeEventStable` |
| `lid` | `"lid_999"` | Retained from the reference sample |
| `dictName` | Same as `_id` | `downtimeEventStable`, `alarmStable`, `workCenterPerformanceStable` |
| `typ` | `"PageConfigStable"` | Fixed |
| `page` | Same as `_id` | Follows the reference sample, where `page` equals `_id` (open question S3) |
| `app`, `module` | `"mes"`, module code | As the owner added to the query page configurations (`perf`, `mast`, `qual`, ...) |
| `dictData.config` | Section 6 | |
| `subTyp` | `"PhantomStable"` | Retained |
| `act` | `true` | Retained |

File: `04_reference_data/ui_controls/table/PageConfigs/PageConfig_<collection>.json`.

## 6. `dictData.config` - fixed blocks

Every block except `column` and `tableSubTitle.title-label` is copied exactly from the reference sample (`build_document` in `gen_stable.py`).

| Block | Content |
|---|---|
| `headerRoute`, `headerMultiline` | `null` |
| `footerMultiline` | `background-color` `#B9C6DF`; one row `multiCol` with a `dataElement` (`colSize` 6.0, key text `From` in Roboto Condensed 300 18px `#ecf0f1`, value text empty in weight 600) and a `blankSpace` (`colSize` 1.0) |
| `tableTitle` | Hidden (`visible: false`), empty label, Roboto Condensed 600 30px `#B1B1B5` |
| `tableSubTitle` | Visible; `title-label` = screen label from `collection_type_matrix.md` (`Downtime Events`); Roboto Condensed 400 16px white on the blue gradient; download icon `#0F62FE`; search control (border `0px solid #0d3070`, inner `#B9C6DF`); icon `fa-list` 16px white |
| `tableConfig` | `visible` true, `tableWidth` `80%`, `divBackgroundColor` transparent / transparent, `divAlignment` left, `leftMargin` 0px, inner padding 15px / 15px, `line-color` `#2ECC71`, searchable, sortable, `pagination` `NumberInt(8)`, `exportToPdf` false, `exportToCsv` true, `noOfRows` `10.0`, `interval` `NumberInt(3000000)` |
| `header` | `#4a4f59`, Roboto Condensed 100 14px `#125FCC`, padding `0px 0px 0px 2px`, visible |
| `footer` | Blue gradient, Roboto Condensed bold 12px `#D0E2FF`, padding 0px, pagination control, colour `#E5F6FF`, background `#0d3070`, border `1px solid #314f85`, rows and page number visible |
| `row` | White, padding `0px 0px 0px 5px`, Roboto Condensed 400 12px black, border colours `#DCD5D5` / `#E74C3C`, `border-bottom` none, alternate rows `stable-row-1` / `stable-row-2` |
| `column` | Section 4 |
| `rat`, `ratConfig` | `[]` |
| `zenPop`, `footerButtons` | `{}` |
| `zenFuncs` | `headerRoute` false, `footerMultiline` true, `headerMultiline` false, `footerButtons` true |

Blue gradient: `linear-gradient(90deg, hsla(211, 100%, 28%, 1) 30%, hsla(236, 100%, 8%, 1) 100%)`.

## 7. Checklist per table

| # | Check |
|---|---|
| 1 | `_id` = `dictName` = `page` = `<collectionSuffix>Stable`; `typ` = `PageConfigStable`; `subTyp` = `PhantomStable`; `act` true |
| 2 | First column is `recordNo` with `fixed: "left"`; no other column is fixed |
| 3 | Every `data_index` is a key of the collection in the field list; none is `_id`, `app`, `siteId`, `siteName`, `schemaVersion`, `createdById`, `updatedById`, or an `...Id` key with a display key |
| 4 | Audit columns, where present, are the last four in the order createdBy, createdAt, updatedBy, updatedAt |
| 5 | Date columns have `YYYY-MM-DD`, Datetime columns `YYYY-MM-DD HH:mm:ss`, both with `isIST: true`; Boolean columns have `isBool: true` |
| 6 | Text left, numbers right, dates and Booleans centre |
| 7 | Every width is between 80px and 300px and a multiple of 10 |
| 8 | `tableSubTitle.title-label` is the screen label of `collection_type_matrix.md` |
| 9 | The file parses as JSON once `NumberInt(n)` is read as `n` (the script checks this) |
| 10 | Keys with no sample value and reference keys without a display key are reported to the user |

## 8. Assumptions and open questions

### 8.1 Assumptions

| No. | Assumption |
|---|---|
| A1 | Alignment: text left, numbers right, dates and Booleans centre (the sample centres everything). |
| A2 | Glyph widths of 7 px (row, 12px) and 8 px (header, 14px) and 20 px for the sort icon. |
| A3 | Fixed blocks are copied from the sample as a valid document; the sample itself does not parse (trailing commas in `footerMultiline`, after `isIST` and `act`; missing comma after `ratConfig`). |
| A4 | Audit columns `createdBy`, `createdAt`, `updatedBy`, `updatedAt` are shown at the end where the collection has them. |

### 8.2 Open questions

| No. | Question |
|---|---|
| S1 | The IvyConfigs hold `stableName` = `mes_perf_downtimeEventStable`, but the table `_id` / `dictName` is now `downtimeEventStable`. Should IvyConfig `stableName` change to `<collectionSuffix>Stable`? |
| S2 | Does the React table use moment / dayjs tokens? If yes, `HH:mm:ss` is right and the sample's `HH:mm:SS` should be corrected. |
| S3 | `page`: same as `_id` (sample) or `"Phantom"` (query page configurations)? |
| S4 | `tableConfig.pagination` is 8 while `noOfRows` is 10.0: which one sets the rows per page, and should `noOfRows` be `NumberInt`? |
| S5 | Is there a column attribute for decimal places or number format (for Decimal128 values such as `oeeTarget`, `taktTimeSec`)? How does the backend serialise Decimal128 for the table? |
| S6 | Is `footerMultiline` (`From` data element) meant to show the query's from-date? Should a `To` element be added? |
| S7 | `tableWidth` `80%`: tables have 13 to 35 columns (2,400 to 6,100 px); confirm horizontal scrolling is expected. |

## 9. Change log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 14 Oct 2026 | First issue: column selection (display keys only), attribute and title rules, computed widths capped at 300px, frame (`<collectionSuffix>Stable`, `PageConfigStable`), fixed blocks from FormatTable.json, generator `05_generator/gen_stable.py`, checklist, assumptions A1 to A4, open questions S1 to S7. Samples produced for Downtime Events, Alarms, Station Performance, Lines, Defect Codes | Claude |
