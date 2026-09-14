# Integration log — manuscript_v1.md

Scope: merges `manuscript/sections/{front_matter, introduction, institutional_background,
data, empirical_strategy, results, robustness, robustness_chained_check, mechanism,
discussion, conclusion, declarations}.md` into `manuscript/manuscript_v1.md`, per the section
order in `plan/04_format_spec.md` §1 and the figure/table numbering in
`plan/02_research_route.md` §7. No claim, number, Non-claim, robustness failure, or piece of
conflicting evidence was removed or softened. Every change below is either (a) a structural/
numbering fix required for internal consistency, (b) a citation-format fix, or (c) a
documented, non-silent resolution of a cross-section factual conflict (§5).

## 1. Section reordering inside Results (numbering-order fix)

`results.md` originally ordered its subsections as: 5.4 Identification argument → **5.5
Structural breakpoints (cites Fig. 4)** → **5.6 Channel composition and convergence over time
(cites Fig. 3)** → 5.7 Summary. Because Fig. 3 (event study) must, by `02_research_route.md`
§7's numbering, be cited before Fig. 4 (breakpoint scan), citing Fig. 4 in §5.5 before Fig. 3
in §5.6 violated `04_format_spec.md` §5's requirement that "正文首次提及顺序须与编号顺序一致"
(first-mention order must match numbering order).

**Fix**: swapped the two subsections. The merged manuscript now reads 5.4 → **5.5 Channel
composition and convergence over time (Fig. 3)** → **5.6 Structural breakpoints (Fig. 4)** →
5.7 Summary. No sentence was reworded beyond the section-number labels and the internal
cross-references listed in §2 below; the two subsections were independent enough that
reordering them changes no argument.

## 2. Figure renumbering: Mechanism vs. Robustness (numbering-order fix)

`02_research_route.md` §7 assigns Fig. 5 to the Winall mechanism three-panel figure and Fig. 6
/ Fig. 7 to the randomisation-inference and missingness-balance figures in the Robustness
section. But `04_format_spec.md` §1 fixes the section order as Results → **Robustness**
(§6) → **Mechanism** (§7) — i.e. the Robustness section, and its Fig. 6/7, appear in the
manuscript *before* the Mechanism section and its Fig. 5. Following the plan's original
numbers verbatim would have made Fig. 6 and Fig. 7 the first-cited figures and Fig. 5 the
last-cited of the three, breaking ascending order.

**Fix**: renumbered so that first-mention order is ascending across the whole manuscript,
while preserving each figure's content:

| Content | Original number (per `02_research_route.md` §7 / source filename) | Published number in `manuscript_v1.md` |
|---|---|---|
| Randomisation-inference null distributions (R6) | Fig. 6 (`fig6_randomization.png`) | **Fig. 5** |
| Missingness-balance dumbbell plot (R8) | Fig. 7 (`fig7_missingness_balance.png`) | **Fig. 6** |
| Winall mechanism three-panel figure | Fig. 5 (`fig5_winall_mechanism.png`) | **Fig. 7** |

This is recorded in full, with the source-filename mapping, in `figure_table_list.md`. No
figure content, caption substance, or underlying number (R6/R8/mechanism) changed — only the
published Fig. number used in prose citations within `robustness.md` and `mechanism.md`.

## 3. A pre-existing numbering contradiction between plan documents (flagged, not resolved by fiat)

`02_research_route.md` §7 assigns Fig. 8 = Manski worst-case bounds plot and Fig. 9 = chained-
check ladder plot. `04_format_spec.md` §5 describes the same two figures in the **reverse**
order ("Fig. 8 对照阶梯不确定性图" = chained-check ladder; "Fig. 9 Manski 界图" = Manski
bounds). The two plan documents disagree with each other on which is Fig. 8 and which is Fig.
9. Per the task brief's instruction to use `02_research_route.md` §7 as the canonical figure
list, this integration follows `02_research_route.md`'s numbering (Fig. 8 = Manski, Fig. 9 =
chained ladder). Both figures are Supplementary-material candidates per the format spec and
are not cited by number in the main-text prose (the relevant robustness subsections, §6.6 and
§6.14, report the bound values and ladder diagnostics in prose without a figure citation), so
this discrepancy does not affect the main-text numbering fixed in §2 above, but it is flagged
here because whichever plan document guides the eventual Supplementary Material file names
will need this resolved explicitly, not silently picked.

