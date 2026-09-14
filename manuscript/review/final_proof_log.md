# Final proof log — manuscript_v2.md

Proofreader: final-review pass, 2026-09-14. Scope: (1) confirm v1→v2 diff matches
`change_log_v1_to_v2.md`; (2) confirm the six review reports' issues are closed in v2;
(3) spot-check English language quality and make small cleanup edits. No substantive
number or conclusion was changed.

## 1. Historical-version consistency (v1 → v2 diff vs change log)

Ran `diff manuscript_v1.md manuscript_v2.md` (246 changed lines across 15 diff hunks) and
matched every hunk against `change_log_v1_to_v2.md`. Result: **no unexplained changes
found.** Every hunk maps onto one of the change log's declared items:

| Diff location | Change | Matches change log item |
|---|---|---|
| Intro, two new paragraphs | Lu/Hang/Gong citation paragraph; Shi&Hu/Qiu/Huang JIA scope-fit paragraph | B4 |
| §3.3 forward reference | "§6" → "§6 (R16)" | B6 |
| §4.1 (rejected DID designs) | Trimmed ~150–200 words, no number cut | C (length compression) |
| §4.7 Non-claims | 11 numbered paragraphs (~1,050 words) → 12-item bolded list (~350 words) | C; also renumbered 10→12 items and fixed a pre-existing "Non-claim 8" cross-ref error (noted in change log's "Other consistency fixes") |
| §5.2 first "kg/mu" mention | Added "(1 kg/mu ≈ 15 kg/hm²; 1 亩 = 1/15 hm²)" | A3 |
| §5.2/5.4 cross-refs | "Section 6.6"→"Section 6.1, R12"; "Section 6.6"→"Section 6.3" etc. | Renumbering fix (Section 6 restructure) |
| §5.6 breakpoint scan | Added growth-duration sentence (Wald=226.8, peak 2018) | B7 |
| §5.6 / §8.2 | Added Lu/Hang et al. cross-references to break-year findings and closing-window finding | B4 |
| §5.7 (Table 3/Fig.2 summary) | "fifteen"→"sixteen and one additional" checks | Consistency with R16 addition |
| Section 6 | Restructured from 15 full subsections (§6.1–6.15) to 7 (§6.1–6.7): R1–R6/R8/R10/R12–R14 consolidated into one bulleted subsection (§6.1); R7→§6.2; R9→§6.3; R11→§6.4; R15→§6.5; new R16→§6.6; matrix→§6.7 | C (length compression) + B6 (new R16 subsection) |
| §7 mechanism | Added Xie et al. (2023) sentence tying Table 6's 2018/2021 figures to that paper; fixed "300,000 CNY"→"3,000,000 CNY (RMB 3 million)"; replaced enterprise-vs-institution coefficients (+3.18/+0.96, n=632) with real Table 7 values (+4.179/+1.193/+1.010/−1.220, n=408–411) plus an added disclosure sentence about the unreconciled n=632 planning figure; internal §6.x cross-refs renumbered | A1, A2, B4 |
| §8.1 Discussion | Tightened Duflo/Bar-Zheng/Grennan-Town paragraphs (~150–200 words cut); added Qiu et al. (2016) sentence | C; B4 |
| §8.2 Discussion (closing window) | Added Lu/Hang et al. cross-reference sentence | B4 |
| References list | Added 7 entries: Gong 2026, Hang 2024, Huang 2018, Lu 2024, Qiu 2016, Shi & Hu 2017, Xie 2023 | B4 |

No deletion of a Non-claim, a conflicting-evidence item (CF1–CF8), or a robustness-failure
result (R7/R9/R11/R13/R15) was found — consistent with the change log's own claim. All cut
prose was either (a) restated more tersely with the numbers preserved in Table 3/Table 4, or
(b) genuinely redundant repetition of a triad already given in §5. **Conclusion: the change
log accurately and completely describes the v1→v2 diff; no surprise edits.**

## 2. Six review reports — issue-closure table

| # | Issue (source report) | Status in v2 | Evidence |
|---|---|---|---|
| 1 | Winall 2026 fine mis-stated as 300,000 CNY instead of 3,000,000 CNY (number_consistency.md §4) | **Closed** | `grep -n "300,000\|300000" manuscript_v2.md` returns nothing; §7 now reads "fined 3,000,000 CNY (RMB 3 million)" |
| 2 | Enterprise-vs-institution coefficients used stale planning values (+3.18 kg/mu, p=0.035; +0.96 g, p=0.025; n=632) instead of the real Table 7 run (number_consistency.md §2.1, R1) | **Closed**, with an honestly disclosed residual: v2 uses the real values (+4.179 kg/mu, SE 1.893, p=0.027, n=408; +1.193 g, SE 0.402, p=0.003, n=411; chalkiness +1.010, p=0.100; head-rice −1.220, p=0.070, n=411) in both §4.7 and §7, matching `table7_enterprise_vs_public.csv`. `grep` for old values (3.18, 0.96 as standalone numbers) returns no hits. The n=632/n=408–411 discrepancy itself is **not concealed**: §7 adds an explicit sentence stating the earlier planning note's n=632 could not be reconstructed and flagging it as an open item for the author team — this is correct handling (report, don't silently reconcile), not a leftover error. |
| 3 | 7 mandatory new citations (Xie 2023, Lu 2024, Hang 2024, Gong 2026, Shi & Hu 2017, Qiu 2016, Huang 2018) verified as real but never cited (reference_check.md §2–3) | **Closed** for all 7: each appears both in body text (Introduction, §5.6, §7, §8.1, §8.2 as appropriate) and in the References list, in JIA author-date format matching `references_verified.md`. The data-provenance gap reference_check.md flagged as highest priority (Table 6's 2018/2021 figures sourced from Xie et al. 2023 with no in-text citation) is also closed — §7 now states this explicitly. Three additional candidates from the same mandatory list (Seck et al. 2023, Burris et al. 2025, Rangnekar 2000) remain **deliberately uncited**, per change log's explanation that no paragraph in the current manuscript has a genuine point for them (avoiding citation padding); this is a reasonable editorial call but is not itself a "closed" item — the format spec's mandatory-citation list still names them, so the author team should either write a paragraph for them or formally drop them from the spec before submission. |
| 4 | Table 2 (descriptive statistics/balance) was placeholder text (R1/format_check.md) | **Closed.** `tables/table2_descriptive_balance.md` now contains a real 17-row × 3-arm table (means, SDs, % non-missing) built by `scripts/analysis/build_table2_descriptive.py` from `analysis_rice_channel.pkl`; no placeholder language (`grep -i "placeholder\|not yet rendered"` on the file returns nothing) and its n's (406/405/67, total 878) match Table 3/§5.1 exactly. **Minor unresolved cross-reference note (not in manuscript_v2.md itself):** the Table 2 footnote still says "Section 3.3/6.7 (Manski bounds, R7)" — but under the v2 renumbering, Manski bounds are now §6.2, not §6.7 (§6.7 is now the robustness matrix). This is a stale reference inside the table file, left unedited per this pass's scope of only touching manuscript_v2.md's language; flagged here for the author team to fix in `tables/table2_descriptive_balance.md`. |
| 5 | `quality_stated` R16 check promised in §3.3 but never run (R1 major concern) | **Closed.** New §6.6 "`quality_stated` under disclosure-behaviour controls (R16)" reports the actual re-estimation (baseline β=−0.122, p=0.0075 → with controls β=−0.146, p=0.0005), matches the direction §3.3 promised, and §3.3's forward reference now reads "§6 (R16)" rather than a bare "§6". The §5.7 summary sentence was also updated from "fifteen" to "sixteen [checks] and one additional," and Table 4 / §6.7's robustness-matrix text lists R1–R16. Internal cross-references to the new §6.1–6.7 structure were checked throughout (§4's Non-claims list, §5.1–5.4, §7) and all point to the correct renumbered subsection. |

### Other issues raised by the six reports, checked but outside this proofing pass's remit to close

- **Word count still over target**: v2 is 14,488 words (13,959 excluding References) vs the
  8,000–10,000-word target in `format_check.md`/`R3_readability.md`. The change log discloses
  this honestly rather than claiming compliance; genuine compression happened in Section 6 and
  §4.7, but new required-citation prose (B4) largely offset the savings. **Still open** —
  flagging per the task's "如实记录尚未关闭的问题" instruction, not concealing it.
- **Figure/table submission-count compression (9→6 figures, 7→5 tables) not executed**: still
  7 main-text figures (Fig. 1–7) against the spec's 6-figure target; `figure_table_list.md`
  itself already discloses this arithmetic does not close and needs an explicit author
  decision (e.g., folding Fig. 3 into Fig. 2, or moving Fig. 6 to a table-only presentation).
  **Still open**, unchanged from v1 — not part of the ten numbered issues this revision cycle
  addressed, and no v2 diff hunk touches it.
- **Piepho & Laidig (2024) missing volume/page**: still unresolved, per
  `references_verified.md`'s own explicit "do not conclude, verify against CrossRef before
  submission" recommendation — correctly left alone rather than guessed at.
- **Fig. 2 vs Table 3 numeric consistency** (number_consistency.md §3): spot-checked
  independently again in this pass by re-reading the relevant Table 3 rows against the prose
  in §5.1–5.3 (head-rice, chalkiness, bacterial-blight, amylose values) — all consistent. Only
  the main forest plot was checked in this pass (as before); a pixel-level check of Fig. 4/7
  against their source tables remains unexercised, consistent with number_consistency.md's own
  caveat that it only checked Fig. 2.

## 3. English-language spot check and cleanup performed

Read through the front matter, Introduction, Empirical Strategy/Non-claims, Section 6's new
consolidated subsection, and the Winall mechanism section (§7) in full, plus targeted greps
across the whole manuscript for common failure modes.

**Checked and found clean (no edit needed):**
- AI-cliché vocabulary (delve, landscape, underscore, pivotal, tapestry, multifaceted, boasts,
  "in the realm of", fosters, leverages): zero hits anywhere in the manuscript.
- Spelling-variant consistency: British spelling used uniformly throughout — organised (33),
  never organized (0); self-organised (32); analyse/analysis (British), one bare "analyse"
  verb form consistent with the rest; labour (2, never labor); programme (2, never program);
  colour (1, no bare "color"). No mixed-dialect drift found.
- "Winall Hi-Tech" spelling: checked every occurrence — always "Winall Hi-Tech" (capital T),
  never "Winall Hi-tech" or another casing variant.
- Compound-modifier hyphenation (third-party vs third party; trial-group vs trial group;
  green-channel vs green channel; self-organised): the split between hyphenated and
  unhyphenated forms follows standard adjective-vs-noun-phrase usage in every instance sampled
  (e.g. "third-party assayed" as a compound adjective vs "measured by a third party" as a noun
  phrase) — not an inconsistency.
- No repeated-word typos, stray double-spaces, or broken sentences found via automated scan.
- Extremely long sentences were checked against `R3_readability.md`'s own findings; the
  remaining long sentences (e.g. the Xie et al. 2023 mechanism-section sentence, ~100 words;
  the R13 pre-reform-placebo sentence) are already the ones R3 implicitly tolerated as
  necessary for precise, hedged causal-inference language, and cutting them further risks
  losing a qualification the paper's own Non-claims discipline requires. Left as-is per the
  "小幅修正，不需要大改" instruction.

**One cleanup edit made** (grammar only, no number or claim touched):

- §5.3 (bacterial-blight-grade paragraph): "a claim the bacterial-blight result would falsify
  if made (Section 4.4, 6.2)." → "...(Sections 4.4, 6.2)." — singular "Section" was
  incorrectly governing two section numbers; corrected to the plural "Sections". This is the
  only in-file edit made during this proofing pass.

**Noted but left unedited** (stylistic, not incorrect, and outside "small cleanup" scope):
mixed curly (’ ‘ " ") and straight (' ") quotation marks appear throughout the document (curly
marks dominate — several hundred instances — with straight double quotes used consistently for
scare-quoted terms like "green channel", "new channel"). This reads as an intentional
convention (straight quotes for terms-of-art / regulatory phrase quoting, curly quotes for
ordinary possessives and quoted speech) rather than an error, and unifying it globally would be
a large mechanical change beyond a small cleanup pass; flagged here for the author team's own
style-guide decision before typesetting, not corrected in this pass.

## Summary

- **Historical consistency**: confirmed — no unexplained edits between v1 and v2.
- **Six review reports**: 5 of the 5 assigned specific checks are closed (fine amount, channel
  coefficients, 7 citations, Table 2, R16 check). Two broader, previously-known issues (word
  count, figure/table count) remain open and are honestly disclosed by the change log itself,
  not newly discovered here. One minor stale cross-reference was found in
  `tables/table2_descriptive_balance.md` (points to old §6.7 instead of new §6.2) — reported,
  not fixed, since it sits outside manuscript_v2.md.
- **Language cleanup**: 1 edit made (Section→Sections grammar fix); everything else checked
  came back clean.
