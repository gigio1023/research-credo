---
name: ml-research-methods
description: >
  Design, run, or review an ML experiment, training comparison, dataset, or
  evaluation benchmark, and decide what its result supports. Use when asked to
  test an idea, improve or compare models, reproduce a result, build or review
  a dataset, its labels, or its splits, design metrics, scorers, or judges, or
  interpret experimental or evaluation findings. NOT for operating an approved
  multi-run campaign (evaluation-operations), literature collection
  (literature-research), or choosing a paper direction (credo-taste).
---

# ML Research Methods

Turn an empirical question into evidence that supports a decision: a comparison that can answer it, data fit for its intended use, and a measurement that reveals the intended capability. A trained checkpoint, a schema-valid dataset, a working runner, or a higher score is not by itself that evidence. A negative finding, an unsuitable dataset, or a bounded unresolved question can finish the work.

Use only the parts the task needs. An experiment, a dataset, and a measurement each stand alone, and one question often needs two of them.

## Start from the question

Recover the question, the decision the answer could change, existing results, the model, data, and evaluator in use, and the constraints before asking. Name the unit being compared, labelled, or scored (a run, record, case, response, conversation, or task completion) and keep counts in that unit; records, source groups, assignments, independent labels, and reviewed items are not interchangeable.

A design or review request returns findings. Building, training, labelling, or executing needs the corresponding request. Fast checks within the same question and always-on resources may proceed. Present the observation, the proposed change, and one sentence predicting the result before changing direction, before any run that spends beyond the always-on tier or the project's stated budget, and before long new work, unless that activity is already authorized. Spend is the gate, not duration: a short run on paid accelerators needs the same presentation as a multi-day one. When the project has a praxis profile, its compute ladder and approval threshold define the tiers. Data access, shared hardware, external annotation, and provider limits still apply to short runs, and public availability does not establish permission or consent.

Use the project's runner, records, identifiers, schemas, and plan. Do not create a new tracking framework, registry, or harness.

## Experiment

State which alternatives the next observation could distinguish and how the answer would change the work. For performance improvement, identify the intended benefit and a credible current baseline; for reproduction, the original claim and its conditions. Choose the smallest comparison that can answer this round: the changed factor, the baseline, comparison conditions, meaningful outputs, and why it is informative. Tune nuisance settings fairly when they interact with the factor under study; identical settings are not always a fair comparison. Separate exploratory selection from a confirmatory comparison.

With little compute, iterate at the smallest model and data scale at which the phenomenon still appears, and say when a result may not transfer to full scale. With little data, spend it on evaluation before training: a few hundred labelled examples usually buy a credible measurement and rarely a credible fine-tune.

For requested execution, inspect the actual runner, checkpoint, preprocessing, split, objective, optimizer, schedule, compute allocation, and result records the experiment depends on, following the framework's version-specific documentation. Before an expensive run, use an authorized small check that data reach the intended computation, losses and gradients behave plausibly, checkpoints save and load, and the measurements can be recovered; a smoke test establishes readiness only. Keep enough identity to tie results to their inputs and configurations, preserve unsuccessful attempts, and inspect live state before restarting.

Read [design and interpretation](references/design-and-interpretation.md) for baselines, interactions, variance, or inconclusive outcomes, and [training and recovery](references/training-and-recovery.md) for execution decisions.

## Dataset

Recover the target task, intended population, unit of observation, source material, permitted handling, and the dataset decision: build a first version, revise a known problem, assess labels, inspect a split, or judge whether a claim is supported. Inspect real records before prescribing categories.

- Relate sampling and coverage to the target population. Convenience sources and synthetic examples do not establish representative coverage.
- Define ambiguous labels with task-specific examples and counterexamples, and preserve disagreement rather than forcing uncertain items into a clean label. A model-generated label is a candidate until the required review establishes it.
- Split by the unit of intended generalization, such as related entities, time, documents, or source groups, and check exact and meaningful near-duplication across the boundary.
- Track transformations and exclusions well enough to recover the version and explain a consequential difference.

For training data, inspect target formatting, contamination with evaluation material, sampling weights, and label noise. For evaluation data, keep it separate from tuning and scoring decisions that would leak answers. Pair structural checks with content review sampled across relevant groups and failure modes; a reviewed sample is not proof that every record is correct. Read [construction and review](references/construction-and-review.md) for sampling, annotation, splitting, or lineage decisions.

## Measurement

State what ability or failure the measurement should reveal and which decision it informs; do not replace the question with the easiest available metric. Separate task success, policy compliance, quality, latency, and cost when combining them would hide a consequential trade-off, and use an aggregate only when its weighting fits the decision.

- Relate cases to intended behaviors, including boundaries and plausible failure modes, not only easy examples or a leaderboard convention.
- Define scoring from observable outputs, with units, denominators, exclusions, missing outcomes, and failure treatment. Missing is not zero.
- Fix the comparison conditions that affect the claim: model version, prompt, tools, decoding, available information, and resource budget.
- Inspect shortcuts and contamination, meaning ways to raise the score without the capability. A suspected shortcut calls for a test, not a verdict that the benchmark is invalid.

When building a benchmark, implement the agreed cases, scorer, and aggregation in the project's runner. Check hand-worked examples and important failure states against the actual scoring path before broad execution, and verify that the denominator and population match across score, table, and chart. A mock response validates scorer logic, not target-model performance. Validate a model judge on task-relevant, independently assessed examples, inspect its errors and sensitivity, and keep its uncertainty distinct from the target's performance. Read [measurement and scoring](references/measurement-and-scoring.md) for metrics, judge validation, uncertainty, and implementation.

## Interpret and report

Inspect actual outputs, comparison conditions, and errors. Separate measured observations from explanations and untested expectations, and investigate an apparent improvement's alternatives: changed data, selection on validation results, a different compute budget, a broken scorer. Repetition and uncertainty estimates should answer a real decision question at the actual independent unit; do not turn every experiment into a fixed seed-count ritual. An inconclusive difference is not equivalence.

Report the result at its supported strength with the conditions that matter to the reader, and keep full configuration and provenance in the project records. Do not hide a consequential failure to make a conclusion more favorable. Record what changed in the project's understanding, where the decisive result lives, and the next selected action or proposed test. Broader direction changes remain the user's decision. Use evaluation-operations to dispatch, resume, or track an approved multi-run campaign.

Read [sources](references/sources.md) when maintaining this package.
