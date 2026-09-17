# Supplementary Material

**Manuscript:** "Rice variety approval records as an innovation indicator source: trial channel, third-party-assayed grain quality, and who measures what enters the market in China, 2017–2022"

> This file contains the table and figures presented as Supplementary Material to the
> manuscript above, to keep the main text within the journal's 6-figure / 5-table target.
> Captions and source data are as cited in the main text.

---

## Supplementary Table S1

**Caption:** Descriptive trait division of labour, enterprise vs. public research institution
applicants (n = 408–411; the applicant-type field is entirely missing for national approvals
in 2016, 2017, 2018 and 2021, so this comparison is confined to years with a non-missing
applicant field — see main text §3.3 and §4.7 Non-claim 9). Reported strictly as descriptive
background, not as a causal or headline comparison. Cited in the main text at §7. Neither
quality coefficient reaches conventional significance (chalkiness p = 0.100, head-rice
p = 0.070); the contrast is suggestive only and no part of the argument rests on it.

| Outcome | θ (Public − Enterprise) | SE | p | n |
|---|---|---|---|---|
| Regional-trial yield (kg/mu) | +4.179 | 1.893 | 0.027 | 408 |
| 1000-grain weight (g) | +1.193 | 0.402 | 0.003 | 411 |
| Chalkiness (%) | +1.010 | 0.614 | 0.100 | 411 |
| Head-rice percentage (%) | −1.220 | 0.673 | 0.070 | 411 |

θ is the coefficient on `Public` (public research institute applicant) relative to enterprise
applicant, from the descriptive specification in main text §4.6 ($Y_i = \theta\,\text{Public}_i
+ \gamma_{y \times g} + \delta_b + \varepsilon_i$), restricted to years with non-missing
`applicant_type`.

---

## Supplementary Fig. S1

**Caption:** Missingness-balance dumbbell plot. For each of the paper's 17 outcome variables,
two markers show the non-missing rate in the Unified arm versus the self-organised arm
(Consortium, Arm 1), connected by a line; outcomes with an imbalance of 8 percentage points or
more are flagged in orange. Most outcomes are balanced within about 2 percentage points; the
three flagged exceptions — the top-two quality-grade indicator, the regional-trial yield-gain
variable, and absolute regional-trial yield in kg/mu — are exactly the three for which the
main text (§6.2, R7) reports Manski worst-case bounds alongside the point estimate, rather than
treating the complete-case estimate as final.

**Reason for placement in Supplementary Material:** its content is reported numerically in
main text Table 2 (missing-rate columns, by arm) and in the §6.1–6.2 prose (checks R7 and R8);
the figure restates visually what the reader already has in numbers.

---

## Note on Supplementary Fig. S2 and Fig. S3

Two further figures are provided for completeness:

- **Fig. S2** — Manski worst-case bounds: observed / best-case / worst-case interval bars for
  the three unbalanced-missingness outcomes. Not yet rendered as an image file; the underlying
  bound values are reported in main text §6.2 (R7) in prose.
- **Fig. S3** — Chained-check genetic-gain ladder (R15): back-solved check-variety yield
  ladder across years with a coefficient-of-variation uncertainty band. Not yet rendered; the
  underlying diagnostics are reported in main text §6.5 (R15) in prose.

Neither is cited by number in the main text. Both should be rendered as image files before
final upload if the journal's submission system requires every named Supplementary figure to
be supplied as an image.

---

## Supplementary Note S1. Chained-check genetic-gain scale (robustness check R15)

Main text §6.5 reports the verdict of this check and its four headline diagnostics. Its
construction and full diagnostics are given here.

**Construction.** The percentage gain over the named check reported in approval announcements
is comparable only within a trial-year-check cell. To place yield on a scale comparable across
years, we exploit the fact that each announcement records mean yield, the named check variety
and the percentage gain over it, which allows the implied check-variety yield to be back-solved
for each record. Records sharing the same check in adjacent approval years are then linked into
a step-wise check ladder. Where the same check recurs, the discrepancy between independently
back-solved yields is an internal-consistency diagnostic; the year-to-year change along the
ladder is the chained estimate of realised genetic gain. The approach follows the established
genetic-gain literature separating genetic from non-genetic sources of trend in official
variety trials (Piepho et al., 2014; Laidig et al., 2014; Mackay et al., 2011).

**Full diagnostics.**

1. *Back-solved check yield is unstable.* Within the main analysis layer, the coefficient of
   variation of the back-solved check yield across records sharing a check-year cell has a
   median of 1.56%, a 90th percentile of 3.32% and a maximum of 5.40%. An independent
   re-verification using only the fields available in the national rice dataset reproduces the
   same order of magnitude — median CV 0.9%–2.4%, 90th percentile roughly 3%–3.6% — but not the
   figures digit-for-digit, because the exact cell construction and backfilled gain variable of
   the original pipeline cannot be fully recovered from that table alone. We report the
   discrepancy rather than adopt the closer-looking number.
2. *A chain step does not reconcile.* A key step in the chain, checked directly against the
   underlying records, moves by +3.14%, not the +7.04% implied by the decomposition's structural
   identity — a gap large enough to discourage taking the point estimate at face value.
3. *The implied rate is not stable to chain composition.* Depending on which years and checks
   enter the chain, the implied genetic-gain rate swings between 0.25% and 0.50% per year, a
   two-fold range from a method whose appeal is a single defensible number.
4. *Inference is thin.* The chain rests on six distinct check varieties (G = 6). Clustering
   standard errors at the check level gives an effective degrees of freedom of about 3,
   inflating standard errors roughly six-fold relative to the naive unclustered calculation.

**Why these are expected.** Each is a known property of check-based genetic-gain estimation
rather than a defect specific to this corpus. Mackay et al. (2011) and Laidig et al. (2014)
document sensitivity to the trial series used; Raymond et al. (2023) show that check-variety
yields are not stable over time and that gain estimates depend heavily on which long-term
checks are chosen; and Piepho and Laidig (2025) formalise why a low check-replacement rate and
multiple checks per cycle are required for the chain to be informative — conditions that
Chinese approval bulletins, with few checks and irregular replacement, do not meet.

**Conclusion.** Re-expressed on a chained cross-year check scale, the direction of the
applicant-self-reported yield advantage does not reverse, but the resulting interval is too
wide to support any precise claim about its magnitude. The chained-scale evidence is
inconclusive — neither confirmatory nor disconfirmatory of the estimate reported in §5.
