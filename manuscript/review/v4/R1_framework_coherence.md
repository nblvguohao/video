# R1 — Framework coherence (review line R-A)

**Reviewer:** R1 (adversarial, framework coherence)
**Manuscript:** `manuscript/manuscript_v4.md` (15,665 words by `wc -w`)
**Baseline:** `manuscript/manuscript_v3.md` (14,103 words)
**Spec reviewed against:** `plan/05_sti_reframing_brief.md` §3
**Review brief:** `plan/06_v4_review_brief.md` line R-A
**Method:** full `diff -u` v3→v4 (265 diff lines, 14 hunks), per-hunk word accounting,
mechanical deletion test, citation-occurrence census. The change log's self-assessment was
not accepted at any point; every number below is independently measured.

---

## 1. Overall assessment

**The S&T-intelligence framing is bolted on, not load-bearing.** It fails the deletion test
cleanly: every intelligence-framed passage in v4 can be removed with two scalpel cuts and no
downstream repair, and the paper that remains is v3 — a complete, coherent, fully argued piece
of work. The framing does not change the research question, the estimand, the identification
argument, the specification, the results, the robustness suite, or the counter-case. Sections 4,
5 and 6 — the paper's entire analytic core, 270 lines of v3 — received **zero** edits in v4.

The quantitative fingerprint is unambiguous. The word "intelligence" occurs 14 times in a
15,665-word manuscript, at lines 9, 33, 47, 55, 75, 79, 80, 97, 545, 547, 555 and 567. Between
line 98 and line 544 — §3.1 body through §8.3, i.e. everything the paper actually argues — it
occurs **not once**. The six new S&T-intelligence references are cited at lines 33, 246, 549,
551, 553 and 555 and nowhere else: **not one of them touches a sentence that existed in v3.**
The new literature and the old manuscript never make contact.

This is not, however, a case of a framing pasted onto an unrelated paper. The hook is real: the
paper's identification argument *is* a provenance argument, and it was already a provenance
argument in v3 — §3.3 was titled "Outcome variables, **measuring party**, and missingness"
before v4 touched it, and §4.5 already formalises $Y^{3rd}$ versus $Y^{self}$. So the dual
identity is defensible in principle. What v4 did was *name* that pre-existing structure in
intelligence vocabulary and wrap it in three new framing slabs (Intro ¶2, §3 preamble, §8.4),
without letting the frame do any work in the argument. The tell is that **§4.5 — the one
paragraph in the paper that formalises the intelligence contribution — was not edited at all.**
If the framing were load-bearing, that is the first place it would show.

Three further problems are worse than "decorative", because v4 introduced logical defects that
v3 did not have:

1. The Abstract and Intro ¶2 assert the corpus is **"unexploited"** and that administrative
   approval records **"sit outside this frame"** — and the manuscript's own Intro ¶4 and §8.4
   contradict both claims, by citation, within the same paper.
2. §8.4's "portable diagnostic" states a decision rule that **inverts this paper's own
   finding**. The recipe does not describe what this paper did.
3. The new title calls 品种审定 "**registrations**". Every other occurrence in the manuscript,
   including the abstract two lines below, says "approval". 审定 and 登记 are distinct legal
   procedures in China's seed system; rice is 审定. This is a substantive terminology error in
   the single most visible line of the paper.

The word budget was overrun roughly 2×, and about 700 of the 1,582 net added words went to
locations the brief did not authorise, of which only one block (the entity-resolution paragraph,
§3.1) earns its length.

**Recommendation: major revision** — major on framing, not on findings. No re-analysis is
needed; everything below is an editing pass. But items M1–M4 are logical errors, not stylistic
preferences, and a v5 is required.

---

## 2. The deletion test

### 2.1 What I deleted

The complete inventory of v4's intelligence-framing edits, from the diff. `A`–`T` are the
passages; the "revert" column is what removal requires.

