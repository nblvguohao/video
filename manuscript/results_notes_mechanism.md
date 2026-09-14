# Results notes — Mechanism section: Winall Hi-tech Seed as a counter-case

> Companion to `plan/01_theme_and_innovation.md` §7 and `plan/02_research_route.md` §3.5 / §7 / §9 group D.
> All numbers below were produced in this session by `manuscript/scripts/mechanism_winall.py`,
> `manuscript/scripts/build_table6_company_panel.py` and `manuscript/scripts/fig5_mechanism.py`,
> run on `evidence/data/analysis_rice_channel.pkl`, `evidence/company_panel.csv`,
> `evidence/05_competitor_financials.csv`, `evidence/04_order_grain_timeseries.csv` and
> `evidence/01_company_financials.md`. Every reproduction below is reported as an *independent
> re-run*, not a byte-for-byte replication of the numbers already quoted in `01_theme_and_innovation.md`
> — the two sometimes diverge in the second decimal or in significance because the exact cell
> construction (which trial groups are pooled, which years are included) is under-specified in the
> plan text and had to be reconstructed here. Divergences are reported, not hidden.

**Role statement (must appear verbatim in the mechanism section, per W2):**
*"Winall enters this paper as a counter-case that rules out an alternative explanation, not as a
source of the main result."*

---

## 1. Channel-choice Logit — does Winall disproportionately use the unified (old) channel?

**Descriptive replication (exact match to `01_theme_and_innovation.md` Increment C):**
Restricting to national-level approvals in 2017 and 2019–2022 (all trial groups, not only the two
major indica groups), Winall-linked records number **n = 166**, of which **60.2%** went through the
Unified channel; all other applicants number **n = 1,101**, of which **47.5%** went through Unified.
This reproduces the plan's headline numbers exactly.

**Logit, `Pr(NewChannel) = Λ(α·Winall + year×trial_group FE)`,** same sample (national, all trial
groups, 2017 + 2019–2022, n = 1,246 after dropping year×trial_group cells with no variation):

| Spec | n | α (Winall) | SE | p | Odds ratio |
|---|---|---|---|---|---|
| Logit with year×trial_group FE (all national trial groups) | 1,246 | **−0.728** | 0.182 | <0.0001 | 0.483 |
| Logit with year×trial_group FE (two major indica groups only) | 849 | −0.558 | 0.201 | 0.005 | 0.572 |
| Logit, no FE (all national trial groups) | 1,267 | −0.516 | 0.170 | 0.002 | 0.597 |

α is negative and significant throughout: conditional on year and trial group, being Winall-linked
roughly halves the odds of entering through a new (Consortium/Green) channel relative to the Unified
channel. This is the same direction as the descriptive 60.2%-vs-47.5% comparison and confirms it
survives a year×trial-group fixed-effects adjustment. Full output: `manuscript/tables/table5b_winall_channel_choice_logit.csv`.

**What this does *not* show:** channel choice is not randomly assigned to firms; α says Winall's
*realised* channel mix is more Unified-heavy than the rest of the sample in the same year and trial
group, not that Winall would have chosen differently under some counterfactual policy.

---

## 2. Within-channel positioning — is Winall's advantage confined to the old channel?

**Specification:** `Y = ρ·Winall + cell FE (year×trial_group×check) + seed-system FE`, estimated
separately within the Unified subsample and within the New (Consortium+Green) subsample, national
approvals, 2017 + 2019–2022, cells clustered SE.

| Subsample | Outcome | ρ | SE | p | n |
|---|---|---|---|---|---|
| **Unified** | Head-rice % (third-party) | **+2.212** | 0.593 | 0.0002 | 495 |
| **Unified** | Quality grade stated, 0/1 (third-party) | **+0.098** (9.8 pp) | 0.028 | 0.0004 | 501 |
| **Unified** | Chalkiness % (third-party) | **−0.692** | 0.188 | 0.0002 | 494 |
| New (Consortium+Green) | Head-rice % | −0.452 | 0.752 | 0.548 | 494 |
| New (Consortium+Green) | Quality grade stated | +0.045 (4.5 pp) | 0.034 | 0.184 | 503 |
| New (Consortium+Green) | Chalkiness % | +0.200 | 0.446 | 0.655 | 495 |

