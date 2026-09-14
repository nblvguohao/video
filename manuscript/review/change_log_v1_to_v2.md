# Change log — manuscript_v1.md → manuscript_v2.md

Scope: implements the revision brief built from `review/R1_technical.md`,
`review/R2_novelty.md`, `review/R3_readability.md`, `review/format_check.md`,
`review/number_consistency.md`, and `review/reference_check.md`. Organised by the
brief's ten numbered issues (A1–A3, B4–B7, C8–C10), each as
**Review comment → Location changed → What was actually changed**. No declared
Non-claim, conflicting-evidence item (CF1–CF8), or robustness failure (R7/R9/R11/R13/R15)
was removed; only prose length was reduced.

---

## A. Factual number errors (highest priority)

### A1 — Winall 2026 penalty: 300,000 CNY → 3,000,000 CNY (number_consistency.md §4)
- **Comment**: `manuscript_v1.md` §7 stated the 2026 regulatory fine as "300,000 CNY," a
  10× error against every primary and planning source (`evidence/05_industry_policy.md`,
  `table_negative_facts_timeline.csv`, `results_notes_mechanism.md`), which all give
  RMB 3 million (3,000,000 CNY).
- **Location**: Section 7 (Mechanism), the paragraph reporting Winall's 2025–2026
  financial facts.
- **Change**: "fined 300,000 CNY" → "fined 3,000,000 CNY (RMB 3 million)". The
  "10.86% of disclosed profit" figure and all other numbers in that sentence were left
  unchanged, since number_consistency.md confirmed those were already correct.

### A2 — Enterprise-vs-public-institution coefficients (Non-claim 8/9 and §7) corrected to the actual Table 7 regression output
- **Comment**: R1/number_consistency.md found that §4.7 and §7 both used a planning-stage
  placeholder (+3.18 kg/mu p=0.035; +0.96 g p=0.025; n=632) instead of the numbers in
  `tables/table7_enterprise_vs_public.csv`, the file the manuscript itself cites as Table 7's
  source (+4.179 kg/mu p=0.027 n=408; +1.193 g p=0.003 n=411; chalkiness +1.010 p=0.100
  n=411; head-rice −1.220 p=0.070 n=411).
- **Location**: §4.7 non-claim on enterprise vs. public institutions (now item 9 in the
  renumbered list), and §7's descriptive paragraph on the enterprise/institute trait division
  of labour.
- **Change**: Replaced all four coefficients, SEs, p-values and n's in both places with the
  values actually in `table7_enterprise_vs_public.csv` (verified independently by re-reading
  the CSV; see numbers above). §4.7's version was also trimmed to a boundary statement with a
  pointer to Table 7/§7 rather than repeating full numbers in both places (see C9 below).
  **We did not fabricate or reverse-engineer n = 632.** Instead we added a sentence in §7
  stating plainly that an earlier planning note anticipated n = 632, the actual regression run
  on `analysis_rice_channel.pkl` returns n = 408–411, and the exact filter behind the n = 632
  figure could not be reconstructed from the materials available — flagged as an item for the
  author team to verify before submission, per the task instruction not to hide or paper over
  this discrepancy.
- Also updated `figure_table_list.md`'s Table 7 row to say n = 408–411 instead of n = 632, for
  consistency with the corrected manuscript.

### A3 — kg/mu → kg/hm² conversion added at first occurrence
- **Comment**: format_check.md item 23: format spec requires a kg/hm² conversion bracketed
  at the first mention of kg/mu; none existed anywhere in v1.
