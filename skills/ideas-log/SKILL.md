---
name: ideas-log
description: "Capture a research idea into an append-only ideas log the moment it comes up ('add this to my ideas', 'note this for later', or an idea that would pull the user off their current task), and re-read the log only when the user is choosing a next project or asks for a review pass. The log is write-mostly on purpose so every idea is judged twice, months apart. NOT for task lists, meeting notes, or deciding whether an idea is good right now (use conclusion-first or research-credo for that)."
---

# Ideas Log

Outcome: the idea is written down in the user's ideas file with today's date and enough context to judge it later, and the user returns to what they were doing. When the user is picking a next project, the outcome is a dated review entry classifying the older ideas.

The habit is adapted from Carlini's [ideas.txt post](https://nicholas.carlini.com/writing/2024/my-research-logfile.html): only ideas the author believes are good go in, entries are appended and never edited, and the file is read a few times a year so the time gap does the filtering.

## Locate the log

Use the path the user names. Otherwise use `~/research/ideas.txt`; if it does not exist, ask once before creating it and remember the answer for the session. The log is user data. Never move, reformat, or deduplicate it.

## Append an entry

Append at the end of the file:

```
## 2026-09-09  One line naming the problem worth solving
- why it might matter: ...
- what makes it possible now (new tool, dataset, result): ...
- where it came from (conversation, paper, task): ...
- nearest prior work I know of: ... (or "unknown")
```

Rules that change behavior:

- Record the problem, not the solution. Carlini noted his early entries described how to solve things and later ones what was worth solving; the second kind aged better. If the user gives a solution, ask what problem it would settle and record that first.
- Only ideas the user currently believes are good. Do not log every passing thought; the file holds candidates for future projects, nothing else.
- Append only. Do not edit, reorder, merge, or delete past entries, even to fix typos. Corrections and updates are new dated entries that name the earlier date.
- Do not evaluate the idea now. Confirm the append and return the user to their current task. Evaluation is a separate act with a separate skill.

## Review pass (only when choosing the next project, or on request)

1. Read entries older than about three months first; the gap is the filter. Newer entries are read last and weighed less.
2. For each entry classify: still worth doing / done by someone else since / no longer matters / do next. Ask the user for the classification when it depends on knowledge you lack; do not guess about what others have published.
3. Append one dated review entry listing the classifications. Do not annotate the original entries in place.
4. Hand any "do next" candidate to conclusion-first for the gate.

## Output

Confirm the file path and the line range appended. In a review pass, report the counts per class and the "do next" list. If the file could not be found or written, say so and give the entry text so the user can paste it.
