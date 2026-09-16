# Version History

**Manuscript:** "Mining administrative approval records for technology assessment: record-level
trial-channel indicators and third-party-assayed grain quality in China's rice variety
registrations, 2017–2022"

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

## 3. v2 → v3 summary (this session, 2026-09-16)

Full detail in `manuscript/review/change_log_v2_to_v3.md`. At the author team's explicit
request, all discussion of Anhui Winall Hi-Tech Seed Co.'s financial performance, business
strategy, or corporate governance was removed from the paper. To avoid one-sidedness, the
paper was not edited to keep only positive Winall content: instead, the entire financial/
business narrative — positive and negative alike — was removed, leaving §7 focused solely on
the two findings load-bearing for the paper's identification argument (Winall's trial-channel
choice, and its within-channel quality positioning). No statistical coefficient, p-value, or
sample size anywhere in the paper was changed.

- **§7 (Mechanism)**: deleted the paragraph reporting Winall's order-grain gross margin
  (2024/2025H1/FY2025), 2025 attributable net profit and loss-making swing, 2024 qualified
  audit opinion, 2026 fine and ST-Winall status change, and the China Seed Group tender offer.
  Retained the channel-choice logit (§7 para. 2) and within-channel positioning (§7 para. 3)
  results, and the robustness/scope paragraphs around them, unchanged.
- **Non-claim 10** (§4.7): rewritten from a claim about Winall's financial-success status
  (which cited the now-removed margin/loss/audit/penalty figures) to a scope statement that
  this paper does not evaluate any applicant firm's financial performance, business strategy,
  or corporate governance.
- **Supplementary Table S1** (Winall/comparator financial panel, formerly Table 6): removed
  in full from `submission/supplementary_material.md`; not retained in any edited or
  positive-only form, since with the financial narrative gone the table had no remaining role.
  Former Supplementary Table S2 (enterprise-vs-institution descriptive comparison, unaffected —
  it is a full-sample analysis, not Winall-specific) is renumbered **Table S1**.
- **Fig. 6** (Winall mechanism figure): former panel (c) — order-grain revenue share and R&D
  intensity time series, annotated with the 2025 loss and 2026 ST event — removed from
  `manuscript/scripts/fig5_mechanism.py`; figure re-rendered as a two-panel image at
  `manuscript/figures/fig5_winall_mechanism.png`. Panels (a) and (b) are otherwise unchanged.
- **Ethical approval statement**: "publicly disclosed company financial filings" removed from
  the data-source description, since the paper no longer draws on any such filings; now reads
  "publicly available government variety-approval announcements" only.
- **Cover letter**: conflict-of-interest paragraph reworded to describe Winall's role via its
  public variety-approval records only, dropping the reference to "publicly disclosed
  financial and regulatory facts."
- **Submission checklist, figure captions, tables list**: updated to reflect the Table S1
  removal/renumbering and the two-panel Fig. 6; checklist items P7 and P11 (Winall
  negative-fact sourcing and financial-panel imputation labelling) closed as no longer
  applicable.
- Not changed: any Non-claim other than #10; any CF1–CF8 conflicting-evidence item; any
  robustness check (R1–R16); any coefficient, CI, p-value, or n in Sections 5–6; Table 5
  (Winall channel-choice and positioning results); Table 4 (robustness matrix, including R10's
  drop-Winall check); the Discussion's treatment of the Ministry's 2022 industry-wide
  rectification campaign (an industry-policy point, not a Winall-specific fact).

## 4. Review-report index

| Report | Location | Role |
|---|---|---|
| R1 — Technical rigor | `manuscript/review/R1_technical.md` | Identified the enterprise/institution placeholder-number issue (A2) and the missing R16 check (B6) |
| R2 — Novelty/promotion | `manuscript/review/R2_novelty.md` | Major-revision verdict; flagged missing mandatory citations (B4) as primary concern |
| R3 — Readability/journal fit | `manuscript/review/R3_readability.md` | Flagged excessive length and long-sentence density (informed the C-category compression) |
| Format check | `manuscript/review/format_check.md` | Checked against `plan/04_format_spec.md`; flagged the kg/hm² conversion gap (A3) and the figure/table count |
| Number consistency | `manuscript/review/number_consistency.md` | Found the 10× fine-amount error (A1) and the stale enterprise/institution coefficients (A2) |
| Reference check | `manuscript/review/reference_check.md` | Verified 10 format-spec-mandatory references as real but uncited (B4); flagged Table 6 data-provenance gap |
| Final proof log | `manuscript/review/final_proof_log.md` | Confirmed the v1→v2 diff matches the change log exactly; closed 5 of 5 assigned issues; left word count and figure/table compression open (the latter resolved this session) |

