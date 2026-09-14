# Tables

**Manuscript:** "Who measures what enters the market? Self-organised variety trials and the
third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"

> Final main-text numbering (5 tables), per `manuscript/figure_table_list.md`. Provided as a
> standalone file in case the target journal requires tables submitted separately from the
> manuscript body. Source data files are listed for each; Supplementary Tables S1–S2 are in
> `submission/supplementary_material.md`.

---

## Table 1. Year-by-year approval-record counts by trial channel

Caption: Year-by-year approval-record counts by trial channel, national two-trial-group
stratum (documents the 2018 channel-label gap). First cited in §3.1.
*Source: `manuscript/tables/table1_channel_by_year.csv`.*

| Approval year | Unified | Green | Consortium | Total | Note |
|---|---|---|---|---|---|
| 2005 | 59 | 0 | 0 | 59 | |
| 2006 | 83 | 0 | 0 | 83 | |
| 2007 | 52 | 0 | 0 | 52 | |
| 2008 | 20 | 0 | 0 | 20 | |
| 2009 | 51 | 0 | 0 | 51 | |
| 2010 | 55 | 0 | 0 | 55 | |
| 2011 | 29 | 0 | 0 | 29 | |
| 2012 | 44 | 0 | 0 | 44 | |
| 2013 | 43 | 0 | 0 | 43 | |
| 2014 | 46 | 0 | 0 | 46 | |
| 2015 | 53 | 0 | 0 | 53 | |
| 2016 | 66 | 0 | 0 | 66 | |
| 2017 | 87 | 88 | 0 | 175 | |
| 2018 | 233 | 1 | 0 | 234 | Of 234 national records, 233 (99.6%) do not carry "green channel/self-organised trial" or "consortium" text and are coded Unified by parsing default, not a genuine channel determination (see §3.1; robustness check R4) |
| 2019 | 135 | 0 | 88 | 223 | |
| 2020 | 164 | 0 | 142 | 306 | |
| 2021 | 182 | 0 | 249 | 431 | |
| 2022 | 55 | 0 | 77 | 132 | |

---

## Table 2. Descriptive statistics and balance, main analysis stratum

Caption: Descriptive statistics and balance — means, standard deviations, and missing rates —
for all outcome and control variables reported as regression outcomes in Table 3, by arm.
Sample: national approvals, two dominant mid-season indica trial groups, 2017 and 2019–2022,
n = 878 (Unified 406 / Consortium 405 / Green 67). First cited in §3.3.
*Source: `manuscript/tables/table2_descriptive_balance.md`.*

| Outcome | Unified mean (SD) | Consortium mean (SD) | Green mean (SD) | Unified % non-missing | Consortium % non-missing | Green % non-missing |
|---|---|---|---|---|---|---|
| Head-rice percentage (%) | 63.130 (4.956) | 61.690 (5.577) | 60.989 (4.187) | 98.8 | 99.3 | 91.0 |
| Chalkiness degree (%) | 2.211 (1.925) | 3.246 (3.022) | 5.521 (3.334) | 98.8 | 98.3 | 97.0 |
| Quality grade stated (0/1) | 0.874 (0.332) | 0.770 (0.421) | 0.463 (0.502) | 100.0 | 100.0 | 100.0 |
| Top-two quality grade (0/1) | 0.665 (0.473) | 0.635 (0.482) | 0.290 (0.461) | 87.4 | 77.0 | 46.3 |
| Amylose content (%) | 16.250 (2.054) | 16.120 (2.186) | 15.798 (2.486) | 97.8 | 95.8 | 97.0 |
| Gel consistency (mm) | 72.181 (8.561) | 69.095 (9.823) | 71.264 (12.493) | 97.5 | 97.0 | 100.0 |
| Grain length-width ratio | 3.212 (0.304) | 3.274 (0.356) | 3.112 (0.146) | 98.8 | 98.5 | 100.0 |
| Neck-blast tolerance OK (0/1) | 0.625 (0.485) | 0.608 (0.489) | -- | 82.8 | 94.6 | 0.0 |
| Bacterial-blight grade | 6.307 (1.379) | 6.057 (1.520) | 5.653 (1.751) | 69.7 | 69.6 | 73.1 |
| Regional-trial yield gain over check (pp) | 4.182 (2.443) | 4.646 (1.848) | 4.439 (1.971) | 77.1 | 99.8 | 40.3 |
| Production-trial yield gain over check (pp) | 4.462 (2.127) | 5.031 (2.089) | 5.075 (2.961) | 82.3 | 75.1 | 100.0 |
| Two-year regional-trial yield (kg/mu) | 645.771 (23.299) | 645.573 (20.065) | 657.860 (24.328) | 91.6 | 100.0 | 100.0 |
| Growth duration (days) | 140.554 (9.312) | 139.696 (9.465) | 141.166 (7.484) | 99.0 | 99.3 | 100.0 |
| Plant height (cm) | 117.693 (6.602) | 118.620 (6.675) | 118.793 (6.389) | 99.0 | 99.3 | 100.0 |
| Seed-setting percentage (%) | 83.883 (2.708) | 84.125 (2.991) | 84.319 (2.087) | 98.8 | 99.3 | 100.0 |
| Thousand-grain weight (g) | 25.591 (2.161) | 25.665 (2.264) | 26.961 (2.434) | 99.0 | 99.3 | 100.0 |
| Grains per panicle | 203.873 (18.950) | 198.817 (18.139) | 197.985 (16.714) | 96.6 | 97.3 | 98.5 |

