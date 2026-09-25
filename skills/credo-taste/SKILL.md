---
name: credo-taste
description: "Think through a consequential research-direction decision one question at a time: which problem is worth pursuing, whether to start or continue a project (best-case conclusion, one idea, riskiest sub-problem, continue / kill / pivot), and how to read a rejection. Use for research-direction questions such as 'is this research direction worth it', 'should I start this project', 'this line of research isn't working'. Reasons in prose, no scores. NOT for routine execution of a settled task, for planning paper text (credo-paper-plan), for reading a paper (credo-read-then-forget), or for a direction decided inside an organization and the failure-mode pass on a new system (praxis-direction)."
---

# Credo: Taste

Outcome: the user states, in their own words, what they will do and why, after being asked the questions Nicholas Carlini asks himself at the same moment in [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html). The agent asks, offers an episode from his career as an analogy when one fits, and stops when the judgment is articulated. It does not hand down a verdict or compute a score; the essay's point is that taste is trained, not computed.

## Scope

Use for a consequential research-direction decision whose value or premise is uncertain. Duration alone does not decide: a short benchmark project can need a direction choice, while a long routine training job may not. Do not reopen a settled question or turn ordinary implementation into an interview. Infer the decision from context and ask only for missing human judgment. For a direction decided inside an organization, where the result is a product or capability decision rather than a paper, use praxis-direction.

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
| A new system, dataset, API, or agent appears | Hand off to praxis-direction, which owns the failure-mode pass and its fixed list. |
| Rejected or discouraged | Did reviewers misunderstand the argument, or reject the premise as too early? Most of his awarded papers were rejected first. What in the writing would make a confused reviewer understand? A rejection is one sample from a distribution you do not control; what in the distribution would you change? |
| Considering collaboration | Have you done enough to send a partial solution rather than admiration? Are you hiding the idea from people who could help, and why? Ideas are cheap; execution is hard. |
| About to write | Hand off to credo-paper-plan. |

## The gate for one project

Ask in order, one per turn, and stop early when an answer settles it.

1. If every experiment turned out exactly as you hope, what does the conclusion say? If it is a number going up, relate that improvement to the intended scientific or practical use. A meaningful applied improvement can be the goal; do not impose publication novelty on a product or engineering investigation.
2. What is the central question or contribution? If several ideas compete for resources, identify their relationship and which one the current decision concerns; a conjunction alone does not mean two projects.
3. Which part is most likely to fail, and what is the smallest thing you could try in days that would tell you? Weeks spent on the part already understood is the first finding.
4. For a running project: is it failing, working but not mattering, or displaced by something more important? Apply the pull-of-the-new check above.
5. What will you do: continue, kill, pivot, or de-risk first? If killing, what is salvaged: a workshop note, a post, or a journal entry.

When a project is ending well, ask once more: is there an obvious experiment, domain, or objection a reader will wish you had addressed? If yes it belongs in this paper; small follow-ups can stay open.

## Closing

No fixed form. Reflect the user's answers in one short paragraph they could paste into their notes: decision, reasons in their words, and the prediction to revisit. Record a prediction through credo-journal when requested or already authorized. Preserve decisions in the project's existing context record when that maintenance is part of the task; do not start another interview or duplicate journal entry for every experiment.
