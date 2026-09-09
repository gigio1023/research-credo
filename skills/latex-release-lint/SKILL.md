---
name: latex-release-lint
description: "Run the mechanical pre-release checks on LaTeX sources with a bundled script: TODO and FIXME markers, author note macros, merge-conflict markers, doubled words, '..' and '??' remnants, author names under blind review, LaTeX macros in the abstract, commented-out acknowledgments, and error/warning/undefined/missing lines in the build log. Use when the user asks to lint the paper source, check the tex before submitting, or when paper-release-checklist needs machine evidence. Reports file:line findings and edits nothing. NOT for the author's walkthrough of a release (paper-release-checklist) or for prose and argument review (writing-pass)."
---

# LaTeX Release Lint

Outcome: every check the script can make has been run on the paper's LaTeX sources (and build log when available), and the findings are reported verbatim with `file:line` so a reviewer can verify each one. The paper is not edited.

This skill automates the part of Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) that can be checked by a program. Which of his items are covered, how, and what stays manual is in [references/coverage.md](references/coverage.md). The items that need eyes, a PDF, or the call for papers belong to paper-release-checklist.

## Run

From the directory containing this SKILL.md:

```bash
python3 scripts/check_tex.py path/to/main.tex
python3 scripts/check_tex.py path/to/main.tex --log path/to/main.log
python3 scripts/check_tex.py path/to/main.tex --blind --author "Full Name" --author "Coauthor Name"
```

The script follows `\input` and `\include` from the root file, strips `%` comments before checking text, and prints one finding per line as `severity<TAB>file:line<TAB>message`, followed by a `summary` line. It needs Python 3.10 or newer and no packages. Exit code 1 means at least one error, 0 means none, 2 means bad usage (missing file, `--blind` without `--author`).

Severity meanings:

- `error`: must be fixed before release. TODO/FIXME/XXX text, `\todo`-style note macros, merge-conflict markers, an author name in a blind submission, and build-log lines containing `error` or `undefined`.
- `warning`: needs a look, may be legitimate. Doubled words (some are correct English), `..` that is not an ellipsis, `??` (usually an unresolved reference), LaTeX macros inside the abstract, an acknowledgments heading inside a comment, and build-log lines containing `warning` or `missing`.
- `info`: printed for the author to eyeball. The `\title{}` text and the abstract text.

## Rules

- Report what the script printed. Do not mark a check passed without its output, and do not summarize "no problems" when the script was not run on the final sources.
- If Python is unavailable, say so and hand the user the equivalent searches by hand (the patterns are listed in the coverage reference). Do not install anything to make the script run.
- The script does not know which doubled words are intentional or whether the title is correct. Pass those to the author; they are decisions, not defects.
- Rerun after the author edits. Findings are tied to line numbers that move.

## Output

1. The command that ran and the `summary` line.
2. All `error` lines, then all `warning` lines, verbatim.
3. The `info` lines (title, abstract) for the author to confirm.
4. What was not covered: no build log supplied, no author names supplied for blind review, or files the script could not resolve.
