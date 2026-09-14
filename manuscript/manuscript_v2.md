# Who measures what enters the market? Self-organised variety trials and the third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022

*Running title:* Trial channels and third-party grain quality in Chinese rice approvals

---

## Abstract

China's 2016 revision of the *Measures for the Administration of Crop Variety Approval* ended the state monopoly on variety-value testing: certified seed firms may run green-channel trials, and consortia of five or more breeders may organise regional trials. Whether this changed what enters the seed market, not only how much, is unknown, because no prior study observes which trial channel a variety passed through. We exploit an unused feature of official approval announcements, which name the trial each variety was tested in, to assign every record to the unified trial, the green channel, or a consortium trial. Using rice approval records parsed from Ministry announcements, we compare self-organised with unified-trial entrants within the same approval year, ecological trial group and named check, estimating the green channel (2017) and consortium trials (2019–2022) as separate treatments since they do not overlap in time. Consortium entrants show 1.84 percentage points lower head-rice percentage, 1.11 points higher chalkiness, and a 12.2-point lower probability of carrying a stated national quality grade, all third-party-assayed under NY/T 593, while the yield advantage recorded in the applicant's own trial is, if anything, higher (+0.55 points, suggestive only); green-channel entrants likewise show higher chalkiness. This sign separation is the identification argument: a pure breeding-ability account predicts both trait classes deteriorate together, whereas third-party grain quality deteriorates while applicant-measured performance does not. Results survive worst-case bounds, randomisation inference, and dropping the focal firm. Bacterial-blight grades are better, not worse, among self-organised entrants, a result that bounds the composition effect.

---

## Keywords

variety approval; third-party certification; self-organised trials; rice quality; seed regulation; China

---

## Highlights

1. Trial channel is reconstructed from approval-announcement text at record level.
2. Consortium-trial entrants show lower third-party-assayed grain quality.
3. Applicant-measured yield performance is not lower for self-organised entrants.
4. Green-channel and consortium-trial gaps diverge and are estimated separately.
5. A leading seed firm uses self-organised trials less, against low breeding capacity.

---

# 1. Introduction

Variety approval decides which rice varieties may be sold as certified seed in China, and until 2016 the government held a monopoly on the trials that produced this decision: every candidate variety was measured, under the same protocol, in the state-run unified regional trial. The 2016 revision of the *Measures for the Administration of Crop Variety Approval* ended that monopoly. Certified integrated seed-breeding-extension enterprises could now organise their own "green-channel" trials, and consortia of five or more breeders could organise their own regional trials. Both channels replace the government as the party that runs the trial in which agronomic performance is measured; neither channel replaces the ministry-designated third-party laboratories that measure grain-processing and appearance quality once a candidate reaches the approval stage. This split — self-organised measurement of performance, third-party measurement of quality, inside the same approval file — is the object of this paper. We ask not how large the reform was, but *who holds the measuring stick* for what enters the market.

This question has not been answered because it has not been asked in a form the data could answer. The two studies that evaluate this same reform, Xiang et al. (2025) and Zhao et al. (2022), both code the reform as a *period* variable — before versus after 2016 — applied to licensing-fee data and to national approval panels, respectively. Xiang et al. (2025) find that licensing fees for hybrid rice varieties are not significantly affected by the reform; Zhao et al. (2022) trace policy variables against approved-variety trait trends over time. Neither paper observes which trial a given variety actually passed through, so neither can distinguish a change in *how much* enters the market from a change in *what* enters it. A null effect on price, in particular, is silent on whether the composition of entering varieties shifted. This is the gap: no existing study has a record-level channel variable to test whether self-organised and state-run entrants differ in what they bring to market.

A related but distinct literature reads approved-variety trait trends by *calendar year* rather than by trial channel. Lu et al. (2024) classify the quality-trait trajectory of 17,785 nationally and provincially approved varieties from 1978–2022, and Hang et al. (2024) track yield and agronomic-trait evolution across 11,811 regional-trial entries from 1990–2023; both papers read the same kind of approval-trial record we use, but neither carries a variable for which trial organised the test, so both attribute trait change to *when* a variety was approved rather than to *which door* it entered through. This paper's structural-break analysis (§5.6) and the "closing window" discussion (§8.2) speak to the same substantive object — the trajectory of quality and yield traits in China's approval records — but ask a channel-conditional question that a year-indexed reading cannot: whether the pre-2016 quality trend Lu et al. (2024) and Hang et al. (2024) document already contains the same channel a variety passed through, or whether it is orthogonal to channel altogether. A recent title-level review of fifty years of three-line hybrid rice trends (Gong et al., 2026) situates this same trait trajectory over a longer horizon; because the full text of that review was not accessible to us at the time of writing, we cite it only for its scope and do not attribute any specific figure to it.

We close this gap using a feature of the official approval announcements that has not previously been exploited: each announcement states, in its own text, the name of the trial in which the variety was tested — the unified regional trial, the green channel, or a named consortium trial. Parsing this text lets us assign every approval record to a channel and compare self-organised entrants with unified-trial entrants within the same approval year, the same ecological trial group, and the same named check variety. Because the green channel is concentrated in a single year (2017) and consortium trials begin only in 2019, the two channels barely overlap in time; we treat them as two separate treatments rather than pooling them into one "new channel."

The paper's estimand is a **composition effect on the entering population**: conditional on year, trial group and check, how do the traits of varieties entering through a self-organised channel differ from those entering through the unified trial. This is not the effect of moving one variety from one channel to the other, since channel assignment is not random and applicants self-select into it; it is the difference in what each door lets through. We do not estimate, and do not claim, a causal effect of the reform on trait levels, and we do not claim that the reform caused any decline in grain quality — the identification strategy below concerns the *entering population*, not the *time trend*.

The identification argument that makes this composition gap informative rests on where the two trait classes are measured. Grain-processing and appearance quality — head-rice percentage, chalkiness, and the national quality grade — are measured after approval by ministry-designated third-party laboratories under the industry standard NY/T 593, uniformly across channels. Agronomic performance in the regional and production trials — yield and the reported yield gain over the check — is measured by the applicant's own trial organisation when the channel is self-organised. A pure difference in applicant breeding ability predicts that both trait classes move together: weaker applicants would enter with worse quality *and* worse performance. We instead find a sign separation: consortium entrants show 1.84 percentage points lower head-rice percentage, 1.11 points higher chalkiness, and a 12.2-point lower probability of carrying a stated national quality grade (n = 742/739/750) — all third-party-assayed — while the applicant-measured yield gain is, if anything, higher rather than lower. A breeding-ability account cannot generate this pattern; only an account in which the two trait classes are measured by different parties, or the two channels apply different thresholds, can. We report this sign separation as the paper's identification argument, not as a discussion-section aside, and we are explicit that it cannot on its own distinguish measurement discretion from a difference in channel-specific admission thresholds.

This paper makes three contributions.

**First**, it constructs the first record-level trial-channel variable for China's variety approval system, built directly from the wording of official approval announcements rather than from a before/after period indicator. This turns "the 2016 reform" from a single time-varying treatment into an observable, record-level assignment that can be compared within year, trial group and check — the design that Xiang et al. (2025) and Zhao et al. (2022) could not implement without this variable.

**Second**, it turns the coexistence of applicant-measured and third-party-measured traits within the same approval file into an identification argument, rather than a description. The regulatory-economics literature on self-certification has shown, experimentally, that a regulated party's own choice of auditor yields systematically favourable readings of the *same* attribute (Duflo et al., 2013), and that firms endogenously choose certifiers that have previously rated them favourably (Bar and Zheng, 2019). We do not have two measurements of the same attribute; we have two different attributes, measured by two different parties, inside a single document. The sign separation described above is the evidence this design can produce, and we show why a pure applicant-selection account cannot reproduce it on its own.

**Third**, it splits the reform into two treatments that do not overlap in time and shows that pooling them manufactures an average that never occurred: the green channel (2017) and consortium trials (2019–2022) differ in sign on at least one trait (the applicant-measured production-trial yield gain), so estimating them jointly as a single "new channel" would misstate the direction of the underlying gap. Within this design, we use Anhui Winall Hi-Tech Seed Co. — the single largest beneficiary of rising national-approval share among integrated seed enterprises over this period, and a firm the green channel was in principle designed to serve — as a counter-case, not as a source of the main result: it uses the unified trial more, not less, than its peers, which rules out "self-organised entrants are simply weaker firms" as an alternative explanation for the quality gap. This role is deliberately narrow, and the main results do not depend on this firm's records.

This paper's approach — an institutional-economics reading of a Chinese crop-sector regulation, using approval-record text rather than a laboratory or field trial as its evidence base — sits alongside a strand of *Journal of Integrative Agriculture* scholarship on cognate topics: variety-improvement history and germplasm contribution (Shi and Hu, 2017), information asymmetry in farmers' seed-choice behaviour (Qiu et al., 2016), and contract-farming incentive design in Chinese agriculture (Huang et al., 2018). We situate the present paper alongside these three not because they share our method, but because they establish that JIA already publishes exactly this blend of institutional-economics-of-agriculture work on China's seed and farming sectors.

The remainder of the paper proceeds as follows. Section 2 describes the institutional path from the unified regional trial to the green channel and consortium trials, and the quality-testing regime under NY/T 593. Section 3 describes the data and the construction and validation of the channel variable. Section 4 sets out the empirical strategy and states formally what the paper does and does not claim. Sections 5 and 6 report the main results and their robustness. Section 7 examines Winall Hi-Tech as a counter-case. Section 8 discusses the paper's contribution to the literature on self-certification and its policy implications, and Section 9 concludes.

---

# 2. Institutional background

China's variety approval system evaluates candidate crop varieties before they may be marketed as certified seed, and until 2016 the evaluation trial itself was uniformly state-run. Under this arrangement, a candidate variety enters the **unified regional trial** (统一区域试验): a multi-site, multi-year trial organised by the provincial or national variety approval committee, in which every applicant's variety is grown alongside a named check variety under a common protocol. The unified trial remained the only route into approval until a green channel was opened in 2014.

