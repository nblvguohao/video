# v4 review synthesis and the v5 decision

> Four independent reviews (R1 framework coherence, R2 integrity + data invariance,
> R3 numbering + citations, R4 journal fit + readability), plus three coordinator checks
> run directly against the data. 2026-09-16.
> Every finding recorded below as CONFIRMED was re-verified by the coordinator against the
> files or the CSVs, not accepted on a reviewer's word.

## Decision: **v5 is required before submission.** No re-analysis is needed.

Every blocking defect is an edit. Not one coefficient changes, no figure is re-rendered,
no model is re-estimated. The science underneath survived the hardest checks the panel
could aim at it. What failed is the framing added in v4, and housekeeping inherited from
v1–v3.

## The one finding that should change how v5 is approached

**The v4 reframing never touched the paper's reasoning.** `diff v3 v4` yields 14 hunks
whose headers jump from line 240 straight to line 516: lines 200–470 — all of §4
(identification), §5 (results) and §6 (robustness) — received **zero edits**. The word
"intelligence" appears at lines 9, 33, 47, 55, 75, 79, 80, then not again until 545.
Between line 80 and line 545, everything the paper argues, it never occurs once.
R1 ran the deletion test properly: it reverted all 20 framing edits and the result was
simply v3, complete and coherent.

So v5's central task is not to add more intelligence prose. It is to make the framing
carry load in §4.5/§5.4 — or to stop claiming it does and let the framing be an honest
secondary contribution. **Adding words is what produced this problem; adding more will
not fix it.**

R4 puts the same point from the other side and raises the stakes: the v4 reframing
*raised the evidentiary bar the paper must clear*. v3 could retreat to a composition-gap
claim under pressure; v4 cannot, because the measurement-attribution claim **is** its
headline contribution. More ambition, unchanged identification.

## Blocking defects, in the order they would sink the paper

### 1. Two self-contradictions a referee will find immediately
- **The verification contradiction (R4, CONFIRMED).** §3.4 says the MARA cross-check
  "will [be done] ... **before submission**" and reports no agreement rate; §8.5 line 559
  says completeness "**was checked** against a 50-record manual audit rather than assumed."
  A Methods section that says "we will do this before submission" means the paper is not
  ready to submit. In a paper whose thesis is that reliability depends on who measured,
  this is the worst possible place to be caught.
- **The abstract is refuted by the Introduction (R1, CONFIRMED).** Abstract line 9:
  approval announcements are "a long-public but **unexploited** intelligence source."
  Line 39: Lu et al. (2024) classify **17,785** approved varieties, Hang et al. (2024)
  track **11,811** regional-trial entries, and "both papers read the same kind of
  approval-trial record we use" — 5–7× this paper's 2,386. v3's narrow claim (the
  *channel variable* is unextracted) was true; v4 generalised it into a false one.
  **Restore the narrow claim.**

### 2. Numbers that disagree with the project's own outputs
- **+0.554 vs +0.553 (R2, CONFIRMED — predicted in `GROUND_TRUTH.md` before review began).**
  The CSV is 0.5534452 → **+0.553**. The manuscript carries **+0.554** at lines 360, 429,
  461, 489, while `submission/tables.md` line 108 already prints **+0.553**. The body and
  the submitted Table 3 contradict each other four times. Also hard-coded in
  `estimate_channel_gap.py:199` and `robustness_supplement.py:24`, and — noted for honesty —
  in my own review brief at `plan/06_v4_review_brief.md:45`. `results_notes_main.md:29`
  certifies the pair as "exact": **the verification step signed off the error**, which is
  the more important lesson than the digit.
- **§6.1 R5 says "8 retain q < 0.05"; the CSV gives 9 (CONFIRMED).** `grains_per_panicle`
  (q = 0.047376) is omitted, and its q is already printed in the submitted Table 3.

### 3. The paper is not dressed for a journal
- **15 internal project artifacts in the body (R4, CONFIRMED):** "this session's network",
  `feasibility_notes.md`, "Unresolved item P4" (×2), "prior planning notes", "an earlier
  planning-stage note" (×2), "Table 7 in the pre-submission working draft", "item for the
  author team", `analysis_rice_channel.pkl` (×2), `results_notes_main.md`,
  `scripts/analysis/`, `manuscript/tables/`, `submission/supplementary_material.md`,
  `[repository link]`. The transparency instinct is right; the venue is wrong.
