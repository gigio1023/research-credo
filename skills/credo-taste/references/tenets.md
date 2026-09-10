# Tenets

Scope: these apply to long-horizon work only, as the repository `AGENTS.md` defines it. They are not a standard for near-term deliverables.

Paraphrased from Nicholas Carlini's writing, mainly [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) (2026-03-09). Section names in parentheses point to that post unless another source is given. Read the originals; these lines are pointers, not replacements. The `stance` column records the owner's position: `adopted` means held as written, `adapted` means held with a change noted here, `open` means undecided.

## Contents

- Choosing problems (T1 to T7)
- Executing (T8 to T10)
- Writing (T11 to T13)
- After submission (T14)
- Habits (T15)
- Sources

## Choosing problems

| # | Tenet | Source | Stance |
| --- | --- | --- | --- |
| T1 | Taste in which problems are worth solving is the single most important research skill. It comes from doing research while paying attention to what worked and what did not, not from reading about it. | Have good taste for problems | adopted |
| T2 | Collaboration starts with work, not admiration. Bring a partial solution to someone already interested in the problem; that email gets answered. Ideas are cheap and execution is hard, so share ideas freely. | Have great collaborators | adopted |
| T3 | Read papers in three modes with different budgets: scan most of them for the one new thing, extract only what the current project needs from related ones, and fully reproduce a few per month. Then set the field's inherited conventions aside so they do not become your defaults. | Read all the papers; Ignore all the papers | adopted |
| T4 | Do not start research with the goal of a conference paper. Aim to find something important and new; the paper follows. One or two projects a year may be great; the rest are practice, and practice is how the great ones are found. | Pick your ideas for impact | adopted |
| T5 | The size of a contribution is the number of months between your result and when the next person would have found it. Aim for problems that would have taken others months, and notice where reading the literature makes you want to shout that everyone is doing it wrong. | Do something only you can do | adopted |
| T6 | Impact is your skill in an area multiplied by how much the area matters right now. Find the corner of the field where you are strongest, name your comparative advantage, and be honest when the world has moved past what you are best at. | Find your comparative advantage; Get lucky: well suited | adapted: the owner names their own comparative advantage in this file when known |
| T7 | Keep a fixed list of ways a system can fail (evasion at inference time, data poisoning, model extraction, training-data extraction, and the rest) and run the whole list against every new system, dataset, or API. Most runs find nothing. That is the cost of finding the ones that matter. | [Latent Space interview](https://www.latent.space/p/carlini), problem-selection segment around 00:53 | adopted; list maintained in the `credo-threat-list` habit under `habits/` |

## Executing

| # | Tenet | Source | Stance |
| --- | --- | --- | --- |
| T8 | Start with the sub-problem most likely to fail, as a small prototype. Expect to finish roughly one project in five. Kill projects that do not work, kill projects that work but will not matter, and pivot when something clearly more important appears, without sunk-cost loyalty and without mistaking novelty for importance. | Kill papers that are not working; Kill papers that end up having low impact; Re-prioritize projects ruthlessly | adopted |
| T9 | Go to lengths a reasonable person would not. Run the extra trials, control the confounders, and answer the skeptical reader's question with an experiment before they ask it. Spending hours to upgrade "sometimes" to "usually" is what caring looks like. | Put in an unreasonable amount of effort | adopted |
| T10 | A paper advances one idea. Write that idea down before the work starts and connect every experiment, paragraph, and figure to it. At the end the paper should sit at a local optimum with no obvious missing experiment, while still leaving small open directions for others. | Have focus; The paper should be the "maximal" version | adopted |

## Writing

| # | Tenet | Source | Stance |
| --- | --- | --- | --- |
| T11 | Write for one reader; the default is yourself six months ago. The abstract carries at least one specific number and no hedging. The introduction is a story that starts where the reader stands and reaches your contribution in at most two pages; when the claim is heretical, lay out the evidence and let the reader arrive at it. | Know your reader; Your abstract does matter; Write a good introduction | adopted |
| T12 | Each figure must be understood from its caption alone. The conclusion is not the abstract in the past tense; it answers "so what". Write the best-case conclusion before doing the research, and drop the project if that conclusion says nothing beyond repeating results. | Each figure must stand on its own; Write a good conclusion | adopted |
| T13 | Read the draft aloud or through text-to-speech and fix what does not land. Being not-bad at prose is enough. Timebox the writing; proofreading has diminishing returns. | On Writing; [Latent Space interview](https://www.latent.space/p/carlini) around 00:07 on timeboxing | open: the owner has not yet decided how strictly to timebox |

## After submission

| # | Tenet | Source | Stance |
| --- | --- | --- | --- |
| T14 | Most award-winning papers were rejected first, sometimes several times, usually because they were early. An award is one sample from a distribution you do not control. You control the distribution. Revise to make the argument land, resubmit, and do not chase the sample. | Don't get discouraged; Conclusion | adopted |

## Habits

| # | Tenet | Source | Stance |
| --- | --- | --- | --- |
| T15 | Keep an append-only ideas file that records problems worth solving rather than solutions, and re-read it only a few times a year so each idea is judged twice with time between. Run a written checklist before every paper release. Keep experiment iteration under a second where possible. | [My research idea logfile](https://nicholas.carlini.com/writing/2024/my-research-logfile.html); [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/credo-release-checklist.html); [Rapid Iteration](https://nicholas.carlini.com/writing/2022/rapid-iteration-machine-learning-research.html) | adopted |

## Where the owner departs from the source

Record disagreements here so the skills can enforce the owner's version. Examples of choices the source leaves to you: whether the paper title truly does not matter; whether one reader (Carlini) or several audiences (editor, reviewer, field) is the right target; how hard to timebox.

## Sources

- Carlini, N. (2026-03-09). How to win a best paper award (or, an opinionated take on how to do important research that matters). https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html
- Carlini, N. (2024-01-21). My research idea logfile, 2016-2019. https://nicholas.carlini.com/writing/2024/my-research-logfile.html
- Carlini, N. (2022-01-30). Research Paper Release Checklist. https://nicholas.carlini.com/writing/2022/credo-release-checklist.html
- Carlini, N. (2022-06-19). Rapid Iteration in Machine Learning Research. https://nicholas.carlini.com/writing/2022/rapid-iteration-machine-learning-research.html
- Latent Space (2024-08-29). Why you should write your own LLM benchmarks, with Nicholas Carlini. https://www.latent.space/p/carlini
