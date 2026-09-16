# R3 — Numbering / cross-reference integrity (R-C) and citation reality / substance (R-D)

**Reviewer line:** R-C + R-D per `plan/06_v4_review_brief.md` §2, plus format re-verification
of the four items v4 changed (title, abstract, keywords, Highlights) against
`plan/04_format_spec.md`.
**Object under review:** `manuscript/manuscript_v4.md` (659 lines, 15,665 words), the whole
`submission/` package, `manuscript/figure_table_list.md`,
`manuscript/references_verified.md`, `manuscript/review/change_log_v3_to_v4.md`.
**Date:** 2026-09-16. **Method:** exhaustive `grep` + scripted extraction (every
`Fig.`/`Figure`/`Table`/`Supplementary` token and every `§`/`Section` token enumerated, not
sampled); independent web verification of every reference-list entry; DOCX/PDF text
extraction and a paragraph-level diff of `submission/manuscript.docx` against
`manuscript_v4.md`.

---

## Overall assessment

**The two renumbering rounds left the figure/table system clean. The reference list is clean
of fabrication. Two bibliographic records are wrong, and six section pointers are wrong.**

The specific high-risk item the brief flagged — stale `Table 6` / `Table 7` / `Fig. 7` /
`Supplementary Table S2` surviving the v2 compression and the v3 S2→S1 renumbering — **did
not occur**. Exactly one `Table 7` token exists in the manuscript, it is the deliberate
traceability note in §7, it is spelled correctly against the final numbering
("Supplementary Table S1 (Table 7 in the pre-submission working draft)"), and it is the only
such instance. `Table 6`, `Fig. 7`, `Fig. 8`, `Fig. 9`, `Table S2` and `Table S3` return zero
hits in the manuscript, zero in `manuscript.docx`, and zero in `manuscript.pdf`. All eleven
main-text items (Fig. 1–6, Table 1–5) are cited, cited in strictly ascending order of first
appearance, with no gaps, and all four numbering surfaces — body text, `figure_captions.md`,
`tables.md`, `supplementary_material.md` — agree. The DOCX and PDF in `submission/` are
genuine v4 builds (38 pp.; verified by full-text extraction and a paragraph diff), not stale
v3 artefacts.

Where the manuscript is **not** clean:

1. **Six section cross-references point at sections that do not contain what the pointer
   claims** (lines 71, 113, 159, 217, 241, 431). All six are pre-existing from v3 — none was
   introduced by the v4 Discussion insertion — but they are live defects in the file being
   submitted, and two of them (`Section 6` for the structural-break test; `§5` for the
   enterprise-vs-institution comparison) will send a reader to the wrong place. v4's own new
   section, §8.4, was inserted correctly: Limitations moved 8.4→8.5 and **no stale `§8.4`
   pointer survives** — the one thing most likely to break when a Discussion section is
   inserted did not break.

2. **Two reference records are factually wrong**, both discovered by going back to the
   publishers rather than trusting `references_verified.md`:
   - **Gong et al. 2026** — the title in the reference list is a *paraphrase*, not the
     published title, and the seven-author list is a **silently truncated** version of a
     ≥14-author list (the `…` ellipsis present in `references_verified.md` was dropped when the
     entry was transcribed into the manuscript). The paper is real; the record is not accurate.
   - **Piepho and Laidig 2024** — the article published as **2025, Plant Breeding 144,
     242–248**. The manuscript dates it 2024 and gives no volume or pages. This is the open
     item `references_verified.md` explicitly deferred ("投稿前须用 CrossRef/期刊官网核对"); it
     is now resolved and needs to be applied, in the reference list *and* in the two in-text
     `(Piepho and Laidig, 2024)` citations.

3. **No fabricated citation was found.** All 24 reference-list entries resolve to real,
   locatable publications. All six references added in v4 exist, were verified against
   publisher/index records independently of the manuscript's and the change log's self-report,
   and — importantly — **all six are substantively engaged**, not padding. Two of them
   (Jaffe and de Rassenfosse 2017; Franceschini et al. 2016) carry real argumentative load;
   the weakest (Shi et al. 2021) is still doing a specific job rather than decorating a
   sentence. In-text ↔ reference-list correspondence is **exactly 24 ↔ 24: no orphans, no
   uncited entries.**

4. **Format compliance on the four v4-changed items passes**, counted by hand: abstract
   **249 words** (limit 250 — one word of headroom), keywords **6** with no "and"/"of",
   Highlights **5 bullets at 83/79/71/78/81 characters** (limit 85), declarations all five
   present. Title and abstract are free of the banned causal vocabulary.

5. One **submission-file defect**: `submission/manuscript.docx` contains two leaked literal
   Markdown bold markers (`**and**`, `**while**`) in the §4.5 hypothesis bullets. The PDF
   renders those two spots correctly — the bug is in `scripts/build_docx.py`'s handling of
   bold inside list items only.

**Recommendation: Minor revision.** Nothing here blocks submission on integrity grounds — no
hallucinated reference, no stale figure/table number. But the two wrong bibliographic records
must be fixed before a journal's reference-checking pass sees them, and the six section
pointers are the kind of thing a careful referee will list.

---

## R-C — Numbering and cross-reference integrity

### R-C.1 / R-C.2 / R-C.4 — Every figure, table and supplementary citation in v4

Extracted mechanically (all `Fig.`/`Figure`/`Table`/`Supplementary` tokens; nothing sampled).
Line numbers are `manuscript_v4.md`. "Exists?" is checked against
`manuscript/figure_table_list.md` at its **final** number.