## 5. Approximate git timeline (this repository, session-relevant commits)

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
10. Figure/table compression decision made and executed throughout `manuscript_v2.md` and
    `figure_table_list.md`; `manuscript.docx`/`manuscript.pdf` rebuilt; full submission
    package assembled under `submission/`.
11. **This session**: `manuscript_v3.md` produced by author request, removing all discussion
    of Winall Hi-Tech Seed's financial performance, business strategy, and corporate
    governance (§7 financial-facts paragraph, Non-claim 10, former Supplementary Table S1,
    and Fig. 6's former panel (c)); `manuscript.docx`/`manuscript.pdf` rebuilt from
    `manuscript_v3.md`; submission-package files updated to match.

---

## 6. v3 → v4 (2026-09-16): S&T intelligence reframing

Full detail in `manuscript/review/change_log_v3_to_v4.md`. Specification input:
`plan/05_sti_reframing_brief.md` §3.

**Purpose.** Make scientific and technological intelligence (S&T information analysis) a main
supporting pillar of the paper, standing alongside agricultural technology assessment rather
than replacing it. The paper's method core — discovering record-level intelligence elements in
a long-public but structurally unexploited administrative text corpus, converting them into a
2,386-record × 17-field indicator system, and diagnosing the reliability of an official
innovation data source *field by field* according to who measured each field — is now stated in
that language from the title onward.

**What changed.**

- **Title** — "Who measures what enters the market? Self-organised variety trials and the
  third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022" →
  "Mining administrative approval records for technology assessment: record-level
  trial-channel indicators and third-party-assayed grain quality in China's rice variety
  registrations, 2017–2022". Running title updated to match.
- **Abstract** — opens on the intelligence source rather than on regulatory history; the
  institutional background is compressed to one sentence; a closing sentence states the
  method's portability to drug approval, device registration and patent examination corpora.
  **Every quantitative result in the middle is unchanged, word for word.** 254 → 249 words
  (JIA limit 250).
- **Keywords** — now *administrative text mining; technology assessment; information
  extraction; data provenance; rice variety approval; China* (6, none containing "and"/"of";
  two农学 entries retained for retrievability by JIA's readership).
- **Introduction** — a new 230-word paragraph after ¶1 sets out administrative approval
  records as an unexploited class of innovation-measurement evidence and names the paper's
  first contribution as a methodological one for S&T intelligence. The former opening
  paragraph of regulatory history is compressed from ~200 to ~135 words, retaining every
  institutional fact. Contribution 1 is restated to lead with the extraction pipeline;
  contribution 2 demotes the self-certification literature to interpretive support.
- **Data / Methods** — §3 retitled "Data and the intelligence-extraction pipeline" and given a
  lead paragraph naming six steps (intelligence-source identification → corpus acquisition →
  field extraction → entity recognition and disambiguation → field-coverage and data-quality
  assessment → indicator construction), with each subsection tagged by step. **Subsection
  numbers were deliberately left unchanged** so that no existing cross-reference breaks. A new
  paragraph in §3.1 documents the entity-resolution rule used for the focal-firm counter-case
  and its error profile (precision 1.000, recall 0.770 on 1,426 institution-labelled records;
  missed records fall into the comparison group, biasing §7 toward zero) — a rule already
  recorded and executed in the project's planning documents, now written into the methods. No
  analysis was re-run.
- **Discussion** — new §8.4 "Implications for S&T intelligence practice" (562 words): the value
  and limits of administrative approval corpora as an innovation data source; the finding that
  reliability is a property of fields rather than of sources, and the provenance-labelling
  practice that follows; portability of the diagnostic to drug, device and patent examination
  corpora; and concrete uses for technology assessment and competitive intelligence. Former
  §8.4 Limitations renumbered §8.5. §8.1 retitled and compressed from ~450 to ~230 words, with
  all five of its citations retained.
- **References** — the reference list grows from 18 to 24 entries, and the verification
  report in `manuscript/references_verified.md` from 21 to 27 records (the three extra
  verified-but-uncited format-spec titles — Seck et al. 2023, Burris et al. 2025, Rangnekar
  2000 — remain uncited, as in v3). Six additions, each verified against at least two independent
  tools, with per-entry records appended to `manuscript/references_verified.md` (entries
  22–27):

  | Reference | Status |
  |---|---|
  | Antons D, Grünwald E, Cichy P, Salge T O. 2020. R&D Management, 50, 329–351. | ✅ Verified (Undermind + WebSearch) |
  | Franceschini F, Maisano D, Mastrogiacomo L. 2016. Journal of Informetrics, 10, 933–953. | ✅ Verified (Undermind + WebSearch) |
  | Jaffe A B, de Rassenfosse G. 2017. JASIST, 68, 1360–1374. | ✅ Verified (Undermind + WebSearch + dblp); NBER working-paper version deliberately not used |
  | Losiewicz P, Oard D W, Kostoff R N. 2000. Journal of Intelligent Information Systems, 15, 99–119. | ✅ Verified (Undermind + WebSearch) |
  | Rammer C, Es-Sadki N. 2023. Technological Forecasting and Social Change, 197, 122874. | ✅ Verified (Undermind + WebSearch); SSRN preprint version deliberately not used |
  | Shi Y, Ren P, Zhang Y, Gong X, Hu M, Liang H. 2021. Frontiers in Research Metrics and Analytics, 6, 670006. | ✅ Verified (Undermind + WebSearch + PubMed) |

  None of the six was read in full text, so each is cited only for a general claim its title
  and abstract support, and no specific figure from any of them is quoted.
- **Highlights** — bullets 1 and 5 are new and carry the S&T-intelligence contribution
  (corpus mining plus indicator construction; the field-level reliability diagnostic). They
  replace the v3 bullets on two-arm estimation and the focal-firm counter-case, both of which
  remain fully reported in the body. Character counts re-measured: 83 / 79 / 71 / 78 / 81, all
  ≤85.
- **Submission package** — `cover_letter.md` gains a "Methodological contribution to S&T
  information analysis" section and a rewritten scope paragraph; `highlights.md`,
  `submission_checklist.md`, `figure_captions.md`, `tables.md`, `supplementary_material.md`,
  `declarations.md` updated for the new title, with figure and table numbering explicitly
  re-verified as unchanged; `manuscript.docx` and `manuscript.pdf` rebuilt from
  `manuscript_v4.md`.

**What did not change.** Every coefficient, confidence interval, p-value, sample size, Wald
statistic, minimum detectable effect, Manski bound, year-by-year estimate and break year is
identical to v3 — verified by a token-level numeric diff of the two files, whose only
differences are the entity-rule precision/recall figures newly written into §3.1 and
section-number cross-references. All eight conflicting-evidence items (CF1–CF8) and all twelve
Non-claims are retained verbatim. **The v3 removal of Winall Hi-Tech Seed's financial,
commercial and governance content was not reverted in any form**, and Non-claim 10 stands.

**Still outstanding after v4** (unchanged from v3 unless noted):

- P4 — the field-by-field manual cross-check of parsed records against the original MARA
  announcements, still disclosed as outstanding in §3.4.
- P5 — Gong et al. (2026) full text still not accessible; title-level citation only.
- Piepho & Laidig (2024) volume/pages still to be confirmed against CrossRef.
- Seck et al. (2023), Burris et al. (2025) and Rangnekar (2000) remain deliberately uncited.
- **New at v4** — author confirmation required on three points raised in
  `plan/05_sti_reframing_brief.md` §1 that no automated pipeline can settle: that the user is
  first author; that the first author's affiliation is the S&T information institute (the
  requirement that the paper carry the home institute as first affiliation, which the S&T
  intelligence framing now makes disciplinarily coherent); and that the journal's impact
  factor and CAS tier be re-checked against the table for the actual year of publication.
- **New at v4** — the entity-resolution precision/recall figures written into §3.1 were taken
  from the project's existing planning documents rather than re-derived in this pass; if a
  referee asks, the labelled-subset validation should be re-run and the two numbers confirmed.
- **New at v4** — `plan/03_target_journal.md` was *not* updated with the assessment-criteria
  matching table from `plan/05_sti_reframing_brief.md` §1; that item sits in the brief's
  execution-order section rather than in the v4 task list and is left for a separate pass.
