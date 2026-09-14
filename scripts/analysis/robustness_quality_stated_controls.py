"""
robustness_quality_stated_controls.py

Additional robustness check (R16) for the quality_stated outcome: does the
Arm-1 (Consortium vs Unified, 2019-2022) coefficient on quality_stated
change once announcement text length and the count of non-missing fields
are added as controls?

This directly tests the forward-reference claim originally made in
Section 3.3 of manuscript_v1.md ("the coefficient survives, and in fact
strengthens, once announcement text length and the count of non-missing
fields are controlled for"), which the R1 technical review found was never
backed by an actual check in Section 6. This script performs that check on
the real data and reports whatever the result actually is, rather than
assuming the planning-stage number.

Run: python3 scripts/analysis/robustness_quality_stated_controls.py
"""
import warnings
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore")

DATA_PATH = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
TRIAL_GROUPS = ["长江中下游中籼迟熟", "长江上游中籼迟熟"]

# The 17 outcome fields used in Table 3 -- used to construct "count of
# non-missing fields" per record.
OUTCOME_FIELDS = [
    "head_rice_pct", "chalkiness_deg_pct", "quality_top2", "amylose_pct",
    "gel_mm", "lw_ratio", "neck_blast_ok", "blb_grade", "yield_gain_pct",
    "gain_prod_pct", "yield_2yr_kg_mu", "duration_d", "plant_height_cm",
    "seed_setting_pct", "tgw_g", "grains_per_panicle",
]


def load_main_stratum(df):
    m = df[
        (df.level == "国审")
        & (df.trial_group.isin(TRIAL_GROUPS))
        & (df.approval_year.isin([2017, 2019, 2020, 2021, 2022]))
    ].copy()
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    m["approval_year"] = m.approval_year.astype(int)
    m["cell"] = (
        m.approval_year.astype(str) + "|" + m.trial_group.astype(str) + "|" + m.ck_n.astype(str)
    )
    m["n_nonmissing_fields"] = m[OUTCOME_FIELDS].notna().sum(axis=1)
    return m


def build_arm1(main):
    sub = main[
        (main.approval_year.isin([2019, 2020, 2021, 2022]))
        & (main.channel.isin(["Unified", "Consortium"]))
    ].copy()
    sub["new_channel"] = (sub.channel == "Consortium").astype(int)
    keep = sub.groupby("cell")["new_channel"].transform("nunique") == 2
    sub = sub[keep].copy()
    sub["cell_id"] = pd.factorize(sub.cell)[0]
    return sub


def fit(sub, formula, label):
    d = sub.dropna(subset=["quality_stated", "bsys", "cell_id",
                            "source_text_len", "n_nonmissing_fields"]).copy()
    n_cells = d.cell_id.nunique()
    if n_cells >= 5:
        m = smf.ols(formula, data=d).fit(cov_type="cluster", cov_kwds={"groups": d.cell_id})
        se_type = f"cluster(cell,G={n_cells})"
    else:
        m = smf.ols(formula, data=d).fit(cov_type="HC1")
        se_type = f"HC1(cells={n_cells})"
    b = m.params["new_channel"]
    se = m.bse["new_channel"]
    p = m.pvalues["new_channel"]
    print(f"{label}: beta={b:.4f}, se={se:.4f}, p={p:.4g}, n={int(m.nobs)}, {se_type}")
    return b, se, p, int(m.nobs)


def main():
    df = pd.read_pickle(DATA_PATH)
    main_df = load_main_stratum(df)
    arm1 = build_arm1(main_df)

    print("=== Baseline (Table 3 specification) ===")
    fit(arm1, "quality_stated ~ new_channel + C(cell_id) + C(bsys)", "Baseline")

    print("\n=== With text-length + non-missing-field-count controls ===")
    fit(
        arm1,
        "quality_stated ~ new_channel + source_text_len + n_nonmissing_fields + "
        "C(cell_id) + C(bsys)",
        "With controls",
    )


if __name__ == "__main__":
    main()
