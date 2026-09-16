# R4 — Format, journal fit and desk-reject risk (v4)

**Reviewer role:** handling editor deciding send-out-for-review vs. desk-reject.
**Manuscript:** `manuscript/manuscript_v4.md`, read end to end 2026-09-16.
**Remit:** `plan/06_v4_review_brief.md` §4 (journal-fit reassessment) + format compliance,
readability, desk-reject risk. I have changed no file other than this one.

---

## Overall assessment

The underlying study is good. The design is honest, the robustness work is unusually
complete, the disclosure of conflicting evidence is better than most published papers in
this space, and the format spec (abstract 249/250 words, 6 keywords with no `and`/`of`,
five highlights at 83/79/71/78/81 characters, author-date references) is met to the letter.

**But I would not send this file out for review, and the reason is not fit — it is finish.**
As it stands, `manuscript_v4.md` is an internal working draft wearing a manuscript's
clothes. It tells the editor, in its own Methods section, that a required verification step
has not been done ("the authors will complete a manual, field-by-field cross-check ...
**before submission**"), then contradicts itself 300 lines later by claiming that check was
done. It cites internal project files, a "pre-submission working draft," "earlier
planning-stage notes," and "this session's network" as if these were sources. It carries
placeholder authors, placeholder CRediT and a placeholder data repository link. And it runs
~14,300 words of body text against the project's own 8,000–10,000-word target.

Any one of those is a returned-without-review at a normal Elsevier/KeAi editorial office.
Together they are decisive. The fix is a cleanup pass, not new science — but it is a
mandatory pass.

On fit: the paper has **not** drifted out of agriculture. The body is still 90% agronomy.
What v4 did was change the packaging — title, first sentence of the abstract, four of six
keywords, two of five highlights — so that the first 60 seconds of an editor's attention now
reads as information science. That is a real risk, and it is cheap to fix without undoing the
S&T-intelligence contribution.

**Recommendation: keep JIA. Do not submit v4. Produce a v5 cleanup, then submit.**

---

## 1. Journal fit verdict

### Verdict: JIA still fits — the *paper* fits; the *packaging* has drifted.

Substantively, nothing in v4 moved the paper out of JIA's scope. JIA runs a standing
**Agricultural Economics and Management** section, and the paper's evidence base is
head-rice percentage, chalkiness degree, NY/T 593 grading, neck-blast and bacterial-blight
grades, ecological trial groups, named check varieties and kg/mu yields. An information-
science journal would call this an agronomy paper on sight.

The problem is the first screen. Here is what a JIA editor sees before opening the PDF:

| Screen element | What it says | Reads as |
|---|---|---|
| Title | "Mining administrative approval records for technology assessment: record-level trial-channel indicators and third-party-assayed grain quality..." | Method-first. "Rice" does not appear until word 18 (in "rice variety registrations"). |
| Abstract, sentence 1 | "Official approval announcements are a long-public but unexploited intelligence source, recording who tested a technology and what a third party measured." | Information science. No crop, no country, no agronomy. |
| Abstract, last sentence | "a diagnostic that transfers to drug approval, device registration and patent examination corpora" | Ends the abstract in pharmacovigilance and patent analytics. |
| Keywords | administrative text mining; technology assessment; information extraction; data provenance; rice variety approval; China | 4 of 6 are information science. |
| Highlights 1 & 5 | "Administrative approval text is mined into a record-level innovation indicator set"; "Evidence strength varies across fields of one source with who measured the field" | Neither mentions rice, quality, yield or seed. |

An editor triaging thirty submissions decides section assignment from exactly these five
things. The risk is not "wrong journal" — it is **no obvious handling editor**. Crop Science
will bounce it as economics; Agricultural Economics and Management may bounce it as
informetrics; and a manuscript that bounces twice inside an editorial office gets returned.

### Specific passages that would make a JIA editor hesitate

1. **Abstract, sentences 1 and last** (lines 9). The frame opens and closes outside
   agriculture. Between them the abstract is excellent and thoroughly agronomic. The two
   bookends are doing the damage.
2. **§8.4 "Implications for S&T intelligence practice"** (lines 545–555, 539 words). This is
   the only section in the paper with no agricultural content at all. Its four bolded claims
   are about scientometrics, patent citation indicators, FDA drug labelling and "the
   indicator toolkit." A JIA reviewer drawn from the seed-economics pool will have no basis
   to evaluate it, and a JIA reader has no use for it. It is also the section most visibly
   **bolted on** — remove it and nothing upstream breaks, which is exactly the test
   `06_v4_review_brief.md` §R-A specifies.
3. **§3's six-step pipeline preamble** (lines 77–95, 241 words). Naming the Data section a
   "six-step S&T intelligence pipeline" and enumerating steps (i)–(vi) — then repeating the
   step numbers in every subsection heading — imposes an information-science vocabulary on
   what is, substantively, a normal and well-written data-construction section. JIA's
   template calls this "Materials and methods."
4. **§1 paragraph 2** (line 33). Roughly 250 words on innovation measurement, patents,
   trademarks, "firm web traces" and Rammer and Es-Sadki (2023) before the reader has been
   told what the paper finds. For a JIA audience this is the least-motivating paragraph in
   the Introduction.
5. **§1 line 53, the "sits alongside *JIA* scholarship" paragraph.** This paragraph belongs
   in the cover letter — where it already is, almost verbatim. In the manuscript body it
   reads as flattery, it is the kind of thing reviewers mock, and it makes the paper
   non-portable if you have to resubmit elsewhere. **Delete from the body; it loses nothing.**

### What this means for the reframing

The v4 reframing was requested and it was executed competently. My objection is narrow and
specific: **the reframing was allowed to reach the title, abstract opening, keywords and
highlights, which are the journal-fit surface, when it only needed to reach the
Introduction, Methods framing and Discussion, which are the contribution surface.**

Concretely — and this is the single highest-leverage change in this report — restore
agriculture to the four screen elements while keeping §3's pipeline framing, §8.4 (trimmed)
and the intelligence citations intact. A title such as:

> *Trial channel and third-party-assayed grain quality in China's rice variety approvals,
> 2017–2022: mining approval announcements for record-level technology-assessment
> indicators*

keeps every v4 keyword in the title but puts rice, quality and China first. Similarly, swap
abstract sentence 1 back to the institutional opening and move the "intelligence source"
claim to sentence 2, and replace two information-science keywords with `seed regulation` and
`grain quality`. This costs the S&T-intelligence contribution nothing — it is still the
title's second clause, §1¶2, §3's framing, §8.4 and the conclusion — and removes the
section-assignment risk entirely.

---

## 2. Alternative venues

**Caveat, please read:** I could not verify current CAS tiers or 2025/2026 impact factors
from this environment. The figures below are from the project documents and from general
knowledge, and **every one must be checked against the current 中科院分区表 before any
decision is made.** Tier boundaries move annually, and the author's rule pins tier and IF to
the *year of publication*, not the year of submission.

| Journal | CAS tier (大类, approx.) | IF (approx.) | Would an agriculture-heavy empirical paper be in scope? | Verdict |
|---|---|---|---|---|
| **Journal of Integrative Agriculture** | 农林科学 **1区** (小类 农业综合 2区) | 5.7 | **Yes.** Standing Agricultural Economics and Management section; direct precedent in Qiu et al. (2016), Shi and Hu (2017), Huang et al. (2018) — all three already cited. | **KEEP.** Satisfies the single-paper path twice over (IF ≥ 5.0 *and* Tier 1). No alternative matches this on tier × fit. |
| China Agricultural Economic Review | 经济学 2区 | ~4.4 | **Yes, excellent.** Chinese agricultural institutions and policy is its core. | Best backup *on fit*, but **Tier 2 → two-paper path only.** Useful only if a second Tier-2 paper already exists or is planned. |
| Food Policy | 经济学 1区 | ~6 | **Partially.** Standards, certification and information asymmetry are core. But Food Policy wants consequences — adoption, prices, welfare — and this paper's Non-claim 6 explicitly refuses all three. An editor will ask "so what for food policy?" and the paper has no answer by design. | Plausible Tier-1 fallback, but handicapped by its own non-claims. Would need a welfare or market-outcome extension. |
| Agricultural Systems | 农林科学 1区 | ~6.6 | **No.** Systems analysis, modelling and farm/food-system boundaries. A regulatory-text-mining paper with no systems model is off-scope. | Poor fit; high desk-reject probability. |
| Technological Forecasting and Social Change | 管理学 1区 | ~11 | **Medium-high for the framing, low for the content.** TFSC publishes new innovation-indicator work — Rammer and Es-Sadki (2023), which this paper cites, is a TFSC article. But TFSC would want the innovation-measurement contribution as the whole paper and the rice agronomy compressed to an application. | **Realistic Plan B if JIA rejects**, at the cost of a genuine rewrite (~50% of the agronomy cut). Two risks: TFSC's desk-reject rate is very high, and 管理学 1区 may not read as "本学科" for an agricultural-information institute — check the IF ≥ 5.0 clause covers you regardless. |
| Government Information Quarterly | 管理学 1区 | ~8 | **Medium-high, and better than IP&M.** GIQ's core is government information quality, administrative-record reuse and open-data practice. §8.4's two theses — "reliability is a property of fields, not sources" and "publish the channel as a field" — are literally a GIQ paper. | The best *information-side* Tier-1 option. Same rewrite cost as TFSC. Worth keeping in reserve. |
| Information Processing & Management | 计算机/情报 1区 (Top) | ~7.4 | **No.** IP&M requires a methodological contribution in IR/NLP. A regular-expression rule set plus OLS with interaction fixed effects is not one by that journal's standards, however well executed. | **Not realistic.** Do not spend a submission cycle here. |
| Research Policy | 管理学 1区 | ~7.5 | High intellectually — regulation and innovation is core. | **Not realistic.** RP's identification bar would reject on the H_threshold problem (see §5 below) without discussion. |
| Scientometrics | 管理学/情报 2区 | ~3 | **Medium.** Does publish "new data sources for indicators." | Tier 2 + IF ~3 → two-paper path only. Low return for the effort. |
| Rice Science | 农林科学 2区 | ~7.4 | **Low for this version.** Would require deleting the firm analysis, the economics and the intelligence framing. | Already the project's declared fallback; Tier 2, two-paper path. |

### Reading of the table

There is **no alternative that improves on JIA.** JIA is the only venue in the list that is
simultaneously (a) Tier 1, (b) IF ≥ 5.0, (c) an agriculture journal — so the affiliation and
"本学科" questions are unambiguous — and (d) a high scope fit for the paper as actually
written. TFSC and GIQ match on tier and IF but require a rewrite that would take months and
that would weaken the agricultural framing the author's institute presumably wants. CAER and
Rice Science fit well but drop the author onto the two-paper path, which is a strictly worse
outcome given that a single JIA paper closes the requirement.

**Recommendation: do not change the target journal.** Fix the packaging instead.

---

## 3. Desk-reject risks

Ranked by how likely each is to end the submission before a reviewer sees it.

### 3.1 CRITICAL — the manuscript contradicts itself on whether the data were verified

- **§3.4 (lines 248–257)** states the cross-check against original MARA announcements
  **has not been done**: "This verification step remains outstanding and is disclosed as
  such: **the authors will complete a manual, field-by-field cross-check of a stratified
  random sample of parsed records against the original MARA announcements before submission,
  and will report the resulting agreement rate in this section; see Unresolved item P4.**
  No specific agreement-rate figure is reported here, and none should be inferred or
  assumed, until that check is done."
- **§8.5 (line 559)** states the opposite: "its completeness **was checked against a
  50-record manual audit** rather than assumed."
- `submission/submission_checklist.md` line 201 lists P4 as **unresolved, priority High**.

This is the worst problem in the file. Two readings are available to an editor, and both are
bad: either the Limitations section asserts an audit that was never performed, or the
Methods section understates verification that was. As handling editor I would not adjudicate
this — I would return the manuscript. Any reviewer who notices it will raise a
research-integrity flag, and in a paper whose entire thesis is *"the reliability of a field
depends on who measured it"* the irony will not be lost on anyone.

**This must be resolved before submission, not flagged as an open item inside the
manuscript.** Either do the 50-record audit and report the agreement rate in §3.4, or delete
the §8.5 sentence and keep §3.4's honest disclosure — but a paper that says in its Methods
"we will do this before submission" *is by definition not ready to submit*.

### 3.2 CRITICAL — internal project artifacts left in the manuscript body

An editorial assistant will see these on the first pass. Full list:

| Location | Text | Problem |
|---|---|---|
| §3.4 line 251–252 | "the present analysis environment could not reach (see `evidence/data/feasibility_notes.md`: the MARA announcement portal was not reachable from **this session's network**)" | "This session's network" is not a sentence in a research paper. Cites an internal file. |
| §3.4 line 256 | "see Unresolved item **P4**" | P4 exists only in the project's own checklist. Meaningless to a reader. |
| §4.7 Non-claim 8, line 411 | "its own disclosed n discrepancy against an **earlier planning-stage run**" | Internal process. |
| §4.7 Non-claim 12, line 415 | "(§3.4, **Unresolved item P4**)" | As above. |
| §6.4 line 493 | "differ from an n = 452 ... recorded in **prior planning notes** ... we were unable to exactly reconstruct the earlier run's cell or filter specification **from the planning documentation alone**" | Announces that the authors cannot reproduce their own earlier analysis. |
| §6.6 line 505 | "differs from a −0.169 figure recorded in an **earlier planning-stage note**" | As above. |
| §7 line 523 | "(**Table 7 in the pre-submission working draft**) ... and record this as **an item for the author team to verify against the original coding before submission**" | An instruction to the authors, printed in the manuscript. |
| §3.3 line 227, 233 | "`manuscript/tables/table2_descriptive_balance.md`", "`submission/supplementary_material.md`" | Internal repository paths cited as if they were locations a reader could reach. |
| §5.5 line 445; §5.6 line 449; §6.1 R10; §6.6 | "`table_event_study_by_year.csv`", "`table_breakpoint_scan_full.csv`", "`table_r10_drop_winall_robustness.csv`", "`scripts/analysis/robustness_quality_stated_controls.py`", "`results_notes_main.md`" | Five more. None resolves to anything a reader can access; the Data Availability statement says the repository link is `[repository link]`. |
| References, Gong et al. 2026 | "(title-level citation only; full text not accessible at time of writing, no specific figures attributed)" | Editorial commentary inside a reference list entry. |

The intent behind several of these — transparency about discrepancies — is admirable and
should be preserved. But the *venue* is wrong. A reader needs "an independent re-run of this
check on the archived data returns n = 495 rather than the n = 452 reported in an earlier
draft; we report the current run." A reader does not need to know that planning
documentation was unreconstructable. And the file paths must become either supplementary
item numbers or deposited-repository DOIs.

### 3.3 CRITICAL — the submission package is unfinished

- Author list: absent. Corresponding author: `[Author to complete]`. Affiliation, email,
  ORCID: all placeholders (`submission/cover_letter.md` lines 96–99).
- Acknowledgements: `[Author to complete: funding sources, reviewer thanks, etc.]`
- CRediT: all nine roles are `[Author(s) to complete]`. JIA **requires** CRediT.
- Data availability: `available at [repository link]`. JIA **requires** a working data
  statement, and this one additionally says the dataset cannot be redistributed because
  "the licensing status of the upstream aggregation" is unresolved.

Also note the affiliation requirement from `05_sti_reframing_brief.md` §1.3: the first
author's affiliation must be the author's own institute. That cannot be verified while the
author block is a placeholder.

### 3.4 HIGH — "pre-registered" is claimed five times with no registration

The manuscript says "sixteen **pre-registered** and one additional robustness checks" (§5.7),
"**pre-registered** placebo traits" and "the **pre-registered** methods statement" (§5.2),
"**pre-declared** placebos ... per the **pre-registered** design" (§6.1 R12). Nowhere is
there a registry name, an identifier, a URL or a date. There is no pre-registration
statement in `submission/declarations.md`.

This is a claim editors check. Either supply the registration (OSF, AsPredicted, or a
timestamped analysis plan deposited with the data) with its identifier in §4 and in the
declarations, or downgrade the language to "specified in advance of estimation in our
analysis plan, deposited at [DOI]". Leaving it as-is invites an integrity query.

(Separately, §5.7's arithmetic is wrong: "sixteen pre-registered **and one additional**"
totals seventeen, while §6 and §6.7 both say sixteen checks R1–R16. R16 is the one added
later, so §5.7 should read "fifteen pre-registered and one additional.")

### 3.5 HIGH — length

| | Words |
|---|---|
| Whole file | 15,500 |
| Body (excl. abstract, keywords, highlights, references, declarations) | **≈ 14,270** |
| Project's own target (`plan/04_format_spec.md` line 11) | **8,000–10,000** |
| Overrun | **+4,300 to +6,300** |

JIA publishes no hard limit for Research Articles, which is why this is a risk rather than a
rule violation — but an editor receiving a 14,300-word manuscript with 6 figures, 5 tables,
a 485-word numbered list of things the paper does not claim, and a 16-item robustness
section will read it as a thesis chapter. Note that the overrun is **not** mainly v4's fault:
v3 was already ~12,700 body words. v4 added 1,552 on top (see §4 below). Both need cutting.

### 3.6 MEDIUM — data provenance

The corpus is a re-parse of a third-party GitHub compilation (`he-zhui/Rice_QA`) of unknown
licence, never checked against the official source, from which the full parsed dataset
cannot be redistributed. §3.1 and §3.4 are commendably frank about this, and the framing
("MARA announcements, obtained through the public third-party compilation ... and parsed by
the authors") is the right one. But an editor weighing whether this clears the journal's
data policy has to balance that frankness against the fact that *nothing* about the corpus
has been independently verified. Resolving P4 (§3.1 above) converts this from a
possible-reject into a stated limitation.

### 3.7 LOW–MEDIUM — structure vs. the JIA template

The manuscript has nine top-level numbered sections and no heading called "Materials and
methods." `plan/04_format_spec.md` §10 anticipated this and argued the mapping is defensible
(Institutional background → after Introduction; Mechanism → after Results). I agree it is
defensible for an economics-style paper and would not reject on it. But an editorial
assistant running a template check may bounce it mechanically. Cheap insurance: retitle §3
"Materials and methods: the approval corpus and its extraction," and demote §6 (Robustness)
and §7 (Mechanism) to §5.8 and §5.9 under Results. Zero content change, one fewer objection.

### 3.8 LOW — the named firm

§7 analyses Anhui Winall Hi-Tech Seed Co. by name, in a paper about a ministry rectification
campaign, in a CAAS-affiliated journal. The handling is careful and the finding is
*favourable* to Winall, which defuses most of the risk, and the cover letter's conflict
statement is appropriately explicit. I flag it only so the author is not surprised if the
editorial office asks for the firm to be anonymised. Do not pre-emptively anonymise — the
counter-case argument needs a real, identifiable firm.

---

## 4. Readability: does it read as one argument?

**No.** It reads as a careful paper that has been defended four times and has kept every
defence. The prose is clear sentence by sentence; the problem is entirely at the level of
architecture and accumulation.

### 4.1 Where the +1,552 words went

Measured section by section against v3:

| Section | v3 | v4 | Δ |
|---|---|---|---|
| §1 Introduction | 1,570 | 1,860 | **+290** |
| §3 preamble (new six-step pipeline framing) | 0 | 241 | **+241** |
| §3.1 | 454 | 652 | **+198** |
| §3.3 | 637 | 699 | +62 |
| §3.4 | 217 | 268 | +51 |
| §7 | 861 | 879 | +18 |
| §8.1 (self-certification, demoted) | 342 | 232 | −110 |
| §8.4 Implications for S&T intelligence (new) | 0 | **539** | **+539** |
| §9 Conclusion | 240 | 330 | **+90** |
| References | 527 | 696 | +169 |
| **Total** | 13,948 | 15,500 | **+1,552** |

Against a 700–800 budget, that is roughly 2× over. §8.4 alone (539 words) is most of the
overrun, and §3's new framing apparatus (+552 across the preamble and §3.1) is the rest.

### 4.2 The bloat, named and located

Ranked by words recoverable with no loss of substance.

1. **§6.5, the chained-check genetic-gain scale (588 words) → ~120 words + supplement.**
   The largest single cuttable block in the paper, and it predates v4. It spends 588 words
   constructing a method, documents four reasons the method does not work on this data
   (CV diagnostics, a +3.14% vs +7.04% discrepancy, a 0.25–0.50% swing, G = 6 clusters),
   cites six papers, and concludes: "the chained-scale evidence is inconclusive, not
   confirmatory or disconfirmatory." Main text needs three sentences: we tried an
   alternative yield scale, the direction does not reverse, the interval is too wide to be
   informative, details in Supplementary Note S2. **Save ~450 words.**
2. **§5.4 (156 words) → delete entirely.** It restates §4.5's H_ability / H_measure /
   H_threshold argument with the same notation, the same logic and the same caveat. §4.5
   sets the argument up (433 words); §5.2 delivers the coefficients; §5.4 explains again
   what §4.5 already explained. Counting the abstract and §1 line 43, the sign-separation
   argument is stated **four times** before §6 begins. **Save ~156 words.**
3. **§8.2 paragraphs 1 and 3 (~400 words of duplication).** ¶1 reproduces §5.5's year-by-year
   convergence numbers *verbatim* — "+2.71 ... +1.63, +0.92 and +0.89 ... +0.77" and
   "−2.63, −1.48 and −3.03" appear identically in both sections. ¶3 reproduces §6.4's
   provincial replication, including β = −0.468, p = 0.001, MDE and the two-part reading, in
   full. A Discussion should interpret results, not reprint them. Keep the interpretive
   sentences ("the two kinds of trend are not the same object"), cut the numbers. **Save
   ~400 words.**
4. **§3's six-step preamble (241 words) → ~60.** The steps are enumerated in the preamble,
   again in each subsection heading ("(steps i–iv)", "(step vi)", "(steps v–vi)"), and again
   in §3.1's opening. Triple labelling. One short paragraph naming the six steps, with the
   headings carrying the mapping, does the whole job. **Save ~180 words.**
5. **§8.4 (539 words) → ~300.** Four bolded theses, of which the first substantially repeats
   §1¶2 (same claim, same citations: Losiewicz, Antons, Rammer) and the fourth repeats the
   first. Losiewicz, Antons, Rammer, Franceschini and Jaffe each appear **three times** in
   the paper. Keep theses 2 ("reliability is a property of fields") and 3 ("the diagnostic is
   portable") — these are the genuinely new contribution — and fold 1 and 4 into a single
   opening paragraph. **Save ~240 words.**
6. **§4.7, the twelve non-claims (485 words).** The list is a real strength and I would not
   remove it. But it is the third of five places the paper disclaims itself: §4.4 (what β
   identifies), §4.7 (twelve non-claims), §5.7 (summary with caveats), §6.7 (robustness
   matrix with caveats), §8.5 (five limitations), §9¶2 (conclusion with caveats). Non-claims
   3, 5, 7, 8, 11 are each restated in full elsewhere. Compress to one sentence each.
   **Save ~200 words.**
7. **§5.6's closing growth-duration passage (~80 words).** "Fig. 4 also plots growth
   duration, a trait we do not otherwise analyse in this paper ... we report this only as
   background context for the figure rather than as part of the paper's argument." This is a
   figure note, not a results sentence. **Move to the Fig. 4 caption.**
8. **§1 line 53, the "sits alongside *JIA* scholarship" paragraph (~90 words).** Cover-letter
   material (see §1 above). **Delete.**
9. **§7's Xie et al. (2023) disclaimer (~60 words).** "...but at the firm level and without
   any variety-level data; this section's own analysis is confined to the variety-level
   channel-choice and within-channel positioning evidence reported below, and does not draw
   on or reproduce Xie et al.'s firm-level contract data." This is a residue of the v3
   removal of the Winall financial narrative. It interrupts the paragraph's argument
   mid-flow to defend against an accusation nobody has made. **Cut to a half-sentence.**

**Total recoverable: ~1,800 words**, which reverses the v4 growth with room to spare and
makes a further pass toward 10,000 realistic.

### 4.3 Vestigial sentences from earlier framings

- **§1 line 31, final sentence: "We ask not how large the reform was, but *who holds the
  measuring stick* for what enters the market."** This is v3's title ("Who measures what
  enters the market?") embedded in the Introduction. It is the best sentence in the paper
  and it now contradicts the title, which promises a paper about mining administrative
  records. Either restore the agricultural framing to the title (my §1 recommendation), in
  which case this sentence works again, or cut it.
- **§5.6: "consistent with a companion finding using classical standard errors."** There is
  no companion paper and no companion finding. Vestigial.
- **§6.4: "in the interest of full transparency" ... §7: "We flag one open item rather than
  resolving it silently."** Both introduce internal reproducibility discrepancies (§3.2
  above). The transparency instinct is right; the phrasing announces that the authors are
  being transparent, which reads as anxiety rather than rigour.
- **§8.1 opening: "The regulatory-economics literature on self-certification is not this
  paper's frame, but..."** and **§1 line 49: "That literature supplies the interpretation ...
  but not the paper's frame."** The paper tells the reader twice, in nearly identical
  words, that a literature it relies on heavily is not its frame. In v1–v2 that literature
  *was* the frame. Saying so twice draws attention to the demotion. Say it once, in §8.1,
  or not at all.

### 4.4 Over-hedging

Counts across 15,500 words: "rather than" **73**, "cannot" **19**, "we do not" **16**,
"underpowered" **12**, "explicitly" **9**, "we do not claim" **9**, "not estimable" **5**,
"we report this" **4**, "we flag" **4**, "suggestive" **4**, "inconclusive" **3**.

"Rather than" at 73 occurrences — roughly once every 210 words — is the paper's signature
tic, and it is almost always doing the same job: asserting X while pre-emptively denying
not-X. ("reported here rather than in §7," "a documentation-format gap rather than
evidence," "statistically inconclusive rather than confirmatory," "reported as an open item
rather than silently reconciled.") Individually each is defensible. Cumulatively they make
the paper sound like it expects to be attacked, which invites reviewers to attack it.

A mechanical fix that would improve the paper more than any other single edit: **halve the
"rather than" constructions.** Where the denial is obvious, delete it. Where it is not, make
it a plain sentence.

### 4.5 Abstract vs. body

Two places where the abstract promises more than the body delivers:

1. **"a diagnostic that transfers to drug approval, device registration and patent
   examination corpora."** The body's delivery is §8.4 thesis 3 — three sentences, one
   citation (Shi et al., 2021, on FDA labelling), and no demonstration on any second corpus.
   The abstract says "transfers"; the body establishes only that the structural feature
   plausibly *recurs*. A reviewer will call this out. Either soften the abstract ("a
   diagnostic that should apply wherever...") or accept the criticism.
2. **"(2,386 records, 17 fields)."** §3.1 says the corpus is 6,734 deduplicated records
   (2,386 national + 4,347 provincial) and the provincial layer *is* analysed in R11; the
   main analysis stratum is n = 878, and individual regressions run on n = 520–759. "2,386
   records" is neither the corpus, the stratum, nor any estimation sample. Pick one and say
   which it is.

### 4.6 Numbers

Not my remit (R3 owns this), but noted in passing: `review/v4/GROUND_TRUTH.md` line 22
records that `yield_gain_pct` = 0.5534 rounds to **0.553**, whereas §5.2, §4.5 and §6's
preamble all carry **0.554**. Flagging for whoever owns the numeric audit.

---

## 5. The strongest attack, and whether the paper survives it

### The attack

Not "H_threshold cannot be ruled out" — the paper concedes that four times, so a reviewer
raising it is pushing on an open door. The damaging version is sharper and the paper does
**not** pre-empt it:

> **The sign separation is the mechanical signature of a compensatory multi-trait approval
> standard, and the paper never controls for — or even mentions — which approval standard
> each variety was judged under.**

China's variety approval standard is not a single hurdle. It defines multiple approval types
(高产稻 / 优质稻 and related categories) with different trait bundles: a variety can be
approved as a high-yield type with a lower quality floor, or as a premium-quality type with a
lower yield requirement. §2 itself reports that the 2021 revision "raised the required
thresholds for yield, quality **and** resistance traits," which confirms a multi-trait
admission rule is operating.

Now suppose self-organised applicants disproportionately pursue the high-yield approval
type — which is exactly what a commercially motivated integrated enterprise would do. Then,
*conditional on being approved*, their entrants must show **lower third-party quality and
equal-or-higher applicant-measured yield gain**. That is the paper's headline result, produced
with:

- no measurement discretion,
- no difference in breeding ability,
- no channel-specific leniency,

purely by selection along a known, published, compensatory admission frontier.

Three things make this worse for the paper than the generic H_threshold objection:

1. **It turns the paper's H_ability rejection into a strawman.** §4.5 sets up a two-way
   contest between "self-organised applicants are worse breeders" and "the two trait classes
   are measured by different parties," and rejects the first. But nobody who knows the
   approval system expects H_ability. The real alternative is trait-bundle selection under a
   compensatory standard, and the paper's design does not test it.
2. **The bacterial-blight result supports the attacker, not the paper.** §5.2 reports
   consortium entrants are *more* resistant to bacterial blight (β = −0.190, p < 0.0001), and
   §4.7 Non-claim 4 uses this to bound the scope of the quality claim. But under the
   trait-bundle story, a third-party-assayed trait moving *in the opposite direction* is
   precisely what you predict: these are entrants who traded appearance and processing
   quality for yield and resistance. The paper's "this bounds the composition effect"
   reading is the weaker of the two available readings of its own result.
3. **The fix is cheap and available, which makes not doing it look like avoidance.** The
   approval standard / variety type is stated in the same announcements the authors already
   parse, with the same regular-expression machinery. Adding it as a control — or better,
   estimating within approval-type cells — is a few hours of work on data already in hand. A
   reviewer who notices this will ask why a paper with sixteen robustness checks does not
   have the one check that addresses its most obvious confound.

### Does the paper survive?

**Partially, and less well than v3 would have.**

The *descriptive* finding survives intact: within the same year, trial group and check,
self-organised entrants carry measurably worse third-party-assayed grain quality. Nothing in
this attack touches that, and it is a real, publishable, policy-relevant fact.

What does **not** survive is the interpretation the v4 framing is built on. Highlight 5
("Evidence strength varies across fields of one source with who measured the field"), the
abstract's closing sentence, §8.4's thesis 2 ("reliability is a property of fields, not
sources") and the portable diagnostic — the entire S&T-intelligence contribution — all
require that the sign separation be *attributable to who measured*. If trait-bundle
selection explains it equally well, the diagnostic does not follow, because there is nothing
wrong with the applicant-measured fields in that story; the entrants are simply different.

This is the part worth saying plainly: **the v4 reframing raised the evidentiary bar the
paper has to clear.** v3's framing ("who measures what enters the market") could retreat to a
composition-gap claim under pressure. v4's framing cannot, because its headline contribution
*is* the measurement-attribution claim. The reframing made the paper more ambitious without
making the identification stronger, and this is where a good reviewer will put the knife.

### What the paper should do about it

1. **Add the approval-standard/variety-type dimension.** Parse it; report the channel gap
   within approval-type cells; report it as R17. If the gap survives, the paper's central
   claim is dramatically stronger and the strongest available attack is dead. If it does not
   survive, the authors need to know that before a reviewer tells them.
2. **Name the mechanism explicitly.** Rewrite §4.5's H_threshold from "the two channels
   simply impose different admission thresholds" to the specific, testable compensatory-
   frontier version, and say what would distinguish it. Naming your strongest opponent
   precisely is worth more than four generic disclaimers.
3. **Re-read the bacterial-blight result.** Currently framed as bounding the claim; it should
   at minimum be acknowledged as also consistent with trait-bundle selection.
4. **If (1) is not feasible before submission**, demote the measurement-attribution language
   from Highlight 5 and the abstract's closing sentence to a Discussion hypothesis. Do not
   put a claim in the highlights that the design cannot defend.

---

## Must-fix (before submission — any one of these alone risks a desk return)

1. **Resolve the §3.4 / §8.5 verification contradiction.** Either perform the 50-record audit
   and report the agreement rate, or delete §8.5's claim that it was performed. Remove
   "before submission," "Unresolved item P4" and "this session's network" from §3.4 entirely.
2. **Strip every internal project artifact** listed in §3.2 above: planning notes, "Table 7 in
   the pre-submission working draft," "an item for the author team to verify," all `.csv` /
   `.py` / `.pkl` / `.md` paths, and the editorial parenthetical inside the Gong et al. (2026)
   reference. Preserve the transparency, change the venue: discrepancies become one clean
   sentence each; file paths become supplementary item numbers or a repository DOI.
3. **Complete the submission package**: author list, affiliations (first author's institute
   per `05_sti_reframing_brief.md` §1.3), corresponding author, ORCID, funding/acknowledge-
   ments, all nine CRediT roles, and a real data-repository URL replacing `[repository link]`.
4. **Resolve the "pre-registered" claim** — supply the registration identifier in §4 and in
   `declarations.md`, or downgrade the wording throughout (§5.2, §5.7, §6.1 R12).
5. **Rebalance the journal-fit surface**: title, abstract sentence 1, two of six keywords,
   and highlights 1 and 5 should lead with rice/quality/China. Keep the S&T-intelligence
   contribution everywhere else (§1¶2, §3's framing, §8.4, §9). See §1 above for a concrete
   title.
6. **Delete §1 line 53** (the "sits alongside *JIA* scholarship" paragraph). It is already in
   the cover letter, where it belongs.
7. **Name the target section in the cover letter**: "Agricultural Economics and Management."
   The cover letter currently says only "Research Article," which leaves section assignment
   to an editor who has just read an information-science title.
8. **Fix §5.7's count**: "sixteen pre-registered and one additional" contradicts §6 and §6.7
   ("sixteen checks, R1–R16"). Should be "fifteen pre-registered and one additional."

## Suggested (strongly recommended, not submission-blocking)

9. **Cut ~1,800 words** per the itemised list in §4.2. Priority order: §6.5 → supplement
   (~450), §8.2 ¶1 and ¶3 de-duplication (~400), §8.4 compression (~240), §4.7 compression
   (~200), §3 preamble (~180), §5.4 deletion (~156), §5.6 growth duration → caption (~80),
   §7 Xie disclaimer (~60), §1 line 53 (~90).
10. **Halve the "rather than" constructions** (currently 73). This will do more for the
    paper's authority than any other line edit.
11. **Cut the sign-separation argument from four statements to two** — §4.5 (setup) and §5.2
    (results). Delete §5.4; trim §1's version to two sentences.
12. **Fix the abstract's "2,386 records"** so it names a real analytical quantity, and soften
    "transfers to drug approval, device registration and patent examination corpora" to match
    what §8.4 actually establishes.
13. **Retitle §3 "Materials and methods: ..."** and demote §6/§7 to §5.8/§5.9, to survive a
    mechanical template check. No content change.
14. **Add the approval-standard/variety-type control as R17** (see §5). This is the highest-
    value *scientific* addition available and uses data already parsed.
15. Remove the two near-identical "this literature is not our frame" sentences (§1 line 49,
    §8.1 opening); keep one.
16. Move §6.5's chained-check material and §6.4's reproducibility discrepancy into a
    Supplementary Note, where a discrepancy can be documented at length without interrupting
    the argument.

---

## Recommendation

**Journal: keep the *Journal of Integrative Agriculture*, submitted to the Agricultural
Economics and Management section.** No alternative in the realistic set improves on it:
JIA is the only venue that is simultaneously Tier 1, IF ≥ 5.0, unambiguously agricultural for
affiliation and 本学科 purposes, and a good scope fit for the paper as written. TFSC and
Government Information Quarterly are the credible Tier-1 fallbacks if JIA rejects, at the
cost of a substantial rewrite; CAER and Rice Science fit well but push the author onto the
two-paper path, which is strictly worse. **Do not send this to Information Processing &
Management** — it will be desk-rejected for lack of methodological novelty in IR/NLP terms,
and a rejection cycle there is pure cost.

**Manuscript: v5 required before submission.** On the file as it stands I would desk-return
it, and the reasons would be housekeeping, not science: a Methods section that says a
required verification has not been done, a Limitations section that says it has, internal
planning notes and repository paths printed as if they were sources, an unregistered
"pre-registered" claim, a placeholder author list, and a body 40–75% over the project's own
length target.

None of that is hard to fix. The science underneath is careful and honest — more honest than
most of what gets published on this topic — and with a disciplined cleanup pass (must-fix
1–8, plus the word cuts in 9–13) this is a legitimate send-out-for-review at JIA, and I would
expect it to come back as major revision rather than reject.

The one thing that would move it from "probably publishable" to "hard to reject" is item 14:
extract the approval-standard/variety-type field and re-estimate within it. That single check
closes the strongest attack available to a hostile reviewer, and the data are already parsed.
