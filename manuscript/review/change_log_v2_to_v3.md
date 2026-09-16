# Change log — v2 → v3

**Manuscript:** "Who measures what enters the market? Self-organised variety trials and the
third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"

**Trigger for this revision:** an explicit editorial instruction that no negative information
about Anhui Winall Hi-Tech Seed Co. ("荃银高科") may appear anywhere in the paper.

**Operating principle adopted (stated up front so every edit below can be checked against
it):** rather than deleting only the negative Winall material and leaving the positive
material in place — which would have turned the paper into one-sided promotion of a real,
named company — the entire financial/business narrative about Winall, positive and negative
alike, was removed from the paper. What remains in §7 is confined to the two findings that
are load-bearing for the paper's identification strategy: (1) Winall's trial-channel choice
(the channel-choice logit), and (2) Winall's within-channel quality positioning relative to
other applicants. Neither of these two findings is a claim about Winall's financial condition,
so removing the financial narrative around them does not weaken the paper's core argument.
No new laudatory or promotional language about Winall was introduced to "balance" the
deletion; Non-claim 10 was rewritten as a neutral scope statement, not a positive one.

---

## 1. Section 7 (Mechanism), main text

**Location:** `manuscript/manuscript_v3.md`, § "7. Mechanism: Winall Hi-Tech Seed as a
counter-case" (was lines 469–483 of `manuscript_v2.md`).

- **Deleted in full** the paragraph beginning "This pattern must be read alongside, not
  instead of, a set of financial facts..." and ending "...this section does not convert the
  quality-grade coefficients above into any implied revenue, processing value, or cost saving
  for Winall or its comparators." This paragraph reported: the order-grain segment's gross
  margin (≈2.66% in 2024, ≈−0.09% in H1 2025, −1.31% for FY2025); the 2025 attributable net
  profit of −212 million CNY (a profit-to-loss swing, −317.91% YoY); the 2024 annual report's
  qualified audit opinion; the 2026 fine of RMB 3 million and the ST Winall stock-name change
  effective 2026-06-30; and China Seed Group's partial tender offer (announced 2025-11-20,
  tender period 2025-12-04 to 2026-01-05, resulting 40.51% stake). All of this — financial,
  regulatory and ownership content — is removed; none of it is retained anywhere else in the
  manuscript or submission package.
- **Retained unchanged:** the role-declaration sentence ("Winall enters this paper as a
  counter-case..."), the channel-choice-logit paragraph (60.2% vs 47.5% unified-channel use;
  α = −0.728, p < 0.0001, odds ratio 0.483), the within-channel-positioning paragraph
  (head-rice +2.212, quality-grade-stated +9.8pp, chalkiness −0.692, all p < 0.001, with the
  new-channel-subsample null replication), the R10 drop-Winall robustness paragraph, the
  enterprise-vs-institution descriptive paragraph, and the two closing scope-limit sentences.
  No coefficient, standard error, p-value, confidence interval, or sample size in §7 was
  changed.
- **Edited (not deleted)** the sentence introducing Xie et al. (2023): removed the clause
  "the order-grain revenue-share and gross-margin figures for 2018 and 2021 reported below
  (Supplementary Table S1) are drawn from that paper's data..." (which pointed at the now-
  removed financial table) and replaced it with a scope clause noting that this section's own
  analysis is confined to the variety-level channel-choice/positioning evidence and does not
  draw on Xie et al.'s firm-level contract data. The citation to Xie et al. (2023) itself is
  kept, since it is one of the format-spec's required citations and remains substantively
  relevant background on Winall's contract-farming business model (a description of a
  business practice, not a financial-performance claim).
- **Checked for a dangling transition** after the deletion: the paragraph before the cut
  (within-channel positioning) and the paragraph after it (R10 robustness) join without any
  edit needed — R10 is a self-contained topic sentence ("Dropping every Winall-linked record
  from the main consortium-versus-unified comparison leaves the headline result intact...")
  that does not depend on the deleted paragraph for context. No new bridging sentence was
  added, to avoid introducing text that was not strictly necessary.
- **Renumbered** two occurrences of "Supplementary Table S2" to "Supplementary Table S1" in
  the enterprise-vs-institution paragraph (see item 3 below for why the numbering shifted).
- Section 7 word count: 870 words (was ~1,110 words in v2), still one of nine main sections
  and well under the format-spec's ≤15%-of-manuscript guideline for this section.

## 2. Non-claim #10 (§4.7, "What this paper does not claim")

**Before (v2):** "We do not claim Winall's quality-oriented positioning has been a financial
success. §7 reports its negative order-grain margin, 2025 loss, qualified audit opinion and
2026 penalty in the same discussion as its quality advantage; financial sustainability is
treated as open."

**After (v3):** "This paper does not evaluate the overall financial performance, business
strategy, or corporate governance of any applicant firm, including Winall. The channel-choice
and within-channel quality comparisons in §7 are silent on firm-level profitability."

This is a scope statement, not a positive or negative claim about Winall — it says the paper
takes no position on Winall's (or any firm's) financial condition, rather than substituting a
favourable characterisation for the removed unfavourable one.

