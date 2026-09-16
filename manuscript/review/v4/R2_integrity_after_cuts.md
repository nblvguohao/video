# R2 — Integrity after the v3 excisions (R-B) and data invariance (R-E)

**Reviewer line:** R-B + R-E of `plan/06_v4_review_brief.md`
**Manuscript under review:** `manuscript/manuscript_v4.md` (660 lines)
**Comparators:** `manuscript/manuscript_v3.md`, `manuscript/manuscript_v2.md`
**Also read:** `manuscript/review/v4/VERIFY_entity_rule.md` (coordinating session's independent
re-run of the §3.1 entity rule), whose open question — does §7 depend on the lineage reading or
the corporate-applicant reading? — is adjudicated in **R-B.7** below, with my own re-computation.
**Numeric authority:** `manuscript/review/v4/GROUND_TRUTH.md`, cross-checked directly against
`manuscript/tables/table3_main_results.csv`, `table7_enterprise_vs_public.csv`,
`table5_winall_positioning.csv`, `table5b_winall_channel_choice_logit.csv`,
`table_r10_drop_winall_robustness.csv`, `table_event_study_by_year.csv`,
`table_breakpoint_scan_full.csv`.
**Date:** 2026-09-16

---

## Overall assessment

**R-E (data invariance): PASS, with two numeric defects.** This is the strongest part of the
v4 revision. A mechanical token-level diff of v3 against v4 shows that **not one numeric token
present in v3 is absent from v4, and not one changed value**. §4.7 (Non-claims), §5 (Results)
and §6 (Robustness) are **byte-identical** between v3 and v4; §7 differs by exactly one
inserted parenthetical. The invariance claim in `change_log_v3_to_v4.md` §10.1 is therefore
verified, not merely asserted. All 8 CF items, all 16 R-checks and all 12 Non-claims are
present and unsoftened. Every headline coefficient, CI, SE, p-value, n, year-by-year
coefficient and breakpoint Wald statistic I could trace to a CSV matched to the reported
precision — **with two exceptions**: the regional-trial yield gain is carried as **+0.554**
where the CSV gives 0.5534 → **+0.553** (and where the paper's own submitted Table 3 already
prints +0.553), and R5's count of BH-surviving outcomes is **8** where the CSV gives **9**.
Both are inherited from v3/v2 rather than introduced by v4, but both are live errors in the
file that would go to the journal, and the first produces a visible text-versus-table
contradiction inside the submission package.

**R-B (integrity after the cuts): the logic survives; the publication-ethics risk does not.**
Tracing the counter-case chain sentence by sentence confirms that **no step depended on the
deleted financial material**. The deleted v2 paragraph was explicitly a *qualifier*, not a
premise — it opened "This pattern must be read alongside, not instead of, a set of financial
facts that are **unrelated to which trial channel Winall used**." Removing a qualifier cannot
break a deduction. So R-B item 1 passes.

R-B item 3 does **not** pass. v3's stated strategy — cut the positive material too, so the
section does not become promotion — was only half executed. What was cut was the *financial*
material, positive and negative. What remains is a body of **non-financial praise** that was
never in scope for the cut and is now completely uncountered: within §7 the named listed
company is described as the single largest beneficiary of the reform, a certified
breeding-production-extension enterprise, a MARA "strong-advantage" seed company, the firm the
green channel was designed to serve, the firm that uses the honest channel more than its peers,
and the firm whose varieties measure significantly better than every other applicant's on all
three third-party-assayed quality traits at p < 0.001. There is not one offsetting or even
neutral-unfavourable statement about the firm anywhere in the manuscript. It is also the
**only named commercial actor in the paper**; its comparison group is anonymous. Against a
thesis whose headline finding is that self-organised-channel entrants deliver worse
third-party-assayed quality, §7 reads as an independent certification that this one named firm
is the quality leader and its (unnamed) competitors are the ones exploiting measurement
discretion. That is a stronger promotional signal than any of the financial facts that were
removed, and it is what a suspicious editor would zero in on.

Three further R-B defects are traceable to the cut itself: a logical contradiction that the
deleted paragraph used to blunt (§7, line 519), an orphaned Xie et al. (2023) citation whose
only remaining job in v2 was to source the deleted table, and — most seriously — **financial
residue surviving in three journal-facing submission files**, including a figure caption that
still names "the 2025 net-loss and 2026 ST status change."

**Separately (R-B.7), §7 describes lineage-derived records in corporate-agency language.** The
`winall` indicator is, as §3.1 correctly states, a germplasm-lineage construct. §7's prose is
uniformly in the corporate-filing register — "its share of national approvals", "where Winall
applied", "channel choice", "Winall's own entrants", "its varieties". I checked the data: in
§7's own sample of n = 166, **only 54 records (32.5%) name the firm or a 荃银-branded affiliate
as applicant**; 37 (22.3%) are named filings by other organisations (江苏中江种业, 中国种子集团,
湖北省种子集团, 北京金色农华, and — pointedly, in a section rebutting an enterprise-versus-public-
institute alternative — 中国水稻研究所, 四川农业大学 and 中国农业科学院深圳农业基因组研究所); 75
(45.2%) have no applicant field at all. **The good news, which I computed and which the paper
should report: the finding survives and the pooled estimate is conservative** — the
applicant-confirmed subset uses the unified channel **66.7%** of the time, versus 60.2% pooled
and 47.5% for the comparison group. So this is a disclosure-and-wording defect, not a broken
result. But it is a must-fix, because a referee who checks will find that two-thirds of
"Winall's own entrants" are not Winall's filings.

**Recommendation: Minor revision.** No result needs re-running and no argument needs
rebuilding. The fixes are surgical: two number corrections, one sentence rewrite, one sentence
relocation, three provenance notes stripped from submission files, a realignment of §7's prose
to the lineage construct it actually implements, and a short neutralising addition to §7.

---

## R-B findings

### R-B.1 — The counter-case logic chain holds end to end (PASS)

§7 (`manuscript_v4.md` lines 513–525) runs as follows. I number the steps and mark
dependence on deleted material.

| # | Step | Location | Depended on deleted financial material? |
|---|---|---|---|
| S1 | Alternative explanation stated: "perhaps seed-marketing enterprises are simply less careful breeders than public research institutes, and the new channels happen to be where enterprises concentrate" | L517 | No |
| S2 | "Anhui Winall Hi-Tech Seed Co. lets us test this alternative directly." | L517 | No |
| S3 | Winall established as the prototypical enterprise/green-channel target | L517 | No |
| S4 | Prediction under the alternative: "Winall should be the entrant that looks *most* like the new channel" | L517 | No |
| S5 | Xie et al. (2023) scope sentence | L517 | **Was rewritten in v3 because it pointed at the deleted table** — see R-B.3 |
| S6 | "It is not." — 60.2% vs 47.5% unified use; logit α = −0.728, p < 0.0001, OR 0.483 | L519 | No |
| S7 | Within-unified positioning: +2.212 / +9.8 pp / −0.692, all p < 0.001 | L519 | No |
| S8 | Edge vanishes inside the new-channel subsample (p > 0.18) | L519 | No |
| S9 | Inference: "A firm that were simply better at breeding across the board should retain some of this edge wherever its varieties enter" | L519 | No — but see R-B.2 |
| S10 | R10 drop-Winall robustness | L521 | No |
| S11 | Enterprise-vs-public descriptive panel as population-level counterweight | L523 | No |
| S12 | Two scope limits | L525 | No |

I then read the deleted v2 paragraph (`manuscript_v2.md` §7, para 4) in full. Its opening
sentence is decisive:

> "This pattern must be read alongside, not instead of, a set of financial facts that are
> **unrelated to which trial channel Winall used** but are directly relevant to how the
> company's overall business should be judged."

The paragraph is self-declared as orthogonal to the identification argument, and its closing
sentence — "two separate and simultaneously true facts about the same firm" — confirms it was
a *balancing* device, not a load-bearing premise. **No step S1–S12 loses a premise.** The
change log's assessment on this point (`change_log_v2_to_v3.md` §1, "Checked for a dangling
transition") is correct as far as it goes.

Section length: v2 §7 = 1,155 words; v3 §7 = 870; v4 §7 = 888 (the +18 is the entity-resolution
parenthetical added in v4). The brief's "1,110 → 870" is close enough.

