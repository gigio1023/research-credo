---
name: paper-release-checklist
description: "Walk the author through the human checks before a conference submission, camera-ready, or arXiv upload: title correct, PDF renders on another machine, no orphan lines, captions readable alone, page limit and numbering per the call for papers, anonymity, author names and affiliations, copyright block, template version, acknowledgments, arXiv form fields. Every item is confirmed by the author, not inferred by the agent. Use when the user says 'submit', 'camera-ready', 'arXiv upload', or 'final check'. NOT for the mechanical source checks (latex-release-lint runs those first) or for content and prose review (paper-plan)."
---

# Paper Release Checklist

Outcome: for the release type at hand, every manual item has been put in front of the author and recorded as confirmed, open, or not applicable, with the machine-checkable items already covered by latex-release-lint evidence. Nothing is ticked on the author's behalf.

The list is adapted from Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html). His rule is that each embarrassing mistake, once made, is added to the list so it happens only once. Items that a program can check were moved to latex-release-lint; the items here are the ones that need a person, a rendered PDF, the build, or the call for papers. The manual items live in [references/checklist.md](references/checklist.md).

## Steps

1. Identify the release type: conference submission, public release (camera-ready), or arXiv upload. Each adds a section of the list.
2. Get the machine evidence first. If the LaTeX sources are available, have latex-release-lint run and attach its error and warning lines; do not repeat those checks by eye. If sources are not available, note that the mechanical items are unverified.
3. Walk the manual items for "every release" and for the release type, one at a time. For each item state what the author should look at (which page, which form field, which file), then record their answer. Items that need the PDF require the author to open it; do not infer layout from the source.
4. Record. An item is "confirmed" only when the author said so, "open" when they have not checked it or found a problem, "n/a" when the release type does not need it.
5. When the author reports a mistake that no item would have caught, append it to [references/checklist.md](references/checklist.md) under "Added later" with the date. That is the point of the list.

## Output

| Item | Result | Note |
| --- | --- | --- |
| e.g. Page count within limit (9 + refs) | confirmed by author | 8.5 pages content |
| e.g. Fonts render on another machine | open | not yet checked |
| e.g. Mechanical checks | see latex-release-lint | 0 errors, 2 warnings reviewed |

Open items block the release. List them first. Do not rewrite the paper; if an item fails, say what to fix and let the author do it or ask for paper-plan.