Notes: `quality_stated`, `neck_blast_ok` and `quality_top2` are 0/1 indicators; their "mean" is
the proportion coded 1. `quality_stated` is non-missing by construction in every arm (§3.3).
Non-missing-rate imbalances of 8 percentage points or more between Unified and Consortium
(`quality_top2`, `yield_gain_pct`, `yield_2yr_kg_mu`) are the same three that motivate the
Manski worst-case bounds reported in §6.2 (R7) and shown in Supplementary Fig. S1.

---

## Table 3. Main regression results

Caption: Main regression results: Arm 1 (Consortium vs. Unified) and Arm 2 (Green vs.
Unified) × 17 outcome variables × β / 95% CI / p / Benjamini–Hochberg q, blocked by measuring
party. First cited in §3.3 (referenced); reported substantively in §5.1–5.2.
*Source: `manuscript/tables/table3_main_results.csv`.*

### Arm 1: Consortium vs. Unified (2019–2022), cluster(cell), G = 10

| Outcome | Party | n | β | SE | 95% CI | p | BH-q |
|---|---|---|---|---|---|---|---|
| Head-rice percentage (%) | 3rd-party | 742 | −1.844 | 0.404 | [−2.636, −1.052] | 5.1×10⁻⁶ | 8.6×10⁻⁵ |
| Chalkiness degree (%) | 3rd-party | 739 | +1.108 | 0.439 | [0.248, 1.969] | 0.0116 | 0.0329 |
| Quality grade stated (0/1) | 3rd-party | 750 | −0.122 | 0.046 | [−0.211, −0.033] | 0.0075 | 0.0293 |
| Top-two quality grade (0/1) | 3rd-party | 618 | −0.091 | 0.035 | [−0.159, −0.023] | 0.0086 | 0.0293 |
| Amylose content (%) | 3rd-party | 724 | −0.118 | 0.170 | [−0.451, 0.214] | 0.485 | 0.589 |
| Gel consistency (mm) | 3rd-party | 728 | −1.814 | 0.748 | [−3.281, −0.347] | 0.0154 | 0.0373 |
| Grain length–width ratio | 3rd-party | 739 | +0.039 | 0.042 | [−0.044, 0.122] | 0.359 | 0.508 |
| Neck-blast tolerance OK (0/1) | 3rd-party | 710 | −0.034 | 0.031 | [−0.095, 0.027] | 0.277 | 0.429 |
| Bacterial-blight grade | 3rd-party | 520 | −0.190 | 0.045 | [−0.278, −0.102] | 2.1×10⁻⁵ | 1.2×10⁻⁴ |
| Regional-trial yield gain over check (pp) | self-reported | 708 | +0.553 | 0.236 | [0.091, 1.016] | 0.0189 | 0.0402 |
| Production-trial yield gain over check (pp) | self-reported | 578 | +0.919 | 0.211 | [0.505, 1.333] | 1.3×10⁻⁵ | 1.1×10⁻⁴ |
| Two-year regional-trial yield (kg/mu) | self-reported | 716 | +1.425 | 2.814 | [−4.089, 6.940] | 0.612 | 0.651 |
| Growth duration (days) | self-reported | 743 | −0.083 | 0.301 | [−0.673, 0.506] | 0.782 | 0.782 |
| Plant height (cm) | self-reported | 743 | +0.952 | 0.473 | [0.025, 1.880] | 0.0442 | 0.0752 |
| Seed-setting percentage (%) | self-reported | 742 | −0.202 | 0.256 | [−0.704, 0.299] | 0.429 | 0.561 |
| Thousand-grain weight (g) | self-reported | 743 | +0.138 | 0.257 | [−0.366, 0.642] | 0.591 | 0.651 |
| Grains per panicle | self-reported | 726 | −5.355 | 2.391 | [−10.041, −0.670] | 0.0251 | 0.0474 |

