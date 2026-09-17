# Sources and Scope

Reviewed September 17, 2026 while authoring this package.

- [Google Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook): inspected the initial-configuration, incremental-tuning, exploration, and experimental-goal sections. Adopted narrow informative rounds, separation of scientific and nuisance settings, and explicit compute tradeoffs. It assumes a working training pipeline and sufficient tuning resources; its batch-size and optimizer advice is not imposed on every architecture.
- [Kapoor and Narayanan, Leakage and the Reproducibility Crisis in ML-based Science](https://arxiv.org/abs/2207.07048): inspected the abstract and publication metadata. It motivates explicit leakage review; this package does not claim to have reproduced the paper or its survey.

The portable workflow and synthetic examples are independently authored. Runtime commands come from the actual project's implementation and version-specific framework documentation. The sources do not establish that these skill instructions improve model behavior.
