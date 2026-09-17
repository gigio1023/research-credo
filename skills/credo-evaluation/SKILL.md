---
name: credo-evaluation
description: >
  Design, build, or review an evaluation method or benchmark: the capability
  being measured, task design, metrics, scorers, comparison conditions, and
  interpretation. NOT for dataset construction alone or dispatching and
  monitoring an already-approved evaluation campaign.
---

# Credo: Evaluation

Establish whether an evaluation measures the intended capability and supports the decision being made. A working runner and a high score do not establish benchmark validity.

## Define the measurement

Recover the user's question, actual system use, target population, inputs and outputs, available data, and existing evaluator. State what ability or failure the measurement should reveal and which decision it informs. Do not replace the question with the easiest available metric.

Identify the unit being evaluated: a response, case, conversation, task completion, or system interaction. Separate task success, policy compliance, quality, latency, cost, and other dimensions when combining them would hide a consequential tradeoff. Use an aggregate only when its meaning and weighting fit the decision.

## Design or inspect the method

Read [measurement and scoring](references/measurement-and-scoring.md) for metrics, judge validation, uncertainty, and benchmark implementation. Select the checks needed for this question:

- Relate cases to intended behaviors and coverage. Include boundaries and plausible failure modes, not just easy examples or a leaderboard convention.
- Define scoring from observable outputs. Preserve units, denominators, exclusions, missing outcomes, and failure treatment in the underlying method.
- Choose comparison conditions that make the result meaningful, including model version, prompt, tools, decoding, available information, and resource budget when they affect the claim.
- Inspect shortcuts, contamination, and ways to improve the score without improving the intended capability. A suspected shortcut calls for a test, not a claim that the benchmark is invalid.
- Separate exploratory choices from assessment on material kept independent of those choices.

Use credo-dataset for selection, annotation, and split changes. This skill owns what is measured and how scores are interpreted, not a duplicate data-construction procedure.

## Build and validate when requested

A method review returns findings. A benchmark build request includes implementing the cases, scorer, aggregation, or harness changes necessary for the agreed method. Reuse the project's runner and interfaces rather than creating another framework.

Check hand-worked examples and important failure states against the actual scoring path before broad execution. Verify that the denominator and selected population are the same in the score, table, and chart. A mock response can validate the scorer's logic; it cannot establish target-model performance.

For model judges, validate the judge on task-relevant independently assessed examples, inspect errors and sensitivity, and keep its uncertainty distinct from the target's performance. Fluency and agreement with itself do not make the judge authoritative.

Use evaluation-operations for authorized multi-run dispatch, resume, scoring state, and result lineage. Fast method checks within scope can proceed. Ask before a changed research direction or long new campaign unless already authorized, preserving all resource and data-access limits.

## Interpret and deliver

State what the results establish and the conditions that matter to the intended reader. Keep method details available in their source records; do not repeat every definition, failure count, or configuration in a report when context already makes it clear. Do not hide a consequential failure to make the conclusion more favorable.

A review can finish by identifying why the present evidence cannot answer the question. A build is complete when the requested method and actual checks work, not when a desired score appears. Record the next decision or proposed discriminating test.

Read [sources](references/sources.md) when maintaining this package.
