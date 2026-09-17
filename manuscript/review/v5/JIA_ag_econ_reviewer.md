# Referee Report — Journal of Integrative Agriculture, Agricultural Economics and Management Section
**Manuscript:** "Rice variety approval records as an innovation indicator source: trial channel, third-party-assayed grain quality, and who measures what enters the market in China, 2017–2022" (v5)
**Submitted under theme:** (1) agricultural science and technology economy and policy
**Reviewer role:** Section referee, Agricultural Economics and Management

---

## Overall recommendation: MAJOR REVISION

The empirical core — a record-level trial-channel variable extracted from approval-announcement text, a clean identification argument built on within-file measurement-party asymmetry, and seventeen honestly-reported robustness checks — is genuinely strong and, on econometric grounds alone, would clear this section's bar. But the manuscript currently has two problems serious enough to warrant major revision rather than minor: (1) it does not consistently read as agricultural-economics-and-policy scholarship — a full discussion subsection (§8.4) and the abstract's own closing sentence explicitly reframe the paper's contribution as "S&T intelligence" methodology rather than agricultural policy, and roughly a third of the reference list is drawn from the scientometrics/information-science literature rather than agricultural or regulatory economics; and (2) the policy-implications section (§8.3), which is the section this journal's theme most cares about, is thin (144 words), partly self-undermining ("not a claim regulators were unaware of the pattern"), and leaves a sharper, more specific, evidence-grounded recommendation sitting unused in the paper's own results (§5.4, §7, §6.6). Neither problem requires new data or new estimation — both are fixable by rewriting the discussion/abstract/title and by re-engaging one cited precedent — but both go beyond copy-editing and require the authors to decide, and commit to, what kind of paper this is for this audience.

---

## 1. Fit and framing

**Where it works.** The Introduction states the paper's actual question in native institutional-economics language:

> "This split — self-organised measurement of performance, third-party measurement of quality, inside the same approval file — is the object of this paper. We ask not how large the reform was, but *who measures what enters the market*." (§1, opening paragraph)

This is exactly the register a policy-and-economics audience wants: a regulatory-design question about how an approval institution allocates measurement authority, not an agronomy question about variety performance. The composition-effect estimand is also stated cleanly and non-methodologically:

> "The paper's estimand is a **composition effect on the entering population**: conditional on year, trial group and check, how do the traits of varieties entering through a self-organised channel differ from those entering through the unified trial." (§1)

The self-certification literature engagement in §8.1 (Duflo et al. 2013; Bar and Zheng 2019; Grennan and Town 2020; Renckens and Auld 2022) is squarely regulatory economics and is used correctly — as a mechanism, not a source of causal identification the paper doesn't have.

**Where it misfires.** Set against the above, the paper repeatedly reframes its own contribution as an information-science exercise rather than an agricultural-policy one, and does so at exactly the points a reader remembers most: the title, the abstract's final sentence, and an entire Discussion subsection.

- The **title** foregrounds "as an innovation indicator source" — a scientometrics framing — ahead of the institutional/policy question the paper actually answers.
- The **abstract's climactic sentence** — the line a reader is likely to carry away — is a data-quality claim, not a policy claim: "The wider point is that evidence strength can differ across fields of one official source according to who measured each field, so approval indicators should be read field by field." (Abstract, final sentence)
- §8.4 opens by explicitly declaring itself outside the agricultural frame: **"Read as an intelligence exercise rather than an agricultural one, this paper makes four points that generalise beyond rice."** (§8.4, opening sentence) A section that begins by telling the reader it is *not* being read as agricultural scholarship is a direct invitation for an Ag-Econ-and-Policy referee to ask why it is in this section at all.
- Even the Methods section is introduced through this frame: §3 opens by casting the whole pipeline as **"a six-step S&T intelligence pipeline"** (§3, opening paragraph) rather than as a data-construction and identification section for an applied micro paper.
- The Conclusion reproduces the split explicitly rather than resolving it: **"Within these bounds the contribution has two faces. As agricultural technology assessment, it supplies a record-level channel variable... As S&T intelligence, it shows a long-public administrative corpus can become a structured indicator system..."** (§9) The paper is telling its own referee that it has two audiences; a section referee is entitled to conclude that only the first "face" is theirs to evaluate, and that the second is padding out of scope.

This is not merely a stylistic quibble — it is checkable in the reference list. Of roughly twenty references, at least six (Losiewicz et al. 2000, *J. Intelligent Information Systems*; Antons et al. 2020, *R&D Management*; Rammer and Es-Sadki 2023, *Technological Forecasting and Social Change*; Franceschini et al. 2016, *J. of Informetrics*; Jaffe and de Rassenfosse 2017, *JASIST*; Shi et al. 2021, *Frontiers in Research Metrics and Analytics*) belong to the scientometrics/S&T-indicator literature, not to agricultural economics or regulatory economics. That is a substantial fraction of the citation base oriented toward a different disciplinary readership than this section's.

