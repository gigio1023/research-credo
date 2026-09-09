# Manual checklist

Adapted from Carlini's [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) (2022-01-30). Only the items that need a person are here. Items a program can check (TODO markers, merge-conflict markers, doubled words, `..` and `??`, blind author names, abstract macros, commented-out acknowledgments, build-log words) are run by latex-release-lint; see its coverage reference. Add new items with a date under "Added later".

## Every release

- Title is correct: compare the printed `\title{}` text against the submission form or accepted title.
- Build log is clean, if it was not given to the lint script: search it for error, warning, undefined, missing.
- No paragraph ends with a single word on its own line; no single line is stranded at the top of a page under a caption (open the PDF).
- Every caption is understandable in near-isolation and late edits did not break one (read only the captions).
- The PDF renders on another computer: fonts embedded, figures legible.

## Conference submission

- Call for papers checked for blind versus non-blind rules; if blind, also check affiliations, grant numbers, repository links, and self-citation phrasing, which the lint script does not know.
- Page numbering follows the call for papers.
- Page count is within the limit, with separate rules for appendix and references versus content pages.
- Bibliography style matches the venue.
- For security venues, the author field reads like "anonymous submission #xyz", with varied formatting when submitting several papers.

## Public release (camera-ready)

- All authors listed; names spelled correctly; affiliations correct.
- Template switched to the accepted version of the style.
- Author block does not break the flow of page one.
- Copyright block or publication notice added as the venue requires.
- Type 3 fonts absent if the venue cares (`pdffonts` or the venue's checker).
- Acknowledgments and author-contribution sections are present and uncommented (the lint script flags a commented heading; confirm by reading the PDF).

## arXiv upload

- Decide whether to strip LaTeX comments before upload.
- Author names on the upload form match the paper, allowing the authors' preferred ASCII variants.
- Copyright block removed if the venue's terms require it for preprints.
- Abstract on the form has no LaTeX macros (paste the text the lint script printed).
- The rendered arXiv PDF matches the local build.

## Added later

Record date, mistake, and the check that would have caught it.
