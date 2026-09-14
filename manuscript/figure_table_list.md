# Figure and table list — manuscript_v1.md

> Companion to `manuscript_v1.md`. Numbering follows the content mapping fixed in
> `plan/02_research_route.md` §7, with the renumbering documented in
> `integration_log.md` §2 applied so that first-mention order in the merged manuscript
> matches ascending figure/table number, as required by `plan/04_format_spec.md` §5.
> "Source file" is the pre-existing rendered file in `manuscript/figures/` or
> `manuscript/tables/`; its own filename number reflects the *original* (pre-merge)
> numbering and does not always match the published number below — see the note column.

## Figures (main text, submission target: 6 of these 7 retained per §5; see note on Fig. 2)

| Published # | Caption (content) | Source file | First cited in | Note |
|---|---|---|---|---|
| Fig. 1 | 2005–2022 national rice approvals by trial channel, stacked area chart, with vertical markers for the 2014 green channel, 2016 Measures, 2021 standard revision, 2022 EDV provision, and 2022 special-rectification notice | `figures/fig1_channel_stacked.png` | §3.1 Data | Number unchanged from source file |
| Fig. 2 | Main forest plot: β and 95% CI for all 17 outcome variables, Arm 1 and Arm 2, colour-coded by measuring party (applicant-self-reported vs third-party-assayed) | `figures/fig2_forest_main.png` / `.pdf` | §5.1 Results | Number unchanged; this is the paper's core figure |
| Fig. 3 | Event-study-style line plot: year-by-year channel gap (new channel − Unified) for head-rice percentage, chalkiness, stated quality grade, and regional-trial yield gain | `figures/fig3_event_study.png` | §5.5 Results (Channel composition and convergence) | Number unchanged. Cited before Fig. 4 only because §5.5 and §5.6 were reordered in the merge (see `integration_log.md` §1) |
| Fig. 4 | sup-Wald unknown-breakpoint scan: Wald statistic by candidate break year, one line per trait, peak years annotated | `figures/fig4_breakpoint_scan.png` | §5.6 Results (Structural breakpoints) | Number unchanged |
| Fig. 5 | Randomisation-inference null distributions (500 permutations) vs observed coefficient, four panels (head-rice, chalkiness, regional-trial yield gain, top-two quality grade) | `figures/fig6_randomization.png` / `.pdf` | §6.5 Robustness (R6) | **Renumbered from Fig. 6 in the source filename/plan to Fig. 5** — see `integration_log.md` §2 |
| Fig. 6 | Missingness-balance dumbbell plot: non-missing rate by arm for all 17 outcomes, imbalanced variables flagged | `figures/fig7_missingness_balance.png` / `.pdf` | §6.6–6.7 Robustness (R7, R8) | **Renumbered from Fig. 7 to Fig. 6** — see `integration_log.md` §2 |
| Fig. 7 | Winall Hi-Tech mechanism, three panels: (a) Winall's national-approval share and channel-composition stack; (b) forest plot of Winall vs. other applicants' trait differences, within the unified channel and within the new channel; (c) order-grain revenue share and R&D-intensity time series, with 2025 loss and 2026 ST annotations | `figures/fig5_winall_mechanism.png` | §7 Mechanism | **Renumbered from Fig. 5 to Fig. 7** — see `integration_log.md` §2 |

## Figures held for Supplementary Material (per `04_format_spec.md` §5; not cited in the main-text body)

| Working # (per `02_research_route.md` §7) | Caption (content) | Source file | Status |
|---|---|---|---|
| Fig. 8 | Manski worst-case bounds: observed / best-case / worst-case interval bars for the four unbalanced-missingness outcomes | not yet rendered | Move to Supplementary per format spec; not cited by number in the main text (R7's prose in §6.6 reports the bound values directly) |
| Fig. 9 | Chained-check ladder (R15): back-solved check-variety yield ladder across years with CV uncertainty band | not yet rendered | Move to Supplementary per format spec; §6.14 reports the diagnostics in prose without a figure citation. **Note**: `04_format_spec.md` §5 itself labels this "Fig. 8" and the Manski plot "Fig. 9" — the reverse of `02_research_route.md` §7's numbering. This document follows `02_research_route.md` as the canonical source per the integration brief; see `integration_log.md` §3 for the discrepancy |

## Tables (main text)

| # | Caption (content) | Source file | First cited in |
|---|---|---|---|
| Table 1 | Year-by-year approval-record counts by trial channel, national two-trial-group stratum (documents the 2018 channel-label gap) | `tables/table1_channel_by_year.csv` | §3.1 Data |
| Table 2 | Descriptive statistics and balance: means, SDs and missing rates for all outcome/control variables, by arm | `tables/table2_descriptive_balance.md` | §3.3 Data |
| Table 3 | Main regression results: Arm 1 and Arm 2 × 17 outcome variables × β / 95% CI / p / BH-q, blocked by measuring party | `tables/table3_main_results.csv` | §3.3 Data (referenced); first substantively reported in §5.1–5.2 Results |
| Table 4 | Robustness matrix, R1–R15, including all checks that qualify or fail to support the headline result | (compiled from `tables/table_r10_drop_winall_robustness.csv`, `table_breakpoint_scan_full.csv`, `table_event_study_by_year.csv`, and the robustness-section point estimates in §6) | §6.15 Robustness |
| Table 5 | Winall Hi-Tech: channel composition (unified vs new-channel share) and within-channel trait-positioning coefficients | `tables/table5_winall_positioning.csv` (positioning) + `tables/table5b_winall_channel_choice_logit.csv` (channel-choice logit) | §7 Mechanism |
| Table 6 | Winall and comparator listed seed enterprises: financial/R&D panel (gross margin, net profit, R&D intensity), imputed values flagged separately | `tables/table6_company_panel.csv` | §7 Mechanism |
| Table 7 | Descriptive trait division of labour, enterprise vs. public research institution applicants (n = 632) | `tables/table7_enterprise_vs_public.csv` | §7 Mechanism |

## Submission-target compression (per `04_format_spec.md` §5)

The format spec directs compressing the working 9-figure/7-table set to 6 figures and 5 tables in the
submitted main text, moving Fig. 8 (Manski bounds) and Fig. 9 (chained-check ladder) to Supplementary.
That leaves 7 main-text figures (Fig. 1–7) above the stated 6-figure target — the spec's own arithmetic
(9 → 6 by removing only 2) does not close, and no plan document identifies which one of Fig. 1–7 would
be the seventh cut. This is flagged as an open item in `integration_log.md` §4 for the author team to
resolve before submission (candidates most defensible to fold into another panel: merging Fig. 3's
event-study lines into Fig. 2, or moving Fig. 6's missingness dumbbell plot to a table-only presentation
since its content is already fully reported in Table 2 and §6.7's prose). No table is identified in any
plan document as a candidate to move to Supplementary to reach the "5 tables" target; this is likewise
unresolved and flagged rather than decided unilaterally here.
