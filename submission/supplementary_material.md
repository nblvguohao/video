# Supplementary Material

**Manuscript:** "Who measures what enters the market? Self-organised variety trials and the
third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"

> This file contains the tables and figure moved out of the main text under the editorial
> decision recorded in `manuscript/figure_table_list.md` (2026-09-14), to bring the
> submission to the journal's 6-figure / 5-table main-text target
> (`plan/04_format_spec.md` §5). Original captions and source data are reproduced unchanged;
> only the numbering and its main-text pointer have changed.
>
> **v3 update (2026-09-16):** the former Supplementary Table S1 (Winall and comparator
> company financial panel) has been **removed in full**, at the author team's request that no
> discussion of any applicant firm's financial or business performance appear in the paper.
> With the §7 financial narrative it supported deleted from the main text, the table no
> longer had an independent role and is not retained in any edited or partial form. The
> former Supplementary Table S2 is renumbered **Table S1**. See
> `manuscript/review/change_log_v2_to_v3.md` for the full record of this revision.

---

## Supplementary Table S1

*(Formerly Table 7 in the pre-submission working draft; formerly Supplementary Table S2 in
the v2 submission package. Renumbered to S1 in v3 after the removal of the former Table S1.)*

**Caption:** Descriptive trait division of labour, enterprise vs. public research institution
applicants (n = 408–411; the applicant-type field is entirely missing for national approvals
in 2016, 2017, 2018 and 2021, so this comparison is confined to years with a non-missing
applicant field — see main text §3.3 and §4.7 Non-claim 9). Reported strictly as descriptive
background, not as a causal or headline comparison. Cited in the main text at §7 (Mechanism).
An earlier planning-stage note anticipated n = 632 for this comparison; the discrepancy
against the n = 408–411 actually returned by the regression is disclosed in the main text
(§7) as an unreconciled open item, not adjusted to match the planning note.

**Source file:** `manuscript/tables/table7_enterprise_vs_public.csv`

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

*(Formerly Fig. 6 in the pre-submission working draft, before the Winall mechanism figure was
renumbered into that slot.)*

**Caption:** Missingness-balance dumbbell plot. For each of the paper's 17 outcome variables,
two markers show the non-missing rate in the Unified arm versus the self-organised arm
(Consortium, Arm 1), connected by a line; outcomes with an imbalance of 8 percentage points or
more are flagged in orange. Most outcomes are balanced within about 2 percentage points; the
three flagged exceptions — the top-two quality-grade indicator, the regional-trial yield-gain
variable, and absolute regional-trial yield in kg/mu — are exactly the three for which the
main text (§6.2, R7) reports Manski worst-case bounds alongside the point estimate, rather than
treating the complete-case estimate as final.

**Source file:** `manuscript/figures/fig7_missingness_balance.png` / `.pdf` (original
rendered-file name retained; the number in the filename reflects the pre-merge working
numbering, not the published number, consistent with the naming convention already used for
Fig. 5 in the main text).

**Reason for placement in Supplementary Material:** its content is already fully reported
numerically in main text Table 2 (missing-rate columns, by arm) and in the §6.1–6.2 prose
(checks R7 and R8); the figure is a visual restatement of numbers the reader already has
rather than a source of new information, which is the criterion this document's own v1 draft
proposed for this specific candidate.

---

## Note on Supplementary Fig. S2 and Fig. S3

Two further figures were already slated for Supplementary Material prior to this session's
compression decision (`plan/02_research_route.md` §7) and are unaffected by the Table
6/7/Fig. 6/7 renumbering above:

- **Fig. S2** — Manski worst-case bounds: observed / best-case / worst-case interval bars for
  the four unbalanced-missingness outcomes. Not yet rendered as an image file; the underlying
  bound values are reported in main text §6.2 (R7) in prose.
- **Fig. S3** — Chained-check genetic-gain ladder (R15): back-solved check-variety yield
  ladder across years with a coefficient-of-variation uncertainty band. Not yet rendered; the
  underlying diagnostics are reported in main text §6.5 (R15) in prose.

Neither is cited by number in the main text, so their absence as rendered image files does not
block submission, but the author team should render both before final Supplementary Material
upload if the target journal's submission system requires all named Supplementary figures to
be supplied as image files (see `submission/submission_checklist.md`).
