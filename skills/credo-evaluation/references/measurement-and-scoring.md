# Measurement and Scoring

## Capability and cases

Describe the observable behavior that counts as success and the cases likely to distinguish competent from superficial performance. Behavioral tests can cover minimum capability, invariance under an irrelevant change, or an expected directional change. Select a form that matches the task; not every benchmark needs all three.

Separate the construct from its proxy. Exact match can be valid for a structured answer but inappropriate where multiple answers are acceptable. Conversely, semantic similarity can reward a plausible response that violates a decisive requirement.

## Metrics and aggregation

Define numerators and denominators before implementation. State how failures, abstentions, invalid outputs, duplicates, repeated trials, and missing records enter the result. Missing is not zero unless the metric explicitly defines that treatment.

Use macro or micro aggregation according to the target question and show a meaningful subgroup when a summary could reverse the interpretation. Latency conditioned on successful responses is a different quantity from reliable request completion. Record both when the decision needs both; do not require every report to reproduce every field.

Estimate uncertainty at the actual independent unit. Repeated paraphrases or requests from one case are not necessarily independent samples. Use paired comparisons when the same cases allow them. Resampling, confidence intervals, and significance tests require assumptions; choose and explain the method instead of adding a generic interval to every score.

## Scorers and judges

Test canonical correct, incorrect, boundary, invalid, and missing outputs. Check normalization, parsing, units, aggregation, and any scorer version change. Keep raw outputs so permitted rescoring can produce linked derived results rather than overwrite history.

For human labels or model judges, establish the criterion and independent reference judgments needed for the decision. Inspect disagreement by relevant class or error type. Test order sensitivity, answer-format preferences, and reference dependence when plausible. Do not treat one judge's score as a general quality measurement without validation.

## Comparison and adaptation

Record which changes came from development feedback. A held-out assessment reused for selection is no longer independent of that selection. Differences in prompt, tools, sampling, or compute may be part of the intended system comparison; identify them rather than pretending the checkpoint alone caused the result.

If an evaluation reveals that its own method is misleading, state the observed issue and propose the correction. User confirmation is needed when the correction changes the research direction or success criterion, not for every local scorer bug fix already authorized.

## Synthetic example

A scorer counts a malformed answer as absent and drops it from the denominator. The resulting accuracy describes only parseable answers. Hand-worked invalid-output cases expose the mismatch if the intended measure is success over all submitted cases. Correcting the method is separate from rerunning the model, which may be unnecessary if retained raw outputs support rescoring.
