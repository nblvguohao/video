# Coordinator's test of R4's "strongest attack" — and why its proposed fix is not available

> R4 named one attack as the most damaging available and called the fix cheap: *"the
> approval type is in the same announcements they already parse"*, recommending it be
> added as robustness check R17 — *"the one change that moves it from 'probably
> publishable' to 'hard to reject'."*
> That premise was tested directly against the corpus before being passed to the author.
> **It is false.** A substitute check that does run is reported below, and it supports
> the paper.

## 1. The proposed control does not exist in this corpus

R4's attack: China's variety-approval system defines multiple approval standards
(高产稻 / 优质稻 and similar) with different trait bundles. If self-organised applicants
disproportionately pursue the high-yield category, then conditional on approval their
entrants *must* show lower third-party quality and equal-or-higher applicant-measured
yield — reproducing the headline result mechanically, with no measurement discretion.

The attack is conceptually sound. The proposed fix is not executable. String counts over
`特征特性 + 产量表现 + 品种来源` in `evidence/data/national_rice_varieties_raw.csv`
(7,883 records):

| Marker | Meaning | Matches |
|---|---|---|
| `高产稻` | high-yield approval category | **0** |
| `高产稳产` | high-yield/stable category (2021 standard) | **0** |
| `绿色优质` | green-superior-quality category | **0** |
| `审定标准` | "approval standard" | **0** |
| `品种类型` / `品种类别` | "variety type" / "variety category" | **0** / **0** |
| `优质稻` | — | 819, but **all** as part of 《优质稻谷》, a grain **grading standard**, not an approval category |
| `特殊类型` | special-type | 32, and these are **trial-group** designations (特殊类型稻品种区域试验, e.g. upland rice), not approval categories |

The announcements do not record which approval-standard category a variety was judged
under. **R17 as R4 specified it cannot be run**, and the recommendation must not be
passed to the author in that form — it would send them looking for a field that is not
there.

Note also that the `特殊类型` records are trial-group designations, and the analysis
stratum already restricts to the two dominant indica trial groups, so they are excluded
already.

## 2. A related confound that IS testable — and the paper survives it

The corpus does contain a real, previously unexamined heterogeneity: **records are graded
under two different quality standards**, and the mix shifts sharply across the study
window. `quality_std` is already parsed in `analysis_rice_channel.pkl`.

National records by year:

| Year | 《优质稻谷》 (GB/T) | 《食用稻品种品质》 (NY/T 593) |
|---|---|---|
| 2017 | 111 | 25 |
| 2018 | 110 | 123 |
| 2019 | 8 | 192 |
| 2021 | 0 | 305 |
| 2022 | 106 | 151 |

This is a genuine threat on its face: Arm 2 (green channel) sits in 2017, when GB/T
dominates, and Arm 1 (consortium) sits in 2019–2022, when NY/T 593 dominates. If channel
correlated with standard, the quality outcomes would not be comparable.

**Test: within each arm's own window, does the standard used differ by channel?**

Arm 1, consortium vs unified, 2019–2022 (n = 1,092), row-normalised:

| | no stated standard | 《优质稻谷》 | 《食用稻品种品质》 |
|---|---|---|---|
| Unified | 0.287 | 0.009 | **0.701** |
| Consortium | 0.388 | 0.005 | **0.604** |

Arm 2, green vs unified, 2017 (n = 175):

| | no stated standard | 《优质稻谷》 | 国标 |
|---|---|---|---|
| Unified | 0.322 | **0.655** | 0.023 |
| Green | 0.500 | **0.466** | 0.034 |

**Conclusion: the standard in force is determined almost entirely by year, not by
channel.** Within Arm 1 both arms are ~97% NY/T 593 among graded records; within Arm 2
both are ~95% GB/T among graded records. The year × trial-group × check interaction fixed
effects therefore absorb the standard switch. This confound does not threaten the result.

**And the test independently reproduces the headline finding.** The whole channel
difference sits in the *no stated standard* column: +10.1 pp for consortium (0.388 vs
0.287) and +17.8 pp for green (0.500 vs 0.322). Those are the raw analogues of the
regression estimates for `quality_stated`, −0.122 and −0.344 (which are larger once the
fixed effects are applied — expected, not anomalous). The finding is about **whether a
grade is disclosed at all**, not about which standard was applied.

## 3. What to do in v5

- **Do not** add R4's R17 as specified — the field does not exist. Say so explicitly in
  the v5 change log so the recommendation is not silently dropped and later re-raised.
- **Do** add the standard-composition check above as a genuine new robustness item. It is
  cheap, it runs on parsed data, and it closes a real alternative explanation.
- **Do** keep R4's underlying criticism alive in the Limitations: the paper cannot rule
  out that channels differ in the *implicit* trait bundle applicants target, because the
  approval category is not recorded in the corpus at all. That is an honest statement of
  a real limit, and it is stronger than silence — it tells the referee the authors looked.
- R4's related point that the bacterial-blight result is read too favourably ("bounds the
  composition effect") deserves separate consideration; trait-bundle selection is an
  alternative reading of that result and is not currently acknowledged.
