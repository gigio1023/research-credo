# Research credo

Guidance for work in this repository, and an optional source to adapt into a research project's instructions when the user requests setup. Installing skills alone does not activate every method or journal habit. Project preferences and records belong with the project, outside installed skill packages.

The repository holds three tracks with different readers. The `credo-` skills are adapted from Nicholas Carlini's [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html); four of them form the paper track, which answers to a reader and a venue. The method skills are ordinary research and ML practice for any task that needs them and carry their own source notes. The organization track answers to a decision a company must make with the compute, data, and experts it has.

## Paper track scope

Apply `credo-taste`, `credo-paper-plan`, `credo-journal`, and `credo-release` only when the work is aimed at a paper or a publishable research claim. Within that scope the essay's bar holds unsoftened: one idea, a best-case conclusion that says more than a number went up, a result months ahead of the next person, and effort a reasonable person would not spend. A ticket, a bug, a customer deadline, a product evaluation, or this week's task is out of scope even when it involves a model, a benchmark, or the word research; do that work well with the method skills and move on. When it is unclear whether the work aims at a paper, ask that one question first.

`credo-taste` and `credo-journal` run only on the user's request, because an unrequested run either interviews the user or writes to the user's journal. Harness adapters keep them out of automatic selection: `disable-model-invocation` in the Claude Code frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for Codex. Each body states the same scope for harnesses without those controls. `credo-read-then-forget` keeps the prefix for its source, but a paper landing is its trigger, so it serves engineering work too.

## Choose the skill

| Track | Work | Skill |
| --- | --- | --- |
| Paper | Choose, continue, pivot, or stop a paper-bound research direction, on request | `credo-taste` |
| Paper | Plan or critique a paper's argument and figures | `credo-paper-plan` |
| Paper | Record research ideas, predictions, and hindsight, on request | `credo-journal` |
| Paper | Check a paper before submission or release | `credo-release` |
| Method | Read a paper for a stated purpose and inspect inherited assumptions | `credo-read-then-forget` |
| Method | Gather and preserve literature and other research sources | `literature-research` |
| Method | Design, run, and interpret an experiment or training comparison | `ml-experiment` |
| Method | Construct or review a dataset and its labels, splits, and suitability | `ml-dataset` |
| Method | Design, build, or review a benchmark, metrics, scoring, and comparisons | `evaluation-design` |
| Method | Operate an approved campaign across attempts and sessions | `evaluation-operations` |
| Method | Reconstruct context from authorized internal sources | `internal-source-research` |
| Organization | Sharpen an agenda into a resourced bet when asked, or run the failure-mode pass on a new system | `praxis-direction` |
| Organization | Create or audit the organization's praxis profile | `praxis-setup` |

Use existing decisions and evidence before asking another question. A user chooses purpose, tradeoffs, and authority; an empirical unknown may require an experiment. A finding, rejected hypothesis, unsuitable dataset, or unresolved comparison can be a useful result without a code change.

Inside an organization, where the result is a product, customer, or capability decision rather than a paper, `praxis-direction` turns the agenda into a bet and `credo-taste` stays with paper directions. The organization's outcomes, compute ladder, experts, and data live in its own `praxis-profile.md`, written by `praxis-setup` in that workspace and never in this repository.

## Work and continuity

State the question and the decision the work could change. Select a credible comparison and assessment appropriate to that question. Novelty, months ahead, and publication claims belong to the paper track; method work does not borrow them. Preserve actual results, relevant conditions, and interpretation in existing project records. Give the reader the explanation needed for this decision without reciting every possible qualification.

Quick checks within the same question and authorized resources can proceed. Ask before a new direction or a newly proposed long activity, such as work expected to take two or three days or more, unless that work is already authorized. Short duration does not grant new spending, data access, or external actions. Honor an existing resource budget and stop condition.

For cross-session purpose, constraints, current understanding, and adaptive plans, use the project's existing records or requested Gigio Pack workflow. Do not create a second project state system here. For document production, use the requested writing method; paper planning does not prohibit prose the user separately asks the agent to draft.

## Source collection

`literature-research` applies actively to explicit research, literature-search, or collection requests. Otherwise use it only when a decision needs evidence from papers or technical research posts; a general lookup, a vendor comparison, or a document task is not a research question because it says "investigate". Search the configured library before expanding it, preserve inspected originals and useful associated material, and record access gaps. Respect read-only, offline, and no-download constraints. Terminology tools, when available, use the project's accepted terms without altering collected originals.

## Maintaining this repository

Keep each skill independently usable with colocated references and resources. Method boundaries should prevent duplicate ownership without forcing every task through all skills. Keep private transcripts, credentials, datasets, and project examples out of published packages. Use synthetic examples or explicitly authorized public sources.

Validate changed packages, resource links, names, and discovery. Static package checks and illustrative walkthroughs do not establish improved model behavior. Do not launch paid or long behavioral trials merely to maintain instructions.

### Tests

A test written after the code, with expected values read off that code, repeats the implementation: it passes by construction, misses the bugs it shares with the code, and breaks on every refactor. Do not write such tests unless the user asks for a specific one.

- Verify features end to end. Run the real entry point on real or fixed input and leave an artifact another person can rerun and compare, such as an output file, log, report, or screenshot. Give the command and the artifact path in the final message.
- When a unit needs an isolated test, first list the ways it can fail, take expected values from the spec or a hand calculation, and only then write the code.
- A bug fix may add one test that reproduces the bug and fails before the fix.
- Keep or add a test only if losing it would let a security, money, data-loss, or reported-number bug ship unnoticed and no end-to-end run covers it.
- If a refactor that keeps behavior breaks a test, the test was checking implementation. Delete it instead of rewriting it and list it in the PR.
- Do not test constants, prompt or message strings, output formatting, internal helpers, or fakes built for the test itself.

End-to-end path here: run each changed bundled script on a sample input, then discover and validate the packages with the Skills CLI. Tests that meet the keep bar: `skills/credo-journal/scripts/journal.py`, which must only append to the user's journal.

## Owner settings (adapt per project)

- Journal path: `~/research/journal.md`
- Research library: existing configured collection first; otherwise `research/` within a project or `~/research/` without one
- Reader for paper planning, unless specified: myself six months ago
- Comparative advantage: not yet written
- Tenets held differently or undecided: T13 timeboxing, undecided
- Journal capture and review schedule: only as requested or explicitly adopted by the project
- Praxis profile: none in this repository; `praxis-setup` writes one in the organization's workspace and links it from that project's instructions
