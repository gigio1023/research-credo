# Research Credo

Nine skills in three groups: a paper track adapted from one researcher's credo for work aimed at a paper, research and ML methods for any task that needs them, and an organization track that sharpens an agenda into a resourced bet. Results may be findings or decisions without code.

## Paper track

Only for work aimed at a paper or a publishable research claim, at the essay's bar: one idea, a conclusion beyond a number going up, a result months ahead of the next person, and unreasonable effort. A ticket, a product evaluation, or this week's task goes to the methods below. `credo-taste` and `credo-journal` run only when invoked (`/credo-taste` in Claude Code, `$credo-taste` in Codex) because they interview the user or write to the journal.

| Skill | Use it to |
| --- | --- |
| [credo-taste](skills/credo-taste/SKILL.md) | Choose a research direction and decide whether to continue, pivot, or stop |
| [credo-paper-plan](skills/credo-paper-plan/SKILL.md) | Plan the reader's argument and figures before drafting |
| [credo-journal](skills/credo-journal/SKILL.md) | Record research ideas, predictions, and hindsight |
| [credo-release](skills/credo-release/SKILL.md) | Check a paper before submission or release |

## Methods

Ordinary research and ML practice, meant to be selected in everyday work, so they carry no `credo-` prefix.

| Skill | Use it to |
| --- | --- |
| [literature-research](skills/literature-research/SKILL.md) | Read a paper for a purpose, survey literature, and preserve original sources |
| [ml-research-methods](skills/ml-research-methods/SKILL.md) | Design, run, or review an experiment, dataset, or evaluation benchmark and interpret what it supports |
| [evaluation-operations](skills/evaluation-operations/SKILL.md) | Operate approved evaluation campaigns with durable attempt and result records |

`ml-research-methods` owns the experiment, the data, and the measurement in one package, so a benchmark build or a training comparison loads one skill and reads only the references it needs. `evaluation-operations` stays separate because dispatching an approved campaign is a different authority from designing one.

## Organization track

| Skill | Use it to |
| --- | --- |
| [praxis-direction](skills/praxis-direction/SKILL.md) | Sharpen an agenda into one bet, run the failure-mode pass on a new system, or set up and audit the praxis profile |
| [internal-source-research](skills/internal-source-research/SKILL.md) | Reconstruct work context from authorized internal sources |

The paper track answers to a reader and a venue. The organization track answers to a decision the company must make with the compute, data, and experts it has, and runs when someone asks for it. Its skills are public and generic; what only the organization knows lives in a one-page `praxis-profile.md` in the organization's own workspace, written and read by praxis-direction. The [template](skills/praxis-direction/references/profile-template.md) shows the fields with a synthetic example. Nothing from a real organization belongs in this repository.

## Install

```bash
npx --yes skills add gigio1023/research-credo \
  --skill '*' --agent claude-code codex --global --yes
```

Omit `--global` for a project install or replace `'*'` with selected names, for example `praxis-direction` and `internal-source-research` alone for a company workspace. Installation does not enable all methods in every conversation. Adapt [AGENTS.md](AGENTS.md) into project instructions only when setup is requested; ask praxis-direction to set up the profile once per organization, outside the installed package.

An install from before the consolidation still carries six names that no longer exist. Remove them after installing so the old and new sets are not both discoverable:

```bash
npx --yes skills remove credo-experiment credo-dataset credo-evaluation \
  credo-research credo-read-then-forget praxis-setup --global --yes
```

## Repository boundaries

[Gigio Pack](https://github.com/gigio1023/gigio-pack) owns project purpose, current understanding, constraints, adaptive plans, and continuity across repositories and sessions. [Agent Skills](https://github.com/gigio1023/agent-skills) owns harness operation, prompting, installation, delegation, coding helpers, and artifact production. Research Credo owns research methods.

[Migration](docs/migration.md) records the incoming packages, the consolidation into nine skills, and the coordinated publication and installation sequence. The earlier [six-skill diagram](docs/research-credo.svg) is a historical view of the initial collection.

## Development and provenance

```bash
npx --yes skills add . --list --full-depth
```

Discovery should find nine unique names. Validate changed skills and their resources. Package validation and illustrative scenarios are not behavioral evaluations.

The original collection was independently inspired by Nicholas Carlini's [research essay](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) and [research log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html); not affiliated. New method references identify their own sources. License not yet chosen.
