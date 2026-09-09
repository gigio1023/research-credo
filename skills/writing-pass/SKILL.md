---
name: writing-pass
description: "Revise a research paper draft, abstract, introduction, figure caption, or conclusion against fixed writing rules: exactly one idea, a named reader (default: the author six months ago), an abstract with at least one specific number and no hedging, an introduction that tells the story in at most two pages, figures that stand alone with their captions, a conclusion that answers 'so what' rather than restating the abstract, and a read-aloud pass. Use when the user asks to review, tighten, or rewrite paper text or asks whether a section reads well. NOT for deciding what to write about (conclusion-first), submission mechanics (paper-release-checklist), or blog posts and general prose."
---

# Writing Pass

Outcome: revised text that the named reader can follow, each change tied to a rule, the claims and numbers unchanged, and a list of what was not done inside the time budget. The rules are adapted from the writing sections of Carlini's [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html).

## Before editing

Establish three things, asking when missing:

1. The one idea, in one sentence. If the user cannot state it, or the sentence needs an "and", stop: the draft is trying to do two things, and no amount of editing fixes that. Report it and offer conclusion-first.
2. The reader. Default is the author six months ago: what would they have needed to hear to believe this idea was worth pursuing and this design was right? If the paper argues against a community's belief, the reader is one member of that community.
3. The time budget. Ask for one and stop when it runs out. Report what remains untouched rather than continuing.

## Rules by section

| Section | Rule | Check |
| --- | --- | --- |
| Title | Accurate, not clever. If a title is hard to write, the paper has more than one idea; fix the cause. | Does the title describe what the paper shows? |
| Abstract | Five moves: topic, the problem in it, result or method, whichever of those was not covered, why it matters. For a broad topic or narrow audience use three: claim, evidence, impact. At least one specific number. No hedging; state the clean, true version. | Is there a number? Any "may", "could potentially", "we believe" that the evidence does not require? |
| Introduction | A story: start where the reader stands, move them into the world where the idea makes sense, then state the contribution. At most two pages. Match the effort to the reader's distance: one sentence for a known problem, a paragraph to remind, two pages to sell a new setting. For a heretical claim, present the evidence and let the reader reach the conclusion. | Where does the reader stand in paragraph one? Where is the contribution stated? |
| Background | Its job is to widen who "the reader" is; after it, assume they know what it taught. Not a block of citations. | Does each paragraph teach something the method later relies on? |
| Figures | Each understood from its caption alone; one-sentence takeaway in the caption. If a caption cannot explain it, split the figure. | Read only figures and captions: is the story visible? |
| Conclusion | Not the abstract in the past tense. Remind briefly, then answer "so what" plainly. Be heavy-handed about the moral. | Does it say something the abstract did not? |
| Prose | Read it aloud or through text-to-speech and fix what does not land. Watch sentences with two readings, sentences that set up one thing and say another, and emphasis on the wrong word. Jargon only where the alternative is imprecise. Long sentences are fine when short ones follow. | Read-aloud pass done? |

## Preservation

Do not change claims, numbers, or the scope of what the evidence supports. Removing hedges means stating what the results show, not upgrading them. When a hedge exists because the evidence is weak, say so and leave the claim alone or narrow it; do not strengthen it. Keep LaTeX macros, citations, and labels intact.

## Output

1. The revised text, or the revised sections in order.
2. A change list: each change with the rule it serves.
3. Rule violations left in place with the reason (evidence, time budget, author's call).
4. What the read-aloud pass caught, and what was not read because time ran out.