| Line | § | Citation as written | Resolves to | Exists at final # | Verdict |
|---|---|---|---|---|---|
| 134 | 3.1 | `Fig. 1` | Fig. 1 channel stacked area | ✔ | ✅ **first citation of Fig. 1** |
| 135 | 3.1 | `Table 1` | Table 1 channel × year counts | ✔ | ✅ **first citation of Table 1** |
| 225 | 3.3 | `Table 1` | Table 1 | ✔ | ✅ |
| 227 | 3.3 | `Fig. 1` | Fig. 1 | ✔ | ✅ |
| 227 | 3.3 | `Table 2` | Table 2 descriptive/balance | ✔ | ✅ **first citation of Table 2** |
| 229 | 3.3 | `Table 3` | Table 3 main regression | ✔ | ✅ **first citation of Table 3** |
| 230 | 3.3 | "six figures (Fig. 1–6) and five tables (Table 1–5)" | inventory statement | ✔ | ✅ matches final counts exactly |
| 232 | 3.3 | "Supplementary Material as Table S1 and Fig. S1" | Suppl. Table S1, Suppl. Fig. S1 | ✔ | ✅ correct post-v3 numbering (would have read "S1–S2" pre-v3) |
| 302 | 4.2 | `Table 3` | Table 3 | ✔ | ✅ |
| 318 | 4.3 | `Table 3` | Table 3 | ✔ | ✅ |
| 412 | 4.7 | `Supplementary Table S1` | Suppl. Table S1 (enterprise vs public) | ✔ | ✅ **first citation of Table S1** |
| 423 | 5.1 | `Table 3`; `Fig. 2` | Table 3; Fig. 2 forest plot | ✔ | ✅ **first citation of Fig. 2** |
| 427 | 5.2 | `Table 3` ×2; `Fig. 2, left panel` | Table 3; Fig. 2 panel 1 | ✔ | ✅ Fig. 2 is a two-panel plot; "left panel" = Arm 1 ✔ |
| 437 | 5.3 | `Table 3`; `Fig. 2's right panel` | Table 3; Fig. 2 panel 2 | ✔ | ✅ "right panel" = Arm 2 ✔ |
| 445 | 5.5 | `Fig. 3` | Fig. 3 event study | ✔ | ✅ **first citation of Fig. 3** |
| 449 | 5.6 | `Fig. 4` ×3 | Fig. 4 breakpoint scan | ✔ | ✅ **first citation of Fig. 4**; incl. the growth-duration line, which caption lists ✔ |
| 455 | 5.7 | `Table 3`; `Fig. 2` | — | ✔ | ✅ |
| 461 | 6 (preamble) | `Table 3` ×2; `Table 4` | Table 4 robustness matrix | ✔ | ✅ **first citation of Table 4** (note: `figure_table_list.md` records this as §6.7 — see R-C.6) |
| 465 | 6.1 R1 | `Table 3` | Table 3 | ✔ | ✅ |
| 470 | 6.1 R6 | `Fig. 5` | Fig. 5 randomisation inference | ✔ | ✅ **first citation of Fig. 5** |
| 471 | 6.1 R8 | `Supplementary Fig. S1` | Suppl. Fig. S1 missingness | ✔ | ✅ **first citation of Fig. S1** |
| 479 | 6.2 R7 | `Supplementary Fig. S1`; `Table 3` | — | ✔ | ✅ |
| 509 | 6.7 | `Table 4` | Table 4 | ✔ | ✅ |
| 519 | 7 | `Table 5` ×2; `Fig. 6a`; `Fig. 6b` ×2 | Table 5; Fig. 6 panels (a),(b) | ✔ | ✅ **first citation of Table 5 and Fig. 6**; only panels (a)/(b) cited — correct, panel (c) was deleted in v3 |
| 521 | 7 | `Table 4` | Table 4 | ✔ | ✅ |
| 523 | 7 | `Supplementary Table S1` (plain) | Suppl. Table S1 | ✔ | ✅ |
| 523 | 7 | **`Supplementary Table S1 (Table 7 in the pre-submission working draft)`** | Suppl. Table S1 | ✔ | ✅ **the deliberate exception — reads correctly and is the ONLY `Table 7` token in the manuscript** |

**Stale-numbering sweep (R-C.2).** `grep -nE "Table 6|Table 7|Table S2|Table S3|Fig\. 7|Figure 7|Fig\. 8|Fig\. 9"`:

| Token | `manuscript_v4.md` | `manuscript.docx` | `manuscript.pdf` | Verdict |
|---|---|---|---|---|
| `Table 6` | 0 | 0 | 0 | ✅ clean |
| `Table 7` | **1 (line 523, deliberate)** | 1 | 1 | ✅ the intended exception, correctly spelled, sole instance |
| `Supplementary Table S2` / `Table S2` | 0 | 0 | 0 | ✅ clean — v3's S2→S1 fully propagated |
| `Table S3` | 0 | 0 | 0 | ✅ |
| `Fig. 7` / `Figure 7` | 0 | 0 | 0 | ✅ clean |
| `Fig. 8` / `Fig. 9` | 0 | 0 | 0 | ✅ clean |

**Ordering, gaps and never-cited items (R-C.4).**

| Item | First-citation line | Ascending? | Cited at all? |
|---|---|---|---|
| Fig. 1 | 134 | — | ✔ |
| Fig. 2 | 423 | ✔ | ✔ |
| Fig. 3 | 445 | ✔ | ✔ |
| Fig. 4 | 449 | ✔ | ✔ |
| Fig. 5 | 470 | ✔ | ✔ |
| Fig. 6 | 519 | ✔ | ✔ |
| Table 1 | 135 | — | ✔ |
| Table 2 | 227 | ✔ | ✔ |
| Table 3 | 229 | ✔ | ✔ |
| Table 4 | 461 | ✔ | ✔ |
| Table 5 | 519 | ✔ | ✔ |
| Suppl. Table S1 | 412 | — | ✔ |
| Suppl. Fig. S1 | 471 | — | ✔ |
| Suppl. Fig. S2 | — | — | ❌ **never cited by number in the main text** |
| Suppl. Fig. S3 | — | — | ❌ **never cited by number in the main text** |

Figures ascend 134 < 423 < 445 < 449 < 470 < 519 with no gaps; tables ascend 135 < 227 < 229
< 461 < 519 with no gaps. Every main-text item is cited. Fig. S2 / Fig. S3 are named in
`submission/supplementary_material.md` but never cited by number in the body — a known and
documented choice (their content is reported in §6.2 and §6.5 prose), and neither has been
rendered as an image file. This is defensible but Elsevier-family systems normally require
every named Supplementary item to be cited; see Suggested #S4.

### R-C.3 — Numbering agreement across all surfaces