### R-B.2 — MUST FIX: S9's concluding sentence contradicts §2 and §3.3

`manuscript_v4.md` line 519, final clause:

> "A firm that were simply better at breeding across the board should retain some of this edge
> wherever its varieties enter; **Winall's edge is specific to the channel in which quality is
> measured by the same third party as everyone else.**"

This asserts that there is a channel in which grain quality is *not* measured by the same third
party. The paper says the opposite, twice, as a foundational premise:

- §2, line 67: "The channel through which a variety enters — unified trial, green channel, or
  consortium trial — therefore determines who measures its agronomic performance, **but not who
  measures its grain-processing and appearance quality**; the latter is measured by the same
  designated third-party laboratories under NY/T 593 **irrespective of channel**."
- §3.3, lines 185–188: head-rice, chalkiness and the stated grade "are **all** assayed by
  MARA-designated third-party grain-quality laboratories under the national testing standard
  NY/T 593."

Head-rice, chalkiness and stated grade — the exact three traits in S7/S8 — are third-party
measured in *both* subsamples. So the sentence is, on the paper's own account, either vacuous
or false, and as written it implies the new channel's quality figures are self-measured, which
would collapse the paper's whole measuring-party architecture.

This is a pre-existing sentence (identical in v2), but the cut is what promoted it: in v2 it
was immediately followed by the qualifying paragraph, so it read as one half of a two-sided
discussion. In v3/v4 it is the terminal sentence of the paragraph and the rhetorical high point
of the section, with nothing after it. **Rewrite required.** The defensible version of the
point is about the *comparison set*, not the measuring party — e.g. "Winall's measured
advantage appears only when it is compared against entrants tested in the same state-run trial;
it does not appear against entrants tested in self-organised trials." Note that this weaker
version also weakens S9's inference, which is appropriate: S8's three nulls (p = 0.548, 0.184,
0.655 in `table5_winall_positioning.csv`) cannot by themselves establish that a general
breeding advantage is absent.

### R-B.3 — MUST FIX (editorial): the Xie et al. (2023) sentence is now orphaned and sits across the section's key transition

`manuscript_v4.md` line 517, final sentence (90 words):

> "Winall's own contract-farming business is separately the subject of Xie et al. (2023), which
> models the seed enterprise's choice of contract design for its order-grain quality incentives
> with a three-tier supply-chain game and a numerical example, but at the firm level and without
> any variety-level data; this section's own analysis is confined to the variety-level
> channel-choice and within-channel positioning evidence reported below, and **does not draw on
> or reproduce Xie et al.'s firm-level contract data**."

Two problems, both created by the cut.

**(a) It is a dangling transition.** The section's setup is S4 — "If enterprises are simply the
more careless applicants, Winall should be the entrant that looks *most* like the new channel."
The payoff is the first two words of the next paragraph: **"It is not."** In v2 these were
adjacent in argumentative function; the Xie sentence then ran on into the financial-table
pointer, which belonged with what followed. In v4, 90 words about a different paper's
game-theoretic model sit between the antecedent and the anaphor, and the bare copula "It is
not" now has to reach back across that digression to recover "Winall is not [the entrant that
looks most like the new channel]." This is precisely the class of artefact R-B item 2 asks
about. Move the Xie sentence to the end of the paragraph, or to §2/§8.1 where its background
role is honest.

**(b) It is an orphaned citation.** Per `change_log_v2_to_v3.md` §1, third bullet, this
sentence's original function was to source the order-grain revenue-share and gross-margin
figures in the now-deleted Supplementary Table S1. v3 replaced that clause with a disclaimer.
What remains is a sentence that describes a cited paper in detail and then states that this
paper does not use it — a citation retained for compliance with the format spec's required-
citation list, not because it does any work. It also adds promotional texture: it informs the
reader that this named firm's contract-farming design is the subject of a published
*Agribusiness* paper. Recommend relocating it and shortening it to a background citation.

### R-B.4 — MUST FIX: §7 now reads as one-sided promotion of a named listed company

This is the risk v3 set out to avoid, and it was not avoided. The v3 operating principle
(`change_log_v2_to_v3.md`, preamble) was: "rather than deleting only the negative Winall
material and leaving the positive material in place — which would have turned the paper into
one-sided promotion of a real, named company — the entire financial/business narrative about
Winall, positive and negative alike, was removed." The category that was balanced is
**financial**. The category that carries the praise is **non-financial**, and it was never in
scope for the cut. Here is the complete inventory of evaluative statements about the firm in
v4:

**Favourable (6):**

1. §1, line 51: "we use Anhui Winall Hi-Tech Seed Co. — **the single largest beneficiary of
   rising national-approval share among integrated seed enterprises over this period, and a firm
   the green channel was in principle designed to serve** — as a counter-case"
2. §7, line 517: "Winall is **the single largest beneficiary of the reform period among
   integrated seed enterprises** — its share of national approvals in the two major indica trial
   groups rose from 0–12% in 2005–2015 to 23–31% in 2022–2024"
3. §7, line 517: "it is **a certified breeding-production-extension enterprise and a Ministry of
   Agriculture and Rural Affairs 'strong-advantage' seed company, the profile the green channel
   was designed to serve**"
4. §7, line 519: "Winall-linked records … **used the unified channel 60.2% of the time, against
   47.5% for all other applicants**" (i.e. it avoids the channel the paper associates with
   measurement discretion)
5. §7, line 519: "Within the unified channel, **Winall's own entrants also outperform other
   unified entrants on the same third-party-assayed traits that define the main result**:
   head-rice percentage +2.212 points, probability of a stated quality grade +9.8 points,
   chalkiness −0.692 points (all p < 0.001)"
6. §9, line 565: the headline result "**survives dropping the single largest beneficiary firm
   from the sample**"

**Unfavourable or neutral-limiting about the firm itself: zero.**

The one apparently deflating statement — §7, line 519, "This within-channel advantage is not a
general Winall effect" — is framed as *supporting* the paper's argument, and is immediately
converted back into a favourable claim by the sentence flagged in R-B.2.

A suspicious editor would put these three things side by side:

- the manuscript names exactly **one** commercial firm, favourably, while its entire comparison
  group ("all other applicants", n = 1,101) is anonymous;
- the manuscript's thesis is that firms entering through self-organised channels deliver worse
  third-party-assayed quality, and this one named firm is shown to (a) avoid that channel and
  (b) beat everyone else on quality at p < 0.001 — i.e. the paper independently certifies a
  specific listed company as the market's quality leader;
- line 579: "**The authors declare no conflict of interest.**"

and would ask why. The existing safeguards do not reach this. Non-claim 10 (line 413) disclaims
only *financial* evaluation — "This paper does not evaluate the overall financial performance,
business strategy, or corporate governance of any applicant firm, including Winall" — which is
exactly orthogonal to the six statements above. The §7 scope limits (line 525) restrict the
*inferential* reach ("not evidence of a causal mechanism"), not the evaluative content. And the
v3 edit to the Ethical approval statement (line 607, now "it uses only publicly available
government variety-approval announcements") removed the last trace that the firm's public
record was ever examined at all.

**Fix — three parts, none requiring new analysis:**

1. **De-brand the counter-case where the name is not load-bearing.** The argument needs "a
   large, certified, integrated seed enterprise of exactly the profile the green channel was
   designed to serve." It does not need the superlative. Delete "the single largest beneficiary
   of the reform period" from §7 line 517 and §1 line 51, and "the single largest beneficiary
   firm" from §9 line 565 (R10 is adequately described as "dropping the focal firm", which is
   already the wording used at line 472). Keep the approval-share series — it is the evidence
   for the profile claim — but state it as a fact, not as a ranking.
2. **Neutralise S7.** The within-unified positioning result (+2.212 / +9.8 pp / −0.692) is the
   single most promotional sentence in the paper and is *not* required by the counter-case: S1→S6
   alone rebuts "enterprises are careless." Either demote it to a sentence that reports the
   contrast without the verb "outperform" and with the new-channel nulls given equal billing in
   the same sentence, or move it to the Supplementary Material alongside Table 5. If it is kept,
   it needs an explicit limitation sentence — it is a within-sample descriptive contrast on
   n = 494–503 records with no correction for the firm's trait-space or trial-group
   specialisation, and the 0.770-recall entity rule means the comparison group contains
   Winall records.