### Arm 2: Green vs. Unified (2017), HC1 (2 cells)

| Outcome | Party | n | β | SE | 95% CI | p | BH-q |
|---|---|---|---|---|---|---|---|
| Head-rice percentage (%) | 3rd-party | 106 | −0.391 | 0.656 | [−1.676, 0.894] | 0.551 | 0.551 |
| Chalkiness degree (%) | 3rd-party | 110 | +2.809 | 0.477 | [1.874, 3.744] | 3.9×10⁻⁹ | 2.1×10⁻⁸ |
| Quality grade stated (0/1) | 3rd-party | 112 | −0.344 | 0.079 | [−0.499, −0.189] | 1.3×10⁻⁵ | 5.3×10⁻⁵ |
| Top-two quality grade (0/1) | 3rd-party | 70 | −0.269 | 0.111 | [−0.486, −0.052] | 0.0151 | 0.0302 |
| Amylose content (%) | 3rd-party | 110 | −1.520 | 0.459 | [−2.420, −0.621] | 9.2×10⁻⁴ | 2.5×10⁻³ |
| Gel consistency (mm) | 3rd-party | 112 | −6.558 | 1.810 | [−10.105, −3.012] | 2.9×10⁻⁴ | 9.3×10⁻⁴ |
| Grain length–width ratio | 3rd-party | 112 | +0.046 | 0.025 | [−0.003, 0.095] | 0.066 | 0.088 |
| Neck-blast tolerance OK (0/1) | 3rd-party | — | — | — | — | — | insufficient variation |
| Bacterial-blight grade (HC1, 1 cell) | 3rd-party | 82 | −0.562 | 0.314 | [−1.179, 0.054] | 0.074 | 0.091 |
| Regional-trial yield gain over check (pp) | self-reported | 21 | −0.994 | 0.718 | [−2.402, 0.414] | 0.166 | 0.190 |
| Production-trial yield gain over check (pp) | self-reported | 112 | −1.036 | 0.420 | [−1.860, −0.213] | 0.0137 | 0.0302 |
| Two-year regional-trial yield (kg/mu) | self-reported | 112 | +6.073 | 3.296 | [−0.387, 12.533] | 0.065 | 0.088 |
| Growth duration (days) | self-reported | 112 | −2.459 | 0.416 | [−3.275, −1.644] | 3.4×10⁻⁹ | 2.1×10⁻⁸ |
| Plant height (cm) | self-reported | 112 | +1.330 | 0.991 | [−0.612, 3.271] | 0.179 | 0.191 |
| Seed-setting percentage (%) | self-reported | 112 | +2.546 | 0.396 | [1.769, 3.323] | 1.3×10⁻¹⁰ | 2.1×10⁻⁹ |
| Thousand-grain weight (g) | self-reported | 112 | +0.846 | 0.357 | [0.147, 1.545] | 0.0177 | 0.0314 |
| Grains per panicle | self-reported | 110 | −5.248 | 2.850 | [−10.833, 0.338] | 0.066 | 0.088 |

Regional-trial yield gain over check, Arm 2, `Unified` sub-arm coverage is only 1.9% (1 of 52
records); this coefficient (n = 21) is reported in the source CSV but flagged in the main text
(§5.3) as *not estimable* and should not be read as informative.

---

## Table 4. Robustness matrix (R1–R16)

Caption: Robustness matrix, R1–R16, including all checks that qualify or fail to support the
headline result. Compiled from `manuscript/tables/table_r10_drop_winall_robustness.csv`,
`table_breakpoint_scan_full.csv`, `table_event_study_by_year.csv`, and the robustness-section
point estimates in main text §6. First cited in §6.7.

