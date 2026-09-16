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
  the four unbalanced-missingness outcomes. Not yet rendered as an image file; the underlying
  bound values are reported in main text §6.2 (R7) in prose.
- **Fig. S3** — Chained-check genetic-gain ladder (R15): back-solved check-variety yield
  ladder across years with a coefficient-of-variation uncertainty band. Not yet rendered; the
  underlying diagnostics are reported in main text §6.5 (R15) in prose.

Neither is cited by number in the main text. Both should be rendered as image files before
final upload if the journal's submission system requires every named Supplementary figure to
be supplied as an image.
