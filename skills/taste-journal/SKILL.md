---
name: taste-journal
description: "Keep the record that trains research taste: append problems worth solving, predictions made at decisions (why it will work, what will kill it, what reviewers will ask), and hindsight notes when outcomes arrive. Use when a long-horizon idea appears, a project decision is made, a result or review comes back, or the user is choosing what to do next. Append-only; re-read on a schedule, not daily. NOT for task tracking, meeting notes, or near-term deliverables."
---

# Taste Journal

Outcome: the idea, prediction, or hindsight is appended to the user's journal with today's date, and the user returns to what they were doing. Over months, the journal lets the user see which of their judgments held, which is the only way the essay says taste is built.

Scope: long-horizon work only, per the repository's `AGENTS.md`. Near-term tasks do not go in.

The habit extends Carlini's [ideas.txt](https://nicholas.carlini.com/writing/2024/my-research-logfile.html): an append-only file of problems worth solving, read a few times a year so that every idea is judged twice with time between, and annotated in hindsight years later. This skill adds the predictions made at decisions so hindsight has something to compare against.

## Locate the journal

Use the path the user names; otherwise `~/research/journal.md`. If it does not exist, ask once before creating it. The journal is user data: never reformat, reorder, deduplicate, or edit past entries.

## Three kinds of entry

Append at the end of the file. Never modify earlier text; corrections are new dated entries that name the earlier date.

```
## 2026-09-09 idea: One line naming the problem worth solving
- why it might matter: ...
- what makes it possible now: ...
- where it came from: ...

## 2026-09-09 prediction: Project or decision name
- decision: continue / start / kill / pivot / submit to X
- why I expect it to work: ...
- what would kill it: ...
- what a skeptical reviewer will ask: ...
- months ahead of the next person, my guess: ...

## 2026-09-09 hindsight: Project or decision name (prediction 2026-06-02)
- what happened: ...
- what I judged right, what I judged wrong: ...
- what I would ask myself earlier next time: ...
```

Rules that change behavior:

- Ideas record problems, not solutions. If the user brings a solution, ask what problem it would settle and record that first.
- A prediction is taken at every decision the `taste` or `conclusion-first` conversation ends with. Ask for it in one question; do not draft it for the user.
- When a result, review, or acceptance arrives, find the matching prediction and read it back to the user before discussing the outcome. Then append the hindsight entry in their words.
- Do not evaluate an idea at capture time. Append and return the user to their task.

## Re-read on a schedule, not daily

The journal is read in two situations only: when the user is choosing what to do next, and during the monthly `distribution-review`. In both, read entries older than about three months first; the gap is the filter. Do not surface journal entries unprompted during ordinary work.

## Output

Confirm the path and the line range appended, or the prediction read back. If the file cannot be written, give the entry text so the user can paste it.
