**Table 5.** Germplasm concentration across resolved parental lines, by trial channel and arm.
Sample: national approvals in the two dominant mid-season indica trial groups — the same
stratum as the main estimates. Sterile (female) lines of the originating cross, resolved from
the announcement's variety-source field (§3.1). HHI is the Herfindahl–Hirschman index across
sterile lines. Distinct-line counts are reported raw and rarefied to the smaller group's *n*,
because distinct counts rise mechanically with sample size; rarefaction is applied to the
sterile-line counts only. The HHI difference is tested by a stratified bootstrap (10,000
resamples, percentile interval) and a label-permutation test (10,000 permutations,
*p* = (1 + *k*)/(1 + *B*)).

| Arm | Channel | *n* | Distinct sterile lines | Rarefied | HHI | Top line share | Distinct restorer lines | HHI (restorer) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Arm 1 (2019–2022) | Unified | 353 | 156 | 156.0 | 0.01858 | 9.1% | 241 | 0.00699 |
| Arm 1 (2019–2022) | Consortium | 405 | 212 | 193.0 | 0.01239 | 5.7% | 304 | 0.00577 |
| Arm 2 (2017) | Unified | 52 | 30 | 30.0 | 0.05621 | 11.5% | 48 | 0.02219 |
| Arm 2 (2017) | Green channel | 67 | 35 | 29.4 | 0.07775 | 22.4% | 56 | 0.02428 |

**Between-channel difference in sterile-line HHI (new channel − Unified)**

| Arm | Observed | 95% bootstrap CI | Permutation *p* | *n* (Unified / new) |
|---|---:|---|---:|---|
| Arm 1: Consortium − Unified | −0.00618 | [−0.01303, −0.00085] | 0.022 | 353 / 405 |
| Arm 2: Green − Unified | +0.02153 | [−0.02398, +0.06712] | 0.344 | 52 / 67 |

**Extraction coverage by channel** (reported because unbalanced extraction failure would
confound the comparison): Arm 1 Unified 99.7%, Arm 1 Consortium 100%, Arm 2 Unified 100%,
Arm 2 Green 100%.

*Consortium entrants draw on a significantly broader sterile-line base than contemporaneous
unified entrants. Green-channel entrants are directionally more concentrated, but at n = 52
versus 67 the interval spans zero and the difference is not significant; that arm is reported
for completeness and no claim rests on it. Because differently spelled variants of the same
line are not merged (§3.1), reported concentration levels are lower bounds.*

Source: `scripts/analysis/germplasm_concentration.py`;
`manuscript/tables/table_germplasm_concentration.csv`.
