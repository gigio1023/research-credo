---
name: credo-dataset
description: >
  Design, build, or review a training or evaluation dataset: sampling,
  selection, annotation, splits, provenance, leakage, and quality. Use for
  dataset composition and label-review work. NOT for choosing benchmark
  metrics, literature collection alone, or merely operating an evaluation run.
---

# Credo: Dataset

Make the data fit its intended use and establish what its construction supports. A schema-valid collection is not necessarily a suitable dataset; a reviewed sample is not proof that every record is correct.

## Establish intended use

Recover the target task, intended population, unit of observation, source material, existing dataset, and permitted data handling. Identify the dataset decision: build a first version, revise a known problem, assess labels, inspect a split, or judge whether a claim is supported.

Inspect available records and representative examples before prescribing categories. Record inclusion and exclusion rules only where they change selection or interpretation. Prefer existing identifiers, schemas, storage, and versioning. A review returns findings; construction or revision requires the corresponding request.

## Construct or inspect the data

Read [construction and review](references/construction-and-review.md) for the relevant sampling, annotation, splitting, or lineage decision. Keep the normal work concrete:

- Relate sampling and coverage to the target population. Convenience sources and synthetic examples do not establish representative coverage.
- Define ambiguous labels using task-specific examples and counterexamples. Preserve disagreements rather than forcing uncertain items into a clean label.
- Separate independent label judgment from model-generated suggestions when independence matters. A generated label is a candidate until the required review establishes it.
- Choose splits by the unit of intended generalization, including related entities, time, documents, or source groups where needed. Check exact and meaningful near-duplication across those boundaries.
- Track transformations and exclusions enough to recover the dataset version and explain a consequential difference. Keep originals under the project's access and retention rules.

For training data, inspect target formatting, contamination of evaluation material, sampling weights, and label noise as relevant. For evaluation data, preserve separation from tuning and scoring decisions that would leak answers. For either, do not infer legal permission or consent from public availability; follow the supplied access and usage constraints.

Use authorized tools and storage. Fast checks within the task can proceed; new collection, external annotation, provider transfer, or a long processing campaign must fit the existing grant. Ask before changing the research purpose or committing to long new work.

## Verify and deliver

Use appropriate structural checks and actual content review. Check counts by the meaningful units: records, unique source groups, assignments, independent labels, and reviewed items are not interchangeable. Sample across relevant groups and failure modes; state the reviewed coverage only when it affects the conclusion.

Deliver the requested version and usable documentation, or findings with representative examples and the implication for use. Preserve underlying data records without dumping their provenance into every reader-facing report. A negative suitability finding can finish a review without modifying the data.

Use credo-evaluation for measurement and benchmark-method decisions, credo-experiment for downstream training comparisons, and evaluation-operations for running an approved evaluation. Reuse their established question rather than requiring a workflow through all three.

Read [sources](references/sources.md) when maintaining the skill.