3. **Extend Non-claim 10 to cover non-financial evaluation.** Add a clause: this paper does not
   assess, rank or endorse the breeding capability, product quality or market standing of any
   named applicant, and the firm's appearance is determined solely by its role in falsifying one
   alternative explanation. This is the cheap fix that closes the gap Non-claim 10 currently
   leaves open, and it costs the paper nothing.

Also worth the authors' attention, though outside the strict R-B remit: the counter-case is a
**case selected on success**. §7 tests "is the *most successful* integrated enterprise
careless?" and generalises to "are enterprises careless?". Scope limit 1 (line 525) addresses a
different issue (comparison against all applicants rather than against other integrated firms).
The selection issue should be named. This weakness was less visible in v2 because the deleted
paragraph established that the firm's quality strategy had not in fact been an unambiguous
success.

### R-B.5 — MUST FIX: financial residue survives in three journal-facing submission files

`change_log_v2_to_v3.md` §9 reports full-text greps against `manuscript_v3.md` and the rebuilt
`.docx`/`.pdf`. It did not grep the Markdown submission deliverables. Three of them are journal
deliverables, not internal notes, and all three still narrate the excision:

- **`submission/figure_captions.md`, line 55** — the worst case, because it names the facts:
  > "In v3, a former third panel (c) — order-grain revenue share and R&D-intensity time series,
  > with **the 2025 net-loss and 2026 ST status change** annotated — was removed at author
  > request, since it reported firm-level financial performance"

  This reproduces two of the specific negative facts about the named listed company, in a file
  that goes to the journal.
- **`submission/figure_captions.md`, line 10** — "Fig. 6's former panel (c), reporting Winall's
  financial performance, has been removed".
- **`submission/supplementary_material.md`, lines 13–15** — "the former Supplementary Table S1
  (Winall and comparator company financial panel) has been **removed in full**, **at the author
  team's request** that no discussion of any applicant firm's financial or business performance
  appear in the paper."
- **`submission/tables.md`, line 11** — "Table S1 (Winall financial panel) was removed and the
  former Table S2 renumbered to S1".

Beyond leaking the content, lines 13–15 of `supplementary_material.md` actively tell an editor
that **the author team requested suppression of financial information about a named company**.
Combined with the uniformly favourable §7 and the "no conflict of interest" declaration, that
is the single most damaging sentence in the package.

**Fix:** strip all removal-provenance notes from `figure_captions.md`,
`supplementary_material.md` and `tables.md`. Version history belongs in
`manuscript/review/change_log_*.md` and `submission/VERSION_HISTORY.md` (internal), not in
files the editor reads. The renumbering footnote in `supplementary_material.md` lines 25–26
("Formerly Table 7 … formerly Supplementary Table S2") is also unnecessary and should go; the
journal receives one numbering, not its history.

### R-B.6 — No other dangling references, orphans or unfulfilled promises (PASS)

Checked and clear:

