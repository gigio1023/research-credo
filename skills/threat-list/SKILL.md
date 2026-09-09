---
name: threat-list
description: "Run a fixed list of failure modes against a newly encountered ML system, dataset, API, model release, agent, or data pipeline: evasion at inference time, data poisoning, model extraction, training-data extraction, prompt injection, and the rest of the list. Use when the user says 'a new dataset/model/API appeared, is there an attack here', 'threat-model this', or when a research direction touches an unfamiliar system. Output is an applicability memo; finding nothing is a normal result. NOT for executing attacks, running a red-team campaign or penetration test, or reviewing an internal product's security (follow that team's process)."
---

# Threat List

Outcome: a short memo that says, for each item on the fixed list, whether it applies to this system, why (which interface, access level, or data flow makes it possible), how practical the most realistic version would be, and whether it is worth a research look. Zero leads is a legitimate memo.

The habit comes from Carlini's description on the [Latent Space podcast](https://www.latent.space/p/carlini) (around 00:53) of keeping a list of bad things that could happen and checking every new system against all of it, accepting that most checks come back empty. The list lives in [references/checklist.md](references/checklist.md); read it before the pass.

## Inputs

Before running the list, establish from the user or from available documentation:

- What the system is: model, dataset, serving API, agent with tools, training pipeline, or retrieval stack.
- Who controls what: who trains, who serves, who supplies data, who can query, and with what access (query outputs only, logits or probabilities, weights, training data).
- Exposed interfaces and their limits: rate limits, logged fields, returned fields, file or URL ingestion, tool calls.
- Assets that matter: weights, training data, user data, system prompt, downstream actions.

If these are unknown, say which are unknown and run the list anyway, marking items whose applicability depends on the missing fact.

## The pass

For every item in the checklist, in order, write one row:

| Item | Applies? | Why (interface, access, data flow) | Most realistic variant and rough cost | Known prior work | Worth a look? |

Rules:

- Separate the objective (what would fail) from the technique (how) and from the access assumed. A row that names only a technique is incomplete.
- Prefer the practical variant. The question is not "could an idealized adversary do this" but "is going through the model or data the easiest way to make the bad thing happen". Carlini's expired-domain poisoning of web-scale datasets is the model case: a known objective made practical by one observation about how the data was distributed.
- Do not skip items because they feel unlikely. An empty row with a reason is the point of a fixed list.
- Do not claim novelty. "Known prior work" is what you can cite now; "none known" means you did not find one, not that none exists.

## Output

1. The table, all items.
2. At most two leads, each with the one observation that makes it practical and the first cheap experiment that would confirm or kill it. Hand a lead to conclusion-first if the user wants to pursue it.
3. If nothing applies, say so in one sentence. Do not manufacture a lead.
4. A disclosure note when a lead is real: is the flaw patchable by the system owner or not, since that decides how quickly it should be reported and published.

This skill analyzes. It does not run attacks, query production systems adversarially, or contact vendors.
