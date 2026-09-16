**Table 5.** Germplasm concentration across resolved parental lines, by trial channel and arm.
National approvals in the two dominant mid-season indica trial groups; sterile (female) lines
of the originating cross, resolved from the announcement's variety-source field (§3.1; 95.6%
of national records resolve). HHI is the Herfindahl–Hirschman index across sterile lines.
Distinct-line counts are reported both raw and rarefied to the smaller group's *n*, because
distinct counts rise mechanically with sample size. The difference in HHI is tested by a
stratified bootstrap (2,000 resamples, percentile interval) and a label-permutation test
(2,000 permutations).

| Arm | Channel | *n* | Distinct sterile lines | Rarefied | HHI | Top line share | Distinct restorer lines | HHI (restorer) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Arm 1 (2019–2022) | Unified | 521 | 238 | 238.0 | 0.01281 | 7.5% | 342 | 0.00574 |
| Arm 1 (2019–2022) | Consortium | 542 | 298 | 290.0 | 0.00846 | 4.6% | 396 | 0.00477 |
| Arm 2 (2017) | Unified | 85 | 61 | 58.6 | 0.02644 | 8.2% | 77 | 0.01481 |
| Arm 2 (2017) | Green channel | 81 | 43 | 43.0 | 0.06447 | 19.8% | 67 | 0.01844 |

**Between-channel difference in sterile-line HHI (new channel − Unified)**

| Arm | Observed | 95% bootstrap CI | Permutation *p* | *n* (Unified / new) |
|---|---:|---|---:|---|
| Arm 1: Consortium − Unified | −0.00435 | [−0.00829, −0.00078] | 0.016 | 521 / 542 |
| Arm 2: Green − Unified | +0.03804 | [+0.00931, +0.07553] | 0.009 | 85 / 81 |

*The two self-organised channels differ from the unified trial in opposite directions, each
matching the number of breeding programmes its rules admit: green-channel trials are run by a
single certified enterprise and draw on a narrower base, while consortium trials pool five or
more breeders and draw on a broader one. Because differently spelled variants of the same line
are not merged (§3.1), reported concentration is a lower bound and the contrasts are biased
toward finding no difference.*

Source: `scripts/analysis/germplasm_concentration.py`;
`manuscript/tables/table_germplasm_concentration.csv`.
