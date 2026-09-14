# Version History

**Manuscript:** "Who measures what enters the market? Self-organised variety trials and the
third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"

## 1. v1 → v2 summary

Full detail in `manuscript/review/change_log_v1_to_v2.md`; organised there around ten
numbered issues raised by six review passes (R1_technical, R2_novelty, R3_readability,
format_check, number_consistency, reference_check). Summary by category:

- **A. Factual number errors (highest priority, all fixed):**
  - A1 — Winall's 2026 regulatory fine corrected from a 10× error (300,000 CNY) to the
    correct 3,000,000 CNY (RMB 3 million).
  - A2 — Enterprise-vs-public-institution comparison (§4.7, §7) replaced a planning-stage
    placeholder (+3.18 kg/mu, n=632) with the actual regression output on
    `table7_enterprise_vs_public.csv` (+4.179 kg/mu, n=408–411); the n=632/n=408–411
    discrepancy is disclosed explicitly rather than silently reconciled.
  - A3 — Added kg/mu → kg/hm² unit conversion at first mention (format-spec requirement).
- **B. Missing content added:**
  - B4 — Seven mandatory citations (Xie et al. 2023; Lu et al. 2024; Hang et al. 2024; Gong
    et al. 2026; Shi & Hu 2017; Qiu et al. 2016; Huang et al. 2018) added with substantive
    engagement, not bare reference-list entries — including repairing a data-provenance gap
    (Table 6's 2018/2021 figures traced explicitly to Xie et al. 2023).
  - B6 — New robustness check R16 (`quality_stated` under disclosure-behaviour controls) run
    and reported in a new §6.6, closing a check §3.3 had promised but v1 never executed.
  - B7 — Added a growth-duration structural-break sentence to §5.6 (Fig. 4 companion trait).
- **C. Length compression:** Section 6 restructured from 15 subsections to 7; §4.7 Non-claims
  compressed from ~1,050 to ~350 words (12 items, renumbered); Discussion §8.1 tightened.
  Net effect only partially offset the length added by B4/B6, so overall word count is still
  above the informal 8,000–10,000-word target (see `submission/submission_checklist.md`).
- No Non-claim, conflicting-evidence item (CF1–CF8), or robustness-failure result (R7, R9,
  R11, R13, R15) was removed in this pass — confirmed independently by
  `manuscript/review/final_proof_log.md` §1's own diff-vs-change-log audit.

## 2. v2 → submission package (this session, 2026-09-14)

The one substantive open item `final_proof_log.md` and `figure_table_list.md` both flagged as
**unresolved** — the figure/table compression to the journal's 6-figure/5-table main-text
target not adding up (7 main-text figures against a 6-figure target, no candidate identified
for the 7-table→5-table cut) — was resolved in this session:

- **Table 6** (Winall/comparator financial panel) and **Table 7** (enterprise-vs-institution
  descriptive comparison) moved to Supplementary Material as **Table S1** and **Table S2**.
- **Fig. 6 (old)**, the missingness-balance dumbbell plot, moved to Supplementary Material as
  **Fig. S1**; **Fig. 7 (old)**, the Winall mechanism figure, renumbered to **Fig. 6**.
- Every in-text citation to the affected figures/tables was located by exhaustive `grep`,
  manually checked against its surrounding paragraph (because "Fig. 6" had two distinct
  referents before the edit), and updated — see `manuscript/figure_table_list.md` for the
  full before/after mapping and rationale.
- A pointer sentence was added to main text §3.1 stating that Supplementary Material contains
  Table S1–S2 and Fig. S1.
- `submission/supplementary_material.md` created, reproducing the moved tables' full data and
  the moved figure's caption and source-file pointer under their new Supplementary numbering.
- `submission/manuscript.docx` and `submission/manuscript.pdf` rebuilt from the renumbered
  `manuscript/manuscript_v2.md` via `scripts/build_docx.py` and `scripts/build_pdf.py`; both
  built successfully (docx ≈74KB; pdf ≈5.0MB, 35 pages).
- Full submission package assembled: cover letter, highlights, declarations,
  figure captions, tables, and a submission checklist cross-referencing
  `plan/04_format_spec.md` and the P1–P12 unresolved items from `plan/00_decision_log.md` §5
  and `plan/03_target_journal.md`.

No substantive number, coefficient, or conclusion was changed in this session — only figure/
table numbering, one added pointer sentence, and the new submission-package files.

## 3. Review-report index

| Report | Location | Role |
|---|---|---|
| R1 — Technical rigor | `manuscript/review/R1_technical.md` | Identified the enterprise/institution placeholder-number issue (A2) and the missing R16 check (B6) |
| R2 — Novelty/promotion | `manuscript/review/R2_novelty.md` | Major-revision verdict; flagged missing mandatory citations (B4) as primary concern |
| R3 — Readability/journal fit | `manuscript/review/R3_readability.md` | Flagged excessive length and long-sentence density (informed the C-category compression) |
| Format check | `manuscript/review/format_check.md` | Checked against `plan/04_format_spec.md`; flagged the kg/hm² conversion gap (A3) and the figure/table count |
| Number consistency | `manuscript/review/number_consistency.md` | Found the 10× fine-amount error (A1) and the stale enterprise/institution coefficients (A2) |
| Reference check | `manuscript/review/reference_check.md` | Verified 10 format-spec-mandatory references as real but uncited (B4); flagged Table 6 data-provenance gap |
| Final proof log | `manuscript/review/final_proof_log.md` | Confirmed the v1→v2 diff matches the change log exactly; closed 5 of 5 assigned issues; left word count and figure/table compression open (the latter resolved this session) |

## 4. Approximate git timeline (this repository, session-relevant commits)

Reconstructed from `git log`; exact hashes omitted as unnecessary — see repository history
for authoritative commit metadata.

1. Early workflow/tooling commits (workflow template genericisation, prior unrelated work).
2. Section-by-section drafting: Introduction/Institutional background/Data, then Empirical
   strategy/Results, Mechanism, Discussion, Conclusion, Robustness, and Front matter —
   committed as separate drafting passes.
3. Figure consolidation into `manuscript/figures/`.
4. Mechanism-section date/precision fixes (Winall tender-offer dates, order-grain margin
   figures corrected to distinguish 2025H1 from FY2025).
5. Main-estimation results notes committed with an independently reproduced Table 3 and new
   robustness diagnostics (R4, R13, R9/R11 minimum-detectable-effect analysis).
6. Manuscript integration into `manuscript_v1.md`: unified figure/table numbering across
   drafted sections, resolved cross-chapter numeric inconsistencies, compiled the reference
   list — with the figure/table compression question flagged as open at this stage.
7. Four review passes committed in sequence: R2 (novelty), R3 (readability), format check,
   number consistency, then reference verification.
8. `manuscript_v2.md` produced: the 10× fine-amount fix, corrected enterprise-vs-institution
   table, 7 required citations added with substantive engagement, real Table 2 built, the
   `quality_stated` (R16) robustness check run, and Robustness/Non-claims sections compressed.
9. Final proofing pass: LaTeX math rendering fixed in the DOCX/PDF builders; `build_log.md`
   and `final_proof_log.md` completed, confirming the v1→v2 diff matches the change log and
   closing five of five assigned review issues.
10. **This session**: figure/table compression decision made and executed throughout
    `manuscript_v2.md` and `figure_table_list.md`; `manuscript.docx`/`manuscript.pdf`
    rebuilt; full submission package assembled under `submission/`.
