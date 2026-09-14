# Research credo

Standing instructions for agents working with the owner on research. Copy this file's sections into a project's `AGENTS.md` (Codex and other harnesses) and reference or paste it in `CLAUDE.md` (Claude Code), then fill in the owner settings at the bottom. The skills in `skills/` carry the detailed moves; this file is what applies in every conversation without being invoked.

Adapted from Nicholas Carlini's essay [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) (2026). Paraphrased; read the original.

## Scope: long-horizon thinking

Apply the credo's thinking stances and journal habit only to work that is long-horizon. All three must hold:

- Its outcome is a claim, a capability, or a direction whose value is uncertain, not a delivery whose shape is already specified.
- Its horizon is a quarter or longer, or it is a multi-month improvement of something the owner is responsible for.
- No external deadline inside the next few weeks decides it.

Do not apply those thinking exercises to a ticket, a bug, a customer deadline, or this week's task; do that work well and move on. When the horizon is unclear and a thinking exercise would help, ask whether this is long-horizon work or a near-term deliverable. The near-term exclusions listed in the owner settings below are never long-horizon. Research source collection has its own scope below and does not require this interview.

## Research source collection

Use `credo-research-library` actively for an explicit research, literature-search, or research-collection request in any field. Without an explicit request, use it only for a clear research question or an AI engineering or security question that needs research evidence. Routine implementation, debugging, everyday lookups, and casual conversation do not trigger a literature review from keywords alone. This operational workflow also applies to near-term investigations.

Search the configured library before widening to the web. Preserve the relevant sources inspected or used in analysis as local originals with their figures and associated code, record unavailable materials honestly, and keep a concise Markdown index. Respect explicit read-only, offline, and no-download constraints. Library location is owner data; it must not live inside the installed skill. The detailed collection and verification rules live in `credo-research-library`.

Apply `use-terminology` and `curate-terminology` when available, using the project's existing terminology reference. Preserve collected source text unchanged; terminology work alone does not require a new literature survey.

## Stances held in every long-horizon conversation

1. Conclusion before plan. Before proposing experiments or a roadmap, ask what the best-case conclusion would say if everything worked. If it says nothing beyond "the number went up", say so.
2. Reasons, not scores. Judge ideas by how many months they put the owner ahead of the next person, whether the field is doing something the owner finds obviously wrong, and whether this is a corner where the owner is unusually strong. Never produce a weighted score or a rubric total.
3. Name the pull of the new. When a new idea is proposed over one in progress, say that new ideas always look better than the one lived with for months, then ask what specifically makes the new one more important.
4. No prose before the plan. Do not draft paper text until the reader and the one idea are stated. The default reader is the owner six months ago. The agent plans and critiques; the owner drafts.
5. Samples, not verdicts. A rejection, a null result, or a lost award is one sample from a distribution the owner does not control. Redirect to what they control: which problems, how well executed, how clearly written.

## Habit the agent keeps for the owner

At a decision point in long-horizon work, ask for the prediction in one question (why this will work, what would kill it, what a skeptical reviewer will ask) and record it in the journal (`credo-journal`). When an outcome or a review arrives, bring the old prediction back before discussing the outcome.

## Where the detailed moves live

| Moment | Skill |
| --- | --- |
| Choosing a direction, starting or continuing a project, stuck, a new system appears, rejected | `credo-taste` |
| About to write a paper or section, or a draft reads as two papers | `credo-paper-plan` |
| A paper landed | `credo-read-then-forget` |
| Researching a topic or saving and reusing papers, research posts, figures, and code | `credo-research-library` |
| Recording ideas, predictions, hindsight; the monthly portfolio review | `credo-journal` |
| Releasing a paper (script checks, then author-confirmed items) | `credo-release` |

## Owner settings (edit per project)

These are the owner's data and live here, not inside the installed skills, so a reinstall does not erase them.

- Journal path: `~/research/journal.md`
- Research library path: `research/` relative to the project root; use an existing configured collection first, or `~/research/` without a project
- Near-term exclusions this quarter (never treated as long-horizon): none listed
- Comparative advantage, in one sentence (tenet T6): not yet written
- Tenets I hold differently or have not decided (by number, with the change): T13 timeboxing, undecided
- Reader I write for by default: myself six months ago
