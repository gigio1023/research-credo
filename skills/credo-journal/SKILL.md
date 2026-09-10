---
name: credo-journal
description: "Keep the record that trains research taste and run the monthly review on it: append ideas (problems worth solving), predictions made at decisions, hindsight when outcomes arrive, and a monthly review of the long-horizon portfolio (which one or two efforts could be great, what dies, months-ahead guesses). Use when an idea appears, a decision is made, a result or review comes back, or monthly and for 'what should I be working on'. Append-only through the bundled script. NOT for task tracking, meeting notes, or near-term deliverables."
---

# Credo: Journal

Outcome: the idea, prediction, hindsight, or monthly review is appended to the user's journal with today's date, and the user returns to what they were doing. Over months the journal shows which judgments held. The essay says taste is built by attending to what worked and what did not; this file is where that attention lands.

The habit extends Carlini's [ideas.txt](https://nicholas.carlini.com/writing/2024/my-research-logfile.html): append-only, problems rather than solutions, read a few times a year so each idea is judged twice with time between, annotated in hindsight. Predictions are added so hindsight has something to compare against.

## Scope

Long-horizon work only (an uncertain claim or direction, a quarter or longer or a multi-month improvement the user owns, no deadline inside the next few weeks). Near-term tasks do not go in.

## Locate the journal

Use the path named in the project's `AGENTS.md` owner settings, else the path the user names, else `~/research/journal.md`. The journal is user data: never reformat, reorder, deduplicate, or edit past entries. Corrections are new dated entries that name the earlier date.

## Append with the script

From the directory containing this SKILL.md:

```bash
python3 scripts/journal.py append --kind idea --title "One line naming the problem" \
  --field "why it might matter=..." --field "what makes it possible now=..." --field "where it came from=..."
python3 scripts/journal.py append --kind prediction --title "Project or decision" \
  --field "decision=continue" --field "why I expect it to work=..." --field "what would kill it=..." \
  --field "what a skeptical reviewer will ask=..." --field "months ahead, my guess=..."
python3 scripts/journal.py append --kind hindsight --title "Project (prediction 2026-06-02)" \
  --field "what happened=..." --field "judged right, judged wrong=..." --field "what I would ask earlier=..."
python3 scripts/journal.py read --older-than 90
```

Add `--path <file>` when the journal is not at the default location. The script opens the file in append mode only, stamps today's date, and refuses unknown kinds; it needs Python 3.10 or newer and no packages. If Python is unavailable, append by hand in the same shape (`## YYYY-MM-DD kind: title` followed by `- field: value` lines) and say so.

## Rules that change behavior

- Ideas record problems, not solutions. If the user brings a solution, ask what problem it would settle and record that first. Only ideas the user currently believes are good.
- A prediction is taken at every decision a credo-taste conversation ends with. Ask for it in one question; do not draft it for the user.
- When a result, review, or acceptance arrives, read the matching prediction back to the user before discussing the outcome, then append the hindsight in their words.
- Do not evaluate an idea at capture time. Append and return the user to their task.
- Do not surface entries unprompted during ordinary work. The journal is read only when choosing what to do next and during the monthly review.

## Monthly review

Inputs: the user's list of long-horizon efforts in flight or parked, and the journal read with `--older-than 90` first; predictions with no matching hindsight are raised first. Ask one question per turn:

1. Which one or two of these could be great? The essay expects one or two a year; the rest are practice.
2. For each effort: is the core still working, does the best-case conclusion still matter, has anything more important appeared? Kill or park what fails; name what is salvaged.
3. For each survivor: how many months ahead of the next person is it now, against the last guess in the journal? Has the area's importance moved?
4. Anything rejected or null since last time: premise or argument? What in the distribution would you change, and what is just the sample?
5. Is the main effort where the user's skill and the area's current importance meet?

Stop after these five, or earlier when the user has said what changes next month. Append one `review` entry in the user's words: the great candidates, what was killed or parked and why, the months-ahead guesses, and the one change for next month. Then one line naming the first action for the coming week.

## Output

Confirm the path and the appended entry heading, or the prediction read back. If the file cannot be written, give the entry text for the user to paste.
