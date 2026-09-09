# research-credo

Agent skills that turn a research credo into daily habits. The credo is adapted from Nicholas Carlini's writing on how to do research that matters, most of all [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) (2026), plus his notes on [keeping an ideas log](https://nicholas.carlini.com/writing/2024/my-research-logfile.html), the [paper release checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html), and the problem-selection habit he described on the [Latent Space podcast](https://www.latent.space/p/carlini) (2024). This repository is not affiliated with him. Tenets are paraphrased and linked; read the originals.

Status: draft v0. The tenets carry a `stance` column (adopted / adapted / open) so the owner can record which principles they actually hold. Several are still marked `open`.

## Why another skill set

Existing skills already port the strategy half of the essay (taste, novelty, kill early, conclusion first), notably [andrehuang/research-companion](https://github.com/andrehuang/research-companion), [moralespanitz/carlini-dm](https://github.com/moralespanitz/carlini-dm), and [moralespanitz/research-loop](https://github.com/moralespanitz/research-loop). What they leave out is the habit layer: the append-only ideas log, the fixed threat checklist run against every new system, the three reading modes, the release checklist, the read-aloud pass, and the portfolio view (one or two potentially great papers a year; the award is a sample, you own the distribution). This repository puts the credo in one place and builds the habits as separate, small skills.

## Skills

| Skill | Use it when | Result |
| --- | --- | --- |
| [research-credo](skills/research-credo/SKILL.md) | Deciding what to work on, ranking directions, checking a plan against the principles | Verdict in prose, the tenets applied, one next action |
| [conclusion-first](skills/conclusion-first/SKILL.md) | Before starting a project, or when one stalls | Best-case conclusion, riskiest sub-problem, continue / kill / pivot / de-risk verdict |
| [ideas-log](skills/ideas-log/SKILL.md) | An idea shows up mid-task, or it is time to pick the next project | Appended entry in a write-mostly log; dated review pass when choosing |
| [threat-list](skills/threat-list/SKILL.md) | A new dataset, model, API, agent, or pipeline appears | Applicability memo over a fixed list of failure modes; "nothing here" is a valid result |
| [reading-modes](skills/reading-modes/SKILL.md) | A paper or preprint lands | Scan, extract, or reproduce output, and the conventions the paper inherits without argument |
| [writing-pass](skills/writing-pass/SKILL.md) | Revising an abstract, introduction, figure, conclusion, or full draft | Revised text tied to the writing rules, read-aloud pass, timeboxed |
| [paper-release-checklist](skills/paper-release-checklist/SKILL.md) | Submitting, uploading to arXiv, or sending a camera-ready | Mechanical checks with file:line evidence, then the manual list for that release type |

The principles themselves live in [skills/research-credo/references/tenets.md](skills/research-credo/references/tenets.md).

## Install

Each skill is a self-contained directory with a `SKILL.md`. Link or copy the ones you want into your harness's skill directory.

Claude Code (user scope):

```bash
for s in skills/*/; do ln -s "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"; done
```

Codex (user scope):

```bash
for s in skills/*/; do ln -s "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"; done
```

Project scope works the same way with `.claude/skills/` or `.agents/skills/` inside a repository. Frontmatter is limited to `name` and `description`, so the same files load in both harnesses. Harness-specific extras (plugin manifests, `agents/openai.yaml`) are not included yet.

The release checklist script needs Python 3.10 or newer and no third-party packages:

```bash
python3 skills/paper-release-checklist/scripts/check_tex.py path/to/main.tex
```

## Attribution and license

Tenets are short paraphrases with links to the source posts; quotations are kept brief. The skills' wording, structure, and scripts are original to this repository. License: not yet chosen.
