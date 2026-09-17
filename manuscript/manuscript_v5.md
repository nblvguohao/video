# Who measures what enters the market? Trial channel and third-party-assayed grain quality in China's rice variety approvals, 2017–2022

*Running title:* Trial channel and third-party grain quality in Chinese rice approvals

**Authors:** [Author(s) to complete — given name and surname, in submission order]

**Affiliations:** [Author(s) to complete. Note: the first author's affiliation must be the
S&T information/intelligence institute, listed first, to satisfy the first-affiliation
requirement.]

**Corresponding author:** [name, postal address, e-mail, ORCID]

---

## Abstract

**Background** Official rice variety-approval announcements record who tested a variety and what a third party measured, but the trial channel has never been extracted as an analysable field. China's 2016 approval reform let seed firms and breeder consortia run their own trials, but no prior study observes the channel, so none can tell whether what enters the market changed. **Objective** We mine these announcements into a record-level indicator system (2,386 records, 17 fields), extract each variety's trial channel, and test whether self-organised and unified-trial entrants differ in what they bring to market. **Methods** We compare self-organised with unified-trial entrants within the same year, trial group and named check, estimating the green channel (2017) and consortium trials (2019–2022) separately since they barely overlap. **Results** Consortium entrants show 1.84 points lower head-rice percentage, 1.11 points higher chalkiness, and a 12.2-point lower probability of a stated national quality grade, all third-party-assayed, while the applicant's own yield advantage is, if anything, higher (+0.55 points, suggestive only); green-channel entrants likewise show higher chalkiness. This sign separation is the identification argument: breeding ability predicts both trait classes deteriorate together, whereas only third-party quality does. Results survive worst-case bounds, randomisation inference, and dropping the most prevalent breeding lineage; bacterial-blight grades are better among self-organised entrants, bounding the composition effect. **Conclusion** Verification since 2022 appears to reach chalkiness but not head-rice, pointing to where oversight should target next; more broadly, evidence strength differs by who measured each field, so approval indicators should be read field by field.

---

## Keywords

rice variety approval; grain quality; trial channel; seed regulation; administrative text mining; China

---

## Highlights

1. Rice variety-approval announcements are mined into record-level indicators.
2. Trial channel is reconstructed from approval-announcement text at record level.
3. Consortium-trial entrants show lower third-party-assayed grain quality.
4. Applicant-measured yield performance is not lower for self-organised entrants.
5. In one rice approval record, evidence strength depends on who measured the field.

---

# 1. Introduction

Variety approval decides which rice varieties may be sold as certified seed in China. Until 2016 the state held a monopoly on the trials that produced this decision; the 2016 revision of the *Measures for the Administration of Crop Variety Approval* ended it, letting certified integrated seed-breeding-extension enterprises run their own "green-channel" trials and consortia of five or more breeders organise their own regional trials. Both channels replace the government as the party that runs the trial in which agronomic performance is measured; neither replaces the ministry-designated third-party laboratories that measure grain-processing and appearance quality once a candidate reaches the approval stage. This split — self-organised measurement of performance, third-party measurement of quality, inside the same approval file — is the object of this paper. We ask not how large the reform was, but *who measures what enters the market*.

Observing that split requires a field nobody has extracted. Approval announcements have been read at scale before, but always as year-indexed trait series, since they are running prose yielding only whatever parsing a given study needs. Innovation measurement more broadly rests on a few curated indicator families, and its text-mining methods were developed over patent and publication corpora (Losiewicz et al., 2000; Antons et al., 2020) rather than over the regulatory record (Rammer and Es-Sadki, 2023). A single variety-approval record carries the applicant, the trial the variety was tested in, the named check it was compared against, and more than a dozen measured agronomic, grain-quality and resistance fields — each, crucially for what follows, with an identifiable measuring party. Our first contribution is to parse that structure into a record-level indicator system carrying the trial channel, and our second is to show what it reveals once the fields are separated by who measured them.

This question has not been answered because it has not been asked in a form the data could answer. Two studies evaluate this same reform as a *period* variable — before versus after 2016 — applied to licensing-fee data (Xiang et al., 2025, who find no significant effect) and to national approval panels (Zhao et al., 2022); neither observes which trial a variety actually passed through, so neither can distinguish a change in *how much* enters the market from a change in *what* enters it. A related literature reads approved-variety trait trends by *calendar year* rather than by channel: Lu et al. (2024) classify quality-trait trajectories for 17,785 approved varieties, and Hang et al. (2024) track agronomic-trait evolution across 11,811 regional-trial entries; both attribute trait change to *when* a variety was approved rather than to *which door* it entered through. This paper's structural-break analysis (§5.5) and "closing window" discussion (§8.2) ask the channel-conditional version of the same question a year-indexed reading cannot. A recent title-level review of fifty years of three-line hybrid rice trends (Gong et al., 2026) situates this trait trajectory over a longer horizon; its full text was not accessible to us, so we cite it only for scope. No existing study has a record-level channel variable to test whether self-organised and state-run entrants differ in what they bring to market — this is the gap we close.

We close it using a feature of the announcements that has not previously been exploited: each states, in its own text, the name of the trial the variety was tested in. Parsing this text lets us assign every record to a channel and compare self-organised with unified-trial entrants within the same approval year, ecological trial group, and named check. Because the green channel is concentrated in 2017 and consortium trials begin only in 2019, the two barely overlap in time; we treat them as separate treatments rather than pooling them into one "new channel."

The paper's estimand is a **composition effect on the entering population**: conditional on year, trial group and check, how do the traits of varieties entering through a self-organised channel differ from those entering through the unified trial. This is not the effect of moving one variety between channels, since assignment is not random and applicants self-select into it; it is the difference in what each door lets through. We do not estimate, and do not claim, a causal effect of the reform on trait levels or on grain quality — the identification strategy concerns the *entering population*, not the *time trend*.

This paper makes three contributions. **First**, an S&T-intelligence extraction pipeline over an unstructured administrative corpus yields the first record-level trial-channel variable for China's approval system — read from announcement wording rather than imposed as a before/after indicator — and a 17-field indicator set labelled by measuring party. **Second**, the coexistence of applicant-measured and third-party-measured traits within one approval file becomes an identification argument, distinct from the randomised self-certification literature's two measurements of the same attribute (Duflo et al., 2013; Bar and Zheng, 2019): here we have two *different* attributes measured by two different parties in a single document. Grain-processing and appearance quality are measured by third-party laboratories uniformly across channels; agronomic performance is measured by the applicant's own trial when self-organised. A pure breeding-ability difference predicts both move together; we instead find a sign separation — third-party quality lower, applicant-measured performance unchanged or higher (§4.5, §5) — that such an account cannot generate on its own, though it cannot alone rule out a difference in channel-specific admission thresholds. **Third**, splitting the reform into two non-overlapping treatments shows pooling them would misstate the gap's direction, since the green channel (2017) and consortium trials (2019–2022) differ in sign on at least one trait. A second indicator — germplasm concentration across parental lines from the same announcements — serves as a counter-case: consortium entrants draw on a significantly broader sterile-line base than the unified entrants they are compared against, so a narrower breeding base cannot explain their deficit. No analysis in the paper is conducted at the level of a named organisation.

Section 2 covers institutional background; Section 3 the extraction pipeline; Section 4 the empirical strategy and its limits; Sections 5–6 results and robustness; Section 7 the germplasm counter-case; Section 8 S&T intelligence and policy implications; Section 9 concludes.

---

# 2. Institutional background

China's variety approval system evaluates candidate crop varieties before they may be marketed as certified seed. Until 2016 the evaluation trial was uniformly state-run: a candidate enters the **unified regional trial** (统一区域试验), a multi-site, multi-year trial organised by the provincial or national approval committee, grown alongside a named check under a common protocol. This remained the only route until a **green channel** (绿色通道) opened in 2014, letting certified integrated seed-breeding-production-extension enterprises run their own trials; in our data it appears concentrated in 2017.

The 2016 revision of the *Measures for the Administration of Crop Variety Approval* (Order No. 4, effective 15 August 2016) extended self-organised testing by creating the **consortium trial** (联合体区域试验), run by a consortium of five or more breeders rather than the state system. Consortium-trial records first appear in 2019 and dominate the self-organised channel from 2019 through 2022; the green channel and consortium trials barely overlap in time.