| Check | Description | Verdict |
|---|---|---|
| R1 | Two channels never pooled | Reference row only; pooling would manufacture a sign that never occurred |
| R2 | Additive (non-interaction) fixed-effects specification | Signs/magnitudes unchanged |
| R3 | Extend to all national trial groups | Direction/significance unchanged |
| R4 | 2018 unlabelled records coded Unified vs. excluded | Numerically identical — immaterial |
| R5 | Benjamini–Hochberg FDR across 17 outcomes | 8/17 retain q<0.05, including all 6 headline coefficients |
| R6 | Randomisation inference (500 permutations) | Head-rice, chalkiness, yield gain in extreme tail (RI p=0.002 each) |
| R7 | Manski worst-case bounds (4 unbalanced-missingness outcomes) | Head-rice, chalkiness sign-stable; top-two grade crosses zero — downgraded to secondary |
| R8 | Missingness balance (Supplementary Fig. S1) | Most outcomes balanced within ~2pp; 3 exceptions motivate R7 |
| R9 | Within-applicant subsample (10 applicants, 51 records) | Underpowered (MDE exceeds main coefficient on every outcome); not informative either way |
| R10 | Drop Winall-linked records | Headline result intact: head-rice −1.368pp (p=0.006), chalkiness +0.940pp (p=0.034), stated grade −0.104 (p=0.011) |
| R11 | Provincial replication (2021–2022) | 3 of 4 outcomes underpowered/undetermined; stated-grade outcome adequately powered and corroborating (β=−0.468, p=0.001) |
| R12 | Pre-declared placebos | Seed-setting, 1000-grain weight non-significant as required; plant height (not a placebo) significant, reported as auxiliary |
| R13 | Pre-reform time placebo (2005–2016) | No significant coefficient on any of 6 outcomes; opposite sign to real design |
| R14 | Cluster by variety (36 varieties) | All headline coefficients remain significant, p≤0.0014 |
| R15 | Chained-check genetic-gain ladder | Inconclusive — wide interval, does not reverse sign but cannot pin magnitude |
| R16 | `quality_stated` under disclosure-behaviour controls | Coefficient survives and strengthens (β=−0.122→−0.146) |

---

## Table 5. Winall Hi-Tech channel composition and within-channel positioning

Caption: Winall Hi-Tech: channel composition (unified vs. new-channel share) and
within-channel trait-positioning coefficients. First cited in §7.
*Source: `manuscript/tables/table5_winall_positioning.csv` (positioning) +
`manuscript/tables/table5b_winall_channel_choice_logit.csv` (channel-choice logit).*

### 5a. Channel share

| Group | n | Share Unified |
|---|---|---|
| Winall | 166 | 60.2% |
| Others | 1,101 | 47.5% |

### 5b. Channel-choice logit (Winall coefficient, α)

| Specification | n | α | SE | p | Odds ratio |
|---|---|---|---|---|---|
| Year × trial-group FE, all national groups | 1,246 | −0.728 | 0.182 | 6.7×10⁻⁵ | 0.483 |
| Year × trial-group FE, two indica groups only | 849 | −0.558 | 0.201 | 0.0054 | 0.572 |
| No fixed effects, all national groups | 1,267 | −0.516 | 0.170 | 0.0024 | 0.597 |

### 5c. Within-channel positioning (ρ, Winall vs. others)

| Sub-sample | Outcome | ρ | SE | p | n |
|---|---|---|---|---|---|
| Unified | Head-rice percentage (%) | +2.212 | 0.593 | 1.9×10⁻⁴ | 495 |
| Unified | Quality grade stated (0/1) | +0.098 | 0.028 | 4.2×10⁻⁴ | 501 |
| Unified | Chalkiness degree (%) | −0.692 | 0.188 | 2.3×10⁻⁴ | 494 |
| New (Consortium+Green) | Head-rice percentage (%) | −0.452 | 0.752 | 0.548 | 494 |
| New (Consortium+Green) | Quality grade stated (0/1) | +0.045 | 0.034 | 0.184 | 503 |
| New (Consortium+Green) | Chalkiness degree (%) | +0.200 | 0.446 | 0.655 | 495 |
