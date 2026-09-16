# Rice variety approval records as an innovation indicator source: trial channel, third-party-assayed grain quality, and who measures what enters the market in China, 2017–2022

*Running title:* Trial channel and third-party grain quality in Chinese rice approvals

**Authors:** [Author(s) to complete — given name and surname, in submission order]

**Affiliations:** [Author(s) to complete. Note: the first author's affiliation must be the
S&T information/intelligence institute, listed first, to satisfy the first-affiliation
requirement.]

**Corresponding author:** [name, postal address, e-mail, ORCID]

---

## Abstract

Official rice variety-approval announcements record who tested a variety and what a third party measured, but the trial channel they name has never been extracted as an analysable field. We mine China's rice variety-approval announcements into a record-level indicator system (2,386 records, 17 fields) and extract an unused element: each variety's trial channel. China's 2016 approval reform let seed firms and breeder consortia run their own trials, but no prior study observes the channel, so none can tell whether what enters the market changed. We compare self-organised with unified-trial entrants within the same approval year, ecological trial group and named check, estimating the green channel (2017) and consortium trials (2019–2022) separately since they do not overlap in time. Consortium entrants show 1.84 percentage points lower head-rice percentage, 1.11 points higher chalkiness, and a 12.2-point lower probability of carrying a stated national quality grade, all third-party-assayed, while the yield advantage recorded in the applicant's own trial is, if anything, higher (+0.55 points, suggestive only); green-channel entrants likewise show higher chalkiness. This sign separation is the identification argument: a breeding-ability account predicts both trait classes deteriorate together, whereas only third-party grain quality does. Results survive worst-case bounds, randomisation inference, and dropping the most prevalent breeding lineage. Bacterial-blight grades are better among self-organised entrants, which bounds the composition effect. The wider point is that evidence strength can differ across fields of one official source according to who measured each field, so approval indicators should be read field by field.

---

## Keywords

rice variety approval; grain quality; trial channel; data provenance; administrative text mining; China

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

Observing that split requires a field nobody has extracted. Approval announcements have been read at scale before — we discuss two such studies below — but always as year-indexed trait series, because the announcements are running prose and yield their contents only to whatever parsing a given study happens to need. Innovation measurement more broadly rests on a few curated indicator families, and its text-mining methods were developed over patent and publication corpora (Losiewicz et al., 2000; Antons et al., 2020) rather than over the regulatory record (Rammer and Es-Sadki, 2023). A single variety-approval record carries the applicant, the trial the variety was tested in, the named check it was compared against, and more than a dozen measured agronomic, grain-quality and resistance fields — each, crucially for what follows, with an identifiable measuring party. Our first contribution is to parse that structure into a record-level indicator system carrying the trial channel, and our second is to show what it reveals once the fields are separated by who measured them.

This question has not been answered because it has not been asked in a form the data could answer. The two studies that evaluate this same reform, Xiang et al. (2025) and Zhao et al. (2022), both code the reform as a *period* variable — before versus after 2016 — applied to licensing-fee data and to national approval panels, respectively. Xiang et al. (2025) find that licensing fees for hybrid rice varieties are not significantly affected by the reform; Zhao et al. (2022) trace policy variables against approved-variety trait trends over time. Neither paper observes which trial a given variety actually passed through, so neither can distinguish a change in *how much* enters the market from a change in *what* enters it. A null effect on price, in particular, is silent on whether the composition of entering varieties shifted. This is the gap: no existing study has a record-level channel variable to test whether self-organised and state-run entrants differ in what they bring to market.

A related but distinct literature reads approved-variety trait trends by *calendar year*. Lu et al. (2024) classify the quality-trait trajectory of 17,785 nationally and provincially approved varieties from 1978–2022, and Hang et al. (2024) track yield and agronomic-trait evolution across 11,811 regional-trial entries from 1990–2023; both papers read the same kind of approval-trial record we use, but neither carries a variable for which trial organised the test, so both attribute trait change to *when* a variety was approved rather than to *which door* it entered through. This paper's structural-break analysis (§5.5) and the "closing window" discussion (§8.2) speak to the same substantive object — the trajectory of quality and yield traits in China's approval records — but ask a channel-conditional question that a year-indexed reading cannot: whether the pre-2016 quality trend Lu et al. (2024) and Hang et al. (2024) document already contains the same channel a variety passed through, or whether it is orthogonal to channel altogether. A recent title-level review of fifty years of three-line hybrid rice trends (Gong et al., 2026) situates this same trait trajectory over a longer horizon; because the full text of that review was not accessible to us at the time of writing, we cite it only for its scope and do not attribute any specific figure to it.

We close this gap using a feature of the official approval announcements that has not previously been exploited: each announcement states, in its own text, the name of the trial in which the variety was tested — the unified regional trial, the green channel, or a named consortium trial. Parsing this text lets us assign every approval record to a channel and compare self-organised entrants with unified-trial entrants within the same approval year, the same ecological trial group, and the same named check variety. Because the green channel is concentrated in a single year (2017) and consortium trials begin only in 2019, the two channels barely overlap in time; we treat them as two separate treatments rather than pooling them into one "new channel."

The paper's estimand is a **composition effect on the entering population**: conditional on year, trial group and check, how do the traits of varieties entering through a self-organised channel differ from those entering through the unified trial. This is not the effect of moving one variety from one channel to the other, since channel assignment is not random and applicants self-select into it; it is the difference in what each door lets through. We do not estimate, and do not claim, a causal effect of the reform on trait levels, and we do not claim that the reform caused any decline in grain quality — the identification strategy below concerns the *entering population*, not the *time trend*.

The identification argument that makes this composition gap informative rests on where the two trait classes are measured. Grain-processing and appearance quality — head-rice percentage, chalkiness, and the national quality grade — are measured after approval by ministry-designated third-party laboratories under a published grain-quality standard (NY/T 593 through most of the window, GB/T 17891 in 2017), uniformly across channels within any given year. Agronomic performance in the regional and production trials — yield and the reported yield gain over the check — is measured by the applicant's own trial organisation when the channel is self-organised. A pure difference in applicant breeding ability predicts that both trait classes move together: weaker applicants would enter with worse quality *and* worse performance. We instead find a sign separation: consortium entrants show 1.84 percentage points lower head-rice percentage, 1.11 points higher chalkiness, and a 12.2-point lower probability of carrying a stated national quality grade (n = 742/739/750) — all third-party-assayed — while the applicant-measured yield gain is, if anything, higher rather than lower. A breeding-ability account cannot generate this pattern; only an account in which the two trait classes are measured by different parties, or the two channels apply different thresholds, can. We report this sign separation as the paper's identification argument, not as a discussion-section aside, and we are explicit that it cannot on its own distinguish measurement discretion from a difference in channel-specific admission thresholds.

This paper makes three contributions.

**First**, it builds an S&T intelligence extraction pipeline over a previously unstructured administrative corpus and, from it, the first record-level trial-channel variable for China's variety approval system — a variable read directly from the wording of official approval announcements rather than imposed as a before/after period indicator. This turns "the 2016 reform" from a single time-varying treatment into an observable, record-level assignment that can be compared within year, trial group and check — the design that Xiang et al. (2025) and Zhao et al. (2022) could not implement without this variable. The same pipeline yields a 17-field indicator set in which each field is labelled by its measuring party, which is what makes the second contribution possible.

**Second**, it turns the coexistence of applicant-measured and third-party-measured traits within the same approval file into an identification argument. We do not have two measurements of the same attribute, as the randomised self-certification literature does (Duflo et al., 2013; Bar and Zheng, 2019); we have two different attributes, measured by two different parties, inside a single document. That literature supplies the interpretation of the pattern we find — reported values reflect who was asked to measure — but not the paper's frame, which is the reliability structure of an official data source. The sign separation described above is the evidence this design can produce, and we show why a pure applicant-selection account cannot reproduce it on its own.

**Third**, it splits the reform into two treatments that do not overlap in time and shows that pooling them manufactures an average that never occurred: the green channel (2017) and consortium trials (2019–2022) differ in sign on at least one trait (the applicant-measured production-trial yield gain), so estimating them jointly as a single "new channel" would misstate the direction of the underlying gap. Within this design, we build a second indicator from the same announcements — germplasm concentration across parental lines resolved from the variety-source field — and use it as a counter-case rather than as a source of the main result: consortium entrants draw on a significantly broader sterile-line base than the unified entrants they are compared against, so a narrower breeding base cannot explain their quality deficit. This role is deliberately narrow, and no analysis in the paper is conducted at the level of a named organisation.