Regardless of channel, grain-processing and appearance quality are assessed under a separate, uniform regime: laboratories designated by the Ministry of Agriculture and Rural Affairs apply a published standard — **NY/T 593** (《食用稻品种品质》) for most of the window, or **GB/T 17891** (《优质稻谷》), which predominates in 2017 — grading head-rice percentage, chalkiness and the national or industry quality grade. The channel therefore determines who measures agronomic performance, but not who measures grain-processing and appearance quality.

Two further changes fall at the edge of our window. In 2021, approval standards for rice and maize were revised upward on yield, quality and resistance thresholds, and approval volumes fell markedly afterward (evidence from industry-media reporting, flagged as lower confidence). On 1 March 2022 the revised Seed Law took effect, establishing an essentially-derived-variety (EDV) system requiring the original right-holder's consent for commercial exploitation of a derived variety. On 31 August 2022 the Ministry issued a notice launching a special-rectification campaign targeting green-channel and consortium-trial practices, at the end of our sample window; we treat it only as the point after which identifying variation becomes harder to observe.

These five events — the 2014 green channel, the 2016 Measures, the 2021 revision, the 2022 EDV provision and the 2022 rectification notice — are reported strictly as a timeline motivating the sample window and two-arm structure. We draw no inference about regulatory intent from their sequence, and attribute no trait trend to a specific event unless a structural-break test (§5.5) supports it.

---

# 3. Data and the intelligence-extraction pipeline

Because the corpus is an unstructured administrative text collection, this section doubles
as a methods section for the extraction itself, set out as a six-step S&T intelligence
pipeline (summarised schematically in Supplementary Fig. S4): (i) **intelligence-source
identification** — recognising approval announcements as
a high-density innovation corpus and the trial-channel statement as extractable (§3.1);
(ii) **corpus acquisition**, documenting its two-step provenance (§3.1); (iii) **field
extraction**, a regex rule set converting prose into typed fields (§3.1); (iv) **entity
recognition and disambiguation**, resolving the variety-source field into parental-line
entities with a resolution rate and per-channel coverage check (§3.1); (v) **field-coverage
and data-quality assessment**, per-field parse rates, missingness, structural gaps, and the
outstanding cross-check against primary announcements (§3.3–3.4); and (vi) **indicator
construction**, assembling parsed fields into 17 analysis variables labelled by measuring
party, over the strata compared (§3.2–3.3). Steps (i)–(iv) are what reproducing the corpus
needs; step (v) is what judging any individual field's trustworthiness needs, reported at
field level rather than as one corpus-wide statement, for reasons the main result makes
concrete.

## 3.1 Intelligence source, corpus acquisition, field extraction and entity resolution (steps i–iv)

The record-level unit of analysis is a *variety × ecological trial group* approval entry.
The underlying corpus is a parsed compilation of China's national and provincial rice
variety approval announcements (6,734 deduplicated records: 2,386 national, 4,347
provincial, 1999–2025), issued by the Ministry of Agriculture and Rural Affairs (MARA) and,
for provincial approvals, by provincial committees. We did not access MARA's own archive
directly; the text corpus was obtained through a public third-party aggregation,
`he-zhui/Rice_QA` (GitHub), re-parsed with our own regular-expression rules. The data are
therefore *MARA announcements, obtained through a public third-party compilation and parsed
by the authors*, not a first-hand MARA product and not a full census (coverage declines
sharply after 2022: 85/409 announcements for 2023, 61/405 for 2024, 2 for 2025 — §3.4). For
this reason approval counts are never used as an outcome variable, only descriptively.

Every element of our identification strategy depends on one feature no prior study has
used: each announcement states, in its "yield performance" or "characteristics" paragraph,
which trial the variety was tested in. We construct a record-level `channel` variable by
regular-expression matching: "绿色通道" or "自主试验" → Green; "联合体" → Consortium; all
else → Unified. `new_channel` collapses Green and Consortium for descriptive use only (§4
explains why they are estimated as separate arms). Trial group, named check and approval
year are parsed from the same paragraph and the approval-number field, succeeding for 100%
of national records; the channel label itself is unrecoverable for 233 of 234 national
records approved in 2018 (99.6%), treated as a documentation-format gap rather than evidence
that self-organised trials did not exist that year (Fig. 1, Table 1; R4 in §6 shows this
coding choice is immaterial).

Step (iv), entity recognition and disambiguation, resolves the free-text variety-source
field into the two parental lines of the originating cross — sterile (female) line, a
separator varying across several typographic conventions, then the restorer (male) line,
often continuing into the parents' own ancestry. We take only the first cross and normalise
separators and quotation marks. The rule resolves 2,304 of 2,386 national records (96.6%);
the 3.4% that fail are multi-parent pedigrees with no single immediate cross, mutagenesis- or
selection-derived varieties recording no cross at all, and a residue using symbols the rule
does not cover — all excluded from the concentration indicator rather than imputed.

Reporting the failure rate is not a formality. An earlier version of this rule handled only
common typographic conventions, and its failures were **channel-correlated** —
green-channel records failed at 8.0% against the unified channel's 2.3% — which would have
biased the Arm-2 comparison in §7 without any visible symptom. Under the current rule,
coverage is 99.7–100% in all four channel-by-arm groups (Table 5), so differential parsing
failure cannot drive the contrasts we report; unbalanced extraction failure is the specific
way this kind of indicator goes wrong, and we state the rate for that reason.

Parental-line names carry their own entity-resolution problem, since a line may appear with
or without its breeder prefix. We normalise whitespace and quotation marks but do not merge
differently spelled names — the conservative choice, since unmerged variants inflate the
distinct-line count and depress the Herfindahl index, so the concentration **levels** we
report are lower bounds. We make no claim about the direction of any resulting bias to the
between-channel **contrast**, which would require knowing variant-splitting rates are equal
across channels — not established here.

## 3.2 Sample, stratification and indicator construction (step vi)

The main analysis stratum restricts to national-level approvals in the two dominant
mid-season indica trial groups — the middle-and-lower Yangtze and the upper-Yangtze
mid-season indica groups — in the years in which the channel variable carries identifying
variation, 2017 and 2019–2022 (2018 is excluded for the reason above; years before 2017 have
no self-organised channel at all and are used only as a pre-reform benchmark, see §4.1 and
§6). This yields **n = 878** records (Unified 406, Consortium 405, Green 67). Because the
green channel is concentrated in 2017 and the consortium channel in 2019–2022, and because
the two barely overlap in time, we split this stratum into two estimation arms: **Arm 1** (Consortium vs. Unified, 2019–2022, n = 759 before outcome-specific
missingness) and **Arm 2** (Green vs. Unified, 2017, n = 119). Arm 2's identifying variation
comes from only two effective year × trial-group × check cells (a third raw cell contains
only Green records and is dropped for lack of within-cell contrast), so all Arm-2 estimates
use heteroskedasticity-robust (HC1) rather than cluster-robust standard errors and are
flagged as small-sample throughout. An extended stratum that adds every other trial group
(n ≈ 1,020–1,029 for Arm 1, 119–125 for Arm 2) is used as a robustness check on the
two-trial-group restriction (§6, R3); a pre-reform benchmark layer (national approvals in
the same two trial groups, 2005–2016, n ≈ 213) supports the structural-break analysis and
the time placebo; and a provincial-approval layer (2021–2022, new-channel 143 / Unified 352)
supports an external replication check that we report as statistically inconclusive rather
than confirmatory or disconfirmatory (§6, R11).

## 3.3 Outcome variables, measuring party, and field-level data quality (steps v–vi)