- **"Pre-registered" claimed with no registry ID anywhere** and no pre-registration
  statement in the declarations (CONFIRMED). Editors check this. Either produce the
  registration or change the wording.
- **Financial residue survives in two journal-facing files (R2):**
  `submission/figure_captions.md:55` still names "the 2025 net-loss and 2026 ST status
  change"; `supplementary_material.md:13–15` discloses the removal was "at the author
  team's request". The v3 greps covered the manuscript and the DOCX/PDF, not the Markdown
  deliverables. **The v3 removal is therefore not actually complete.**
- **Six cross-reference errors (R3, three spot-CONFIRMED):** line 71 `Section 6` → §5.6;
  line 217 `§5` → §7; line 113 `§3.3` → §3.4; three mis-targeted `§4.4` pointers. All six
  are pre-existing from v3, not v4's doing. 78 of 84 pointers are correct.
- **DOCX leaks two literal `**` markers (CONFIRMED)** in the §4.5 hypothesis bullets. The
  PDF is fine, so the bug is in `scripts/build_docx.py`'s bold-inside-list-item path.
- **Reference record errors (R3):** Gong et al. 2026 has a paraphrased title and a
  **silently truncated** author list (the `…` was dropped in transcription; the real run is
  ≥14 names). Piepho & Laidig is **2025**, not 2024 — *Plant Breeding*, 144, 242–248.

### 4. The named-company problem was not solved
**R2's M4 is the finding I would have least expected and it deserves attention.** v3
balanced the *financial* register — but the praise that matters is *non-financial* and was
never in scope. §7 contains six favourable statements about a named listed firm and zero
counterweights; it is the only named commercial actor while its comparison group is
anonymous; and against a thesis that self-organised entrants deliver worse quality, §7
certifies this firm as the quality leader (+2.212 head-rice, p < 0.001). Non-claim 10
disclaims only financial evaluation, which is orthogonal to all six statements.
**Removing the negative information did not remove the one-sidedness; it concentrated it.**

## Where the panel was wrong, and I overruled it

**R4's "strongest attack" fix does not exist.** R4 named an uncontrolled approval-category
confound (高产稻 vs 优质稻) as the most damaging criticism available, called the fix cheap —
"the approval type is in the same announcements they already parse" — and called it *the*
change moving the paper from probably-publishable to hard-to-reject.
Tested against 7,883 raw records: `高产稻` **0**, `高产稳产` **0**, `绿色优质` **0**,
`审定标准` **0**, `品种类型` **0**, `品种类别` **0**. The 819 `优质稻` hits are all part of
《优质稻谷》, a grain-*grading* standard. The 32 `特殊类型` hits are trial-group labels already
excluded by the analysis stratum. **Do not pass this recommendation to the author as
written** — it sends them after a field that is not in the corpus.

The conceptual worry is still valid and belongs in Limitations: the paper cannot rule out
that channels differ in the implicit trait bundle applicants target, *because the approval
category is not recorded at all*. Stating that is stronger than silence.

**A substitute check that does run, and that the paper passes** (full detail in
`COORD_approval_type_confound.md`): records are graded under two different standards whose
mix flips across the window (2017: 111 GB/T vs 25 NY/T; 2021: 0 vs 305). Since Arm 2 sits
in 2017 and Arm 1 in 2019–2022, this looked threatening. But within each arm's own window
the standard does not vary by channel (Arm 1: 70.1% vs 60.4% NY/T; Arm 2: 65.5% vs 46.6%
GB/T), so the year × group × check fixed effects absorb it. The test also **independently
reproduces the headline result from raw shares**: the entire channel gap sits in the
*no stated grade* column, +10.1 pp (consortium) and +17.8 pp (green), against regression
estimates of −0.122 and −0.344. Add this as a real robustness item.

## The entity-rule question, adjudicated

I re-ran the validation the v4 agent admitted it had never executed: **n = 1,426,
precision 1.000, recall 0.770 reproduce exactly.** But precision 1.000 is measured against
a ground truth that reads the same pedigree field the rule reads, and under an
applicant-only ground truth 32% of rule-positive records were filed by other companies.

