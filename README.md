# research-credo

A way of thinking about research, packaged so an agent keeps it in the room during long-horizon work. The credo is adapted from Nicholas Carlini's essay [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) (2026), his [ideas log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html), and the problem-selection habit he described on the [Latent Space podcast](https://www.latent.space/p/carlini) (2024). Not affiliated with him; tenets are paraphrased and linked. Read the originals.

Status: draft v0. License not yet chosen.

## What this is, and is not

The essay's content is not a checklist. It is a set of questions Carlini asks himself at particular moments (what makes me want to shout, how many months ahead am I, what would the conclusion say if everything worked, who is the reader and what do they believe) and the episodes in which those questions paid off. This repository carries the questions and the episodes, and the one habit the essay says builds taste: writing predictions down and comparing them with what happened. Five skills, one always-on file, two small scripts.

It applies to long-horizon work only. A research direction, a paper, a multi-month improvement of a system you own: yes. A ticket, a bug, a customer deadline, this week's task: no. The scope test is in [AGENTS.md](AGENTS.md); the agent asks which kind of work it is before applying anything here.

Existing skills such as [research-companion](https://github.com/andrehuang/research-companion), [carlini-dm](https://github.com/moralespanitz/carlini-dm), and [research-loop](https://github.com/moralespanitz/research-loop) already turn the essay's strategy into evaluation pipelines and scorecards. This repository goes the other way: no scores, one question at a time, and a journal that closes the loop.

## Three layers

1. Always on. [AGENTS.md](AGENTS.md) holds the scope test, five stances the agent keeps in every long-horizon conversation, and the owner settings (journal path, near-term exclusions, comparative advantage, tenets held differently). Copy it into your project's `AGENTS.md`; [CLAUDE.md](CLAUDE.md) points Claude Code at it. Skills fire only when triggered; this layer is what makes the thinking continuous, and it is where your own data lives so a reinstall does not erase it.
2. Thinking skills. Dialogue-first, no forms or scores, one question per turn, with stop rules, ending when you can state your own judgment.
3. The record. A journal of ideas, predictions, hindsight, and monthly reviews, appended by a small script so nothing old is ever rewritten.

## Skills

| Skill | Kind | Moment | What you leave with |
| --- | --- | --- | --- |
| [credo-taste](skills/credo-taste/SKILL.md) | thinking | Choosing a direction, starting or continuing a project, stuck or drifting, a new system or dataset appears, rejected | Your own stated judgment, reached through his questions; the project gate (best-case conclusion, one idea, riskiest part, continue / kill / pivot); the failure-mode pass over a fixed list |
| [credo-paper-plan](skills/credo-paper-plan/SKILL.md) | thinking | About to write a paper or section | A seven-part plan (idea, reader, conclusion, story arc, figures, section order with reasons, abstract shape); you draft, the agent critiques |
| [credo-read-then-forget](skills/credo-read-then-forget/SKILL.md) | thinking | A paper landed | Scan, extract, or reproduce, then what the paper inherits unexamined and what you would do without it |
| [credo-journal](skills/credo-journal/SKILL.md) | record | An idea appears, a decision is made, a result arrives, monthly | An appended idea, prediction, hindsight, or review entry; predictions read back when outcomes come |
| [credo-release](skills/credo-release/SKILL.md) | checklist | Submitting, camera-ready, arXiv | Script findings with `file:line` for what a program can catch, then the human items confirmed one by one |

`credo-release` is the one procedural skill and is kept apart from the thinking skills on purpose: a checklist should not argue, and a judgment skill should not pretend to be exhaustive. Its [coverage.md](skills/credo-release/references/coverage.md) records which of Carlini's checklist items a program checks and which still need eyes, a PDF, or the call for papers.

The tenets are in [skills/credo-taste/references/tenets.md](skills/credo-taste/references/tenets.md) and the episodes used as analogies in [skills/credo-taste/references/episodes.md](skills/credo-taste/references/episodes.md). Both load only when a conversation needs them.

## Install

Two things get installed: the five skills and the always-on layer (`AGENTS.md` copied into your project and filled in). The CLI handles the first; the second is a copy you make once per project.

Every skill is named `credo-<name>` so the pack groups together in a skill list and does not collide with generic names such as `taste` or `threat-list` used by other packs. The prefix is the repository's, not a reference to the Elixir linter of the same name.

### With `npx skills` (preferred)

Prerequisite: Node.js 18 or newer. Browse the pack first:

```bash
npx --yes skills add 'gigio1023/research-credo#main' --list
```

Install the five skills globally for the agents you use. Pass an explicit `--agent` list; the CLI otherwise installs for whatever agent it detects.

```bash
npx --yes skills add 'gigio1023/research-credo#main' \
  --skill credo-taste credo-paper-plan credo-read-then-forget credo-journal credo-release \
  --agent claude-code codex \
  --global \
  --yes
```

Drop the trailing `--yes` to review the overwrite summary when a global skill of the same name already exists. Omit `--global` for a project-local install. Verify and update later with:

```bash
npx --yes skills list --global
npx --yes skills update --global
```

Installing from the GitHub source records the origin, so `update` picks up later releases. Installing from a local checkout does not; rerun `add` instead.

### By asking your agent

Paste this into Claude Code, Codex, or another agent that can run shell commands. If the agent has [install-skill-pack](https://github.com/gigio1023/agent-skills) available, it will review each package before installing.

```text
Install the research-credo skills from https://github.com/gigio1023/research-credo
with `npx skills`, global scope, for the agents I use here (five skills under
skills/). Then copy that repository's AGENTS.md sections into this project's
AGENTS.md, ask me for the owner settings at the bottom (journal path, near-term
exclusions, comparative advantage), and add a one-line pointer in CLAUDE.md.
Show me `npx skills list --global` when done.
```

### Manually

Each skill is a self-contained directory with a `SKILL.md`. From a checkout, link the ones you want into your harness's skill directory:

```bash
for s in skills/*/; do ln -s "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"; done   # Claude Code
for s in skills/*/; do ln -s "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"; done   # Codex
```

### Wire the always-on layer

Whichever way the skills were installed, copy [AGENTS.md](AGENTS.md) into your research project's `AGENTS.md` (Codex and other harnesses that read it), fill in the owner settings at its bottom, and add a pointer in `CLAUDE.md` (Claude Code), as this repository does. Without this step the skills fire only when triggered, nothing keeps the credo in the room between calls, and your journal path and stances have no home.

Frontmatter is limited to `name` and `description`, so the same files load in both harnesses. The two scripts need Python 3.10 or newer and no packages:

```bash
python3 skills/credo-release/scripts/check_tex.py path/to/main.tex --log path/to/main.log
python3 skills/credo-journal/scripts/journal.py --path ~/research/journal.md read --older-than 90
```

## Local development

Inspect a checkout without creating an update-tracked install. The listing must report five names.

```bash
npx --yes skills add . --list
python3 skills/credo-release/scripts/test_check_tex.py
python3 skills/credo-journal/scripts/test_journal.py
```

## Attribution and license

Tenets and episodes are short paraphrases with links to the sources; quotations are kept brief. The skills' wording, structure, and scripts are original to this repository. License: not yet chosen.
