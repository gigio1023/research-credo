---
name: praxis-setup
description: >
  Create or audit an organization's praxis profile: the one-page file that
  praxis-direction reads for organizational outcomes, evidence conventions,
  compute ladder and spend gate, in-house experts and data, time horizon, and
  record locations. Use when asked to set up praxis for a company or
  workspace, or when praxis-direction reports a missing or stale profile.
  Writes only into the user's project, never into installed skills. NOT for
  project plans (gigio-write-plan), general project context
  (gigio-project-setup), or running the direction gate (praxis-direction).
---

# Praxis: Setup

Outcome: `praxis-profile.md` exists in the organization's workspace, is linked from the project's instructions, and answers what praxis-direction cannot infer. The profile is the organization's private data; the installed skill stays generic.

## Locate or create

Resolve the target in this order: a path the user names; a path already named in `AGENTS.md` or `PROJECT.md`; otherwise `praxis-profile.md` at the workspace root. If the file exists, run the audit below instead of a new interview.

Before writing, check where the file will land. Refuse to write inside an installed skill directory. If the workspace's Git remote points at a public host and the target path is not ignored, say so and offer an ignored path or a private location; the profile names customers, budgets, and people and must not reach a public repository. Do not edit `.gitignore` without asking.

## Interview

Read [references/profile-template.md](references/profile-template.md) for the fields and a synthetic example. Ask one field per turn, in the template's order, and skip a field the user's existing documents already answer; cite where the answer came from. Record what the user says, not what the agent would prefer; a field the user cannot answer yet is written as `undecided` with the date.

Keep the profile within about forty lines. It holds facts the gate needs, not strategy prose: one line per outcome, one row per tier, one row per expert role, one row per dataset. Refer to people by role, not name, unless the user wants names.

## Write and link

Write the file, then add one line to `AGENTS.md` or `PROJECT.md` that names the path, for example `Praxis profile: praxis-profile.md`. Do not restructure those files. Report the path and the fields left undecided.

## Audit

On a rerun, compare each field with the current facts the user or the workspace supplies and append a dated line under the changed field rather than rewriting history; praxis-direction reads the latest line. Flag a tier, threshold, or dataset that no longer exists. Do not remove past values.

Setup does not run the gate, create plans, or record predictions; those belong to praxis-direction and the project's records.
