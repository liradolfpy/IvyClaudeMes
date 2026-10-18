# Token optimisation review - UI configuration work and skills

Date: 18 October 2026 | Decision: D073 | Requested by the owner after the PlanningAndExecution query task (D066, D067) and the skill change of D071.

## 1. Where the tokens went (estimates from the two sessions)

| Step | Approx. tokens | What happened | Needed for a UI task? |
|---|---|---|---|
| Start-up reading (rules section 7.1) | ~45k | Full reads of decision log, modeling standard, output rules, register, assumptions, profile, Folder_Guide | Mostly no: the model does not change in a UI task |
| Skill loading | ~30k | Account skill (0.18) loaded, then the library copy 0.19 and its change log read again | Only the core, once |
| Module field list | ~31k | 1,529 lines read to choose the controls | No: a script reduces it to about 3k |
| Query key strategy | ~7k | Read in full | No: the skill holds the rules that matter |
| Generator writing | ~12k | One-off | Done |
| Skill review card | ~40k | The 43 KB skill retyped twice for a two-number change, plus a read of the installed copy | No |
| Governance edits | ~10k | Long handover note, repeated staging and committing | Partly |

Every tool call resends the conversation so far, so a large read early in a task keeps costing tokens until the end of the task.

## 2. Measures implemented (D073)

1. **Generator-driven query work.** `05_generator/gen_query.py --digest <module>` prints one line per collection; `--propose <module>` drafts the SCREENS entries with the skill's rules and the D067 readings; `--compare <module>` shows the difference from decided entries; decisions live in `05_generator/query_screens.py`. On PlanningAndExecution the draft reproduces 30 of 43 decided screens exactly; the rest differ by one or two judgement calls. Digest plus draft for a module of 27 collections: about 12 KB of text instead of a 62 KB field list.
2. **Slim skills.** `mes-query-control` 0.21: core 10 KB (was 43 KB), every rule kept; templates, attribute table, registry, MasterDict and worked example in `references/`, read only when needed. Section 0 of the core holds the token rules.
3. **Pointer account skills.** `mes-query-control`, `mes-ivy-config`, `mes-stable-table`, `mes-menu-builder` and `skill-library-sync` are installed as short pointers that read the library file. A rule change is a library edit with no review card (`skill-library-sync` 1.2).
4. **Task-type reading lists.** `project_working_rules.md` section 7.1: read the handover note and what the task type needs; search other governance files instead of reading them; `log_decision.py next` instead of reading the decision log.
5. **Records by script.** `05_generator/log_decision.py` adds decision rows with the next free number (and reports duplicates such as the two D069 rows) and writes `00_governance/session_handover.md`, which now holds the latest handover note outside the decision log.
6. **In-place editing.** Files on the connected computer are edited with short scripts; container-to-computer commits are verified with `md5sum`, because a commit was seen to deliver the previous version of a file.

## 3. Expected effect

| Work | Before | After |
|---|---|---|
| Query and IvyConfigs for one module | ~150k | ~15-25k |
| Small skill rule change | ~40-50k | ~2-5k |
| Task start-up (UI task) | ~75k | ~10k |

## 4. Open points

- The other skills (`mes-stable-table` 15 KB, `mes-menu-builder` 23 KB) are pointers now but their library cores are not yet slimmed; the menu skill's 130-line validator could move into `gen_menu.py --check` or `references/`.
- `gen_query.py` keeps `colSize` 8 / `labelColSpan` 8 until the existing configurations are regenerated to the 0.20 standard (D071).
- Several modules can now be handled in one task (for example `matl`, `trac`, `ehs`).