| # | Location | Passage | Net words | Revert cost |
|---|---|---|---|---|
| A | L1 | Title | +2 | restore v3 title |
| B | L3 | Running title | 0 | restore v3 |
| C | L9 | Abstract sents 1–2 + final sent | −5 | restore v3 abstract |
| D | L15 | Keywords (4 of 6 replaced) | 0 | restore v3 |
| E | L21, L25 | Highlights 1 and 5 | +13 | restore v3 items 4–5 |
| F | **L33** | **Intro ¶2 (wholly new)** | **+251** | **delete; no repair needed** |
| G | L47 | Contribution 1: pipeline clause + final sentence | +~45 | delete clause |
| H | L49 | Contribution 2: "…but not the paper's frame…" | +~14 | delete sentence |
| I | L53 | "institutional-economics reading" → "text-mining reading" | 0 | one-word revert |
| J | L55 | Roadmap: §3 and §8 descriptions | +~10 | revert |
| K | **L75, L77–95** | **§3 heading + six-step pipeline preamble** | **+241** | **delete; no repair needed** |
| L | L138–151 | §3.1 entity-resolution paragraph | +198 | **see §2.3 — do not delete** |
| M | L97, 153, 176, 235 | Four subsection headings + "(step …)" tags | +~20 | revert headings |
| N | L178–182 | §3.3 opening 4 sentences | +62 | delete; next sentence already says it |
| O | L242–247 | §3.4 Franceschini sentence | +51 | delete |
| P | L519 | §7 parenthetical cross-ref to §3.1 rule | +18 | keep (belongs to L) |
| Q | L531–533 | §8.1 retitle + 3¶→1¶ compression | −106 | independent of framing |
| R | **L545–555** | **§8.4 "Implications for S&T intelligence practice"** | **+539** | **delete; §8.5 renumbers to §8.4** |
| S | L567 | Conclusion "two faces" expansion | +90 | revert to v3 sentence |
| T | refs | 6 new references | +169 | delete |

### 2.2 What broke: nothing

I reverted A–K and M–T (holding L, see below) and read the result end to end.

**Intro.** Deleting F (L33) does not leave a hole — it *closes* one. L31 ends:

> "We ask not how large the reform was, but *who holds the measuring stick* for what enters the market."

L35 begins:

> "This question has not been answered because it has not been asked in a form the data could answer."

In v3 these were adjacent and "This question" pointed one clause back. In v4, 251 words about
patent bibliometrics, trademark indicators and firm web traces sit between the question and its
anaphor. **The new paragraph degrades the Introduction's cohesion rather than supporting it.**
That is the opposite of load-bearing.

Nothing downstream cites Intro ¶2. The contribution list at L47–51 restates the pipeline claim
independently; the motivation for the empirical work is supplied entirely by L35 (Xiang, Zhao)
and L37 (Lu, Hang) — both untouched v3 paragraphs.

