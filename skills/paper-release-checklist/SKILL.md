---
name: paper-release-checklist
description: "Run the pre-release checklist on a LaTeX paper before a conference submission, camera-ready, or arXiv upload: title, TODO and FIXME notes, merge-conflict markers, doubled words, unresolved references, captions, anonymity, page and formatting rules, author names, copyright block, abstract macros. Use when the user says 'submit', 'upload to arXiv', 'camera-ready', or 'final check on the paper'. NOT for content review (writing-pass) or fixing bibliography formatting."
---

# Paper Release Checklist

Outcome: a pass/fail table for the release type at hand, every mechanical item backed by a script finding or a quoted line, every manual item marked done by the user or left open, and no item marked passed without evidence. The paper is not edited unless the user asks.

The list is adapted from Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html), whose rule is that each embarrassing mistake gets added to the list so it is made only once. When the user reports a new mistake, add it to [references/checklist.md](references/checklist.md) with a date.

## Steps

1. Identify the release type: conference submission, public release (camera-ready), or arXiv upload. Each adds a section of the manual list.
2. Run the mechanical checks from the directory containing this SKILL.md:

   ```bash
   python3 scripts/check_tex.py path/to/main.tex
   python3 scripts/check_tex.py path/to/main.tex --blind --author "Full Name" --author "Coauthor Name"
   ```

   The script follows `\input` and `\include`, strips comments, and reports `error`, `warning`, and `info` lines as `severity  file:line  message`. It needs Python 3.10 or newer and no packages. Exit code 1 means at least one error. If Python is unavailable, run the equivalent greps by hand and say so.
3. Walk the manual items for the release type in [references/checklist.md](references/checklist.md). Items that need the rendered PDF (orphan lines, fonts, figure legibility, page count against the limit) require the user to open the PDF; ask them and record their answer.
4. Report.

## Output

| Item | Result | Evidence |
| --- | --- | --- |
| e.g. No TODO/FIXME | fail | `error  sec/eval.tex:41  TODO marker` |
| e.g. Title correct | pass (user confirmed) | `\title{...}` as printed by the script |

Errors block release; warnings need a look; info lines are for eyeballing. State plainly which manual items were not verified. Do not summarize a check as passed because the script ran; the evidence column must hold the line or the user's confirmation.