The remainder of the paper proceeds as follows. Section 2 describes the institutional path from the unified regional trial to the green channel and consortium trials, and the third-party quality-testing regime. Section 3 describes the intelligence-extraction pipeline, the data it produces, and the construction and validation of the channel variable. Section 4 sets out the empirical strategy and states formally what the paper does and does not claim. Sections 5 and 6 report the main results and their robustness. Section 7 tests a germplasm-concentration counter-case. Section 8 discusses the paper's implications for S&T intelligence practice, its relation to the self-certification literature, and its policy implications; Section 9 concludes.

---

# 2. Institutional background

China's variety approval system evaluates candidate crop varieties before they may be marketed as certified seed, and until 2016 the evaluation trial itself was uniformly state-run. Under this arrangement, a candidate variety enters the **unified regional trial** (统一区域试验): a multi-site, multi-year trial organised by the provincial or national variety approval committee, in which every applicant's variety is grown alongside a named check variety under a common protocol. The unified trial remained the only route into approval until a green channel was opened in 2014.

The **green channel** (绿色通道), introduced in 2014, allows certified integrated seed-breeding-production-extension enterprises to organise and run their own regional and production trials for their own candidate varieties, rather than entering the state-run unified trial. In our data the green channel appears concentrated in a single approval year, 2017, before consortium trials became available as an alternative self-organised route.

The 2016 revision of the *Measures for the Administration of Crop Variety Approval* (主要农作物品种审定办法, Order No. 4 of the Ministry of Agriculture, effective 15 August 2016), which superseded the 2001, 2007 and prior 2014 versions, extended self-organised testing further by creating the **consortium trial** (联合体区域试验): a regional trial organised by a consortium of five or more breeders — an enterprise consortium, a science-enterprise consortium, or a consortium of research institutes — rather than by the state trial system. In the approval announcements we parse, consortium-trial records first appear in 2019 and are the dominant self-organised channel from 2019 through 2022, while the green channel and consortium trials barely overlap in time.

Once a candidate variety completes its trial, regardless of which of the three channels produced it, its grain-processing and appearance quality are assessed under a separate, uniform regime. This assessment is not organised by the applicant or by the trial channel: samples are tested by laboratories designated by the Ministry of Agriculture and Rural Affairs, applying a published grain-quality standard — the agricultural industry standard **NY/T 593** (《食用稻品种品质》, "Cooking rice variety quality"), which grades records through most of our window, or the national standard **GB/T 17891** (《优质稻谷》, "High-quality paddy"), which predominates in 2017 — each of which defines the grading of traits such as head-rice percentage and chalkiness degree and the national or industry quality grade that an approved variety may carry. The channel through which a variety enters — unified trial, green channel, or consortium trial — therefore determines who measures its agronomic performance, but not who measures its grain-processing and appearance quality; the latter is measured by the same designated third-party laboratories under NY/T 593 irrespective of channel.

Two further regulatory changes fall inside or at the edge of our sample window. In 2021, the approval standards for rice and maize were revised to raise the required thresholds for yield, quality and resistance traits; approval volumes for rice fell markedly in the years that followed. Our evidence for the content and date of this revision comes from industry-media reporting rather than a first-hand ministry document, and we flag this lower confidence explicitly. On 1 March 2022, the revised Seed Law took effect — its fourth revision since the law's original 2000 promulgation — establishing an essentially derived variety (EDV) system under which a variety found to be essentially derived from a protected variety may itself be granted a variety right, but its commercial exploitation requires the consent of the original right-holder, and the scope of protection was extended from propagating material to harvested material. On 31 August 2022, the General Office of the Ministry of Agriculture and Rural Affairs issued the *Notice on Strengthening the Management of Green-Channel and Consortium Trials for Major Crop Varieties*, launching a special rectification campaign directed at green-channel and consortium-trial practices. This notice falls at the end of our sample window (2017–2022); we treat it as marking the point after which the identifying variation in trial channel becomes harder to observe in later announcements, without inferring what motivated the notice.

We report these five events — the 2014 green channel, the 2016 Measures establishing consortium trials, the 2021 standard revision, the 2022 EDV provision, and the 2022 special-rectification notice — strictly as a timeline of official actions that preceded or coincided with our sample period. Their sequence motivates the sample window and the two-arm treatment structure used throughout the paper, but we do not draw any inference about regulatory intent from this sequence, and we do not attribute any trend in trait levels to a specific event unless a corresponding structural-break test (Section 5.5) supports it.

---

# 3. Data and the intelligence-extraction pipeline

Because the corpus underlying this paper is an unstructured administrative text collection,
the Data section doubles as a methods section for the
extraction itself. We set it out as a six-step S&T intelligence pipeline, and flag each step
where it occurs below: (i) **intelligence-source identification** — recognising variety-approval
announcements as a high-density, record-level innovation corpus, and the trial-channel
statement inside them as an extractable element (§3.1); (ii) **corpus acquisition** — obtaining
the announcement text and documenting its two-step provenance (§3.1); (iii) **field extraction**
— a regular-expression rule set that converts each announcement's running prose into typed
fields (§3.1); (iv) **entity recognition and disambiguation** — resolving the free-text
variety-source field into the parental-line entities of the originating cross, with a
reported resolution rate and a per-channel coverage check (§3.1); (v) **field-coverage and data-quality
assessment** — per-field parse rates, missingness by arm, structural gaps in the source, and the
outstanding cross-check against the primary announcements (§3.3–§3.4); and (vi) **indicator
construction** — assembling the parsed fields into the 17 analysis variables, each labelled by
its measuring party, and defining the strata over which they are compared (§3.2–§3.3). Steps
(i)–(iv) are what a reader wanting to reproduce the corpus needs; step (v) is what a reader
wanting to judge how far to trust any individual field needs, and we report it at field level
rather than as a single corpus-wide quality statement, for reasons the paper's main result
makes concrete.

## 3.1 Intelligence source, corpus acquisition, field extraction and entity resolution (steps i–iv)

The record-level unit of analysis in this paper is a *variety × ecological trial group*
approval entry. The underlying corpus is a parsed compilation of China's national and
provincial rice variety approval announcements (6,734
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
for 2025 — see §3.4). For this reason the number of approved varieties in any given year is
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
(see §4 for why the two channels are estimated as separate treatment arms). The trial group itself (`trial_group`) is extracted from the surrounding
"participated in [X] regional trial" text and stripped of the year and channel label; the
named check variety (`ck_n`) and the approval year (`approval_year`) are parsed directly
from the same paragraph and from the approval-number field. Parsing succeeded for 100% of
national-level records for `trial_group`, `ck_n`, and `approval_year`; the channel label
itself is unrecoverable for 233 of 234 national records approved in 2018 (99.6%), which we
treat as a documentation-format gap for that year rather than as evidence that self-organised
trials did not exist in 2018 (see the year-by-year channel count by channel, Fig. 1 and
Table 1, and robustness check R4 in §6, which shows the 2018 coding choice is immaterial to
the main estimates).

Step (iv) of the pipeline, entity recognition and disambiguation, resolves the free-text
variety-source field into the two parental lines of the originating cross. Announcements
record that cross in a recurring but unnormalised form — female (sterile) line, a separator
that varies between several typographic conventions, then the male (restorer) line — and
frequently continue into the parents' own ancestry. We therefore take only the first cross,
which gives the variety's immediate parents, and normalise the separator and the quotation
marks that often enclose line names, together with the several conventions the announcements
use for the cross symbol itself and for hyphens inside line names. The rule resolves 2,304 of
2,386 national records (96.6%) into two parental-line entities. The 3.4% that do not resolve
are of three kinds: multi-parent pedigrees written with a double slash, where no single
immediate cross is defined; varieties derived by mutagenesis or selection from an existing
variety, which record no cross at all; and a small number of records using symbols the rule
does not cover. These are excluded from the concentration indicator rather than imputed.

Reporting the failure rate is not a formality. An earlier version of this rule handled only
the common typographic conventions, and its failures were **channel-correlated** —
green-channel records failed at 8.0% against the unified channel's 2.3% — which would have
biased the Arm-2 comparison in §7 without any visible symptom. Under the current rule,
extraction coverage is 99.7–100% in all four channel-by-arm groups (Table 5), so differential
parsing failure cannot drive the contrasts we report. We state this because an
entity-resolution rule whose failure profile is not reported is not auditable by anyone
re-using the pipeline, and because unbalanced extraction failure is the specific way this kind
of indicator goes wrong.

