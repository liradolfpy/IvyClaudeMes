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