**Confidence:** high that this is a real, quotable fit risk (it rests on the manuscript's own sentences, not inference); moderate on how large a problem it is in the editor's eyes, since JIA's theme (1) is itself named "agricultural science and **technology** economy and policy," which gives some legitimate room for an S&T-institutions angle. But "S&T intelligence practice" (§8.4) is a methodological contribution to indicator-building, not a policy-and-economics contribution about agricultural technology — the two are adjacent, not identical, and the manuscript currently leans on the former for its rhetorical climax.

---

## 2. Policy-guidance bar (§8.3)

§8.3 is 144 words and makes three points. Assessed against "policy guiding significance":

1. *"extending independent measurement to a subset of yield traits, even periodic spot-checks, would let regulators test directly whether the sign separation also appears under independent measurement"* — this recommends more **research/verification design**, not a specific regulatory fix. It tells a regulator how to test the paper's own hypothesis further, not what to change about the approval process.
2. *"such spot-checks are already the Ministry's own initiative since 2022, and this finding is best read as independent quantitative corroboration of that direction, **not a claim regulators were unaware of the pattern**"* — the authors themselves concede this point is not novel. Left as written, this sentence actively damages the section's case for "policy guiding significance," since it pre-empts the referee's own objection before the referee gets to raise it, without offering something new in its place.
3. *"the channel-of-entry information already exists inside every announcement but is not published as a standalone field; doing so would let downstream users condition on it directly"* — concrete and low-cost, but it is a data-transparency/data-infrastructure recommendation, not a recommendation that addresses the underlying quality-verification problem the paper's own results document.

**A sharper claim is available in the paper's own evidence and is currently unused:**

- §5.4 shows the third-party traits do *not* all converge under the post-2022 tightening: chalkiness narrows monotonically and stated-grade weakens on balance, but **head-rice "shows no convergence... its largest values in the most recent years"** (§5.4). This directly supports a specific, falsifiable, non-obvious recommendation: whatever verification MARA is currently applying is reaching chalkiness and (weakly) stated grade but not head-rice, so any strengthened oversight should explicitly target head-rice-percentage re-assay for self-organised-trial candidates. §8.3 does not make this claim at all, despite having the evidence for it in §5.4/§8.2.
- §7's germplasm-concentration result is a genuine "rules out the wrong fix" finding: consortium entrants draw on a **broader**, not narrower, sterile-line base than the unified entrants they are compared against (§7, HHI 0.0124 vs. 0.0186). A natural-sounding but wrong regulatory instinct — tightening consortium eligibility or breeding-base diversity rules to fix the quality gap — is directly contraindicated by this paper's own data. That is a specific, novel, low-risk-of-overclaiming policy statement (the lever is measurement/verification, not consortium composition), and it is currently confined to a methodological aside in §7 rather than surfaced in §8.3 as policy guidance.
- §6.6 shows the `quality_stated` non-disclosure effect **survives and strengthens** once text-length and field-count are controlled for (β = −0.122 → −0.146, p = 0.0005), ruling out the "shorter announcements say less" artifact. That licenses a specific, actionable trigger rule the paper does not propose: treat non-disclosure of a quality grade as an automatic flag for mandatory third-party re-verification before market approval, rather than the currently implied discretionary/generic spot-check regime.

None of these three additions requires new estimation — they restate results already in the paper — but none currently appears in §8.3.

**Verdict:** §8.3 as written does not clear the "policy guiding significance" bar expected by this section; it reads as directionally sensible but generic, and one of its three points is explicitly conceded as non-novel.

---

## 3. Empirical rigor bar

- **Identification stated up front:** yes, and clearly. By the end of §1 a non-methodologist reader has the research question, the composition-effect estimand, and the measurement-party identification argument (§1, contribution 2), all in plain language before any equation appears. This meets the bar.
- **Robustness presentation:** the seventeen checks are organised legibly, not buried — §6.1 dispatches the thirteen checks that don't change the picture in one paragraph each with full statistics deferred to Table 4, while §6.2–6.6 give full narrative treatment to the four checks that qualify the headline result (R7, R9, R11, R15) plus R16. This is a good structure for an econ referee to follow linearly. A single "would strengthen" gap: there is no single at-a-glance visual (a compact verdict table or coefficient-style summary) that lets a reader confirm the overall robustness picture without reading through §6.1–6.7; Table 4 apparently holds the full statistics but the *verdict per check* (robust / qualifies / inconclusive) is only assembled in the §6.7 prose paragraph.
- **Engagement with the leading alternative explanation:** handled honestly and repeatedly. $H_{threshold}$ (differing admission thresholds rather than measurement discretion) is flagged as un-rejectable at §4.5, restated as Non-claim 1 in §4.7, tested (and found underpowered, not resolved) in §6.3's within-applicant check, and revisited in §7's closing paragraph. This is a genuine strength — the paper does not oversell what its design can separate.
- **Where it falls short of JAE/AJAE-caliber even accounting for JIA's lower bar:** the paper never translates any headline coefficient into an economic magnitude a reader can evaluate (a price premium, a milling-yield revenue effect, a subsidy-eligibility threshold crossed). This is transparently scoped out via Non-claim 6 ("No welfare claim"), which is honest, but a top-tier ag-econ referee would still want at least a rough benchmark of what a 1.84-point head-rice gap or a 12.2-point drop in stated-grade probability means in farm-gate or procurement terms, even without a formal welfare model. This is a "would strengthen" item rather than a blocking one, given the paper's explicit scope discipline.

---

## 4. The "so what should a regulator do, and is it novel" test

Reading only §7, §8.3 and §8.4 as that referee would: the paper's own text hands the referee the rebuttal before they need to ask for it — §8.3 point 2 explicitly says the audit-spot-check recommendation is *"not a claim regulators were unaware of the pattern."* The third point (publish the channel field) is concrete but addresses discoverability of already-collected information, not the underlying quality-verification gap the paper documents. As currently written, §8.3/§8.4 read as **descriptively interesting with a directionally sensible but non-actionable gesture**, not as a policy contribution that would by itself justify a policy-section publication.

This is fixable without new claims, using only what is already in the paper: the head-rice non-convergence finding (§5.4) gives a *specific trait* a regulator should prioritize; the germplasm result (§7) rules out a plausible-sounding wrong fix and licenses the right one; and the disclosure-robustness result (§6.6) licenses a specific, cheap trigger rule (non-disclosure ⇒ mandatory re-verification). Recommendation 1 below asks the authors to make this connection explicit in §8.3, because right now the paper is one rewrite away from clearing this bar, not several.

---

## 5. Comparison bar: engagement with Qiu et al. (2016)

Qiu et al. (2016) — the cover letter's named JIA precedent for information-asymmetry work — appears exactly once, in a single sentence at the end of §8.1:

> "Qiu et al. (2016) describe the same problem one stage downstream, where farmers infer unobservable seed quality from imperfect signals; our result places an analogous asymmetry inside the approval file itself." (§8.1, closing sentence)

This is a citation by analogy, not an engagement. It does not state what Qiu et al. actually find (which signals maize farmers use, what mitigates the asymmetry, what their policy conclusion was), it does not address the crop mismatch (maize vs. rice) or whether the mechanism plausibly transfers, and — most importantly for the paper's own argument — it misses the natural causal chain that would make the citation substantive: if approval records (or extension materials and seed-dealer claims derived from them) are one channel through which farmers infer quality, then a systematically weaker third-party quality signal for self-organised-channel entrants does not merely sit "one stage upstream" of Qiu et al.'s problem, it **compounds** it — the same asymmetric-information gap Qiu et al. document at the farmer level would be reproduced, or worsened, at the point where the "official" record itself is generated. The paper has the material to make this connection (its own §2 institutional description and §7 counter-case) but does not.

**Verdict:** as it stands, this is a token citation. A referee who is Qiu et al., or who treats that paper as the bar for what counts as adequate engagement with a cited precedent, would notice the asymmetry between how much weight the cover letter places on this precedent and how little text the manuscript spends on it.

---

## 6. Length and density after compression to ~10,000 words

Confirmed: §8.3 is 144 words. For a paper submitted under a theme whose stated purpose is "policy guiding significance," this is too thin, and it is thin in the specific place that matters most for this section's evaluation — not because it was cut carelessly (the rest of the Discussion, §8.1/§8.2/§8.4/§8.5, is proportionate and the compression elsewhere looks deliberate and well-judged), but because the compression left the policy section as three compressed bullets when the paper's own results (identified above) could support a substantially more specific treatment at, plausibly, 300–400 words without adding a single new estimate. This is the one place in the manuscript where the ~10,000-word target should be renegotiated internally — e.g., by shortening §8.4 (which currently generalises at length beyond agriculture) and reallocating that space to §8.3.

---

## Section-order note (for completeness, not a compliance verdict)

The manuscript's headings — Introduction / Institutional background / Data and pipeline / Empirical strategy / Results / Robustness / Germplasm concentration / Discussion / Conclusion — depart from JIA's literal Introduction–Materials and methods–Results–Discussion–Conclusion order by splitting "Materials and methods" into three top-level sections (§2–§4) and inserting two top-level sections (§6 Robustness, §7 Germplasm concentration) between Results and Discussion.

For an econometrics-style, survey/administrative-data paper (not lab-based), this is normal disciplinary practice: institutional background, data/construction, and identification strategy are the standard three-part decomposition of "methods" in applied microeconomics, and a separate Robustness section following Results, before Discussion, is standard in that literature (e.g., typical structure in applied micro / regulatory-economics journals). I would not expect a knowledgeable Ag-Econ-and-Policy referee to object to the Results/Robustness/Germplasm split — **confidence: high** that this is normal practice, not a compliance risk.

I am less certain about the literal absence of a heading titled "Materials and methods" — JIA's production/copyediting desk may enforce this mechanically regardless of subfield norms, independent of what a referee in this section would think substantively. **Confidence: moderate** that this specific point is a real risk (I have no access to comparable published JIA Ag-Econ-section papers to check against, so this is a risk flag, not a verified finding). A cheap mitigation exists (see Must-address #4 below).

---

## Ranked "must address before submission"

1. **Rewrite and lengthen §8.3 with specific, evidence-grounded recommendations, and remove the self-undermining admission.**
   Proposed fix: expand §8.3 to ~300–400 words. Add: (a) a recommendation, grounded in §5.4, that verification effort be specifically targeted at head-rice percentage for self-organised-trial entrants, since this is the one third-party trait not converging under the post-2022 tightening; (b) a recommendation, grounded in §7, that consortium-eligibility/composition rules are *not* the right lever (since consortium entrants draw on a broader, not narrower, germplasm base) — the fix belongs at the trial/verification stage, not the composition-rule stage; (c) a recommendation, grounded in §6.6, that non-disclosure of a stated quality grade be treated as an automatic trigger for mandatory third-party re-verification, since this pattern survives and strengthens under disclosure-behaviour controls. Either delete the sentence "not a claim regulators were unaware of the pattern" or immediately pair it with what the paper newly contributes (magnitude and trait-specific targeting), so it does not read as a concession with nothing offered in exchange.

2. **Rebalance the paper's climax away from "S&T intelligence" framing toward the institutional/policy point, specifically for this section.**
   Proposed fix: revise the abstract's final sentence so the paper's takeaway is a policy point (e.g., that verification currently reaches some third-party traits but not others, and that the germplasm counter-case rules out a composition-based fix), not a data-quality aphorism. Reframe or shorten §8.4 — either cut it to two or three sentences that connect back to the ag-policy argument, or move the bulk of it to Supplementary Material, since as written it explicitly declares itself "not agricultural" (§8.4, opening sentence) and pulls roughly a third of the reference list toward a different disciplinary literature. Consider revising the title to foreground "who measures what enters the market" over "as an innovation indicator source."

3. **Deepen engagement with Qiu et al. (2016) beyond the single analogy sentence in §8.1.**
   Proposed fix: add 3–5 sentences summarizing Qiu et al.'s actual mechanism and findings, address the crop difference (maize vs. rice) and whether the informational mechanism plausibly transfers, and draw the compounding-asymmetry connection explicitly: a weaker third-party quality signal for self-organised entrants does not just sit upstream of farmer-level information asymmetry, it likely reproduces or worsens it if approval records or derived extension materials are among the signals farmers or dealers rely on.

4. **Mitigate the "Materials and methods" heading risk at low cost (moderate-confidence risk).**
   Proposed fix: add a top-level "2. Materials and methods" heading with §2–§4 folded in as subsections 2.1 Institutional background, 2.2 Data and the intelligence-extraction pipeline, 2.3 Empirical strategy (renumbering subsequent sections accordingly), or, if the authors prefer to keep the current structure, add a line in the cover letter noting that Sections 2–4 jointly constitute "Materials and methods" for a survey/administrative-data paper, to pre-empt a desk-level query.

---

## Would strengthen, not blocking

- Add a compact robustness-verdict table or figure (17 rows, one verdict column: robust / qualifies / inconclusive) near §5.6 or the start of §6, so the overall robustness picture is visible without reading through §6.1–6.7 sequentially. Table 4 appears to already hold the full statistics; this would be a thin summary layer on top of it.
- Add a rough economic-magnitude benchmark for at least the two most secure coefficients (head-rice −1.844 pp, chalkiness +1.108 pp) against any available external reference for price or procurement effects of these grades, even without a formal welfare claim, to help an ag-econ reader gauge stakes.
- Double-check the Abstract against JIA's structured-abstract requirement: the current abstract (246 words, within the ≤250 limit) is a single unstructured paragraph rather than labeled Background/Objective/Methods/Results/Conclusion sections; confirm whether JIA's Ag-Econ section expects explicit structure labels, and note the word count is close enough to the 250-word ceiling that any further revision (e.g., following recommendation 2 above) should be checked against the limit.
- Consider whether a brief, simple screening/selection framing of the applicant's channel-choice decision (in the spirit of Bar and Zheng 2019, already cited) would give the regulatory-economics engagement more structure, though this is not required given the paper's explicit non-causal, non-structural scope.
