# Figure and table list — manuscript_v3.md (RESOLVED)

> Companion to `manuscript_v3.md`. **Status: RESOLVED (2026-09-14); updated 2026-09-16 for
> v3.** The compression question flagged as open in the v1 version of this document — 9
> working figures / 7 working tables had to be compressed to a "6 figures / 5 tables"
> main-text target, but the arithmetic did not close and no candidate cut had been chosen —
> was closed by the editorial decision below in the v2 session. In the v3 revision, the
> author team additionally required that no discussion of Winall Hi-Tech Seed's financial or
> business performance appear anywhere in the paper (see
> `manuscript/review/change_log_v2_to_v3.md`); this removed the former Supplementary Table S1
> (company financial panel) entirely and reduced Fig. 6 from three panels to two. Former
> Supplementary Table S2 is renumbered **Table S1**. No main-text figure or table numbering
> changed, since the financial panel and its panel (c) counterpart were already Supplementary/
> sub-panel material, not main-text Table/Fig. numbers.

## Editorial decision (this document's own candidate, adopted)

Two moves close the gap, both drawn from the "candidates most defensible" list this
document itself proposed in the v1 draft:

1. **Table 6** (Winall and comparator company financial panel) and **Table 7** (enterprise
   vs. public-institution descriptive comparison) are moved to Supplementary Material as
   **Supplementary Table S1** and **Supplementary Table S2** respectively. Both are
   secondary/background material relative to the paper's main channel-gap result (Table 6
   supports the Winall counter-case narrative in prose; Table 7 is explicitly flagged as
   "descriptive background only, not a causal comparison" in the main text, §4.7 Non-claim
   9). Main text retains **Table 1–5** — 5 tables, meeting the target.
2. **Fig. 6 (old)**, the missingness-balance dumbbell plot, is moved to Supplementary
   Material as **Supplementary Fig. S1**. Rationale (the reason this document itself gave in
   the v1 draft for this specific candidate): its content is already fully reported in Table
   2's missing-rate columns and in the §6.1–6.2 prose (R7, R8), so the figure is a
   visualisation of numbers the reader already has, not a source of new information. **Fig. 7
   (old)**, the Winall Hi-Tech three-panel mechanism figure, is renumbered to **Fig. 6**. Main
   text retains **Fig. 1–6** — 6 figures, meeting the target.

No other figure or table is moved, and no additional cut was needed once both moves above
are made: 9 working figures − 2 moved (old Fig. 6, old Fig. 8/9 already slated for
Supplementary — see below) = 6 main-text figures; 7 working tables − 2 moved (Table 6,
Table 7) = 5 main-text tables. The arithmetic now closes.

All in-text citations to the moved/renumbered items have been updated throughout
`manuscript_v2.md` (verified by exhaustive `grep` for every remaining "Table 6", "Table 7",
"Fig. 7" and "Fig. 6" occurrence — see `submission/VERSION_HISTORY.md` for the specific line
changes). The moved content itself, including original captions, was reproduced in
`submission/supplementary_material.md` as Table S1, Table S2 and Fig. S1.

> **Superseded by v3 (see box at the top of this document and the "Verification note (v3)"
> section below).** The v3 revision removed Table S1 (the Winall financial panel) entirely
> and renumbered Table S2 to Table S1; the description in this "Editorial decision" section
> is retained as the historical record of the v2 compression decision, not as the current
> state of the Supplementary Material.

## Figures (main text — final, 6 of 6)

| Published # | Caption (content) | Source file | First cited in | Note |
|---|---|---|---|---|
| Fig. 1 | 2005–2022 national rice approvals by trial channel, stacked area chart, with vertical markers for the 2014 green channel, 2016 Measures, 2021 standard revision, 2022 EDV provision, and 2022 special-rectification notice | `figures/fig1_channel_stacked.png` | §3.1 Data | Unchanged |
| Fig. 2 | Main forest plot: β and 95% CI for all 17 outcome variables, Arm 1 and Arm 2, colour-coded by measuring party (applicant-self-reported vs third-party-assayed) | `figures/fig2_forest_main.png` / `.pdf` | §5.1 Results | Unchanged; the paper's core figure |
| Fig. 3 | Event-study-style line plot: year-by-year channel gap (new channel − Unified) for head-rice percentage, chalkiness, stated quality grade, and regional-trial yield gain | `figures/fig3_event_study.png` | §5.5 Results (Channel composition and convergence) | Unchanged |
| Fig. 4 | sup-Wald unknown-breakpoint scan: Wald statistic by candidate break year, one line per trait, peak years annotated | `figures/fig4_breakpoint_scan.png` | §5.6 Results (Structural breakpoints) | Unchanged |
| Fig. 5 | Randomisation-inference null distributions (500 permutations) vs observed coefficient, four panels (head-rice, chalkiness, regional-trial yield gain, top-two quality grade) | `figures/fig6_randomization.png` / `.pdf` | §6.1 Robustness (R6) | Unchanged from v1 numbering |
| Fig. 6 | Winall Hi-Tech mechanism, two panels: (a) Winall's national-approval share and channel-composition stack; (b) forest plot of Winall vs. other applicants' trait differences, within the unified channel and within the new channel | `figures/fig5_winall_mechanism.png` | §7 Mechanism | Renumbered from Fig. 7 to Fig. 6 in the v2 session; **in v3, the former panel (c) — order-grain revenue share/R&D-intensity time series with 2025 loss and 2026 ST annotations — was removed at author request (financial/business content), leaving a two-panel figure** (see `manuscript/review/change_log_v2_to_v3.md`) |

## Tables (main text — final, 5 of 5)

