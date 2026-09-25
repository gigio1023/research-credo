---
name: credo-experiment
description: >
  Design, run, or review a bounded research experiment or model-training
  comparison when asked to test an idea, improve a model, reproduce a result,
  or interpret experimental findings. NOT for literature collection alone,
  dataset construction, benchmark-method design, or campaign status tracking.
---

# Credo: Experiment

Turn a research question into a useful comparison, inspect what actually happened, and decide what the result supports. Work can finish with a negative finding or a bounded unresolved question. A trained checkpoint or higher score is not automatically a useful research conclusion.

## Choose the next informative experiment

Recover the question, existing results, relevant model and data, and constraints before asking. State which alternatives the next observation could distinguish and how the answer would change the work. For performance improvement, identify the intended benefit and a credible current baseline; for reproduction, identify the original claim and conditions.

Choose the smallest comparison that can answer this round's question. Specify the changed factor, the baseline, comparison conditions, meaningful outputs, and the reason the comparison is informative. Tune nuisance settings fairly when they interact with the factor under study; identical settings are not always a fair comparison. Distinguish exploratory selection from a confirmatory comparison.

With little compute, iterate at the smallest model and data scale at which the phenomenon still appears, and say so when a result may not transfer to full scale. With little data, spend it on evaluation before training: a few hundred labeled examples usually buy a credible measurement and rarely a credible fine-tune. State what the available count supports before designing the comparison.

Keep future experiments conditional on the findings. Use the project's existing plan or a compact experiment note; do not create a mandatory new tracking framework. Read [design and interpretation](references/design-and-interpretation.md) for ambiguous baselines, interactions, variance, or inconclusive outcomes.

## Train or execute within the grant

A design or review request does not authorize training. For requested execution, inspect the actual runner, model/checkpoint, preprocessing, data split, objective, optimizer, schedule, compute allocation, and result records needed for this experiment. Follow the project implementation and framework's version-specific documentation.

Before an expensive run, use an authorized small check to establish that data reach the intended computation, losses and gradients behave plausibly, checkpoint save/load works, and the requested measurements can be recovered. A successful smoke test establishes readiness only. Read [training and recovery](references/training-and-recovery.md) for execution decisions.

Fast follow-up checks within the same research question and always-on resources may proceed. Present the observation, the proposed change, and one sentence predicting the result before changing direction, before any run that spends beyond the always-on tier or the project's stated budget, and before long new work, unless that activity is already authorized. Spend is the gate, not duration: a short run on paid accelerators needs the same presentation as a multi-day one. When the project has a praxis profile, its compute ladder and approval threshold define the tiers. Data access, shared hardware, and external-provider limits still apply to short runs.

Keep enough identity to associate results with their actual inputs and configurations. Use existing experiment logs and checkpoints, preserve unsuccessful attempts, and inspect live state before restarting. Use evaluation-operations for an evaluation campaign's dispatch, resume, scoring state, and attempts; do not create a second campaign registry.

## Interpret and continue

Inspect the actual outputs, comparison conditions, and errors. Separate measured observations from explanations and untested expectations. Investigate an apparent improvement's plausible alternatives, such as changed data, selection on validation results, a different compute budget, or a broken scorer. Use credo-dataset or credo-evaluation when the relevant question concerns data or measurement.

Report the result at its supported strength. Repetition or uncertainty estimates should answer a real decision question and respect dependence among observations; do not turn every experiment into a fixed seed-count ritual. An inconclusive difference is not equivalence.

Record what changed in the project's understanding, the decisive result location, and the next selected action or proposal. Complete the bounded round when the intended question is resolved to the requested degree or its remaining limit is established. Broader direction changes remain user decisions.

For maintenance and limits of the adopted methods, see [sources](references/sources.md).
