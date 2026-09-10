---
name: credo-release
description: "Check a LaTeX paper before a conference submission, camera-ready, or arXiv upload in two separated phases: a bundled script for everything a program can catch (TODO markers, merge-conflict markers, doubled words, '..' and '??', author names under blind review, abstract macros, commented-out acknowledgments, build-log errors), then the human items the author confirms one by one (title, layout orphans, captions, fonts, page limits, anonymity beyond names, author block, copyright, template, arXiv form). Use for 'submit', 'camera-ready', 'arXiv', 'final check', 'lint the tex'. NOT for content or structure review (credo-paper-plan)."
---

# Credo: Release

Outcome: a release table for the paper in which every mechanical item carries a script finding or a quoted line, every manual item is recorded as confirmed by the author, open, or not applicable, and nothing is marked passed without evidence. The paper is not edited.

Adapted from Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html): a list the author runs before every release, grown by adding each mistake once it has been made. Which of his items a program can check and which need a person is recorded in [references/coverage.md](references/coverage.md); read it if the author asks why an item is where it is.

This is the one procedural skill in the pack. It applies to any paper the user is releasing, not only long-horizon work.

## Phase A: what the script catches

From the directory containing this SKILL.md:

```bash
python3 scripts/check_tex.py path/to/main.tex --log path/to/main.log
python3 scripts/check_tex.py path/to/main.tex --blind --author "Full Name" --author "Coauthor Name"
```

The script follows `\input` and `\include`, strips `%` comments, optionally scans the build log, and prints `severity<TAB>file:line<TAB>message` lines plus a `summary`. Python 3.10 or newer, no packages. Exit 1 means at least one error, 2 means bad usage.

- `error`: fix before release. TODO/FIXME/XXX, `\todo`-style macros, merge-conflict markers, an author name under `--blind`, build-log lines with `error` or `undefined`.
- `warning`: look at it. Doubled words (some are correct), `..` that is not an ellipsis, `??`, macros in the abstract, an acknowledgments heading inside a comment, build-log `warning` or `missing`.
- `info`: for the author to eyeball. The `\title{}` text and the abstract text.

Report the command, the summary line, then every error and warning verbatim. Rerun after edits; line numbers move. If Python is unavailable, run the grep equivalents in the coverage reference by hand and say so.

## Phase B: what the author confirms

Identify the release type (submission, camera-ready, arXiv) and walk the items for "every release" plus that type in [references/manual-checklist.md](references/manual-checklist.md), one at a time. For each, say what to look at (which page, form field, or file) and record the author's answer. Items that need the rendered PDF require the author to open it; do not infer layout from source. "Confirmed" only when the author said so; "open" when unchecked or failing; "n/a" when the release type does not need it.

When the author reports a mistake no item would have caught, append it with the date under "Added later" in the manual checklist. That is how the list is supposed to grow.

## Output

| Item | Result | Evidence or note |
| --- | --- | --- |
| No TODO/FIXME | fail | `error  sec/eval.tex:41  TODO/FIXME/XXX text` |
| Page count within limit | confirmed by author | 8.5 content pages |
| Fonts render on another machine | open | not yet checked |

Open items block the release; list them first. Do not rewrite the paper; if an item fails, say what to fix and let the author do it, or hand structure problems to credo-paper-plan.