## 4. Table-order fix in Data (§3.3)

The original `data.md` §3.3 closed with one sentence that named Table 3, then Table 2, then
Table 1, in that order — reading "...in Table 3 — is assembled in Table 2 (...); Table 1
reports...". Because this is the first mention of Table 2 and Table 3 in the manuscript, and
Table 1 numbering must precede Table 2 which must precede Table 3, this sentence order broke
first-mention order.

**Fix**: reordered the sentence to introduce Table 1, then Table 2, then Table 3, without
adding or removing any factual content.

## 5. Missing figure/table citations added

Several figures and tables specified in `02_research_route.md` §7 were never cited by number
in any section file, even though the section prose describes exactly their content. Per the
task brief, these were added as in-text citations (no new numbers, data, or claims — only a
"(Fig. X)" / "(Table X)" tag next to prose that already existed):

- **Fig. 1** (channel-stacked area chart) — added in `data.md` §3.1, where the 2018
  channel-label gap and year-by-year channel counts are already discussed, and again in the
  Table 1/Table 2 sentence in §3.3.
- **Table 7** (enterprise-vs-institute descriptive comparison) — added in `mechanism.md`'s
  closing descriptive-background paragraph, which already reports exactly the trait-division
  numbers `02_research_route.md` §7 attributes to Table 7. **Not** added to
  `empirical_strategy.md` §4.6, which introduces the same comparison in general terms before
  Table 4, 5 and 6 have been cited — citing Table 7 there would have put it before Tables
  4–6 in first-mention order, which are cited later in the merged manuscript (Robustness §6,
  Mechanism §7).
- **Table 5 and Fig. 7(a, b)** (Winall channel composition and within-channel positioning) —
  added in `mechanism.md`'s second paragraph (channel-choice and within-channel outperformance
  results), which already reports the underlying 60.2%/47.5% and trait-positioning numbers.
- **Table 6 and Fig. 7(c)** (Winall financial/R&D panel) — added in `mechanism.md`'s financial-
  facts paragraph, which already reports the underlying margin, net-profit, audit-opinion,
  fine and ST-designation facts.

## 6. `robustness_chained_check.md` was not concatenated separately

The task brief asked us to check whether `robustness.md` already embeds the R15 chained-check
sub-section and, if not, splice `robustness_chained_check.md` in. **It already does**:
`robustness.md`'s §6.14 ("A chained-check genetic-gain scale as an alternative yield metric
(R15)") is, on comparison, the same analysis, diagnostics, and conclusion as the standalone
`robustness_chained_check.md` file (same CV figures — median 1.56%, 90th percentile 3.32%,
maximum 5.40%; same +3.14%/+7.04% discrepancy; same 0.25–0.50%/yr range; same G = 6 clustering
caveat; same citations to Piepho et al. 2014, Laidig et al. 2014, Mackay et al. 2011, Raymond
et al. 2023, Piepho and Laidig 2024), reworded rather than copied verbatim, and already placed
in the robustness list where R15 belongs (§6.14, immediately before the robustness-matrix
summary). Concatenating `robustness_chained_check.md` as well would have duplicated this
content in the merged manuscript. It was therefore **not** included as a separate block in
`manuscript_v1.md`; only `robustness.md`'s own §6.14 (renumbered to keep its position, see §1
of this log — its position among R1–R15 was not moved) carries this check.

## 7. Internal cross-reference fixes made necessary by §1 and §2 above

Renumbering the Robustness subsections (§2) and swapping the two Results subsections (§1)
required updating every in-manuscript cross-reference that pointed to a robustness subsection
by number, so that each still points at the same *content* it did before the reorder:

