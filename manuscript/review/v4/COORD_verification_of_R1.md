# Coordinator's independent verification of R1's findings

> R1 returned a "major revision — the framing is bolted on" verdict. Because that verdict
> drives whether a v5 is needed, its load-bearing claims were re-checked directly against
> the files rather than accepted on the reviewer's word. Checked 2026-09-16.

## Confirmed

**1. The analytic core is untouched. ✅ CONFIRMED — this is the decisive finding.**
`diff -u manuscript_v3.md manuscript_v4.md` produces 14 hunks. The hunk headers jump from
`@@ -199,7 +240,11 @@` straight to `@@ -471,7 +516,7 @@`. v3 lines 200–470 — the whole of
§4 (empirical strategy, estimand, identification), §5 (results) and §6 (robustness) —
received **zero edits**. A reframing that claims to make S&T intelligence a co-equal pillar
did not touch a single line of the paper's reasoning.

**2. "intelligence" never appears in the body. ✅ CONFIRMED.**
Occurrences at lines 9, 33, 47, 55, 75, 79, 80, then nothing until 545, 547, 555, 567.
Between line 80 and line 545 — everything the paper actually argues — the word does not
occur once. (Count is 13, not R1's 14; immaterial.)

**3. M1 — the "unexploited source" claim is contradicted by the paper's own Introduction.
✅ CONFIRMED, and this is the most dangerous item in the report.**
Abstract line 9: *"Official approval announcements are a long-public but unexploited
intelligence source."* Line 33: the corpus *"has barely touched"* S&T intelligence work and
*"sit[s] outside this frame."*
But line 39 states that Lu et al. (2024) classify **17,785** approved varieties and Hang et
al. (2024) track **11,811** regional-trial entries, and that *"both papers read the same kind
of approval-trial record we use."* That is 5–7× this paper's 2,386 records.
The paper hands a referee the refutation of its own abstract, in its own Introduction.
The precise and defensible claim is the one v3 made at line 41 — that the **channel
variable** has not previously been extracted, not that the **corpus** is unexploited. v4
generalised a true narrow claim into a false broad one.

**4. M3 — 审定 vs 登记 terminology. ✅ CONFIRMED.**
The title ends *"in China's rice variety registrations"* while the abstract two lines below
says *"approval announcements"* and *"approval reform"*. 品种审定 (approval) and 品种登记
(registration) are distinct statutory procedures under the Seed Law; rice is 审定. The wrong
term sits in the single most visible line of the paper.

## Confirmed but overstated by R1

**M2 — the portable diagnostic in §8.4.** R1 says the stated rule *"classifies the paper's
headline result as the artefact."* That is stronger than the text supports. Line 553 reads:
*"A contrast confined to the self-supplied partition is a candidate reporting artefact; one
present in both is more likely real."*
That rule names two cases: confined-to-self (artefact) and present-in-both (real). This
paper's contrast is confined to the **third-party** partition — a third case the rule does
not name. So the rule does not misclassify the paper; it **fails to cover the very case the
paper exemplifies**.
The defect is real and still a must-fix — a flagship "portable diagnostic" that is silent on
its own author's result is a visible weakness — but it is an incompleteness, not a
contradiction. The fix is a third branch, not a rewrite. R1's underlying point stands;
its characterisation should be softened before it reaches the author.

## Not yet independently checked
M4 (§8.4/§8.3 duplication), M5, M6, and R1's recomputed word-count and change-log
discrepancies (§8.4 = 539 not 562; §8.1 compression −34% not −49%). R1's verified track
record on items 1–4 makes these credible, but they are not confirmed here.

## Bearing on the v5 decision
R1's central claim survives scrutiny: the reframing changed vocabulary at the paper's
surfaces and left its reasoning untouched. Combined with M1 and M3 — a false claim in the
abstract and wrong terminology in the title — a v5 pass is warranted on this line alone,
before the other three reviewers are counted.
