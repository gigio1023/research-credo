# Checklist

Adapted from Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) (2022-01-30). Items marked (script) are covered by `scripts/check_tex.py`; the rest are manual. Add new items with a date when a new mistake happens.

## Every release

- Title is correct (script prints it; the user confirms).
- Author TODO macros are disabled and no TODO or FIXME text remains (script).
- LaTeX build log is clean: search it for `error`, `warning`, `undefined`, `missing` (manual; needs the log).
- Doubled words such as "the the" (script; review each, some are legitimate).
- Lines with `..` that are not `...`, and `??` from unresolved references (script).
- No merge-conflict markers `<<<<<<<`, `=======`, `>>>>>>>` (script).
- No paragraph ending with a single word on its own line; no single line stranded at the top of a page under a caption (manual; PDF).
- Every caption is understandable in near-isolation and was not broken by late edits (manual).
- The PDF renders on another machine: fonts embedded, figures legible (manual).

## Conference submission

- Call for papers checked for blind versus non-blind rules. If blind, author names appear nowhere in the document (script with `--blind --author`; also check acknowledgments and self-citation phrasing by hand).
- Page numbering follows the call for papers.
- Page count is within the limit; check separate rules for appendix and references versus content pages (manual; PDF).
- Bibliography style matches the venue.
- For security venues, the author field reads like "anonymous submission #xyz" with varied formatting when submitting several papers.

## Public release (camera-ready)

- All authors listed; names spelled correctly; affiliations correct.
- Template switched to the accepted version of the style.
- Author block does not break the flow of page one.
- Copyright block or publication notice added as the venue requires.
- Type 3 fonts absent if the venue cares.
- Acknowledgments and author-contribution sections uncommented.

## arXiv upload

- Decide whether to strip LaTeX comments before upload.
- Author names on the upload form match the paper (allowing the authors' preferred ASCII variants).
- Copyright block removed if the venue's terms require it for preprints.
- Abstract on the form has no LaTeX macros (script prints the abstract for review).
- The rendered arXiv PDF matches the local build.

## Added later

Record date, mistake, and check here.
