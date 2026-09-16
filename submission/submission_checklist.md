# Submission Checklist — Journal of Integrative Agriculture

**Manuscript:** "Mining administrative approval records for technology assessment: record-level
trial-channel indicators and third-party-assayed grain quality in China's rice variety
registrations, 2017–2022"

> Checked against `plan/04_format_spec.md`. [x] = done by this automated pipeline and
> verifiable in the files as they stand. [ ] = requires action by the human author team before
> submission; this pipeline cannot complete these items.
>
> **v3 update (2026-09-16):** the manuscript no longer discusses Winall Hi-Tech Seed's
> financial performance, business strategy, or corporate governance anywhere in the paper, per
> author request; see `manuscript/review/change_log_v2_to_v3.md`. Checklist items below that
> referred to that content have been struck through or rewritten accordingly.
>
> **v4 update (2026-09-16):** the manuscript was reframed so that S&T information analysis
> stands as a main supporting pillar alongside agricultural technology assessment — new title,
> intelligence-source abstract opening, new Introduction paragraph, the Data section set out
> as a six-step intelligence-extraction pipeline, a new Discussion §8.4 "Implications for S&T
> intelligence practice", six new verified information-science references, and two new
> Highlights. **No statistical result, sample size, robustness conclusion, conflicting-evidence
> item (CF1–CF8) or Non-claim was changed.** See
> `manuscript/review/change_log_v3_to_v4.md`.

## 1. Article type and structure

- [x] Article type: Research Article.
- [x] Section order maps onto the official template (Institutional background nested after
      Introduction; Mechanism nested after Results, before Discussion) — see
      `manuscript/manuscript_v4.md` headings.
- [ ] **Word count** — the v3 draft is approximately 14,100 words (13,600 excluding
      References; slightly shorter than v2's ~14,500/13,900 after the v2→v3 Winall
      financial-narrative deletion, see `manuscript/review/change_log_v2_to_v3.md`), still
      above the 8,000–10,000-word informal target noted in `04_format_spec.md`
      §1 and flagged as still open in `manuscript/review/final_proof_log.md`. **Author
      action required**: either further compress the manuscript or confirm with the
      editorial office (informally, or at submission) that JIA's Research Articles have no
      hard word-count ceiling before submitting at this length.

## 2. Title, abstract, keywords

- [x] **(v4)** Title names the method ("Mining administrative approval records", "indicators")
      and the application ("technology assessment"), and uses "third-party-assayed" to scope the
      quality claim. It avoids effect/impact/caused-by language, consistent with the
      composition-effect estimand; the word "gap" moved from the title into the abstract and
      body, where the estimand is defined precisely.
- [x] Abstract: 249 words, under the 250-word structured-abstract limit.
- [ ] **Structured-abstract formatting** — the abstract is written as an implicitly
      structured paragraph rather than with explicit Background/Methods/Results/Conclusion
      labels, because the source material consulted could not confirm whether JIA requires
      explicit headings (see `manuscript/sections/front_matter.md` note). **Author action
      required**: confirm against the actual submission template or a recent JIA issue
      whether explicit headings are mandatory; if so, re-segment the existing 249 words under
      labels (no further word-cutting needed).
- [x] **(v4)** Keywords: 6, within the 3–6 range, none containing "and"/"of" as an internal
      connector — *administrative text mining; technology assessment; information extraction;
      data provenance; rice variety approval; China*. Four carry the S&T-information-analysis
      framing; *rice variety approval* and *China* preserve retrievability for JIA's agronomic
      readership.

## 3. Highlights

- [x] 5 bullets, each ≤85 characters including spaces (see `submission/highlights.md`);
      re-measured with `awk '{print length}'` after the v4 rewrite (83/79/71/78/81).
- [x] **(v4)** Bullets 1 and 5 carry the S&T-intelligence contribution (administrative-text
      corpus mining plus indicator construction; field-level data-reliability diagnostic).
- [ ] **Author action required**: submit `highlights.md` as its own file with "highlights" in
      the filename, per the journal's Guide for Authors.

## 4. Body-text writing rules

- [x] Estimand consistently described as a "composition effect," never "effect of / caused
      by / impact of."
- [x] No "fraud/manipulation" language; "measurement discretion" used throughout.
- [x] Winall section length checked qualitatively against the ≤15%-of-manuscript guideline
      (§7 is one of nine main sections and does not dominate the text).
- [x] **(v3)** §7 contains no discussion of Winall's financial performance, business strategy,
      or corporate governance; it is confined to the trial-channel-choice and within-channel
      quality-positioning evidence that supports the paper's identification argument (see
      Non-claim 10, §4.7, and `manuscript/review/change_log_v2_to_v3.md`).
- [x] No profit/revenue conversion of regression coefficients (§7 explicitly disclaims this).
- [x] No "ranked by integration depth" framing (§7 explicitly disclaims this).
- [x] Non-claims subsection present as its own numbered list at the end of §4 (12 items).
- [x] Conflicting-evidence items (bacterial-blight reversal, Arm 2 sign flips, R7/R9/R11/R13/
      R15 qualifying or non-supporting robustness results) are reported in the body, not
      omitted.

