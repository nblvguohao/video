# Ground-truth number sheet for the v4 review (R-E line)

> Compiled directly from the CSV outputs, not from any manuscript version, so that
> reviewers have an independent reference. Any manuscript figure that disagrees with
> this sheet is a defect in the manuscript, not in the sheet.
> Source files: `manuscript/tables/table3_main_results.csv`,
> `manuscript/tables/table7_enterprise_vs_public.csv`. Read 2026-09-16.

## Headline coefficients — Arm 1 (consortium vs unified)

| Outcome | Measuring party | β (exact) | β (3 d.p.) | SE | p | BH-q | n |
|---|---|---|---|---|---|---|---|
| head_rice_pct | third-party | −1.844094 | **−1.844** | 0.4043 | 5.08e−06 | 8.64e−05 | 742 |
| chalkiness_deg_pct | third-party | +1.108465 | **+1.108** | 0.4392 | 0.01161 | 0.03290 | 739 |
| quality_stated | third-party | −0.121893 | **−0.122** | 0.0456 | 0.00750 | 0.02930 | 750 |
| quality_top2 | third-party | −0.090933 | **−0.091** | 0.0346 | 0.00862 | 0.02930 | 618 |
| gel_mm | third-party | −1.813892 | **−1.814** | 0.7484 | 0.01537 | 0.03732 | 728 |
| blb_grade | third-party | −0.190219 | **−0.190** | 0.0448 | 2.15e−05 | 1.22e−04 | 520 |
| yield_gain_pct | self-reported | +0.553445 | **+0.553** | 0.2358 | 0.01893 | 0.04022 | 708 |
| gain_prod_pct | self-reported | +0.918871 | **+0.919** | 0.2111 | 1.34e−05 | 1.14e−04 | 578 |

**Rounding caution.** `yield_gain_pct` is 0.5534, which rounds to **0.553**, not 0.554.
`plan/06_v4_review_brief.md` §R-E quotes "+0.554" — the brief is wrong on that digit,
the CSV is right. Reviewers must check which value the manuscript carries and flag
"+0.554" if present. All other headline values in the brief match the CSV exactly.

Null/non-significant Arm 1 outcomes (must not be reported as findings): amylose_pct
(−0.118, p = 0.485), lw_ratio (+0.039, p = 0.359), neck_blast_ok (−0.034, p = 0.277),
yield_2yr_kg_mu (+1.425, p = 0.612), duration_d (−0.083, p = 0.782),
seed_setting_pct (−0.202, p = 0.429), tgw_g (+0.138, p = 0.591).
plant_height_cm (+0.952, p = 0.044) and grains_per_panicle (−5.355, p = 0.025) are
nominally significant but have BH-q = 0.075 and 0.047 respectively.

## Headline coefficients — Arm 2 (green channel vs unified)

| Outcome | Measuring party | β | SE | p | n |
|---|---|---|---|---|---|
| chalkiness_deg_pct | third-party | **+2.809** | 0.4771 | 3.92e−09 | 110 |
| quality_stated | third-party | **−0.344** | 0.0789 | 1.32e−05 | 112 |
| quality_top2 | third-party | **−0.269** | 0.1108 | 0.01509 | 70 |
| amylose_pct | third-party | −1.520 | 0.4588 | 0.00092 | 110 |
| gel_mm | third-party | −6.558 | 1.8097 | 0.00029 | 112 |
| head_rice_pct | third-party | −0.391 | 0.6557 | 0.551 (n.s.) | 106 |
| gain_prod_pct | self-reported | −1.036 | 0.4202 | 0.01367 | 112 |
| yield_gain_pct | self-reported | −0.994 | 0.7183 | 0.166 (n.s.) | 21 |

`neck_blast_ok` in Arm 2 is `insufficient_variation` — no estimate exists. Any manuscript
sentence reporting an Arm 2 neck-blast coefficient is fabricated.
SE type differs by arm: Arm 1 is `cluster(cell, G=10)`; Arm 2 is `HC1` with 2 cells
(1 cell for `blb_grade`). Arm 2 inference is therefore weak by construction and the
manuscript must say so.

## Enterprise vs public-institution descriptive panel (Supplementary Table S1)

| Outcome | θ | SE | p | n |
|---|---|---|---|---|
| yield_2yr_kg_mu (regional-trial yield, kg/mu) | **+4.179** | 1.893 | 0.0273 | 408 |
| tgw_g (1000-grain weight, g) | **+1.193** | 0.402 | 0.0030 | 411 |
| chalkiness_deg_pct (chalkiness, %) | **+1.010** | 0.614 | 0.100 | 411 |
| head_rice_pct (head-rice %) | **−1.220** | 0.673 | 0.070 | 411 |

**Sign convention — RESOLVED, no defect.** The CSV column `theta` carries no stated
direction, so this was checked against the estimator rather than inferred from the
prose. `manuscript/scripts/mechanism_winall.py` (TASK 4, ~line 275) sets
`main_layer["public"] = (main_layer.applicant_type == "Public").astype(int)` and fits
`Y ~ public + C(yxg) + C(bsys)` with `cov_type="cluster"` on `yxg`, taking θ as the
coefficient on `public`. **θ is therefore Public minus Enterprise.** §7's reading is
correct: public-institute applicants show higher regional-trial yield and 1000-grain
weight, *and* higher chalkiness and lower head-rice — i.e. worse third-party grain
quality than enterprise applicants. That is what makes the paragraph a counter-case to
the "enterprises are careless breeders" alternative, so the argument stands as written.
Reviewers do not need to re-open this; they do need to confirm the four values and the
n = 408–411 range are reproduced unchanged in v4.

n ranges 408–411. The planning-document values **+3.18 / +0.96** and the planning n of
**632** are superseded and must not appear anywhere in v4 (this was the v2 correction;
a regression to those numbers is a hard failure).
Note both chalkiness (p = 0.100) and head-rice (p = 0.070) are **not** significant at
5%; only the two self-reported/agronomic outcomes are. The manuscript must not describe
this panel as showing a significant third-party quality deficit.

## Invariance requirement

v2, v3 and v4 all declare that no statistical result changes. Concretely, every number in
the two tables above must appear in `manuscript_v4.md` with the same value and the same
sign as in `manuscript_v3.md`. The reframing was permitted to change framing, section
order, title, abstract wording and citations only.
