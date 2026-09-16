# Independent re-run of the entity-identification rule (§3.1, v4 line 145)

> Run 2026-09-16 by the coordinating session, because the v4 revision agent disclosed
> that it had carried the precision/recall figures into the Methods text from planning
> documents **without re-executing the validation** this round. A validation statistic
> stated in a Methods section that nobody has reproduced is a submission risk, so it
> was recomputed from the data.
> Script: `scratchpad/verify_rule3.py` (re-runnable).

## Verdict: the claim reproduces exactly. No correction needed to the stated numbers.

The manuscript (§3.1) states: *"Validated against the 1,426 records that do carry an
institutional label, the rule attains a precision of 1.000 and a recall of 0.770."*

Recomputed from `evidence/data/analysis_national_rice.csv`:

| Quantity | Manuscript | Recomputed | Match |
|---|---|---|---|
| Labelled subset n | 1,426 | **1,426** | ✅ |
| Precision | 1.000 | **1.0000** (TP = 107, FP = 0) | ✅ |
| Recall | 0.770 | **0.7698** (FN = 32) | ✅ |

"Records that do carry an institutional label" resolves to `applicant_type != 'Unknown'`
— i.e. 2,386 national records − 960 Unknown = 1,426 (Enterprise 802 + Public 520 +
Joint 104). This reading was not obvious from the text and is worth confirming is what
the authors intend a replicator to do; the phrase could also be read as "non-empty
applicant string", which gives n = 1,481 and does **not** reproduce the stated figures.
**Suggested (not must-fix): state the filter explicitly as `applicant_type != Unknown`.**

## One substantive caveat the manuscript does not currently disclose

**Precision 1.000 is measured against a ground truth that shares an input field with the
rule being validated.** The script's ground truth is `is_winall`, defined in
`scripts/parse_variety_texts.py:100` as the string 荃银 occurring anywhere in
pedigree + breeder + applicant + breeder fields. The rule under test
(`build_analysis_dataset.py:89–91`) also reads the pedigree field. Records whose
pedigree names the firm therefore satisfy both by construction, so the zero-false-positive
result is partly structural rather than an independent confirmation.

Under the stricter and more natural reading of "this is one of the firm's varieties" —
ground truth = the **applicant field alone** names the firm — the rule's precision falls
to **0.682**: 34 of 107 rule-positive records (**31.8%**) were applied for by other
companies (江苏中江种业 5, 中国种子集团 4, 湖北省种子集团 2, 安徽华安种业 2, and others).
These are varieties bred *from* the firm's 荃-series sterile lines but registered by
third parties.

### Is this a defect? Partly — it is a disclosure gap, not a false statement.

The manuscript defines the indicator transparently as **firm-linked** by lineage: *"a
record is coded firm-linked if the variety name begins with the firm's characteristic
name element, or either parent line carries that element or the firm's line-code prefix."*
That is a germplasm-lineage construct, and under that construct the other firms'
registrations are correctly included. The text is not making a false claim.

The risks are two:
1. **Reader inference.** "Firm-linked" will be read by most readers as "the firm's own
   varieties". A referee who checks will find that roughly a third were registered by
   competitors, and will treat the undisclosed gap as worse than the fact itself.
2. **The conservative-bias argument is stated only for false negatives.** §3.1 argues
   unrecalled records fall into the comparison group, so contrasts are biased toward
   zero. That is correct for FN. It is silent on the composition of the treated group.
   Under the lineage definition there are no false positives and the argument is
   complete; under the applicant reading the treated group is ~32% other firms and the
   sign of the bias is no longer guaranteed.

### Recommended fix (one or two sentences in §3.1, no re-analysis)
Disclose that (a) the validation target overlaps the rule's pedigree input, so precision
is a consistency check rather than an independent gold standard; and (b) the indicator is
deliberately lineage-based, and ~32% of firm-linked records carry a third-party applicant
— which is intended, since the counter-case in §7 concerns the firm's germplasm, not its
corporate filings. Stating this pre-empts the referee finding it first.

**R2 should judge whether §7's argument depends on the lineage or the applicant reading,
and confirm §7's prose does not describe these records in a way that implies corporate
ownership.** That determination is the open item, not the arithmetic.