The single most consequential pipeline step attaches a **measuring party** to each
extracted field. Beyond a conventional data-quality assessment of completeness and
transcription accuracy, we ask field by field *who generated the number the source
reports*, and treat that as a dimension of reliability on a par with coverage. The paper's
identification argument turns on a distinction the announcements make explicit: head-rice
percentage, chalkiness degree, whether a quality grade is stated, and the two
disease-resistance grades are all assayed by MARA-designated third-party bodies under the
applicable standard (NY/T 593 or GB/T 17891, §2); the yield outcomes and most agronomic
outcomes (growth duration, plant height, seed-set, thousand-grain weight, grains per
panicle) are recorded from the applicant's own trial. `quality_stated` is coded 1 if the
announcement carries a numeric grade or a named standard, defined for every record by
construction; its two source fields agree on presence/absence 84.5% of the time, so we use
their union. Because it is mechanically close to a missingness indicator for the underlying
grade field, we report it as measuring *announcement disclosure behaviour* rather than
grain quality itself, and §6 (R16) shows the coefficient strengthens once text length and
field-count are controlled for.

Missingness in the main stratum is low and mostly balanced across arms (within ~2 pp for
most outcomes in Arm 1). Three outcomes are not: regional-trial yield gain is 99.8% vs.
88.1% non-missing (Consortium vs. Unified, an 11.6-point gap); the top-two quality-grade
indicator is 77.0% vs. 88.7% (11.7 points); and absolute regional-trial yield is 100% vs.
90.4% (9.6 points). We report Manski worst-case bounds alongside the point estimate for
these three (§6, R7). Arm 2 is more severe for one outcome: regional-trial yield gain is
populated for only 1.9% of Arm-2 Unified records (1 of 52), so that coefficient is not
estimable and is reported as such rather than as a null. `applicant_type` (enterprise /
public / joint / unknown), used only in the descriptive comparison in §7, is entirely
missing for national approvals in 2016, 2017, 2018 and 2021 (904 records) — a documented
structural gap in the source, not our parsing — which is why any enterprise-vs.-public
comparison is confined to years with a non-missing field and presented as descriptive only.

Table 1 reports year-by-year record counts by channel, plotted alongside the institutional
timeline (§2) in Fig. 1. Table 2 gives a full descriptive and balance summary by arm for
every outcome and control in Table 3. The main text retains six figures and five tables; the
enterprise-vs.-institution comparison and the missingness-balance plot are in the
Supplementary Material as Table S1 and Fig. S1.

## 3.4 Representativeness and source verification (step v)

Two representativeness concerns bear on how results should be read. The compilation is a
sample of announcements, not a verified census, with declining coverage after 2022 (§3.1);
we restrict the window to 2017–2022 and treat post-2022 only as background evidence that the
channel distinction is currently being narrowed by regulatory action (§8.2). And because the
compilation is a third-party re-transcription rather than the official record, transcription
and parsing error are a live concern — not a peculiarity of our source, since large-scale
audits of S&T indicator databases find similar systematic error rates (Franceschini et al.,
2016), and the appropriate response is to state a corpus's verification status.

We state ours plainly: **we have not cross-checked the parsed corpus field by field against
the original MARA text, and report no transcription agreement rate.** Doing so requires the
primary announcements directly, which was not possible with our access. Every quantity here
is conditional on faithful transcription — an assumption relied on but not independently
confirmed, testable by a replicator with primary access — and is, per §8.5, the single most
consequential unverified assumption in the study.

---

# 4. Empirical strategy

## 4.1 Two difference-in-differences designs we considered and rejected

Before settling on the specification below, we considered and rejected two
difference-in-differences (DID) designs that would have let us speak of a causal "effect of
the reform." Using the provincial-to-national approval switch as a DID shock fails because
its parallel-trends assumption fails pre-period for three of six candidate outcomes
(chalkiness +0.515 pp/year, p = 0.006; amylose +0.212, p < 0.0001; thousand-grain weight
−0.130, p = 0.003 — all trending differently across administrative levels before 2016), so a
post-2016 gap would conflate a real channel effect with pre-existing divergence. Using
varying channel exposure across trial groups as a differential-intensity DID fails because
penetration ranges only 0.33–0.63 across groups, leaving no low-exposure counterfactual. Our
design is accordingly not a DID and does not estimate a pre/post treatment effect; it is a
within-cell cross-sectional comparison, described next.

## 4.2 A record-level trial-channel treatment and the collinearity problem

Reconstructing the trial channel at the record level — rather than treating the 2016 reform as a single period indicator, as the one existing evaluation does (Xiang et al., 2025) — makes it possible to ask not "did the market change after the reform" but "does what enters differ by door, within the same year." A naive specification $Y \sim \text{channel} + \text{year} + \text{trial\_group} + \text{check} + \text{breeding\_system}$ is not estimable: the named check is nearly perfectly nested within trial group, so entering both additively produces a rank-deficient design matrix. Rather than dropping either variable — losing the institutional structure the comparison needs held fixed — we absorb the hierarchy into one interaction fixed effect,

$$c(i) \;=\; \text{Year}_i \times \text{TrialGroup}_i \times \text{Check}_i,$$

which eliminates the collinearity and sharpens interpretation: every gap is identified from records tested in the same year, ecological trial group and against the same named check. Cells with only one channel contribute no identifying variation and are dropped; the resulting effective sample sizes appear in Table 3.

## 4.3 Main specification and estimator

The main specification is

$$Y_i \;=\; \beta\,\text{NewChannel}_i \;+\; \gamma_{c(i)} \;+\; \delta_{b(i)} \;+\; \varepsilon_i,$$