R2 adjudicated the interpretive question with data, and its answer is uncomfortable:
**§7's prose depends on the corporate-applicant reading, not the lineage reading.** The
decisive sentence (line 517) — "If enterprises are simply the more careless **applicants**,
Winall should be **the entrant** that looks most like the new channel" — is a non-sequitur
under lineage, since a germplasm pool has no channel-choice behaviour. R2's decomposition:
only 54 of 166 treated records (32.5%) name the firm or an affiliate as applicant; 37
(22.3%) are filings by other organisations — including 中国水稻研究所, 四川农业大学 and
中国农科院深圳基因组所, which is pointed, in a section rebutting an enterprise-vs-public-
institute alternative; 75 (45.2%) have no applicant field at all.

**The finding survives**: applicant-confirmed 66.7% vs pooled 60.2% vs comparison 47.5%,
so third-party filings dilute toward the control and the pooled estimate is conservative.
My worry in `VERIFY_entity_rule.md` that "the sign of the bias is no longer guaranteed"
resolves favourably — **but only because someone checked, and that check is not in the
paper.** Fix direction: realign §7's prose to lineage terms and disclose the composition
in §3.1. Useful side effect — lineage language cannot attribute market success to a
corporate entity, so this also does much of the de-branding that defect 4 requires.

## Journal: keep JIA

No alternative improves on it. JIA is the only option that is simultaneously CAS Tier 1,
IF ≥ 5.0, unambiguously agricultural (so 本学科 and the first-affiliation requirement are
unambiguous), and a good scope fit as written. TFSC and Government Information Quarterly
are credible Tier-1 fallbacks at the cost of a real rewrite. CAER and Rice Science fit but
drop the author onto the two-paper path — strictly worse against the stated criterion.
**Do not submit to IP&M**: regex + OLS is not a methodological contribution by their
standards.
The drift is confined to the five surfaces an editor triages on — title puts "rice" at
word 18, abstract opens and closes with no crop, 4 of 6 keywords are information science,
Highlights 1 and 5 are crop-free. The risk is not "wrong journal"; it is **no obvious
handling editor**. Rebalancing those five surfaces costs the intelligence contribution
nothing. Name the Agricultural Economics and Management section in the cover letter.

## v5 work plan

**Tier 1 — blocking, do first**
1. Resolve the verification contradiction (§3.4 vs §8.5). Either run the 50-record audit
   and report the agreement rate, or delete the §8.5 claim and keep §3.4 honest.
2. Fix +0.554 → +0.553 at lines 360, 429, 461, 489, plus both scripts; and 8 → 9 at line 469.
3. Strip all 15 internal artifacts; supply author list, CRediT, acknowledgements, data link.
4. Resolve the pre-registration claim — registry ID or reword.
5. Purge financial residue from `figure_captions.md` and `supplementary_material.md`.
6. Correct the Gong et al. 2026 title and restore the truncated author list; fix
   Piepho & Laidig to 2025, 144, 242–248, and the two in-text cites.

**Tier 2 — framing, the real work**
7. Restore the narrow, true "unexploited" claim in abstract and §1¶2.
8. Fix the title: 审定 is *approval*, not *registrations*; move "rice" forward.
9. Rebalance keywords and Highlights 1 and 5 toward agronomy.
10. Make the framing load-bearing in §4.5/§5.4, or downgrade the claim. Do not add prose.
11. Realign §7 to lineage language; add the §3.1 composition disclosure; de-brand.
12. Give §8.4's portable diagnostic a third branch covering the confined-to-third-party
    case — the case this paper actually exemplifies. (R1 called this a contradiction; it is
    an incompleteness. The fix is one clause.)

**Tier 3 — quality**
13. Cut ~1,800 words (R4's list): §6.5 → supplement, §8.2's verbatim reprints of §5.5/§6.4,
    §5.4's restatement of §4.5, §1 line 53's cover-letter paragraph.
14. Halve the 73 "rather than" constructions.
15. Add the quality-standard composition check as a new robustness item; add the
    approval-category limitation to §8.5.
16. Fix `build_docx.py`'s bold-in-list bug and rebuild.
17. Six cross-reference corrections; refresh `figure_table_list.md`'s v3 header.

**Not doing:** R4's R17 as specified — the field does not exist in the corpus. Record this
explicitly in the v5 change log so it is not silently dropped and re-raised later.
