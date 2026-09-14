# 4. Empirical strategy

## 4.1 Two difference-in-differences designs we considered and rejected

Before settling on the specification below, we considered — and rejected — two
difference-in-differences (DID) designs that would have let us speak in terms of a causal
"effect of the reform." The first would have used the switch from provincial to national
approval, or the reverse, as a difference-in-differences shock, comparing quality trends at
the two administrative levels before and after 2016. We tested the parallel-trends
assumption this design requires on six candidate outcomes in the pre-period and it failed for
three of them: chalkiness degree (+0.515 percentage points per year, p = 0.006), amylose
percentage (+0.212, p < 0.0001), and thousand-grain weight (−0.130, p = 0.003) all trend
differently across the two administrative levels well before 2016, so any post-2016 gap
between them would conflate a genuine channel effect with a pre-existing divergence. The
second candidate design would have used varying exposure to the new channels across trial
groups as a differential-intensity DID. This fails for a simpler reason: channel penetration
in the years we study ranges only from about 0.33 to 0.63 across trial groups, so there is no
low-exposure comparison group left to serve as the counterfactual trend. We report both
rejections here, rather than silently choosing the specification that worked, because the
paper's central claim — that self-organised entrants differ systematically from unified-trial
entrants — could otherwise be read as resting on a DID design it does not actually use. Our
design is not a difference-in-differences and does not estimate a pre/post treatment effect
of the 2016 reform; it is a within-cell cross-sectional comparison, described next.

## 4.2 A record-level trial-channel treatment and the collinearity problem

Reconstructing the trial channel at the level of the individual approval record — rather
than treating the 2016 reform as a single period indicator, as the one existing evaluation of
this reform does [REF: Xiang, Yang, Wang & Huang 2025 Agribusiness 10.1002/agr.22020] — makes
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

First and most fundamentally, $\beta$ is not a causal effect. It answers "how much do the
varieties entering through the self-organised door differ from the varieties entering
through the unified-trial door, within the same year–ecology–check cell," not "what would
happen if a given variety were moved from one door to the other." Our within-applicant
comparison — the only design in this data that could speak to the latter question — has only
about ten applicants and 26–64 records depending on the outcome, confidence intervals wide
enough to include effects several times the main estimate, and point estimates that in
several cases run opposite in sign to the main design. We report this explicitly as a power
limitation, not as a contradicting result, but it also means this paper cannot separate a
genuine channel effect from applicant self-selection into channel, and we do not claim to
have done so. Related to this, we do not claim that the yield and agronomic data recorded in
self-organised trials are fabricated or manipulated; every instance of measurement-authority
language in this paper is phrased as *consistent with measurement discretion in
self-organised trials, though channel self-selection cannot be ruled out*, and words such as
"fraud" or "manipulation" do not appear.

Second, we do not claim that the 2016 approval-system reform caused the quality gap we
document, nor that it caused any decline in rice quality over time. Our unknown-breakpoint
scan finds that the structural break in most quality traits — head-rice percentage around
2015, chalkiness degree around 2009 — predates the reform, while the comparative yield-gain
series shows no significant break at all; only absolute regional-trial yield breaks near
2017. What we estimate is a within-year gap between two contemporaneous channels, not a
before/after time effect, and attributing the pre-2016 quality trajectory to a post-2016
policy would be a basic error of temporal attribution that this paper is careful to avoid.

Third, we do not claim that third-party-assayed traits are uniformly worse among
self-organised entrants. Bacterial-blight resistance grade is, if anything, *better* (more
resistant) among self-organised entrants in both arms, and neck-blast tolerance shows no
detectable difference. We therefore confine the headline claim to grain processing and
appearance quality — head-rice percentage, chalkiness degree, and the probability of a stated
quality grade — and report the resistance results in the main results table rather than
setting them aside as inconvenient. Fourth, and in a related vein, we do not claim that
self-reported yield performance is systematically higher for self-organised entrants; that
half of the sign-separation argument is presented as suggestive only. The production-trial
yield-gain coefficient reverses sign between the two arms (+0.919 in the consortium arm,
−1.036 in the green-channel arm), the regional-trial yield-gain coefficient is not estimable
at all in the green-channel arm because of near-total missingness in its unified-trial
comparison group, and the Manski worst-case lower bound on the main regional-trial yield-gain
estimate is close to zero. The abstract accordingly describes this result as "if anything,
higher (suggestive only)," not as an established finding.

Fifth, this paper does not translate the quality gap into any statement about farmer or
consumer welfare; we have no data on adoption, planted area, seed prices, or downstream
consumption, and welfare is outside the scope of what this data can speak to. Sixth, we do
not treat the number of approved varieties, or its change over time, as a result of this
paper: because the underlying compilation is a sample of announcements with declining
coverage after 2022, not a verified census, approval counts appear only as descriptive
background with their coverage caveats attached, never as a dependent variable. Seventh, we
do not claim that this paper's findings replicate at the provincial level; our provincial
replication attempt returns a non-significant coefficient on head-rice percentage (β = −0.134,
p = 0.93) and other outcomes, and we present two candidate explanations — insufficient
statistical power at that sample size, or a genuine concentration of the effect at the
national level, where the regulatory stakes of approval are highest — without favouring
either.

Eighth, we do not claim that enterprises are generally better or worse breeders than public
research institutions, or vice versa. In the sub-sample with a non-missing applicant-type
field, public institutions show directionally higher regional-trial yield (+3.18 kg/mu,
p = 0.035) and thousand-grain weight (+0.96 g, p = 0.025) relative to enterprises, alongside
directionally higher chalkiness and lower head-rice percentage that do not reach
significance; we present this only as a descriptive, directional background fact about trait
specialization, not as a conclusion, not least because the applicant-type field is entirely
missing for four approval years. Ninth, in the mechanism section on a single integrated seed
enterprise, we do not claim that its quality-oriented positioning has been a financial
success — the same section reports, in the same discussion, its negative gross margin on
contract-grain sales, its move from profit to loss in 2025, a qualified 2024 annual-report
opinion, and a 2026 regulatory penalty and special-treatment designation, and we treat the
financial sustainability of a quality-differentiation strategy as an open question rather
than a settled one. Tenth, where we report a variety-homogenization robustness check, we do
not claim that varietal homogenization is increasing or decreasing over this period; both the
parentage-diversity and trait-space tests return null results and are presented only as
evidence against a common industry narrative, not as a positive finding of change in either
direction.

Finally, we do not treat the parsed compilation as equivalent to an official, complete
record of China's variety-approval history. The primary source is MARA's own approval
announcements; our access to them is mediated by a public third-party compilation whose
coverage of recent years is incomplete and whose field-level agreement with the original
announcement text has not yet been independently verified at the time of this draft (see
§3.4 and Unresolved item P4). We report this as an open verification step to be completed
before submission, not as an already-established data-quality guarantee.