| Reference (content it points to) | Location | Old number | New number |
|---|---|---|---|
| Manski worst-case bounds (R7) | `results.md` §5.2 (top-two grade caveat) | Section 6.4 | Section 6.6 |
| Bacterial-blight sign-separation discussion | `results.md` §5.2 | Section 4.4, 6.5 | Section 4.4, 6.6 |
| Placebo traits / plant height (R12) | `results.md` §5.2 | Section 6.7 | Section 6.8 |
| Within-applicant subsample (R9) | `results.md` §5.4 | Section 6.6 | Section 6.10 |
| Manski bounds, secondary flag reason | `robustness.md` §6.4 (R5/BH-FDR) | "Section 6.5 below" | "Section 6.6 below" |
| Manski bounds, RI cross-check | `robustness.md` §6.5 (R6, formerly §6.8) | "Section 6.5" | "Section 6.6" |
| Year-by-year event-study evidence | `robustness.md` §6.15 (matrix summary) | "Section 5.6" | "Section 5.5" |
| 2018 documentation gap / Table 1 | `robustness.md` §6.3 (R4) | "Section 5.5/Table 1" | "Section 5.6/Table 1" |

**Two of these were themselves pre-existing errors, independent of this integration's
renumbering**, and are flagged as such rather than silently absorbed into the mechanical
renumbering:
- `results.md` §5.2 originally pointed the Manski-bounds caveat to "Section 6.4" (the
  Benjamini–Hochberg subsection), when the Manski-bounds content was actually at the
  old §6.5. This looks like an authoring slip in the original `results.md` (wrong number by
  one), not something my reordering introduced. Corrected to point at the Manski-bounds
  content's new location (§6.6).
- `results.md` §5.4 originally pointed the within-applicant-subsample reference to "Section
  6.6" (the missingness-balance subsection), when the within-applicant test was actually at
  old §6.10. Also an apparent pre-existing slip, corrected to point at §6.10 (unchanged
  position; only the label was wrong before).

## 8. REF-tag citations converted to author-date form; reference list assembled

All `[REF: Author Year DOI]` bracket tags in `introduction.md`, `empirical_strategy.md`, and
`discussion.md` were removed; in every case the surrounding prose already carried a properly
formatted `(Author, Year)` or `Author (Year)` citation, so no rewording was needed beyond
deleting the bracket. One inline citation was added where a sentence would otherwise have lost
its citation entirely: `empirical_strategy.md` §4.2's reference to "the one existing evaluation
of this reform" now reads "...does (Xiang et al., 2025) — makes...".