Parental-line names are themselves an entity-resolution problem, since a line may be written
with or without its breeder prefix. We normalise whitespace and quotation marks but do not
merge differently spelled names, which is the conservative choice for a concentration
measure: unmerged variants inflate the distinct-line count and depress the Herfindahl index,
so the concentration **levels** we report are lower bounds. We make no claim about the
direction in which this biases the between-channel **contrast**, since that would require
knowing that variant-splitting rates are equal across channels, which we have not established.

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

The single most consequential step in the pipeline is the one that attaches a **measuring
party** to each extracted field. A conventional data-quality assessment asks how complete and
how accurately transcribed a source is; here we additionally ask, field by field, *who
generated the number the source reports*, and treat that as a dimension of field reliability on
a par with coverage. The paper's identification argument turns on a distinction the
announcements make explicit: some fields report performance as measured by a ministry-designated third-party
assay body, and others report performance as measured and submitted by the applicant's own
trial. The main quality outcomes — head-rice percentage (processing quality), chalkiness
degree (appearance quality), and whether the announcement states a national or industry
grain-quality grade — are all assayed by MARA-designated third-party grain-quality
laboratories under the applicable grain-quality standard (NY/T 593 or GB/T 17891, see §2); two disease-resistance outcomes
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
report Manski worst-case bounds alongside the point estimate (§6, R7). Arm 2 has a more severe problem for one
outcome: the regional-trial yield-gain field is populated for only 1.9% of Arm-2 Unified
records (1 of 52), so that coefficient is not estimable in this design and is reported as
such rather than as a null result. `applicant_type` (enterprise / public research
institution / joint / unknown), used only in the descriptive comparison in §7 and never as a
channel-gap outcome or control in the main specification, is entirely missing for national
approvals in 2016, 2017, 2018 and 2021 (904 records) because the announcements in those
years do not carry an applicant-institution field; this is a documented structural gap in
the source data, not an artefact of our parsing, and it is why any enterprise-vs.-public
comparison in this paper is confined to years with a non-missing applicant field and is
presented as descriptive rather than causal.

Table 1 reports the year-by-year record counts by channel underlying the sample definition
above, plotted over the full 2005–2022 series alongside the institutional timeline (§2) in
Fig. 1. Table 2 assembles a full
descriptive and balance summary by arm — means, standard deviations, and missing rates — for
all outcome and control variables reported as regression outcomes in Table 3. The main text
retains six figures (Fig. 1–6) and five tables (Table 1–5); the enterprise-versus-public-institution
descriptive comparison and the missingness-balance dumbbell plot are reported in the
Supplementary Material as Table S1 and Fig. S1 respectively (see §7 and §6.1–6.2 for the
in-text pointers, and the Supplementary Material for the moved content).

## 3.4 Representativeness and source verification (step v)

Two representativeness concerns bear directly on how the results should be read. First, the
underlying compilation is a sample of announcements rather than a verified census, with
declining coverage after 2022 (§3.1); we therefore restrict the analysis window to
2017–2022 and treat the post-2022 period only as background evidence that the channel
distinction is currently being narrowed by regulatory action (see §8.2). Second, because the
compilation is a third-party re-transcription of official text rather than the official
record itself, transcription and parsing error are a live concern for any single field. This
is not a peculiarity of our source: large-scale audits of the databases on which S&T
indicators are routinely built find systematic, non-negligible error rates in them as well
(Franceschini et al., 2016), and the appropriate response is to state the verification status
of a corpus.
One verification step that would ordinarily belong here has not been carried out, and we
state this plainly. **We have not cross-checked the
parsed corpus field by field against the original MARA announcement text, and we therefore
report no transcription agreement rate.** Doing so requires consulting the primary
announcements directly, which was not possible with the access available to us. Every
quantity in this paper is accordingly conditional on the compilation transcribing the
announcements faithfully — an assumption we rely on but have not independently confirmed,
and one a replicator with access to the primary announcements could test directly. We note
below (§8.5) that this is the single most consequential unverified assumption in the study.

---

# 4. Empirical strategy

## 4.1 Two difference-in-differences designs we considered and rejected

Before settling on the specification below, we considered and rejected two
difference-in-differences (DID) designs that would have let us speak in terms of a causal
"effect of the reform." We report both rejections here. The first would have used the switch from provincial to national
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
outcome within the same specification. It is worth being explicit that this move is also
the paper's methodological claim in operation, not merely an application of it: we are
treating *who measured a field* as a property of the field rather than of the source, and
partitioning the outcome set on it before estimating anything. Every field below comes from
the same announcement, issued by the same authority on the same date, so a source-level
data-quality judgement — the kind ordinarily made about an official corpus — cannot
distinguish them. The identification argument therefore depends on the provenance partition
being real, and the general lesson we draw in §8.4 is nothing more than this section's
premise stated in the abstract. Let $Y^{3rd}$ denote an outcome assayed by a
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
grade (p = 0.008), while $\beta^{self}$ is +0.553 for regional-trial yield gain (p = 0.020)
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
germplasm-concentration comparison — the Herfindahl–Hirschman index across resolved parental
lines, with a stratified bootstrap and a label-permutation test for the between-channel
difference, and rarefaction for the distinct-line counts — supports the counter-case in §7
and is not used to estimate the main channel gap. An unknown-breakpoint sup-Wald scan (candidate breakpoints 2009–2019, with level-shift
and trend-shift specifications) is used only to test whether the quality trajectory has a
structural break coincident with the 2016 reform (§4.7, Non-claim 3), not to estimate the
channel gap itself.

## 4.7 What this paper does not claim

This paper's estimates support a narrower and more specific set of claims than the pattern
of results might suggest at first reading, and we state the boundaries explicitly here so
that no reader — including the authors, in a later paper — mistakes a composition gap for
something it is not.

One point of terminology first. Where we describe an outcome, a placebo or a robustness
check as *pre-specified*, we mean that it was fixed in a written analysis plan before the
corresponding estimates were run. That plan was not deposited in a public registry, and we
make no pre-registration claim: readers should treat these as author-documented
pre-specifications, which are weaker than registered ones, and weigh them accordingly.

1. **$\beta$ is not a causal effect.** It is a within-cell composition gap, not the effect of moving a variety between channels; the only design that could speak to the latter (within-applicant, §6.3) is underpowered by 2–3× on every headline coefficient (full numbers there), so we do not claim to have separated a genuine channel effect from applicant self-selection.
2. **We do not use language of fabrication or manipulation.** Every measurement-authority claim is phrased as *consistent with measurement discretion, though channel self-selection cannot be ruled out*.
3. **We do not claim the 2016 reform caused the quality gap or any quality decline.** The structural-break scan (§5.5) dates the main quality breaks to 2009–2015, before the reform; what we estimate is a same-year channel gap, not a before/after effect.
4. **We do not claim third-party-assayed traits are uniformly worse among self-organised entrants.** Bacterial-blight grade moves the opposite way (§5.2); the headline claim is confined to grain-processing and appearance quality.
5. **We do not claim the self-reported yield advantage is an established finding.** It reverses sign between arms and its Manski lower bound sits near zero (§5.3, §6.2); the abstract accordingly calls it "suggestive only."
6. **We make no welfare claim.** No data on adoption, prices, or consumption exists in this study to support one.
7. **Approval counts are never used as an outcome variable**, only as descriptive background, because underlying compilation coverage declines sharply after 2022 (§3.1).
8. **We do not claim this paper's findings replicate at the provincial level.** The provincial re-estimation is non-significant for three of four headline outcomes and adequately powered and corroborating for the fourth (stated grade); see §6.4 for the full, two-part reading.
9. **We do not claim enterprises are generally better or worse breeders than public institutions.** The enterprise-vs-institution comparison (Supplementary Table S1, §7) is descriptive background only, not least because the applicant-type field is entirely missing for four approval years.
10. **This paper does not evaluate any individual applicant organisation.** No analysis in it is conducted at the level of a named firm or institute, and nothing in §7 should be read as assessing the breeding capability, commercial performance or conduct of any particular applicant. The germplasm-concentration indicator describes entry routes, not organisations.
11. **We do not claim varietal homogenization is increasing or decreasing over time.** §7 compares germplasm concentration *between channels within a period*; it does not estimate a time trend in concentration, and nothing here should be read as evidence that the breeding base is narrowing or widening.
12. **We do not treat the parsed compilation as an official, complete registry.** Our access is mediated by a third-party compilation whose field-level agreement with original MARA text we have not verified (§3.4). This is an assumption the paper relies on, not an established data-quality guarantee.

