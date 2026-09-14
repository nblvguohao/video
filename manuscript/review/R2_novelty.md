# Reviewer R2 — Novelty, Contribution, and Corporate-Promotion Screen

**Manuscript**: "Who measures what enters the market? Self-organised variety trials and the third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022"
**Reviewer focus**: originality/contribution relative to prior literature; whether any section reads as corporate promotion rather than scholarship.

---

## Overall assessment

The paper's core idea — reconstructing a record-level trial-channel variable from approval-announcement text and using the co-existence of third-party-assayed and applicant-measured traits within the same document as an identification device — is a genuine and, as far as I can tell from the manuscript and the verification materials provided, novel contribution relative to the two studies that evaluate the same 2016 reform (Xiang et al., 2025; Zhao et al., 2022). The empirical execution (sign-separation logic, two non-overlapping treatment arms, extensive robustness reporting, explicit non-claims) is unusually disciplined for a paper built partly from a text-mining exercise on secondary data.

However, I cannot fully certify the novelty argument as presented, because the manuscript's own supporting record (`integration_log.md`, §8) discloses that **ten of the twenty-one references the authors themselves verified as necessary "mandatory citations" are never cited anywhere in the drafted text**, and several of these are precisely the papers a reader would need to see engaged with in order to judge the claimed increment. This is not a minor bibliographic housekeeping issue — it is a gap in the novelty argument itself, and I list it as a major concern below rather than a technical failing only.

On the corporate-promotion question: having read Section 7 (Mechanism) line by line against the plan's seven writing rules (W1–W7), I find the section is, on the evidence available to me, **compliant** with the self-imposed constraints — length, role framing, co-location of positive and negative facts, no revenue conversion, no ranking rhetoric. This is worth stating plainly because a reviewer's job is not only to find problems but to verify that a stated safeguard was actually followed, and in this case it was. I flag one secondary point (table count in the Mechanism section) under Technical failings, but it does not amount to promotional framing.

**Recommendation: Major revision.** The empirical contribution appears sound and likely publishable at JIA once (a) the missing mandatory citations are integrated into the Introduction/Discussion with real engagement, not just added to the reference list, and (b) the JIA scope-fit precedents are cited in the Introduction/cover letter as required by the journal's own local-literature convention.

---

## Major strengths

1. **A genuinely new observable.** No prior paper (as represented by Xiang et al. 2025 and Zhao et al. 2022, both coded as a before/after period indicator) has a record-level trial-channel variable. Turning "the 2016 reform" into a within-year, within-trial-group, within-check comparison is a real design improvement over a period-indicator DID, and the manuscript is explicit and correct that this is what distinguishes it (Introduction, §1, paragraph 3; §4.2).

2. **The sign-separation argument is the paper's actual identification strategy, not a discussion-section flourish**, and it is stated in the abstract, Introduction and Methods alike (manuscript_v1.md lines 39, 45, 290–330). This is good practice: a design this reliant on within-document heterogeneity in measuring party needs the logic on the table early, and it is.

3. **The paper is unusually candid about what it does not show.** Section 4.7's twelve numbered non-claims, and the parallel disclosure of the pre-reform placebo failing to move in the same direction (§6.12), the underpowered within-applicant test (§6.10), and the sign-unstable top-two-grade indicator (§6.6), are exactly the kind of self-policing that guards against inflated novelty claims. I did not find any claim in the body text that oversells what the data can support (see also "unsupported claims" below — I found none rising to that level).

4. **The Winall case is explicitly scoped as a counter-case rather than as the paper's substantive finding**, and the manuscript demonstrates (not merely asserts) that the headline result survives dropping all of Winall's records (§6.9). This is the correct way to use a single-firm illustration in a paper about a market-wide composition effect.

---

## Major concerns

### MC1 — Ten mandatory-citation references are verified as real and relevant but never cited in the manuscript body; this leaves the novelty argument unverifiable against the closest literature

Per `integration_log.md` §8 and `references_verified.md`, the following ten works were checked as real, correctly attributed sources but do **not appear anywhere in the twelve drafted section files or in `manuscript_v1.md`**: Xie et al. (2023), Lu et al. (2024), Hang et al. (2024), Gong et al. (2026), Shi and Hu (2017), Qiu et al. (2016), Huang et al. (2018), Seck et al. (2023), Burris et al. (2025), and Rangnekar (2000).