## 5. Figures and tables

- [x] **Figure/table compression to the 6-figure/5-table target — RESOLVED in the v2 session.**
      See `manuscript/figure_table_list.md` for the decision (Table 6/7 → Supplementary
      Table S1/S2; old Fig. 6 → Supplementary Fig. S1; old Fig. 7 → Fig. 6). Main text now
      carries exactly Fig. 1–6 and Table 1–5.
- [x] **(v3)** Former Supplementary Table S1 (Winall financial panel) removed entirely; former
      Table S2 renumbered to Table S1. Fig. 6 reduced from three panels to two (panel (c),
      Winall's financial time series, removed). See
      `manuscript/review/change_log_v2_to_v3.md`.
- [x] Every in-text figure/table citation checked against the new numbering by exhaustive
      grep; no stale reference to the old Table 6/7 or Fig. 7 numbering remains in the main
      text (one deliberate historical cross-reference in §7 is spelled out explicitly as
      "Table 7 in the pre-submission working draft").
- [x] Figures cited in ascending first-mention order matching their published numbers.
- [ ] **Image format/resolution** — `manuscript/figures/*.png` and `*.pdf` files exist but
      their resolution and colour-mode (RGB vs. CMYK) have not been verified against the
      journal's "no low-resolution GIF/BMP/PICT/WPG" requirement. **Author action required**:
      confirm each figure file meets the journal's minimum-resolution requirement before
      upload.
- [ ] **Supplementary Fig. S2 and Fig. S3 are not yet rendered as image files** (Manski
      bounds; chained-check ladder) — see `submission/supplementary_material.md`. Neither is
      cited by number in the main text, so this does not block submission, but **author
      action required** if the journal's submission system requires every named Supplementary
      figure to be an uploaded image file.
- [x] Non-linear image adjustments: none used; no gamma-correction disclosure needed.

## 6. References

- [x] Author-date system used throughout; reference list alphabetised; journal names spelled
      out in full.
- [x] **(v4)** Reference list grew from 21 to 27 entries. The six additions are S&T-information
      and information-science sources supporting the new framing — Antons et al. (2020),
      Franceschini et al. (2016), Jaffe and de Rassenfosse (2017), Losiewicz et al. (2000),
      Rammer and Es-Sadki (2023), Shi et al. (2021) — each verified against at least two
      independent tools, with per-entry verification records appended to
      `manuscript/references_verified.md` (entries 22–27). Two working-paper-versus-journal
      traps were caught and corrected during that check (Rammer and Es-Sadki: the SSRN
      preprint superseded by the *Technological Forecasting and Social Change* article of
      record; Jaffe and de Rassenfosse: NBER w21868 superseded by the JASIST article).
- [x] **(v4)** None of the six new sources was read in full text, so each is cited only for a
      general claim its title and abstract explicitly support, and **no specific figure from
      any of them is quoted** — the same conservative rule already applied to Gong et al.
      (2026).
- [ ] **Piepho & Laidig (2024)** reference is missing volume/page numbers — flagged as
      unresolved in `manuscript/references_verified.md`. **Author action required**: verify
      against CrossRef/publisher record before submission.
- [ ] **Gong et al. (2026)** is cited at title-level only; full text was not accessible during
      drafting (see reference and In-text note). **Author action required**: obtain the full
      text and confirm no specific figure needs re-attribution (this is also
      Unresolved-item **P5**, below).
- [ ] Three format-spec "mandatory" citations — Seck et al. (2023), Burris et al. (2025),
      Rangnekar (2000) — remain deliberately uncited because no paragraph in the current draft
      has a genuine point for them (see `manuscript/review/final_proof_log.md` §2, item 3).
      **Author action required**: either write a paragraph incorporating each, or formally
      drop them from the citation requirement before submission.

## 7. Units and statistical reporting

- [x] Yield reported in kg/亩 with kg/hm² conversion given at first mention.
- [x] Percentage-point traits reported as "percentage points (pp)" consistently.
- [x] Point estimates, 95% CIs, exact p-values, and BH-FDR q-values reported throughout;
      cluster level and cluster count stated for every clustered SE.
- [x] No star-only significance reporting; tables carry exact p-values.

## 8. Declarations — author-supplied content still needed

All of the following are placeholders in `manuscript/sections/declarations.md` and
`submission/declarations.md` and require the author team to fill in before submission:

- [ ] **Acknowledgements** — funding sources, reviewer/colleague thanks, etc.
- [ ] **CRediT author contributions** — assign each of Conceptualization, Methodology, Formal
      analysis, Investigation, Data curation, Writing (original draft), Writing (review &
      editing), Visualization, and Supervision to named authors.
- [ ] **Author names, order, and affiliations** — not yet fixed anywhere in the manuscript
      package; `[author names/affiliations]` placeholders throughout.
- [ ] **ORCID iDs** for all authors.
- [ ] **Corresponding author contact details** (email, mailing address) — placeholder in
      `submission/cover_letter.md`.
- [ ] **Funding/grant numbers**, if applicable, for the Acknowledgements section and any
      journal funding-disclosure form.
- [ ] **Data-availability repository link** — the Data Availability Statement currently says
      "[repository link]" as a placeholder; the actual repository (e.g. GitHub/Zenodo/OSF URL
      for parsing scripts, field dictionary, and record-ID list) must be created and linked
      before submission. Note this is contingent on resolving **P3** below (licensing status
      of the upstream `he-zhui/Rice_QA` compilation), which determines exactly what may be
      redistributed.

## 9. Submission-system practicalities

- [ ] **Confirm APC** (Article Processing Charge) — see Unresolved item **P12** below; JIA is
      reported to have moved to a US$1,800 APC as of 2026, which conflicts with earlier
      "no OA fee" search results. **Author action required**: confirm current fee against the
      chinaagrisci.com official notice before submission and confirm the budget covers it, or
      re-evaluate China Agricultural Economic Review / Rice Science as alternatives.
- [ ] **Confirm actual review timeline** — search results disagreed (12 weeks / 222 days /
      ~50 weeks); set author-team expectations accordingly (also covered by P6 below).
- [ ] Create an account and manuscript submission on ChinaAgriSci.com (the journal's own
      submission platform, not a standard Editorial Manager/EVISE system).

## 10. Unresolved items from `plan/00_decision_log.md` §5 and `plan/03_target_journal.md`

These items require human judgement, external verification, or access this automated
pipeline could not obtain (a blocked network, a document only a human account can retrieve, a
judgement call only the author team can make). **None of them can be closed by this
submission-package assembly step** — they are listed here so the author team has a single
place to track them before final submission.

| # | Item | Why it needs a human | Blocking level |
|---|---|---|---|
| **P1** | Whether the performance-evaluation criterion accepts "Economics" as well as "Agricultural & Forestry Sciences" as the journal's top-level discipline category | Determines whether China Agricultural Economic Review remains a viable fallback journal | High (journal-choice path) |
| **P2** | JIA's and Rice Science's official 2025 journal-quartile rankings | Can only be confirmed via an institutional account on fenqubiao.com or the official ranking table; this session could only use search-result summaries | High (must confirm before submission) |
| **P3** | Licensing status of the upstream `he-zhui/Rice_QA` GitHub compilation | Determines whether the Data Availability Statement may redistribute the parsed full table or must stay restricted to scripts/dictionary/ID list (current wording assumes the restrictive case) | High (Methods/Data Availability cannot be finalised without this) |
| **P4** | Field-by-field agreement rate between a 50-record random sample and the original MARA announcement text | The MARA announcement portal was not reachable from the automated session's network; this is the one step that would upgrade "the source is public MARA announcements" from an assertion to a verified fact — see manuscript §3.4 | High |
| **P5** | Full text of Gong et al. (2026) | Currently cited at title-level only; needed before attributing any specific figure to it | Medium |
| **P6** | JIA's actual APC/fee schedule and review-cycle length | Search sources disagreed significantly | Medium (also see item 9 above / P12) |
| **P7** | ~~Public documentary source for each individual Winall negative fact~~ | **Closed in v3**: the manuscript no longer reports any Winall financial/regulatory fact (fine, audit opinion, ST status, tender offer), so this compliance requirement no longer applies | Closed |
| **P8** | Manual spot-check of the 30 unlabelled 2018 announcements | Requires a human to read the original announcement text and judge whether "no channel wording" is a documentation-format quirk rather than a genuine channel omission | Medium |
| **P9** | Whether to submit this paper alone or alongside a companion paper (Proposal A) | If both are submitted around the same time, the cover letter must disclose the companion relationship to avoid a salami-slicing concern; current cover letter does not mention a companion paper | Medium |
| **P10** | Whether to fall back to Rice Science if both JIA and CAER reject the paper | Only the author team can authorise this trade-off if triggered; the paper's Winall strand is now confined to channel-choice/quality-positioning evidence, not company financials, so this no longer conflicts with the no-financial-narrative constraint | Low (only relevant if triggered) |
| **P11** | ~~Labelling of imputed vs. directly observed values in the Winall/comparator financial panel~~ | **Closed in v3**: the financial panel (former Supplementary Table S1) has been removed from the submission package entirely | Closed |
| **P12** | JIA's APC now reported as US$1,800 from 2026, conflicting with earlier "no OA fee" reports | Budget/cost-structure decision only the author team (or their institution) can make | Medium-high |

## Summary

- **Figure/table compression (the task this package was built to resolve): CLOSED.** Main
  text is at exactly 6 figures / 5 tables; see `manuscript/figure_table_list.md` for the
  decision record and `submission/supplementary_material.md` for the moved content.
- **Manuscript rebuild: DONE.** `submission/manuscript.docx` and `submission/manuscript.pdf`
  regenerated successfully from `manuscript/manuscript_v4.md`, the version with all
  Winall financial/business content removed (see `manuscript/review/change_log_v2_to_v3.md`).
- **Everything under "author action required" above is a genuine gap that only the human
  author team, an institutional account, or a live network connection to MARA/the journal's
  own site can close** — none of it was skipped by oversight; each is cross-referenced to the
  specific plan document or review report that first raised it.