**Methods.** Deleting K (L77–95) reverts §3 to "# 3. Data" and costs nothing. The preamble is a
table of contents for the four subsections that immediately follow, whose own headings now carry
the same information; it names six steps and points each to a subsection that already existed in
v3 doing exactly that work. Nothing outside v4-added text refers to "step (i)–(vi)". The only
two places that do — L138 ("Step (iv) of the pipeline…") and L549 ("pipeline steps (iv) and
(v)") — are themselves v4 additions. **The pipeline vocabulary is a closed loop: it is referenced
only by the other passages that introduced it.** That is the textbook signature of a bolt-on.

Deleting N (L178–182) is a strict improvement. The new opener says:

> "The single most consequential step in the pipeline is the one that attaches a **measuring party** to each extracted field. A conventional data-quality assessment asks how complete and how accurately transcribed a source is; here we additionally ask, field by field, *who generated the number the source reports*…"

The very next sentence — v3's, unedited — already says it:

> "The paper's identification argument turns on a distinction the announcements make explicit: some fields report performance as measured by a ministry-designated third-party assay body, and others report performance as measured and submitted by the applicant's own trial."

Sixty-two words of restatement immediately preceding the statement. This is padding.

**Empirical core.** The diff jumps from hunk `@@ -199,7 +240,11 @@` (§3.4) to `@@ -471,7 +516,7 @@`
(§7). Lines 200–470 of v3 — §3.4 tail, all of §4 (empirical strategy, estimand, identification,
non-claims), all of §5 (results), all of §6 (robustness) — are **byte-identical** in v4. The
framing does not reach the argument.

**Discussion.** Deleting R (§8.4) leaves §8.1–§8.3 and §8.5 intact; §8.5 renumbers back to §8.4,
which is the number it carried in v3. Nothing references §8.4. Deleting S restores v3's
conclusion sentence verbatim.

**Result of the deletion test: the reverted manuscript is v3.** It is complete, coherent, fully
motivated and fully argued. No section begins with a dangling premise, no cross-reference
dangles, no claim in the abstract goes unsupported, no method is unexplained. The framing is
detachable in its entirety.

### 2.3 The one exception — and why it does not rescue the framing

**L (L138–151, §3.1 entity-resolution paragraph) is genuinely load-bearing and must be kept.**
Deleting it leaves §7's "Winall-linked records (n = 166)" with no stated identification rule —
a real gap in v3 that a referee would have raised. The paragraph supplies the rule
(pedigree-and-naming), its validation (precision 1.000, recall 0.770 on 1,426 labelled records),
and a bias-direction argument that §7 now invokes at L519. It is the best single addition in v4.

But it does **not** demonstrate that the intelligence framing is integrated, for two reasons:

1. **Its content is framing-neutral.** It is ordinary methods reporting — an entity-matching
   heuristic and its error profile. Any referee reviewing v3 on agronomy grounds alone would
   have demanded it. Strip the label "Step (iv) of the pipeline" from its first clause and
   nothing in the paragraph tells you it belongs to an intelligence paper.
2. **The change log concedes the content pre-existed.** §5.4's own note states the rule and its
   precision/recall "并非本次新造" — they were already recorded in `plan/02_research_route.md`
   and `plan/BRIEF.md` and merely moved into the manuscript. So this is not a methodological
   contribution the framing produced; it is a v3 disclosure gap that v4 happened to close.

Reporting this accurately: **the framing produced one paragraph of real value, and that
paragraph is not about the framing.**

### 2.4 Is the renaming substantive or cosmetic? — verdict: cosmetic

Three tests:

- **"Information extraction pipeline."** The actual method is regex matching on three Chinese
  strings (绿色通道 / 自主试验 / 联合体) plus field parsing plus one naming heuristic (L120–130,
  L141–144). No NLP, no extraction-accuracy evaluation, no comparison against an alternative
  extractor, no released schema. Calling this "an S&T intelligence extraction pipeline" (L47)
  and a "six-step S&T intelligence pipeline" (L79) does not add methodological content; it adds
  six step-names to work already described in v3.
- **"17-field indicator set."** v3 already said "the full set of **17 outcome variables**"
  (v3 L410, unchanged at v4 L455). v4 rebrands the same 17 regression dependent variables as a
  "record-level indicator system (2,386 records, 17 fields)" (Abstract L9) and "a 17-field
  indicator set" (L47). **No new field was extracted.** Worse, 17 is the count of *analysed
  outcomes*, not the size of the extraction schema — the corpus also carries `channel`,
  `trial_group`, `ck_n`, `approval_year`, `applicant_type`, none of which is an outcome. "17
  fields" in the abstract invites the reader to infer an extraction product it does not describe.
- **"Measuring party."** The concept that §8.4 presents as the paper's methodological discovery —
  "Reliability is a property of fields, not of sources" — was v3's §3.3 section title and v3's
  §4.5 formalism. v4 renames it; it does not develop it.

### 2.5 Is the research question now an intelligence question? — No

The paper's question is stated at L31 and is verbatim v3's: *"We ask not how large the reform
was, but who holds the measuring stick for what enters the market."* The estimand at L41 is
verbatim v3's: *"a composition effect on the entering population."* §4.5's hypotheses
($H_{ability}$ / $H_{measure}$ / $H_{threshold}$) are verbatim v3's. Every quantity in §5 and §6
is an agronomic or regulatory quantity.

This produces a visible seam. L33 announces:

> "The first contribution of this paper is accordingly a methodological one for S&T intelligence"

but the research question two paragraphs earlier is a seed-regulation question, and the
contribution list at L47 describes contribution "First" as *a variable*, not a method. The paper
asserts an intelligence identity in its framing paragraphs and then asks and answers an
agronomy/regulation question. It is agronomy wearing intelligence clothes.

---

## 3. Specific problems

### M1 — The Abstract and Intro ¶2 are contradicted by the manuscript's own Introduction and Discussion

**Abstract, L9, sentence 1:**
> "Official approval announcements are a long-public but **unexploited** intelligence source…"

**Intro ¶2, L33:**
> "…belong to a class of evidence that science-and-technology (S&T) intelligence work has **barely touched**… Administrative approval and registration records… **sit outside this frame**…"

**Contradicted at Intro ¶4, L37 (v3 text, unchanged):**
> "Lu et al. (2024) classify the quality-trait trajectory of 17,785 nationally and provincially approved varieties from 1978–2022, and Hang et al. (2024) track yield and agronomic-trait evolution across 11,811 regional-trial entries from 1990–2023; **both papers read the same kind of approval-trial record we use**…"

**Contradicted again at §8.4, L553 (v4's own text):**
> "…in drug approval, where sponsor-run trial results and regulator-reviewed labelling coexist in **documents already mined at scale** (Shi et al., 2021)…"

So the manuscript states in its abstract that this class of corpus is unexploited and outside the
frame, cites two papers four paragraphs later that exploit precisely this corpus at 5–7× the
scale, and then cites a third paper in §8.4 that mines administrative approval records at scale.
A referee will find this in ten minutes. **The defensible claim is much narrower and is already
true: the *trial-channel field* has never been extracted.** v3 stated it correctly at L39 ("a
feature of the official approval announcements that has not previously been exploited: each
announcement states… the name of the trial"). v4's framing generalised a precise claim into a
false one.

### M2 — §8.4's "portable diagnostic" inverts this paper's own finding

**L553:**
> "The test is the same and cheap in each case: partition fields by measuring party and check whether the contrast of interest holds the same sign in both partitions. **A contrast confined to the self-supplied partition is a candidate reporting artefact; one present in both is more likely real.**"

Apply that rule to this paper. The contrast here is confined to the **third-party** partition
(head-rice −1.84, chalkiness +1.11, stated grade −12.2 pp), and is *absent or reversed* in the
self-supplied partition (yield gain +0.55, if anything higher). Under the stated rule, a contrast
confined to one partition and absent in the other is a "candidate reporting artefact" — which
would make the paper's headline third-party result the suspect one. That is the exact opposite of
the paper's inference, which is that the *self-supplied* partition is the flattered one.

The recipe as written generalises a different, more common scenario (self-reported metric
inflated relative to an audited one). It does not generalise what this paper actually did. Either
the rule must be restated to cover the asymmetric case the paper found, or §8.4 must state
explicitly that this paper is the mirror case. As it stands, the flagship "portable" claim of the
intelligence section does not describe the paper carrying it.

### M3 — The title calls 品种审定 "registrations"

**L1:**
> "…third-party-assayed grain quality in China's rice variety **registrations**, 2017–2022"

"registration" appears four times in the manuscript: once here, once at L33 in a generic phrase,
and twice at L553 ("device registration"). **Everywhere else — including the abstract at L9 two
lines below — the paper says "approval"**, ~60 times, and §2 correctly names the governing
instrument *Measures for the Administration of Crop Variety **Approval*** (主要农作物品种审定办法).

In China's seed system 审定 (approval, for major crops incl. rice) and 登记 (registration, for
non-major crops) are distinct statutory procedures. A JIA editor or reviewer will read
"registrations" in the title of a 审定 paper as an error of the field, in the most visible line
of the submission. v3's title said "approvals". Fix to "approvals".

### M4 — §8.4's fourth bullet repeats §8.3 and overclaims the paper's actor-level content

**§8.3, L543 (v3 text):**
> "Third, the channel-of-entry information already exists inside every approval announcement but is not compiled or published as a standalone field; publishing it directly… would let downstream users of the seed catalogue — processors, distributors, other researchers — condition on it themselves."

**§8.4, L555 (v4 text), 12 lines later:**
> "The recommendation for the corpus publisher is correspondingly cheap: the channel already exists inside every announcement, and issuing it as a field would let downstream users condition on it directly (§8.3)."

This is the same recommendation twice in the same Discussion, and the second instance
cross-references the first — the text acknowledges its own duplication rather than resolving it.
Cut it.

The same bullet also overstates: "The indicators built here answer the questions such work
asks — **which actors produce approved varieties**, by which testing route, at what measured
quality." But §8.5 (L559) discloses that `applicant_type`, the field needed for any actor-level
statement, "is **entirely missing** for the 2016, 2017, 2018 and 2021 approval cohorts." The
paper cannot deliver the actor-level indicator the bullet advertises for four of its six years.

### S1 — The six new references are unread abstracts, cited only inside v4-added text

Citation census (body only, reference list excluded):

| Reference | Cited at | Uses | Independent of its pair? |
|---|---|---|---|
| Losiewicz et al., 2000 | L33, L555 | 2 | never — always paired with Antons |
| Antons et al., 2020 | L33, L555 | 2 | never — always paired with Losiewicz |
| Rammer & Es-Sadki, 2023 | L33, L549 | 2 | yes, but both are the same generic claim |
| Franceschini et al., 2016 | L246, L551 | 2 | yes — L246 is a real use |
| Jaffe & de Rassenfosse, 2017 | L551, L553 | 2 | yes — L553 is the best use in the set |
| Shi et al., 2021 | L553 | 1 | one clause |

Every one of those six line numbers is a v4 addition. **No new reference touches a v3 sentence.**
And the change log §7.1 concedes that none of the six was obtained in full text, so all citations
are restricted to "摘要与题名明确支持的一般性论断".

The consequence for R-A: the paper claims a methodological contribution *to* S&T intelligence,
and its entire engagement with the S&T intelligence literature consists of six abstracts, read at
title/abstract level, cited exclusively inside the three paragraphs added to make the claim. Two
of them (Losiewicz, Antons) are never invoked separately and function as a single citation.

Only Jaffe & de Rassenfosse (L553, examiner-added versus applicant-drafted citations) is used in
a way that engages an argument. That one is a genuinely good analogy and should be promoted.

### S2 — §3.4's Franceschini sentence reads as deflection

**L242–247:**
> "This is not a peculiarity of our source: large-scale audits of the databases on which S&T indicators are routinely built find systematic, non-negligible error rates in them as well (Franceschini et al., 2016), and the appropriate response is to state the verification status of a corpus rather than to assume it."

It is inserted between the admission that the corpus is an unverified third-party
re-transcription and the disclosure that the field-by-field cross-check (item P4) **remains
outstanding** (L253–258). Placed there, "Scopus and Web of Science have errors too" reads as a
softener for an unperformed verification. The second half of the sentence ("state the
verification status rather than assume it") is fine and is what §3.4 already does. Keep the
second half, cut the first.

### S3 — The paper claims an intelligence methods contribution while disclosing that its extraction was never validated

**L33:** "The first contribution of this paper is accordingly a methodological one for S&T intelligence".

**L253–258, ~500 words later:** "This verification step remains outstanding and is disclosed as such: **the authors will complete a manual, field-by-field cross-check… before submission**… No specific agreement-rate figure is reported here."

For an agronomy readership this is exemplary transparency about a data source. For the
*information-science* identity the paper now claims as co-equal, it is the central weakness: the
only reported extraction performance figure in the entire manuscript is the entity rule's
1.000/0.770, and field-level parse accuracy against the primary source is unmeasured. An
IP&M/JASIST referee would stop there. The dual identity is therefore asymmetrically risky — the
half the paper can fully defend is the agronomy half. This argues for the framing being presented
as *a lens on the finding*, not as a claimed methodological contribution.

### S4 — Change-log numbers do not reproduce

The change log's own header says v4 is **15,609 words**; `wc -w` gives **15,665** (+56). Three
further self-reported figures do not reproduce under a consistent tokenizer:

| Change log claim | Measured | Delta |
|---|---|---|
| v4 total = 15,609 words | 15,665 | +56 |
| §8.4 = 562 words | 539 (L546–555) | −23 |
| v3 §8.1 = "3段 ~450 词" | 349 | −101 |
| §8.1 compression = "~49%" | 349 → 232 = **−34%** | −15 pp |
| §3 preamble = "~210 词" | 241 | +31 |
| §3.1 entity para = "~170 词" | 198 | +28 |

None of these changes a scientific claim. But §10 of the change log asserts that a rigorous
token-level numeric diff was run, and a stale headline word count suggests the log was not
regenerated after the final edit. The §8.1 compression figure is overstated by 15 percentage
points. Treat the log's self-assessments as unverified going forward — which is what this review
did.

---

## 4. Where the 1,562 extra words went

Measured per diff hunk (`+added −deleted`, net **+1,582** by hunk accounting, +1,562 by `wc -w`):

| Location | Net words | Authorised by brief? | Earns its length? |
|---|---|---|---|
| Title / abstract / keywords / Highlights / Intro ¶1 compression | +235 | yes (§3.1–3.3) | yes — though Intro ¶2 (251 w) sits at the ceiling of the 200–250 budget |
| Intro contributions 1–2 + roadmap | +59 | no | partly — the frame sentence at L49 is useful |
| **§3 six-step pipeline preamble (L77–95)** | **+241** | **no** — brief said "补一段流程小标题与一句方法学定位" | **no** — signposting for headings that already signpost. Should be ≤60 words |
| §3.1 entity-resolution paragraph (L138–151) | +198 | no | **yes** — the one addition that closes a real gap |
| §3.3 opener (L178–182) | +62 | "一句" | **no** — restates the sentence it precedes |
| §3.4 Franceschini (L242–247) | +51 | no | half — see S2 |
| §7 cross-reference (L519) | +18 | no | yes |
| §8.1 compression | −106 | yes (§3.7) | yes, but −34% not the claimed −49% |
| **§8.4 new section (L546–555)** | **+539** | yes, budget 400–500 | **over by 8–35%**, and ~90 of those words are duplicative (M4) |
| **Conclusion rewrite (L567)** | **+90** | **no** | **no** — 149→239 words, restating §8.4 |
| References ×6 | +169 | yes (§3.7) | yes |

**Budget:** ~700–800 words of prose + ~170 of references ≈ 870–970.
**Actual:** +1,582.
**Overrun:** ~610–710 words, of which ~552 are unbudgeted §3 additions and ~90 an unbudgeted
Conclusion expansion.

**Judgement.** Of the ~700 unbudgeted words, **198 earn their place** (the entity-resolution
paragraph) and roughly **500 are signposting, restatement and duplication** (§3 preamble 241,
§3.3 opener 62, Conclusion 90, §8.4's duplicated recommendation ~60, §3.4's deflection clause
~25). This is padding of a specific and recognisable kind: prose that announces the frame rather
than using it. Cutting it would bring v4 to ≈15,150 words and would *strengthen* the framing by
removing the passages that most obviously exist only to carry it.

---

## 5. JIA fit: does the dual identity read as 两张皮?

**Yes, at the surfaces an editor screens first, and no, in the body.** The problem is precisely
that the intelligence identity lives only in the screening surfaces.

Passages that will trigger an out-of-scope reflex, in the order an editor encounters them:

1. **Title (L1).** The first seven words — "Mining administrative approval records for
   technology assessment" — contain no crop, no trait, no agronomy. A JIA editor triaging by
   title may route this to informetrics or desk-reject as out of scope before reaching
   "grain quality". Compounded by the "registrations" error (M3).

2. **Keywords (L15).** `administrative text mining; technology assessment; information
   extraction; data provenance; rice variety approval; China`. Four of six are pure
   information-science terms; **one** is agronomic. The brief asked for "1–2 agronomy words to
   keep JIA readers able to find it" and delivered the floor. An editor assigning reviewers by
   keyword will not surface a single rice agronomist. Swap `data provenance` → `rice grain
   quality`: grain quality is literally the paper's outcome, and provenance is well covered by
   `information extraction`.

3. **Highlights 1 and 5 (L21, L25).** Two of five highlights are crop-free method statements.
   Highlight 5 — *"Evidence strength varies across fields of one source with who measured the
   field"* — is intelligible only after reading the paper; as a standalone highlight in an
   agronomy journal it will read as a non sequitur. v3's displaced Highlight 5 ("A leading seed
   firm uses self-organised trials less, against low breeding capacity") was far more legible to
   the target reader.

4. **Abstract's final sentence (L9).** *"…a diagnostic that transfers to drug approval, device
   registration and patent examination corpora."* This is the last sentence a JIA editor reads
   before deciding. Ending an agronomy abstract on drug approval and patent examination is the
   single highest-risk sentence in the manuscript.

5. **§8.4 as a whole, especially L553.** 539 words on FDA drug labelling, medical-device
   registration and patent-examiner citations inside a rice paper. This is the passage that most
   reads as a second, unrelated paper stapled to the first.

**Against that**, the body is entirely safe: §§2–7 are agronomy and seed regulation throughout,
and the three JIA-precedent citations at L53 (Shi & Hu 2017; Qiu et al. 2016; Huang et al. 2018)
still anchor scope. But note that L53 itself was weakened in v4: "an institutional-economics
reading of a Chinese crop-sector regulation" became "a **text-mining** reading of a Chinese
crop-sector regulatory corpus", while the sentence continues to justify fit by pointing at three
*institutional-economics* JIA papers. The scope argument now names a method the cited precedents
do not share — the sentence half-defeats itself.

**Recommendation on positioning.** The dual identity is salvageable and should be kept, but the
ratio must invert at the screening surfaces: agronomy-first in title, keywords and abstract
opening; intelligence as the *generalisable lesson* in the Discussion and Conclusion, where it is
genuinely earned. Concretely: restore "approvals" and lead the title with the rice finding;
restore one agronomy keyword; move the transferability sentence out of the abstract's final
position (or make it a subordinate clause on a rice-anchored sentence); cut §8.4 to ~350 words
built around its one genuinely earned bullet.

**On JIA as target:** nothing here argues for changing journals. The intelligence contribution as
currently evidenced (no validated extraction accuracy, six unread references, a single-corpus
case) would not survive review at IP&M or TFSC. JIA remains the right venue — which is exactly
why the framing must not be allowed to obscure the agronomy at the point of triage.

---

## 6. What is genuinely good (not manufactured criticism)

To be clear about what survives scrutiny:

- **§8.4 bullet 2, "Reliability is a property of fields, not of sources" (L551).** This is the
  real intellectual payload of the reframing and it follows directly from this paper's result.
  It is not boilerplate; no other paper could carry this paragraph. It should be the spine of a
  shortened §8.4.
- **Jaffe & de Rassenfosse at L553** — the applicant-drafted-claims / examiner-added-citations
  parallel is apt, specific, and the one place the new literature earns its citation.
- **§3.1 entity-resolution paragraph (L138–151)** — the best addition in v4 on any criterion,
  independent of framing.
- **§8.1's compression and repositioning (L531–533)** — the retitle to "self-certification as
  theoretical support" and the explicit "not this paper's frame" sentence are exactly right, and
  all five references were retained rather than dropped. This is the one place where the
  reframing genuinely changed the paper's argumentative structure rather than its vocabulary.
- **Conclusion's "two faces" idea (L567)** is the correct final framing, even though its
  execution is 90 words too long and partly duplicates §8.4.

---

## 7. Must-fix items

| # | Item | Location |
|---|---|---|
| **M1** | Remove the internal contradiction. Abstract L9 "unexploited intelligence source" and Intro L33 "barely touched" / "sit outside this frame" are contradicted by L37 (Lu et al. 2024; Hang et al. 2024 read the same records) and by L553 ("already mined at scale"). Narrow the claim to what is true and already stated at L39: the **trial-channel field** has not been extracted before. | L9, L33 |
| **M2** | Fix the portability recipe. As written at L553 it classifies this paper's own finding as a "candidate reporting artefact". Restate the rule to cover the asymmetric case actually observed (contrast present in the independently-assayed partition and absent in the self-supplied one), or state explicitly that this paper is the mirror case. | L553 |
| **M3** | Title: "registrations" → "approvals". 审定 is approval; 登记 is registration; the rest of the manuscript, including L9, says approval. | L1 |
| **M4** | Cut §8.4's duplicated recommendation (L555, final sentence — already made verbatim in substance at L543), and drop or qualify "which actors produce approved varieties", which §8.5 (L559) discloses is unavailable for four of six cohorts. | L543/L555, L559 |
| **M5** | Make the framing carry load somewhere in §4–§6, or stop claiming it does. The minimum honest fix is one or two sentences in **§4.5** (L338–346) connecting the $Y^{3rd}$ / $Y^{self}$ formalism to provenance-stratified reliability assessment, and one in **§5.4** where the sign separation is reported. Currently the paper's only formal statement of its intelligence contribution sits in a paragraph v4 did not touch. Without this, the deletion test result stands as reported. | §4.5, §5.4 |
| **M6** | Cut the padding: §3 preamble (L77–95) from 241 to ≤60 words — the six step names plus the field-level-reporting rationale, dropping the subsection pointers that the headings now duplicate; delete §3.3's opener (L178–182), which restates the sentence after it; trim the Conclusion addition (L567) from 90 to ~40 words. Target ≈500 words of net reduction. | L77–95, L178–182, L567 |

## 8. Suggested items

| # | Item | Location |
|---|---|---|
| S-a | Keywords: swap `data provenance` for `rice grain quality`, restoring a second agronomy retrieval path without losing the intelligence signal. | L15 |
| S-b | Highlights: consider restoring v3's Highlight 5 (the Winall counter-case) in place of current Highlight 5, which is unreadable without the paper. Keeping Highlight 1 alone satisfies the brief's "at least one" method highlight. | L21–25 |
| S-c | Abstract: demote the transferability sentence from final position — end on rice, or fold transferability into a subordinate clause. | L9 |
| S-d | §3.4: cut the first half of the Franceschini sentence ("This is not a peculiarity of our source…"); keep "state the verification status rather than assume it". It currently reads as deflection ahead of the outstanding P4 disclosure. | L242–247 |
| S-e | L53: the scope paragraph now says "a text-mining reading" while justifying fit with three institutional-economics precedents. Either restore "institutional-economics" or add a clause acknowledging the method differs from the cited precedents. | L53 |
| S-f | Abstract L9 and L47: "17 fields" / "17-field indicator set" describes the count of analysed outcomes, not the extraction schema (the corpus also carries channel, trial_group, ck_n, approval_year, applicant_type). Say "17 analysed trait fields" or drop the number from the abstract. | L9, L47 |
| S-g | Promote Jaffe & de Rassenfosse from §8.4 into §3.3 or §4.5, where the applicant/examiner provenance parallel would actually support the argument rather than decorate the Discussion. | L551–553 |
| S-h | Regenerate the change log header (15,609 → 15,665) and correct §6.1 (562→539 words), §6.2 (v3 §8.1 349 not ~450; compression 34% not 49%), §5.2 (241 not ~210) and §5.4 (198 not ~170). | change log |

---

## 9. Recommendation

**Major revision.**

Reasoning. The empirical paper underneath is unchanged and, on this review line, uncompromised —
v4 altered no coefficient, no sample, no robustness conclusion, and §§4–6 were not touched at
all. The reframing did not damage the science. But R-A asks one question, and the answer is
negative: **the S&T-intelligence framing fails the deletion test.** Removing every intelligence
passage except one methods paragraph yields v3 intact, with no holes in the Introduction's
motivation and none in the Methods' logic — and in one place (Intro ¶2) removal improves the
text. The framing's vocabulary is a closed loop referenced only by itself; its six new references
touch no pre-existing sentence; and the one paragraph that formalises its claimed contribution
(§4.5) was not edited.

"Major" rather than "minor" rests on M1, M2 and M3, which are errors of fact and logic that v4
introduced — a false novelty claim contradicted twice within the manuscript, a generalisable
diagnostic that misclassifies the paper's own result, and a legally wrong term for 品种审定 in
the title. Those are not tuning.

None of the fixes requires new analysis, new data or new literature. A v5 editing pass
implementing M1–M6 — roughly 500 words cut, ~150 words added in §4.5/§5.4, and four corrected
sentences — would convert the framing from a wrapper into something that carries load, and would
simultaneously bring the manuscript back toward its word budget. I would expect to recommend
acceptance of the framing after that pass.
