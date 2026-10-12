# Project working rules

Source: owner's requirements of 11 October 2026. These rules apply to every task in this project.

## 1. Ownership and approval

- The project is run by one person. There are no draft, current, superseded or review stages on any file or action.
- All actions and prompts are approved by default. Claude proceeds without asking for confirmation.
- Claude asks for clarification only when the answer is needed to complete dependent work. Otherwise Claude chooses, proceeds, and records the choice in `decision_log.md` or `assumptions_log.md`.

## 2. Standing authorization

Claude may, without asking again: inspect the project folders; list and search files; read project documents and collection specifications; verify them against the applicable rules; and run the prerequisite checks, consistency reviews and validations needed to carry out a requested stage.

If the application enforces an access or approval requirement, Claude follows it and states the specific action that was blocked. These rules do not change application permissions or bypass enforced access controls.

## 3. Folders

- Paths come from the project root and `Folder_Guide.md`.
- Optional folders are created only when needed.
- Supplied originals, requirements, designs and generated outputs stay in their assigned locations.
- `100_Self_Notes` and `99_Archive` are reference-only; their content is not project authority. Material promoted from them into current documentation is reviewed and the promotion recorded in `decision_log.md`.
- The folder is a Git repository. Earlier versions are retrieved from Git; files are overwritten in place rather than copied with version suffixes.

## 4. Order of authority

1. `00_governance/project_working_rules.md`, `data_modeling_standard.md`, `mongodb_output_rules.md` (the owner's requirements).
2. `00_governance/data_model_register.md` and `decision_log.md`.
3. `02_architecture` documents and `05_generator/model/flat_model.json`.
4. `03_design` collection specifications.
5. Everything else.

Where the project instructions stored in the Claude project settings differ from the files in level 1 (collection naming, nesting, audit keys), the level 1 files apply, because they are later.

## 5. Before any model or data work

Field-level specifications are documented and checked for consistency before use. Before accepting a document or generating sample or seed data, run `schema_review_checklist.md`. No frontend, backend, cloud or deployment technology is implied by any model document.

## 6. Carried over from the original project brief

- Reference product: Front Brake Caliper Assembly, LH; Tier-1 plant in Pune; process from gravity die casting to dispatch.
- No shortening, summarising or placeholders in specifications and data.
- State every assumption (in `assumptions_log.md`).
- Referential integrity: every reference points to an `_id` that exists.
- Dates form one coherent timeline over the two-week production period, stored as local plant time (IST) with the +0000 suffix, without UTC conversion (DATA-004, replaces 'IST stored as UTC').
- `data_model_register.md` is kept up to date and handed over at the end of each phase.

## 7. Session handover

A session is a Cowork **task** (or a Chat **conversation**). Work is done in one task per phase or work package. The project documents carry the memory between tasks; a task's own workspace is temporary and is cleared after a period of inactivity, so nothing is left only in a task's workspace or only in its conversation history.

### 7.1 Starting a task

The owner opens a new task with a brief in this form:

> Task: <phase or work package name>. Goal: <the outcome required>. Inputs: <any new files or instructions>. Connect E:\Ivy\Claude\ClaudeProjects\ClaudeMES. Follow section 7 of project_working_rules.md.

Before doing any work, Claude:

0. Checks that the project root folder `E:\Ivy\Claude\ClaudeProjects\ClaudeMES` is connected to the task. If it is not, Claude requests access to the root folder (not to single subfolders) and waits for the owner's approval. Folder access is granted per task and does not carry over from earlier tasks. If access is declined or the computer cannot be reached, Claude works on the project documents only and states, at the end of the task, which files were not written to the folder.
1. Reads the level 1 and level 2 files of section 4 in full: `project_working_rules.md`, `data_modeling_standard.md`, `mongodb_output_rules.md`, `data_model_register.md` and `decision_log.md`.
2. Reads `assumptions_log.md` and `Folder_Guide.md` where they are available.
3. Reads the latest **Session handover note** at the end of `decision_log.md` (section 7.3), if one exists, and continues from its open items.
4. Reads the generator sources the task will touch (for example `flatten_model.py`, `gen_specs.py`, `sample_universe.py`, `sample_rules.py`, `gen_samples.py`, `master_refs.py`, `keydict_text.py`, `keydict_num.py`, `entity_samples.py`, `ext_req01.py`, `ext_req01_samples.py`) from the project, not from memory of an earlier task.
5. States in its first reply, in a few lines: the documents read, the current collection count and key count from `data_model_register.md`, the last decision number in `decision_log.md`, and the plan for the task.
6. Uses the current conventions as recorded in those files and nothing older: collection names `u_mes_<moduleCode>_<singular camelCase>` (D002, D026); flat documents (D003); 16-digit numeric string `_id` (D029); `recordNo` as business identifier (D004); ten sample documents per collection (D030); sample period April to September 2026 with the production fortnight 15 to 26 September 2026 (D031); local plant time with the +0000 suffix (D035); new collections numbered after the last existing one and existing IDs never changed (D042); one BSON type per key name (D044).

### 7.2 During a task

- Changes to specifications are made in the generator sources and regenerated (D019), not hand-edited in output files.
- Every decision taken is added to `decision_log.md` with the next free number; every assumption to `assumptions_log.md`.
- Finished files are saved to the project as soon as they are complete, not only at the end of the task.

### 7.3 Ending a task

Before the task is closed, Claude:

1. Saves every changed or new file to the project and to its assigned location in the connected project root folder (per `Folder_Guide.md`), overwriting in place, so that the project documents and the Git folder hold the same content.
2. Updates `data_model_register.md` (collections, keys, business keys, master ID registry, counts) and hands it over to the owner.
3. Runs the checks the task affects (`schema_review_checklist.md`, the type consistency check in `flatten_model.py`, referential integrity and timeline checks on the samples) and records the result.
4. Appends a **Session handover note** to the end of `decision_log.md` with: date; task name; what was completed; files changed; collection and key counts after the task; last decision number; checks run and their result; open items and the recommended next task. Only the latest handover note is kept; the previous one is replaced.
5. Ends its final reply with the recommended brief for the next task, in the form of section 7.1.

### 7.4 When to start a new task

A new task is started when a phase or work package is complete, when the task changes to an unrelated subject, or when the conversation has become long enough that earlier content may be compacted. A long task is closed with section 7.3 and continued in a new task rather than carried on.
