# Research Credo

Eleven independent skills for research judgment, sources, experiments, training, datasets, evaluation, and paper work. A short investigation can need research methods; a long task does not need every method. Results may be findings or decisions without code.

| Skill | Use it to |
| --- | --- |
| [credo-taste](skills/credo-taste/SKILL.md) | Choose a direction and decide whether to continue, pivot, or stop |
| [credo-research](skills/credo-research/SKILL.md) | Investigate a question and preserve useful original sources |
| [credo-read-then-forget](skills/credo-read-then-forget/SKILL.md) | Read for a purpose and examine inherited assumptions |
| [credo-experiment](skills/credo-experiment/SKILL.md) | Design, run, and interpret experiments and training comparisons |
| [credo-dataset](skills/credo-dataset/SKILL.md) | Construct or review data, labels, splits, and intended-use suitability |
| [credo-evaluation](skills/credo-evaluation/SKILL.md) | Design, build, and review benchmarks, metrics, scoring, and fair comparisons |
| [evaluation-operations](skills/evaluation-operations/SKILL.md) | Operate approved evaluation campaigns with durable attempt and result records |
| [internal-source-research](skills/internal-source-research/SKILL.md) | Reconstruct work context from authorized internal sources |
| [credo-paper-plan](skills/credo-paper-plan/SKILL.md) | Plan the reader's argument and figures before drafting |
| [credo-journal](skills/credo-journal/SKILL.md) | Record meaningful ideas, predictions, and hindsight |
| [credo-release](skills/credo-release/SKILL.md) | Check a paper before submission or release |

Use the experiment skill for the comparison, dataset skill for what the data represents, evaluation skill for what scores measure, and operations skill for running an already approved campaign. Compose them only where the task needs those responsibilities.

## Install

```bash
npx --yes skills add gigio1023/research-credo \
  --skill '*' --agent claude-code codex --global --yes
```

Omit `--global` for a project install or replace `'*'` with selected names. Installation does not enable all methods in every conversation. Adapt [AGENTS.md](AGENTS.md) into project instructions only when setup is requested.

## Repository boundaries

[Gigio Pack](https://github.com/gigio1023/gigio-pack) owns project purpose, current understanding, constraints, adaptive plans, and continuity across repositories and sessions. [Agent Skills](https://github.com/gigio1023/agent-skills) owns harness operation, prompting, installation, delegation, coding helpers, and artifact production. Research Credo owns research methods.

[Migration](docs/migration.md) records the two incoming packages and the coordinated publication and installation sequence. The earlier [six-skill diagram](docs/research-credo.svg) is a historical view of the initial collection.

## Development and provenance

```bash
npx --yes skills add . --list --full-depth
```

Discovery should find eleven unique names. Validate changed skills and their resources. Package validation and illustrative scenarios are not behavioral evaluations.

The original collection was independently inspired by Nicholas Carlini's [research essay](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) and [research log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html); not affiliated. New method references identify their own sources. License not yet chosen.
