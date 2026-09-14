# Results notes — main estimation and robustness (实跑, 2026-09-14)

> Data: `evidence/data/analysis_rice_channel.pkl` (6,734 records; 国审 2,386 / 省审 4,347).
> Scripts: `scripts/analysis/estimate_channel_gap.py` (Table 3), `scripts/analysis/robustness_supplement.py`
> (R4, R13, R9/R11 MDE), `scripts/analysis/make_figures.py` (Figs. 2, 6, 7).
> Model: $Y_i=\beta\,\text{NewChannel}_i+\gamma_{c(i)}+\delta_{b(i)}+\varepsilon_i$, $c(i)$ = approval
> year × trial group × named check (single interaction fixed effect — **not** additive
> trial-group + check, which is collinear; see `plan/02_research_route.md` §3.1).
> Cells with only one channel present are dropped (no identifying variation). SE clustered by
> cell when the arm has ≥5 effective clusters; HC1 otherwise (flagged).

Main stratum (国审 × {长江中下游中籼迟熟, 长江上游中籼迟熟} × {2017, 2019–2022}): **n = 878**
(Unified 406 / Consortium 405 / Green 67) — matches `plan/02_research_route.md` §2 exactly.

---

## 1. Table 3 replication and consistency check

Table 3 is at `manuscript/tables/table3_main_results.csv` (34 rows: 17 outcomes × 2 arms).

**Arm 1 (Consortium vs Unified, 2019–2022, n = 759 pre-outcome-drop, 8–10 clustered cells)**
cross-checked against the numbers already reported in `01_theme_and_innovation.md` §5/§9:

| outcome | reported (01/02) | this run | match |
|---|---|---|---|
| head_rice_pct | β=−1.844, p<0.0001 | β=−1.8441, p=5.1e-06, n=742 | exact |
| chalkiness_deg_pct | β=+1.108, p=0.012 | β=+1.1085, p=0.0116, n=739 | exact |
| quality_stated | β=−0.122, p=0.008 | β=−0.1219, p=0.0075, n=750 | exact |
| yield_gain_pct | β=+0.554, p=0.020 | β=+0.5534, p=0.0189, n=708 | exact |
| gain_prod_pct | β=+0.919, p<0.0001 | β=+0.9189, p=1.3e-05, n=578 | exact |
| blb_grade | β=−0.190, p<0.0001 | β=−0.1902, p=2.1e-05, n=520 | exact |

All six pre-registered numbers reproduce to 3–4 decimal places. **No discrepancy to explain** —
the cell construction (`approval_year|trial_group|ck_n`, factorized, singleton-channel cells
dropped, cluster-robust SE by cell) recovers the numbers already logged in the theme file.

**Arm 2 (Green vs Unified, 2017, n = 112, 2 identifying cells out of 3 raw cells — the third
raw cell has only Green records and is dropped, HC1 SE)** also reproduces the logged numbers,
e.g. chalkiness +2.809 (p<0.0001), quality_stated −0.344 (p<0.0001), head_rice −0.391 (p=0.55,
not significant, as previously reported).

**quality_stated construction note**: defined as `quality_grade.notna() | quality_std.notna()`
(the announcement carries either a numeric grade or a named quality standard). The two source
fields agree on presence/absence 84.5% of the time; using the union rather than either field
alone maximizes consistency with the "载明国家/行业米质等级" definition and gives 0% missingness
by construction, as specified in `02_research_route.md` §1.2.

---

## 2. Full Table 3 (β / 95% CI / p / BH-q), key rows

See CSV for all 34 rows. Selected non-headline rows worth flagging:

- **quality_top2** (米质一二级), Arm 1: β=−0.091, p=0.009, q=0.029 — significant here, but recall
  CF4/K5: under Manski worst-case bounds this sign is **not stable** (`[−0.253, +0.088]`,
  documented in `01_theme_and_innovation.md` §9). Treat as secondary, per pre-registration.
- **plant_height_cm**, Arm 1: β=+0.952, p=0.044 — reproduces CF7/K9. Per pre-registration this
  is **not** in the placebo set; it is auxiliary evidence consistent with a tall/large-panicle
  selection type, declared *before* seeing the result.
- **seed_setting_pct** (β=−0.202, p=0.429) and **tgw_g** (β=+0.138, p=0.591), Arm 1 — the two
  pre-declared placebo traits — are both non-significant, as required.
- **gel_mm**, Arm 1: β=−1.814, p=0.015 — third-party assayed, same direction as the head-rice/
  chalkiness story (worse gel consistency in Consortium entrants); not previously headlined but
  consistent with the sign-separation pattern.
- Arm 2 **yield_gain_pct**: n=21 only — confirms CF3 ("not estimable" in practice; Unified-arm
  coverage in 2017 is ~1.9%, i.e. this coefficient should not be interpreted).
- Arm 2 **gain_prod_pct**: β=−1.036, p=0.014 — confirms CF2, opposite sign to Arm 1's +0.919.

---

## 3. Robustness checks run this session

### R4 — 2018 treatment (exclude vs code as Unified)