**Comparison with the plan's target numbers** (head-rice +2.224 p<0.0001, quality grade +9.7pp
p=0.0014, chalkiness −0.498 p=0.058, all within the Unified subsample): the head-rice (+2.212 vs
+2.224) and quality-grade (+9.8pp vs +9.7pp) coefficients reproduce almost exactly; the chalkiness
coefficient reproduces in direction and is of similar magnitude (−0.692 vs −0.498) but comes out
*more* significant here (p=0.0002 vs the plan's p=0.058) — a difference attributable to which trial
groups and which exact cell definition is pooled, not to a different substantive finding. In all
three outcomes, **the Winall-vs-others gap inside the Unified channel points toward better
third-party-measured quality, and it disappears (all p>0.18) inside the new-channel subsample.**
Full output: `manuscript/tables/table5_winall_positioning.csv`; Fig. 5(b).

**Reading, and its negative-fact anchor (per W4):** if "the new channel looks worse" were driven by
"enterprises are less careful than public breeding institutes," the most integrated seed-marketing
enterprise in the sample should look most like the new-channel entrants. It does not: Winall is both
more likely to use the old channel and, when it does, to outperform other Unified entrants on
third-party-measured grain quality. **This pattern coexists with, and does not offset, the fact that
Winall's own order-grain trading business ran roughly break-even to negative gross margin in
2024–2025 (about 2.66% in 2024, falling to −0.09% in 2025H1 and −1.31% for full-year 2025), that the
company's 2025 attributable net profit was −212 million CNY (a swing from profit to loss), that its
2024 annual report received a qualified (non-clean) audit opinion, and that in 2026 it was fined
300,000 CNY for false statements in that report and its stock short name was changed to ST Winall.**
The quality-side finding is about which trial channel a variety entered through, not about whether
Winall's overall business model is financially sound — the two are separate claims and must stay
adjacent in text, not sequential chapters.

---

## 3. R10 robustness — does the main arm-1 result survive dropping all Winall records?

**Specification:** identical to the arm-1 main spec (`Y = β·NewChannel + cell FE + seed-system FE`,
Consortium vs Unified, national, two major indica trial groups, 2019–2022), re-estimated after
dropping every Winall-linked record and re-dropping any cell left with no channel variation
(n = 609, down from 720 with Winall included).

| Outcome | β | SE | p | n |
|---|---|---|---|---|
| Head-rice % | **−1.368** | 0.494 | 0.0057 | 602 |
| Chalkiness % | **+0.940** | 0.443 | 0.0338 | 599 |
| Quality grade stated (0/1) | **−0.104** (−10.4 pp) | 0.041 | 0.0106 | 609 |

**Comparison with the plan's target numbers** (head-rice −1.200 p=0.019, chalkiness +1.050 p=0.041,
quality grade −11.6pp p=0.016): all three coefficients reproduce closely in sign and magnitude, and
all three remain statistically significant at conventional levels after Winall is entirely removed.
**This confirms W3: the main result's immunity to dropping the focal firm is directly demonstrable
and belongs in a main-text table, not an appendix.** Full output:
`manuscript/tables/table_r10_drop_winall_robustness.csv`.

---

## 4. Enterprise vs Public research institute — descriptive trait division of labour (Table 7)

**Specification:** `Y = θ·Public + year×trial_group FE + seed-system FE`, national approvals, two
major indica trial groups, years with a non-missing `applicant_type` label (Public or Enterprise
only; Joint and Unknown excluded).

| Outcome | θ (Public − Enterprise) | SE | p | n |
|---|---|---|---|---|
| Regional-trial yield (kg/mu) | +4.18 | 1.89 | 0.027 | 408 |
| 1000-grain weight (g) | +1.19 | 0.40 | 0.003 | 411 |
| Chalkiness (%) | +1.01 | 0.61 | 0.100 | 411 |
| Head-rice (%) | −1.22 | 0.67 | 0.070 | 411 |

**Comparison with the plan's target numbers** (yield +3.18 p=0.035, TGW +0.96 p=0.025, chalkiness
+0.94 p=0.066, head-rice −0.84 p=0.114, n=632): this run's sample (n=408–412) does not reach n=632
under any sample construction tried here (two-indica-groups-only with Public/Enterprise labels,
2005–2022, gives n≈480–602 depending on whether "Joint" applicants and 2023–2025 years are
included) — the exact filter behind the plan's n=632 could not be reverse-engineered from the
variable-definition table alone, and **this discrepancy is flagged rather than papered over.** All
four coefficients, however, reproduce the same **direction and rough order of magnitude** as the
plan's numbers (Public institutes show higher yield and 1000-grain weight, worse — i.e. higher —
chalkiness, and worse — i.e. lower — head-rice, relative to Enterprise applicants), and land in the
same marginal-significance band (yield and TGW clearly significant; chalkiness and head-rice at
p≈0.07–0.10, not significant at conventional 5% level for two of the four outcomes).