- No residual "this pattern" / "as noted above" / "described above" anaphora in or near §7
  pointing at deleted text (grep over the full manuscript; the only "alongside" occurrences are
  §3.2/§3.3 Manski and Fig. 1 usages, plus §9's unrelated sense).
- No forward promise anywhere in §1–§6 that the deleted material was to fulfil. §1 mentions
  Winall only at lines 51 and 55, and the §1 roadmap sentence ("Section 7 examines Winall
  Hi-Tech as a counter-case") is fulfilled.
- Paragraph join at the deletion site (S9 → S10, lines 519 → 521) is clean; R10's topic sentence
  is self-contained.
- No residue of "financial", "profit", "margin", "revenue", "order-grain", "audit opinion",
  "ST Winall", "tender", "penalty" in `manuscript_v4.md` other than Non-claim 10 and the
  Xie et al. sentence's "order-grain quality incentives" (a description of a contract-design
  model, not a financial claim).
- Supplementary Table S1 renumbering is consistent inside the manuscript (§4.7 Non-claim 9
  line 412; §7 line 523).

One minor heading/content mismatch, pre-existing: §7 is titled "**Mechanism**: Winall Hi-Tech
Seed as a counter-case" while line 525 states the section is "not evidence of a causal
mechanism." Suggest retitling to "A counter-case: Winall Hi-Tech Seed".

### R-B.7 — MUST FIX: §7's argument is written in the corporate-applicant register, but the indicator is a germplasm-lineage construct

This addresses the open question in `VERIFY_entity_rule.md` lines 73–75. My determination:
**§7's argument as written depends on the corporate-applicant reading**, not the lineage
reading. Not one load-bearing sentence in the section survives translation into lineage terms
without losing its force.

#### (a) Sentence-by-sentence: every load-bearing sentence ascribes corporate agency

I checked every sentence in §7 (and §1, §4.6) that describes these records. Quoting, with the
agency-bearing language in bold:

| Line | Sentence | Register |
|---|---|---|
| 517 | "If so, the quality gap would reflect ***who* enters through each door**" | applicant — the alternative explanation is itself about applicant identity |
| 517 | "**its share of national approvals** in the two major indica trial groups rose from 0–12% in 2005–2015 to 23–31% in 2022–2024" | corporate — an ownership share |
| 517 | "**it is a certified** breeding-production-extension enterprise and a MARA 'strong-advantage' seed company" | corporate — a legal status held by an entity |
| 517 | "If enterprises are simply the more careless **applicants**, Winall should be **the entrant** that looks most like the new channel" | applicant — the syllogism's major premise |
| 519 | "Winall-linked records … **used the unified channel** 60.2% of the time" | corporate — "used" ascribes a decision to an agent |
| 519 | "A logit for **channel choice** … confirms this is not an artefact of **when or where Winall applied**" | corporate — *applied* is a filing act |
| 519 | "being Winall-linked is associated with roughly half the odds of **entering through a new channel**" | corporate |
| 519 | "Within the unified channel, **Winall's own entrants** also outperform other unified entrants" | corporate — the strongest ownership phrase in the paper |
| 519 | "A firm … should retain some of this edge wherever **its varieties** enter" | corporate |
| 525 | "the comparison is **Winall against *all* other applicants** pooled together" | applicant — the control group is defined by applicant identity |
| 51 | "the single largest beneficiary of rising **national-approval share** among integrated seed enterprises" | corporate |

The decisive one is line 517: *"If enterprises are simply the more careless **applicants**,
Winall should be **the entrant** that looks most like the new channel."* That is the major
premise of the whole counter-case. Under the lineage reading it becomes "if enterprises are
careless applicants, then varieties descended from 荃-series germplasm should look most like the
new channel" — a non-sequitur, because a germplasm pool is not an applicant and has no
channel-choice behaviour. The channel is chosen by whoever files. **The syllogism requires the
treated group to be the firm's own filings.**

#### (b) What the data actually contains (my independent re-computation)

Reproducing §7's sample from `evidence/data/analysis_rice_channel.pkl` — national (国审)
approvals, approval years 2017 and 2019–2022 — recovers the manuscript's figures exactly
(n = 166 firm-linked at 60.2% unified; n = 1,101 others at 47.5%), confirming I am looking at
the right group. Decomposing that group by whether the applicant string names the firm:

| Subset | n | % of 166 | Unified-channel share |
|---|---|---|---|
| **All firm-linked records (the manuscript's group)** | **166** | 100% | **60.2%** |
| (a) applicant names 荃银 (firm or a 荃银-branded affiliate) | 54 | 32.5% | **66.7%** |
| (b) applicant does not name 荃银 | 112 | 67.5% | 57.1% |
| (b1) — applicant field missing/unknown | 75 | 45.2% | 60.0% |
| (b2) — applicant **named, and it is another organisation** | 37 | 22.3% | 51.4% |
| Comparison group ("all other applicants") | 1,101 | — | 47.5% |

Reproduction (the whole check is six lines, and the authors should run it before submission):

```python
import pandas as pd
d = pd.read_pickle('evidence/data/analysis_rice_channel.pkl')
s = d[(d.level == '国审') & (d.approval_year.isin([2017, 2019, 2020, 2021, 2022]))]
w = s[s.winall == True]                      # n = 166, matches §7
named = w.applicant.astype(str).str.contains('荃银')
for lbl, g in [('all', w), ('applicant names firm', w[named]), ('does not', w[~named])]:
    print(lbl, len(g), round((g.channel == 'Unified').mean() * 100, 1))
```

Subset (a) is generous to the authors: I counted any applicant string containing 荃银, which
sweeps in 安徽荃银超大种业, 安徽荃银禾丰种业, 四川荃银种业, 湖北荃银高科种业, 广东荃银种业,
上海中科荃银分子育种 and 安徽荃银农业高科技研究所 as the firm. **32.5% is therefore an upper bound
on applicant confirmation.** So roughly **two-thirds of the records the manuscript calls
"Winall's own entrants" are not confirmed as the firm's filings, and 22.3% are positively
identified as someone else's.**

The named third-party filers in §7's sample are: 江苏中江种业 (5), 中国种子集团 (4), 江西天涯种业
(3), 安徽喜多收种业 (3), 湖北省种子集团 (2), 北京金色农华 (2), and a tail of singletons including
**四川农业大学水稻研究所, 四川农业大学, 中国水稻研究所, 中国农业科学院深圳农业基因组研究所,
江苏丘陵地区镇江农业科学研究所 and 合肥信达高科农业科学研究所**. That last group is a specific,
pointed problem rather than a general dilution one: §7's entire job is to rebut an
**enterprise-versus-public-research-institute** alternative, and the treated group — the
"enterprise" side of that test — contains public research institutes and a national academy
institute.

A second, related contamination: **17 named organisations appear as applicants in *both* the
treated and the comparison group, accounting for 100 of the 1,101 comparison-group records
(9.1%)** — 中国水稻研究所 (14), 北京金色农华 (14), 中国种子集团 (12), 科荟种业 (9), and others. So
under the applicant reading, "Winall against all other applicants" is not a clean partition:
the same firms sit on both sides of the comparison.

#### (c) The finding nevertheless survives — and the paper should say so with this number

This is the part the authors will want. The applicant-confirmed subset does **not** weaken the
result; it strengthens it. Records that genuinely name the firm use the unified channel
**66.7%** of the time — further from the 47.5% comparison group than the pooled 60.2% — while
the third-party-filed records (51.4%) sit close to the comparison group and pull the pooled
estimate toward zero. **The conservative-bias claim at §3.1 line 146 and §7 line 519 therefore
happens to hold for the treated group as well as for the unrecalled records, but the manuscript
does not know this and does not argue it.** `VERIFY_entity_rule.md` line 64 is right that "the
sign of the bias is no longer guaranteed" — it is guaranteed only because I checked, and the
check is not in the paper.

#### (d) Why the lineage construct is nonetheless the right choice, and what that implies

Two facts make it impossible simply to switch §7 to the applicant reading:

1. **The applicant reading is not computable across the sample.** §3.3 line 219 states the
   applicant field "is entirely missing for national approvals in 2016, 2017, 2018 and 2021
   (904 records)." Recomputing the approval-share series under an applicant-only definition
   returns **0.0% for 2017 and 0.0% for 2021** — two of the five years in §7's own window —
   purely because the field is absent. This is exactly the structural gap §3.1 line 138 gives as
   the reason the entity rule exists ("the announcements do not carry a stable applicant
   identifier … for four approval years the applicant field is absent altogether"). The rule is
   well motivated; the prose is what is wrong.
2. **Resolving the 37 third-party filings would require exactly the research the paper has
   excised.** Deciding whether 江苏中江种业 or 湖北省种子集团 is a group subsidiary, a licensee, or
   an arm's-length purchaser of germplasm requires corporate-ownership information — precisely
   what Non-claim 10 (line 413) commits the paper not to introduce ("This paper does not evaluate
   the overall financial performance, business strategy, or corporate governance of any applicant
   firm"). The paper cannot tighten the applicant reading without re-entering the territory v3
   removed.

The resolution therefore runs the other way: **make §7's prose match the lineage construct the
indicator actually implements.** This is a wording fix, not a re-analysis, and it has a useful
side effect — it is simultaneously a large part of the de-branding required by **M4**, because
germplasm-lineage language stops attributing agency, market success and product quality to a
named corporate entity.

#### (e) One further number this undermines

§7 line 517's "**its share of national approvals** in the two major indica trial groups rose
from 0–12% in 2005–2015 to 23–31% in 2022–2024" — the evidentiary basis for the "single largest
beneficiary" superlative — has three problems once the indicator is read correctly:

- It is a **lineage** share, not a corporate approval share, so "its share" is the wrong
  possessive. Recomputing under the applicant-named reading gives 11.2% / 28.3% / 25.6% for
  2022–2024, and is undefined for 2017 and 2021.
- The 2022 value does not reproduce cleanly: on the lineage flag over the two indica trial
  groups I get 21.3% for 2022 (2023: 32.1%, 2024: 30.8%), against the stated lower bound of 23%.
  The authors should confirm the exact stratum; I may be using a slightly different denominator.
- **Two of the three years cited lie outside the paper's own analysis window and inside the
  period the paper says it cannot trust.** §3.1 line 112 reports the corpus captures 85 of 409
  announcements for 2023 and 61 of 405 for 2024 — roughly 21% and 15% coverage — and Non-claim 7
  (line 410) bars approval counts as an outcome for exactly this reason. Using 2023–2024
  approval shares to crown a named company "the single largest beneficiary" leans on the two
  worst-covered years in the corpus.

#### Fix

One disclosure paragraph in §3.1 and a wording pass over §7. No re-analysis.

1. **§3.1 (after line 146)** — add: (i) the filter is `applicant_type != 'Unknown'`
   (n = 1,426), so a replicator can reproduce it; (ii) the precision-1.000 validation target
   shares the pedigree field with the rule under test, so it is a consistency check rather than
   an independent gold standard; (iii) the indicator is deliberately lineage-based and roughly
   two-thirds of firm-linked records do not name the firm as applicant — intended, because the
   counter-case concerns the firm's germplasm, and because the applicant field is absent for four
   approval years; (iv) state the treated-group composition alongside the existing
   false-negative argument, since §3.1 currently argues conservativeness only for unrecalled
   records.
2. **§7 line 519** — replace corporate-agency wording with lineage wording throughout:
   "Winall-linked records **used** the unified channel" → "**entered through** the unified
   channel"; "when or where **Winall applied**" → "when or where these varieties **were
   submitted**"; "**Winall's own entrants**" → "**varieties in this lineage**". Retain "channel
   choice" only if the sentence makes clear the choice is the filing applicant's.
3. **§7 line 519 or a footnote** — report the decomposition in (b) and the conservativeness
   result in (c). Three sentences. It converts the section's biggest exposure into a robustness
   check the authors performed, which is strictly better than a referee performing it.
4. **§7 line 525** — add a third scope limit: the treated group is defined by germplasm lineage,
   includes filings by other organisations (some of them public research institutes), and shares
   applicants with the comparison group, so the contrast is a lineage contrast and not a
   firm-versus-rivals contrast.
5. **§7 line 517 and §1 line 51** — drop "its share of national approvals" as a possessive and
   the "single largest beneficiary" superlative (already required by **M4**), or restrict the
   series to the 2017–2022 analysis window.

---

## R-E findings

### R-E.1 — Mechanical numeric diff, v3 → v4 (PASS)

Extracted every numeric token (`[-−+]?\d+(,\d{3})*(\.\d+)?`, including scientific-notation
forms) from both files and diffed the multisets.

- **Tokens present in v3 but absent in v4: zero.**
- **Tokens whose value changed: zero.** No token was altered; only frequencies moved.
- **Tokens new in v4 (15), every one accounted for:**
  - `0.770` (×2), `1.000` (×1), `1,426` (×1) — the entity-resolution precision/recall and its
    validation set, §3.1 line 146 and §7 line 519. Justified in `change_log_v3_to_v4.md` §5.4
    and §10.1 as pre-existing project documentation written into the Methods, with no re-run.
    (See R-E.6 for the caveat that attaches to these three.)
  - `329`, `351`, `933`, `953`, `1360`, `1374`, `99`, `197`, `122874`, `670006`, `68` — page,
    volume and article numbers of the six references added in v4. Not results.
  - `8.5` — the §8.5 Limitations heading, renumbered from §8.4 to make room for §8.4
    "Implications for S&T intelligence practice".
- **Frequency-only changes (20 tokens)**, all section cross-references (`3.1`, `3.2`, `3.3`,
  `3.4`, `4.7`, `8.3`, `6`, `7`, `10`, `15`, `17`) or years (`2000`, `2016`, `2017`, `2020`,
  `2021`, `2022`, `2023`, `50`, `119`). No result frequency changed.

Stronger still, a line-level diff of the four result-bearing sections:

| Section | v3 → v4 |
|---|---|
| §4.7 What this paper does not claim | **byte-identical** |
| §5 Results (5.1–5.7) | **byte-identical** |
| §6 Robustness (6.1–6.7) | **byte-identical** |
| §7 Mechanism | one insertion only: "; identified by the pedigree-and-naming entity-resolution rule described in §3.1, whose 0.770 recall biases every comparison below toward zero" (line 519) |

The invariance claim in `change_log_v3_to_v4.md` §10.1 is **verified**.

### R-E.2 — Per-coefficient comparison against GROUND_TRUTH / source CSVs

Every value below was read from the CSVs, not from `GROUND_TRUTH.md`'s transcription, and
compared to the manuscript text at the cited line.

#### Arm 1 — Consortium vs Unified (`table3_main_results.csv`)

| Outcome | CSV β (exact) | Correct 3 d.p. | v4 text | v4 location | Match |
|---|---|---|---|---|---|
| head_rice_pct | −1.844094 | −1.844 | −1.844 | L9, L43, L358, L427, L461, L489 | ✅ |
| head_rice CI / p / n | [−2.63648, −1.05171], 5.082e−06, 742 | [−2.636, −1.052], 5.1×10⁻⁶ | [−2.636, −1.052], p = 5.1 × 10⁻⁶, n = 742 | L427 | ✅ |
| chalkiness_deg_pct | +1.108465 | +1.108 | +1.108 | L9, L43, L359, L427, L461, L489 | ✅ |
| chalkiness CI / p / n | [0.24760, 1.96933], 0.011613, 739 | [0.248, 1.969], 0.012 | [0.248, 1.969], p = 0.012, n = 739 | L427 | ✅ |
| quality_stated | −0.121893 | −0.122 | −0.122 (and "12.2 pp") | L9, L43, L359, L427, L461, L505 | ✅ |
| quality_stated CI / p / n | [−0.21124, −0.03254], 0.0074990, 750 | [−0.211, −0.033], 0.0075 | [−0.211, −0.033], p = 0.008 / 0.0075 | L427, L505 | ✅ |
| quality_top2 | −0.090933 | −0.091 | −9.1 pp, p = 0.009, n = 618 | L427 | ✅ |
| amylose_pct | −0.118365 | −0.118 (n.s.) | "no significant difference" | L427 | ✅ |
| gel_mm | −1.813892 | −1.814 | −1.814 mm, p = 0.015, n = 728 | L427 | ✅ |
| lw_ratio | +0.038870 | +0.039 (n.s.) | "no significant difference" | L427 | ✅ |
| neck_blast_ok | −0.034052 | −0.034, p = 0.277 | "no significant Arm 1 gap either (p = 0.28)" | L427 | ✅ |
| **blb_grade** | −0.190219 | −0.190 | −0.190, [−0.278, −0.102], p < 0.0001, n = 520 | L431, L461 | ✅ |
| **yield_gain_pct** | **+0.553445** | **+0.553** | **+0.554** | **L360, L429, L461, L489** | ❌ **DEFECT — see R-E.3** |
| yield_gain CI / p / n | [0.09125, 1.01564], 0.018929, 708 | [0.091, 1.016], 0.019 | [0.091, 1.016], p = 0.019, n = 708 | L429 | ✅ |
| gain_prod_pct | +0.918871 | +0.919 | +0.919, [0.505, 1.333], p < 0.0001, n = 578 | L320, L429, L461, L465 | ✅ |
| yield_2yr_kg_mu | +1.425271 | +1.425 | +1.43, p = 0.61, n = 716 | L429 | ✅ |
| duration_d | −0.083309 | −0.083 (n.s.) | not reported as a finding | — | ✅ |
| plant_height_cm | +0.952150 | +0.952 | +0.952 cm, p = 0.044 | L429, L473 | ✅ |
| seed_setting_pct | −0.202380 | −0.202 | −0.202, p = 0.43 | L429 | ✅ |
| tgw_g | +0.138316 | +0.138 | +0.138, p = 0.59 | L429 | ✅ |
| grains_per_panicle | −5.355257, q = 0.04738 | −5.355 | not reported in prose | — | ⚠️ see R-E.4 |

#### Arm 2 — Green channel vs Unified (`table3_main_results.csv`)

| Outcome | CSV β | v4 text | v4 location | Match |
|---|---|---|---|---|
| chalkiness_deg_pct | +2.808718, [1.87370, 3.74374], 3.92e−09, n = 110 | +2.809, [1.874, 3.744], p < 0.0001, n = 110 | L435 | ✅ |
| quality_stated | −0.343811, 1.325e−05, n = 112 | −0.344 (34.4 pp), p < 0.0001, n = 112 | L435 | ✅ |
| head_rice_pct | −0.390690, 0.55127, n = 106 | −0.391, p = 0.55, n = 106 | L435 | ✅ |
| gain_prod_pct | −1.036186, [−1.85983, −0.21255], 0.013673, n = 112 | −1.036, [−1.860, −0.213], p = 0.014, n = 112 | L320, L437, L465 | ✅ |
| yield_gain_pct | −0.994167, 0.16635, n = 21 | n = 21, β = −0.994, p = 0.17, flagged "not estimable" | L437 | ✅ |
| neck_blast_ok | `insufficient_variation` — no estimate | "not estimable … the field is 100% missing for all 119 Arm-2 records"; **no coefficient reported** | L427, L437 | ✅ no fabrication |
| SE type disclosure | Arm 1 cluster(cell, G = 10); Arm 2 HC1, 2 cells | stated at L164–168, L314, L423, L435 | — | ✅ |

#### Enterprise vs public-institution panel (`table7_enterprise_vs_public.csv`, Supplementary Table S1)

| Outcome | CSV θ (Public − Enterprise) | SE | p | n | v4 text (L523) | Match |
|---|---|---|---|---|---|---|
| yield_2yr_kg_mu | +4.179117 | 1.89314 | 0.027279 | 408 | +4.179, SE 1.893, p = 0.027, n = 408 | ✅ |
| tgw_g | +1.193025 | 0.40218 | 0.0030131 | 411 | +1.193 g, SE 0.402, p = 0.003, n = 411 | ✅ |
| chalkiness_deg_pct | +1.009876 | 0.61449 | 0.100294 | 411 | +1.010, SE 0.614, p = 0.100, n = 411 | ✅ |
| head_rice_pct | −1.219585 | 0.67337 | 0.070115 | 411 | −1.220, SE 0.673, p = 0.070, n = 411 | ✅ |
| Sign convention | θ = coefficient on `Public` | | | | "applicants labelled 'public research institute' show higher … than enterprise applicants" | ✅ matches `mechanism_winall.py` |
| n range | 408–411 | | | | "n = 408–411" | ✅ |

#### §7 Winall statistics (`table5_winall_positioning.csv`, `table5b_…logit.csv`, `table_r10_…csv`)

| Quantity | CSV | v4 text (L519, L521) | Match |
|---|---|---|---|
| Winall unified share | 0.6024096, n = 166 | 60.2%, n = 166 | ✅ |
| Others unified share | 0.4750227, n = 1,101 | 47.5%, n = 1,101 | ✅ |
| Logit α (year×group FE) | −0.7276184, SE 0.182442, p = 6.657e−05, OR 0.483058 | α = −0.728, SE = 0.182, p < 0.0001, OR 0.483 | ✅ |
| Logit, no-FE / two-group | −0.5155 / −0.5582 | "robust in magnitude and sign, though somewhat attenuated" | ✅ |
| Unified head_rice ρ | +2.2116452, p = 1.90e−04, n = 495 | +2.212 points, p < 0.001 | ✅ |
| Unified quality_stated ρ | +0.0977068, p = 4.17e−04, n = 501 | +9.8 points, p < 0.001 | ✅ |
| Unified chalkiness ρ | −0.6916010, p = 2.26e−04, n = 494 | −0.692 points, p < 0.001 | ✅ |
| New-channel subsample | −0.4517 (p = 0.548), +0.0452 (p = 0.184), +0.1995 (p = 0.655) | "all three coefficients lose significance (p > 0.18 throughout)… move toward zero or reverse sign" | ✅ |
| R10 head_rice | −1.3676255, p = 0.0056572, n = 602 | −1.368 pp, p = 0.006, n = 602 | ✅ |
| R10 chalkiness | +0.9399013, p = 0.0338128, n = 599 | +0.940 pp, p = 0.034, n = 599 | ✅ |
| R10 quality_stated | −0.1044896, p = 0.0105916, n = 609 | −0.104, p = 0.011, n = 609 | ✅ |

#### §5.5 year-by-year (`table_event_study_by_year.csv`) and §5.6 breakpoints (`table_breakpoint_scan_full.csv`)

| Quantity | CSV | v4 text | Match |
|---|---|---|---|
| Chalkiness 2017/19/20/21/22 | +2.7108 / +1.6267 / +0.9158 / +0.8906 / +0.7714 | +2.71 / +1.63 / +0.92 / +0.89 / +0.77 | ✅ |
| Chalkiness p 2019–2022 | 0.00395 / 0.00427 / 0.00198 / 0.03766 | 0.004 / 0.004 / 0.002 / 0.038 | ✅ |
| quality_stated 2017 → 2022 | −0.3266 → −0.0520; 2020 p = 0.333, 2022 p = 0.293 | −0.327 → −0.052, "2020 and 2022 not significant" | ✅ |
| head_rice 2017/20/21/22 | −0.6142 (p = 0.38) / −2.6335 (p = 0.00033) / −1.4845 (p = 0.0213) / −3.0326 (p = 0.0056) | −0.61 (n.s.) / −2.63 (p = 0.0003) / −1.48 (p = 0.021) / −3.03 (p = 0.006) | ✅ |
| yield_gain by year | −0.6307 / +0.6977 / +0.7315 / +0.3247 / +0.9307 | "fluctuates around +0.3 to +0.9 pp" | ⚠️ omits the −0.63 in 2017 — see Suggested |
| Break: yield_2yr | τ = 2017, Wald 230.29, p = 9.8e−51, n = 1,167 | 2017, Wald = 230.3, p < 10⁻⁵⁰, n = 1,167 | ✅ |
| Break: head_rice | τ = 2015, Wald 73.95, p = 8.8e−17, n = 1,186 | 2015, Wald = 73.9, p < 10⁻¹⁶, n = 1,186 | ✅ |
| Break: chalkiness | τ = 2009, Wald 22.88, p = 1.08e−05, n = 1,187 | 2009, Wald = 22.9, p = 1.1 × 10⁻⁵, n = 1,187 | ✅ |
| Break: quality_top2 | τ = 2015, Wald 45.53, p = 1.3e−10, n = 845 | 2015, Wald = 45.5, p = 1.3 × 10⁻¹⁰, n = 845 | ✅ |
| Break: yield_gain | τ = 2018, Wald 6.55, p = 0.0378 | Wald = 6.55, p = 0.038, HC1; classical 5.40, p = 0.067 | ✅ |
| Break: duration_d | τ = 2018, Wald 226.77, p = 5.7e−50, n = 1,196 | 2018, Wald = 226.8, p < 10⁻⁴⁹, n = 1,196 | ✅ |

**Tally: 58 quantities checked, 56 exact matches, 1 rounding defect (yield_gain_pct, 4
occurrences), 1 derived-count defect (R5's "8").**

### R-E.3 — MUST FIX: `+0.554` should be `+0.553`, and the manuscript contradicts its own Table 3

`table3_main_results.csv` gives `yield_gain_pct` β = **0.5534452042714533**, which rounds to
**0.553** at the three-decimal precision the manuscript uses for every other Arm-1 coefficient.
v4 carries **+0.554** at four locations:

- **L360 (§4.5)**: "while $\beta^{self}$ is **+0.554** for regional-trial yield gain (p = 0.020)"
- **L429 (§5.2)**: "The two-year regional-trial yield gain over the named check is **0.554** pp
  *higher* for Consortium entrants (95% CI [0.091, 1.016], p = 0.019, n = 708)"
- **L461 (§6 intro)**: "regional-trial yield gain **+0.554** pp"
- **L489 (§6.4, R11)**: "MDE = 5.62 pp against **+0.554** pp nationally"

`manuscript_v3.md` carries the same value at the parallel lines 315, 384, 416, 444, so this is
**inherited, not a v4 regression**. It is nevertheless wrong, and it is worse than a lone
rounding slip for two reasons:

1. **The submission package already prints the correct value.** `submission/tables.md` line 108
   (Table 3, Arm 1): "| Regional-trial yield gain over check (pp) | self-reported | 708 |
   **+0.553** | 0.236 | [0.091, 1.016] | 0.0189 | 0.0402 |". The manuscript body and the
   submitted table therefore **disagree with each other**, four times. A referee comparing text
   to table will find this immediately.
2. **The project's own reconciliation table certifies the mismatch as exact.**
   `manuscript/results_notes_main.md` line 29 reads "| yield_gain_pct | β=+0.554, p=0.020 |
   β=+0.5534, p=0.0189, n=708 | **exact** |". The verification step that should have caught this
   instead signed it off. The `+0.554` originates in the planning documents
   (`plan/02_research_route.md` lines 109/133/154, `plan/06_v4_review_brief.md` line 45) and in
   the analysis scripts' hard-coded expectation values
   (`scripts/analysis/estimate_channel_gap.py` line 199, `scripts/analysis/robustness_supplement.py`
   line 24), so a fix that touches only the manuscript will leave the same wrong digit in the
   scripts that "verify" it.

**Fix:** change all four manuscript occurrences to `+0.553`; correct
`results_notes_main.md` line 29 and the two script constants; correct
`plan/06_v4_review_brief.md` line 45 so a later reviewer is not sent back down the same path.
Abstract line 9's "+0.55 points" is correct at its precision and needs no change.

### R-E.4 — MUST FIX (minor): R5 reports 8 BH-surviving outcomes; the CSV gives 9

`manuscript_v4.md` line 469 (§6.1, R5):

> "**R5 (Benjamini–Hochberg FDR).** Of 17 Arm-1 outcomes, **8 retain q < 0.05** after BH
> correction across all 17 tests, including all six headline coefficients; only the top-two
> quality-grade indicator is borderline (see R7)."

Counting `bh_q < 0.05` over the 17 Arm-1 rows of `table3_main_results.csv` gives **9**:

| # | Outcome | BH-q |
|---|---|---|
| 1 | head_rice_pct | 0.000086 |
| 2 | gain_prod_pct | 0.000114 |
| 3 | blb_grade | 0.000122 |
| 4 | quality_stated | 0.029298 |
| 5 | quality_top2 | 0.029298 |
| 6 | chalkiness_deg_pct | 0.032904 |
| 7 | gel_mm | 0.037318 |
| 8 | yield_gain_pct | 0.040223 |
| 9 | **grains_per_panicle** | **0.047376** |

(next: plant_height_cm at 0.075222, which correctly fails)

`grains_per_panicle` (β = −5.355, p = 0.025, q = 0.047) is the omitted ninth —
`GROUND_TRUTH.md` lines 31–32 flag it explicitly as nominally significant with BH-q = 0.047.
Identical in v3, so again inherited rather than introduced. **Fix:** change "8" to "9" at line
469; if the authors prefer not to surface `grains_per_panicle`, the honest wording is "9 of 17
retain q < 0.05 (the ninth being grains per panicle, an agronomic trait not part of this paper's
argument)". Suppressing it while reporting a count is not an option — the submitted Table 3
(`submission/tables.md` line 111) already prints its q = 0.0474.

Secondary wording point at the same line: "only the top-two quality-grade indicator is borderline
(see R7)" is confusing in a BH sentence, since `quality_top2`'s q = 0.0293 is not the closest to
the threshold (`yield_gain_pct` at 0.0402 is). The "(see R7)" makes clear the reference is to the
Manski bound rather than to BH, but the sentence should say so.

### R-E.5 — Superseded planning values (PASS)

| Forbidden value | Occurrences in v4 | Verdict |
|---|---|---|
| `+3.18` | **0** | ✅ |
| `+0.96` / `0.96` | **0** | ✅ |
| `n = 632` | **2**, both inside the single flagged-open-item sentence at L523 | ✅ acceptable per brief |

L523, in full, is the only place `632` appears:

> "We flag one open item rather than resolving it silently: an earlier planning-stage note for
> this comparison anticipated a sample of **n = 632** records, whereas the regression actually
> run on `analysis_rice_channel.pkl` for Supplementary Table S1 (Table 7 in the pre-submission
> working draft) returns n = 408–411 depending on outcome; we were unable to reconstruct the
> exact filter or sample-construction choice behind the **n = 632** figure from the materials
> available, and record this as an item for the author team to verify against the original
> coding before submission, rather than adjusting the reported n to match the earlier planning
> note."

Both instances are inside the disclosure, neither is presented as a result. The parallel
disclosure in `submission/supplementary_material.md` lines 33–35 is consistent. Identical to v3
(L478). **No regression.**

### R-E.6 — CF1–CF8, R1–R16, Non-claims 1–12: enumerated and confirmed

**Conflicting-evidence register (source: `plan/01_theme_and_innovation.md` §9).**

| # | Item | v4 location | Status |
|---|---|---|---|
| CF1 | Bacterial-blight grade **better** (more resistant) in self-organised entrants | §5.2 L431 (Arm 1: −0.190, [−0.278, −0.102], p < 0.0001, n = 520); §4.7 Non-claim 4 L407; §9 L567 | ✅ present, prominent; ⚠️ Arm-2 value −0.562 (p = 0.074, n = 82) still appears only in Table 3, not in prose — **pre-existing, identical in v2/v3, already logged in `review/format_check.md` item 16** |
| CF2 | Arm 2 production-trial yield gain reverses sign | §4.3 L320; §5.3 L437 (−1.036, [−1.860, −0.213], p = 0.014, n = 112); §5.7 L455; R1 L465 | ✅ intact |
| CF3 | Arm 2 regional-trial yield gain not estimable | §3.3 L213–216; §5.3 L437 (1 of 52, 1.9%; n = 21 reported but flagged uninterpretable) | ✅ intact |
| CF4 | Top-two quality grade fails Manski bounds | §5.2 L427; §6.2 L479 ([−0.253, +0.088], crosses zero, explicitly downgraded) | ✅ intact |
| CF5 | Within-applicant estimates mostly flip sign | §6.3 L483 (+0.780 / +0.846 / +0.118 / +0.100 / −0.126 / −0.421, all n.s.); §4.7 Non-claim 1 L404 | ✅ intact (value is the re-run +0.780, not the planning-stage +3.68; that substitution predates v3 and is logged in `number_consistency.md`) |
| CF6 | Provincial replication non-significant | §6.4 L489–493; §8.2 L539; §4.7 Non-claim 8 L411 — including the disclosed n = 495 vs 452 and −0.134 planning discrepancy | ✅ intact |
| CF7 | Plant-height placebo is significant, moved out of the placebo set | §5.2 L429 (+0.952 cm, p = 0.044); §6.1 R12 L473 | ✅ intact |
| CF8 | `quality_stated` is mathematically a missingness indicator | §3.3 L194–202; §6.6 R16 L505 (−0.122 → −0.146 with controls; the −0.169 planning figure disclosed as not reproduced) | ✅ intact |

**Robustness checks R1–R16 — all 16 present.**

| Check | v4 location | One-line content |
|---|---|---|
| R1 | §6.1 L465 | Two channels never pooled (+0.919 vs −1.036) |
| R2 | §6.1 L466 | Additive vs interaction fixed effects |
| R3 | §6.1 L467 | Extend to all national trial groups |
| R4 | §6.1 L468 | 2018 coding immaterial (233 records) |
| R5 | §6.1 L469 | Benjamini–Hochberg FDR — **count error, R-E.4** |
| R6 | §6.1 L470 | Randomisation inference, 500 draws, RI p = 0.002 |
| R7 | §6.2 L479 | Manski worst-case bounds |
| R8 | §6.1 L471 | Missingness balance, Supplementary Fig. S1 |
| R9 | §6.3 L483–485 | Within-applicant subsample + MDE |
| R10 | §6.1 L472 | Drop the focal firm |
| R11 | §6.4 L489–493 | Provincial replication + MDE |
| R12 | §6.1 L473 | Pre-declared placebos |
| R13 | §6.1 L474 | Pre-reform time placebo (n = 153, 13 cells) |
| R14 | §6.1 L475 | Cluster by variety (36 varieties, 72 records) |
| R15 | §6.5 L497–501 | Chained-check genetic-gain scale |
| R16 | §6.6 L505 | `quality_stated` under disclosure controls |

Section-6 text is byte-identical to v3, so nothing was softened. The reporting hierarchy is
preserved: the four qualifying/failing checks (R7, R9, R11, R15) still get full prose
treatment while the passing ones are summarised (§6 intro L461).

**Non-claims 1–12 — all 12 present, byte-identical to v3, §4.7 lines 404–415.**

| # | Line | Claim disclaimed |
|---|---|---|
| 1 | 404 | β is not a causal effect; within-applicant design underpowered 2–3× |
| 2 | 405 | No language of fabrication or manipulation |
| 3 | 406 | The 2016 reform is not claimed to have caused the gap or any decline |
| 4 | 407 | Third-party traits are not uniformly worse (bacterial blight) |
| 5 | 408 | The self-reported yield advantage is not an established finding |
| 6 | 409 | No welfare claim |
| 7 | 410 | Approval counts never used as an outcome |
| 8 | 411 | No claim of provincial replication |
| 9 | 412 | No claim that enterprises breed better or worse than public institutions |
| 10 | 413 | No evaluation of any applicant firm's financial performance, business strategy or corporate governance |
| 11 | 414 | No claim about varietal homogenization |
| 12 | 415 | The parsed compilation is not treated as an official complete registry |

Non-claim 10 is the v3 rewrite (neutral scope statement, not a substituted favourable
characterisation) and has survived v4 unchanged — correct as far as it goes, but see R-B.4 for
why its *financial-only* scope is now the wrong scope.

**One note on the three new numbers.** `0.770`, `1.000` and `1,426` (§3.1 L146, §7 L519) are
the only numeric additions in v4 that are results rather than bibliography, and
`change_log_v3_to_v4.md` §12 concedes they were carried from planning documents without
re-execution ("本次未重跑验证脚本"). The coordinating session has since re-run the validation
(`VERIFY_entity_rule.md`) and **all three reproduce exactly** — labelled subset n = 1,426,
TP = 107, FP = 0 → precision 1.0000, FN = 32 → recall 0.7698. I re-derived the labelled subset
independently and confirm n = 1,426 under `applicant_type != 'Unknown'` (2,386 − 960). **These
figures are verified; do not treat them as unsupported.** What they need is not re-computation
but the disclosure described in **R-B.7** — the filter definition, the fact that the validation
target shares the pedigree field with the rule under test, and the treated-group composition.

### R-E.7 — Over-claiming on the two non-significant panel coefficients (partially upheld)

The brief asks whether §7's prose loads more weight onto chalkiness (p = 0.100) and head-rice
(p = 0.070) than two non-significant coefficients can bear. My reading: **mostly no, with one
specific over-reach and one internal contradiction.**

What the paper does right:

- It prints both p-values inline and unrounded — "p = 0.100" and "p = 0.070" (L523). It does not
  hide them behind asterisks or a "p < 0.10" band.
- It uses the word "**directionally**" for chalkiness rather than "significantly".
- It never describes the panel as showing a significant third-party quality deficit, which is the
  specific prohibition in `GROUND_TRUTH.md` lines 78–80. ✅
- Non-claim 9 (L412) and the paragraph's own opener ("As descriptive background — not as a
  conclusion about which type of institution breeds better rice") both fence it.
- Structurally, the load-bearing rebuttal of "enterprises are careless" is **S6** — the channel-
  choice logit, α = −0.728, p < 0.0001 — not S11. The panel is a supplementary corroboration.

The over-reach, at L523:

> "**This division of labour runs in the opposite direction from what an 'enterprises are
> careless' account would predict for chalkiness and head-rice**, and is silent on causation in
> either direction; it is reported here only as a background fact, not evidence for or against
> either institution type."

Two problems in one sentence.

1. **"This division of labour"** presupposes an established pattern. A division of labour is a
   *finding*; two coefficients at p = 0.100 and p = 0.070 are two coefficients at p = 0.100 and
   p = 0.070. The noun phrase does argumentative work the estimates do not support. Recommended:
   "The point estimates on chalkiness and head-rice run in the opposite direction from …, though
   neither is significant at 5%."
2. **The sentence contradicts itself.** It first says the result "runs in the opposite direction
   from what an 'enterprises are careless' account would predict" — that is, it *is* evidence
   against that account — and then says it is "not evidence for or against either institution
   type." The paper is claiming the rhetorical benefit of the rebuttal while formally disclaiming
   the inference. An adversarial referee will quote both halves. Pick one: either state that the
   estimates are too imprecise to bear on the question and drop the rebuttal framing, or state
   that they weakly disfavour the "careless enterprises" account and own the weakness explicitly
   ("neither coefficient reaches 5% significance, so this is at most a weak absence of support
   for the alternative, not a refutation of it").

Also worth adding at L523: nothing in the paragraph says the two significant coefficients in
the panel (regional-trial yield +4.179, TGW +1.193) are the **applicant-measured** ones, while
the two third-party-assayed ones are the non-significant ones. That is a striking pattern given
this paper's whole thesis, and stating it costs one clause and strengthens the section's
honesty.

---

## Must-fix

| # | Finding | Location | Line |
|---|---|---|---|
| **M1** | `+0.554` → `+0.553` (CSV = 0.5534). Four occurrences in the manuscript, which contradict the correct `+0.553` already printed in the submitted Table 3. Also correct `results_notes_main.md` L29 (which wrongly certifies the pair "exact"), `scripts/analysis/estimate_channel_gap.py` L199, `scripts/analysis/robustness_supplement.py` L24, and `plan/06_v4_review_brief.md` L45. | §4.5, §5.2, §6 intro, §6.4 | 360, 429, 461, 489 |
| **M2** | R5's "8 retain q < 0.05" → **9**; `grains_per_panicle` (q = 0.047376) is omitted, and its q already appears in the submitted Table 3. | §6.1, R5 | 469 |
| **M3** | "Winall's edge is specific to the channel in which quality is measured by the same third party as everyone else" contradicts §2 L67 and §3.3 L185–188, which state third-party quality measurement is uniform across channels. Rewrite as a statement about the comparison set. | §7 | 519 |
| **M4** | §7 is uniformly favourable about a named listed company (6 favourable statements, 0 counterweights; the only named commercial actor in the paper). De-brand the superlatives, neutralise or relocate the within-unified positioning result, and extend Non-claim 10 beyond *financial* evaluation to cover breeding capability, product quality and market standing. | §1, §7, §9, §4.7 NC10 | 51, 517, 519, 565, 413 |
| **M5** | Financial residue in journal-facing submission files: `submission/figure_captions.md` L55 still names "the 2025 net-loss and 2026 ST status change"; L10, `submission/supplementary_material.md` L13–15 and `submission/tables.md` L11 narrate the removal and disclose that it was "at the author team's request". Strip all removal-provenance notes from files the editor reads; keep the history in the internal change logs only. | submission package | see cells |
| **M6** | Relocate the Xie et al. (2023) sentence out of the gap between S4 and the "It is not." payoff — it is an orphaned citation (its v2 job was to source the deleted table) sitting across the section's key transition. | §7 | 517 |
| **M7** | §7 describes a germplasm-lineage indicator in corporate-agency language ("its share of national approvals", "where Winall applied", "Winall's own entrants", "its varieties"). In §7's own n = 166, only 54 records (32.5%) name the firm or a 荃银 affiliate as applicant; 37 (22.3%) are other organisations' filings, including public research institutes; 17 applicants appear in both treated and comparison groups. Rewrite §7 in lineage terms and add the third scope limit. | §1, §7 | 51, 517, 519, 525 |
| **M8** | Add the §3.1 disclosure paragraph: the `applicant_type != 'Unknown'` filter; the precision-1.000 target shares the pedigree field with the rule under test; ~two-thirds of firm-linked records carry a third-party or missing applicant, which is intended under the lineage construct; and the treated-group composition, since the conservative-bias argument currently covers only false negatives. Report the decomposition and the conservativeness check from R-B.7(b)–(c) — the applicant-confirmed subset is at 66.7% unified vs 60.2% pooled vs 47.5% comparison, so the pooled estimate is conservative. | §3.1, §7 | 146, 519 |

## Suggested

| # | Finding | Location | Line |
|---|---|---|---|
| S1 | L523: "This division of labour runs in the opposite direction…" over-reads two coefficients at p = 0.100 and p = 0.070, and contradicts the same sentence's "not evidence for or against either institution type." Rewrite to name the imprecision, and add the observation that the two significant coefficients in the panel are the applicant-measured ones. | §7 | 523 |
| S2 | §5.5's "regional-trial yield-gain coefficient fluctuates around +0.3 to +0.9 pp" omits the 2017 value of −0.63 in the same series. Say "−0.63 in 2017 (n = 27, n.s.) and +0.32 to +0.93 thereafter". | §5.5 | 445 |
| S3 | Name the case-selection issue in §7's scope limits: the counter-case is selected on success, so it tests whether the *most successful* enterprise is careless, not whether enterprises are. | §7 | 525 |
| S4 | Retitle §7 from "Mechanism: …" to "A counter-case: …" — L525 explicitly disclaims a causal mechanism. | §7 | 513 |
| S5 | R5's "only the top-two quality-grade indicator is borderline (see R7)" reads as a BH statement but refers to the Manski bound; say so. | §6.1 | 469 |
| S6 | The "23–31% in 2022–2024" approval-share range: 2022 comes out at 21.3% on my recomputation (two indica trial groups, lineage flag), and two of the three cited years lie outside the 2017–2022 analysis window in a period where the corpus captures ~21% and ~15% of announcements (§3.1 L112). Confirm the stratum, or restrict the series to 2017–2022. | §7 | 517 |
| S7 | CF1's Arm-2 bacterial-blight coefficient (−0.562, p = 0.074, n = 82) appears only in Table 3, not in prose — a pre-existing gap already noted in `review/format_check.md` item 16. One sentence in §5.3 closes it. | §5.3 | 437 |

---

## Recommendation

**Minor revision.** On R-E I return a **pass**: the invariance claim is not just asserted but
demonstrable — §4.7, §5 and §6 are byte-identical across v3 → v4, §7 differs by one clause, and
the numeric multiset is unchanged except for bibliography and two documented methodological
additions. Of 58 quantities traced to source CSVs, 56 match exactly. The two that do not (M1,
M2) are inherited transcription/counting errors, not products of the reframing, and both are
one-character fixes — but M1 must be fixed because the manuscript body currently contradicts its
own submitted Table 3 four times, and because the project's own verification note certifies the
mismatch as "exact", meaning the error will survive any re-check that trusts that note.

On R-B I return a **qualified pass on logic, a fail on ethics and on construct description**.
The counter-case argument holds end to end and lost no premise to the excision — I traced all
twelve steps and confirmed the deleted paragraph was self-declared as orthogonal to the
identification argument. But v3's stated defence against one-sidedness ("cut the positive
material too") balanced only the *financial* register, while the praise that actually matters is
non-financial, was never in scope for the cut, and now stands entirely uncountered in a section
about the paper's only named commercial actor. Combined with the financial facts still legible
in the submission package's own figure caption (M5) and the bare "The authors declare no
conflict of interest", this is the finding most likely to cost the paper an editorial screen.

Independently of the excisions, **M7/M8**: §7 argues in the corporate-applicant register over an
indicator that is, by the paper's own definition, a germplasm-lineage construct — and only about
a third of the treated records are confirmed as the firm's own filings. The result survives
(indeed the pooled estimate is conservative: 66.7% unified among applicant-confirmed records
versus 60.2% pooled and 47.5% comparison), so this costs the paper nothing substantive, but it
must be disclosed rather than discovered. Conveniently, the fix — rewriting §7 in lineage terms
— also does much of the de-branding that M4 requires, since lineage language cannot attribute
market success or product quality to a corporate entity.

M3–M8 fix all of this without touching a single estimate. No v5 is required on these two lines: a
targeted revision of §7 plus the §3.1 disclosure paragraph, five numeric/package edits, and the
submission-file cleanup is sufficient. The revision should be re-checked against the §7 rewrite,
the new §3.1 paragraph, and the four `0.554` sites; the rest of the numeric surface is verified
and stable.
