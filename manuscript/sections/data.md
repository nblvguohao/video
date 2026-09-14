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
trials did not exist in 2018 (see the year-by-year channel count, Table 1, and robustness
check R4 in §6, which shows the 2018 coding choice is immaterial to the main estimates).

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
in §6 that the coefficient survives, and in fact strengthens, once announcement text length
and the count of non-missing fields are controlled for.

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

A full descriptive and balance summary by arm — means, standard deviations, and missing
rates for all outcome and control variables in Table 3 — is assembled in Table 2
(`manuscript/tables/table2_descriptive_balance.md`); Table 1 reports the year-by-year record
counts by channel underlying the sample definition above.

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
