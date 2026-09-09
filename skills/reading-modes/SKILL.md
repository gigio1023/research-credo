---
name: reading-modes
description: "Read a paper in one of three declared modes and return only what that mode needs. Scan gives the one new thing in one sentence and whether it is useful; extract pulls the specific technique, setup, or result the current project needs; reproduce lists the assumptions, omissions, and errors and what redoing the work would take. Use when the user shares a paper, arXiv link, or PDF and asks what it does, whether to read it, or what to take from it. NOT for literature surveys across many papers or for writing related-work sections."
---

# Reading Modes

Outcome: the user gets the output of one reading mode, sized to that mode, plus a short note on which of the field's conventions the paper inherits without argument. Reading budgets differ by an order of magnitude between modes; do not spend reproduce-level effort on a scan.

Adapted from the "Read all the papers" and "Ignore all the papers" sections of Carlini's [How to win a best paper award](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html).

## Pick the mode

- Scan (default): the user wants to know whether the paper matters. Most papers get this and nothing more.
- Extract: the user names what they need from it (a technique, an experimental setup, a specific result, a proof step).
- Reproduce: the user intends to build on or refute the paper, or asks for a critical read. A few per month at most.

If the paper is not accessible (paywall, missing PDF), say so and stop. Do not reconstruct a paper from its abstract or from memory and present it as a read.

## Scan

Return two lines: the one new thing the paper adds, in one sentence in your words, and whether it is useful to the user's stated work. If the paper does not make its one thing findable, say that; it is information about the paper. Do not paraphrase the abstract as the takeaway.

## Extract

Return only the requested piece with enough surrounding detail to use it: the exact definition, the hyperparameters or setup, the number with its evaluation unit and denominator, the proof step with its assumptions. Cite the section, table, or equation. Do not summarize the rest of the paper.

## Reproduce

Read top to bottom and return:

1. What you would need to redo the work without the paper: data, code, compute, and the steps the paper leaves implicit.
2. Assumptions the method depends on, stated or not.
3. What is left for future work, and what is claimed but not shown.
4. Errors or inconsistencies found, with location.
5. Whether the evaluation would convince a skeptical reader, and the one experiment that is missing if not.

## Inherited conventions

For every mode, add one short paragraph naming the conventions the paper adopts because the field does (metric choice, threat model, baseline set, dataset, an early paper's arbitrary decision). Mark any that look unjustified. This is the note the user keeps after deliberately setting the paper aside, so their own approach is not shaped by defaults nobody argued for.

## Output

State the mode used, then the mode's content, then the inherited-conventions paragraph. Nothing else.
