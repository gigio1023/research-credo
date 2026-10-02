# Research Credo

Thirteen skills in three groups: a paper track adapted from one researcher's credo for work aimed at a paper, research and ML methods for any task that needs them, and an organization track that sharpens an agenda into a resourced bet. Results may be findings or decisions without code.

## Paper track

Only for work aimed at a paper or a publishable research claim, at the essay's bar: one idea, a conclusion beyond a number going up, a result months ahead of the next person, and unreasonable effort. A ticket, a product evaluation, or this week's task goes to the methods below. `credo-taste` and `credo-journal` run only when invoked (`/credo-taste` in Claude Code, `$credo-taste` in Codex) because they interview the user or write to the journal.

| Skill | Use it to |
| --- | --- |
| [credo-taste](skills/credo-taste/SKILL.md) | Choose a research direction and decide whether to continue, pivot, or stop |
| [credo-paper-plan](skills/credo-paper-plan/SKILL.md) | Plan the reader's argument and figures before drafting |
| [credo-journal](skills/credo-journal/SKILL.md) | Record research ideas, predictions, and hindsight |
| [credo-release](skills/credo-release/SKILL.md) | Check a paper before submission or release |

## Methods

Ordinary research and ML practice, meant to be selected in everyday work, so they carry no `credo-` prefix. `credo-read-then-forget` keeps the prefix for its source; a paper landing is its trigger.

| Skill | Use it to |
| --- | --- |
| [literature-research](skills/literature-research/SKILL.md) | Investigate a research question and preserve useful original sources |
| [credo-read-then-forget](skills/credo-read-then-forget/SKILL.md) | Read for a purpose and examine inherited assumptions |
| [ml-experiment](skills/ml-experiment/SKILL.md) | Design, run, and interpret experiments and training comparisons |
| [ml-dataset](skills/ml-dataset/SKILL.md) | Construct or review data, labels, splits, and intended-use suitability |
| [evaluation-design](skills/evaluation-design/SKILL.md) | Design, build, and review benchmarks, metrics, scoring, and fair comparisons |
| [evaluation-operations](skills/evaluation-operations/SKILL.md) | Operate approved evaluation campaigns with durable attempt and result records |
| [internal-source-research](skills/internal-source-research/SKILL.md) | Reconstruct work context from authorized internal sources |

## Organization track

| Skill | Use it to |
| --- | --- |
| [praxis-direction](skills/praxis-direction/SKILL.md) | Sharpen an agenda into one bet: outcome, measure, intervention, first test, compute ladder, kill condition; run the failure-mode pass on a new system |
| [praxis-setup](skills/praxis-setup/SKILL.md) | Create or audit the organization's praxis profile |

The paper track answers to a reader and a venue. The organization track answers to a decision the company must make with the compute, data, and experts it has, and runs when someone asks for a bet. Its skills are public and generic; what only the organization knows lives in a one-page `praxis-profile.md` in the organization's own workspace, written by praxis-setup and read by praxis-direction. The [template](skills/praxis-setup/references/profile-template.md) shows the fields with a synthetic example. Nothing from a real organization belongs in this repository.

Use the experiment skill for the comparison, dataset skill for what the data represents, evaluation skill for what scores measure, and operations skill for running an already approved campaign. Compose them only where the task needs those responsibilities.

## Install

```bash
npx --yes skills add gigio1023/research-credo \
  --skill '*' --agent claude-code codex --global --yes
```

Omit `--global` for a project install or replace `'*'` with selected names, for example the two `praxis-*` skills alone for a company workspace. Installation does not enable all methods in every conversation. Adapt [AGENTS.md](AGENTS.md) into project instructions only when setup is requested; run praxis-setup once per organization to write its profile outside the installed package.

An install from before the method rename still carries `credo-experiment`, `credo-dataset`, `credo-evaluation`, and `credo-research`. Remove them after installing the new names so both sets are not discoverable:

```bash
npx --yes skills remove credo-experiment credo-dataset credo-evaluation credo-research --global --yes
```

## Repository boundaries

[Gigio Pack](https://github.com/gigio1023/gigio-pack) owns project purpose, current understanding, constraints, adaptive plans, and continuity across repositories and sessions. [Agent Skills](https://github.com/gigio1023/agent-skills) owns harness operation, prompting, installation, delegation, coding helpers, and artifact production. Research Credo owns research methods.

[Migration](docs/migration.md) records the two incoming packages, the method rename, and the coordinated publication and installation sequence. The earlier [six-skill diagram](docs/research-credo.svg) is a historical view of the initial collection.

## Development and provenance

```bash
npx --yes skills add . --list --full-depth
```

Discovery should find thirteen unique names. Validate changed skills and their resources. Package validation and illustrative scenarios are not behavioral evaluations.

The original collection was independently inspired by Nicholas Carlini's [research essay](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) and [research log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html); not affiliated. New method references identify their own sources. License not yet chosen.
