# Figure and table list — manuscript_v5.md

> Current as of v5 (2026-09-16). Supersedes the v3 version of this document. Main text holds
> **6 figures and 5 tables**, meeting the journal target; everything else is Supplementary.
>
> Two structural changes since v3 affect this list. In v4→v5 the paper was de-identified: no
> analysis is now conducted at the level of a named organisation, so the former firm-level
> mechanism figure and positioning table were replaced by a germplasm-concentration figure and
> table built from parental-line entity resolution. Separately, §5.4 was deleted as a
> restatement of §4.5, so sections after it renumber (old 5.5→5.4, 5.6→5.5, 5.7→5.6).

## Figures (main text — 6 of 6)

| # | Content | Source file | First cited |
|---|---|---|---|
| Fig. 1 | 2005–2022 national rice approvals by trial channel, stacked area, with markers for the 2014 green channel, 2016 Measures, 2021 standard revision, 2022 EDV provision and 2022 special-rectification notice | `figures/fig1_channel_stacked.png` | §3.1 |
| Fig. 2 | Main forest plot: β and 95% CI for all 17 outcomes, both arms, colour-coded by measuring party | `figures/fig2_forest_main.png` / `.pdf` | §5.1 |
| Fig. 3 | Year-by-year channel gap for head-rice, chalkiness, stated grade and regional-trial yield gain | `figures/fig3_event_study.png` | §5.4 |
| Fig. 4 | sup-Wald unknown-breakpoint scan, Wald statistic by candidate break year, one line per trait | `figures/fig4_breakpoint_scan.png` | §5.5 |
| Fig. 5 | Randomisation-inference null distributions (500 permutations) vs observed coefficient, four panels | `figures/fig6_randomization.png` / `.pdf` | §6.1 (R6) |
| Fig. 6 | **Germplasm concentration by trial channel**, two panels: (a) concentration curves over sterile lines; (b) sterile-line HHI with 95% bootstrap intervals | `figures/fig6_germplasm_concentration.png` / `.pdf` | §7 |

Fig. 5 and Fig. 6 keep rendered-file names from earlier working numbering; the published
number is the one in column 1. Fig. 6b draws its interval as a standalone segment because a
percentile bootstrap interval for the HHI need not bracket the point estimate.

## Tables (main text — 5 of 5)

| # | Content | Source file | First cited |
|---|---|---|---|
| Table 1 | Year-by-year approval counts by trial channel, national two-trial-group stratum | `tables/table1_channel_by_year.csv` | §3.1 |
| Table 2 | Descriptive statistics and balance: means, SDs, missing rates by arm | `tables/table2_descriptive_balance.md` | §3.3 |
| Table 3 | Main regression results: both arms × 17 outcomes × β / 95% CI / p / BH-q, blocked by measuring party | `tables/table3_main_results.csv` | §3.3; reported in §5.2–5.3 |
| Table 4 | Robustness matrix, R1–R17 | compiled from the robustness outputs and §6 point estimates | §6.7 |
| Table 5 | **Germplasm concentration across resolved parental lines**, by channel and arm, with bootstrap CI and permutation test | `tables/table5_germplasm_concentration.md`, `tables/table_germplasm_concentration.csv` | §7 |

## Supplementary Material

| # | Content | Source | Note |
|---|---|---|---|
| Table S1 | Descriptive trait division of labour, enterprise vs public research institution (n = 408–411) | `tables/table7_enterprise_vs_public.csv` | Descriptive only; neither quality coefficient is significant |
| Fig. S1 | Missingness-balance dumbbell plot, non-missing rate by arm for all 17 outcomes | `figures/fig7_missingness_balance.png` / `.pdf` | Content also in Table 2 and §6.1–6.2 |
| Fig. S2 | Manski worst-case bounds for the three unbalanced-missingness outcomes | not yet rendered | Not cited by number; values in §6.2 prose |
| Fig. S3 | Chained-check genetic-gain ladder (R15) with CV band | not yet rendered | Not cited by number; see Note S1 |
| Note S1 | **Chained-check genetic-gain scale (R15): construction and full diagnostics** | moved from main §6.5 in v5 | §6.5 retains the verdict and four headline diagnostics |

Fig. S2 and Fig. S3 remain unrendered. Neither is cited by number in the main text, so this
does not block submission, but both should be rendered before final upload if the journal
requires every named Supplementary figure as an image file.

## Verification note (v5)

Checked after the v5 edits: every `Fig.` and `Table` citation in the body resolves to an item
above at its final number; no stale `Table 6`, `Table 7`, `Fig. 7` or `Supplementary Table S2`
remains; figures are first cited in ascending order; no figure or table is uncited. Section
cross-references were re-checked after the §5.4 deletion, and one stale pointer — a
year-by-year reference still aimed at the breakpoint section — was found and corrected.
