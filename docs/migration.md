# Research method migration

`internal-source-research` and `evaluation-operations` move from [agent-skills](https://github.com/gigio1023/agent-skills) to this repository without renaming their skill handles. Their reference resources move with them.

| Previous source | New source |
| --- | --- |
| `skills/productivity/internal-source-research/` in agent-skills | `skills/internal-source-research/` |
| `skills/development/evaluation-operations/` in agent-skills | `skills/evaluation-operations/` |

These packages were copied from the companion agent-skills writer branch at `ba51fcc1cecf2bfb64de39d907df21a14547cc9e`, retaining its reader-record improvements. Their earlier development remains in that repository's Git history. The three new `credo-experiment`, `credo-dataset`, and `credo-evaluation` packages separate experimental design, data suitability, and measurement; they do not duplicate campaign state management.

## Publication order

Merge this destination before the companion agent-skills change removes the two source packages. Then merge the agent-skills change that receives Gigio's seven harness and coding helpers, before Gigio removes those sources. The slop revision companion can follow the writer's availability.

Draft publication is not installation. Existing copies continue to exist at their installed paths, but old tracked source paths will no longer be update targets after migration. During a separately requested refresh, use `install-skill-pack` to select the published repository and revision, reinstall these exact names from the new source, and verify their source metadata and intended harness destinations. Do not rely on a same-name directory alone or manually edit installation lock files. Avoid discoverable duplicate compatibility packages.

Existing project journals, libraries, run ledgers, and source archives remain project data. A skill refresh must preserve them and any user-customized installed content.