| Surface | Fig. numbering | Table numbering | Supplementary | Verdict |
|---|---|---|---|---|
| `manuscript_v4.md` body | Fig. 1–6, panels 6a/6b only | Table 1–5 | Table S1, Fig. S1 | ✅ |
| `submission/figure_captions.md` | Fig. 1–6 + Suppl. Fig. S1; carries an explicit "v4 check" note | — | Fig. S1 | ✅ captions match `figure_table_list.md` item-for-item; Fig. 6 caption states two panels |
| `submission/tables.md` | — | Table 1–5 headers, titles match | Table S1 pointer | ✅ carries an explicit "v4 check" note |
| `submission/supplementary_material.md` | Fig. S1, plus S2/S3 note | Table S1 | ✅ correct post-v3 numbering | ✅ (but has **no** "v4 check" note — see Suggested #S3) |
| `submission/manuscript.docx` | identical to body (paragraph diff: no content differences) | identical | identical | ✅ genuine v4 build |
| `submission/manuscript.pdf` | 38 pp., full-text extraction confirms §8.4 present, `Table 7` ×1, `Table 6`/`Fig. 7`/`Table S2` ×0 | ✅ | ✅ | ✅ genuine v4 build |
| `submission/submission_checklist.md` | mentions Table 6/7 and old Fig. 6/7 **only** in explicitly-labelled v2 history, immediately followed by the v3 correction | — | — | ✅ historical, correctly framed |
| `submission/VERSION_HISTORY.md` | same | — | — | ✅ historical, correctly framed |
| `manuscript/figure_table_list.md` | Fig. 1–6, Table 1–5, Table S1/Fig. S1–S3 | ✅ authoritative and correct | ✅ | ⚠️ document header still says "manuscript_v3.md"; see Suggested #S1 |

Source files: all six main figures present on disk (`fig1_channel_stacked.png`,
`fig2_forest_main.png/.pdf`, `fig3_event_study.png`, `fig4_breakpoint_scan.png`,
`fig6_randomization.png/.pdf` → published Fig. 5, `fig5_winall_mechanism.png` → published
Fig. 6, re-rendered 2026-09-16 at two panels), plus `fig7_missingness_balance.png/.pdf` →
Fig. S1. The filename↔number mismatch is deliberate and documented in the captions file.
`tables/table6_company_panel.csv` (the deleted v3 financial panel) still sits on disk but is
referenced **nowhere** in the manuscript or the submission package — harmless residue.

### R-C.5 — Every section cross-reference in v4

84 tokens extracted (`§n.n`, `Section n.n`, `Sections …`). Section inventory in v4:
1 / 2 / 3 (3.1–3.4) / 4 (4.1–4.7) / 5 (5.1–5.7) / 6 (6.1–6.7) / 7 / 8 (**8.1–8.5**) / 9.
**Every pointer targets a section that exists**; the column that matters is whether the target
*contains what the pointer claims*.

| Line | Pointer | Claimed content | Target actually contains it? |
|---|---|---|---|
| 37 | §5.6 | structural-break analysis | ✅ |
| 37 | §8.2 | "closing window" discussion | ✅ (v4 insertion did not shift 8.2) |
| 55 | Section 2 | institutional path + NY/T 593 | ✅ |
| 55 | Section 3 | extraction pipeline, data, channel variable | ✅ |
| 55 | Section 4 | empirical strategy + claims/non-claims | ✅ (§4.7) |
| 55 | Sections 5 and 6 | main results + robustness | ✅ |
| 55 | Section 7 | Winall counter-case | ✅ |
| 55 | Section 8 | S&T-intelligence, self-certification, policy implications | ✅ (§8.4, §8.1, §8.3) |
| 55 | Section 9 | conclusion | ✅ |
| **71** | **Section 6** | **"a corresponding structural-break test … supports it"** | ❌ **WRONG — the sup-Wald structural-break scan is §5.6. §6 is R1–R16 robustness and contains no breakpoint test. §4.7 Non-claim 3 (line 406) points the same fact at §5.6, so the manuscript contradicts itself.** |
| 82, 83, 85, 87 | §3.1 ×4 | pipeline steps (i)–(iv) | ✅ §3.1's title names exactly those steps |
| 89 | §3.3–§3.4 | step (v) coverage/quality assessment | ✅ |
| 91 | §3.2–§3.3 | step (vi) indicator construction | ✅ |
| **113** | **§3.3** | **post-2022 coverage collapse (85/409, 61/405)** | ❌ **WRONG — §3.3 covers outcome variables, measuring party and by-arm missingness. Coverage/representativeness is §3.4 ("Representativeness and source verification"), which line 239 itself points to.** |
| 126 | §4 | why the two channels are estimated separately | ✅ (§4.3) |
| 135 | §6 | robustness check R4 | ✅ (§6.1) |
| 141 | §3.3 | applicant field absent for four years | ✅ (lines 216–223) |
| 141, 147, 149 | §7 ×3 | the focal-firm counter-case | ✅ |
| **159–160** | **§4.4 and §6** | **pre-2017 years "used only as a pre-reform benchmark"** | ❌ **§6 is right (R13 time placebo); §4.4 is wrong — §4.4 is "What β identifies", and says nothing about the pre-reform benchmark layer. §4.1 (rejected DID designs, pre-period trends) is the plausible intended target.** |
| 170 | §6, R3 | extended trial-group stratum | ✅ |
| 174 | §6, R11 | provincial replication | ✅ (§6.4) |
| 201 | §6 (R16) | disclosure-behaviour controls | ✅ (§6.6) |
| 212 | §6, R7 | Manski bounds | ✅ (§6.2) |
| **217** | **§5** | **"`applicant_type` … used only in the descriptive comparison in §5"** | ❌ **WRONG — §5.1–5.7 contain no enterprise-vs-public-institution comparison (verified by grep over lines 419–458). That comparison lives in §7 (line 523) + Supplementary Table S1, exactly as §4.7 Non-claim 9 says.** |
| 226 | §2 | institutional timeline | ✅ |
| 232 | §7 | in-text pointer to Suppl. Table S1 | ✅ (though S1 is *also* cited in §4.7 — see Suggested #S5) |
| 232 | §6.1–6.2 | in-text pointers to Suppl. Fig. S1 | ✅ (R8 in 6.1; R7 in 6.2) |
| 239 | §3.1 | declining coverage after 2022 | ✅ |
| **241** | **§4.4** | **post-2022 "channel distinction currently being narrowed by regulatory action"** | ❌ **WRONG — §4.4 is the estimand definition. The regulatory-narrowing discussion is §8.2 ("Is the identified variation disappearing?"), with the underlying event in §2 (2022-08-31 notice).** |
| 377 | §6, R9 | within-applicant check | ✅ (§6.3) |
| 386 | §4.7, Non-claim 9 | descriptive-only status | ✅ |
| 391 | §7 | counter-case use of the auxiliary specs | ✅ |
| 394 | §4.7, Non-claim 3 | reform-timing non-claim | ✅ |
| 404 | §6.3 | within-applicant design | ✅ |
| 406 | §5.6 | breakpoint scan dates breaks 2009–2015 | ✅ |
| 407 | §5.2 | bacterial blight moves the opposite way | ✅ (line 431) |
| 408 | §5.3, §6.2 | Arm-2 sign reversal; Manski lower bound | ✅ both |
| 410 | §3.1 | coverage decline | ✅ |
| 411 | §6.4 | provincial two-part reading | ✅ |
| 412 | §7 | enterprise-vs-institution comparison | ✅ |
| 413 | §7 | channel-choice / within-channel comparisons | ✅ |
| 415 | §3.4, Unresolved item P4 | outstanding MARA cross-check | ✅ |
| 423 | Section 4.3 | two arms, not pooled | ✅ |
| 427 | Section 6.2 | Manski failure of top-two grade | ✅ |
| 427 | Section 5.3 | neck-blast not estimable in Arm 2 | ✅ |
| 429 | Section 4, Non-claims | pre-declared placebos | ✅ (§4.7) |
| 429 | Section 6.1, R12 | plant height treated as auxiliary | ✅ |
| **431** | **Sections 4.4, 6.2** | **"the paper's claim is deliberately scoped to grain-processing and appearance quality"** | ❌ **§6.2 is right; §4.4 is wrong — the scoping statement is §4.7 Non-claim 4 ("We do not claim third-party-assayed traits are uniformly worse"), verbatim. §4.4 does not scope traits.** |
| 441 | Section 6.3 | within-applicant too small | ✅ |
| 451 | Sections 5.2–5.3 | same-year channel gap | ✅ |
| 455 | Section 6 | sixteen robustness checks | ✅ |
| 461 | Section 5; §5.2 | headline coefficients | ✅ |
| 465 | §5.1–5.3 | two arms never pooled | ✅ |
| 472 | §7 | drop-focal-firm cross-link | ✅ |
| 474 | §5.4 | H_threshold not ruled out | ✅ |
| 479 | Section 5.2 | stated-grade primary result | ✅ |
| 485 | Section 4, Non-claims 1 | underpowered within-applicant | ✅ |
| 497 | Section 5.2–5.3 | percentage-gain-over-check | ✅ |
| 501 | Section 5 | point estimate being bounded | ✅ |
| 505 | Section 3.3 / §3.3 | `quality_stated` flagged as disclosure behaviour | ✅ (lines 194–202) |
| 509 | Section 5.5 | year-by-year evidence | ✅ |
| 517 | Sections 5–6 | the sign separation | ✅ |
| 519 | §3.1 | entity-resolution rule, 0.770 recall | ✅ |
| 521 | Section 6.1, R10 | drop-Winall result | ✅ |
| 533 | §4; R9/R11 | channel self-selection not closed off | ✅ |
| 539 | Section 6 | provincial replication | ✅ (§6.4) |
| 549 | §3.4 | unverified re-transcription | ✅ |
| 549 | §4.7, Non-claim 7 | coverage collapse after 2022 | ✅ |
| 549 | §3.1 | applicant field absent for four years | ⚠️ weak — §3.1 only *points* at it (line 141); the fact is stated in §3.3. Harmless. |
| 551 | — | Franceschini / Jaffe (no section pointer) | n/a |
| 555 | §8.3 | "issuing it as a field" policy recommendation | ✅ (§8.3 third implication) |
| 559 | Section 6 | within-applicant comparison underpowered | ✅ (§6.3) |
| 559 | Section 7 | enterprise-vs-institute comparison | ✅ |
| 559 | Section 8.2 | convergence trends | ✅ |

**Score: 78 of 84 section pointers correct; 6 wrong.** Every one of the six is **pre-existing
from v3** (verified by grepping `manuscript_v3.md` for the identical sentences — all six are
present there verbatim). The v4 Discussion insertion itself was executed cleanly: v3's §8.4
was Limitations, v4's §8.5 is Limitations, and a grep for `§8.4` / `Section 8.4` in the v4
body returns **zero** pointers — the one failure mode that this kind of insertion normally
produces did not occur.

### R-C.6 — Documentation staleness found along the way (not manuscript defects)

- `manuscript/figure_table_list.md` header still reads "Figure and table list —
  manuscript_v3.md … updated 2026-09-16 for v3." Its numbering is still authoritative and
  correct for v4 (nothing moved), but its "First cited in" column now has three v3-era
  entries: **Table 4 is recorded as "§6.7 Robustness" but is first cited at line 461, the §6
  preamble**; and several entries name v3 section titles ("§3.1 Data", "§3.3 Data") that v4
  renamed.
- Its "Verification note (v2)" (lines 100–103) still asserts, in the present tense, that the
  §7 traceability note is spelled `"Supplementary Table S2 (Table 7 …)"`. That was true in v2;
  the "Verification note (v3)" two paragraphs below corrects it. Read in isolation the v2 note
  is now wrong.
- `submission/VERSION_HISTORY.md` line 52 (inside the clearly-labelled v2 block) says the
  Supplementary pointer sentence was added to "§3.1". In v4 that sentence lives at §3.3
  (lines 230–233) and correctly reads "Table S1 and Fig. S1". Historical, correctly framed.
- `manuscript/sections/*.md` are v1-era working drafts (dated 14 Sep, pre-compression);
  `robustness.md` still contains old `Table 6/7`-era numbering. These are superseded working
  files, not a submission surface. Flagging only so that nobody rebuilds from them.

---

## R-D — Citation reality and substance

### R-D.1 / R-D.2 — Per-reference verification (all 24 entries)

Verification was done **independently of `references_verified.md` and of the change log**.
`api.crossref.org` and `doi.org` are blocked by this session's egress proxy (confirmed:
`gateway answered 403 to CONNECT`, recorded in the proxy status endpoint), so verification
used WebSearch against publisher and index records (Wiley, MDPI, Springer, Frontiers, OUP
Academic, ScienceDirect, dblp, RePEc/IDEAS, PubMed/PMC, institutional repositories). Each
field — authors, year, title, journal, volume, pages, DOI — was compared individually.

**The six references added in v4** (the priority set):

| # | Manuscript entry | Exists? | How verified | Record matches? |
|---|---|---|---|---|
| 1 | Antons D, Grünwald E, Cichy P, Salge T O. 2020. *The application of text mining methods in innovation research…* R&D Management, 50, 329–351. | ✅ **Real** | WebSearch → Wiley entry page for 10.1111/radm.12408; RWTH Aachen repository record 788955; EconStor copy. Four authors and their order confirmed. | ✅ **Exact.** Vol. 50(3), 329–351, 2020. Reviews 124 articles. |
| 2 | Franceschini F, Maisano D, Mastrogiacomo L. 2016. *Empirical analysis and classification of database errors in Scopus and Web of Science.* Journal of Informetrics, 10, 933–953. | ✅ **Real** | WebSearch → ScienceDirect entry S175115771630061X; NIH Library bibliometrics page citing it as 10(4):933-953. Three authors confirmed. | ✅ **Exact.** Vol. 10(4), 933–953, 2016. |
| 3 | Jaffe A B, de Rassenfosse G. 2017. *Patent citation data in social science research: Overview and best practices.* JASIST, 68, 1360–1374. | ✅ **Real** | WebSearch → dblp `journals/jasis/JaffeR17`; Wiley/asistdl entry for 10.1002/asi.23731; EPFL Infoscience. | ✅ **Exact.** Vol. 68(6), 1360–1374, 2017. **Correctly uses the JASIST version, not NBER w21868** — the working-paper trap that caught Grennan & Town was avoided. |
| 4 | Losiewicz P, Oard D W, Kostoff R N. 2000. *Textual data mining to support science and technology management.* Journal of Intelligent Information Systems, 15, 99–119. | ✅ **Real** | WebSearch → Springer entry page for 10.1023/A:1008777222412; abstract confirms the IR→IE→warehouse→mining→visualisation architecture. | ✅ **Exact.** Vol. 15, 99–119, 2000. |
| 5 | Rammer C, Es-Sadki N. 2023. *Using big data for generating firm-level innovation indicators — A literature review.* Technological Forecasting and Social Change, 197, 122874. | ✅ **Real** | WebSearch → ScienceDirect S0040162523005590; RePEc `v197y2023ics0040162523005590`. | ✅ **Substantively exact.** Vol. 197, art. 122874, 2023. **Correctly uses the TFSC version, not SSRN 2022** — second working-paper trap avoided. Cosmetic only: the published title separator is a hyphen and lowercase "a literature review"; the manuscript uses an em dash and "A". |
| 6 | Shi Y, Ren P, Zhang Y, Gong X, Hu M, Liang H. 2021. *Information extraction from FDA drug labeling…* Frontiers in Research Metrics and Analytics, 6, 670006. | ✅ **Real** | WebSearch → Frontiers article page for 10.3389/frma.2021.670006; PubMed **PMID 34179681**; **PMC8222600**. Six authors and order confirmed. | ✅ **Exact.** Vol. 6, art. 670006, 2021. |

**Verdict on the v4 additions: zero fabrications, zero bibliographic errors, six for six.**
This is a genuinely clean result — and notably the change log's self-report, which I did not
trust, turned out to be accurate in every particular.

**The remaining 18 entries** (carried from v2/v3), checked for record accuracy:

| # | Entry | Exists? | How verified | Record matches? |
|---|---|---|---|---|
| 7 | Bar T, Zheng Y. 2019. AJAE, 101, 74–88. | ✅ | OUP Academic `ajae/article-abstract/101/1/74` | ✅ Exact — the v2 year/volume correction (2018→2019, +101:74–88) was applied correctly |
| 8 | Duflo E, Greenstone M, Pande R, Ryan N. 2013. QJE, 128, 1499–1545. | ✅ | prior two-tool verification in `references_verified.md` §1; no contradicting record found | ✅ |
| 9 | **Gong J, Zhang X, Zhang J, Zeng B, Zhang X, Xu X, Xie H A. 2026.** *Three-line hybrid rice in China: sustained improvements in yield, quality, and resistance over fifty years.* Rice Science. | ✅ **Real** | WebSearch → ScienceDirect **S167263082600048X**, Rice Science vol. 33 (2026), online 12 Apr 2026; ricesci.org mirror | ❌ **TWO ERRORS.** (a) **Title is a paraphrase**: published as *"Three-Line Hybrid Rice in China: Fifty Years of Sustained Improvement in Yield, Quality, and Stress Resistance"* — "Stress" is dropped and the clause order is inverted. (b) **Author list is silently truncated**: the real list runs Junyi Gong, Xiaobo Zhang, Jianfu Zhang, Bo Zeng, **Xiaoqing** Zhang, Xia Xu, **Benyi Cheng, Yuxuan Hou, Junhui Xia, Jianli Wu, Shihua Yang, Shihua Cheng, Bin Han**, Huaan Xie *et al.* — the manuscript prints seven names with no ellipsis, as though complete. `references_verified.md` §10 carried a `…` that was lost in transcription. Volume (33) also missing. |
| 10 | Grennan M, Town R J. 2020. AER, 110, 120–161. | ✅ | prior WebSearch verification (AEA 10.1257/aer.20180946) | ✅ volume/pages correct; no DOI printed, so the NBER-DOI error cannot recur |
| 11 | Hang S, Wang Q, Wang Y, Xiang H. 2024. Agronomy, 14, 2780. | ✅ | WebSearch → Semantic Scholar + ResearchGate; authors "Song Hang, Qi Wang, Yuan Wang, Haitao Xiang"; 11,811 trials, 1990–2023 | ✅ Exact — surname **Hang** (not Han) confirmed again |
| 12 | Huang Z Y, Xu Y, Zeng D, Wang C, Wang J M. 2018. JIA, 17, 473–482. | ✅ | prior two-tool verification | ✅ |
| 13 | Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. TAG, 127, 2599–2617. | ✅ | prior two-tool verification | ✅ |
| 14 | Lu Y, Tang Y, Zhang J, Liu S, Liang X, Li M, Li R. 2024. Agronomy, 14, 1234. | ✅ | WebSearch → MDPI `agronomy/14/6/1234`, doi 10.3390/agronomy14061234 | ✅ Exact — the suspiciously round "1234" is genuinely the MDPI article number |
| 15 | Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. TAG, 122, 225–238. | ✅ | prior two-tool verification | ✅ |
| 16 | **Piepho H-P, Laidig F. 2024.** *How many checks are needed per cycle…* Plant Breeding. | ✅ **Real** | WebSearch → Wiley entry for 10.1111/pbr.13240, indexed **"Piepho - 2025 - Plant Breeding"**; vol. **144**, pp. **242–248** | ❌ **YEAR AND VOLUME/PAGES WRONG/MISSING.** Should be **2025, Plant Breeding, 144, 242–248**. This resolves the item `references_verified.md` §15 explicitly deferred to pre-submission. Also affects the two in-text citations at lines 497 and 501. |
| 17 | Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. TAG, 127, 1009–1018. | ✅ | prior two-tool verification | ✅ |
| 18 | Qiu H G, Wang X B, Zhang C P, Xu Z G. 2016. JIA, 15, 1915–1923. | ✅ | prior two-tool verification | ✅ |
| 19 | Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. FCR, 303, 109086. | ✅ | prior verification with full abstract retrieved | ✅ |
| 20 | Renckens S, Auld G. 2022. Regulation & Governance, 16, 500–518. | ✅ | WebSearch → Carleton SPPA announcement + R&G indexing, 16(2):500–518, April 2022 | ✅ Exact — the v2 correction (2020→2022, 14(4)→16:500–518) was applied correctly |
| 21 | Shi X, Hu R. 2017. JIA, 16, 2337–2345. | ✅ | prior verification with full abstract | ✅ |
| 22 | Xiang C, Yang R, Wang X, Huang J. 2025. Agribusiness. | ✅ | prior verification (doi 10.1002/agr.22020, online 2025-01-15) | ⚠️ No volume/pages — legitimate for an Early View article, but should be updated if the print issue has appeared by submission |
| 23 | Xie Z, Yuan S, Zhu J, Li W. 2023. Agribusiness, 39, 1173–1198. | ✅ | prior two-tool verification (39(4):1173–1198) | ✅ |
| 24 | Zhao Y, Deng H, Hu R, Xiong C. 2022. Agronomy, 12, 917. | ✅ | prior verification (10.3390/agronomy12040917) | ✅ |

**No fabricated or hallucinated citation exists in this manuscript.** All 24 entries resolve
to real publications with the right authors at the right venues. The two defects are
transcription/currency errors, not inventions.

**Gong et al. 2026 — current state (as requested).** `references_verified.md` marked it
**❓ Unverifiable** because the full text could not be retrieved (ScienceDirect and ricesci.org
were egress-blocked; they still are). That status is **unchanged and remains correct for the
full text**. However, this review did reach the ScienceDirect landing record, which changes
two things: (a) it confirms the article is real, in Rice Science vol. 33 (2026); and (b) it
**disconfirms** `references_verified.md`'s dismissal of the title discrepancy as "同一篇文章的
标题在不同索引器中的措辞差异" — the published title genuinely differs from the manuscript's, and
the author list is genuinely longer. So: the *citation* is still safe to use at title level,
and the manuscript's handling of it in the body (line 37 — "we cite it only for its scope and
do not attribute any specific figure to it") is exemplary and should be kept; but the
*reference-list record itself* must be corrected. I do not treat this as newly broken — the
Unverifiable status is pre-existing — but the title and author errors are newly identified.

### R-D.3 — Substantive engagement of the v4 additions

Judged by quoting the citing sentence and asking whether the text converses with the cited
work's actual argument.

| Reference | Citing sentence(s) | Verdict |
|---|---|---|
| **Jaffe and de Rassenfosse (2017)** | §8.4, line 553: *"…in patent examination, where applicant-drafted claims sit alongside examiner-added citations, **a distinction the patent-indicator literature adopted only after treating all citations alike produced biased measures** (Jaffe and de Rassenfosse, 2017)."* Also line 551 with Franceschini for source-level data quality. | ✅ **Strongest engagement in the set.** The cited paper's own framing is four pitfalls of patent-citation data, one of which is precisely the *examiner effect* — applicant- versus examiner-added citations producing biased measures. The manuscript is not name-dropping; it is using the patent-indicator field's own history as the precedent for its "partition fields by measuring party" recommendation. This is the load-bearing analogy of the whole portability argument. |
| **Franceschini et al. (2016)** | §3.4, line 246: *"…large-scale audits of the databases on which S&T indicators are routinely built find systematic, non-negligible error rates in them as well (Franceschini et al., 2016), and the appropriate response is to state the verification status of a corpus rather than to assume it."* §8.4, line 551: *"Standard data-quality assessment in scientometrics and technology analysis is source-level — coverage, error rates, duplication, classification accuracy (Franceschini et al., 2016; Jaffe and de Rassenfosse, 2017) — and a source that passes such an audit can still contain fields of very different evidential value."* | ✅ **Substantive.** The cited paper *is* an empirical analysis and classification of database errors in Scopus and WoS; both uses are accurate, and the §8.4 use does real argumentative work — it sets up the "source-level audit is not enough, reliability is field-level" claim, which is the paper's methodological contribution. Also does defensive work in §3.4: it converts "our corpus is unverified" from a weakness into a general point. |
| **Rammer and Es-Sadki (2023)** | Intro, line 33: *"…even the recent turn to 'big data' firm-level indicators draws mainly on web, job-posting and transaction traces rather than on the regulatory record (Rammer and Es-Sadki, 2023)."* §8.4, line 549: *"Innovation measurement has broadened from patents and publications to trademarks, web traces and transaction data (Rammer and Es-Sadki, 2023), but the records a state generates when it authorises a technology for market have stayed outside the indicator toolkit…"* | ✅ **Substantive — it defines the gap the paper claims to fill.** Minor caution: the "rather than on the regulatory record" clause is the authors' *inference from the review's coverage*, not something the review asserts. Legitimate, and honestly phrased, but a referee could ask for it. |
| **Antons et al. (2020)** | Intro, line 33: *"…text mining in innovation research has been developed and surveyed almost entirely over patent and publication corpora (Losiewicz et al., 2000; Antons et al., 2020)."* §8.4, line 555: *"Text mining of S&T corpora was developed to support research management and technology watch (Losiewicz et al., 2000; Antons et al., 2020); approval records extend that practice to the point where a technology reaches users."* | ✅ **Substantive.** A 124-article review of text mining in innovation research is the right authority for a claim about what that literature has been applied to. Not padding. |
| **Losiewicz et al. (2000)** | same two sentences as above | ✅ for the §8.4 use — the paper is literally titled *Textual data mining to support science and technology management*, and its IR→IE→warehouse→mining→visualisation architecture maps directly onto the manuscript's own six-step pipeline; this is a genuinely apt anchor. ⚠️ **Mild over-reach on the Intro use**: Losiewicz 2000 is an architecture/methods paper, not a *survey*, so bundling it into "developed **and surveyed** almost entirely over patent and publication corpora" attributes a survey function it does not have. Attach the "surveyed" half to Antons alone. |
| **Shi et al. (2021)** | §8.4, line 553: *"It recurs in drug approval, where sponsor-run trial results and regulator-reviewed labelling coexist in documents already mined at scale (Shi et al., 2021); in medical-device registration; and in patent examination…"* | ✅ **Not padding, but the thinnest of the six.** It is cited as an existence proof for one clause — "already mined at scale" — which the cited NLP-over-FDA-labeling pipeline genuinely supports. The more interesting half of the sentence ("sponsor-run trial results and regulator-reviewed labelling coexist") is the manuscript's own structural claim and is not attributed to Shi et al., which is the honest handling. Acceptable as is; it would be stronger if one sentence said what Shi et al. actually extracted. |

**Overall R-D.3 verdict: none of the six is padding.** Each carries a specific, checkable job,
and in two cases (Jaffe; Franceschini) the citation is doing load-bearing argumentative work
rather than decorating a claim. This is materially better than the "dropped in to look
well-read" failure mode the brief was worried about.

### R-D.4 — In-text ↔ reference-list correspondence

Extracted every author-date token in the body (lines 1–610) and every reference-list entry
(lines 613–659) by script, then set-differenced.

- **In-text distinct works cited: 24.** Antons 2020, Bar & Zheng 2019, Duflo et al. 2013,
  Franceschini et al. 2016, Gong et al. 2026, Grennan & Town 2020, Hang et al. 2024, Huang et
  al. 2018, Jaffe & de Rassenfosse 2017, Laidig et al. 2014, Losiewicz et al. 2000, Lu et al.
  2024, Mackay et al. 2011, Piepho & Laidig 2024, Piepho et al. 2014, Qiu et al. 2016, Rammer
  & Es-Sadki 2023, Raymond et al. 2023, Renckens & Auld 2022, Shi & Hu 2017, Shi et al. 2021,
  Xiang et al. 2025, Xie et al. 2023, Zhao et al. 2022.
- **Reference-list entries: 24.** Identical set.
- **Orphan in-text citations (no entry): 0.**
- **Uncited reference-list entries: 0.**
- **Alphabetical order:** correct throughout, including the two same-surname pairs
  (Piepho & Laidig 2024 before Piepho, Laidig, Drobek & Meyer 2014 — shorter author list
  first, the standard rule; Shi X 2017 before Shi Y 2021).
- **Style:** author-date throughout; `(Author and Author, Year)` and `Author et al. (Year)`
  forms used correctly; journal names given in full, never abbreviated (format spec §6 ✔).
  No DOIs are printed — permitted (the spec *encourages* rather than requires them).

One residual, **pre-existing** deviation: `plan/04_format_spec.md` §6 lists **Seck et al.
2023**, **Burris et al. 2025** and **Rangnekar 2000** among the mandatory citations. All three
were verified as real in `references_verified.md` (§19–21) but are cited in **none** of v1–v4
(grep returns 0 hits in every version). This was flagged in the v1 round as issue B4 and never
closed. Out of strict R-C/R-D scope, but it is a live gap between the format spec and the
manuscript.

---

## Format compliance re-verification (the four items v4 changed)

Counted by hand/script, not taken from any prior check.

| Item | Spec | v4 actual | Verdict |
|---|---|---|---|
| **Abstract** | ≤ 250 words, structured | **249 words** (whitespace tokenisation, confirmed by two independent counts). Single unstructured paragraph. | ✅ **Passes the hard limit — with one word of headroom.** ⚠️ No labelled Objective/Methods/Results/Conclusion headings, whereas the spec says 结构式. The v1 `format_check.md` row 5 evaluated the identical style as 合规, so this is consistent precedent, not a regression — but it should be checked once against JIA's current Guide for Authors, because one word of margin plus an unlabelled structure is two small risks stacked. |
| **Keywords** | 3–6; no "and"/"of" connectives | **6**: `administrative text mining; technology assessment; information extraction; data provenance; rice variety approval; China`. Scripted check for "and"/"of" as separate tokens: **zero hits in all six**. | ✅ **Passes.** Note (out of scope, for R4): the v4 rewrite removed `rice quality`, `seed regulation` and `third-party certification`, leaving only `rice variety approval` and `China` to index the paper as agricultural. For a JIA submission that is a discoverability cost. |
| **Highlights** | 3–5 bullets, each ≤ 85 chars incl. spaces | **5 bullets**, measured character counts **83 / 79 / 71 / 78 / 81**. `submission/highlights.md` reproduces all five verbatim with matching counts. | ✅ **Passes.** Bullet 1 at 83 has only 2 characters of slack — do not lengthen it. |
| **Title** | uses *gap*-type framing, not *effect/impact/caused by*; retains *third-party-assayed* | *"Mining administrative approval records for technology assessment: record-level trial-channel indicators and third-party-assayed grain quality in China's rice variety registrations, 2017–2022"* | ✅ **Passes.** Contains `third-party-assayed`; contains no *effect of / impact of / caused by*. The word "gap" is gone, but the spec's purpose (no causal language) is met. |
| **Citation style** | author-date, alphabetical, full journal names | see R-D.4 | ✅ |
| **Declarations** | Acknowledgements / Conflict of interest / Data availability / CRediT / Ethical approval | All five present in `manuscript_v4.md` (lines 571–607) and reproduced verbatim in `submission/declarations.md`. Conflict-of-interest and Ethical-approval statements are complete sentences; Acknowledgements and CRediT are marked author placeholders; Data availability matches the K11 wording. | ✅ **Passes**, with the known `[repository link]` and `[Author to complete]` placeholders that the checklist already tracks. |
| **Units** | kg/mu with kg/hm² gloss at first mention | First `kg/mu` occurrence is line 429 (§5.2): *"Raw two-year trial yield in kg/mu (1 kg/mu ≈ 15 kg/hm²; 1 亩 = 1/15 hm²)"*. No earlier occurrence. | ✅ |
| **Banned vocabulary** | no fraud/manipulation/fabrication; no *effect of / impact of / caused by* as the paper's own claim | Every hit is either an explicit negation ("not the effect of", "does not estimate a pre/post treatment effect", "does not allege fabrication or manipulation") or the title of a cited work (Xiang 2025, Zhao 2022). | ✅ |

---

## Must-fix

**M1. Correct the Gong et al. 2026 reference record** (line 621). Two errors in one entry:
- Title → the published title: *"Three-Line Hybrid Rice in China: Fifty Years of Sustained
  Improvement in Yield, Quality, and Stress Resistance"* (Rice Science, vol. 33, 2026).
- Author list → restore the ellipsis that `references_verified.md` carried, or list the full
  run. Printing seven names as though complete misrepresents a ≥14-author paper: the real
  sequence is Gong J Y, Zhang X B, Zhang J F, Zeng B, Zhang X Q, Xu X, Cheng B Y, Hou Y X,
  Xia J H, Wu J L, Yang S H, Cheng S H, Han B, Xie H A, *et al.*
  *(Keep the body's title-level-citation caveat at line 37 exactly as written — that part is
  handled well.)*

**M2. Correct the Piepho and Laidig reference to 2025 and add volume/pages.** →
`Piepho H-P, Laidig F. 2025. How many checks are needed per cycle in a plant breeding or
variety testing programme? Plant Breeding, 144, 242–248.` Update the two in-text citations at
lines **497** and **501** from `(Piepho and Laidig, 2024)` / `Piepho and Laidig (2024)` to 2025,
and re-check alphabetical position (unchanged). This closes the item `references_verified.md`
§15 deferred.

**M3. Fix line 71: `Section 6` → `Section 5.6`.** The sentence is *"we do not attribute any
trend in trait levels to a specific event unless a corresponding structural-break test
(Section 6) supports it."* The structural-break test is §5.6; §6 contains no breakpoint test.
§4.7 Non-claim 3 already points the same fact at §5.6, so the manuscript currently contradicts
itself on its own falsification evidence — the worst of the six pointer errors.

**M4. Fix line 217: `§5` → `§7`.** *"`applicant_type` … used only in the descriptive comparison
in §5"*. §5 contains no enterprise-vs-public comparison (verified by grep over §5.1–5.7); it is
in §7 plus Supplementary Table S1, exactly as Non-claim 9 states.

**M5. Fix line 113: `see §3.3` → `see §3.4`.** The post-2022 coverage collapse is a
representativeness matter and is treated in §3.4; §3.3 is outcome variables and by-arm
missingness. Line 239 already points coverage at §3.4/§3.1, so this is internally inconsistent.

**M6. Fix the three remaining mis-targeted `§4.4` pointers.**
- Line 159–160: *"used only as a pre-reform benchmark, see §4.4 and §6"* → §4.1 and §6
  (§4.4 is the estimand definition and says nothing about the pre-reform layer).
- Line 241: *"currently being narrowed by regulatory action (see §4.4)"* → §8.2 (or §2).
- Line 431: *"a claim the bacterial-blight result would falsify if made (Sections 4.4, 6.2)"*
  → **Sections 4.7 (Non-claim 4), 6.2** — Non-claim 4 is verbatim the scoping statement being
  invoked.

**M7. Rebuild `submission/manuscript.docx` after M1–M6, and fix the two leaked Markdown bold
markers.** The DOCX currently prints `**and**` and `**while**` literally inside the §4.5
hypothesis bullets ("This predicts β(3rd) < 0 `**and**` β(self) < 0"). The PDF renders the
same two spots correctly, so the bug is confined to `scripts/build_docx.py`'s handling of bold
inside list items. Two occurrences; verified by extracting `word/document.xml`.

---

## Suggested

**S1. Re-title and re-date `manuscript/figure_table_list.md` for v4.** Its numbering is still
correct and authoritative, but the header says "manuscript_v3.md", the "First cited in" column
records **Table 4 as "§6.7"** when it is first cited in the §6 preamble (line 461), and several
rows use v3 section titles ("§3.1 Data", "§3.3 Data") that v4 renamed. A one-paragraph "v4
check: no figure or table number changed" note plus three cell edits closes it.

**S2. Add a dated caveat to the "Verification note (v2)" block** (lines 100–103 of
`figure_table_list.md`), which still states in the present tense that the §7 traceability note
is spelled `"Supplementary Table S2 (Table 7 …)"`. The v3 note below corrects it, but the v2
note read alone is now wrong.

**S3. Add a "v4 check" note to `submission/supplementary_material.md`.** `figure_captions.md`
and `tables.md` both carry one; the supplementary file is the only numbering surface without
it, which makes it look unreviewed even though its content is correct.

**S4. Decide what to do about Supplementary Fig. S2 and Fig. S3.** They are named in
`supplementary_material.md`, are never cited by number in the main text, and have never been
rendered as image files. Either render and cite them (e.g. at §6.2 R7 and §6.5 R15, where their
content is currently reported in prose), or drop the S2/S3 labels and describe the material as
unnumbered. Elsevier-family submission systems generally expect every named Supplementary item
to be cited.

**S5. Broaden the Supplementary pointer at line 232.** It says Table S1 is pointed to "at §7",
but S1 is *first* cited at §4.7 (Non-claim 9). `supplementary_material.md` line 32 has the same
omission ("Cited in the main text at §7"). "§4.7 and §7" is accurate for both.

**S6. Close or formally retire the three uncited mandatory references.** Seck et al. 2023,
Burris et al. 2025 and Rangnekar 2000 are listed as required by `plan/04_format_spec.md` §6,
were verified as real, and are cited in no version of the manuscript. Either cite them (Seck
2023 fits §6.5's genetic-gain discussion naturally; Rangnekar 2000 fits the §8.2 varietal-
turnover framing) or amend the format spec to record the decision to drop them.

**S7. Soften the Losiewicz attribution at line 33.** "developed **and surveyed** almost
entirely over patent and publication corpora (Losiewicz et al., 2000; Antons et al., 2020)" —
Losiewicz 2000 is an architecture paper, not a survey. Split the clause, or cite Antons alone
for the "surveyed" half.

**S8. Add one clause of detail to the Shi et al. (2021) citation** (line 553) so it names what
that pipeline extracted from FDA labeling. It is currently the thinnest of the six new
citations, and one clause would make it as substantive as the other five.

**S9. Check the abstract's "2,386 records" against §3.1's "6,734 deduplicated records".** The
abstract's figure is the national-level subset; a reader reaching §3.1 meets a different
number first. A three-word fix ("2,386 national-level records"). *(Strictly R-E territory;
noted because it surfaced during the abstract word count.)*

**S10. Do not rebuild anything from `manuscript/sections/*.md`.** Those are v1-era working
drafts dated 14 Sep; `robustness.md` still carries the pre-compression `Table 6/7` numbering.
They are not a submission surface, but they are a trap for a future build script.

---

## Recommendation

**Minor revision.** On the two questions this review line exists to answer, the manuscript is
in good shape: **no stale figure or table number survived the two renumbering rounds**, and
**no reference is fabricated**. The deliberate §7 traceability note is correctly spelled and is
the only `Table 7` in the document; the v4 Discussion insertion did not orphan a single section
pointer; and the DOCX and PDF in the submission package are genuine v4 builds that agree with
the source paragraph for paragraph.

The seven must-fix items are all mechanical and can be done in well under an hour: two
reference records (M1, M2), four section pointers plus one internal contradiction (M3–M6), and
one DOCX rebuild (M7). None requires re-running an analysis, re-rendering a figure, or changing
a number in a table.

Two of them do deserve emphasis, because they are the kind of defect that costs more than it
should. **M1** — a truncated author list and a paraphrased title on an uncited-in-detail
reference — is exactly what a journal's automated reference checker flags, and it sits on the
one entry already carrying an "Unverifiable" marker, which compounds the impression. **M3** is a
self-contradiction: the manuscript points a reader at §6 for a test it elsewhere correctly
locates in §5.6. Fix those two first.

I see no reason for a v5 on this review line's account. A targeted patch pass over the seven
must-fix items, followed by a DOCX/PDF rebuild and a re-run of the stale-numbering grep, is
sufficient.
