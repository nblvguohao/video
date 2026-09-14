# Table 2. Descriptive statistics and balance, main analysis stratum

*Placeholder / construction note — not yet rendered as a formatted table with means and
standard deviations. This file records what Table 2 must contain and the numbers already
available for it; the final version should be built from `analysis_rice_channel.pkl`
directly (means, SDs, and non-missing rates by arm and channel) rather than retyped here.*

Sample: national approvals, two dominant mid-season indica trial groups, 2017 and
2019–2022, n = 878 (Unified 406 / Consortium 405 / Green 67).

## Missing-rate columns already available (from `results_notes_main.md` §R8 and
`plan/02_research_route.md` §1.2), by outcome, Arm 1 (Consortium / Unified, 2019–2022):

| Outcome | Non-missing %, Consortium | Non-missing %, Unified | Balanced? |
|---|---|---|---|
| head_rice_pct | 99.3 | 98.6 | yes |
| chalkiness_deg_pct | 98.3 | 98.6 | yes |
| blb_grade | 69.6 | 68.6 | yes |
| neck_blast_ok | 94.6 | 94.9 | yes |
| quality_stated | 100 | 100 | yes (non-missing by construction) |
| quality_top2 | 77.0 | 88.7 | **no, 11.7pp gap — Manski bounds reported (R7)** |
| yield_gain_pct | 99.8 | 88.1 | **no, 11.6pp gap — Manski bounds reported (R7); Arm-2 Unified coverage 1.9% (not estimable)** |
| yield_2yr_kg_mu | 100 | 90.4 | **no, 9.6pp gap — Manski bounds reported (R7)** |

## Still to be added before submission

1. Column means and SDs for all 17 outcome variables in Table 3, by arm and channel
   (Unified / Consortium / Green), computed directly from `analysis_rice_channel.pkl`.
2. Distribution of `bsys` (two-line / three-line / conventional) and `trial_group` by
   channel, to show the fixed-effect cells are not degenerate.
3. Year-by-year record counts by channel — already produced as
   `manuscript/tables/table1_channel_by_year.csv` (Table 1) and cross-referenced here rather
   than duplicated.

This placeholder exists so the Data section (§3.3) can cite "Table 2" without asserting
numbers not yet computed in tabular form; it should be replaced with the rendered table
before the manuscript is typeset.