| # | Caption (content) | Source file | First cited in |
|---|---|---|---|
| Table 1 | Year-by-year approval-record counts by trial channel, national two-trial-group stratum (documents the 2018 channel-label gap) | `tables/table1_channel_by_year.csv` | §3.1 Data |
| Table 2 | Descriptive statistics and balance: means, SDs and missing rates for all outcome/control variables, by arm | `tables/table2_descriptive_balance.md` | §3.3 Data |
| Table 3 | Main regression results: Arm 1 and Arm 2 × 17 outcome variables × β / 95% CI / p / BH-q, blocked by measuring party | `tables/table3_main_results.csv` | §3.3 Data (referenced); first substantively reported in §5.1–5.2 Results |
| Table 4 | Robustness matrix, R1–R16, including all checks that qualify or fail to support the headline result | (compiled from `tables/table_r10_drop_winall_robustness.csv`, `table_breakpoint_scan_full.csv`, `table_event_study_by_year.csv`, and the robustness-section point estimates in §6) | §6.7 Robustness |
| Table 5 | Winall Hi-Tech: channel composition (unified vs new-channel share) and within-channel trait-positioning coefficients | `tables/table5_winall_positioning.csv` (positioning) + `tables/table5b_winall_channel_choice_logit.csv` (channel-choice logit) | §7 Mechanism |

## Supplementary Material (final)

| # | Caption (content) | Source file | Formerly | Reason for moving / removing |
|---|---|---|---|---|
| ~~Table S1~~ | ~~Winall and comparator listed seed enterprises: financial/R&D panel~~ | ~~`tables/table6_company_panel.csv`~~ | Table 6 | **Removed entirely in v3.** The paper's financial/business narrative about Winall was removed at author request (no negative-information constraint); with that narrative gone, this table had no remaining independent purpose and is not retained in any edited/positive-only form (see `manuscript/review/change_log_v2_to_v3.md`). |
| Table S1 | Descriptive trait division of labour, enterprise vs. public research institution applicants (n = 408-411, see `change_log_v1_to_v2.md` for the n=632 planning-note discrepancy) | `tables/table7_enterprise_vs_public.csv` | Table 7 (v2: Table S2) | Explicitly descriptive-only per main text §4.7 Non-claim 9; not a causal or headline comparison. **Renumbered from S2 to S1 in v3** once the former S1 was removed. |
| Fig. S1 | Missingness-balance dumbbell plot: non-missing rate by arm for all 17 outcomes, imbalanced variables flagged | `figures/fig7_missingness_balance.png` / `.pdf` | Fig. 6 (old) | Content is fully reported in Table 2 and §6.1–6.2 prose (R7, R8); the figure adds visualisation, not new information |
| Fig. S2 | Manski worst-case bounds: observed / best-case / worst-case interval bars for the four unbalanced-missingness outcomes | not yet rendered | Working Fig. 8 (`02_research_route.md` §7) | Not cited by number in the main text; §6.2 (R7) reports the bound values directly in prose |
| Fig. S3 | Chained-check ladder (R15): back-solved check-variety yield ladder across years with CV uncertainty band | not yet rendered | Working Fig. 9 (`02_research_route.md` §7) | Not cited by number in the main text; §6.5 (R15) reports the diagnostics in prose without a figure citation |

Fig. S2 and Fig. S3 were already slated for Supplementary in the v1 draft of this document
and required no renumbering decision — only Table 6/7 and the old Fig. 6/7 pair were
contested in v2, and the v2 Table S1 removal / S2→S1 renumbering in v3. Both Fig. S2/S3
remain unrendered; rendering them is not required for the compression question to be
resolved, since neither is cited by number in the main text, but the author team should
render them before final Supplementary Material submission if the journal expects
Supplementary figures to be provided as image files rather than described in prose (see
`submission/submission_checklist.md`).

## Verification note (v2)

Every remaining occurrence of "Table 6", "Table 7", "Fig. 6" and "Fig. 7" in
`manuscript_v2.md` was checked by hand against its surrounding paragraph before being edited
or left alone, because "Fig. 6" carried two distinct referents in the pre-edit manuscript
(the missingness-balance plot, cited in §6.1–6.2, and — after this session's renumbering —
the Winall mechanism figure, cited in §7). No stale numeric reference to the old numbering
remains; confirmed by `grep -n "Table 6\|Table 7\|Fig\. 7"` returning no main-text hits after
the edit (one internal cross-reference in §7 to the pre-submission working-draft table
number is retained deliberately, spelled out as "Supplementary Table S2 (Table 7 in the
pre-submission working draft)", to keep the discrepancy note in that paragraph traceable).

## Verification note (v3)

The v3 revision removed all Winall financial/business-performance content: the §7 paragraph
reporting order-grain gross margin, 2025 net profit/loss, the 2024 qualified audit opinion,
the 2026 fine and ST status change, and the China Seed Group tender offer was deleted in
full; the former Supplementary Table S1 (`tables/table6_company_panel.csv`) was removed from
`submission/supplementary_material.md`; and Fig. 6's former panel (c), which plotted
order-grain revenue share/R&D intensity with the 2025 loss and 2026 ST annotations, was
removed from `manuscript/scripts/fig5_mechanism.py` and the figure re-rendered as a two-panel
image. Every remaining "Supplementary Table S2" reference in `manuscript_v3.md` was updated
to "Supplementary Table S1" (2 occurrences, both in §7). Confirmed by
`grep -n "Winall" manuscript/figure_table_list.md manuscript/manuscript_v3.md
submission/supplementary_material.md` and by the full-text negative-information grep recorded
in `manuscript/review/change_log_v2_to_v3.md`.
