---
name: credo-read-then-forget
description: "Read a paper in a declared mode (scan for the one new thing, extract one needed piece, or reproduce), then examine inherited assumptions when they could change the user's approach. Use when a paper, preprint, or PDF lands and the user asks what it does, whether to read it, or what to take from it. NOT for surveys across many papers or related-work sections."
---

# Read, Then Forget

Outcome: deliver the requested reading result and, when useful, a short check of assumptions the user might otherwise inherit. A narrow extraction does not need an additional reflection.

Scope: reading that supports the user's current research or engineering question. Use the assumption check when a paper's framing could change the approach, regardless of project duration. A narrow extraction can finish with the requested piece when broader reflection adds nothing.

Adapted from the "Read all the papers" and "Ignore all the papers" sections of Carlini's essay.

## Read: pick the mode

- Scan (default, most papers). Return two lines: the one new thing in your words, and whether it matters for the user's stated work. If the paper hides its one thing, say so; that is information about the paper. Do not paraphrase the abstract.
- Extract (the user names what they need). Return only that piece with enough context to use it: the definition, the setup, the number with its unit and denominator, the proof step with its assumptions, and where it is in the paper.
- Reproduce (the user intends to build on or refute it). Return what redoing the work would take, the assumptions stated and unstated, what is claimed but not shown, errors found with location, and the one missing experiment a skeptical reader would want.

If the paper is not accessible, say so and stop. Do not reconstruct it from the abstract or from memory.

## Then forget

When inherited assumptions could change the user's approach, explain the relevant parts briefly:

1. Inherited conventions: the metric, threat model, baseline set, dataset, or early arbitrary decision the paper adopts because the field does, with any that look unjustified marked.
2. The counterfactual: if the user had not read this paper, what would they have done on their problem? Name where the paper's framing would pull them and whether that pull is earned.
3. One question the paper makes the user want to shout about, if any. That is where their own problem may be (episode E1 in the credo-taste package, file episodes.md under its references).

## Output

The chosen reading result, then a brief assumption check when useful. Do not impose a reflection paragraph on a straightforward lookup.