where $\gamma_{c(i)}$ is the interaction fixed effect above and $\delta_{b(i)}$ a breeding-system fixed effect (two-line/three-line hybrid/conventional). Standard errors are clustered at $c$ when an arm has at least five effective clusters, or HC1 otherwise (Arm 2's stratum has only three cells), flagged in every table. We estimate the two channels separately rather than pooling, since the green channel (2017) and consortium channel (2019–2022) barely overlap in time and diverge in sign on at least one outcome (production-trial yield gain: +0.919 pp consortium vs. −1.036 pp green). **Arm 1** sets $\text{NewChannel}_i = \mathbb{1}[\text{Consortium}_i]$ on Unified/Consortium records, 2019–2022; **Arm 2** sets it to $\mathbb{1}[\text{Green}_i]$ on Unified/Green records, 2017. A pooled specification is reported only as a reference row, never the headline estimate.

## 4.4 What $\beta$ identifies: a composition effect, not a treatment effect

$\beta$ is a **composition effect on the entering population**: within the same cell, how much better or worse, on average, are varieties entering through the self-organised door than the unified-trial door. It is not an estimate of what would happen if one variety moved between doors — that would need random assignment or a credible instrument, and we have neither. This is nonetheless what a regulator monitoring the entering population needs, and we avoid the language of *effect of*, *impact of* or *caused by* throughout.

## 4.5 Identification argument: separating ability from measurement

The paper's central inferential move compares two behaviourally distinct outcome classes
within the same specification. This move is also the paper's methodological claim in
operation, not merely an application of it: we treat *who measured a field* as a property of
the field rather than of the source, partitioning the outcome set on it before estimating
anything. Every field comes from the same announcement, issued by the same authority on the
same date, so a source-level data-quality judgement cannot distinguish them; the general
lesson drawn in §8.4 is nothing more than this section's premise stated in the abstract. Let
$Y^{3rd}$ denote an outcome assayed by a third party (head-rice, chalkiness, stated quality
grade) and $Y^{self}$ an outcome from the applicant's own trial (yield gain over check). Two
hypotheses predict different relations between $\beta^{3rd}$ and $\beta^{self}$:

- **$H_{ability}$** (pure breeding-ability difference): self-organised applicants breed
  systematically weaker varieties, so $\beta^{3rd} < 0$ **and** $\beta^{self} < 0$ together.
- **$H_{measure}$** (measurement-authority allocation): the two classes are measured by
  different parties with different incentives, predicting $\beta^{3rd} < 0$ **while**
  $\beta^{self} \ge 0$ — a sign separation.

Arm 1 shows exactly the pattern $H_{measure}$ predicts and $H_{ability}$ rules out:
$\beta^{3rd}$ is −1.844 for head-rice (p < 0.0001), +1.108 for chalkiness (p = 0.012), and
−0.122 for stated grade (p = 0.008), while $\beta^{self}$ is +0.553 for regional-trial yield
gain (p = 0.019) and +0.919 for production-trial yield gain (p < 0.0001). A pure
ability-difference story would need self-organised applicants to be simultaneously worse
breeders on quality and not worse on yield, within the same variety; only different
measuring parties, or different admission thresholds, can produce this pattern.

We are equally explicit about the limits. This rules out $H_{ability}$, but not a third
hypothesis, $H_{threshold}$ — that the two channels simply impose different admission
thresholds independent of measurement. $H_{measure}$ and $H_{threshold}$ predict the same
sign pattern here, and distinguishing them needs exactly the individual-level, cross-channel
variation the within-applicant check (§6, R9) shows this sample cannot supply with power.

## 4.6 Auxiliary specifications

Three auxiliary specifications support the main argument without altering it. A descriptive
specification, $Y_i = \theta\,\text{Public}_i + \gamma_{y \times g} + \delta_b + \varepsilon_i$,
restricted to years with a non-missing applicant-type field, characterizes the enterprise
vs. public-institution trait division of labour; it is reported only as a directional,
descriptive background fact (§4.7, Non-claim 9), not as a structural or causal comparison. A
germplasm-concentration comparison — the Herfindahl–Hirschman index across resolved parental
lines, with a stratified bootstrap and a label-permutation test for the between-channel
difference, and rarefaction for the distinct-line counts — supports the counter-case in §7
and is not used to estimate the main channel gap. An unknown-breakpoint sup-Wald scan (candidate breakpoints 2009–2019, with level-shift
and trend-shift specifications) is used only to test whether the quality trajectory has a
structural break coincident with the 2016 reform (§4.7, Non-claim 3), not to estimate the
channel gap itself.

## 4.7 What this paper does not claim

This paper's estimates support a narrower set of claims than the pattern of results might
suggest, and we state the boundaries explicitly so no reader mistakes a composition gap for
something it is not. One terminology note: where we call an outcome or check
*pre-specified*, we mean it was fixed in a written analysis plan before estimation, not
deposited in a public registry — weaker than a registered claim, and readers should weigh it
accordingly.

1. **$\beta$ is not a causal effect** — a within-cell composition gap, not the effect of
   moving a variety between channels; the design for the latter (§6.3) is underpowered by
   2–3× on every headline coefficient.
2. **No language of fabrication or manipulation** — claims are phrased as *consistent with*
   discretion, not proof of it.
3. **We do not claim the reform caused the quality gap.** The breakpoint scan (§5.5) dates
   the main quality breaks to 2009–2015, before the reform; we estimate a same-year gap.
4. **Not all third-party traits move the same way** — bacterial-blight grade moves opposite
   (§5.2); the headline claim is confined to grain-processing and appearance quality.
5. **The self-reported yield advantage is not established** — it reverses sign between arms
   and its Manski lower bound sits near zero (§6.2), hence "suggestive only."
6. **No welfare claim** — no adoption, price or consumption data exists here.
7. **Approval counts are never an outcome variable**, only descriptive background, since
   coverage declines sharply after 2022.
8. **Findings do not replicate at the provincial level for three of four outcomes** — see
   §6.4 for the full, two-part reading.
9. **No claim that enterprises are better or worse breeders than institutions** — the
   comparison (Supplementary Table S1) is descriptive background only.
10. **No individual applicant organisation is evaluated.** Nothing in §7 assesses the
    breeding capability, performance or conduct of any applicant; the concentration
    indicator describes entry routes, not organisations.
11. **No claim that homogenization is rising or falling over time** — §7 compares
    concentration *between channels within a period*, not a time trend.
12. **We do not treat the compilation as an official, complete registry** — its field-level
    agreement with the original MARA text has not been verified (§3.4), which the paper
    relies on rather than guarantees.

---

# 5. Results

## 5.1 Sample and strata

The main analysis layer restricts to national-level (国审) approvals in the two dominant indica trial groups (middle-and-lower-Yangtze; upper-Yangtze mid-season) in years the channel variable actually varies — 2017 and 2019–2022 — yielding **n = 878** (Unified 406, Consortium 405, Green 67). Since the green channel (2017) and consortium trials (2019–2022) do not overlap, we estimate two separate arms (§4.3): **Arm 1** compares Consortium (n = 405) with Unified (n = 354) within 2019–2022 (pre-outcome-drop n = 759, later n = 520–759 by missingness); **Arm 2** compares Green (n = 67) with Unified (n = 52) within 2017 (n = 119, 2–3 identifying cells). Table 3 reports both arms for all 17 outcomes, split into third-party-assayed and applicant-self-reported blocks; Fig. 2 plots the same 34 estimates as a forest plot, colour-coded by measuring party.

## 5.2 Arm 1: Consortium versus Unified, 2019–2022

Consortium entrants show a consistent, statistically robust deficit on every third-party-assayed grain-processing and appearance trait in the main quality block (Table 3; Fig. 2, left panel). Head-rice percentage is 1.844 pp lower (95% CI [−2.636, −1.052], p = 5.1 × 10⁻⁶, n = 742); chalkiness degree is 1.108 pp higher, i.e. worse (95% CI [0.248, 1.969], p = 0.012, n = 739); and the probability a national/industry quality grade is stated at all (`quality_stated`) is 12.2 pp lower (95% CI [−0.211, −0.033], p = 0.008, n = 750). Among graded records, the probability of the top two national tiers (`quality_top2`) is also lower by 9.1 pp (p = 0.009, n = 618), though this does not survive Manski worst-case bounds (§6.2) and is treated as secondary. Gel consistency moves the same way (β = −1.814 mm, p = 0.015, n = 728). Amylose content and grain length–width ratio show no significant difference; neck-blast resistance is not estimable in Arm 2 (§5.3) and shows no Arm 1 gap (p = 0.28).

Against this, applicant-self-reported yield traits move oppositely: regional-trial yield gain over check is 0.553 pp *higher* (95% CI [0.091, 1.016], p = 0.019, n = 708), and production-trial yield gain is 0.919 pp higher (95% CI [0.505, 1.333], p < 0.0001, n = 578). Raw two-year yield (kg/mu) shows no difference (β = +1.43, p = 0.61, n = 716), consistent with the gain-over-check measures capturing a comparison-scale effect. Two of three pre-specified placebos — seed-setting (β = −0.202, p = 0.43) and 1000-grain weight (β = +0.138, p = 0.59) — are non-significant as required. Plant height is 0.952 cm higher (p = 0.044); pre-specified *outside* the placebo set, this is reported as auxiliary evidence of a taller, larger-panicle selection type (§6.1, R12).

One trait falls outside the sign-separation pattern in a way that supports rather than undermines the identification argument: bacterial-blight grade, also third-party assayed, is 0.190 grades *lower* (more resistant) among Consortium entrants (95% CI [−0.278, −0.102], p < 0.0001, n = 520). We report this prominently because the claim is scoped to grain-processing and appearance quality, not to third-party traits deteriorating uniformly — a claim this result would falsify (§4.7, §6.2).

## 5.3 Arm 2: Green channel versus Unified, 2017

Green-channel entrants in 2017 (n = 119, HC1 SEs, 2–3 identifying cells) reproduce the same direction on appearance and grading traits at larger magnitude: chalkiness is 2.809 pp higher (95% CI [1.874, 3.744], p < 0.0001, n = 110) and stated-grade probability is 34.4 pp lower (p < 0.0001, n = 112). Head-rice, by contrast, is *not* significantly different (β = −0.391, p = 0.55, n = 106) — a genuine cross-arm inconsistency and one reason the arms are kept separate.

Two results diverge from Arm 1 and are reported, not deferred. Production-trial yield gain is 1.036 pp *lower* for Green entrants (95% CI [−1.860, −0.213], p = 0.014, n = 112) — opposite Arm 1's +0.919 pp. Regional-trial yield gain cannot be meaningfully estimated here: only 21 of 119 records are non-missing, driven by the Unified sub-arm's 1.9% coverage (1 of 52); we flag this as *not estimable*, as we do neck-blast (100% missing for all 119 records). Arm 2 does *not* replicate Arm 1's suggestive yield-advantage pattern, and we do not claim it does.

## 5.4 Channel composition and convergence over time

A year-by-year re-estimation of the Arm-1-style channel gap (HC1 SEs, years both channels co-exist: 2017 and 2019–2022; 2018 excluded, a parsing default rather than a real assignment) shows two patterns that must be reported separately. Chalkiness narrows monotonically from +2.71 pp in 2017 (p = 1.1 × 10⁻⁸) to +1.63 (2019), +0.92 (2020), +0.89 (2021) and +0.77 pp (2022, p = 0.038) — genuine convergence. The stated-grade gap weakens on balance (−0.327 to −0.052) but non-monotonically, non-significant in 2020 and 2022. Head-rice shows **no convergence**: −0.61 pp in 2017 (n.s.), widening to −2.63 (2020, p = 0.0003), −1.48 (2021, p = 0.021) and −3.03 pp (2022, p = 0.006) — its largest values in the most recent years. Regional-trial yield gain fluctuates between −0.63 pp (2017, n.s.) and +0.93 pp (2022), mostly positive from 2019 onward, with no clear convergence or divergence pattern (Fig. 3; full values in Supplementary Material). We therefore do not claim the quality gap is generally closing: only chalkiness, and more weakly stated grade, converge; head-rice — arguably the more material trait — does not.

## 5.5 Structural breakpoints predate the 2016 reform

An unknown-breakpoint (sup-Wald/Quandt) scan over 2009–2019, on the full 2005–2022 national two-trial-group layer, asks whether the quality traits behind Arm 1's headline result break structurally at the 2016 reform. They do not. Regional-trial yield per mu breaks at **2017** (Wald = 230.3, p < 10⁻⁵⁰, n = 1,167; Fig. 4), consistent with a level shift when the new channels opened. But the three quality traits central to this paper's argument break *earlier*: head-rice at **2015** (Wald = 73.9, p < 10⁻¹⁶), chalkiness at **2009** (Wald = 22.9, p = 1.1 × 10⁻⁵), and the top-two quality-grade indicator at **2015** (Wald = 45.5, p = 1.3 × 10⁻¹⁰) — all one to seven years before the reform. Yield gain over check shows no robust break: the 2018 candidate is marginally significant under HC1 (Wald = 6.55, p = 0.038) but not under classical SEs (Wald = 5.40, p = 0.067), and its non-missing rate jumps from 21–22% in 2016–2017 to 100% in 2018, confounding the apparent break with reporting completeness rather than a real discontinuity. Fig. 4 also plots growth duration for context only (peak at 2018, Wald = 226.8), since it is not one of the third-party-assayed traits this section addresses; full scan values are in the Supplementary Material.

These results support a falsification claim, not a positive dating claim: whatever quality trend is visible pre-2016 was already underway, so attributing it to the reform — rather than to the *channel gap conditional on year* this paper estimates (§5.2–5.3) — would be mistaken. The result also bears on the year-indexed readings of the same corpus by Lu et al. (2024) and Hang et al. (2024): our break years (2015, 2009) sit inside their trend windows, consistent with, though not a direct test of, gradual rather than reform-triggered change. The two approaches are complementary: a year-indexed design cannot distinguish, as our Arm 1/Arm 2 comparison does, whether varieties entering through one channel look different from contemporaries in another.

## 5.6 Summary

Table 3 and Fig. 2 present the full set of 17 outcome variables for both arms, including the outcomes that run against the paper's central narrative (bacterial-blight resistance, Arm 2's reversed production-trial yield gain, Arm 2's non-estimable regional-trial yield gain). The pattern that survives across both arms is a consistent, third-party-assayed grain-processing and appearance-quality deficit among self-organised-trial entrants, paired with an applicant-measured yield performance that is, if anything, higher — a sign separation inconsistent with a pure breeding-ability account, but not by itself sufficient to rule out differing entry thresholds across channels. Section 6 subjects this pattern to sixteen pre-specified and one additional robustness checks, several of which qualify or fail to replicate parts of the headline result, and reports all of them.

---

# 6. Robustness, placebos and bounds

This section reports seventeen robustness checks (R1–R17) against the Arm-1 headline results of Section 5 (head-rice −1.844 pp, chalkiness +1.108 pp, stated quality grade −0.122, regional-trial yield gain +0.553 pp, production-trial yield gain +0.919 pp, bacterial-blight grade −0.190; see Table 3 and §5.2 for full CIs, p-values and n). No check is omitted, and where a check does not support the main result, we say so and report the number. Checks that leave the headline pattern essentially unchanged (R1–R6, R8, R10, R12–R14, R17) are reported briefly, with full statistics left in Table 3/Table 4; checks that qualify or complicate the headline pattern (R7, R9, R11) are given full treatment, since these are the ones a reader needs explained rather than tabulated. R15 is the one exception to that arrangement: its verdict and headline diagnostics are reported in §6.5, with its construction and full diagnostics in the Supplementary Material.

## 6.1 Checks that leave the headline pattern unchanged (R1–R6, R8, R10, R12–R14, R17)

Full statistics for every check below are in Table 4; this section states only the check and its conclusion.

- **R1 (two channels never pooled).** Pooling Arm 1 and Arm 2 would average a +0.919 pp yield-gain coefficient with a −1.036 pp one, manufacturing a sign that never occurred; reported only as a reference row, never the headline estimate.
- **R2 (fixed-effects specification).** The additive, collinearity-prone year + trial-group + check specification reproduces the same signs and comparable magnitudes for all four cross-checked coefficients — the fixed-effects structure does not drive the result.
- **R3 (extend to all national trial groups).** Direction and significance are essentially unchanged in both arms — not an artefact of the two-trial-group restriction.
- **R4 (2018 treatment).** Coding the 233 unlabelled 2018 records as Unified rather than excluding them produces numerically identical estimates, because every 2018 cell in this stratum is a singleton carrying no identifying variation either way.
- **R5 (Benjamini–Hochberg FDR).** 9 of 17 Arm-1 outcomes retain q < 0.05 across all 17 tests, including all six headline coefficients (q = 0.00009–0.040); the sign-separation pattern does not depend on uncorrected multiple testing.
- **R6 (randomisation inference).** Exact permutation p-values (500 draws per cell; Fig. 5) place head-rice, chalkiness and regional-trial yield gain in the extreme tail of their null distributions (p = 0.002 each), independently of cluster-asymptotic assumptions.
- **R8 (missingness balance).** Fig. S1 shows most of the 17 outcomes balanced within ~2 pp of non-missing rate across arms; the three exceptions motivate the Manski-bounds exercise (R7, below).
- **R10 (drop the dominant germplasm lineage).** Dropping every record whose sterile line is the most prevalent one (65 of 878 records) leaves the result significant with the same sign (head-rice −1.367 pp, p = 0.001; chalkiness +1.077 pp, p = 0.020; stated grade −0.119, p = 0.017) — no dependence on any one breeding lineage; see also §7.
- **R12 (pre-declared placebos).** Seed-setting percentage and thousand-grain weight are both non-significant, as pre-declared. Plant height, pre-declared *outside* the placebo set, is significantly higher among Consortium entrants (β = +0.952 cm, p = 0.044) and is reported as auxiliary evidence, not a failed placebo.
- **R13 (pre-reform time placebo).** A pseudo-treatment built the same way in 2005–2016, before any channel existed, returns no significant coefficient on any outcome, with the opposite sign for both headline quality traits — weakening one confound without ruling out $H_{threshold}$ (§4.5).
- **R14 (cluster by variety).** Re-clustering at the variety level (36 varieties, 72 multi-zone records) leaves all headline coefficients significant at p ≤ 0.0014.
- **R17 (quality-grading standard composition).** Records are graded under NY/T 593 or GB/T 17891, and which is in force shifts across the window (2017 predominantly GB/T, 2019–2022 predominantly NY/T 593). Within each arm's own window the standard does not vary by channel (Arm 1: 99.2% vs 99.2% NY/T 593; Arm 2: entirely GB/T both sides), so the year × trial-group × check cell absorbs the switch; the check independently recovers the disclosure result from raw shares (+13.0 pp and +32.6 pp). The quality contrasts are not an artefact of which standard applied.

## 6.2 Manski worst-case bounds (R7)

Three outcomes show meaningfully unbalanced missingness between arms — the top-two quality grade (23.0% missing in Consortium vs. 11.3% in Unified), regional-trial yield gain (0.2% vs. 11.9%, and separately 1.9% in the 2017 Unified sub-arm), and absolute regional-trial yield in kg/mu (Fig. S1; imbalances ≥8 pp flagged) — so we compute Manski worst-case bounds, filling missing values at the 5th/95th percentile extremes. Head-rice and chalkiness, whose missingness is balanced (~1–2 pp), have narrow, sign-stable bounds ([−2.001, −1.623] and [+0.976, +1.203]) and are the paper's most secure results. The top-two quality-grade indicator does **not** survive: its bound is [−0.253, +0.088], crossing zero, so we downgrade it to secondary and rely on the fully-defined stated-quality-grade indicator as the primary grading result (Table 3, §5.2). Regional-trial yield gain's bound is [+0.049, +0.912] — the lower end near zero (p = 0.91 there) — so this is downgraded from "suggestive support" to "directionally positive but not robustly bounded away from zero." No other headline result changes sign.

## 6.3 Within-applicant subsample and its minimum detectable effect (R9)

The most direct test of self-selection versus a genuine channel effect compares the same applicant's own varieties across channels: 10 applicants, 51 records (26 Consortium, 25 Unified), estimated with applicant fixed effects and HC1 SEs. None of the six headline coefficients is significant, and three (head-rice, chalkiness, stated grade) flip sign (head-rice +0.780, p = 0.61; chalkiness +0.846, p = 0.21; stated grade +0.118, p = 0.40; regional-trial yield gain +0.100, p = 0.86; production-trial yield gain −0.126, p = 0.82; bacterial-blight −0.421, p = 0.38).

The minimum detectable effect (MDE) at 80% power exceeds the main-design coefficient for every outcome — head-rice 4.37 pp (≈2.4×), chalkiness 1.96, stated grade 0.41, regional-trial yield gain 1.66 (≈3×), production-trial yield gain 1.56, bacterial-blight 1.41 — converting "underpowered" into a quantitative claim: **this design cannot distinguish "no channel effect once self-selection is removed" from "the effect exists but this subsample is too small to detect it."** The sign flips are consistent with severe noise rather than a credible contradiction, but the test does not confirm the main effect either — it lacks the power to adjudicate (§4.7, Non-claim 1).

## 6.4 Provincial replication and its minimum detectable effect (R11)

Provincial-level approvals (省审) in 2021–2022, pooling Consortium and Green under a single new-channel indicator against Unified (cell: year × trial group, no check dimension since provincial labels are far more heterogeneous), give n = 495 (new-channel 143, Unified 352). None of three headline outcomes replicates at comparable magnitude, and all are severely underpowered: head-rice β = −3.354, p = 0.53, n = 280, MDE = 14.99 pp against −1.844 nationally; chalkiness β = −0.549, p = 0.24, n = 256, MDE = 1.31 pp against +1.108 (sign reversed, but the MDE shows this uninformative); regional-trial yield gain β = −0.994, p = 0.62, n = 205, MDE = 5.62 pp against +0.553 nationally.

**Stated quality grade is the exception:** the provincial sample is adequately powered (MDE = 0.41, smaller than the national coefficient) and returns a significant, larger-magnitude, same-direction coefficient (β = −0.468, p = 0.001) — read as strengthening rather than qualifying that half of the headline result. R11's correct reading is therefore two-part: for head-rice, chalkiness and yield gain the national effect is **statistically undecidable** at the provincial level, not disproved; for stated grade, the provincial result is adequately powered and corroborates.

Because provincial trial-group labels are heterogeneous, the cell definition is a judgement call and the sample size is sensitive to it; we read this check for direction only where the MDE shows point estimates uninformative.

## 6.5 A chained-check genetic-gain scale as an alternative yield metric (R15)

The gain over the named check (§5.2–5.3) is comparable only within a trial-year-check cell, so we also re-expressed yield on a chained cross-year check scale (Piepho et al., 2014; Laidig et al., 2014; Mackay et al., 2011; Raymond et al., 2023; Piepho and Laidig, 2025). Four known weaknesses appear: an unstable back-solved check yield (median CV 1.56%); a chain step moving +3.14% where the decomposition implies +7.04%; an implied gain rate swinging 0.25–0.50%/year; and only six distinct checks (~3 effective degrees of freedom). The self-reported yield advantage does not reverse direction, but the interval is too wide to pin its magnitude — inconclusive rather than confirmatory or disconfirmatory. Construction and full diagnostics are in the Supplementary Material.

## 6.6 `quality_stated` under disclosure-behaviour controls (R16)

§3.3 flags `quality_stated` as mechanically close to a missingness indicator for the grade field, reported as measuring *disclosure behaviour* rather than quality itself. This check asks whether the Arm-1 coefficient is an artefact of shorter announcements: re-estimating with two added controls, text length and the count of non-missing fields among the other 16 outcomes (n = 750), the baseline β = −0.122 (p = 0.0075) becomes β = −0.146 (p = 0.0005) with controls — it survives and strengthens, ruling out the simplest "shorter announcements say less" account.

## 6.7 Robustness matrix

Table 4 collects all seventeen checks (R1–R17), including two that qualify a headline result (R7's Manski bound on top-two quality grade; R11's mostly-underpowered, partly-corroborating provincial replication) and one genuinely underpowered rather than informative either way (R9). Read with the year-by-year evidence (§5.4), the central identification claim — third-party quality deficit paired with unchanged-or-higher applicant-measured performance — survives every adequately powered check (R1–R6, R8, R10, R12–R14, R16, R17), is not reproduced by a pre-reform placebo sharing no real channel variation (R13), and is qualified rather than contradicted by the two low-power checks (R9; three of four outcomes in R11). The one secondary result failing worst-case bounds (top-two grade, R7) is downgraded from headline evidence; the alternative yield metric (chained-check ladder, R15) returns an inconclusive result that neither strengthens nor weakens the main yield finding.

---

# 7. Germplasm concentration by channel: does each door admit a different breeding base?

*This section tests an alternative explanation for the sign separation using a second indicator built from the same announcements. It is not a source of the main result.*

The sign separation in Sections 5–6 is consistent with measurement discretion in self-organised trials, but equally consistent with a cruder alternative: the self-organised channels may simply admit varieties bred from a narrower germplasm base, so the quality deficit records *what* enters rather than *how* it is measured. The announcements support a direct test, since each names the cross that produced the variety.

We resolve the variety-source field into the sterile (female) and restorer (male) line of the originating cross, succeeding for 2,304 of 2,386 national records (96.6%; §3.1 gives the extraction rule and failure profile). The indicator is computed on the same stratum as the main estimates — the two dominant indica trial groups, since pooling unrelated breeding pools would inflate any contrast — using the Herfindahl–Hirschman index across sterile lines, distinct-line counts (rarefied to the smaller group), and top-line share, with a stratified bootstrap and label-permutation test for the between-channel difference. Extraction coverage is 99.7–100% in all four channel-by-arm groups, so differential parsing failure cannot drive the comparison.

Consortium entrants draw on a **broader** sterile-line base than contemporaneous unified entrants (Table 5; Fig. 6): HHI 0.0124 against 0.0186 (difference −0.0062, 95% CI [−0.0130, −0.0009], permutation *p* = 0.022) — 212 distinct lines against 156 (193.0 rarefied), top-line share 5.7% against 9.1%. This is what consortium rules, pooling five or more breeding programmes, predict.

Green-channel entrants are directionally more concentrated (HHI 0.0778 against 0.0562, top share 22.4% against 11.5%), matching what a single-enterprise-run channel predicts, but at 67 against 52 records the interval spans zero (+0.0215, 95% CI [−0.0240, +0.0671], *p* = 0.344); we report Arm 2 for completeness and rest nothing on it. An earlier version of this analysis, computed across all national trial groups rather than the estimation stratum, returned a significant Arm-2 contrast; restricted to the correct stratum, it does not survive.

The Arm-1 result alone rules the alternative out. A narrow-breeding-base account predicts the quality deficit appears where fewer lines are drawn on; consortium entrants show 1.844 points lower head-rice and 1.108 points higher chalkiness than unified entrants, yet draw on a significantly **broader** base than that same comparison group. What separates the two channels is measurement arrangement, not germplasm: the applicant organises the performance trial, while grain quality is assayed by the same ministry-designated third party either way (§2; §3.3). We claim no more than this — the germplasm-diversity story is inconsistent with the Arm-1 data; other composition stories, including selection on an unobserved threshold, remain open (§4.7, §6).

Dropping every record whose sterile line is the most prevalent one in the stratum leaves the headline result intact (§6.1 R10; Table 4): head-rice −1.367 pp (p = 0.001, n = 689), chalkiness +1.077 pp (p = 0.020, n = 686), stated grade −0.119 (p = 0.017, n = 696).

As descriptive background only, applicants labelled "public research institute" show higher regional-trial yield (+4.179 kg/mu, p = 0.027, n = 408) and thousand-grain weight (+1.193 g, p = 0.003, n = 411) than enterprise applicants, alongside directionally higher chalkiness (+1.010, p = 0.100) and lower head-rice (−1.220, p = 0.070, n = 411; Supplementary Table S1) — neither quality coefficient significant. This runs opposite to an "enterprises are careless" prediction for chalkiness and head-rice but is silent on causation; no part of the argument rests on it.

Three scope limits apply. Concentration across parental lines measures breeding-base breadth, not genetic distance — two varieties sharing a sterile line may still differ substantially. The extraction rule takes only the first cross, so ancestry beyond the immediate parents is unrepresented, and the 3.4% of unparsed records are excluded rather than imputed. And "identification argument" is the operative phrase throughout: the concentration contrast rules out one alternative explanation and is not evidence of a causal mechanism linking channel, germplasm and outcome.

---

# 8. Discussion

## 8.1 Why the sign separation arises: self-certification as theoretical support

The regulatory-economics literature on self-certification is not this paper's frame, but supplies the mechanism that makes the sign separation intelligible. Duflo et al. (2013) randomly assigned polluting Indian plants to regulator-paid versus plant-paid auditors and observed the *same* readings diverge systematically; Bar and Zheng (2019) show firms endogenously choose certifiers with a history of lenient grading — the closest analogue to the channel self-selection alternative this paper cannot close off (§4; R9/R11). Grennan and Town (2020) compare device outcomes *across* two regulatory systems, where ours compares *within* one system across two pathways a single reform created; Renckens and Auld (2022) show private-audit efficiency varies with auditor incentives. Together these establish that reported values move with who was asked to measure — the interpretation the sign separation invites, reported as consistent with measurement discretion rather than proof of it, since none of these designs is directly available here (we observe two different attributes measured by two parties, not one attribute measured twice). Qiu et al. (2016) describe a related asymmetry one stage downstream in the same seed system: using survey data from maize farmers across four leading production provinces, they find that farmers with less information about a variety's true performance are more likely to adopt a new variety specifically to hedge production risk, rather than on an expectation of higher yield, and they recommend better seed-market information provision as the remedy. Their setting is maize, not rice, and their asymmetry sits between seller and farmer rather than applicant and regulator, so the mechanism does not transfer mechanically; but the two results compound rather than merely sit adjacent. If approval records, or the extension and seed-dealer materials derived from them, are among the signals a farmer's information set draws on, then a third-party-assayed quality signal that this paper shows is weaker for self-organised-channel entrants does not stop at the regulator's desk — it propagates into exactly the farmer-level information gap Qiu et al. document, at the very first point in the seed system where measured quality is recorded. Better information provision at the point Qiu et al. study presupposes that the underlying record is a reliable input to provision in the first place; this paper's finding is that, for one entry route, it is a weaker one.

## 8.2 Is the identified variation disappearing? A qualified answer

MARA has, since 2022, conducted a special rectification campaign targeting the green channel and consortium trials, raising the question of whether the gap documented here is a closing window rather than a stable feature. The year-by-year re-estimation in §5.4 answers this outcome by outcome, not uniformly: the chalkiness gap declines roughly monotonically, consistent with narrowing as regulatory attention increases; the stated-grade gap weakens more faintly and non-monotonically, non-significant in two of four post-2017 years; the head-rice gap does not narrow at all, its largest and most significant values in the most recent years (Fig. 3). We therefore do not claim the variation is disappearing as a blanket statement — that holds for chalkiness, holds weakly for stated grade, and does not hold for head-rice, the paper's cleanest estimate. Coverage falls sharply after 2022, so this paper cannot verify further convergence beyond its window. Read against the calendar-year trends in Lu et al. (2024) and Hang et al. (2024), our channel-conditional gap shows a mix of convergence and non-convergence within six years, suggesting their long-run trajectory and our channel-specific gap are not the same object.

One further result belongs here. The province-level replication (§6.4) is underpowered for three of four headline outcomes — their provincial non-significance is "undetermined," not evidence against the national result — and adequately powered and corroborating for stated quality grade. That split runs against a common but incorrect reading of provincial null results in this literature: the evidence should be described precisely, one outcome significant and adequately powered, three underpowered, not summarised as either "confirms" or "does not replicate."

## 8.3 Policy implications

The evidence supports three specific recommendations, each grounded in a result already reported rather than in new analysis, and a fourth cautions against a plausible-sounding but wrong one.

**Target verification at the trait that is not converging.** §5.4 shows the third-party quality traits do not respond uniformly to the post-2022 tightening: chalkiness narrows monotonically toward zero and stated quality grade weakens on balance, but head-rice percentage shows no convergence at all, with its largest and most significant gaps in the most recent years of the sample. Whatever verification effort the current rectification campaign applies, it appears to be reaching chalkiness and, more weakly, stated grade, but not head-rice. A regulator prioritising where to add independent re-assay capacity, rather than spreading it evenly across traits, has a specific, falsifiable target in this result.

**Do not fix this by tightening consortium composition rules.** A natural regulatory instinct — narrow eligibility for consortium trials, or require a more diverse breeding-base among participating consortium members, on the theory that a narrower germplasm pool produces weaker varieties — is directly contraindicated by §7: consortium entrants draw on a significantly *broader* sterile-line base than the unified-trial entrants they are compared against (HHI 0.0124 vs. 0.0186), yet still show the quality deficit. The lever this paper's evidence points to is measurement and verification at the point of testing, not the composition rules governing who may form a consortium.

**Treat non-disclosure as an automatic verification trigger.** §6.6 shows the gap in whether a national quality grade is stated at all survives, and strengthens, once announcement length and field-completeness are controlled for (β = −0.122 to −0.146, p = 0.0005) — ruling out the alternative that self-organised-channel announcements are simply thinner on detail. A cheap, low-discretion rule follows directly: an approval record entering through a self-organised channel without a stated national or industry quality grade should trigger mandatory third-party re-verification before market approval, rather than resting on periodic or discretionary spot-checks.

**This is not a claim of regulatory blindness, and does not need to be one to matter.** Independent spot-checks of self-organised trials are already the Ministry's own initiative since 2022 (§2); this paper's contribution is not to report that verification is needed, which the 2022 notice already establishes, but to say *which trait, which mechanism, and which trigger* — head-rice specifically, verification rather than consortium composition, and non-disclosure specifically — using evidence a regulator would otherwise have to construct from the same announcements this paper already parsed.

## 8.4 A methodological note for building indicators from administrative records

The result behind §8.3's recommendations rests on a general data-quality point worth stating on its own, since it bears on any technology-assessment exercise built from administrative rather than laboratory data. Approval, registration and licensing records are a source class technology-policy measurement has under-used relative to patents and publications (Rammer and Es-Sadki, 2023), chiefly because they are published as prose; §3 shows they repay parsing, at the cost of most analyst effort falling on entity resolution and data-quality assessment (§3.1, §3.4) rather than extraction.

The specific quality lesson is that **reliability is a property of a field, not of a source.** Within one document, issued by one authority on one date, fields differed in evidential strength according to who measured them: laboratory-assayed quality moved one way, applicant-recorded yield the other (§4.5). Standard data-quality assessment of administrative and scientometric sources is conducted at the source level — coverage, error rates, classification accuracy (Franceschini et al., 2016; Jaffe and de Rassenfosse, 2017) — but a source that passes such an audit can still contain fields of very different evidential value, exactly as this one does. For technology-assessment work built on approval or registration corpora, the practical implication is the same one §8.3 turns into a policy rule for this dataset: tag each field with its measuring party, and treat a contrast confined to the independently-assayed fields as more credible than one confined to the self-reported fields. The same structure — applicant-supplied material bound with independent assay results in one official record — recurs in drug approval (Shi et al., 2021) and patent examination (Jaffe and de Rassenfosse, 2017), so the diagnostic is not specific to seed regulation; but its use here is to support the agricultural-policy recommendations in §8.3, not to generalise beyond them.

## 8.5 Limitations

Six limitations bound this paper's scope. (1) The evidence covers a single country and crop; whether the same channel-measurement asymmetry appears elsewhere is untested. (2) Channel self-selection cannot be fully separated from measurement discretion — the within-applicant comparison (§6) is directionally uninformative because it is underpowered, not because it rules out self-selection. (3) `applicant_type`, needed for the enterprise-vs-institute comparison in §7, is entirely missing for the 2016, 2017, 2018 and 2021 cohorts, limiting that comparison to years with non-missing labels. (4) The compilation's field-level fidelity to the original text has not been verified (§3.4) — the single most consequential unverified assumption in the study, since every estimate would inherit any systematic transcription error we cannot presently bound; a replicator with primary access should treat this as the first check to run. (5) The window runs through 2022 because coverage falls sharply afterward, so this paper cannot speak to whether the trends in §8.2 continue, reverse or stabilise. (6) China's approval standards define categories judged against different trait bundles, and applicants targeting a high-yield category would rationally accept weaker quality; we cannot control for this, since no category term or field occurs anywhere in the corpus. The §7 germplasm evidence constrains one version of this story but not all of it — an argument for the provenance-labelling recommendation in §8.4.

---

# 9. Conclusion

Since 2016, rice varieties have entered the Chinese market through three trial channels instead of one. Parsing which trial each variety passed through shows that what enters differs by channel on precisely the traits a third party, rather than the applicant, measures: self-organised entrants carry worse third-party-assayed quality alongside applicant-measured performance that is unchanged or higher — a difference in what each door admits, not an estimate of what the reform did, and a sign separation a breeding-ability story cannot produce, surviving the removal of the most prevalent breeding lineage.

This is a composition effect on the population entering each pathway, not a causal effect on any individual variety. It does not speak to farmer welfare, extension outcomes or seed prices; it does not allege fabrication, a possibility the data cannot distinguish from self-selection or differing thresholds; and it does not extend to every third-party trait or level of government, since disease-resistance grading moves the other way and provincial replication is conclusive for only one of four outcomes. Within these bounds, the contribution is an agricultural technology-assessment one: a record-level channel variable, read from announcement text rather than imposed as a before/after indicator, that shows what changed after 2016 was not only volume, and evidence pointing to where verification effort should be concentrated (§8.3). The method behind it generalises — a long-public administrative corpus can become a structured indicator system whose fields must be read individually, since evidence strength inside one official source depended on who did the measuring (§8.4) — but that generalisation supports the agricultural-policy conclusion; it is not a second, separate contribution alongside it.

---

## Acknowledgements

[Author to complete: funding sources, reviewer thanks, etc.]

---

## Conflict of interest

The authors declare no conflict of interest.

---

## Data availability statement

The variety-approval text corpus underlying this study was compiled from publicly available Ministry of Agriculture and Rural Affairs announcements via a third-party aggregation (§3). Parsing scripts, the field dictionary, and the list of approval-record identifiers used in the analysis are available at [repository link]. Due to the unresolved licensing status of the upstream aggregation, the full parsed dataset is not redistributed; researchers can reconstruct it from the cited public announcements using the provided scripts.

---

## CRediT author contributions

*(Placeholder — to be completed by the author team before submission. List each named author against the CRediT roles that apply; a role may be shared by more than one author.)*

- **Conceptualization**: [Author(s) to complete]
- **Methodology**: [Author(s) to complete]
- **Formal analysis**: [Author(s) to complete]
- **Investigation**: [Author(s) to complete]
- **Data curation**: [Author(s) to complete]
- **Writing – original draft**: [Author(s) to complete]
- **Writing – review & editing**: [Author(s) to complete]
- **Visualization**: [Author(s) to complete]
- **Supervision**: [Author(s) to complete]

---

## Ethical approval

Not applicable. This study did not involve human participants or animal experiments; it uses only publicly available government variety-approval announcements.

---

# References

Antons D, Grünwald E, Cichy P, Salge T O. 2020. The application of text mining methods in innovation research: Current state, evolution patterns, and development priorities. R&D Management, 50, 329–351.

Bar T, Zheng Y. 2019. Choosing certifiers: Evidence from the British Retail Consortium food safety standard. American Journal of Agricultural Economics, 101, 74–88.

Duflo E, Greenstone M, Pande R, Ryan N. 2013. Truth-telling by third-party auditors and the response of polluting firms: Experimental evidence from India. Quarterly Journal of Economics, 128, 1499–1545.

Franceschini F, Maisano D, Mastrogiacomo L. 2016. Empirical analysis and classification of database errors in Scopus and Web of Science. Journal of Informetrics, 10, 933–953.

Gong J Y, Zhang X B, Zhang J F, Zeng B, Zhang X Q, Xu X, Cheng B Y, Hou Y X, Xia J H, Wu J L, Yang S H, Cheng S H, Han B, Xie H A, et al. 2026. Three-line hybrid rice in China: fifty years of sustained improvement in yield, quality, and stress resistance. Rice Science, 33. (Cited at title level only; the full text was not accessible to us, and no specific figure is attributed to it.)

Grennan M, Town R J. 2020. Regulating innovation with uncertain quality: Information, risk, and access in medical devices. American Economic Review, 110, 120–161.

Hang S, Wang Q, Wang Y, Xiang H. 2024. Evolution of rice cultivar performance across China: A multi-dimensional study on yield and agronomic characteristics over three decades. Agronomy, 14, 2780.

Jaffe A B, de Rassenfosse G. 2017. Patent citation data in social science research: Overview and best practices. Journal of the Association for Information Science and Technology, 68, 1360–1374.

Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. Theoretical and Applied Genetics, 127, 2599–2617.

Losiewicz P, Oard D W, Kostoff R N. 2000. Textual data mining to support science and technology management. Journal of Intelligent Information Systems, 15, 99–119.

Lu Y, Tang Y, Zhang J, Liu S, Liang X, Li M, Li R. 2024. Variations and trends in rice quality across different types of approved varieties in China, 1978–2022. Agronomy, 14, 1234.

Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. Theoretical and Applied Genetics, 122, 225–238.

Piepho H-P, Laidig F. 2025. How many checks are needed per cycle in a plant breeding or variety testing programme? Plant Breeding, 144, 242–248.

Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. Theoretical and Applied Genetics, 127, 1009–1018.

Qiu H G, Wang X B, Zhang C P, Xu Z G. 2016. Farmers' seed choice behaviors under asymmetrical information: Evidence from maize farming in China. Journal of Integrative Agriculture, 15, 1915–1923.

Rammer C, Es-Sadki N. 2023. Using big data for generating firm-level innovation indicators — A literature review. Technological Forecasting and Social Change, 197, 122874.

Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. Field Crops Research, 303, 109086.

Renckens S, Auld G. 2022. Time to certify: Explaining varying efficiency of private regulatory audits. Regulation & Governance, 16, 500–518.

Shi Y, Ren P, Zhang Y, Gong X, Hu M, Liang H. 2021. Information extraction from FDA drug labeling to enhance product-specific guidance assessment using natural language processing. Frontiers in Research Metrics and Analytics, 6, 670006.

Xiang C, Yang R, Wang X, Huang J. 2025. Impact of seed regulation reform on licensing fees of varieties in China. Agribusiness.


Zhao Y, Deng H, Hu R, Xiong C. 2022. Impact of government policies on seed innovation in China. Agronomy, 12, 917.
