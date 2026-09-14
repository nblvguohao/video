# Referee report R1 — Technical rigour and data credibility

Manuscript: "Who measures what enters the market? Self-organised variety trials and the
third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"
(`manuscript_v1.md`)

Scope of this report: statistical/data support for claims, completeness of reported
statistics, treatment of public-data bias/endogeneity, generality of the single-firm
(Winall) case, and cross-document numerical consistency (per `integration_log.md` and
`plan/02_research_route.md`).

---

## Overall assessment

This is an unusually self-policing manuscript: the empirical design (year × trial-group ×
check fixed effects), the explicit "composition effect, not treatment effect" framing, the
15-item robustness battery, and the extensive Non-claims section (§4.7) meet or exceed what
this reviewer would expect from a paper working with observational, third-party-aggregated
administrative text. The headline result (Arm 1: head-rice −1.844 pp, chalkiness +1.108 pp,
stated-grade −0.122, all with CI, p, n and clustering method reported; Table 3) is
well-identified within its own stated scope and survives the checks that have power to test
it (BH-FDR, randomisation inference, dropping Winall, variety-level clustering, extending
trial groups). However, the manuscript is not yet submission-ready on strictly technical
grounds: one section's numbers do not match the underlying computed data file that is cited
as its source (Table 7 / Non-claim 8 / §7), a table the Data section relies on (Table 2) is
an unpopulated placeholder, a promised robustness check for `quality_stated` is referenced
but never actually appears in the Robustness section, and the foundational data-verification
step (manual cross-check against original MARA text) remains undone. None of these is fatal
to the paper's central claim, but each is a concrete, fixable technical failing rather than a
matter of framing or emphasis.

## Major strengths

1. **Statistical reporting is essentially complete** for the headline results: every
   Table 3 row carries β, SE, 95% CI, p, BH-q, n, and an explicit clustering/SE-type tag
   (`cluster(cell,G=10)` for Arm 1, `HC1(cells=2)` for Arm 2). This is verified directly
   against `tables/table3_main_results.csv`, and the in-text numbers in §5.2–5.3 match the
   CSV to reported precision (e.g. head-rice β = −1.844094, CI [−2.636, −1.052], p =
   5.08×10⁻⁶, n = 742, matching the text exactly).
2. **The sign-separation identification argument is stated with its own limits attached**
   (§4.5, §5.4): H_measure vs. H_threshold are explicitly acknowledged as observationally
   equivalent given this data, and the within-applicant test's inability to adjudicate is
   quantified via minimum detectable effect (MDE), not merely asserted as "underpowered."
   This is good practice rarely seen in observational-composition papers.
3. **Adverse and inconvenient results are kept in the main text, not banished to an
   appendix**: bacterial-blight resistance moving the *opposite* direction (§5.2, C7),
   Arm 2's reversed production-trial yield-gain sign (§5.3), the non-significant provincial
   replication for 3 of 4 outcomes (§6.11), and the inconclusive chained-check ladder (§6.14)
   are all reported with their numbers rather than summarised away.
4. **R10 (drop Winall) is numerically identical across the two places it is cited.** I
   independently checked `tables/table_r10_drop_winall_robustness.csv` against both §6.9 and
   §7: head-rice −1.368 pp (p = 0.006, n = 602), chalkiness +0.940 pp (p = 0.034, n = 599),
   stated grade −0.104 (p = 0.011, n = 609) appear identically in both places and match the
   CSV (β = −1.3676/0.9399/−0.10449, p = 0.00566/0.03381/0.01059) to the reported rounding.
   This specific cross-chapter consistency check (requested in the review brief) **passes**.
5. **Manski bounds are used to actually downgrade a result**, not just to pad the robustness
   section: `quality_top2`'s bound [−0.253, +0.088] crosses zero and the paper explicitly
   demotes it to secondary (§6.6), consistent with `table3` and the plan document's R7 row.
6. **The single-firm (Winall) generalizability problem is handled about as well as it can
   be for an n = 1 case study**: the role is repeatedly and explicitly scoped as a
   "counter-case that rules out an alternative explanation, not a source of the main result"
   (§1, §7 opening line, §7 closing paragraph, §9), R10 shows the headline gap survives
   dropping all Winall records, and a 5-comparator financial panel is used only descriptively
   (Table 6). This satisfies the "is single-case generality bounded" check.