## 3. Supplementary Table S1 (Winall/comparator financial panel) — removed entirely

- **File:** `submission/supplementary_material.md`. The full table (14 companies, 2015–2026,
  columns for revenue, gross margin, net profit, R&D intensity, order-grain revenue/share/
  margin, imputation flags) has been deleted in full, along with its caption and source-file
  pointer (`manuscript/tables/table6_company_panel.csv`).
- **Not edited to keep only positive rows or columns.** The instruction was to remove the
  negative-information problem, not to selectively publish a positive-only version of a real
  company's (and its listed comparators') financial data. Since the §7 financial narrative
  that motivated this table's inclusion has itself been removed, the table has no remaining
  independent role in the paper and is dropped rather than edited.
- The underlying source file `manuscript/tables/table6_company_panel.csv` is left in place on
  disk (as raw evidence data, not as a cited artefact) but is no longer referenced from
  `manuscript_v3.md`, `figure_table_list.md`, or the supplementary material.
- **Renumbering:** the former Supplementary Table S2 (descriptive trait division of labour,
  enterprise vs. public research institution applicants — a full-sample analysis, not
  Winall-specific, and already flagged in the main text as "descriptive background only, not
  a causal comparison") is renumbered **Supplementary Table S1**. Its content, caption, and
  source file (`manuscript/tables/table7_enterprise_vs_public.csv`) are unchanged.
- Updated cross-references to the renumbered table in: `manuscript/manuscript_v3.md` (§4.7
  Non-claim 9; §7, two occurrences), `manuscript/figure_table_list.md`,
  `submission/supplementary_material.md`, `submission/tables.md`.

## 4. Fig. 6 (Winall mechanism figure) — panel (c) removed

- **Script:** `manuscript/scripts/fig5_mechanism.py`. Removed the entire "Panel (c)" block
  that plotted order-grain revenue share and R&D intensity over 2015–2025 from
  `evidence/04_order_grain_timeseries.csv` and `evidence/company_panel.csv`, including its
  two annotations — a vertical marker and text label for "2025: net loss (-212M CNY, turned
  from profit)" and another for "2026-06: fined & renamed ST Winall". Changed the figure grid
  from 3 rows to 2 rows and shrank the overall figure height (11×11 in → 11×7.5 in)
  accordingly. Updated the figure's suptitle from "...channel choice, within-channel trait
  gap, and financial context" to "...channel choice and within-channel trait gap".
- **Panels (a) and (b) are otherwise unchanged**: same data sources
  (`evidence/data/analysis_rice_channel.pkl`, `manuscript/tables/table5_winall_positioning.csv`),
  same statistics, same visual encoding.
- **Re-ran the script** (`python3 manuscript/scripts/fig5_mechanism.py`); it completed without
  error (panels (a)/(b) do not depend on the two evidence files removed from panel (c)) and
  overwrote `manuscript/figures/fig5_winall_mechanism.png` in place. The filename is
  unchanged, since the manuscript text never embeds the image by path (all figure references
  in `manuscript_v3.md` are prose citations like "Fig. 6a"/"Fig. 6b", not Markdown image
  syntax — confirmed no `![...]()` tags exist in the manuscript source), so no in-text path
  reference needed updating.
- Verified visually (inspected the re-rendered PNG) that the output is a clean two-panel
  figure with no residual financial content.

## 5. Figure/table documentation updated to match

- `manuscript/figure_table_list.md`: added a v3 status note at the top; struck through the
  Table S1 (financial panel) row and marked it "Removed entirely in v3"; relabelled the
  former Table S2 row as "Table S1"; updated the Fig. 6 row to describe two panels instead of
  three and to note panel (c)'s removal; added a new "Verification note (v3)" section
  recording the grep checks performed.
- `submission/figure_captions.md`: updated the Fig. 6 caption to two panels; added a header
  note pointing to this change log.
- `submission/tables.md`: updated the header note referencing Supplementary Table S1
  (singular, not S1–S2) and flagging the v3 renumbering.