---

# 5. Results

## 5.1 Sample and strata

The main analysis layer restricts the record-level approval data to national-level (国审) approvals in the two dominant indica trial groups (middle-and-lower-Yangtze mid-season indica; upper-Yangtze mid-season indica) in the years in which the channel variable actually varies — 2017 and 2019–2022 — yielding **n = 878** records (Unified 406, Consortium 405, Green 67). Because the green channel (2017) and consortium trials (2019–2022) do not overlap in time, we estimate them as two separate arms (Section 4.3): **Arm 1** compares Consortium (n = 405) with Unified (n = 354) entrants within 2019–2022 (pre-outcome-drop n = 759, later outcomes ranging n = 520–759 depending on missingness); **Arm 2** compares Green (n = 67) with Unified (n = 52) entrants within 2017 (n = 119, 2–3 identifying cells). Table 3 reports both arms for all 17 outcome variables, split into third-party-assayed (grain-processing and appearance quality, resistance) and applicant-self-reported (yield, agronomic) blocks; Fig. 2 plots the same 34 estimates as a two-panel forest plot, colour-coded by measuring party.

## 5.2 Arm 1: Consortium versus Unified, 2019–2022

Consortium entrants show a consistent, statistically robust deficit on every third-party-assayed grain-processing and appearance trait carried in the main quality block (Table 3; Fig. 2, left panel, blue markers). Head-rice percentage is 1.844 percentage points (pp) lower (95% CI [−2.636, −1.052], p = 5.1 × 10⁻⁶, n = 742); chalkiness degree is 1.108 pp higher, i.e. worse appearance quality (95% CI [0.248, 1.969], p = 0.012, n = 739); and the probability that the announcement states a national/industry-standard quality grade at all (`quality_stated`) is 12.2 pp lower (β = −0.122, 95% CI [−0.211, −0.033], p = 0.008, n = 750). A secondary quality measure restricted to graded records — the probability of being graded 1 or 2, the top two national quality tiers (`quality_top2`) — is also lower by 9.1 pp (p = 0.009, n = 618), though we flag below (Section 6.2) that this coefficient does not survive Manski worst-case bounds and is therefore treated as secondary rather than headline evidence. Gel consistency, a third assayed grain-eating-quality trait not previously highlighted, moves in the same direction (β = −1.814 mm, p = 0.015, n = 728), consistent with the broader pattern of worse third-party-assayed eating and appearance quality among consortium entrants. Amylose content and grain length–width ratio show no significant difference (Table 3), and neck-blast resistance is not estimable for Arm 2 (100% missing in 2017 records; see Section 5.3) but shows no significant Arm 1 gap either (p = 0.28).

Against this, the applicant-self-reported yield-performance traits move in the opposite direction. The two-year regional-trial yield gain over the named check is 0.553 pp *higher* for Consortium entrants (95% CI [0.091, 1.016], p = 0.019, n = 708), and the production-trial (生产试验) yield gain over check is 0.919 pp higher (95% CI [0.505, 1.333], p < 0.0001, n = 578). Raw two-year trial yield in kg/mu (1 kg/mu ≈ 15 kg/hm²; 1 亩 = 1/15 hm²) shows no significant difference (β = +1.43, p = 0.61, n = 716) — consistent with the gain-over-check measures capturing a comparison-scale effect rather than raw yield levels. Two of the three pre-specified placebo traits, seed-setting percentage (β = −0.202, p = 0.43) and 1000-grain weight (β = +0.138, p = 0.59), are both non-significant, as required by the pre-declared design (Section 4, Non-claims). Plant height is 0.952 cm higher (p = 0.044); per the pre-specified methods statement, this is **not** treated as a placebo result but reported as auxiliary evidence consistent with a taller, larger-panicle selection type declared before the analysis was run (Section 6.1, R12, gives the full treatment).

One trait falls outside the sign-separation pattern in a way that itself supports the paper's identification argument rather than undermining it: bacterial-blight grade, also third-party assayed, is 0.190 grades *lower* (i.e. *more* resistant) among Consortium entrants (95% CI [−0.278, −0.102], p < 0.0001, n = 520). This is reported prominently, not hidden, because the paper's claim is deliberately scoped to grain-processing and appearance quality, not to "third-party-measured traits deteriorate uniformly" — a claim the bacterial-blight result would falsify if made (Sections 4.4, 6.2).

## 5.3 Arm 2: Green channel versus Unified, 2017

Green-channel entrants in 2017 (n = 119, HC1 standard errors, 2–3 identifying cells) reproduce the same direction on appearance and grading traits, at larger magnitude: chalkiness degree is 2.809 pp higher (95% CI [1.874, 3.744], p < 0.0001, n = 110) and the probability of a stated quality grade is 34.4 pp lower (β = −0.344, p < 0.0001, n = 112). Head-rice percentage, by contrast, is *not* significantly different in this arm (β = −0.391, p = 0.55, n = 106) — a genuine cross-arm inconsistency, and one reason the two arms are kept separate.

Two results in Arm 2 diverge from the Arm 1 narrative and are reported here as required, not deferred to a robustness appendix. First, the production-trial yield gain over check is 1.036 pp *lower* for Green-channel entrants (β = −1.036, 95% CI [−1.860, −0.213], p = 0.014, n = 112) — the opposite sign from Arm 1's +0.919 pp. Second, the regional-trial yield gain over check cannot be meaningfully estimated in this arm at all: only 21 of 119 records carry a non-missing value, driven almost entirely by the Unified sub-arm, whose regional-trial-gain coverage in the 2017 stratum is only 1.9% (1 of 52 records; Table 3 reports n = 21, β = −0.994, p = 0.17, but this coefficient should not be interpreted as informative about the underlying population). We flag this explicitly as *not estimable*; Fig. 2's right panel marks the corresponding neck-blast row "not estimable" for the same reason (the field is 100% missing for all 119 Arm-2 records). Together, these two results mean that Arm 2 does *not* replicate Arm 1's suggestive yield-advantage pattern, and the paper does not claim that it does.

## 5.4 Channel composition and convergence over time

A year-by-year re-estimation of the Arm-1-style channel gap (new channel vs Unified, within `trial_group × check` cells, HC1 standard errors, years in which both channels co-exist: 2017 and 2019–2022; 2018 is excluded because only 1 of 234 national records that year carries a green/consortium label, a parsing default rather than a genuine channel assignment) shows two distinct patterns that must be reported separately rather than summarised as a single "gap is narrowing" story. Chalkiness degree narrows monotonically from +2.71 pp in 2017 (p = 1.1 × 10⁻⁸) to +1.63 (2019, p = 0.004), +0.92 (2020, p = 0.004), +0.89 (2021, p = 0.002) and +0.77 pp in 2022 (p = 0.038) — a genuine, monotonic convergence in this one trait. The stated-quality-grade gap also weakens on balance (from −0.327 in 2017 to −0.052 in 2022) but non-monotonically, with 2020 and 2022 not significant. Head-rice percentage, by contrast, shows **no convergence**: the gap is −0.61 pp in 2017 (not significant) and widens to −2.63 (2020, p = 0.0003), −1.48 (2021, p = 0.021) and −3.03 pp (2022, p = 0.006) — its largest, most significant values occur in the *most recent* years of the sample. The regional-trial yield-gain-over-check coefficient fluctuates around +0.3 to +0.9 pp with no clear convergence or divergence pattern (Fig. 3; full year-by-year coefficients in the Supplementary Material). We therefore do not claim that "the quality gap between channels is closing" as a general statement; only chalkiness, and more weakly the stated-grade indicator, show convergence, while head-rice — arguably the more economically material processing-quality trait — does not.

## 5.5 Structural breakpoints predate the 2016 reform

