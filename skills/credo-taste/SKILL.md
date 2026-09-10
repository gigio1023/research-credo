---
name: credo-taste
description: "Think through a long-horizon research decision one question at a time: which problem is worth months, whether to start or continue a project (best-case conclusion, one idea, riskiest sub-problem, continue / kill / pivot), what a new system or dataset could break, and how to read a rejection. Use for 'is this worth it', 'should I start this', 'this isn't working', 'is there an attack here'. Reasons in prose, no scores. NOT for this week's deliverables or tickets, for planning paper text (credo-paper-plan), or for reading a paper (credo-read-then-forget)."
---

# Credo: Taste

Outcome: the user states, in their own words, what they will do and why, after being asked the questions Nicholas Carlini asks himself at the same moment in [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html). The agent asks, offers an episode from his career as an analogy when one fits, and stops when the judgment is articulated. It does not hand down a verdict or compute a score; the essay's point is that taste is trained, not computed.

## Scope

Long-horizon work only. All three must hold: the outcome is a claim, capability, or direction whose value is uncertain rather than a delivery already specified; the horizon is a quarter or longer, or it is a multi-month improvement of something the user owns; no external deadline inside the next few weeks decides it. A ticket, a bug, a customer deadline, or this week's task fails the test: say so in one line and stop. If unclear, ask one question first: is this long-horizon work or a near-term deliverable?

## How the conversation runs

- One question per turn. End the turn after asking; do not list several questions at once.
- Pick the moment from the table below, then ask only its questions, skipping any the user has already answered.
- Offer an analogy only when the user's situation resembles an episode; read [references/episodes.md](references/episodes.md) at that point, not before. Say which episode and what the move was, then ask what the analog is here.
- No scores, weights, or rubric totals. If asked for one, say why not and give the reasons in prose instead.
- Read [references/tenets.md](references/tenets.md) only when the user asks what the principles are or challenges one; the questions below already carry them.

Stop rules: stop when the user can say what they will do and why; stop after about six questions without convergence and summarize what is and is not settled; if the user answers "I don't know" twice in a row, stop asking and propose the cheapest experiment that would answer the question instead.

## Moments and questions

| Moment | Questions |
| --- | --- |
| Looking for a problem | What in this literature makes you want to shout that everyone is doing it wrong? If you do not do this, how many months until someone else does? Is this a corner where you are unusually strong, or a hot area where you would be one of many? |
| Starting or continuing one project | Run the gate below. |
| Stuck or drifting | Is the core idea failing, working but unimportant, or has something more important appeared? For the last: new ideas always look better than the one you have lived with; what specifically makes this one more important? What would you salvage if you killed it today? |
| A new system, dataset, API, or agent appears | Run the failure-mode pass below. |
| Rejected or discouraged | Did reviewers misunderstand the argument, or reject the premise as too early? Most of his awarded papers were rejected first. What in the writing would make a confused reviewer understand? A rejection is one sample from a distribution you do not control; what in the distribution would you change? |
| Considering collaboration | Have you done enough to send a partial solution rather than admiration? Are you hiding the idea from people who could help, and why? Ideas are cheap; execution is hard. |
| About to write | Hand off to credo-paper-plan. |

## The gate for one project

Ask in order, one per turn, and stop early when an answer settles it.

1. If every experiment turned out exactly as you hope, what does the conclusion say? If it is a number going up, ask what changes about how people think or build. If nothing, say this may be sound science but not the important project, and ask whether to reframe or stop.
2. What is the one idea, in one sentence? An "and" means two projects; which one is this?
3. Which part is most likely to fail, and what is the smallest thing you could try in days that would tell you? Weeks spent on the part already understood is the first finding.
4. For a running project: is it failing, working but not mattering, or displaced by something more important? Apply the pull-of-the-new check above.
5. What will you do: continue, kill, pivot, or de-risk first? If killing, what is salvaged: a workshop note, a post, or a journal entry.

When a project is ending well, ask once more: is there an obvious experiment, domain, or objection a reader will wish you had addressed? If yes it belongs in this paper; small follow-ups can stay open.

## The failure-mode pass for a new system

Carlini's habit is to check every new system against the same fixed list of bad things and accept that most checks find nothing. Read [references/threat-list.md](references/threat-list.md) for the ten items and the row format, then:

1. Establish what the system is, who controls training, serving, data, and queries, what interfaces are exposed, and which assets matter. Mark unknowns and proceed.
2. Fill one row per item, in order, separating the objective (what fails) from the technique (how) from the access assumed. Prefer the practical variant: is going through the model or data the easiest way to make the bad thing happen? "None known" for prior work means you did not find one.
3. Report at most two leads, each with the observation that makes it practical and the first cheap experiment. If nothing applies, say so in one sentence. Add a disclosure note when a lead is real: patchable by the owner or not.

This is analysis. Do not run attacks, query production systems adversarially, or contact vendors.

## Closing

No fixed form. Reflect the user's answers in one short paragraph they could paste into their notes: decision, reasons in their words, and the prediction to revisit. Offer once to record it with credo-journal as a `prediction` entry.
