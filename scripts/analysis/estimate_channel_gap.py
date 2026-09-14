"""
estimate_channel_gap.py

Main pre-registered estimation script for
"Who measures what enters the market?" (rice variety approval trial channels).

Implements the model in plan/02_research_route.md §3:
    Y_i = beta * NewChannel_i + gamma_{c(i)} + delta_{b(i)} + eps_i
with c(i) = approval_year x trial_group x check-variety (single interaction
fixed effect, NOT additive trial_group + check, which is collinear -- see
§3.1), and delta_b(i) = breeding system (two-line/three-line/inbred) FE.

Two separate arms are estimated (never pooled as the main result):
    Arm 1: Consortium vs Unified, national approval (国审), trial_group in
           {长江中下游中籼迟熟, 长江上游中籼迟熟}, approval_year in 2019-2022.
    Arm 2: Green vs Unified, same strata, approval_year == 2017.
Cells with only one channel present are dropped (no identifying variation).
Standard errors are clustered by cell when the arm has >=5 effective
clusters; otherwise HC1 is used and the table is flagged.

Outputs:
    manuscript/tables/table3_main_results.csv

Run: python3 scripts/analysis/estimate_channel_gap.py
"""
import warnings
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)

DATA_PATH = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
OUT_TABLE = "/home/user/video/manuscript/tables/table3_main_results.csv"

TRIAL_GROUPS = ["长江中下游中籼迟熟", "长江上游中籼迟熟"]

# 17 outcome variables, per plan §1.2, with measurement-party label
OUTCOMES = [
    ("head_rice_pct",        "3rd-party"),
    ("chalkiness_deg_pct",   "3rd-party"),
    ("quality_stated",       "3rd-party"),
    ("quality_top2",         "3rd-party"),
    ("amylose_pct",          "3rd-party"),
    ("gel_mm",                "3rd-party"),
    ("lw_ratio",             "3rd-party"),
    ("neck_blast_ok",        "3rd-party"),
    ("blb_grade",            "3rd-party"),
    ("yield_gain_pct",       "self-reported"),
    ("gain_prod_pct",        "self-reported"),
    ("yield_2yr_kg_mu",      "self-reported"),
    ("duration_d",           "self-reported"),
    ("plant_height_cm",      "self-reported"),
    ("seed_setting_pct",     "self-reported"),
    ("tgw_g",                "self-reported"),
    ("grains_per_panicle",   "self-reported"),
]


def load_main_stratum(df):
    """国审 x {长江中下游中籼迟熟, 长江上游中籼迟熟} x {2017, 2019-2022}."""
    m = df[
        (df.level == "国审")
        & (df.trial_group.isin(TRIAL_GROUPS))
        & (df.approval_year.isin([2017, 2019, 2020, 2021, 2022]))
    ].copy()
    # quality_stated: announcement carries a stated national/industry quality
    # grade or standard (defined for every record -> no missingness by
    # construction)
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    m["approval_year"] = m.approval_year.astype(int)
    m["cell"] = (
        m.approval_year.astype(str) + "|" + m.trial_group.astype(str) + "|" + m.ck_n.astype(str)
    )
    return m


def build_arm(main, arm):
    if arm == 1:
        sub = main[
            (main.approval_year.isin([2019, 2020, 2021, 2022]))
            & (main.channel.isin(["Unified", "Consortium"]))
        ].copy()
        sub["new_channel"] = (sub.channel == "Consortium").astype(int)
    elif arm == 2:
        sub = main[
            (main.approval_year == 2017) & (main.channel.isin(["Unified", "Green"]))
        ].copy()
        sub["new_channel"] = (sub.channel == "Green").astype(int)
    else:
        raise ValueError(arm)
    # drop cells with only one channel present -> no identifying variation
    keep = sub.groupby("cell")["new_channel"].transform("nunique") == 2
    sub = sub[keep].copy()
    sub["cell_id"] = pd.factorize(sub.cell)[0]
    return sub


def fit_one(sub, outcome):
    d = sub.dropna(subset=[outcome, "bsys", "cell_id"]).copy()
    if d[outcome].nunique() < 2 or d.new_channel.nunique() < 2:
        return None
    n_cells = d.cell_id.nunique()
    formula = f"Q('{outcome}') ~ new_channel + C(cell_id) + C(bsys)"
    try:
        if n_cells >= 5:
            m = smf.ols(formula, data=d).fit(
                cov_type="cluster", cov_kwds={"groups": d.cell_id}
            )
            se_type = f"cluster(cell,G={n_cells})"
        else:
            m = smf.ols(formula, data=d).fit(cov_type="HC1")
            se_type = f"HC1(cells={n_cells})"
    except Exception as e:  # perfect collinearity / singular design etc.
        return {"error": str(e)}
    b = m.params["new_channel"]
    se = m.bse["new_channel"]
    p = m.pvalues["new_channel"]
    ci = m.conf_int().loc["new_channel"]
    return dict(n=int(m.nobs), beta=b, se=se, ci_low=ci[0], ci_high=ci[1], p=p,
                se_type=se_type, n_cells=n_cells)