- `submission/supplementary_material.md`: added a v3 update note at the top explaining the
  removal and renumbering; replaced the "Supplementary Table S1" financial-panel section with
  nothing (fully removed); relabelled the enterprise-vs-institution table's heading to
  "Supplementary Table S1" with a footnote tracing its numbering history (Table 7 →
  Supplementary S2 (v2) → Supplementary S1 (v3)).

## 6. Ethical approval / data availability statement

- **Location:** `manuscript/manuscript_v3.md` (Ethical approval, end of paper),
  `manuscript/sections/declarations.md`, `submission/declarations.md`.
- **Before:** "...it uses only publicly available government variety-approval announcements
  and publicly disclosed company financial filings."
- **After:** "...it uses only publicly available government variety-approval announcements."
- Rationale: with the financial-filings-derived Table S1 and the §7 financial narrative
  removed, the paper no longer draws on company financial filings as a data source, so the
  clause was inaccurate as well as unnecessary and has been dropped (not merely reworded to
  sound more neutral while still referencing financial filings).

## 7. Submission package — other files

- `submission/cover_letter.md`: reworded the Conflict-of-interest paragraph so it no longer
  says the manuscript "reports publicly disclosed financial and regulatory facts about"
  Winall; it now says the manuscript discusses Winall "only through its publicly available
  variety-approval records" and explicitly states the manuscript does not evaluate any
  company's financial performance or business standing. The "Alignment with current
  regulatory direction" paragraph, which discusses the Ministry's 2022 industry-wide
  rectification campaign, was left unchanged — it is an industry/policy-level point, not a
  Winall-specific fact, consistent with the scope of this revision.
- `submission/submission_checklist.md`: added a v3 status note; rewrote the item that had
  required "every positive statement about Winall's quality positioning [to be] paired... with
  its negative financial facts" (no longer applicable, since neither now appears); marked
  unresolved items **P7** (sourcing for each Winall negative fact) and **P11** (imputed-value
  labelling in the financial panel) as **Closed** with an explanation; updated the
  figure/table-compression checklist entry and the word-count estimate.
- `submission/VERSION_HISTORY.md`: added a new "§3. v2 → v3 summary" section documenting this
  revision in full, renumbered the subsequent "Review-report index" and "Approximate git
  timeline" sections, and appended a timeline entry for this session.

## 8. What was deliberately left unchanged

To confirm this revision did not overreach past its stated scope:

- **No statistical result was altered.** Every coefficient, standard error, confidence
  interval, p-value, BH-q value, and sample size in Sections 5, 6 and 7 (Table 3, Table 4,
  Table 5, the channel-choice logit, the within-channel positioning regressions, and R1–R16)
  is identical to `manuscript_v2.md`.
- **No conflicting-evidence item (CF1–CF8) or robustness-failure result (R7, R9, R11, R13,
  R15) was removed or softened.** These are full-sample findings, not Winall-specific
  negative information, and are out of scope for this instruction.
- **The Discussion (§8) and Introduction (§1) required no edits.** Neither section mentions
  Winall at all (confirmed by grep); the Discussion's treatment of the Ministry's 2022
  special-rectification campaign (§8.2, §8.3) is an industry-policy point and was left as is.
- **Table 5** (Winall channel composition and within-channel positioning coefficients) and
  **Table 4's R10 row** (drop-Winall robustness check) are both retained without modification,
  since they are part of the identification-strategy evidence this revision was instructed to
  keep.

## 9. Verification

Full-text greps run against `manuscript/manuscript_v3.md` after all edits, confirming zero
remaining hits for: `ST Winall`, `qualified audit`/`audit opinion`, `净利`, `归母`, `tender
offer`, `罚款`, and stand-alone `loss`/`margin`/`profit` (the only string-level matches for a
bare "fine" substring were inside unrelated English words such as "defined"/"confined"/
"refined", not the word "fine" itself). `Table 6` and `table6_company_panel` no longer appear
in the main text. The rebuilt `submission/manuscript.docx` and `submission/manuscript.pdf`
were independently checked (via `python-docx` text extraction) for the same terms, with the
same all-clear result.

## 10. Rebuild

```
python3 scripts/build_docx.py manuscript/manuscript_v3.md submission/manuscript.docx --line-numbers
python3 scripts/build_pdf.py manuscript/manuscript_v3.md submission/manuscript.pdf
```

Both completed successfully: `submission/manuscript.docx` (≈73 KB) and
`submission/manuscript.pdf` (35 pages, ≈4.99 MB).
