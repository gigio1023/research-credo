---
name: read-then-forget
description: "Read a paper the way the essay prescribes: pick the mode (scan for the one new thing, extract one needed piece, or reproduce), then name what the paper inherits from its field without argument and what the user would do if they had not read it. Use when a paper, preprint, or PDF lands during long-horizon work and the user asks what it does, whether to read it, or what to take from it. NOT for surveys across many papers, related-work sections, or reading for a near-term deliverable."
---

# Read, Then Forget

Outcome: the user gets exactly what one reading mode is for, and then a short note that helps them set the paper aside without inheriting its defaults. The second part is the point: read everything, then do not let it decide your approach.

Scope: long-horizon work only, per the repository's `AGENTS.md`.

Adapted from the "Read all the papers" and "Ignore all the papers" sections of Carlini's essay.

## Read: pick the mode

- Scan (default, most papers). Return two lines: the one new thing in your words, and whether it matters for the user's stated work. If the paper hides its one thing, say so; that is information about the paper. Do not paraphrase the abstract.
- Extract (the user names what they need). Return only that piece with enough context to use it: the definition, the setup, the number with its unit and denominator, the proof step with its assumptions, and where it is in the paper.
- Reproduce (a few per month; the user intends to build on or refute it). Return what redoing the work would take, the assumptions stated and unstated, what is claimed but not shown, errors found with location, and the one missing experiment a skeptical reader would want.

If the paper is not accessible, say so and stop. Do not reconstruct it from the abstract or from memory.

## Then forget

Add one paragraph with three parts:

1. Inherited conventions: the metric, threat model, baseline set, dataset, or early arbitrary decision the paper adopts because the field does, with any that look unjustified marked.
2. The counterfactual: if the user had not read this paper, what would they have done on their problem? Name where the paper's framing would pull them and whether that pull is earned.
3. One question the paper makes the user want to shout about, if any. That is where their own problem may be (see episode E1 in the taste references).

## Output

The mode and its content, then the forget paragraph. Nothing else.
