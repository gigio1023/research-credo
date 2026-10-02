# Research method migration

`internal-source-research` and `evaluation-operations` move from [agent-skills](https://github.com/gigio1023/agent-skills) to this repository without renaming their skill handles. Their reference resources move with them.

| Previous source | New source |
| --- | --- |
| `skills/productivity/internal-source-research/` in agent-skills | `skills/internal-source-research/` |
| `skills/development/evaluation-operations/` in agent-skills | `skills/evaluation-operations/` |

These packages were copied from the companion agent-skills writer branch at `ba51fcc1cecf2bfb64de39d907df21a14547cc9e`, retaining its reader-record improvements. Their earlier development remains in that repository's Git history. The same change added `credo-experiment`, `credo-dataset`, and `credo-evaluation` for experimental design, data suitability, and measurement, without duplicating campaign state management; the consolidation below later merged them into `ml-research-methods`.

## Publication order

Merge this destination before the companion agent-skills change removes the two source packages. Then merge the agent-skills change that receives Gigio's seven harness and coding helpers, before Gigio removes those sources. The slop revision companion can follow the writer's availability.

Draft publication is not installation. Existing copies continue to exist at their installed paths, but old tracked source paths will no longer be update targets after migration. During a separately requested refresh, use `install-skill-pack` to select the published repository and revision, reinstall these exact names from the new source, and verify their source metadata and intended harness destinations. Do not rely on a same-name directory alone or manually edit installation lock files. Avoid discoverable duplicate compatibility packages.

Existing project journals, libraries, run ledgers, and source archives remain project data. A skill refresh must preserve them and any user-customized installed content.

## Threat list ownership

The fixed list of ten failure modes moved from `skills/credo-taste/references/threat-list.md` to `skills/praxis-direction/references/threat-list.md` when the organization track was added. `credo-taste` hands the failure-mode pass to `praxis-direction`; an installation that carries only the paper track no longer includes the list.

## Consolidation into nine skills

The paper track regained its scope test, and the skills outside it were consolidated where one task had several owners. The `credo-` prefix now marks exactly the paper track; the methods carry ordinary research and ML practice and are meant to be selected in everyday work.

| Previous skill | Now |
| --- | --- |
| `credo-experiment` | `ml-research-methods`, Experiment section |
| `credo-dataset` | `ml-research-methods`, Dataset section |
| `credo-evaluation` | `ml-research-methods`, Measurement section |
| `credo-research` | `literature-research` |
| `credo-read-then-forget` | `literature-research`, Read one paper section |
| `praxis-setup` | `praxis-direction`, Set up or audit the profile section |

The topical references moved unchanged into the absorbing package, and the three method source notes became one. A refresh installs the nine names and removes the six previous ones; project libraries under `research/`, journals, praxis profiles, and experiment records stay where they are.