- **Location**: Results §5.2, first sentence mentioning "kg/mu" ("Raw two-year trial yield in
  kg/mu...").
- **Change**: Added "(1 kg/mu ≈ 15 kg/hm²; 1 亩 = 1/15 hm²)" immediately after the first
  occurrence.

---

## B. Missing content

### B4 — Seven mandatory citations added with substantive engagement (not bare reference-list entries)
- **Comment**: R2/reference_check.md/format_check.md found ten format-spec-mandatory
  references verified as real (`references_verified.md`) but never cited anywhere in
  `manuscript_v1.md`.
- **Changes made** (all in `manuscript_v2.md`, with full reference-list entries added in
  alphabetical, JIA author-date format):
  1. **Xie et al. (2023)** — added in §7 (Mechanism), at the point Winall is introduced,
     explicitly distinguishing Xie et al.'s firm-level contract-design game theory from this
     paper's variety-level evidence, **and** repairing the data-provenance gap
     reference_check.md flagged as highest priority: Table 6's 2018/2021 order-grain
     revenue-share and gross-margin figures are sourced from Xie et al. (2023) per
     `tables/table6_company_panel.csv`'s own note field, and this is now stated explicitly in
     the text rather than left untraceable.
  2. **Lu et al. (2024)** and **Hang et al. (2024)** — added in two places: (a) a new
     paragraph in the Introduction (after the Xiang/Zhao paragraph) distinguishing this
     paper's channel-conditional design from their calendar-year trend readings of the same
     underlying approval-record corpus; (b) a new sentence in Results §5.6 relating the
     paper's break-year estimates (head-rice 2015, chalkiness 2009) to their trend-series
     windows, and a new sentence in Discussion §8.2 relating the "closing window" finding to
     their year-indexed trend evidence.
  3. **Gong et al. (2026)** — added as a title-level-only citation in the same new
     Introduction paragraph ("a recent title-level review of fifty years of three-line hybrid
     rice trends"), with no specific figures attributed, per `references_verified.md`'s
     explicit caveat that the full text remains unobtainable.
  4. **Shi and Hu (2017)**, **Qiu et al. (2016)**, **Huang et al. (2018)** — added as a new
     paragraph at the end of the Introduction establishing JIA scope-fit, one clause each.
     **Qiu et al. (2016)** is additionally engaged with substantively in Discussion §8.1,
     connecting its information-asymmetry framework (farmer seed choice) to this paper's own
     "who measures what" argument (variety approval), as reference_check.md recommended as
     the theoretically closest paper.
- **Seck et al. (2023), Burris et al. (2025), Rangnekar (2000) — deliberately NOT inserted.**
  We reviewed every candidate location (Discussion §8.1's self-certification literature,
  Introduction, the chained-check genetic-gain robustness check §6.5) and found no paragraph
  in the current manuscript that discusses realised genetic-gain magnitudes or public/private
  breeding-sector divergence as its own topic — §6.5 already cites Piepho et al. (2014),
  Laidig et al. (2014), Mackay et al. (2011) and Raymond et al. (2023) for that specific
  robustness check, and adding three more citations to the same sentence without a distinct
  point to make would be exactly the "citation padding" R2 warned against. Per the task's own
  instruction ("如果手稿里根本没有合适的段落容纳它们，就不要生硬插入...在 change_log 里明确说明"),
  we record this as a deliberate decision, not an oversight: **these three references remain
  outside `manuscript_v2.md`'s citation list**, and the author team should either write a new
  paragraph for them (e.g., in Discussion, contrasting global genetic-gain rates with this
  paper's chained-check exercise) or formally drop them from the format spec's mandatory list
  before submission.
- All seven cited references added to the References list in alphabetical order with JIA
  author-date formatting (surname, initials; journal in full; volume/pages where available).
  Piepho and Laidig (2024)'s volume/page uncertainty was left as-is per
  `references_verified.md`'s own "do not conclude" recommendation — outside this revision's
  scope.

### B5 — Table 2 (descriptive statistics and balance) built from the actual data
- **Comment**: R1/format_check.md: `tables/table2_descriptive_balance.md` was an explicit
  placeholder ("not yet rendered... this placeholder exists so the Data section can cite
  'Table 2' without asserting numbers not yet computed"), while §3.3 and
  `figure_table_list.md` both cited it as a completed table.
- **What was built**: `scripts/analysis/build_table2_descriptive.py` reads
  `evidence/data/analysis_rice_channel.pkl`, reproduces the exact main-stratum filter used by
  `scripts/analysis/estimate_channel_gap.py` (national approvals, two dominant indica trial
  groups, 2017 and 2019–2022), and computes mean, SD and non-missing % for **all 17** outcome
  variables used in Table 3, by arm (Unified/Consortium/Green) — not only the 6-variable
  minimum the brief allowed as a fallback. Verified sample sizes match Table 3/§5.1 exactly
  (Unified 406, Consortium 405, Green 67, n = 878).
- **Output**: `manuscript/tables/table2_descriptive_balance.md` was overwritten with the
  rendered table (means/SDs/% non-missing, 17 rows × 3 arms), replacing the placeholder text.
  §3.3's citation of "Table 2" in `manuscript_v2.md` needed no wording change since it already
  described the table's intended content correctly; it now points to a real table.

### B6 — `quality_stated` forward-reference resolved by actually running the promised check (R16)
- **Comment**: R1 found that §3.3 promised "we show in §6 that the coefficient survives, and
  in fact strengthens, once announcement text length and the count of non-missing fields are
  controlled for," but no such check existed anywhere in Section 6.
- **What was built**: `scripts/analysis/robustness_quality_stated_controls.py` re-estimates
  the Arm-1 `quality_stated` specification with `source_text_len` and a constructed
  `n_nonmissing_fields` (count of non-missing values among the other 16 outcome variables)
  added as controls, on the identical n = 750 sample and cluster structure as the baseline.
  **Real result**: baseline β = −0.122 (p = 0.0075) → with controls β = −0.146 (p = 0.0005).
  The coefficient does survive and strengthen, confirming the direction of the original
  promise, but the specific magnitude (−0.146) differs from an earlier planning-stage figure
  of −0.169/p=0.0001; we report the number the check actually produces, not the older figure,
  and say so explicitly.
- **Manuscript changes**: added new subsection **§6.6 "`quality_stated` under
  disclosure-behaviour controls (R16)"** reporting this check in full, and updated §3.3's
  forward reference to point to "§6 (R16)" specifically. We chose to run and report the check
  (option (a) in the brief) rather than delete the promissory sentence, since the check turned
  out to be straightforward to run on the existing pipeline and the result is informative
  (rules out "shorter announcements just say less" as the sole driver of the stated-grade gap).

### B7 — Fig. 4's undiscussed growth-duration curve
- **Comment**: R3/format_check.md: Fig. 4 (breakpoint scan) plots a growth-duration series
  that §5.6's text never mentions, leaving a reader unable to interpret it from the figure
  alone.
- **Investigation**: no figure-generation script for `fig4_breakpoint_scan.png` could be
  located anywhere in `scripts/` (checked `scripts/analysis/make_figures.py` and a repo-wide
  search); regenerating the figure without that script risked introducing a new, unverified
  rendering rather than editing an existing one, so per the task's own fallback instruction we
  chose the text-based fix instead of touching the image.
- **Change**: Results §5.6 now includes a new sentence, using the real number from
  `tables/table_breakpoint_scan_full.csv` (duration_d's Wald statistic peaks at 2018, Wald =
  226.8, p < 10⁻⁴⁹, n = 1,196), stating explicitly that growth duration is plotted only as
  background context and is not part of the paper's formal structural-break argument, since it
  is not one of the third-party-assayed quality traits that section is built to speak to.

---

## C. Length compression (target 8,000–10,000 words; retain all Non-claims/CF/robustness-failure content)

**Honest result reported, not overstated**: `manuscript_v2.md` is 14,488 words total
(13,959 excluding the References list), versus `manuscript_v1.md`'s 14,691 words — a net
reduction of only about 200 words. This falls well short of the 8,000–10,000-word target.
The reasons and the real compression work done are recorded here rather than glossed over:

- **Real compression achieved**: Section 6 (Robustness) was restructured from fifteen
  full-prose subsections (~2,850 words) to a two-tier structure — a single consolidated
  subsection (§6.1) presenting R1–R6, R8, R10, R12–R14 as one-paragraph-per-check bullets
  (check → result → conclusion, pointing to Table 3/Table 4 rather than re-quoting full
  CI/p/n triples), plus full prose retained only for the genuinely qualifying/complicating
  checks (R7, R9, R11, R15) and the new R16 — cutting roughly 900 words net even after adding
  R16's new content. Section 4.7 (Non-claims) was compressed from eleven multi-sentence
  numbered paragraphs (~1,050 words) to a twelve-item bolded list of boundary statement +
  one-clause reason (~350 words), moving full numeric detail to each claim's home section
  (Table 7/§7 for the enterprise-institute comparison, §6.4 for the provincial-replication
  discrepancy) rather than repeating it in both places — this also fixed a pre-existing
  cross-reference error (§8.2's "Non-claim 8" pointed to the wrong item under the old
  numbering; it is now correct under the new list). Section 4.1 (rejected DID designs) and
  Discussion §8.1 (self-certification literature) were each tightened by roughly 150–200
  words without cutting any cited number or comparison.
- **Why the net reduction is small**: the seven newly required citations (B4) added
  substantial new prose — a full new Introduction paragraph, a new JIA scope-fit paragraph,
  new sentences in §5.6, §7, §8.1 and §8.2 — by design, since the task required "有实质对话内容
  的句子," not bare citations. This new content (roughly 500–600 words) largely offset the
  robustness/non-claims cuts. The corrected Table 7/Non-claim 8 discussion (A2) also added an
  explicit disclosure paragraph about the n=632 discrepancy that did not exist in v1.
  De-duplicating the headline-coefficient triad (C10) was applied only where a repetition was
  genuinely redundant (the Robustness section); it was **not** applied to §4.5 (Empirical
  strategy), because §4.5 states the sign-separation identification argument *before* Results
  is reached in reading order — R2 specifically praised this early statement as good practice,
  and cutting it to "see Table 3" there would remove the paper's stated identification logic
  from its own methods section, which the brief's "do not cut the sign-separation argument"
  instruction (C.5 "Do not cut" list, R3) forbids.
- **What we did not attempt**: further compression to reach the 8,000–10,000 word target would
  require either (a) cutting into the Results section's first full statement of headline
  coefficients (explicitly protected — this is the "home section" the de-duplication is
  supposed to point *to*, not cut), or (b) removing declared robustness detail for R7/R9/R11/R15
  (explicitly forbidden), or (c) shortening the Data/Institutional-background sections enough
  to risk losing the provenance and definitional detail that R1 and format_check.md separately
  praised as a strength. We judged that reaching the numeric target this revision cycle would
  require the author team's explicit sign-off on which substantive detail to cut (not just
  restate more tersely), and flag this as unresolved rather than force it silently. A
  second compression pass focused on the Data (§3) and Institutional Background (§2) sections,
  or a decision to move some robustness/mechanism detail to Supplementary Material, is the
  most direct path to closing the remaining gap.

---

## Other consistency fixes made in passing (not separately requested, but required by
## "must not reintroduce inconsistency")

- Fixed a pre-existing internal inconsistency in v1: the old Non-claim 7 (provincial
  replication) quoted a stale figure (β = −0.134, p = 0.93) that matched neither the actual
  provincial-replication run reported in §6.4/§8.2 (β = −3.354, p = 0.53, n = 280) nor the
  number needed for internal consistency. The compressed Non-claim list (item 8) now points to
  §6.4 for the current numbers instead of repeating the stale figure, and §6.4 already
  discloses the −0.134/n=452 discrepancy as an explicitly unreconciled planning-note artifact
  (unchanged from v1, since this was already correctly self-disclosed there).
- Renumbered every internal `Section 6.x` cross-reference in the text (e.g. "Section 6.6" for
  Manski bounds, "Section 6.9" for R10, "Section 6.10" for the within-applicant test,
  "Section 6.8" for the placebo-trait discussion) to match the new §6.1–6.7 structure.
- Updated `figure_table_list.md`'s Table 4/Fig. 5/Fig. 6 "first cited in" column references
  from the old §6.5/§6.6–6.7/§6.15 labels to the new §6.1/§6.1–6.2/§6.7 labels, and its Table 7
  description to reflect the corrected n.

## Scripts produced

- `/home/user/video/scripts/analysis/build_table2_descriptive.py` — builds Table 2 from
  `analysis_rice_channel.pkl` (see B5).
- `/home/user/video/scripts/analysis/robustness_quality_stated_controls.py` — runs the R16
  disclosure-behaviour-controls check (see B6).