This is a fatal gap in the Introduction as currently written, for a specific reason: **three of these — Lu et al. (2024), Hang et al. (2024), Gong et al. (2026) — are exactly the "closest neighbouring literature" a reader needs in order to judge the paper's incremental contribution**, because all three describe long-run trends in Chinese rice variety trait/quality outcomes using approval or trial records, i.e. the same underlying object (approved-variety trait trends) that this paper's structural-break analysis (§5.6) and Discussion §8.2 directly engage with, without ever naming them. As currently drafted, a reader who knows this literature has no way to see the authors' own account of how their structural-break falsification (quality trends predate the 2016 reform) relates to, confirms, or complicates the trend claims in Lu (2024)/Hang (2024)/Gong (2026). `01_theme_and_innovation.md` §5 (创新点3) explicitly plans this comparison — "这对 Lu24 / Hang24 / Gong26 一类'按年代读趋势'的做法是一条方法学提醒" — but this planned engagement never made it into any drafted section. Without it, the reader cannot verify the paper's incremental claim relative to the nearest work on the same substantive topic (rice-quality trend over the approval system), and I must treat this as a **major concern that blocks a full novelty assessment**, not a copy-editing note.

Xie et al. (2023) is also directly relevant and its absence is a missed opportunity rather than merely a housekeeping gap: it studies exactly the same focal firm's (Winall's) contract-farming quality incentives via a game-theoretic model, and the Introduction/Mechanism section would be strengthened, not weakened, by distinguishing this paper's variety-level empirical evidence from Xie et al.'s firm-level contract-design theory — as `01_theme_and_innovation.md` (创新点3) itself notes ("以荃银高科的订单农业为对象，博弈模型 + 数值算例，无品种级数据"). Leaving it uncited risks the appearance that the authors are unaware of, or avoiding, the one paper that studies their own case-study firm.