**Per Non-claim #9 in `01_theme_and_innovation.md` §8, this table is reported strictly as a
descriptive, direction-only background fact, not as a conclusion about which institution type
"is better."** Output: `manuscript/tables/table7_enterprise_vs_public.csv`.

---

## 5. Table 6 — Winall and comparator listed seed-company panel

Built in `manuscript/scripts/build_table6_company_panel.py` from `evidence/company_panel.csv`
(Winall FY2015–2025 plus a 2026Q1 memo row) and `evidence/04_order_grain_timeseries.csv` (order-grain
segment detail), joined with `evidence/05_competitor_financials.csv` for nine comparator listed seed
companies (Longping High-Tech, Denghai Seed, DBN, Guotou Fengle, Shennong, Kenfeng, Nongfa,
Dunhuang, Wanxiang Denong), mostly available only as a single 2025 (or, for two companies, a
2024/2025-labelled but otherwise unfound) cross-section rather than a full 2015–2025 run — this
asymmetry (one company with an 11-year panel, nine with essentially one snapshot each) is itself
part of what the table must show honestly, not something to paper over by inventing missing years.

Saved: `manuscript/tables/table6_company_panel.csv` (21 rows: 11 Winall annual rows 2015–2025 + 1
Winall 2026Q1 memo row + 9 comparator rows).

**Observed vs. estimated (推算) flagging.** A `value_type_order_grain` column marks every
order-grain revenue/share/margin cell drawn from `04_order_grain_timeseries.csv` as either
`observed` or `estimated (推算) — see note`. The rows flagged as estimated are:

| Year | Order-grain revenue (100M CNY) | Share of revenue (%) | Gross margin (%) | Basis for the flag |
|---|---|---|---|---|
| 2021 | 7.24 (推算) | 28.73 | 7.6 | Revenue itself back-solved from 2022's reported YoY growth; share/margin from Xie et al. (2023) |
| 2022 | 8.94 (推算) | 25.6 (推算) | n/a | Back-solved from the 2023 annual report's stated YoY change in "order-farming" (订单农业) revenue |
| 2023 | n/a | 17.2/20.1 (推算) | 4.89 (observed) | Two overlapping business-scope definitions ("order grain" vs "order farming") give two different share estimates |
| 2024 | n/a | 25.3 (observed, cited) | 2.66 (推算) | Margin back-solved from the 2025 annual report's stated point-change vs. the prior year |

**2025H1 gross margin of approximately −0.09%** (order-grain segment) is drawn from a February 2026
Jiemian ("界面新闻") article summarising the 2025 interim report, confidence "中" (medium) because
the underlying interim-report PDF itself was not directly re-opened in this session. It is distinct
from, and must not be conflated with, the **full-year 2025** order-grain gross margin of **−1.31%**,
which comes directly from the 2025 annual report (confidence "高").

---

## 6. Negative-fact timeline — verification and precision flags

Full table: `manuscript/tables/table_negative_facts_timeline.csv`. Summary of verification status:

| # | Claim as stated in the brief | Verified? | Precision issue found |
|---|---|---|---|
| 1 | Order-grain gross margin ≈ −0.09% | **Verified, but imprecise** | The −0.09% figure is the **2025H1 (interim)** margin, not a full-year or generic figure. Full-year 2025 margin is −1.31%. Any sentence using "−0.09%" must say "2025 上半年" / "2025H1" explicitly. |
| 2 | 2025 attributable net profit −2.12亿元, swing to loss | **Verified**, high confidence | Matches the 2025 annual report directly (−317.91% YoY, swing from profit to loss). |
| 3 | 2024 annual report received a qualified audit opinion | **Verified**, high confidence | Confirmed as "保留意见" tied to receivables/inventory audit-scope limitations; the full text of the qualification paragraph was not independently re-opened. |
| 4 | 2026 fined 300万元 for false statements, renamed ST Winall | **Verified**, high confidence | Fine and cause (under-provisioned credit-impairment losses of 18.7151M CNY, 10.86% of disclosed profit) confirmed; two dates apply — 2026-06-26 (penalty/media report) and 2026-06-30 (short-name change effective date) — both should be cited, not collapsed into one. |
| 5 | 2025-12 China Seed Group tender offer, up to 40.51% | **Needs a date correction** | The first public announcement was **2025-11-20**, not December; the formal tender offer report is dated 2025-12-03, a further shareholder report 2025-12-22, the tender period ran 2025-12-04 to 2026-01-05, and the 40.51% stake was reached only **after** the tender period closed, i.e. around **2026-01**. "2025-12 tender offer, 40.51%" conflates several distinct dates spanning Nov 2025–Jan 2026; the manuscript should either cite 2025-11-20 (first announcement) or spell out the full date range, and should say "待确认具体完成日期的月份" only if a single completion date is needed but not found — here it *is* findable (≈2026-01) and should be used rather than "2025-12." |