Two cell definitions tested: (i) the main `year×trial_group×check` cell, (ii) a coarser
`year×trial_group` cell (no check). Under **both**, coding all 233 unlabeled-channel 2018
records as Unified produces **identical** point estimates and p-values to excluding them
(main design) — because 2018 never contains a Consortium record in this stratum (only 1 Green
record among 236), so any 2018 cell is a Unified-only (or, in one case, Green-only) singleton
that carries no identifying variation for the Consortium-vs-Unified contrast regardless of its
label. Concretely:

| outcome | (a) exclude 2018 | (b) 2018→Unified |
|---|---|---|
| head_rice_pct | β=−1.844, p<0.0001, n=742 | identical |
| chalkiness_deg_pct | β=+1.109, p=0.012, n=739 | identical |
| quality_stated | β=−0.122, p=0.008, n=750 | identical |
| yield_gain_pct | β=+0.553, p=0.019, n=708 | identical |
| gain_prod_pct | β=+0.919, p<0.0001, n=578 | identical |
| blb_grade | β=−0.190, p<0.0001, n=520 | identical |

**Interpretation**: the 2018 coding choice is provably immaterial to Arm 1's headline numbers
under this design, not merely "empirically similar." This is a stronger and more transparent
statement than a re-estimated "close" number, and it should replace/support the previously
logged "提案 C 在合并层已验证结果不变 (−1.603/+1.398)" reference, which used a different
(additive, pooled) specification.

### R13 — time placebo, 2005–2016 (pre-reform, no real channel variable)

Pseudo-treatment = `applicant_type == 'Enterprise'` (proxy for integrated/enterprise
applicants; the closest available construct to "育繁推一体化企业" given the data — a stricter
integration flag is not separately coded). Sample: 国审 × two trial groups × 2005–2016 ×
applicant-labelled records only, cell FE = year×trial_group×check, singleton cells dropped:
**n = 153, 13 cells**.

| outcome | pseudo-treatment β | p | real-design β (Arm 1) |
|---|---|---|---|
| head_rice_pct | +0.939 | 0.261 | −1.844 |
| chalkiness_deg_pct | −0.828 | 0.212 | +1.108 |
| quality_stated | +0.038 | 0.652 | −0.122 |
| yield_gain_pct | −0.289 | 0.563 | +0.554 |
| gain_prod_pct | −0.155 | 0.594 | +0.919 |
| blb_grade | −0.232 | 0.424 | −0.190 |

**None of the six pseudo-treatment coefficients is significant, and for the two headline
quality traits the sign is opposite to the real design** (head_rice +0.94 vs −1.84; chalkiness
−0.83 vs +1.11). This is the expected null result: applicant-type composition alone, in a
period with no real channel variation, does not reproduce the "quality worse" pattern. It does
**not** by itself prove H_measure over H_threshold (per §3.4/§4-R9, that distinction remains
open), but it does show the quality gap is not simply an artifact of enterprise-vs-public
applicant mix.

**Caveat**: `applicant_type` is missing for 2016/2017/2018/2021 entirely in the full dataset,
so this placebo uses only the applicant-labelled subset of 2005–2016 (n=213 raw → 153 after
dropping singleton cells); it is not a full-population check.

### R9 supplement — within-applicant MDE

Same-applicant, both-channel subsample, Arm 1 window: **10 applicants, 51 records** (26
Consortium / 25 Unified), matching the previously logged "约10家申请人/26条记录." Regression
uses applicant fixed effects (rather than the main year×group×check cell, which is too fine for
this subsample) with HC1 SE:

| outcome | n | β | p | MDE (80% power) | vs main effect |
|---|---|---|---|---|---|
| head_rice_pct | 51 | +0.780 | 0.609 | 4.37 | main β=−1.844 → **underpowered** |
| chalkiness_deg_pct | 51 | +0.846 | 0.214 | 1.96 | main β=+1.108 → **underpowered** |
| quality_stated | 51 | +0.118 | 0.402 | 0.41 | main β=−0.122 → **underpowered** |
| yield_gain_pct | 49 | +0.100 | 0.862 | 1.66 | main β=+0.554 → **underpowered** |
| gain_prod_pct | 49 | −0.126 | 0.816 | 1.56 | main β=+0.919 → **underpowered** |
| blb_grade | 32 | −0.421 | 0.383 | 1.41 | main β=−0.190 → **underpowered** |

For every headline outcome, the 80%-power minimum detectable effect **exceeds** the magnitude
of the main-design coefficient — in several cases by 2–8×. This converts the qualitative
"检验力不足" claim in `01_theme_and_innovation.md` §8 (Non-claim 1) into a quantitative one: this
design **cannot** distinguish "no channel effect once self-selection is removed" from "the
channel effect exists but this subsample is too small to see it." The point estimates
themselves also flip sign relative to the main design on head_rice, chalkiness, and
quality_stated — consistent with a severely underpowered, noisy estimate rather than a
credible contradiction.

### R11 supplement — provincial replication MDE

Provincial sample: 省审 × 2021–2022, `new_channel = Consortium ∪ Green`, cell FE =
`year×trial_group` (no check — provincial trial-group labels are far more heterogeneous and a
check-level cell collapses the sample to single digits). **Raw n = 495** (new_channel 143 /
Unified 352).