def bh_fdr(pvals):
    """Benjamini-Hochberg q-values."""
    p = np.array(pvals, dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order]
    q = ranked * n / (np.arange(n) + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    q = np.clip(q, 0, 1)
    out = np.empty(n)
    out[order] = q
    return out


def main():
    df = pd.read_pickle(DATA_PATH)
    main_df = load_main_stratum(df)
    print(f"Main stratum n = {len(main_df)} "
          f"(Unified {(main_df.channel=='Unified').sum()} / "
          f"Consortium {(main_df.channel=='Consortium').sum()} / "
          f"Green {(main_df.channel=='Green').sum()})")

    arm1 = build_arm(main_df, 1)
    arm2 = build_arm(main_df, 2)
    print(f"Arm 1 (Consortium vs Unified, 2019-2022): n = {len(arm1)}, "
          f"cells = {arm1.cell.nunique()}")
    print(f"Arm 2 (Green vs Unified, 2017): n = {len(arm2)}, "
          f"cells = {arm2.cell.nunique()}")

    rows = []
    for arm_label, sub in [("Arm1_Consortium_vs_Unified", arm1),
                            ("Arm2_Green_vs_Unified", arm2)]:
        for outcome, party in OUTCOMES:
            res = fit_one(sub, outcome)
            if res is None:
                rows.append(dict(arm=arm_label, outcome=outcome,
                                  measurement_party=party, n=np.nan,
                                  beta=np.nan, se=np.nan, ci_low=np.nan,
                                  ci_high=np.nan, p=np.nan, se_type="insufficient_variation"))
                continue
            if "error" in res:
                rows.append(dict(arm=arm_label, outcome=outcome,
                                  measurement_party=party, n=np.nan,
                                  beta=np.nan, se=np.nan, ci_low=np.nan,
                                  ci_high=np.nan, p=np.nan, se_type="error:" + res["error"][:60]))
                continue
            rows.append(dict(arm=arm_label, outcome=outcome, measurement_party=party,
                              n=res["n"], beta=res["beta"], se=res["se"],
                              ci_low=res["ci_low"], ci_high=res["ci_high"],
                              p=res["p"], se_type=res["se_type"]))

    table = pd.DataFrame(rows)

    # BH-FDR within each arm, over the 17 outcomes with a valid p-value
    table["bh_q"] = np.nan
    for arm_label in table.arm.unique():
        mask = (table.arm == arm_label) & table.p.notna()
        if mask.sum() > 0:
            table.loc[mask, "bh_q"] = bh_fdr(table.loc[mask, "p"].values)

    cols = ["arm", "outcome", "measurement_party", "n", "beta", "se",
            "ci_low", "ci_high", "p", "bh_q", "se_type"]
    table = table[cols]
    table.to_csv(OUT_TABLE, index=False)
    print(f"\nWrote {OUT_TABLE}")
    print(table.round(4).to_string(index=False))

    # --- sanity check against numbers already reported in 01_theme_and_innovation.md ---
    print("\n=== Cross-check against 01_theme_and_innovation.md §5/§9 (Arm 1) ===")
    checks = [
        ("head_rice_pct", -1.844, None),
        ("chalkiness_deg_pct", 1.108, 0.012),
        ("quality_stated", -0.122, 0.008),
        ("yield_gain_pct", 0.554, 0.020),
        ("gain_prod_pct", 0.919, None),
        ("blb_grade", -0.190, None),
    ]
    a1 = table[table.arm == "Arm1_Consortium_vs_Unified"].set_index("outcome")
    for outcome, exp_b, exp_p in checks:
        got_b = a1.loc[outcome, "beta"]
        got_p = a1.loc[outcome, "p"]
        print(f"  {outcome:22s} expected beta={exp_b:+.3f}  got beta={got_b:+.4f}  "
              f"| got p={got_p:.4g}" + (f" (expected p={exp_p})" if exp_p else ""))

    return table, arm1, arm2, main_df


if __name__ == "__main__":
    main()