No claim in this list was found to be fabricated or unsourced; the correction needed is entirely one
of **date precision**, not of substance.

---

## 7. Figure 5 (three-panel mechanism figure)

Saved: `manuscript/figures/fig5_winall_mechanism.png` (built by `manuscript/scripts/fig5_mechanism.py`).

- **(a)** Winall's national-approval share by year (right axis, line) and channel composition of its
  own records (left axis, stacked bars: Unified / Consortium / Green), 2015–2024. Confirms the Green
  (2017-only) and Consortium (2019–2022-only) channels do not overlap in time.
- **(b)** Forest plot of the Table 5 within-channel coefficients (§2 above), split into the Unified
  subsample (filled circles) and the New-channel subsample (filled squares), with 95% CI. Visually
  shows the gap collapsing to statistical indistinguishability from zero once outside the Unified
  channel.
- **(c)** Order-grain revenue share (left axis, orange) and R&D intensity (right axis, blue) by year;
  **hollow orange markers mark the 2021/2022/2023/2024 estimated (推算) points** per the Table 6
  flagging above; a red dotted vertical line marks 2025 (net loss) and a dark-red dash-dot line marks
  2026-06 (fine and ST renaming).

---

## 8. Statements this analysis does **not** support (must not appear in the mechanism section)

Per `01_theme_and_innovation.md` §8 Non-claims and §7 W1–W7, and confirmed by the results above:

1. **No causal or "mechanism" claim.** ρ and α are within-cell composition comparisons ("Winall
   entrants vs. other entrants in the same year×trial-group×channel cell"), not the effect of any
   intervention on Winall or on the sector. The word "mechanism" in this section's title refers to
   the *identification argument* (ruling out the "enterprises are more careless" alternative
   explanation), not to a causal channel being estimated.
2. **No "ranked by integration depth" rhetoric (W6).** This analysis says nothing about how Winall
   compares to other *vertically integrated* seed enterprises specifically — it compares Winall to
   *all* other applicants pooled together. `00_decision_log.md` §2.2 (BD-3) already shows a placebo
   test in which a non-integrated firm (Hunan Xiwang) displays a larger quality tilt than Winall;
   this section must not imply or restate any ordering by integration depth.
3. **No profit/output monetisation of the regression coefficients (W5).** None of the coefficients in
   §1–§4 are converted into implied revenue, processing value, or cost savings for Winall or any
   comparator company.
4. **No claim that Winall's quality strategy is financially successful.** The opposite is explicitly
   documented in §2 and §6 above: negative-to-break-even order-grain margins, a 2025 net loss, a
   qualified audit opinion, and a 2026 fine and ST designation. "Better third-party-measured grain
   quality within the Unified channel" and "financially troubled order-grain segment" are two
   separate, simultaneously true facts about the same company, and are reported together here per W4.
5. **No claim that this section's regressions are the paper's main result.** Per W1, the entire
   Winall-related content (this note plus Table 5/5b/6/negative-facts-timeline plus Figure 5) is
   meant to occupy at most one mechanism section, one figure and one main table in the final
   manuscript — consistent with the ≤15%-of-paper budget in W1. The main arm-1/arm-2 channel-gap
   result (not covered by this note) does not depend on Winall and remains significant after Winall
   is dropped entirely (§3 above).
6. **No claim that the n=632 Table 7 sample was exactly reproduced.** As flagged in §4, this run's
   Enterprise-vs-Public sample (n≈408–412 under the most natural filter) does not match the plan's
   stated n=632 exactly; the direction and approximate magnitude of all four coefficients do match,
   but the exact sample filter behind n=632 is **not fully documented in the available plan files**
   and should be reconciled against the original script before the manuscript is finalised.
7. **No claim about a single, precise date for the tender offer's completion at 40.51%** beyond
   "around 2026-01" (§6, item 5) — the exact settlement date was not directly located in the evidence
   files and is marked "待确认具体日期" for that one sub-detail (the announcement, report, and tender
   window dates themselves are all precisely sourced).