**Only 11 of the ~21 references verified in `references_verified.md` are actually cited
anywhere in the 12 section files' body text**: Bar and Zheng (2019), Duflo et al. (2013),
Grennan and Town (2020), Laidig et al. (2014), Mackay et al. (2011), Piepho and Laidig (2024),
Piepho et al. (2014), Raymond et al. (2023), Renckens and Auld (2022), Xiang et al. (2025),
Zhao et al. (2022). The remaining ten works on `04_format_spec.md` §6's "本文必引文献清单"
mandatory-citation list — Xie et al. (2023), Lu et al. (2024), Hang et al. (2024), Gong et al.
(2026), Shi and Hu (2017), Qiu et al. (2016), Huang et al. (2018), Seck et al. (2023), Burris
et al. (2025), and Rangnekar (2000) — were verified as real, citable works by the reference
verifier but were **never actually cited in any of the 12 drafted section files**. Per the
brief's instruction not to introduce new claims or citations during integration, these were
**not** inserted into the manuscript body; only the 11 references actually cited appear in the
final `References` section. **This gap between the format spec's mandatory-citation list and
what the section-writing agents actually cited is flagged here for the author team** — several
of these (especially Lu et al. 2024, Hang et al. 2024, and Gong et al. 2026 on rice-quality
trait trends, which bear directly on the paper's structural-break and quality-trend claims)
likely belong in the Discussion or Introduction and were probably an oversight rather than a
deliberate omission, but adding them now would mean writing new sentences these individual
section agents did not author.

The three DOI/year corrections flagged in `references_verified.md` (Bar & Zheng 2019, not
2018, with pages 101(1):74–88; Renckens & Auld 2022, not 2020, with pages 16(2):500–518;
Grennan & Town's DOI 10.1257/aer.20180946, not the NBER working-paper DOI) were **already**
applied correctly in the section files' REF tags and inline citations before this integration
began — no correction was needed on this front; the References list uses the corrected forms.

One residual reference-list judgment call: Bar and Zheng (2019) was published in the
**American Journal of Agricultural Economics** (matching its DOI prefix `10.1093/ajae`);
an early draft of the assembled References list in this session briefly mistyped the journal
name as "Journal of Agricultural Economics" and this was caught and corrected before
finalizing `references.md`.

## 9. Terminology and formatting normalised

- **"Winall Hi-tech" → "Winall Hi-Tech"**: `mechanism.md`'s section heading used lower-case
  "Hi-tech" while every other mention of the firm across `introduction.md`, `robustness.md`,
  and `declarations.md` uses "Hi-Tech". Standardised to "Winall Hi-Tech Seed Co." at first
  mention (Introduction) and "Winall" / "Winall Hi-Tech" thereafter, matching the majority
  usage.
- Checked and found already consistent (no changes needed): "green channel" / "consortium
  trial" / "unified regional trial" as lower-case generic nouns throughout, versus "Green" /
  "Consortium" / "Unified" as capitalised regression-variable levels — this dual convention is
  used consistently across all 12 sections. Percentage-point notation ("percentage points"
  spelled out at first substantial use per section, "pp" abbreviated thereafter) and p-value/
  CI formatting (`p = 0.XXX`, `p < 0.XXX`, `95% CI [a, b]`, spaced consistently) were also
  already uniform across sections and required no changes.
- Removed process/QA scaffolding not appropriate for a submission-ready manuscript:
  `front_matter.md`'s "Source:" provenance note, "Title self-check" bullet list, the
  structured-abstract compliance note, the keyword and-of-check table, and the highlight
  character-count annotations; `declarations.md`'s "Source:" provenance note. No substantive
  content (title wording, abstract text, keyword list, highlight wording, declaration wording)
  was altered — only the meta-commentary describing how each was produced was removed.

## 10. Cross-section numeric conflict found and resolved (flagged per the brief, not silently picked)

**A genuine conflict between two sections reporting the same comparison with different
numbers**, found while integrating the mechanism section's descriptive background paragraph
on enterprise-vs-public-institution trait division of labour:

| Outcome | `empirical_strategy.md` §4.7 (Non-claim 8) | `mechanism.md` (original) | `02_research_route.md` §5 (C11) / `00_decision_log.md` |
|---|---|---|---|
| Regional-trial yield (public institutions vs. enterprises) | **+3.18 kg/mu, p = 0.035** | +4.18 kg/mu, p = 0.027 | +3.18 kg/mu, p = 0.035 |
| Thousand-grain weight | **+0.96 g, p = 0.025** | +1.19 g, p = 0.003 | +0.96 g, p = 0.025 |

Both `empirical_strategy.md` and `mechanism.md` describe the same underlying comparison (the
descriptive, non-causal enterprise-vs-institute trait split reported in Table 7, n = 632) but
give different point estimates and p-values for the same two outcomes.

**Resolution**: the manuscript now uses the `empirical_strategy.md` figures (+3.18 kg/mu,
p = 0.035; +0.96 g, p = 0.025) throughout, including in `mechanism.md`, which was edited to
match. **Reason for this choice**: these figures agree exactly, to three significant figures,
with the "实跑" (actual-run) numbers recorded independently in two planning documents —
`02_research_route.md` §5's risk-register entry C11 ("区试亩产 +3.18 kg/亩(p=0.035)、千粒重
+0.96 g(p=0.025)") and `00_decision_log.md`'s item on the same comparison — both of which
predate and are independent of either section draft. The `mechanism.md` figures (+4.18 kg/mu,
p = 0.027; +1.19 g, p = 0.003) do not match any planning document found in this repository and
are treated as the erroneous value. This is reported here rather than silently corrected
because it is exactly the kind of cross-section numeric conflict the integration brief asked
to be surfaced, not adjudicated invisibly. The chalkiness and head-rice figures in
`mechanism.md`'s version of this paragraph (+0.94, p = 0.066; −0.84, p = 0.114) were not
present in `empirical_strategy.md`'s version at all — these were retained from
`mechanism.md` because they match `02_research_route.md`'s C11 entry exactly and simply add
detail `empirical_strategy.md`'s shorter Non-claim sentence omitted, not because they
conflicted.

A second, smaller instance of imprecise cross-referencing (not a numeric conflict, but a
loss of precision) was also corrected: `mechanism.md`'s R10 paragraph originally summarised
the "drop Winall" robustness check with a single n ("n falls from 720 to 609") applied loosely
to all three outcomes, when `robustness.md`'s own R10 section (§6.9) reports three different,
outcome-specific sample sizes (n = 602 for head-rice, n = 599 for chalkiness, n = 609 for
stated grade). `mechanism.md` was edited to cite the same three outcome-specific n's as
`robustness.md`, rather than the single, only-sometimes-correct n = 609. The point estimates
and directions were already consistent between the two sections (differing only in decimal
rounding, e.g. p = 0.0057 vs. p = 0.006), so this was a precision fix, not a conflict
resolution.

## 11. Not changed / explicitly left as-is

- The genuine cross-arm inconsistencies documented within `results.md` (Arm 2's head-rice
  coefficient not significant unlike Arm 1's; Arm 2's production-trial yield gain reversing
  sign relative to Arm 1; Arm 2's regional-trial yield gain not estimable), all Non-claims in
  `empirical_strategy.md` §4.7, and every robustness check in `robustness.md` that qualifies or
  fails to support the headline result (R7's Manski-bound sign instability, R9's underpowered
  within-applicant subsample, R11's three underpowered provincial outcomes, R13's placebo, and
  R15's inconclusive chained-check ladder) are preserved verbatim in content and are not
  softened, reworded, or removed.
- The provincial-replication discrepancy `robustness.md` §6.11 itself flags (n = 495/Unified
  352 in this run vs. n = 452/Unified 318 and a −0.134 head-rice coefficient in prior planning
  notes) is an inconsistency the original section author already disclosed and left
  unreconciled; this integration did not attempt to resolve it further, consistent with the
  brief's instruction not to "和稀泥" (paper over) unresolved substantive conflicts.

## 12. Outstanding items for the author team (not addressed by this integration pass)

- **Word count**: the merged manuscript body (excluding the References list) runs to
  approximately 14,000 words, well above `04_format_spec.md` §1's 8,000–10,000-word guideline
  for a JIA Research Article. Trimming (most likely candidates: the Robustness section's
  fifteen fully spelled-out checks, and some of the Empirical Strategy section's rejected
  alternative designs in §4.1) was not attempted here, since cutting content is an editorial
  decision beyond what a merge-and-fact-check pass should do unilaterally.
- **Missing mandatory citations**: see §8 above (ten works on the format spec's required
  citation list are not cited anywhere in the drafted text).
- **Figure/table compression to submission targets**: see `figure_table_list.md`'s final
  section — the format spec's "9 figures/7 tables → 6 figures/5 tables" compression
  instruction does not resolve to a consistent count, and no plan document names which
  additional figure or which two tables should move to Supplementary.
- **Fig. 8/Fig. 9 numbering contradiction between plan documents**: see §3 above.
- **Data verification step (§3.4 of the manuscript)**: the manuscript's own Data section
  states that a manual field-by-field cross-check of parsed records against original MARA
  announcements is still outstanding and must be completed before submission; this was not
  something this integration pass could complete either, and the placeholder language was
  preserved as-is.