**Recommendation**: insert, with real engaged sentences (not bare citations):
- **Introduction, §1** (after the paragraph introducing Xiang et al. 2025 / Zhao et al. 2022 as the two existing evaluations of the reform): add Lu et al. (2024) and Hang et al. (2024) as the literature on long-run rice-trait/quality trends that this paper's record-level channel variable and structural-break test speak to; note that neither uses a channel variable either.
- **Introduction or §2 Institutional background**: add Gong et al. (2026) alongside Lu/Hang if its content (hybrid rice yield/quality/resistance trend over 50 years) is confirmed once full text is available — the reference-verification file flags its numbers as still "title-level only," so any citation before submission must stay qualitative until the full text is checked.
- **§7 Mechanism or §8.1 Discussion**: add Xie et al. (2023) when introducing Winall, distinguishing its firm-level contract-theoretic treatment from this paper's variety-level empirical claim.
- **§8.1 Discussion (self-certification literature)** or **Introduction**: Seck et al. (2023), Burris et al. (2025) and Rangnekar (2000) are about realised genetic gain and public/private breeding-sector divergence; if the authors intend them as support for the yield/breeding-ability discussion (as `01_theme_and_innovation.md` groups them under 创新点3's evidence base), they need an actual sentence — currently they support nothing in the drafted text and their inclusion in the "mandatory" list with no home in the manuscript suggests either an oversight in drafting or that the plan over-scoped the citation list. Either way, this needs the author team's decision, not a silent drop.

### MC2 — JIA scope-fit precedent citations (Shi & Hu 2017; Qiu et al. 2016; Huang et al. 2018) are absent from the Introduction, and no cover letter/scope-fit argument is currently visible

Per the task brief, these three *Journal of Integrative Agriculture* papers are meant to establish, alongside the manuscript's other content, that a paper about seed/variety regulation and China's crop sector fits JIA's remit even though its methodology and framing (composition-effect estimation, third-party-audit economics) may read as agricultural economics rather than agronomy. `integration_log.md` confirms these three are **not cited anywhere** in the drafted sections. This is a real submission-readiness gap: JIA editors and reviewers routinely check whether a submission engages with the journal's own prior publications on cognate topics (variety germplasm contribution, farmer seed-choice behaviour under information asymmetry, contract farming) as evidence the authors know the venue. I could not find any cover-letter draft in the manuscript materials that makes this case either.

**Recommendation**: add one sentence each to the Introduction (or the not-yet-drafted cover letter) situating this paper's institutional-economics-of-seed-regulation approach alongside Shi and Hu (2017) (germplasm/variety-improvement history in JIA), Qiu et al. (2016) (asymmetric information in Chinese farmer seed choice, JIA) and Huang et al. (2018) (contract farming and information/incentive design in Chinese agriculture, JIA) — these three collectively establish that JIA already publishes exactly this blend of institutional-economics-of-agriculture work, which is the scope-fit argument the submission currently lacks.

### MC3 — Without MC1/MC2 resolved, I cannot independently verify the "first record-level trial-channel variable" claim is not already anticipated by adjacent literature

The manuscript's strongest novelty claim — nobody has previously exploited the announcement text's channel-naming convention — is asserted against exactly two named comparators (Xiang 2025, Zhao 2022) and is plausible on the evidence given. But because the Lu/Hang/Gong papers on rice-quality trend using (I infer, from their titles and the descriptions in `references_verified.md`) similarly large compiled variety-approval datasets are never discussed, I cannot rule out that one of them already uses some form of channel or trial-organisation metadata. This should be checked and stated explicitly in the manuscript rather than left for the reviewer to wonder about. This is why MC1 is listed as a "major," not "minor," concern: it directly bears on whether the novelty claim as stated is falsifiable by the reader.

---

## Technical failings

1. **Table count in the Mechanism section may exceed the self-imposed W1 constraint on table/figure count** (per `01_theme_and_innovation.md` §7, "机制章节最多 1 节 + 1 图 + 1 表"). Section 7 as drafted cites Table 5, Table 6, and Table 7, and Fig. 7(a,b,c) (one multi-panel figure, which reasonably counts as "1 图"). Table 7 (enterprise-vs-institute descriptive split) is arguably shared with the empirical-strategy section's auxiliary specification (§4.6) rather than being Winall-specific, so this may be a labeling/scoping issue rather than a true violation, but it should be reconciled: either narrow Table 7's placement to make clear it is not "Winall content" for the purposes of the 15%-length and "1 table" self-constraints, or explicitly note in the plan that the constraint was revised to "1 table per sub-topic."

2. **Structural note, not a novelty issue**: `integration_log.md` §12 records the manuscript body at ~14,000 words against a stated 8,000–10,000-word JIA guideline. This affects the Introduction's own length budget and is worth flagging here because a bloated Introduction ironically dilutes, rather than strengthens, the novelty argument — trimming §4.1's rejected-DID-designs discussion (which duplicates content already implicit in the identification strategy) would create room for the MC1/MC2 citations without net length growth.

---

## Assessment against journal criteria

| Criterion | Assessment |
|---|---|
| Originality of contribution | Strong in substance (record-level channel variable; sign-separation identification logic); **currently unverifiable in the Introduction as written**, because the papers needed to benchmark the claim are absent from the text (MC1). |
| Scope fit for JIA | Not currently demonstrated in-text; JIA-precedent citations required and absent (MC2). |
| Theoretical grounding of framework | Adequate — the $H_{ability}$ vs. $H_{measure}$ vs. $H_{threshold}$ framework (§4.5) is a clean, falsifiable structure, and its limits (cannot separate $H_{measure}$ from $H_{threshold}$) are honestly stated. |
| Overclaiming / fabricated novelty | None found. The paper is unusually careful (twelve explicit non-claims, sign-instability and MDE reporting) about not overstating what it shows. |
| Corporate-promotion risk (Mechanism section) | Not found on a rule-by-rule (W1–W7) check of Section 7; role-declaration, negative-fact co-location, no-revenue-conversion, and no-ranking-rhetoric constraints all verified as followed in the current draft. |

---

## Recommendation

**Major revision.** The empirical design and identification logic are novel and well-argued, and the Mechanism section does not read as corporate promotion. But the Introduction cannot presently be certified as demonstrating the claimed increment over the nearest literature, because ten verified, relevant references — including the three papers closest in subject matter (Lu et al. 2024; Hang et al. 2024; Gong et al. 2026) and the three JIA scope-fit precedents (Shi & Hu 2017; Qiu et al. 2016; Huang et al. 2018) — are never engaged with in the drafted text. This must be fixed with substantive citing sentences, not a reference-list-only fix, before the novelty claim can be fully evaluated.

---

### Summary for the record

- **Recommendation**: Major revision.
- **Major concerns**: (1) MC1 — Lu et al. 2024 / Hang et al. 2024 / Gong et al. 2026 / Xie et al. 2023 / Seck et al. 2023 / Burris et al. 2025 / Rangnekar 2000 verified-relevant but uncited, blocking full novelty verification; (2) MC2 — Shi & Hu 2017 / Qiu et al. 2016 / Huang et al. 2018 (JIA scope-fit precedents) uncited, no scope-fit argument visible; (3) MC3 — novelty claim against Lu/Hang/Gong cannot be independently confirmed until they are engaged with in text.
- **Unsupported claims found**: none rising to the level of fabricated or inflated novelty — the manuscript's self-imposed non-claims discipline is a genuine strength.
- **Specific fix for the ten missing citations**:
  - Introduction §1 (near the Xiang 2025 / Zhao 2022 discussion): add Lu et al. (2024) and Hang et al. (2024) as the nearest trend-based literature this paper's channel variable and structural-break falsification speak to.
  - Introduction or Institutional Background §2 (once full text is confirmed): add Gong et al. (2026), qualitatively only, per the reference-verification file's caveat.
  - Mechanism §7 (Winall introduction) or Discussion §8.1: add Xie et al. (2023), distinguishing firm-level contract theory from this paper's variety-level evidence.
  - Discussion §8.1 (self-certification/breeding literature) or Introduction: add Seck et al. (2023), Burris et al. (2025), Rangnekar (2000) if they are meant to support the yield/genetic-gain argument — otherwise the author team should explicitly drop them from the "mandatory" list rather than leave them stranded.
  - Introduction (new paragraph or clause) and/or cover letter: add Shi and Hu (2017), Qiu et al. (2016), Huang et al. (2018) as the JIA scope-fit precedents.