An unknown-breakpoint (sup-Wald / Quandt) scan over candidate years 2009–2019, run on the full 2005–2022 national two-trial-group layer (n up to 1,204 records depending on trait non-missingness), asks whether the quality traits behind Arm 1's headline result show a structural break coinciding with the 2016 reform that created the consortium and green-channel pathways. They do not. Regional-trial yield per mu shows a clear break at **2017** (peak Wald = 230.3, p < 10⁻⁵⁰, n = 1,167; Fig. 4), consistent with a level shift in absolute yields around when the new channels opened. But the three quality traits central to this paper's argument break *earlier*: head-rice percentage at **2015** (Wald = 73.9, p < 10⁻¹⁶, n = 1,186), chalkiness degree at **2009** (Wald = 22.9, p = 1.1 × 10⁻⁵, n = 1,187), and the top-two quality-grade indicator at **2015** (Wald = 45.5, p = 1.3 × 10⁻¹⁰, n = 845). All three precede the 2016 institutional reform by one to seven years. Yield gain over check shows no robust break: under the paper's default heteroskedasticity-robust (HC1) covariance, the candidate break at 2018 is marginally significant (Wald = 6.55, p = 0.038), but under classical (homoskedastic) standard errors the same candidate year is not significant (Wald = 5.40, p = 0.067), and a diagnostic check shows the non-missing rate of this variable jumps from 21–22% in 2016–2017 to 100% in 2018 — i.e., the 2018 "break" in Wald statistics is confounded with a sudden change in reporting completeness rather than a real trend discontinuity in the underlying trait. We therefore report yield-gain-over-check as showing **no robust structural break**, consistent with a companion finding using classical standard errors, and flag the HC1 result's sensitivity to this covariance choice explicitly (Fig. 4; full scan values in the Supplementary Material). Fig. 4 also plots growth duration, a trait we do not otherwise analyse in this paper; its scan peaks at **2018** (Wald = 226.8, p < 10⁻⁴⁹, n = 1,196), close to the absolute-yield break but one year later, and we report this only as background context for the figure rather than as part of the paper's argument, since growth duration is not one of the third-party-assayed quality traits this section is built to falsify a reform-timing story for.

Taken together, these results support a falsification claim rather than a positive dating claim: whatever quality improvement trend is visible in the pre-2016 data was already underway before the reform, so attributing the level of grain-processing and appearance quality in this period to the 2016 reform itself — as opposed to reading the *channel gap conditional on year* reported in Sections 5.2–5.3 — would be a mistaken inference. This paper's estimand is explicitly the latter (the same-year channel gap), and the breakpoint evidence is reported to pre-empt the former misreading. This falsification result also bears on a year-indexed reading of the same corpus: Lu et al. (2024) and Hang et al. (2024) both document long-run quality- and yield-trait trends in Chinese variety-approval records using calendar year as the explanatory variable, without a channel distinction; our break-year estimates (head-rice 2015, chalkiness 2009) sit inside the window their national trend series cover, which is consistent with, though not a direct test of, their finding that these trait trajectories are gradual rather than reform-triggered. The two approaches are complementary rather than competing: a channel-conditional design like ours cannot itself characterise the decades-long trend that a year-indexed design is built to describe, and neither of those papers can distinguish (as this paper's Arm 1/Arm 2 comparison does) whether varieties entering through a given channel in a given year look different from their contemporaries in another channel.

## 5.6 Summary

Table 3 and Fig. 2 present the full set of 17 outcome variables for both arms, including the outcomes that run against the paper's central narrative (bacterial-blight resistance, Arm 2's reversed production-trial yield gain, Arm 2's non-estimable regional-trial yield gain). The pattern that survives across both arms is a consistent, third-party-assayed grain-processing and appearance-quality deficit among self-organised-trial entrants, paired with an applicant-measured yield performance that is, if anything, higher — a sign separation inconsistent with a pure breeding-ability account, but not by itself sufficient to rule out differing entry thresholds across channels. Section 6 subjects this pattern to sixteen pre-specified and one additional robustness checks, several of which qualify or fail to replicate parts of the headline result, and reports all of them.

---

# 6. Robustness, placebos and bounds

This section reports seventeen robustness checks (R1–R17) against the Arm-1 headline results of Section 5 (head-rice −1.844 pp, chalkiness +1.108 pp, stated quality grade −0.122, regional-trial yield gain +0.553 pp, production-trial yield gain +0.919 pp, bacterial-blight grade −0.190; see Table 3 and §5.2 for full CIs, p-values and n). No check is omitted, and where a check does not support the main result, we say so and report the number. Checks that leave the headline pattern essentially unchanged (R1–R6, R8, R10, R12–R14, R17) are reported briefly, with full statistics left in Table 3/Table 4; checks that qualify or complicate the headline pattern (R7, R9, R11) are given full treatment, since these are the ones a reader needs explained rather than tabulated. R15 is the one exception to that arrangement: its verdict and headline diagnostics are reported in §6.5, with its construction and full diagnostics in the Supplementary Material.

## 6.1 Checks that leave the headline pattern unchanged (R1–R6, R8, R10, R12–R14, R17)

- **R1 (two channels never pooled).** Already established in §5.1–5.3: pooling Arm 1 and Arm 2 would average a +0.919 pp production-trial yield-gain coefficient with a −1.036 pp one, manufacturing a sign that never occurred. Reported only as a reference row (Table 3), never as the headline estimate.
- **R2 (fixed-effects specification).** Re-estimating on the additive, collinearity-prone year + trial-group + check specification (rather than the interaction cell used throughout) reproduces the same signs and comparable magnitudes for all four cross-checked coefficients. Conclusion: the choice of fixed-effects structure is not what drives the result (full numbers: Table 4).
- **R3 (extend to all national trial groups).** Extending from the two dominant indica trial groups to all national trial groups leaves direction and significance essentially unchanged in both arms. Conclusion: not an artefact of the two-trial-group restriction.
- **R4 (2018 treatment).** Coding the 233 unlabelled 2018 records as Unified, instead of excluding them, produces numerically identical point estimates, SEs and p-values to the main design, because every 2018 cell in this stratum is a Unified-only (or one Green-only) singleton carrying no identifying variation either way. Conclusion: the 2018-coding choice is provably immaterial.
- **R5 (Benjamini–Hochberg FDR).** Of 17 Arm-1 outcomes, 9 retain q < 0.05 after BH correction across all 17 tests, including all six headline coefficients (q = 0.00009 to 0.040); the remaining three are the top-two quality-grade indicator (q = 0.029, qualified in R7), gel consistency (q = 0.037) and grains per panicle (q = 0.047, the closest to the threshold). Conclusion: the sign-separation pattern does not depend on uncorrected multiple testing.
- **R6 (randomisation inference).** Exact permutation p-values (500 draws within each year × trial-group × check cell; Fig. 5) place head-rice, chalkiness and regional-trial yield gain in the extreme tail of their null distributions (RI p = 0.002 each). Conclusion: corroborates the headline results independently of cluster-asymptotic assumptions.
- **R8 (missingness balance).** Supplementary Fig. S1 shows most of the 17 outcomes balanced within ~2 pp of non-missing rate across arms; the three exceptions (top-two grade, regional-trial yield gain, two-year kg/mu yield) are exactly the three that motivate the Manski-bounds exercise (R7, below).
- **R10 (drop the dominant germplasm lineage).** Dropping every record whose resolved sterile line is the most prevalent one in the estimation stratum (65 of 878 records, 7.4%) leaves the headline result significant with the same sign: head-rice −1.367 pp (p = 0.001, n = 689), chalkiness +1.077 pp (p = 0.020, n = 686), stated grade −0.119 (p = 0.017, n = 696) (Table 4). Conclusion: the result does not depend on any one breeding lineage; see also §7.
- **R12 (pre-declared placebos).** Seed-setting percentage and thousand-grain weight, declared as placebos before estimation, are both non-significant. Plant height was pre-declared *outside* the placebo set and is significantly higher among Consortium entrants (β = +0.952 cm, p = 0.044); this is reported as auxiliary agronomic evidence, not a failed placebo, per the pre-specified design.
- **R13 (pre-reform time placebo).** A pseudo-treatment built the same way in 2005–2016, before any channel existed (using `applicant_type == Enterprise` as the closest available proxy, n = 153, 13 cells), returns no significant coefficient on any of the six outcomes, and the sign is opposite the real design's for both headline quality traits. Conclusion: enterprise-versus-public composition alone, absent real channel variation, does not reproduce the quality-deficit pattern — though this only weakens one specific confound and does not by itself rule out $H_{threshold}$ (§4.5).
- **R14 (cluster by variety).** Re-clustering standard errors at the variety level (36 varieties, 72 records approved in multiple ecological zones) leaves all headline coefficients significant at p ≤ 0.0014. Conclusion: this source of non-independence does not threaten the main inference.
- **R17 (quality-grading standard composition).** Records state their grain-quality grade under one of two standards — NY/T 593 《食用稻品种品质》 and the national standard GB/T 17891 《优质稻谷》 — and which is in force shifts across the window (2017 is predominantly GB/T, 2019–2022 predominantly NY/T 593), so a channel that correlated with standard would not be comparable on the quality outcomes. Within each arm's own window it does not: among records carrying a stated grade, Arm 1 is 99.2% NY/T 593 under the unified channel against 99.2% under the consortium channel, and Arm 2 is entirely GB/T on both sides. Because the standard in force is determined by approval year and not by channel, the year × trial-group × check cell absorbs the switch. The check also recovers the headline disclosure result from raw shares: the share of records carrying no stated grade is 13.0 percentage points higher for consortium entrants and 32.6 points higher for green-channel entrants than for their respective unified comparison groups. Conclusion: the quality contrasts are not an artefact of which standard was in force. This is a composition check on the estimation stratum, not a within-cell test; it establishes that standard choice tracks year rather than channel, which is what the cell structure requires.

