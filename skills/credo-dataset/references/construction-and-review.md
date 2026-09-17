# Dataset Construction and Review

## Population and selection

Name what one item represents and what the dataset should generalize to. A user's sessions, a document's excerpts, and independently collected documents have different dependence. Counts should follow the chosen unit.

Describe actual source coverage and meaningful missing populations. If balancing or oversampling changes the distribution, distinguish construction counts from deployment prevalence. Keep synthetic material identified, with its generation and review scope when relevant. A generator's diversity claim is not measured coverage.

## Annotation

Write the operational label definition with positive, negative, and ambiguous examples. Pilot it on actual in-scope items before broad annotation when ambiguity could be costly. Identify who or what produced each label, which judgments were independent, and how unresolved disagreement is handled.

Review disagreements for a definition problem, missing context, or true ambiguity before treating every difference as annotator error. Aggregate agreement can conceal rare-label failure. Preserve the examples needed to repair the instruction, subject to privacy rules.

An adjudicated label can be an approved dataset decision without being unquestionable ground truth. Do not call generated question families, criterion assignments, or a formatting pass a gold-labelled dataset.

## Splits and leakage

Set the split boundary according to the intended use: entity, source, conversation, time, or another relevant unit. Fit preprocessing, selection, and imputation only on the information permitted for that split. Check whether near-duplicates or shared sources create shortcuts across it.

Use exact hashes for identical bytes or records and an appropriate similarity method for near-duplicates. Review borderline matches rather than treating every similarity threshold as fact. Split before data-dependent augmentation or retain source-group identity so descendants cannot cross boundaries.

Repeated exposure to a test set during tuning weakens its role as an independent final assessment. Document actual access; do not infer isolation from a filename such as test or gold.

## Dataset versions and review

Preserve stable identifiers and the reason for changed labels, exclusions, or transforms. Follow existing manifests and schema; add only the smallest missing documentation. A short source note can cover purpose, selection, annotation, split, permitted use, known limits, and version identity when those matter.

Verify both the loader's output and representative original records. Structural checks find missing fields or invalid values; semantic review establishes whether an item and label fit the task. Keep their conclusions distinct.

## Synthetic example

A dataset contains five paraphrases of each original query. Random row splitting puts related queries in train and test. If the intended claim is performance on unseen original queries, partition by original query first. If the intended use is repeated variants of known queries, that is a different claim and must be evaluated as such.