The **green channel** (绿色通道), introduced in 2014, allows certified integrated seed-breeding-production-extension enterprises to organise and run their own regional and production trials for their own candidate varieties, rather than entering the state-run unified trial. In our data the green channel appears concentrated in a single approval year, 2017, before consortium trials became available as an alternative self-organised route.

The 2016 revision of the *Measures for the Administration of Crop Variety Approval* (主要农作物品种审定办法, Order No. 4 of the Ministry of Agriculture, effective 15 August 2016), which superseded the 2001, 2007 and prior 2014 versions, extended self-organised testing further by creating the **consortium trial** (联合体区域试验): a regional trial organised by a consortium of five or more breeders — an enterprise consortium, a science-enterprise consortium, or a consortium of research institutes — rather than by the state trial system. In the approval announcements we parse, consortium-trial records first appear in 2019 and are the dominant self-organised channel from 2019 through 2022, while the green channel and consortium trials barely overlap in time.

Once a candidate variety completes its trial, regardless of which of the three channels produced it, its grain-processing and appearance quality are assessed under a separate, uniform regime. This assessment is not organised by the applicant or by the trial channel: samples are tested by laboratories designated by the Ministry of Agriculture and Rural Affairs, applying the agricultural industry standard **NY/T 593** ("Quality requirements for rice," 优质稻谷), which defines the grading of traits such as head-rice percentage and chalkiness degree and the national or industry quality grade that an approved variety may carry. The channel through which a variety enters — unified trial, green channel, or consortium trial — therefore determines who measures its agronomic performance, but not who measures its grain-processing and appearance quality; the latter is measured by the same designated third-party laboratories under NY/T 593 irrespective of channel.

Two further regulatory changes fall inside or at the edge of our sample window. In 2021, the approval standards for rice and maize were revised to raise the required thresholds for yield, quality and resistance traits; approval volumes for rice fell markedly in the years that followed. Our evidence for the content and date of this revision comes from industry-media reporting rather than a first-hand ministry document, and we flag this lower confidence explicitly. On 1 March 2022, the revised Seed Law took effect — its fourth revision since the law's original 2000 promulgation — establishing an essentially derived variety (EDV) system under which a variety found to be essentially derived from a protected variety may itself be granted a variety right, but its commercial exploitation requires the consent of the original right-holder, and the scope of protection was extended from propagating material to harvested material. On 31 August 2022, the General Office of the Ministry of Agriculture and Rural Affairs issued the *Notice on Strengthening the Management of Green-Channel and Consortium Trials for Major Crop Varieties*, launching a special rectification campaign directed at green-channel and consortium-trial practices. This notice falls at the end of our sample window (2017–2022); we treat it as marking the point after which the identifying variation in trial channel becomes harder to observe in later announcements, without inferring what motivated the notice.

We report these five events — the 2014 green channel, the 2016 Measures establishing consortium trials, the 2021 standard revision, the 2022 EDV provision, and the 2022 special-rectification notice — strictly as a timeline of official actions that preceded or coincided with our sample period. Their sequence motivates the sample window and the two-arm treatment structure used throughout the paper, but we do not draw any inference about regulatory intent from this sequence, and we do not attribute any trend in trait levels to a specific event unless a corresponding structural-break test (Section 6) supports it.

---

# 3. Data

## 3.1 Source and construction of the trial-channel variable

The record-level unit of analysis in this paper is a *variety × ecological trial group*
approval entry. The underlying corpus is a parsed compilation of China's national and
provincial rice variety approval announcements, `analysis_rice_channel.pkl` (6,734
deduplicated records: 2,386 national-level and 4,347 provincial-level, 1999–2025). The
announcements themselves — issued by the Ministry of Agriculture and Rural Affairs (MARA)
and, for provincial approvals, by provincial crop variety approval committees — are the
primary source of every substantive field used in the analysis. We did not access these
announcements directly from MARA's own archive; the text corpus was obtained through a
publicly available third-party aggregation, `he-zhui/Rice_QA` (GitHub), which we re-parsed
with our own regular-expression rules. We are explicit about this two-step provenance
throughout: the data are *MARA variety-approval announcements, obtained through the public
third-party compilation he-zhui/Rice_QA and parsed by the authors*, not a first-hand MARA
data product and not a full official census of approvals (coverage of the compilation
declines sharply after 2022: 85/409 announcements captured for 2023, 61/405 for 2024, and 2
for 2025 — see §3.3). For this reason the number of approved varieties in any given year is
never used as an outcome variable in this paper; it appears only descriptively, with its
coverage caveat attached.

Every element of our identification strategy depends on one feature of the announcement
text that, to our knowledge, no prior study has used: each announcement states, in its
"yield performance" or "characteristics" paragraph, which trial the variety was actually
tested in. We use this to construct a record-level trial-channel variable, `channel`, by
regular-expression matching on the announcement text (after whitespace normalization):
records containing "绿色通道" (green channel) or "自主试验" (self-organised trial) are coded
Green; records containing "联合体" (consortium) are coded Consortium; all remaining records
are coded Unified (the state-run integrated regional trial). `new_channel` collapses Green
and Consortium into a single self-organised indicator, used only for descriptive purposes
(see §4 for why the two channels are estimated as separate treatment arms rather than
pooled). The trial group itself (`trial_group`) is extracted from the surrounding
"participated in [X] regional trial" text and stripped of the year and channel label; the
named check variety (`ck_n`) and the approval year (`approval_year`) are parsed directly
from the same paragraph and from the approval-number field. Parsing succeeded for 100% of
national-level records for `trial_group`, `ck_n`, and `approval_year`; the channel label
itself is unrecoverable for 233 of 234 national records approved in 2018 (99.6%), which we
treat as a documentation-format gap for that year rather than as evidence that self-organised
trials did not exist in 2018 (see the year-by-year channel count by channel, Fig. 1 and
Table 1, and robustness check R4 in §6, which shows the 2018 coding choice is immaterial to
the main estimates).

## 3.2 Sample and stratification

The main analysis stratum restricts to national-level approvals in the two dominant
mid-season indica trial groups — the middle-and-lower Yangtze and the upper-Yangtze
mid-season indica groups — in the years in which the channel variable carries identifying
variation, 2017 and 2019–2022 (2018 is excluded for the reason above; years before 2017 have
no self-organised channel at all and are used only as a pre-reform benchmark, see §4.4 and
§6). This yields **n = 878** records (Unified 406, Consortium 405, Green 67). Because the
green channel is concentrated in 2017 and the consortium channel in 2019–2022, and because
the two barely overlap in time, we split this stratum into two estimation arms rather than
pooling: **Arm 1** (Consortium vs. Unified, 2019–2022, n = 759 before outcome-specific
missingness) and **Arm 2** (Green vs. Unified, 2017, n = 119). Arm 2's identifying variation
comes from only two effective year × trial-group × check cells (a third raw cell contains
only Green records and is dropped for lack of within-cell contrast), so all Arm-2 estimates
use heteroskedasticity-robust (HC1) rather than cluster-robust standard errors and are
flagged as small-sample throughout. An extended stratum that adds every other trial group
(n ≈ 1,020–1,029 for Arm 1, 119–125 for Arm 2) is used as a robustness check on the
two-trial-group restriction (§6, R3); a pre-reform benchmark layer (national approvals in
the same two trial groups, 2005–2016, n ≈ 213) supports the structural-break analysis and
the time placebo; and a provincial-approval layer (2021–2022, new-channel 143 / Unified 318)
supports an external replication check that we report as statistically inconclusive rather
than confirmatory or disconfirmatory (§6, R11).

## 3.3 Outcome variables, measuring party, and missingness

The paper's identification argument turns on a distinction the announcements make
explicit: some fields report performance as measured by a ministry-designated third-party
assay body, and others report performance as measured and submitted by the applicant's own
trial. The main quality outcomes — head-rice percentage (processing quality), chalkiness
degree (appearance quality), and whether the announcement states a national or industry
grain-quality grade — are all assayed by MARA-designated third-party grain-quality
laboratories under the national testing standard NY/T 593; two disease-resistance outcomes
(neck-blast tolerance grade and bacterial-blight grade) are likewise assessed by
ministry-designated resistance-screening units. By contrast, the yield outcomes (two-year
regional-trial yield gain over the named check, production-trial yield gain, and absolute
regional-trial yield) and most agronomic outcomes (growth duration, plant height, seed-set
percentage, thousand-grain weight, grains per panicle) are recorded from the applicant's own
trial. `quality_stated` is coded 1 if the announcement carries either a numeric quality
grade or a named quality standard, and is defined (hence non-missing) for every record by
construction; the two source fields underlying it agree on presence/absence 84.5% of the
time, and we use their union rather than either field alone to match the substantive
definition "the announcement states a quality grade." Because this variable is mechanically
close to a missingness indicator for the underlying grade field, we report it explicitly as
measuring *announcement disclosure behaviour* rather than grain quality itself, and we show
in §6 (R16) that the coefficient survives, and in fact strengthens, once announcement text
length and the count of non-missing fields are controlled for.

Missingness in the main stratum is low and, for most outcomes, balanced across arms: in Arm
1, head-rice percentage is missing for 0.7% of Consortium records and 1.4% of Unified
records, chalkiness for 1.7%/1.4%, and the resistance and grain-composition traits are all
within about two percentage points of balance between arms. Three outcomes are not balanced
and are treated accordingly: the regional-trial yield-gain variable is 99.8% non-missing in
the Consortium arm but only 88.1% in the Unified arm (an 11.6-point gap); the top-two
quality-grade indicator is 77.0% vs. 88.7% non-missing (an 11.7-point gap); and absolute
regional-trial yield is 100% vs. 90.4% non-missing (a 9.6-point gap). For these three we
report Manski worst-case bounds alongside the point estimate (§6, R7) rather than treating
the complete-case estimate as the final word. Arm 2 has a more severe problem for one
outcome: the regional-trial yield-gain field is populated for only 1.9% of Arm-2 Unified
records (1 of 52), so that coefficient is not estimable in this design and is reported as
such rather than as a null result. `applicant_type` (enterprise / public research
institution / joint / unknown), used only in the descriptive comparison in §5 and never as a
channel-gap outcome or control in the main specification, is entirely missing for national
approvals in 2016, 2017, 2018 and 2021 (904 records) because the announcements in those
years do not carry an applicant-institution field; this is a documented structural gap in
the source data, not an artefact of our parsing, and it is why any enterprise-vs.-public
comparison in this paper is confined to years with a non-missing applicant field and is
presented as descriptive rather than causal.

