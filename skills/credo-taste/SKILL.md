---
name: credo-taste
description: "Think through a long-horizon research decision the way Carlini's essay does: which problem is worth months, whether an idea is yours to do, when to kill or pivot, how a paper will land. Use when the user is choosing a direction, weighing an idea, stuck mid-project, or asks 'is this worth it'. One question at a time, reasons in prose, ends when the user can state their own judgment. For long-horizon work only; NOT for this week's deliverables, tickets, or deadline-driven tasks, and NOT a scoring rubric."
---

# Taste

Outcome: the user states, in their own words, what they will do and why, having been asked the questions Carlini asks himself at the same moment. The agent does not hand down a verdict or a score; it asks, offers an analogy from his career when one fits, and stops when the user's judgment is articulated.

Scope: long-horizon work only, as defined in the repository's `AGENTS.md`. If the work is a near-term deliverable, say so and do not run this skill.

Sources: [references/tenets.md](references/tenets.md) holds the stances with the owner's position on each; [references/episodes.md](references/episodes.md) holds the episodes from the essay used as analogies. Read both once, then keep them out of the conversation except as analogies.

## How the conversation runs

- One question at a time. Wait for the answer before the next. Do not list all questions at once.
- Pick the moment first, then the questions for it (table below). Skip questions the user has already answered.
- When the user's situation resembles an episode, say which and what the move was, then ask what the analog is here. Do not force an analogy.
- No scores, no weights, no rubric totals. If the user asks for a score, explain that the essay's point is that taste is trained, not computed, and give the reasons instead.
- End when the user can say what they will do and why. Then offer, in one line, to record the judgment and its prediction with `credo-journal`.

## Questions by moment

| Moment | Questions Carlini asks himself |
| --- | --- |
| Looking for a problem | What in this literature makes you want to shout that everyone is doing it wrong? If you do not do this, how many months until someone else does? Is this a corner where you are unusually strong, or a hot area where you would be one of many? |
| Holding one idea | If every experiment succeeded, what would the conclusion say beyond a number going up? Can you state the idea in one sentence without an "and"? Which sub-problem is most likely to fail, and can you try it first in days? Hand off to `credo-conclusion-first` when the user wants the full gate. |
| Stuck or drifting | Is the core idea failing, or working but unimportant, or has something more important appeared? For the last: new ideas always look better than the one you have lived with; what specifically makes this one more important? What would you salvage if you killed it today? |
| About to write | Who is the reader and what do they believe now? Is the claim something they will reject if stated outright? Hand off to `credo-paper-plan`. |
| Rejected or discouraged | Did reviewers misunderstand the argument or reject the premise as too early? Most of his awarded papers were rejected first. What in the writing would make a confused reviewer understand? |
| Considering collaboration | Have you done enough that you can send a partial solution rather than admiration? Are you hiding the idea from people who could help, and why? |
| A new system, dataset, or API appears | Run the fixed list of ways it could fail before deciding whether it is interesting; the list and its procedure are the `credo-threat-list` habit in this repository's `habits/` directory. Finding nothing is a normal result. |

## Output

No fixed format. The conversation ends with the user's stated judgment. If they ask for a written record, produce the one-paragraph summary they would write themselves: the decision, the reasons in their words, and the prediction to revisit.