## 6.2 Manski worst-case bounds (R7)

Because four outcome variables show meaningfully unbalanced missingness between arms — the top-two quality grade (23.0% missing in the Consortium arm vs 11.3% in Unified), regional-trial yield gain (0.2% vs 11.9%, and separately the 2017 Unified sub-arm at 1.9%), production-trial yield gain, and two-year trial yield in kg/mu (Supplementary Fig. S1; imbalances ≥ 8 percentage points flagged in orange) — we compute Manski worst-case bounds by filling missing values at the 5th/95th percentile extremes appropriate to each arm. Head-rice percentage and chalkiness degree, whose missingness is balanced (~1–2 pp gap across arms), have narrow, sign-stable bounds ([−2.001, −1.623] and [+0.976, +1.203] respectively) and are treated as the paper's most secure headline results. The top-two quality-grade indicator does **not** survive this test: its worst-case bound is [−0.253, +0.088], which crosses zero — the sign is unstable under worst-case imputation. We therefore explicitly downgrade this variable to a secondary result and rely on the fully defined (0% missing by construction) stated-quality-grade indicator as the primary grading-related headline result (Table 3; Section 5.2). Regional-trial yield gain's worst-case bound is [+0.049, +0.912] — the lower bound is close to zero (p = 0.91 at that bound) — so this coefficient is downgraded from "suggestive support for a positive self-reported advantage" to "directionally positive but not robustly bounded away from zero." No headline third-party-quality result other than the top-two grade indicator changes sign under worst-case bounds.

## 6.3 Within-applicant subsample and its minimum detectable effect (R9)

The most direct test of self-selection versus a genuine channel effect compares the same applicant's own varieties across channels. This subsample is small: 10 applicants, 51 records (26 Consortium, 25 Unified) within the Arm-1 window, estimated with applicant fixed effects (rather than the main year × group × check cell, which is too fine for a sample this size) and HC1 standard errors. None of the six headline coefficients is significant in this subsample, and three (head-rice, chalkiness, stated grade) flip sign relative to the main design (Table: head-rice +0.780, p = 0.61; chalkiness +0.846, p = 0.21; stated grade +0.118, p = 0.40; regional-trial yield gain +0.100, p = 0.86; production-trial yield gain −0.126, p = 0.82; bacterial-blight grade −0.421, p = 0.38).

We compute the minimum detectable effect (MDE) this subsample could reliably distinguish from zero at 80% power for each outcome: head-rice 4.37 pp, chalkiness 1.96 pp, stated grade 0.41, regional-trial yield gain 1.66 pp, production-trial yield gain 1.56 pp, bacterial-blight grade 1.41. In every case, the MDE exceeds the magnitude of the corresponding main-design coefficient — for head-rice by roughly 2.4×, for regional-trial yield gain by roughly 3×. This converts a qualitative "underpowered" claim into a quantitative one: **this design cannot statistically distinguish "no channel effect once self-selection is removed" from "the channel effect exists, but this subsample is too small to detect it."** The sign flips are consistent with a severely underpowered, noisy estimate rather than a credible contradiction of the main design, but we do not claim the within-applicant test confirms the main effect either — it simply lacks the power to adjudicate the question (Section 4, Non-claims 1).

## 6.4 Provincial replication and its minimum detectable effect (R11)