Table 1 reports the year-by-year record counts by channel underlying the sample definition
above, plotted over the full 2005–2022 series alongside the institutional timeline (§2) in
Fig. 1. Table 2 (`manuscript/tables/table2_descriptive_balance.md`) assembles a full
descriptive and balance summary by arm — means, standard deviations, and missing rates — for
all outcome and control variables reported as regression outcomes in Table 3. The main text
retains six figures (Fig. 1–6) and five tables (Table 1–5); the Winall financial panel, the
enterprise-versus-public-institution descriptive comparison, and the missingness-balance
dumbbell plot are reported in the Supplementary Material as Table S1, Table S2, and Fig. S1
respectively (see §7 and §6.1–6.2 for the in-text pointers, and
`submission/supplementary_material.md` for the moved content).

## 3.4 Representativeness and verification

Two representativeness concerns bear directly on how the results should be read. First, the
underlying compilation is a sample of announcements rather than a verified census, with
declining coverage after 2022 (§3.1); we therefore restrict the analysis window to
2017–2022 and treat the post-2022 period only as background evidence that the channel
distinction is currently being narrowed by regulatory action (see §4.4). Second, because the
compilation is a third-party re-transcription of official text rather than the official
record itself, transcription and parsing error are a live concern for any single field.
Cross-checking the parsed corpus against the original MARA announcement text for a
stratified random sample of records — the step needed to report a field-by-field agreement
rate in this Methods section — requires reading the primary announcements directly, which
the present analysis environment could not reach (see `evidence/data/feasibility_notes.md`:
the MARA announcement portal was not reachable from this session's network). This
verification step remains outstanding and is disclosed as such: **the authors will complete
a manual, field-by-field cross-check of a stratified random sample of parsed records against
the original MARA announcements before submission, and will report the resulting agreement
rate in this section; see Unresolved item P4.** No specific agreement-rate figure is reported
here, and none should be inferred or assumed, until that check is done.

---

# 4. Empirical strategy

## 4.1 Two difference-in-differences designs we considered and rejected

Before settling on the specification below, we considered and rejected two
difference-in-differences (DID) designs that would have let us speak in terms of a causal
"effect of the reform," reporting the rejections rather than silently choosing the
specification that worked. The first would have used the switch from provincial to national
approval as a DID shock; its parallel-trends assumption fails in the pre-period for three of
six candidate outcomes (chalkiness +0.515 pp/year, p = 0.006; amylose +0.212, p < 0.0001;
thousand-grain weight −0.130, p = 0.003, all trending differently across administrative
levels well before 2016), so a post-2016 gap would conflate a genuine channel effect with a
pre-existing divergence. The second would have used varying channel exposure across trial
groups as a differential-intensity DID; this fails because channel penetration ranges only
from about 0.33 to 0.63 across trial groups in our sample years, leaving no low-exposure
comparison group to serve as a counterfactual trend. Our design is accordingly not a
difference-in-differences and does not estimate a pre/post treatment effect of the 2016
reform; it is a within-cell cross-sectional comparison, described next.

## 4.2 A record-level trial-channel treatment and the collinearity problem

Reconstructing the trial channel at the level of the individual approval record — rather
than treating the 2016 reform as a single period indicator, as the one existing evaluation of
this reform does (Xiang et al., 2025) — makes
it possible to ask a sharper question: not "did the market change after the reform," but
"does what enters the market differ depending on which door it came through, within the same
year." A naive specification of the form $Y \sim \text{channel} + \text{year} +
\text{trial\_group} + \text{check} + \text{breeding\_system}$ is not estimable as written: the
named check variety is nearly perfectly nested within the trial group (a given trial group in
a given year is compared against only one or two checks), so entering trial group and check
additively produces a rank-deficient design matrix. We resolve this not by dropping one of
the two variables — which would throw away exactly the institutional structure the comparison
needs to hold fixed — but by absorbing the year–trial-group–check hierarchy into a single
interaction fixed effect,

$$c(i) \;=\; \text{Year}_i \times \text{TrialGroup}_i \times \text{Check}_i,$$

which both eliminates the collinearity and sharpens the interpretation of the comparison:
every estimated gap is identified purely from records that were tested in the same year, in
the same ecological trial group, against the same named check. Cells in which only one
channel is observed contribute no identifying variation and are dropped before estimation;
the resulting effective sample sizes are what is reported for each outcome in Table 3.

## 4.3 Main specification and estimator

The main specification is

$$Y_i \;=\; \beta\,\text{NewChannel}_i \;+\; \gamma_{c(i)} \;+\; \delta_{b(i)} \;+\; \varepsilon_i,$$

where $i$ indexes an approval record, $\gamma_{c(i)}$ is the year × trial-group × check
interaction fixed effect defined above, and $\delta_{b(i)}$ is a fixed effect for the
breeding system (two-line hybrid / three-line hybrid / conventional). Standard errors are
clustered at the level of $c$ when an arm has at least five effective clusters; when it does
not (Arm 2's two-trial-group stratum has only three cells), we report heteroskedasticity-
robust (HC1) standard errors instead and flag this explicitly in every table. We estimate the
model separately for the two channels rather than pooling them into a single "new channel"
treatment, because the green channel (2017) and the consortium channel (2019–2022) are
almost non-overlapping in time and, as Table 3 shows, diverge in sign on at least one outcome
(the production-trial yield gain is +0.919 percentage points in the consortium arm but
−1.036 in the green-channel arm). **Arm 1** sets $\text{NewChannel}_i = \mathbb{1}[\text{Consortium}_i]$
on the sample restricted to Unified and Consortium records, 2019–2022; **Arm 2** sets
$\text{NewChannel}_i = \mathbb{1}[\text{Green}_i]$ on the sample restricted to Unified and Green
records, 2017. A pooled specification that combines both channels into one indicator is
reported only as a reference row and is never treated as the paper's headline estimate.

## 4.4 What $\beta$ identifies: a composition effect, not a treatment effect

$\beta$ must be read as a **composition effect on the entering population**: within the same
year–ecology–check cell, how much better or worse, on average, are the varieties that entered
through the self-organised door than the varieties that entered through the state-run
unified-trial door. It is not an estimate of what would happen if a given variety were moved
from one door to the other — that quantity would require either random assignment to channel
or a credible instrument for channel choice, and we have neither. This is nonetheless the
quantity a regulator monitoring the entering population actually needs, and we are careful
never to describe it using the language of *effect of*, *impact of*, or *caused by* in the
title, abstract, or body of the paper.

## 4.5 Identification argument: separating ability from measurement

The paper's central inferential move is to compare two behaviourally distinct classes of
outcome within the same specification. Let $Y^{3rd}$ denote an outcome assayed by a
ministry-designated third party (head-rice percentage, chalkiness degree, whether a quality
grade is stated) and $Y^{self}$ denote an outcome recorded from the applicant's own trial
(regional-trial and production-trial yield gain over the check). Two hypotheses make
different predictions about how $\beta^{3rd}$ and $\beta^{self}$ should relate:

- **$H_{ability}$ (pure breeding-ability difference)**: applicants who choose the
  self-organised channel breed systematically weaker varieties. This predicts
  $\beta^{3rd} < 0$ **and** $\beta^{self} < 0$ — both trait classes deteriorate together,
  because a weaker breeding programme should show up in every trait it touches, whichever
  party measures it.
- **$H_{measure}$ (measurement-authority allocation)**: the two trait classes are measured
  by different parties with different incentives. This predicts $\beta^{3rd} < 0$ **while**
  $\beta^{self} \ge 0$ — a sign separation, because only the third-party-assayed traits are
  insulated from the applicant's own reporting incentives.

The estimates in Arm 1 show exactly the pattern $H_{measure}$ predicts and $H_{ability}$
rules out: $\beta^{3rd}$ is −1.844 percentage points for head-rice percentage (p < 0.0001),
+1.108 for chalkiness degree (p = 0.012), and −0.122 for the probability of a stated quality
grade (p = 0.008), while $\beta^{self}$ is +0.554 for regional-trial yield gain (p = 0.020)
and +0.919 for production-trial yield gain (p < 0.0001) — the self-reported traits do not
deteriorate; if anything they move in the opposite direction. A pure ability-difference story
cannot generate this sign separation: it would need self-organised applicants to be
simultaneously worse breeders (on quality) and better breeders, or at least not worse ones
(on yield), within the same variety. Only an account in which the two trait classes pass
through different measuring parties, or in which the two channels differ in the threshold
they must clear, can produce it. This sign separation is reported here, in the empirical
strategy, and in the abstract — not held back for the Discussion — precisely because it is
the paper's identification argument, not an incidental finding.

We are equally explicit about the limits of this argument. It rules out $H_{ability}$; it
does **not** let us separate $H_{measure}$ from a third hypothesis, $H_{threshold}$ — that the
two channels simply impose different admission thresholds on applicants, independent of how
well any given applicant's variety would perform if it had gone through the other door. Both
$H_{measure}$ and $H_{threshold}$ predict the same sign pattern in this data, and distinguishing
them would require exactly the individual-level, cross-channel variation that our
within-applicant robustness check (§6, R9) shows this sample cannot supply with adequate
power.

## 4.6 Auxiliary specifications

Three auxiliary specifications support the main argument without altering it. A descriptive
specification, $Y_i = \theta\,\text{Public}_i + \gamma_{y \times g} + \delta_b + \varepsilon_i$,
restricted to years with a non-missing applicant-type field, characterizes the enterprise
vs. public-institution trait division of labour; it is reported only as a directional,
descriptive background fact (§4.7, Non-claim 9), not as a structural or causal comparison. A
logit specification, $\Pr(\text{NewChannel}_i) = \Lambda(\alpha\,\text{Winall}_i +
\gamma_{y \times g})$, and a within-channel positioning specification,
$Y_i = \rho\,\text{Winall}_i + \gamma_{c(i)} + \delta_b + \varepsilon_i$ (estimated separately
within the Unified and the self-organised sub-samples), support the counter-case role of a
single large integrated seed enterprise in §7 and are not used to estimate the main channel
gap. An unknown-breakpoint sup-Wald scan (candidate breakpoints 2009–2019, with level-shift
and trend-shift specifications) is used only to test whether the quality trajectory has a
structural break coincident with the 2016 reform (§4.7, Non-claim 3), not to estimate the
channel gap itself.

## 4.7 What this paper does not claim

This paper's estimates support a narrower and more specific set of claims than the pattern
of results might suggest at first reading, and we state the boundaries explicitly here so
that no reader — including the authors, in a later paper — mistakes a composition gap for
something it is not.

1. **$\beta$ is not a causal effect.** It is a within-cell composition gap, not the effect of moving a variety between channels; the only design that could speak to the latter (within-applicant, §6.3) is underpowered by 2–3× on every headline coefficient (full numbers there), so we do not claim to have separated a genuine channel effect from applicant self-selection.
2. **We do not use language of fabrication or manipulation.** Every measurement-authority claim is phrased as *consistent with measurement discretion, though channel self-selection cannot be ruled out*.
3. **We do not claim the 2016 reform caused the quality gap or any quality decline.** The structural-break scan (§5.6) dates the main quality breaks to 2009–2015, before the reform; what we estimate is a same-year channel gap, not a before/after effect.
4. **We do not claim third-party-assayed traits are uniformly worse among self-organised entrants.** Bacterial-blight grade moves the opposite way (§5.2); the headline claim is confined to grain-processing and appearance quality.
5. **We do not claim the self-reported yield advantage is an established finding.** It reverses sign between arms and its Manski lower bound sits near zero (§5.3, §6.2); the abstract accordingly calls it "suggestive only."
6. **We make no welfare claim.** No data on adoption, prices, or consumption exists in this study to support one.
7. **Approval counts are never used as an outcome variable**, only as descriptive background, because underlying compilation coverage declines sharply after 2022 (§3.1).
8. **We do not claim this paper's findings replicate at the provincial level.** The provincial re-estimation is non-significant for three of four headline outcomes and adequately powered and corroborating for the fourth (stated grade); see §6.4 for the full, two-part reading and its own disclosed n discrepancy against an earlier planning-stage run.
9. **We do not claim enterprises are generally better or worse breeders than public institutions.** The enterprise-vs-institution comparison (Supplementary Table S2, §7) is descriptive background only, not least because the applicant-type field is entirely missing for four approval years.
10. **We do not claim Winall's quality-oriented positioning has been a financial success.** §7 reports its negative order-grain margin, 2025 loss, qualified audit opinion and 2026 penalty in the same discussion as its quality advantage; financial sustainability is treated as open.
11. **We do not claim varietal homogenization is increasing or decreasing.** The parentage-diversity and trait-space checks both return null results, reported only as evidence against a common industry narrative.
12. **We do not treat the parsed compilation as an official, complete registry.** Our access is mediated by a third-party compilation whose field-level agreement with original MARA text remains an open verification step (§3.4, Unresolved item P4), not yet an established data-quality guarantee.

---

# 5. Results

## 5.1 Sample and strata

The main analysis layer restricts the record-level approval data to national-level (国审) approvals in the two dominant indica trial groups (middle-and-lower-Yangtze mid-season indica; upper-Yangtze mid-season indica) in the years in which the channel variable actually varies — 2017 and 2019–2022 — yielding **n = 878** records (Unified 406, Consortium 405, Green 67). Because the green channel (2017) and consortium trials (2019–2022) do not overlap in time, we estimate them as two separate arms rather than pooling them into one "new channel" treatment (Section 4.3): **Arm 1** compares Consortium (n = 405) with Unified (n = 354) entrants within 2019–2022 (pre-outcome-drop n = 759, later outcomes ranging n = 520–759 depending on missingness); **Arm 2** compares Green (n = 67) with Unified (n = 52) entrants within 2017 (n = 119, 2–3 identifying cells). Table 3 reports both arms for all 17 outcome variables, split into third-party-assayed (grain-processing and appearance quality, resistance) and applicant-self-reported (yield, agronomic) blocks; Fig. 2 plots the same 34 estimates as a two-panel forest plot, colour-coded by measuring party.

## 5.2 Arm 1: Consortium versus Unified, 2019–2022

Consortium entrants show a consistent, statistically robust deficit on every third-party-assayed grain-processing and appearance trait carried in the main quality block (Table 3; Fig. 2, left panel, blue markers). Head-rice percentage is 1.844 percentage points (pp) lower (95% CI [−2.636, −1.052], p = 5.1 × 10⁻⁶, n = 742); chalkiness degree is 1.108 pp higher, i.e. worse appearance quality (95% CI [0.248, 1.969], p = 0.012, n = 739); and the probability that the announcement states a national/industry-standard quality grade at all (`quality_stated`) is 12.2 pp lower (β = −0.122, 95% CI [−0.211, −0.033], p = 0.008, n = 750). A secondary quality measure restricted to graded records — the probability of being graded 1 or 2, the top two national quality tiers (`quality_top2`) — is also lower by 9.1 pp (p = 0.009, n = 618), though we flag below (Section 6.2) that this coefficient does not survive Manski worst-case bounds and is therefore treated as secondary rather than headline evidence. Gel consistency, a third assayed grain-eating-quality trait not previously highlighted, moves in the same direction (β = −1.814 mm, p = 0.015, n = 728), consistent with the broader pattern of worse third-party-assayed eating and appearance quality among consortium entrants. Amylose content and grain length–width ratio show no significant difference (Table 3), and neck-blast resistance is not estimable for Arm 2 (100% missing in 2017 records; see Section 5.3) but shows no significant Arm 1 gap either (p = 0.28).

Against this, the applicant-self-reported yield-performance traits move in the opposite direction. The two-year regional-trial yield gain over the named check is 0.554 pp *higher* for Consortium entrants (95% CI [0.091, 1.016], p = 0.019, n = 708), and the production-trial (生产试验) yield gain over check is 0.919 pp higher (95% CI [0.505, 1.333], p < 0.0001, n = 578). Raw two-year trial yield in kg/mu (1 kg/mu ≈ 15 kg/hm²; 1 亩 = 1/15 hm²) shows no significant difference (β = +1.43, p = 0.61, n = 716) — consistent with the gain-over-check measures capturing a comparison-scale effect rather than raw yield levels. Two of the three pre-registered placebo traits, seed-setting percentage (β = −0.202, p = 0.43) and 1000-grain weight (β = +0.138, p = 0.59), are both non-significant, as required by the pre-declared design (Section 4, Non-claims). Plant height is 0.952 cm higher (p = 0.044); per the pre-registered methods statement, this is **not** treated as a placebo result but reported as auxiliary evidence consistent with a taller, larger-panicle selection type declared before the analysis was run (Section 6.1, R12, gives the full treatment).

One trait falls outside the sign-separation pattern in a way that itself supports the paper's identification argument rather than undermining it: bacterial-blight grade, also third-party assayed, is 0.190 grades *lower* (i.e. *more* resistant) among Consortium entrants (95% CI [−0.278, −0.102], p < 0.0001, n = 520). This is reported prominently, not hidden, because the paper's claim is deliberately scoped to grain-processing and appearance quality, not to "third-party-measured traits deteriorate uniformly" — a claim the bacterial-blight result would falsify if made (Sections 4.4, 6.2).

## 5.3 Arm 2: Green channel versus Unified, 2017

Green-channel entrants in 2017 (n = 119, HC1 standard errors, 2–3 identifying cells) reproduce the same direction on appearance and grading traits, at larger magnitude: chalkiness degree is 2.809 pp higher (95% CI [1.874, 3.744], p < 0.0001, n = 110) and the probability of a stated quality grade is 34.4 pp lower (β = −0.344, p < 0.0001, n = 112). Head-rice percentage, by contrast, is *not* significantly different in this arm (β = −0.391, p = 0.55, n = 106) — a genuine cross-arm inconsistency that we report rather than smooth over, and one reason the two arms are kept separate.

Two results in Arm 2 diverge from the Arm 1 narrative and are reported here as required, not deferred to a robustness appendix. First, the production-trial yield gain over check is 1.036 pp *lower* for Green-channel entrants (β = −1.036, 95% CI [−1.860, −0.213], p = 0.014, n = 112) — the opposite sign from Arm 1's +0.919 pp. Second, the regional-trial yield gain over check cannot be meaningfully estimated in this arm at all: only 21 of 119 records carry a non-missing value, driven almost entirely by the Unified sub-arm, whose regional-trial-gain coverage in the 2017 stratum is only 1.9% (1 of 52 records; Table 3 reports n = 21, β = −0.994, p = 0.17, but this coefficient should not be interpreted as informative about the underlying population). We flag this explicitly as *not estimable* rather than reporting the numerically available but data-starved coefficient as if it answered the same question as Arm 1's analogous estimate; Fig. 2's right panel marks the corresponding neck-blast row "not estimable" for the same reason (the field is 100% missing for all 119 Arm-2 records). Together, these two results mean that Arm 2 does *not* replicate Arm 1's suggestive yield-advantage pattern, and the paper does not claim that it does.

## 5.4 Identification argument: sign separation against the ability hypothesis

Let $Y^{3rd}$ denote third-party-assayed traits and $Y^{self}$ applicant-measured traits. A pure breeding-ability account of channel choice (H_ability: self-organised-channel applicants simply breed weaker varieties) predicts that both trait classes deteriorate together, $\beta^{3rd} < 0$ *and* $\beta^{self} < 0$. The alternative, that measurement authority itself differs across channels (H_measure), predicts sign separation: $\beta^{3rd} < 0$ while $\beta^{self} \ge 0$. Arm 1's results match the second pattern exactly — third-party head-rice, chalkiness and stated-grade coefficients are negative and highly significant, while self-reported regional- and production-trial yield gains are positive and significant — and H_ability is therefore rejected as the sole explanation. We are explicit, however, that this design cannot distinguish H_measure from a third possibility, that the two channels apply different *entry thresholds* to applicants (H_threshold): both predict the same sign pattern, and separating them would require observing the same variety tested through both channels, which the within-applicant subsample (Section 6.3) is too small to do with any power.

## 5.5 Channel composition and convergence over time

A year-by-year re-estimation of the Arm-1-style channel gap (new channel vs Unified, within `trial_group × check` cells, HC1 standard errors, years in which both channels co-exist: 2017 and 2019–2022; 2018 is excluded because only 1 of 234 national records that year carries a green/consortium label, a parsing default rather than a genuine channel assignment) shows two distinct patterns that must be reported separately rather than summarised as a single "gap is narrowing" story. Chalkiness degree narrows monotonically from +2.71 pp in 2017 (p = 1.1 × 10⁻⁸) to +1.63 (2019, p = 0.004), +0.92 (2020, p = 0.004), +0.89 (2021, p = 0.002) and +0.77 pp in 2022 (p = 0.038) — a genuine, monotonic convergence in this one trait. The stated-quality-grade gap also weakens on balance (from −0.327 in 2017 to −0.052 in 2022) but non-monotonically, with 2020 and 2022 not significant. Head-rice percentage, by contrast, shows **no convergence**: the gap is −0.61 pp in 2017 (not significant) and widens to −2.63 (2020, p = 0.0003), −1.48 (2021, p = 0.021) and −3.03 pp (2022, p = 0.006) — its largest, most significant values occur in the *most recent* years of the sample. The regional-trial yield-gain-over-check coefficient fluctuates around +0.3 to +0.9 pp with no clear convergence or divergence pattern (Fig. 3; full year-by-year coefficients in `table_event_study_by_year.csv`). We therefore do not claim that "the quality gap between channels is closing" as a general statement; only chalkiness, and more weakly the stated-grade indicator, show convergence, while head-rice — arguably the more economically material processing-quality trait — does not.

## 5.6 Structural breakpoints predate the 2016 reform

An unknown-breakpoint (sup-Wald / Quandt) scan over candidate years 2009–2019, run on the full 2005–2022 national two-trial-group layer (n up to 1,204 records depending on trait non-missingness), asks whether the quality traits behind Arm 1's headline result show a structural break coinciding with the 2016 reform that created the consortium and green-channel pathways. They do not. Regional-trial yield per mu shows a clear break at **2017** (peak Wald = 230.3, p < 10⁻⁵⁰, n = 1,167; Fig. 4), consistent with a level shift in absolute yields around when the new channels opened. But the three quality traits central to this paper's argument break *earlier*: head-rice percentage at **2015** (Wald = 73.9, p < 10⁻¹⁶, n = 1,186), chalkiness degree at **2009** (Wald = 22.9, p = 1.1 × 10⁻⁵, n = 1,187), and the top-two quality-grade indicator at **2015** (Wald = 45.5, p = 1.3 × 10⁻¹⁰, n = 845). All three precede the 2016 institutional reform by one to seven years. Yield gain over check shows no robust break: under the paper's default heteroskedasticity-robust (HC1) covariance, the candidate break at 2018 is marginally significant (Wald = 6.55, p = 0.038), but under classical (homoskedastic) standard errors the same candidate year is not significant (Wald = 5.40, p = 0.067), and a diagnostic check shows the non-missing rate of this variable jumps from 21–22% in 2016–2017 to 100% in 2018 — i.e., the 2018 "break" in Wald statistics is confounded with a sudden change in reporting completeness rather than a real trend discontinuity in the underlying trait. We therefore report yield-gain-over-check as showing **no robust structural break**, consistent with a companion finding using classical standard errors, and flag the HC1 result's sensitivity to this covariance choice explicitly rather than reporting only the marginally significant version (Fig. 4; full year-by-year values in `table_breakpoint_scan_full.csv`). Fig. 4 also plots growth duration, a trait we do not otherwise analyse in this paper; its scan peaks at **2018** (Wald = 226.8, p < 10⁻⁴⁹, n = 1,196), close to the absolute-yield break but one year later, and we report this only as background context for the figure rather than as part of the paper's argument, since growth duration is not one of the third-party-assayed quality traits this section is built to falsify a reform-timing story for.

Taken together, these results support a falsification claim rather than a positive dating claim: whatever quality improvement trend is visible in the pre-2016 data was already underway before the reform, so attributing the level of grain-processing and appearance quality in this period to the 2016 reform itself — as opposed to reading the *channel gap conditional on year* reported in Sections 5.2–5.3 — would be a mistaken inference. This paper's estimand is explicitly the latter (the same-year channel gap), and the breakpoint evidence is reported to pre-empt the former misreading. This falsification result also bears on a year-indexed reading of the same corpus: Lu et al. (2024) and Hang et al. (2024) both document long-run quality- and yield-trait trends in Chinese variety-approval records using calendar year as the explanatory variable, without a channel distinction; our break-year estimates (head-rice 2015, chalkiness 2009) sit inside the window their national trend series cover, which is consistent with, though not a direct test of, their finding that these trait trajectories are gradual rather than reform-triggered. The two approaches are complementary rather than competing: a channel-conditional design like ours cannot itself characterise the decades-long trend that a year-indexed design is built to describe, and neither of those papers can distinguish (as this paper's Arm 1/Arm 2 comparison does) whether varieties entering through a given channel in a given year look different from their contemporaries in another channel.

## 5.7 Summary

Table 3 and Fig. 2 present the full set of 17 outcome variables for both arms, including the outcomes that run against the paper's central narrative (bacterial-blight resistance, Arm 2's reversed production-trial yield gain, Arm 2's non-estimable regional-trial yield gain). The pattern that survives across both arms is a consistent, third-party-assayed grain-processing and appearance-quality deficit among self-organised-trial entrants, paired with an applicant-measured yield performance that is, if anything, higher — a sign separation inconsistent with a pure breeding-ability account, but not by itself sufficient to rule out differing entry thresholds across channels. Section 6 subjects this pattern to sixteen pre-registered and one additional robustness checks, several of which qualify or fail to replicate parts of the headline result, and reports all of them.

---

# 6. Robustness, placebos and bounds

This section reports sixteen robustness checks (R1–R16) against the Arm-1 headline results of Section 5 (head-rice −1.844 pp, chalkiness +1.108 pp, stated quality grade −0.122, regional-trial yield gain +0.554 pp, production-trial yield gain +0.919 pp, bacterial-blight grade −0.190; see Table 3 and §5.2 for full CIs, p-values and n). None is moved to an appendix or omitted; where a check does not support the main result, we say so and report the number. Checks that leave the headline pattern essentially unchanged (R1–R6, R8, R10, R12–R14) are reported briefly, with full statistics left in Table 3/Table 4 rather than repeated in prose; checks that qualify or complicate the headline pattern (R7, R9, R11, R15) are given full treatment, since these are the ones a reader needs explained rather than tabulated.

## 6.1 Checks that leave the headline pattern unchanged (R1–R6, R8, R10, R12–R14)

- **R1 (two channels never pooled).** Already established in §5.1–5.3: pooling Arm 1 and Arm 2 would average a +0.919 pp production-trial yield-gain coefficient with a −1.036 pp one, manufacturing a sign that never occurred. Reported only as a reference row (Table 3), never as the headline estimate.
- **R2 (fixed-effects specification).** Re-estimating on the additive, collinearity-prone year + trial-group + check specification (rather than the interaction cell used throughout) reproduces the same signs and comparable magnitudes for all four cross-checked coefficients. Conclusion: the choice of fixed-effects structure is not what drives the result (full numbers: `results_notes_main.md`).
- **R3 (extend to all national trial groups).** Extending from the two dominant indica trial groups to all national trial groups leaves direction and significance essentially unchanged in both arms. Conclusion: not an artefact of the two-trial-group restriction.
- **R4 (2018 treatment).** Coding the 233 unlabelled 2018 records as Unified, instead of excluding them, produces numerically identical point estimates, SEs and p-values to the main design, because every 2018 cell in this stratum is a Unified-only (or one Green-only) singleton carrying no identifying variation either way. Conclusion: the 2018-coding choice is provably immaterial.
- **R5 (Benjamini–Hochberg FDR).** Of 17 Arm-1 outcomes, 8 retain q < 0.05 after BH correction across all 17 tests, including all six headline coefficients; only the top-two quality-grade indicator is borderline (see R7). Conclusion: the sign-separation pattern does not depend on uncorrected multiple testing.
- **R6 (randomisation inference).** Exact permutation p-values (500 draws within each year × trial-group × check cell; Fig. 5) place head-rice, chalkiness and regional-trial yield gain in the extreme tail of their null distributions (RI p = 0.002 each). Conclusion: corroborates the headline results independently of cluster-asymptotic assumptions.
- **R8 (missingness balance).** Supplementary Fig. S1 shows most of the 17 outcomes balanced within ~2 pp of non-missing rate across arms; the three exceptions (top-two grade, regional-trial yield gain, two-year kg/mu yield) are exactly the three that motivate the Manski-bounds exercise (R7, below).
- **R10 (drop the focal firm).** Dropping all Winall-linked records leaves the headline result significant with the same sign: head-rice −1.368 pp (p = 0.006, n = 602), chalkiness +0.940 pp (p = 0.034, n = 599), stated grade −0.104 (p = 0.011, n = 609) (`table_r10_drop_winall_robustness.csv`). Conclusion: the result does not depend on this single firm; see also §7.
- **R12 (pre-declared placebos).** Seed-setting percentage and thousand-grain weight, declared as placebos before estimation, are both non-significant. Plant height was pre-declared *outside* the placebo set and is significantly higher among Consortium entrants (β = +0.952 cm, p = 0.044); this is reported as auxiliary agronomic evidence, not a failed placebo, per the pre-registered design.
- **R13 (pre-reform time placebo).** A pseudo-treatment built the same way in 2005–2016, before any channel existed (using `applicant_type == Enterprise` as the closest available proxy, n = 153, 13 cells), returns no significant coefficient on any of the six outcomes, and the sign is opposite the real design's for both headline quality traits. Conclusion: enterprise-versus-public composition alone, absent real channel variation, does not reproduce the quality-deficit pattern — though this only weakens one specific confound and does not by itself rule out $H_{threshold}$ (§5.4).
- **R14 (cluster by variety).** Re-clustering standard errors at the variety level (36 varieties, 72 records approved in multiple ecological zones) leaves all headline coefficients significant at p ≤ 0.0014. Conclusion: this source of non-independence does not threaten the main inference.

## 6.2 Manski worst-case bounds (R7)

Because four outcome variables show meaningfully unbalanced missingness between arms — the top-two quality grade (23.0% missing in the Consortium arm vs 11.3% in Unified), regional-trial yield gain (0.2% vs 11.9%, and separately the 2017 Unified sub-arm at 1.9%), production-trial yield gain, and two-year trial yield in kg/mu (Supplementary Fig. S1; imbalances ≥ 8 percentage points flagged in orange) — we compute Manski worst-case bounds by filling missing values at the 5th/95th percentile extremes appropriate to each arm. Head-rice percentage and chalkiness degree, whose missingness is balanced (~1–2 pp gap across arms), have narrow, sign-stable bounds ([−2.001, −1.623] and [+0.976, +1.203] respectively) and are treated as the paper's most secure headline results. The top-two quality-grade indicator does **not** survive this test: its worst-case bound is [−0.253, +0.088], which crosses zero — the sign is unstable under worst-case imputation. We therefore explicitly downgrade this variable to a secondary result and rely on the fully defined (0% missing by construction) stated-quality-grade indicator as the primary grading-related headline result (Table 3; Section 5.2). Regional-trial yield gain's worst-case bound is [+0.049, +0.912] — the lower bound is close to zero (p = 0.91 at that bound) — so this coefficient is downgraded from "suggestive support for a positive self-reported advantage" to "directionally positive but not robustly bounded away from zero." No headline third-party-quality result other than the top-two grade indicator changes sign under worst-case bounds.

## 6.3 Within-applicant subsample and its minimum detectable effect (R9)

The most direct test of self-selection versus a genuine channel effect compares the same applicant's own varieties across channels. This subsample is small: 10 applicants, 51 records (26 Consortium, 25 Unified) within the Arm-1 window, estimated with applicant fixed effects (rather than the main year × group × check cell, which is too fine for a sample this size) and HC1 standard errors. None of the six headline coefficients is significant in this subsample, and three (head-rice, chalkiness, stated grade) flip sign relative to the main design (Table: head-rice +0.780, p = 0.61; chalkiness +0.846, p = 0.21; stated grade +0.118, p = 0.40; regional-trial yield gain +0.100, p = 0.86; production-trial yield gain −0.126, p = 0.82; bacterial-blight grade −0.421, p = 0.38).

Rather than reading this as evidence against the main result, we compute the minimum detectable effect (MDE) this subsample could reliably distinguish from zero at 80% power for each outcome: head-rice 4.37 pp, chalkiness 1.96 pp, stated grade 0.41, regional-trial yield gain 1.66 pp, production-trial yield gain 1.56 pp, bacterial-blight grade 1.41. In every case, the MDE exceeds the magnitude of the corresponding main-design coefficient — for head-rice by roughly 2.4×, for regional-trial yield gain by roughly 3×. This converts a qualitative "underpowered" claim into a quantitative one: **this design cannot statistically distinguish "no channel effect once self-selection is removed" from "the channel effect exists, but this subsample is too small to detect it."** The sign flips are consistent with a severely underpowered, noisy estimate rather than a credible contradiction of the main design, but we do not claim the within-applicant test confirms the main effect either — it simply lacks the power to adjudicate the question (Section 4, Non-claims 1).

## 6.4 Provincial replication and its minimum detectable effect (R11)

Provincial-level approvals (省审) in 2021–2022, pooling Consortium and Green under a single new-channel indicator against Unified (cell fixed effect: year × trial group, without the check dimension, because provincial trial-group labels are far more heterogeneous), give a raw sample of n = 495 (new-channel 143, Unified 352). None of the four headline outcomes replicates as significant in the same direction and comparable magnitude as the national result, with one important exception. Head-rice percentage: β = −3.354, p = 0.53, n = 280, MDE = 14.99 pp against a national effect of −1.844 pp — severely underpowered. Chalkiness degree: β = −0.549, p = 0.24, n = 256, MDE = 1.31 pp against a national effect of +1.108 pp — underpowered (and the point estimate's sign is even reversed, though the MDE analysis shows this reversal is not informative). Regional-trial yield gain: β = −0.994, p = 0.62, n = 205, MDE = 5.62 pp against +0.554 pp nationally — underpowered.

**The stated-quality-grade coefficient is the one exception, and it is a new finding from this session's analysis that must be reported rather than omitted:** at n = 495 the provincial sample is adequately powered for this outcome (MDE = 0.41, smaller than the national coefficient's magnitude), and it returns a significant, larger-magnitude, same-direction (negative) coefficient: β = −0.468, p = 0.001. This is the one provincial result that is not simply underpowered, and it is read as strengthening, rather than qualifying, the stated-grade half of the headline result — provincial-level approvals show the same self-organised-channel deficit in whether a quality grade is stated at all, and here the sample has the power to say so with confidence. The correct overall reading of R11 is therefore two-part: for head-rice, chalkiness and yield gain, the national-level effect size is **statistically undecidable** at the provincial level, not disproved by it; for the stated-grade indicator, the provincial result is adequately powered and corroborates the national finding.

We also note, in the interest of full transparency, that the provincial sample size and coefficient values obtained in this run (n = 495, Unified 352) differ from an n = 452 (Unified 318) figure and an earlier head-rice coefficient of −0.134 (p = 0.93) recorded in prior planning notes. The "143" new-channel count matches exactly across both runs; we were unable to exactly reconstruct the earlier run's cell or filter specification from the planning documentation alone. The direction of the finding — provincial-level non-significance for head-rice, chalkiness and yield gain — is identical in both runs, which is what matters for this check's role in the argument, but the discrepancy in point estimates is reported here as an open item rather than silently reconciled.

## 6.5 A chained-check genetic-gain scale as an alternative yield metric (R15)

The reported "percentage gain over the named check" (Section 5.2–5.3) is comparable only within the same trial-year-check cell, so it cannot on its own establish whether the self-reported yield advantage reflects a stable feature of the underlying entrants or an artefact of a shifting comparison scale across years. As a robustness check only, we construct a chained-check index in the spirit of the established genetic-gain literature that separates genetic from non-genetic sources of trend in official variety trials (Piepho et al., 2014; Laidig et al., 2014; Mackay et al., 2011). From the structure of China's approval announcements — mean yield, the named check variety, and the percentage gain over it — we back-solve an implied check-variety yield for each record and link records sharing the same check across adjacent approval years into a step-wise check ladder; where the same check recurs, the discrepancy between independently back-solved yields is our internal-consistency diagnostic, and the year-to-year change along the ladder is our chained estimate of realised genetic gain (Piepho and Laidig, 2024).

We report the diagnostics in full, including those that argue against over-reading this method on Chinese approval-bulletin data. Within the main analysis layer, the coefficient of variation (CV) of the back-solved check yield across records sharing the same check-year cell has a median of 1.56% (90th percentile 3.32%, maximum 5.40%). An independent re-verification using only the fields available in the national rice dataset (`yield_2yr_kg_mu`, `yield_gain_pct`, `ck`, `approval_year`, `region_group`) reproduces the same order of magnitude — median CV of 0.9%–2.4%, 90th percentile roughly 3%–3.6% — but not the reported figures digit-for-digit, since the exact cell construction and backfilled gain variable of the original pipeline cannot be fully recovered from this table alone; we report this discrepancy rather than silently adopting the closer-looking number. A key step in the chain, checked directly against the underlying records, moves by +3.14%, not the +7.04% implied by the decomposition's structural identity — a gap large enough to discourage taking the point estimate at face value. Depending on which years and checks enter the chain, the implied genetic-gain rate swings between 0.25% and 0.50% per year — a two-fold range from a method whose appeal is supposed to be a single defensible number. Finally, because the chain rests on only six distinct check varieties (G = 6), clustering standard errors at the check level yields an effective degrees of freedom of about 3, inflating the standard errors roughly six-fold relative to the naive, unclustered calculation.

Each of these four problems is a known property of check-based genetic-gain estimation, not a defect specific to this dataset: Mackay et al. (2011) and Laidig et al. (2014) both document that estimates are sensitive to the trial series used; Raymond et al. (2023) show directly that check-variety yields are not stable over time and that genetic-gain estimates are highly sensitive to which long-term checks are chosen; and Piepho and Laidig (2024) formalise why a low check-replacement rate and multiple checks per cycle are needed for the chain to be informative — conditions that Chinese approval bulletins, with their small number of checks and irregular replacement, do not meet. Given this, we draw only the following conclusion: even when yield performance is re-expressed on a chained, cross-year check scale rather than the raw within-year percentage-over-check figure, the direction of the applicant-self-reported yield advantage does not reverse, but the resulting interval is too wide to support any precise claim about its magnitude — the chained-scale evidence is inconclusive, not confirmatory or disconfirmatory, of the point estimate reported in Section 5.

## 6.6 `quality_stated` under disclosure-behaviour controls (R16)

Section 3.3 flags `quality_stated` as mechanically close to a missingness indicator for the underlying grade field, and states that we report it as measuring *announcement disclosure behaviour* rather than grain quality itself. This check asks directly whether the Arm-1 coefficient on `quality_stated` is an artefact of some announcements simply being shorter or thinner on detail: we re-estimate the main Arm-1 specification adding two controls, the announcement's raw text length (`source_text_len`) and the count of non-missing fields among the paper's other 16 outcome variables, on the same sample (n = 750, cluster(cell, G = 10)). The baseline coefficient is β = −0.122 (p = 0.0075); with both controls added it is β = −0.146 (p = 0.0005) — the coefficient survives and strengthens in both magnitude and significance, consistent with the direction anticipated in §3.3, though the specific magnitude realised here (−0.146) differs from a −0.169 figure recorded in an earlier planning-stage note and should be read as the number this check actually produces on the data, not as confirmation of that earlier figure (script: `scripts/analysis/robustness_quality_stated_controls.py`). This rules out the simplest version of the "shorter announcements just say less" alternative account of the stated-grade gap.

## 6.7 Robustness matrix

Table 4 collects all sixteen checks (R1–R16) in a single matrix, including the two that qualify a headline result (R7's Manski bound on the top-two quality grade; R11's mostly-underpowered but partly-corroborating provincial replication) and the one that is genuinely underpowered rather than informative either way (R9's within-applicant subsample). Read together with the year-by-year evidence in Section 5.5, this paper's central identification claim — a third-party-assayed grain-quality deficit paired with an unchanged or higher applicant-measured yield performance among self-organised-trial entrants — survives every check that has adequate statistical power to test it (R1–R6, R8, R10, R12–R14, R16), is not reproduced by a pre-reform placebo that shares no real channel variation (R13), and is qualified rather than contradicted by the two checks with genuinely limited power (R9, and three of four outcomes in R11). The one secondary result that does not survive worst-case bounds (top-two quality grade, R7) is explicitly downgraded rather than retained as headline evidence, and the one alternative yield metric explored as an additional check (the chained-check ladder, R15) returns an inconclusive, wide-interval result that neither strengthens nor weakens the main yield-side finding.

---

# 7. Mechanism: Winall Hi-Tech Seed as a counter-case

*Winall enters this paper as a counter-case that rules out an alternative explanation, not as a source of the main result.*

The sign separation reported in Sections 5–6 is consistent with measurement discretion in self-organised trials, but it is equally consistent with a cruder alternative: perhaps seed-marketing enterprises are simply less careful breeders than public research institutes, and the new channels happen to be where enterprises concentrate. If so, the quality gap would reflect *who* enters through each door, not *how* the door is measured. Anhui Winall Hi-Tech Seed Co. lets us test this alternative directly. Winall is the single largest beneficiary of the reform period among integrated seed enterprises — its share of national approvals in the two major indica trial groups rose from 0–12% in 2005–2015 to 23–31% in 2022–2024 — and it is a certified breeding-production-extension enterprise and a Ministry of Agriculture and Rural Affairs "strong-advantage" seed company, the profile the green channel was designed to serve. If enterprises are simply the more careless applicants, Winall should be the entrant that looks *most* like the new channel. Winall's own contract-farming business is separately the subject of Xie et al. (2023), which models the seed enterprise's choice of contract design for its order-grain quality incentives with a three-tier supply-chain game and a numerical example, but at the firm level and without any variety-level data; the order-grain revenue-share and gross-margin figures for 2018 and 2021 reported below (Supplementary Table S1) are drawn from that paper's data rather than from Winall's own disclosures for those two years, and we flag the distinction explicitly here so that this section's variety-level empirical claim is not conflated with Xie et al.'s firm-level contract-theoretic one.

It is not. Restricting to national approvals in 2017 and 2019–2022, Winall-linked records (n = 166) used the unified channel 60.2% of the time, against 47.5% for all other applicants (n = 1,101) (Table 5; Fig. 6a). A logit for channel choice, conditioning on year×trial-group fixed effects, confirms this is not an artefact of when or where Winall applied: being Winall-linked is associated with roughly half the odds of entering through a new channel (α = −0.728, SE = 0.182, p < 0.0001, odds ratio 0.483; robust in magnitude and sign, though somewhat attenuated, under a no-fixed-effects specification and a two-major-trial-group-only sample). Within the unified channel, Winall's own entrants also outperform other unified entrants on the same third-party-assayed traits that define the main result: head-rice percentage +2.212 points, probability of a stated quality grade +9.8 points, chalkiness −0.692 points (all p < 0.001) (Table 5; Fig. 6b). This within-channel advantage is not a general Winall effect, however: repeating the same comparison inside the new-channel subsample, all three coefficients lose significance (p > 0.18 throughout), and the point estimates move toward zero or reverse sign (Fig. 6b). A firm that were simply better at breeding across the board should retain some of this edge wherever its varieties enter; Winall's edge is specific to the channel in which quality is measured by the same third party as everyone else.

This pattern must be read alongside, not instead of, a set of financial facts that are unrelated to which trial channel Winall used but are directly relevant to how the company's overall business should be judged (Supplementary Table S1; Fig. 6c). Winall's order-grain trading segment — its channel for monetising the grain-quality differentiation documented above — ran a gross margin of approximately 2.66% in 2024, falling to about −0.09% in the first half of 2025 and to −1.31% for full-year 2025. The company's 2025 attributable net profit was −212 million CNY, a swing from profit to loss (down 317.91% year on year). Its 2024 annual report received a qualified (非无保留) audit opinion tied to receivables and inventory audit-scope limitations, and in 2026 the company was fined 3,000,000 CNY (RMB 3 million) for under-provisioning credit-impairment losses in that report (10.86% of disclosed profit) and had its stock short name changed to ST Winall, effective 2026-06-30. China Seed Group's partial tender offer for Winall — first announced 2025-11-20, with the tender period running 2025-12-04 to 2026-01-05 and the resulting 40.51% stake reached only after the tender closed, around 2026-01 — places the company's future ownership in flux at the same time. That Winall's varieties measure better on third-party grain-quality traits inside the unified channel, and that its order-grain business is financially troubled, are two separate and simultaneously true facts about the same firm; neither offsets the other, and this section does not convert the quality-grade coefficients above into any implied revenue, processing value, or cost saving for Winall or its comparators.

Dropping every Winall-linked record from the main consortium-versus-unified comparison leaves the headline result intact (Section 6.1, R10; Table 4): head-rice percentage −1.368 pp (p = 0.006, n = 602), chalkiness degree +0.940 pp (p = 0.034, n = 599), and stated quality grade −0.104 (p = 0.011, n = 609). The main result does not depend on this firm.

As descriptive background — not as a conclusion about which type of institution breeds better rice — applicants labelled "public research institute" show higher regional-trial yield (+4.179 kg/mu, SE 1.893, p = 0.027, n = 408) and thousand-grain weight (+1.193 g, SE 0.402, p = 0.003, n = 411) than enterprise applicants, alongside directionally higher chalkiness (+1.010, SE 0.614, p = 0.100, n = 411) and lower head-rice percentage (−1.220, SE 0.673, p = 0.070, n = 411) (Supplementary Table S2). This division of labour runs in the opposite direction from what an "enterprises are careless" account would predict for chalkiness and head-rice, and is silent on causation in either direction; it is reported here only as a background fact, not evidence for or against either institution type. We flag one open item rather than resolving it silently: an earlier planning-stage note for this comparison anticipated a sample of n = 632 records, whereas the regression actually run on `analysis_rice_channel.pkl` for Supplementary Table S2 (Table 7 in the pre-submission working draft) returns n = 408–411 depending on outcome; we were unable to reconstruct the exact filter or sample-construction choice behind the n = 632 figure from the materials available, and record this as an item for the author team to verify against the original coding before submission, rather than adjusting the reported n to match the earlier planning note.

Two scope limits bound what this section argues. First, the comparison is Winall against *all* other applicants pooled together, not against other vertically integrated enterprises specifically; it makes no claim, and should not be read as making one, about how firms rank by degree of integration. Second, "identification argument" is the operative phrase throughout: Winall's channel choice and within-channel positioning rule out one alternative explanation for the sign separation reported elsewhere in the paper — they are not evidence of a causal mechanism linking integration, channel choice, or trial outcome.

---

# 8. Discussion

## 8.1 Contribution to the self-certification literature

Duflo et al. (2013) randomly assigned polluting Indian plants to regulator-paid versus plant-paid auditors and observed the *same* pollution readings diverge systematically — a randomised, same-attribute design this paper cannot match. We observe no randomisation of channel assignment and have no same-attribute comparison; we instead have two *different* attributes, third-party-assayed grain quality and applicant-measured agronomic performance, coexisting in the same approval file. This is a weaker design for the same underlying question — does control over measurement shape what gets reported — but it offers scale and duration a bespoke audit experiment cannot: every one of 2,386 national approval records over six years carries this same self-organised/third-party split.

Bar and Zheng (2019) show that firms endogenously choose certifiers on the basis of geographic proximity and a certifier's history of lenient grading — a self-selection channel our design cannot close off, and the closest existing analogue to the "channel self-selection" alternative flagged throughout this paper (§4; R9/R11), which our within-applicant test lacks the power to rule out. Qiu et al. (2016) offer the theoretical framework closest to this paper's own "who measures what" question, from the demand side: Chinese maize farmers' seed choices are shaped by asymmetric information between sellers and buyers, who rely on imperfect quality signals because they cannot observe quality directly. Our paper documents an analogous asymmetry one stage upstream, at variety approval rather than farmer purchase — the two papers describe the same information problem recurring at different links of the same seed-supply chain.

Grennan and Town (2020) compare medical-device outcomes *across* two regulatory systems (EU, US); our comparison is *within* one system, across two trial pathways a single reform created side by side — narrower but more tightly controlled, since year, ecology and check are held fixed by construction. Renckens and Auld (2022) show private regulatory audits vary in efficiency with auditor incentives and monitoring intensity, a mechanism consistent with, though not directly tested by, our finding that the identification argument rests on where the third party sits relative to the applicant, not on auditor effort per se.

## 8.2 Is the identified variation disappearing? A qualified answer

The Ministry of Agriculture and Rural Affairs has, since 2022, conducted a special rectification campaign targeting the green channel and consortium trials, and this raises the question of whether the gap this paper documents is a closing window rather than a stable feature of the system. The answer is outcome-specific, not uniform, and the two must not be conflated. For chalkiness, a year-by-year re-estimation of the channel gap shows a clear, roughly monotonic decline — from +2.71 percentage points in 2017 to +0.77 in 2022, falling through +1.63, +0.92 and +0.89 in the intervening years — consistent with the gap narrowing as the reform matures and regulatory attention increases. The probability of a stated quality grade shows a weaker, noisier version of the same pattern (largest gap in 2017, smaller and non-monotonic thereafter, non-significant in two of the four post-2017 years). Head-rice percentage does not follow this pattern at all: the year-by-year gap does not narrow over 2019–2022 and if anything widens in the years with the largest samples (−2.63, −1.48 and −3.03 points in 2020, 2021 and 2022), remaining negative and mostly significant throughout. We therefore do not claim that "the identified variation is disappearing" as a blanket statement about the paper's outcomes; that claim holds for chalkiness, holds more weakly for the stated-grade indicator, and does not hold for head-rice percentage, the outcome with the cleanest and most consistent estimate in the paper. Whatever a closing window means for policy, it does not yet mean the head-rice gap has closed, and coverage of official announcements falls sharply after 2022 (85 of an expected 409 records in 2023, 61 of 405 in 2024), so this paper cannot verify whether any of the three outcomes converges further after the window it observes. This outcome-specific pattern is worth reading against the calendar-year trend evidence in Lu et al. (2024) and Hang et al. (2024): where their year-indexed series show gradual, decades-long trait change, our channel-conditional gap shows a mix of convergence (chalkiness) and non-convergence (head-rice) within a six-year window, which suggests the two kinds of trend — the long-run trajectory their design measures and the channel-specific gap ours measures — are not the same object and need not move together.

One further result belongs in this discussion rather than in the robustness section proper. A province-level replication (Section 6) is statistically underpowered, relative to the national-level effect sizes, for head-rice percentage, chalkiness and self-reported yield gain — the minimum detectable effect at 80% power exceeds the national coefficient for all three, so their non-significance at the provincial level should be read as "undetermined," not as evidence against the national result. The stated-quality-grade indicator is the exception: the provincial sample is adequately powered for this outcome, and it returns a coefficient that is significant (β = −0.468, p = 0.001), larger in magnitude than, and in the same direction as, the national result. We report this because it runs against a common but incorrect reading of provincial null results in this literature, and because Non-claim 8 in the design stage of this project anticipated only a null and did not anticipate a significant, adequately powered result on this one outcome; the provincial evidence should be described precisely — one outcome significant and adequately powered, three underpowered — not summarised as either "confirms" or "does not replicate."

## 8.3 Policy implications

Three implications follow without extending beyond what the data show. First, the identification argument rests on an asymmetry: third-party assay covers grain-processing and appearance quality but not the agronomic-performance traits measured in the applicant's own regional and production trials. Extending independent, ministry-designated measurement to a subset of yield and performance traits — even a periodic spot-check rather than universal coverage — would let regulators test directly whether the sign separation this paper documents in observational data also appears when performance itself is measured by an independent party. Second, an audit-style re-verification of a random sample of self-organised trial results, analogous in spirit to the spot-checks the Ministry has run against the green channel and consortium trials since 2022, would generate exactly the kind of within-attribute comparison that Duflo et al. (2013) had and this paper does not; such spot-checks are already the Ministry's own initiative, and this paper's finding is best read as an independent, quantitative corroboration of the direction that 2022-08-31 rectification notice already took, not as a claim that regulators were unaware of the pattern. Third, the channel-of-entry information already exists inside every approval announcement but is not compiled or published as a standalone field; publishing it directly, rather than leaving it to be reconstructed by text-parsing as this paper did, would let downstream users of the seed catalogue — processors, distributors, other researchers — condition on it themselves.

## 8.4 Limitations

Five limitations bound this paper's scope. The evidence covers a single country and a single crop (rice); whether the same channel-measurement asymmetry appears in other crops or seed-regulation regimes is untested here. Channel self-selection cannot be fully separated from measurement discretion with the data at hand — the within-applicant comparison in Section 6 is directionally uninformative because it is underpowered, not because it rules out self-selection. The `applicant_type` field needed for the enterprise-versus-institute comparison in Section 7 is entirely missing for the 2016, 2017, 2018 and 2021 approval cohorts, which limits that comparison to years with non-missing labels and to the two major trial groups. The underlying announcement compilation is not an official, complete registry of all approvals; it is a secondary compilation of Ministry announcements, and its completeness was checked against a 50-record manual audit rather than assumed. Finally, the analysis window runs through 2022 because compiled announcement coverage falls sharply afterward; this paper accordingly cannot speak to whether the convergence trends documented in Section 8.2, or the divergent trend in head-rice percentage, continue, reverse, or stabilise after 2022.

---

# 9. Conclusion

China's 2016 reform of variety approval did not just change how many rice varieties reach the market through self-organised trials; by parsing which trial each variety actually passed through, we show it changed what those varieties look like on the traits that a third party, rather than the applicant, measures — worse third-party-assayed grain-processing and appearance quality among self-organised entrants, alongside applicant-measured performance that is unchanged or higher, a sign separation that a simple breeding-ability story cannot produce and that survives dropping the single largest beneficiary firm from the sample.

This finding is a composition effect on the population of varieties entering under each trial pathway, not a causal effect of channel assignment on any individual variety, and should not be read more broadly. It does not speak to farmer welfare, extension outcomes, or seed prices; it does not allege fabrication or manipulation of any applicant's trial results, a possibility the data cannot distinguish from channel self-selection or differing admission thresholds; and it does not extend to every third-party-measured trait or every level of government, since disease-resistance grading moves the other way and the provincial replication is conclusive for only one of four outcomes. Within these bounds, the contribution is narrow: a record-level channel variable, built from the text of approval announcements rather than a before/after indicator, that lets who measures what be observed directly — and shows that this, not only the volume of entrants, changed after 2016.

---

## Acknowledgements

[Author to complete: funding sources, reviewer thanks, etc.]

---

## Conflict of interest

The authors declare no conflict of interest.

---

## Data availability statement

The variety-approval text corpus underlying this study was compiled from publicly available Ministry of Agriculture and Rural Affairs announcements via a third-party aggregation (see Methods). Parsing scripts, the field dictionary, and the list of approval-record identifiers used in the analysis are available at [repository link]. Due to the unresolved licensing status of the upstream aggregation, the full parsed dataset is not redistributed; researchers can reconstruct it from the cited public announcements using the provided scripts.

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

Not applicable. This study did not involve human participants or animal experiments; it uses only publicly available government variety-approval announcements and publicly disclosed company financial filings.

---

# References

Bar T, Zheng Y. 2019. Choosing certifiers: Evidence from the British Retail Consortium food safety standard. American Journal of Agricultural Economics, 101, 74–88.

Duflo E, Greenstone M, Pande R, Ryan N. 2013. Truth-telling by third-party auditors and the response of polluting firms: Experimental evidence from India. Quarterly Journal of Economics, 128, 1499–1545.

Gong J, Zhang X, Zhang J, Zeng B, Zhang X, Xu X, Xie H A. 2026. Three-line hybrid rice in China: sustained improvements in yield, quality, and resistance over fifty years. Rice Science. (title-level citation only; full text not accessible at time of writing, no specific figures attributed)

Grennan M, Town R J. 2020. Regulating innovation with uncertain quality: Information, risk, and access in medical devices. American Economic Review, 110, 120–161.

Hang S, Wang Q, Wang Y, Xiang H. 2024. Evolution of rice cultivar performance across China: A multi-dimensional study on yield and agronomic characteristics over three decades. Agronomy, 14, 2780.

Huang Z Y, Xu Y, Zeng D, Wang C, Wang J M. 2018. One size fits all? Contract farming among broiler producers in China. Journal of Integrative Agriculture, 17, 473–482.

Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. Theoretical and Applied Genetics, 127, 2599–2617.

Lu Y, Tang Y, Zhang J, Liu S, Liang X, Li M, Li R. 2024. Variations and trends in rice quality across different types of approved varieties in China, 1978–2022. Agronomy, 14, 1234.

Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. Theoretical and Applied Genetics, 122, 225–238.

Piepho H-P, Laidig F. 2024. How many checks are needed per cycle in a plant breeding or variety testing programme? Plant Breeding.

Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. Theoretical and Applied Genetics, 127, 1009–1018.

Qiu H G, Wang X B, Zhang C P, Xu Z G. 2016. Farmers' seed choice behaviors under asymmetrical information: Evidence from maize farming in China. Journal of Integrative Agriculture, 15, 1915–1923.

Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. Field Crops Research, 303, 109086.

Renckens S, Auld G. 2022. Time to certify: Explaining varying efficiency of private regulatory audits. Regulation & Governance, 16, 500–518.

Shi X, Hu R. 2017. Rice variety improvement and the contribution of foreign germplasms in China. Journal of Integrative Agriculture, 16, 2337–2345.

Xiang C, Yang R, Wang X, Huang J. 2025. Impact of seed regulation reform on licensing fees of varieties in China. Agribusiness.

Xie Z, Yuan S, Zhu J, Li W. 2023. Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? Agribusiness, 39, 1173–1198.

Zhao Y, Deng H, Hu R, Xiong C. 2022. Impact of government policies on seed innovation in China. Agronomy, 12, 917.