## Major concerns

1. **Table 7 / Non-claim 8 / §7 numbers do not match the underlying data file
   (`tables/table7_enterprise_vs_public.csv`), and the integration log resolved this
   conflict by preferring a planning-note prose figure over the actual computed table.**
   The manuscript (Non-claim 8 in §4.7, and §7's descriptive paragraph, verbatim identical
   in both places) states: regional-trial yield +3.18 kg/mu (p = 0.035), 1000-grain weight
   +0.96 g (p = 0.025), chalkiness +0.94 (p = 0.066), head-rice −0.84 (p = 0.114), n = 632.
   The CSV that Table 7 is sourced from gives: yield θ = 4.179 (p = 0.0273, n = 408), TGW
   θ = 1.193 (p = 0.00301, n = 411), chalkiness θ = 1.0099 (p = 0.100, n = 411), head-rice
   θ = −1.2196 (p = 0.0701, n = 411). Two of the four statistics printed in the manuscript
   (yield, TGW) match almost exactly the version `integration_log.md` §10 explicitly
   *rejected as erroneous* (mechanism.md's original +4.18/p=0.027, +1.19/p=0.003), not the
   version it adopted. The other two (chalkiness, head-rice) match neither version cleanly.
   `integration_log.md`'s stated reason for its choice — agreement with `02_research_route.md`
   §5's C11 risk-register entry and `00_decision_log.md` — treats a planning note as more
   authoritative than the actual regression output file that the published Table 7 claims to
   summarise. This is backwards: a CSV generated from `analysis_rice_channel.pkl` is data; a
   risk-register entry is a plan. Whichever number is correct must be re-derived from the
   actual regression code and reconciled with the table file before submission; as it stands,
   a spot-check of the manuscript against its own cited table fails for a Results-adjacent
   claim used in both the Non-claims section and the Mechanism section (i.e., this is not a
   one-off typo confined to a single sentence).
2. **Table 2 (descriptive statistics and balance) is not actually a table — it is an
   explicit placeholder**, per `tables/table2_descriptive_balance.md`'s own header ("not yet
   rendered as a formatted table with means and standard deviations... this placeholder
   exists so the Data section can cite 'Table 2' without asserting numbers not yet computed").
   Yet `manuscript_v1.md` §3.3 and `figure_table_list.md` both cite it as an assembled
   descriptive/balance table with means, SDs and missing rates for all 17 outcomes. A reader
   who follows the citation gets a construction memo, not a table. This must be rendered
   before submission; it is currently a documented but unresolved gap between what the prose
   claims exists and what has been produced.
3. **A specific promised robustness check is referenced but never delivered.** Data §3.3
   states: "we show in §6 that the [quality_stated] coefficient survives, and in fact
   strengthens, once announcement text length and the count of non-missing fields are
   controlled for." I read all of Section 6 (§6.1–6.15, covering R1–R15 in full) and found no
   such check — no mention of announcement text length, field-count controls, or a
   strengthened quality_stated coefficient anywhere in the Robustness section. This matches a
   specific mitigation the risk register promised for K4 (`02_research_route.md` §8: "报告控制
   公告文本长度（−13.5 字，p=0.078）与非缺失字段数后系数增强至 −0.169(p=0.0001)"), which was
   apparently planned but not actually written into any of the twelve section files that were
   merged. This is a forward reference to evidence that does not exist in the manuscript as
   assembled — it should be added as an explicit R16/appendix to the Robustness section, or
   the promissory sentence in §3.3 must be removed or rewritten to describe what §6 actually
   contains.
4. **The foundational data-verification step is still outstanding and this bears on every
   number in the paper, not just a subset.** §3.4 states plainly that the manual field-by-
   field cross-check of parsed records against original MARA announcement text "remains
   outstanding" and reports no agreement-rate figure (flagged as Unresolved item P4). Because
   every substantive variable in this paper (channel, trial group, check, all 17 outcomes) is
   extracted by regex from a third-party re-transcription (`he-zhui/Rice_QA`) rather than from
   MARA's own archive, this is not a routine caveat — it is the single largest open threat to
   the paper's factual claims, and the manuscript is correct to flag it as blocking rather than
   cosmetic. It must be completed, with a reported agreement rate, before this paper can be
   assessed as evidentially sound; I cannot independently verify parsing accuracy from the
   repository as provided.
5. **Arm 2 (Green vs Unified, 2017) rests on only 2–3 effective identifying cells (n =
   119), and several Arm 2-only estimates (e.g., duration_d β = −2.46, p = 3.4×10⁻⁹; amylose
   β = −1.52, p = 0.0009; gel consistency β = −6.56, p = 0.0003) are reported with very small
   p-values from a design with essentially no cluster structure to support asymptotic
   cluster-robust inference — the paper substitutes HC1 for cluster-robust SEs here (correctly
   disclosed), but HC1 with 2–3 fixed-effect cells absorbing most of a 119-row sample's
   variation is still a fragile basis for point estimates this precise. The paper is honest
   that Arm 2 is "small-sample" throughout, but readers should not treat any Arm-2-only p-value
   below the extremely well-powered Arm-1 p-values as comparably reliable, and the manuscript
   could be more explicit that Arm 2's HC1 SEs assume correctly specified functional form with
   no adjustment for the small number of clusters (no wild-cluster bootstrap or similar was
   attempted).
6. **The public-data endogeneity/coverage caveats are well-disclosed where they concern
   coverage (post-2022 decline, §3.1/§3.4) but the channel-choice endogeneity itself
   (applicants self-select into channel) is acknowledged in words throughout but never
   quantified beyond the underpowered within-applicant test.** This is a genuine data
   limitation rather than a writing failure — the paper says as much (§4.7, "we do not claim
   to have [separated selection from effect]") — but it means the paper's strongest possible
   claim really is the composition-effect claim it makes, not anything stronger, and a referee
   should confirm the title/abstract/conclusion never drift into causal language. On this
   specific check: they do not — I found no instance of "effect of," "causes," or "impact of"
   applied to the channel variable in the text I read (abstract, §1, §4.4, §9); this is
   correctly disciplined throughout.
7. **Cross-arm/cross-section 0.019 vs 0.020 rounding inconsistency (minor):** §5.2 reports
   the regional-trial yield-gain p-value as p = 0.019 (matching the CSV's 0.0189285 correctly
   rounded), while §4.5 and `02_research_route.md` §3.4 both report the same coefficient with
   p = 0.020. This is a trivial rounding slip, listed here only because the review brief asked
   for numeric-consistency checking; it does not affect any substantive conclusion and can be
   fixed in a final numbers pass.

## Technical failings that must be addressed

- Resolve the Table 7 / Non-claim 8 / §7 numeric conflict against the actual regression
  output (not a planning-note figure) and update every place the four statistics appear
  (Non-claims §4.7, Mechanism §7, Table 7 itself, and `figure_table_list.md`'s description).
- Render Table 2 as an actual table of means/SDs/missing rates; it cannot remain a
  construction memo in a manuscript that cites it as a completed descriptive table.
- Either write the promised text-length/field-count robustness check for `quality_stated`
  into Section 6, or remove the forward reference in §3.3 that currently points to nothing.
- Complete the MARA-announcement cross-check (§3.4/P4) and report the resulting agreement
  rate; until then, no number in this paper can be certified as free of transcription error
  at a known rate.
- Reconcile, or at minimum flag more prominently in the main text (currently only in §6.11's
  prose), the unexplained discrepancy between this session's provincial-replication sample
  (n = 495, Unified 352) and an earlier n = 452 (Unified 318) run with a different head-rice
  coefficient (−0.134 vs the current run's own reported values) — the paper discloses this but
  a referee will want to know which run is the one being defended.
- Trim toward the journal's stated 8,000–10,000-word guideline (current draft ≈14,000 words
  per `integration_log.md` §12) and resolve the Fig. 1–7-vs-6-target and table-count mismatch
  flagged in `figure_table_list.md` before submission; this is a completeness rather than a
  correctness issue but will block desk acceptance.
- Add the ten mandatory-list citations that were verified as real but never cited
  (`integration_log.md` §8), particularly Lu et al. 2024, Hang et al. 2024 and Gong et al.
  2026 on rice-quality trait trends, which bear directly on the structural-break dating claim
  in §5.6/§8.2 and are currently missing from a claim about pre-2016 quality trends that a
  referee would expect this literature to engage with.

## Assessment against journal criteria

- **Internal statistical validity**: strong for Arm 1 (adequately powered, full CI/p/n/
  clustering reporting, FDR-corrected, randomisation-inference-corroborated); weak-but-honestly-
  flagged for Arm 2 and the within-applicant/provincial subsamples (small samples, explicitly
  labelled and MDE-quantified rather than overclaimed).
- **Reproducibility/data provenance**: currently insufficient — the outstanding MARA
  cross-check (§3.4) and the Table 7/CSV mismatch (Concern 1) mean a diligent referee cannot
  yet confirm that the numbers in the manuscript are the numbers the underlying pipeline
  actually produces, which is a core journal requirement independent of the paper's framing.
- **Scope discipline (claims vs. evidence)**: excellent — the Non-claims section (§4.7) is
  unusually thorough and, on spot-check, accurately describes what the results do and do not
  support (verified against Table 3, R7, R9, R11 numbers directly).
- **Completeness for submission**: not yet met — placeholder Table 2, missing mandatory
  citations, word-count overage, and the Fig/Table compression target are all still open per
  the paper's own integration log.

## Recommendation

**Major revision** (equivalent to a "major revision, resubmit" journal decision — not
reject, not accept/minor). The empirical design and the paper's candor about its own limits
are genuinely strong and, once the items below are fixed, this could be a clean minor-revision
case. But three items are blocking on strictly technical grounds as submitted: (a) the
Table 7/Non-claim 8/§7 numeric mismatch against the underlying data file, (b) the unrendered
Table 2, and (c) the still-outstanding manual verification of the parsed corpus against
original MARA text, without which no number in the paper carries a known error rate. None of
these requires a new empirical strategy — they require finishing work already scoped in the
paper's own integration log and risk register — but none can be waved through as "cosmetic."

## Numbered major concerns (for cross-review synthesis)

1. Table 7 / Non-claim 8 / §7 figures conflict with `table7_enterprise_vs_public.csv`; the
   integration log's resolution favoured a planning note over the actual computed table.
2. Table 2 (descriptive/balance) is an unrendered placeholder cited as a completed table.
3. A promised robustness check for `quality_stated` (text-length/field-count control) is
   referenced in §3.3 but absent from Section 6 as assembled.
4. Manual cross-check of parsed records against original MARA announcements (§3.4/P4) is
   still outstanding; no agreement rate is reported.
5. Arm 2's very small effective cluster count (2–3 cells, n = 119) supports some
   highly-precise-looking p-values that should be read with more caution than the text
   currently signals.
6. Unreconciled provincial-replication sample discrepancy (n = 495/Unified 352 vs. an earlier
   n = 452/Unified 318 run) is disclosed but not resolved.
7. Manuscript exceeds the target word count (~14,000 vs. 8,000–10,000) and the stated
   figure/table compression targets are not met by any current plan.
8. Ten format-spec-mandatory citations, several directly relevant to the structural-break/
   quality-trend claim, are verified as real but not cited anywhere in the drafted text.

## Unsupported claims

- Data §3.3's statement that the `quality_stated` coefficient "survives, and in fact
  strengthens" to a specific value (implied ≈ −0.169, p = 0.0001, per the risk register) once
  announcement length and non-missing-field-count are controlled for **cannot be verified in
  this manuscript** — the check does not appear in Section 6 as written, so this is currently
  an unsupported forward-reference rather than a demonstrated result.
- The four enterprise-vs-institute statistics repeated identically in Non-claim 8 (§4.7) and
  in §7 (+3.18 kg/mu p=0.035; +0.96 g p=0.025; +0.94 chalkiness p=0.066; −0.84 head-rice
  p=0.114) are **not supported by the table file cited as their source**
  (`tables/table7_enterprise_vs_public.csv`), which reports materially different values for at
  least two of the four (yield +4.18 vs +3.18; TGW +1.19 vs +0.96). This claim should be
  treated as unverified until the discrepancy is resolved against the regression code.