Provincial-level approvals (省审) in 2021–2022, pooling Consortium and Green under a single new-channel indicator against Unified (cell fixed effect: year × trial group, without the check dimension, because provincial trial-group labels are far more heterogeneous), give a raw sample of n = 495 (new-channel 143, Unified 352). None of the four headline outcomes replicates as significant in the same direction and comparable magnitude as the national result, with one important exception. Head-rice percentage: β = −3.354, p = 0.53, n = 280, MDE = 14.99 pp against a national effect of −1.844 pp — severely underpowered. Chalkiness degree: β = −0.549, p = 0.24, n = 256, MDE = 1.31 pp against a national effect of +1.108 pp — underpowered (and the point estimate's sign is even reversed, though the MDE analysis shows this reversal is not informative). Regional-trial yield gain: β = −0.994, p = 0.62, n = 205, MDE = 5.62 pp against +0.553 pp nationally — underpowered.

**The stated-quality-grade coefficient is the one exception:** at n = 495 the provincial sample is adequately powered for this outcome (MDE = 0.41, smaller than the national coefficient's magnitude), and it returns a significant, larger-magnitude, same-direction (negative) coefficient: β = −0.468, p = 0.001. This is the one provincial result that is not simply underpowered, and it is read as strengthening, rather than qualifying, the stated-grade half of the headline result — provincial-level approvals show the same self-organised-channel deficit in whether a quality grade is stated at all, and here the sample has the power to say so with confidence. The correct overall reading of R11 is therefore two-part: for head-rice, chalkiness and yield gain, the national-level effect size is **statistically undecidable** at the provincial level, not disproved by it; for the stated-grade indicator, the provincial result is adequately powered and corroborates the national finding.

Because provincial trial-group labels are heterogeneous, the cell definition at provincial level is a judgement call, and the resulting sample size is sensitive to it. We therefore read this check for the direction of its results only — provincial-level non-significance for head-rice, chalkiness and yield gain — and not for its point estimates, which the minimum-detectable-effect calculations above show to be uninformative at this sample size in any case.

## 6.5 A chained-check genetic-gain scale as an alternative yield metric (R15)

The gain over the named check (Section 5.2–5.3) is comparable only within a trial-year-check cell, so we also re-expressed yield on a chained cross-year check scale, back-solving each record's implied check yield and chaining records that share a check across adjacent approval years (Piepho et al., 2014; Laidig et al., 2014; Mackay et al., 2011; Raymond et al., 2023; Piepho and Laidig, 2025). Four known weaknesses of the method appear here: an unstable back-solved check yield (median CV 1.56%); a chain step moving +3.14% where the decomposition implies +7.04%; an implied gain rate swinging between 0.25% and 0.50% per year; and only six distinct checks (G = 6, about 3 effective degrees of freedom). The self-reported yield advantage does not reverse in direction on this scale, but the interval is too wide to pin its magnitude, so the check is inconclusive rather than confirmatory or disconfirmatory. Construction and full diagnostics are in the Supplementary Material.

## 6.6 `quality_stated` under disclosure-behaviour controls (R16)

Section 3.3 flags `quality_stated` as mechanically close to a missingness indicator for the underlying grade field, and states that we report it as measuring *announcement disclosure behaviour* rather than grain quality itself. This check asks directly whether the Arm-1 coefficient on `quality_stated` is an artefact of some announcements simply being shorter or thinner on detail: we re-estimate the main Arm-1 specification adding two controls, the announcement's raw text length (`source_text_len`) and the count of non-missing fields among the paper's other 16 outcome variables, on the same sample (n = 750, cluster(cell, G = 10)). The baseline coefficient is β = −0.122 (p = 0.0075); with both controls added it is β = −0.146 (p = 0.0005) — the coefficient survives and strengthens in both magnitude and significance, consistent with the direction anticipated in §3.3. This rules out the simplest version of the "shorter announcements just say less" alternative account of the stated-grade gap.

## 6.7 Robustness matrix

Table 4 collects all seventeen checks (R1–R17) in a single matrix, including the two that qualify a headline result (R7's Manski bound on the top-two quality grade; R11's mostly-underpowered but partly-corroborating provincial replication) and the one that is genuinely underpowered rather than informative either way (R9's within-applicant subsample). Read together with the year-by-year evidence in Section 5.4, this paper's central identification claim — a third-party-assayed grain-quality deficit paired with an unchanged or higher applicant-measured yield performance among self-organised-trial entrants — survives every check that has adequate statistical power to test it (R1–R6, R8, R10, R12–R14, R16, R17), is not reproduced by a pre-reform placebo that shares no real channel variation (R13), and is qualified rather than contradicted by the two checks with genuinely limited power (R9, and three of four outcomes in R11). The one secondary result that does not survive worst-case bounds (top-two quality grade, R7) is explicitly downgraded from headline evidence, and the one alternative yield metric explored as an additional check (the chained-check ladder, R15) returns an inconclusive, wide-interval result that neither strengthens nor weakens the main yield-side finding.

---

# 7. Germplasm concentration by channel: does each door admit a different breeding base?

*This section tests an alternative explanation for the sign separation using a second indicator built from the same announcements. It is not a source of the main result.*

The sign separation reported in Sections 5–6 is consistent with measurement discretion in self-organised trials, but it is equally consistent with a cruder alternative: perhaps the self-organised channels simply admit varieties bred from a narrower or weaker germplasm base, and the third-party quality deficit records that fact rather than anything about who measured it. If so, the gap would reflect *what* enters through each door, not *how* the door is measured. The announcements support a direct test, because each one names the cross that produced the variety.

We resolve the variety-source field into two parental-line entities per record — the female (sterile) and male (restorer) line of the originating cross — which succeeds for 2,304 of 2,386 national records (96.6%; see §3.1 for the extraction rule and its failure profile). The indicator is computed on the same stratum as the main estimates, the two dominant mid-season indica trial groups, since pooling ecologically unrelated breeding pools would inflate any contrast. Over those entities we compute the Herfindahl–Hirschman index across sterile lines, the count of distinct lines, and the share held by the most frequent line. Because concentration measures are non-linear in the sample, differences are assessed by a stratified bootstrap and a label-permutation test, and distinct-line counts are rarefied to the smaller group so they cannot be read as a sample-size artefact. Extraction coverage is 99.7–100% in all four channel-by-arm groups, so differential parsing failure cannot drive the comparison.

Consortium entrants draw on a **broader** sterile-line base than contemporaneous unified entrants (Table 5; Fig. 6): HHI 0.0124 against 0.0186 (difference −0.0062, 95% CI [−0.0130, −0.0009], permutation *p* = 0.022), with 212 distinct sterile lines against 156, or 193.0 against 156.0 once rarefied to the smaller group, and the most frequent line covering 5.7% of entries against 9.1%. This is what consortium rules would lead one to expect, since a consortium trial pools five or more breeding programmes.

Green-channel entrants are directionally more concentrated — HHI 0.0778 against 0.0562, the most frequent line covering 22.4% against 11.5% — which is likewise what a channel whose trials one certified enterprise runs would lead one to expect. But at 67 against 52 records the interval spans zero (difference +0.0215, 95% CI [−0.0240, +0.0671], permutation *p* = 0.344), and we therefore report Arm 2 for completeness and rest nothing on it. We note this explicitly because an earlier version of this analysis, computed across all national trial groups rather than the estimation stratum, returned a significant Arm-2 contrast; restricted to the stratum the main estimates use, it does not survive.

The Arm-1 result is what rules the alternative out, and it does so on its own. A narrow-breeding-base account predicts the quality deficit appears where fewer lines are drawn on. Consortium entrants record 1.844 points lower head-rice percentage and 1.108 points higher chalkiness than unified entrants, yet they are drawing on a significantly **broader** sterile-line base than the same comparison group. Breeding-base narrowness cannot explain a quality deficit in a channel that is less concentrated than the entrants it is measured against. What separates the two is not germplasm but measurement arrangement: the applicant organises the trial in which agronomic performance is recorded, while grain quality is assayed by the same ministry-designated third party in either channel (§2; §3.3). We claim no more than this: the germplasm-diversity version of the composition story is inconsistent with the Arm-1 data. Other composition stories, including selection on an unobserved entry threshold, remain open and are treated in §4.7 and §6.

Dropping every record whose resolved sterile line is the most prevalent one in the estimation stratum leaves the headline result intact (Section 6.1, R10; Table 4): head-rice percentage −1.367 pp (p = 0.001, n = 689), chalkiness degree +1.077 pp (p = 0.020, n = 686), and stated quality grade −0.119 (p = 0.017, n = 696). The result does not rest on any one breeding lineage.

As descriptive background — not as a conclusion about which type of institution breeds better rice — applicants labelled "public research institute" show higher regional-trial yield (+4.179 kg/mu, SE 1.893, p = 0.027, n = 408) and thousand-grain weight (+1.193 g, SE 0.402, p = 0.003, n = 411) than enterprise applicants, alongside directionally higher chalkiness (+1.010, SE 0.614, p = 0.100, n = 411) and lower head-rice percentage (−1.220, SE 0.673, p = 0.070, n = 411) (Supplementary Table S1). This division of labour runs in the opposite direction from what an "enterprises are careless" account would predict for chalkiness and head-rice, and is silent on causation in either direction; it is reported here only as a background fact, not evidence for or against either institution type. Note also that neither quality coefficient reaches conventional significance (chalkiness p = 0.100, head-rice p = 0.070); the contrast is suggestive of a division of labour, and we do not rest any part of the argument on it.

Three scope limits bound what this section argues. First, concentration across parental lines measures the breadth of the breeding base an entry route draws on; it is not a measure of genetic distance, and two varieties sharing a named sterile line may still differ substantially. Second, the extraction rule takes only the first cross in the source field, so ancestry beyond the immediate parents is not represented, and the 4.4% of records whose source field does not parse are excluded rather than imputed. Third, "identification argument" is the operative phrase throughout: the concentration contrast rules out one alternative explanation for the sign separation reported elsewhere in the paper, and is not evidence of a causal mechanism linking channel, germplasm and trial outcome.

---

# 8. Discussion

## 8.1 Why the sign separation arises: self-certification as theoretical support

The regulatory-economics literature on self-certification is not this paper's frame, but it supplies the mechanism that makes the observed sign separation intelligible, and we draw on it in that narrower role. Duflo et al. (2013) randomly assigned polluting Indian plants to regulator-paid versus plant-paid auditors and observed the *same* pollution readings diverge systematically; Bar and Zheng (2019) show that firms endogenously choose certifiers with a history of lenient grading — the closest existing analogue to the "channel self-selection" alternative this paper cannot close off (§4; R9/R11). Grennan and Town (2020) compare medical-device outcomes *across* two regulatory systems, where ours is a comparison *within* one system across two pathways a single reform created side by side, and Renckens and Auld (2022) show private regulatory audits vary in efficiency with auditor incentives and monitoring intensity. Taken together these results establish that reported values move with who was asked to measure — which is exactly the interpretation the sign separation invites, and which is why we report it as consistent with measurement discretion rather than proof of it: none of these designs is available here, since we observe two different attributes measured by two parties rather than one attribute measured twice. Qiu et al. (2016) describe the same information problem one stage downstream, where Chinese farmers must infer unobservable seed quality from imperfect signals; our result places an analogous asymmetry inside the approval file itself.

## 8.2 Is the identified variation disappearing? A qualified answer

The Ministry of Agriculture and Rural Affairs has, since 2022, conducted a special rectification campaign targeting the green channel and consortium trials, and this raises the question of whether the gap this paper documents is a closing window rather than a stable feature of the system. The year-by-year re-estimation in §5.4 answers it outcome by outcome rather than uniformly; the coefficients are reported there and not repeated here. The chalkiness gap declines roughly monotonically across the window, consistent with narrowing as the reform matures and regulatory attention increases; the stated-quality-grade gap weakens more faintly and non-monotonically, and is not significant in two of the four post-2017 years; the head-rice gap does not narrow at all, its largest and most significant values falling in the sample's most recent years (Fig. 3). We therefore do not claim that "the identified variation is disappearing" as a blanket statement about the paper's outcomes; that claim holds for chalkiness, holds more weakly for the stated-grade indicator, and does not hold for head-rice percentage, the outcome with the cleanest and most consistent estimate in the paper. Whatever a closing window means for policy, it does not yet mean the head-rice gap has closed, and coverage of official announcements falls sharply after 2022 (85 of an expected 409 records in 2023, 61 of 405 in 2024), so this paper cannot verify whether any of the three outcomes converges further after the window it observes. This outcome-specific pattern is worth reading against the calendar-year trend evidence in Lu et al. (2024) and Hang et al. (2024): where their year-indexed series show gradual, decades-long trait change, our channel-conditional gap shows a mix of convergence (chalkiness) and non-convergence (head-rice) within a six-year window, which suggests the two kinds of trend — the long-run trajectory their design measures and the channel-specific gap ours measures — are not the same object and need not move together.

One further result belongs in this discussion. The province-level replication (§6.4) is underpowered for three of the four headline outcomes — head-rice percentage, chalkiness and self-reported yield gain, whose provincial non-significance is therefore "undetermined" rather than evidence against the national result — and adequately powered, and corroborating, for the stated-quality-grade indicator; §6.4 reports the coefficients and minimum detectable effects behind both halves of that reading. Its place here is interpretive: that split runs against a common but incorrect reading of provincial null results in this literature, and Non-claim 8 in the design stage of this project anticipated only a null and did not anticipate a significant, adequately powered result on this one outcome; the provincial evidence should be described precisely — one outcome significant and adequately powered, three underpowered — not summarised as either "confirms" or "does not replicate."

## 8.3 Policy implications

Three implications follow without extending beyond what the data show. First, the identification argument rests on an asymmetry: third-party assay covers grain-processing and appearance quality but not the agronomic-performance traits measured in the applicant's own regional and production trials. Extending independent, ministry-designated measurement to a subset of yield and performance traits — even a periodic spot-check rather than universal coverage — would let regulators test directly whether the sign separation this paper documents in observational data also appears when performance itself is measured by an independent party. Second, an audit-style re-verification of a random sample of self-organised trial results, analogous in spirit to the spot-checks the Ministry has run against the green channel and consortium trials since 2022, would generate exactly the kind of within-attribute comparison that Duflo et al. (2013) had and this paper does not; such spot-checks are already the Ministry's own initiative, and this paper's finding is best read as an independent, quantitative corroboration of the direction that 2022-08-31 rectification notice already took, not as a claim that regulators were unaware of the pattern. Third, the channel-of-entry information already exists inside every approval announcement but is not compiled or published as a standalone field; publishing it directly, rather than leaving it to be reconstructed by text-parsing as this paper did, would let downstream users of the seed catalogue — processors, distributors, other researchers — condition on it themselves.

## 8.4 Implications for S&T intelligence practice

Read as an intelligence exercise rather than an agricultural one, this paper makes four points that generalise beyond rice.

**Administrative approval corpora are a usable, unusually rich innovation data source — within limits.** Innovation measurement has broadened from patents and publications to trademarks, web traces and transaction data (Rammer and Es-Sadki, 2023), but the records a state generates when it authorises a technology for market have stayed outside the indicator toolkit, chiefly because they are published as prose. They repay parsing: one announcement yields the applicant, the testing arrangement, the comparison baseline and more than a dozen measured performance fields, tied to an actual market-entry decision rather than to an application. The limits were equally concrete here — an unverified third-party re-transcription (§3.4), coverage collapsing after 2022 (§4.7, Non-claim 7), and an applicant field absent for four years (§3.3) — so an analyst adopting this class of source should expect most of the effort to fall on pipeline steps (iv) and (v), not on extraction.

**Reliability is a property of fields, not of sources.** Within one official document, issued by one authority on one date, fields differed in evidential strength, and what predicted the difference was who measured: the laboratory-assayed quality traits moved one way, the applicant-recorded yield gain the other. Standard data-quality assessment in scientometrics and technology analysis is source-level — coverage, error rates, duplication, classification accuracy (Franceschini et al., 2016; Jaffe and de Rassenfosse, 2017) — and a source that passes such an audit can still contain fields of very different evidential value. Provenance labelling should therefore be a required step when building indicators from approval corpora: tag each field with its measuring party and stratify the reliability assessment by that tag, rather than issuing one verdict for the source.

**The diagnostic is portable.** The structural feature exploited here — applicant-supplied dossier material and independent assay results bound into one official record — is not specific to seed regulation. It recurs in drug approval, where sponsor-run trial results and regulator-reviewed labelling coexist in documents already mined at scale (Shi et al., 2021); in medical-device registration; and in patent examination, where applicant-drafted claims sit alongside examiner-added citations, a distinction the patent-indicator literature adopted only after treating all citations alike produced biased measures (Jaffe and de Rassenfosse, 2017). The test is the same and cheap in each case: partition fields by measuring party and check whether the contrast of interest holds the same sign in both partitions. Three outcomes are possible, and they carry different weight. A contrast present in both partitions is the most credible, since no single reporting party controls it. A contrast confined to the self-supplied partition is a candidate reporting artefact. A contrast confined to the independently assayed partition — the case this paper reports — is not an artefact of that kind, since the party with the reporting incentive is not the party producing the number; but neither is it self-validating, because it remains consistent with any process that sorts entrants on the independently measured trait, selection on an unobserved threshold included. What the partition buys in that third case is narrower than credibility: it rules out the reporting-incentive explanation and leaves the remaining alternatives to be addressed on other evidence, as we do in §4.7 and §6.

**For technology assessment and competitive intelligence specifically.** Text mining of S&T corpora was developed to support research management and technology watch (Losiewicz et al., 2000; Antons et al., 2020); approval records extend that practice to the point where a technology reaches users. The indicators built here answer the questions such work asks — which actors produce approved varieties, by which testing route, at what measured quality — while the provenance labels tell the analyst which of those indicators will bear weight. The recommendation for the corpus publisher is correspondingly cheap: the channel already exists inside every announcement, and issuing it as a field would let downstream users condition on it directly (§8.3).

## 8.5 Limitations

Six limitations bound this paper's scope. The evidence covers a single country and a single crop (rice); whether the same channel-measurement asymmetry appears in other crops or seed-regulation regimes is untested here. Channel self-selection cannot be fully separated from measurement discretion with the data at hand — the within-applicant comparison in Section 6 is directionally uninformative because it is underpowered, not because it rules out self-selection. The `applicant_type` field needed for the enterprise-versus-institute comparison in Section 7 is entirely missing for the 2016, 2017, 2018 and 2021 approval cohorts, which limits that comparison to years with non-missing labels and to the two major trial groups. The underlying announcement compilation is not an official, complete registry of all approvals; it is a secondary compilation of Ministry announcements, and its field-level fidelity to the original announcement text has not been verified (§3.4). This is the single most consequential unverified assumption in the study: every estimate reported here would inherit any systematic transcription error in the compilation, and we cannot presently bound that error. A replicator with access to the primary announcements should treat this as the first check to run. Fifth, the analysis window runs through 2022 because compiled announcement coverage falls sharply afterward; this paper accordingly cannot speak to whether the convergence trends documented in Section 8.2, or the divergent trend in head-rice percentage, continue, reverse, or stabilise after 2022. Finally, China's approval standards define categories of variety judged against different trait bundles, and applicants targeting a high-yield category would rationally accept weaker grain quality. We cannot control for this, because the announcements do not record which approval category a variety was judged under: searching the full corpus returns no occurrence of the category terms or of an explicit category field. The germplasm-concentration evidence in §7 constrains one version of this story but not all of it, and a corpus that published the approval category would settle it directly — which is itself an argument for the provenance-labelling recommendation in §8.4.

---

# 9. Conclusion

Since 2016, rice varieties have entered the Chinese market through three trial channels instead of one. Parsing which trial each variety actually passed through shows that what enters differs by channel on precisely the traits a third party, rather than the applicant, measures: self-organised entrants carry worse third-party-assayed grain-processing and appearance quality, alongside applicant-measured performance that is unchanged or higher. This is a difference in what each door admits, not an estimate of what the reform did — a sign separation that a simple breeding-ability story cannot produce, and that survives dropping the most prevalent breeding lineage from the sample.

This finding is a composition effect on the population of varieties entering under each trial pathway, not a causal effect of channel assignment on any individual variety, and should not be read more broadly. It does not speak to farmer welfare, extension outcomes, or seed prices; it does not allege fabrication or manipulation of any applicant's trial results, a possibility the data cannot distinguish from channel self-selection or differing admission thresholds; and it does not extend to every third-party-measured trait or every level of government, since disease-resistance grading moves the other way and the provincial replication is conclusive for only one of four outcomes. Within these bounds, the contribution is narrow but has two faces. As agricultural technology assessment, it supplies a record-level channel variable, built from the text of approval announcements rather than a before/after indicator, that lets who measures what be observed directly — and shows that this, not only the volume of entrants, changed after 2016. As S&T intelligence, it demonstrates that a long-public administrative corpus can be converted into a structured indicator system, and that the resulting indicators must be read field by field: inside a single official source, the strength of the evidence depended on who did the measuring. That diagnostic is the part of this paper most likely to be useful outside rice, and it can be applied wherever self-supplied dossier material and independent assay results are bound into the same approval record.

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
