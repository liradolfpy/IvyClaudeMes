#!/usr/bin/env python3
"""
log_decision.py - decision log and session handover helper (D073).

Keeps 00_governance/decision_log.md (decision table only) and
00_governance/session_handover.md (the latest handover note only) without
reading or retyping either file in a conversation.

Usage (from the repository root or anywhere):
  python3 05_generator/log_decision.py next
      prints the next free decision number, the last number and any duplicate numbers
  python3 05_generator/log_decision.py add "<decision>" "<reason>" "<source>" [--date "18 Oct 2026"]
      appends one row with the next number to the decision table; prints the number
  python3 05_generator/log_decision.py check
      lists duplicate and missing decision numbers
  python3 05_generator/log_decision.py handover <file.md | ->
      replaces session_handover.md with the given note (Markdown, from a file or stdin)
  python3 05_generator/log_decision.py show-handover
      prints the latest handover note
"""
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "00_governance", "decision_log.md")
HANDOVER = os.path.join(ROOT, "00_governance", "session_handover.md")
ROW = re.compile(r"^\| D(\d{3}) \|")


def numbers(lines):
    return [int(m.group(1)) for m in (ROW.match(l) for l in lines) if m]


def cell(text):
    return text.replace("|", "/").replace("\n", " ").strip()


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    lines = open(LOG, encoding="utf-8").read().split("\n")
    nums = numbers(lines)
    dup = sorted({n for n in nums if nums.count(n) > 1})
    cmd = argv[0]
    if cmd == "next":
        print("next D%03d | last D%03d | duplicates %s" % (max(nums) + 1, max(nums),
              ", ".join("D%03d" % n for n in dup) or "none"))
    elif cmd == "check":
        missing = sorted(set(range(1, max(nums) + 1)) - set(nums))
        print("decisions %d | duplicates %s | missing %s" % (len(nums), ", ".join("D%03d" % n for n in dup) or "none",
              ", ".join("D%03d" % n for n in missing) or "none"))
        return 1 if dup or missing else 0
    elif cmd == "add":
        args = argv[1:]
        date = datetime.date.today().strftime("%d %b %Y").lstrip("0")
        if "--date" in args:
            i = args.index("--date"); date = args[i + 1]; args = args[:i] + args[i + 2:]
        if len(args) != 3:
            raise SystemExit('add needs "<decision>" "<reason>" "<source>"')
        n = max(nums) + 1
        row = "| D%03d | %s | %s | %s | %s |" % (n, date, cell(args[0]), cell(args[1]), cell(args[2]))
        last = max(i for i, l in enumerate(lines) if ROW.match(l))
        lines.insert(last + 1, row)
        open(LOG, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        print("D%03d added" % n)
    elif cmd == "handover":
        src = sys.stdin.read() if argv[1] == "-" else open(argv[1], encoding="utf-8").read()
        text = "# Session handover note\n\nOnly the latest note is kept (project_working_rules.md section 7.3); earlier notes are in Git.\n\n" + \
               re.sub(r"^#+ *Session handover note\s*\n", "", src.strip()) + "\n"
        open(HANDOVER, "w", encoding="utf-8", newline="\n").write(text)
        print("session_handover.md written (%d characters)" % len(text))
    elif cmd == "show-handover":
        print(open(HANDOVER, encoding="utf-8").read())
    else:
        raise SystemExit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