**Important discrepancy, reported as required rather than reconciled**: this n (495) and the
regression sample sizes below do not exactly match the "n=452 (新通道143/统一318)" figure
logged in `02_research_route.md` §2 and the "整精米率 −0.134 (p=0.93)" result logged in
`01_theme_and_innovation.md` §8/§9 (Non-claim 8 / CF6). The "143" new-channel count does match
exactly; the "318" Unified count and the resulting point estimates do not, most likely because
the earlier session used a different cell/FE specification (possibly `year×trial_group×check`
at the province level, or an additional filter not documented in the plan files) that this
script cannot exactly reverse-engineer from the plan text alone. **The direction of the
finding — provincial-level non-significance — is the same in both runs**, which is what
matters for R11's role in the argument; the point estimates differ and this is flagged rather
than silently reconciled, per instructions.

| outcome | n | β | p | MDE (80% power) | vs national Arm‑1 β |
|---|---|---|---|---|---|
| head_rice_pct | 280 | −3.354 | 0.528 | 14.99 | national β=−1.844 → **underpowered** |
| chalkiness_deg_pct | 256 | −0.549 | 0.239 | 1.31 | national β=+1.108 → **underpowered** |
| quality_stated | 495 | −0.468 | 0.001 | 0.41 | national β=−0.122 → adequately powered (and *significant*, larger magnitude, opposite direction of concern) |
| yield_gain_pct | 205 | −0.994 | 0.617 | 5.62 | national β=+0.554 → **underpowered** |

**Interpretation**: for head_rice, chalkiness and yield_gain, the provincial replication genuinely
lacks the power to detect an effect the size of the national one — "国审层效应量在省审层不可判定"
is the correct reading, not "province disproves nation." `quality_stated` is the one outcome
where the province sample **is** adequately powered and returns a significant, larger-magnitude,
same-direction (negative) coefficient — worth noting in Discussion as the one provincial result
that is not simply underpowered.

---

## 4. Figures produced

- `figures/fig2_forest_main.png` / `.pdf` — forest plot, both arms, 17 outcomes, colored by
  measurement party (blue = third-party assayed, red = applicant self-reported). Arm 2's
  `neck_blast_ok` is marked "not estimable" — the field is **100% missing** for all 119 Arm-2
  records (both channels; 2017-stratum announcements do not populate it), not merely
  imbalanced, so the FE regression has no rows to fit.
- `figures/fig6_randomization.png` / `.pdf` — 500-permutation randomization-inference null
  distributions vs observed β, four panels (head rice, chalkiness, yield gain vs check, quality
  top-2). Reproduces the logged RI p-values almost exactly: head_rice RI p=0.002 (null mean
  +0.028, sd 0.396 vs logged −0.009/0.396), chalkiness RI p=0.002 (null mean −0.010, sd 0.191),
  yield_gain RI p=0.004 (null mean −0.014, sd 0.170), quality_top2 RI p=0.016.
- `figures/fig7_missingness_balance.png` / `.pdf` — dumbbell plot, non-missing rate by channel,
  Arm 1, all 17 outcomes, orange highlighting ≥8pp imbalance. Confirms R8: yield_gain_pct
  (88.1% Unified / 99.8% Consortium, gap 11.6pp), quality_top2 (88.7%/77.0%, gap 11.7pp), and
  yield_2yr_kg_mu (90.4%/100%, gap 9.6pp) are flagged as imbalanced; all quality/anatomy traits
  (head rice, chalkiness, L/W ratio, amylose, gel, TGW, height, duration) are balanced within
  ~2pp.

---

## 5. Statements this analysis supports vs does not support

**Supported by this run:**
- Arm 1's sign-separation result (third-party quality worse, self-reported yield/production
  gain higher or unchanged) reproduces exactly.
- The 2018-treatment choice (R4) is provably immaterial to Arm 1, under two different cell
  definitions.
- The pre-reform time placebo (R13) shows no significant, same-signed pseudo-channel effect —
  consistent with (not proof of) the sign-separation argument not being an artifact of
  applicant-type composition.
- Both within-applicant (R9) and provincial (R11) "failures to replicate" are, for most
  outcomes, quantitatively attributable to insufficient statistical power (MDE > main effect),
  not to a credible contradicting estimate — except provincial `quality_stated`, which is
  adequately powered and gives a significant, same-direction, larger-magnitude result.

**Not supported — do not claim:**
- That the within-applicant or provincial subsamples "confirm" the main effect — they mostly
  cannot statistically distinguish "no effect" from "main effect masked by noise."
- That R13's null result rules out H_threshold (the "两条通道的申报门槛不同" alternative) — it
  only weakens one specific confound (applicant-type composition in the pre-reform sample), not
  the general self-selection story.
- Any causal language for β — it remains the composition/entering-effect estimand defined in
  `02_research_route.md` §3.3.
- That the R11 n/point-estimate mismatch has been resolved — it has not; it is reported as an
  open discrepancy per instructions, not explained away.
