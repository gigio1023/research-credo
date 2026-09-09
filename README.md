# research-credo

A way of thinking about research, packaged so an agent keeps it in the room during long-horizon work. The credo is adapted from Nicholas Carlini's essay [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) (2026), his [ideas log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html), and the problem-selection habit he described on the [Latent Space podcast](https://www.latent.space/p/carlini) (2024). Not affiliated with him; tenets are paraphrased and linked. Read the originals.

Status: draft v0. License not yet chosen.

## What this is, and is not

The essay's content is not a checklist. It is a set of questions Carlini asks himself at particular moments (what makes me want to shout, how many months ahead am I, what would the conclusion say if everything worked, who is the reader and what do they believe) and the episodes in which those questions paid off. This repository carries the questions and the episodes, and the one habit the essay says builds taste: writing predictions down and comparing them with what happened.

It applies to long-horizon work only. A research direction, a paper, a multi-month improvement of a system you own: yes. A ticket, a bug, a customer deadline, this week's task: no. The scope test is in [AGENTS.md](AGENTS.md); the agent asks which kind of work it is before applying anything here.

Existing skills such as [research-companion](https://github.com/andrehuang/research-companion), [carlini-dm](https://github.com/moralespanitz/carlini-dm), and [research-loop](https://github.com/moralespanitz/research-loop) already turn the essay's strategy into evaluation pipelines and scorecards. This repository goes the other way: no scores, one question at a time, and a journal that closes the loop.

## Three layers

1. Always on. [AGENTS.md](AGENTS.md) holds the scope test and five stances the agent keeps in every long-horizon conversation. Copy its credo section into your project's `AGENTS.md`; [CLAUDE.md](CLAUDE.md) points Claude Code at it. Skills fire only when triggered; this layer is what makes the thinking continuous.
2. Thinking skills. Dialogue-first, no forms, ending when you can state your own judgment.
3. The record. A journal of ideas, predictions, and hindsight, plus a monthly review of the portfolio.

### Thinking skills

| Skill | Moment | What you leave with |
| --- | --- | --- |
| [taste](skills/taste/SKILL.md) | Choosing a direction, weighing an idea, stuck mid-project | Your own stated judgment, reached through his questions and his episodes as analogies |
| [conclusion-first](skills/conclusion-first/SKILL.md) | Starting or continuing one project | The best-case conclusion, the one idea, the riskiest part, and a continue / kill / pivot / de-risk decision |
| [paper-plan](skills/paper-plan/SKILL.md) | About to write a paper or section | A seven-part plan (idea, reader, conclusion, story arc, figures, section order with reasons, abstract shape); you draft, the agent critiques |
| [read-then-forget](skills/read-then-forget/SKILL.md) | A paper landed | Scan, extract, or reproduce, then what the paper inherits unexamined and what you would do without it |
| [taste-journal](skills/taste-journal/SKILL.md) | An idea appears, a decision is made, a result arrives | An appended idea, prediction, or hindsight entry; predictions read back when outcomes come |
| [distribution-review](skills/distribution-review/SKILL.md) | Monthly | Which one or two efforts could be great, what dies, months-ahead guesses, rejections read as samples |

The tenets with the owner's stance on each are in [skills/taste/references/tenets.md](skills/taste/references/tenets.md); the episodes used as analogies are in [skills/taste/references/episodes.md](skills/taste/references/episodes.md).

### Habits (not the credo)

Fixed procedures that run at a moment, kept apart from the thinking skills so a checklist never pretends to be judgment.

| Habit | Moment | Result |
| --- | --- | --- |
| [threat-list](habits/threat-list/SKILL.md) | A new dataset, model, API, or agent appears | Applicability memo over a fixed list of failure modes; "nothing here" is a valid result |
| [latex-release-lint](habits/latex-release-lint/SKILL.md) | LaTeX sources are near final | Script findings with `file:line` for everything a program can catch; see [coverage.md](habits/latex-release-lint/references/coverage.md) |
| [paper-release-checklist](habits/paper-release-checklist/SKILL.md) | Submitting, camera-ready, arXiv | The human items, one at a time, each confirmed by the author |

## Install

Always-on layer: copy the credo section of [AGENTS.md](AGENTS.md) into your research project's `AGENTS.md` (Codex and other harnesses that read it) and add a pointer in `CLAUDE.md` (Claude Code), as this repository does.

Skills and habits are self-contained directories with a `SKILL.md`. Link the ones you want into your harness's skill directory.

Claude Code (user scope):

```bash
for s in skills/*/ habits/*/; do ln -s "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"; done
```

Codex (user scope):

```bash
for s in skills/*/ habits/*/; do ln -s "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"; done
```

Frontmatter is limited to `name` and `description`, so the same files load in both harnesses. The lint script needs Python 3.10 or newer and no packages:

```bash
python3 habits/latex-release-lint/scripts/check_tex.py path/to/main.tex --log path/to/main.log
```

## Attribution and license

Tenets and episodes are short paraphrases with links to the sources; quotations are kept brief. The skills' wording, structure, and scripts are original to this repository. License: not yet chosen.
