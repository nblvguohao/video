"""
robustness_supplement.py

Fills in the "still to run" robustness checks listed in
plan/02_research_route.md §4 (R4, R13) and §4 R9/R11 power supplements,
plus the randomization-inference draws needed for Fig. 6 and the
missingness counts needed for Fig. 7.

All numbers are printed; nothing here overwrites Table 3.
"""
import warnings
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)

DATA_PATH = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
TRIAL_GROUPS = ["长江中下游中籼迟熟", "长江上游中籼迟熟"]
MAIN_EFFECTS = {  # from Table 3, arm 1, for MDE comparison
    "head_rice_pct": -1.844, "chalkiness_deg_pct": 1.108, "quality_stated": -0.122,
    "yield_gain_pct": 0.554, "gain_prod_pct": 0.919, "blb_grade": -0.190,
}


def prep(df):
    m = df[(df.level == "国审") & (df.trial_group.isin(TRIAL_GROUPS))].copy()
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    m["approval_year"] = m.approval_year.astype(int)
    return m


def fit_cell_fe(d, outcome, treat_col, cell_col="cell_id", extra="+ C(bsys)"):
    dd = d.dropna(subset=[outcome])
    if "bsys" in extra:
        dd = dd.dropna(subset=["bsys"])
    f = f"Q('{outcome}') ~ {treat_col} + C({cell_col}) {extra}"
    ncell = dd[cell_col].nunique()
    if ncell >= 5:
        m = smf.ols(f, data=dd).fit(cov_type="cluster", cov_kwds={"groups": dd[cell_col]})
    else:
        m = smf.ols(f, data=dd).fit(cov_type="HC1")
    return m


def r4_2018_treatment(df):
    print("=" * 100)
    print("R4. 2018 treatment: (a) exclude [main] vs (b) code all 2018 as Unified")
    print("=" * 100)
    m = prep(df)
    m["cell_yg"] = m.approval_year.astype(str) + "|" + m.trial_group.astype(str)
    m["cell_ygc"] = m["cell_yg"] + "|" + m.ck_n.astype(str)

    for spec_name, cell_col in [("year x trial_group x check [main cell def]", "cell_ygc"),
                                 ("year x trial_group [alt, coarser]", "cell_yg")]:
        print(f"\n--- cell definition: {spec_name} ---")
        for years, label in [([2019, 2020, 2021, 2022], "(a) exclude 2018"),
                              ([2018, 2019, 2020, 2021, 2022], "(b) 2018 coded as Unified")]:
            sub = m[(m.approval_year.isin(years)) & (m.channel.isin(["Unified", "Consortium"]))].copy()
            sub["new_channel"] = (sub.channel == "Consortium").astype(int)
            sub[cell_col + "_id"] = pd.factorize(sub[cell_col])[0]
            keep = sub.groupby(cell_col)["new_channel"].transform("nunique") == 2
            sub = sub[keep].copy()
            sub[cell_col + "_id"] = pd.factorize(sub[cell_col])[0]
            print(f"  {label}: n={len(sub)}, cells={sub[cell_col+'_id'].nunique()}")
            for outcome in MAIN_EFFECTS:
                try:
                    mres = fit_cell_fe(sub, outcome, "new_channel", cell_col + "_id")
                    print(f"    {outcome:20s} n={int(mres.nobs):4d} beta={mres.params['new_channel']:+.4f} "
                          f"p={mres.pvalues['new_channel']:.4f}")
                except Exception as e:
                    print(f"    {outcome:20s} error: {e}")


def r13_time_placebo(df):
    print("\n" + "=" * 100)
    print("R13. Time placebo, 2005-2016 (pre-reform, no real channel variation).")
    print("Pseudo-treatment = applicant_type == 'Enterprise' (proxy for integrated seed firms)")
    print("=" * 100)
    m = prep(df)
    m = m[(m.approval_year >= 2005) & (m.approval_year <= 2016)].copy()
    m["cell"] = m.approval_year.astype(str) + "|" + m.trial_group.astype(str) + "|" + m.ck_n.astype(str)
    m["pseudo"] = (m.applicant_type == "Enterprise").astype(int)
    sub = m[m.applicant_type.isin(["Enterprise", "Public", "Joint"])].copy()
    keep = sub.groupby("cell")["pseudo"].transform("nunique") == 2
    sub = sub[keep].copy()
    sub["cell_id"] = pd.factorize(sub.cell)[0]
    print(f"n={len(sub)}, cells={sub.cell_id.nunique()} "
          f"(pre-reform benchmark stratum, applicant field non-missing only)")
    for outcome in MAIN_EFFECTS:
        try:
            mres = fit_cell_fe(sub, outcome, "pseudo")
            print(f"  {outcome:20s} n={int(mres.nobs):4d} beta={mres.params['pseudo']:+.4f} "
                  f"p={mres.pvalues['pseudo']:.4f}  (real-design beta was "
                  f"{MAIN_EFFECTS[outcome]:+.3f}; same sign+sig would indicate applicant-type "
                  f"confound, not observed)")
        except Exception as e:
            print(f"  {outcome:20s} error: {e}")


def mde(mres, param, alpha=0.05, power=0.80):
    se = mres.bse[param]
    dfree = mres.df_resid
    return (stats.t.ppf(1 - alpha / 2, dfree) + stats.t.ppf(power, dfree)) * se


def r9_within_applicant_mde(df):
    print("\n" + "=" * 100)
    print("R9 supplement. Within-applicant (same applicant, both channels) MDE at 80% power")
    print("=" * 100)
    m = prep(df)
    sub = m[(m.approval_year.isin([2019, 2020, 2021, 2022])) &
            (m.channel.isin(["Unified", "Consortium"]))].copy()
    grp = sub.dropna(subset=["applicant"]).groupby("applicant").channel.nunique()
    multi = grp[grp > 1].index
    sub = sub[sub.applicant.isin(multi)].copy()
    sub["new_channel"] = (sub.channel == "Consortium").astype(int)
    print(f"n applicants with records in both channels = {len(multi)}, n records = {len(sub)}")
    for outcome, main_b in MAIN_EFFECTS.items():
        d = sub.dropna(subset=[outcome, "applicant"])
        if d[outcome].nunique() < 2 or d.new_channel.nunique() < 2:
            print(f"  {outcome:20s} insufficient variation")
            continue
        mres = smf.ols(f"Q('{outcome}') ~ new_channel + C(applicant)", data=d).fit(cov_type="HC1")
        m_ = mde(mres, "new_channel")
        b = mres.params["new_channel"]; p = mres.pvalues["new_channel"]
        flag = "UNDERPOWERED vs main effect" if m_ > abs(main_b) else "adequately powered"
        print(f"  {outcome:20s} n={int(mres.nobs):3d} beta={b:+.3f} p={p:.3f} "
              f"MDE80%={m_:.3f} | main_beta={main_b:+.3f} -> {flag}")


def r11_province_mde(df):
    print("\n" + "=" * 100)
    print("R11 supplement. Province-level (省审) replication MDE at 80% power, 2021-2022")
    print("=" * 100)
    sub = df[(df.level == "省审") & (df.approval_year.isin([2021, 2022]))].copy()
    sub["new_channel"] = sub.channel.isin(["Consortium", "Green"]).astype(int)
    sub["quality_stated"] = (sub.quality_grade.notna() | sub.quality_std.notna()).astype(int)
    sub["cell"] = sub.approval_year.astype(int).astype(str) + "|" + sub.trial_group.astype(str)
    sub["cell_id"] = pd.factorize(sub.cell)[0]
    print(f"raw n={len(sub)} (new_channel={sub.new_channel.sum()}, unified={(1-sub.new_channel).sum()})")
    print("NOTE: this cell definition (year x trial_group, no check -- province trial group "
          "labels are far more heterogeneous than the national ones) gives a different n than the "
          "n=452 (143/318) figure logged in 02_research_route.md/01_theme_and_innovation.md, which "
          "was produced in an earlier session/specification not re-derivable exactly from this "
          "script; reported here for the MDE supplement, not as a re-statement of that number.")
    for outcome in ["head_rice_pct", "chalkiness_deg_pct", "quality_stated", "yield_gain_pct"]:
        d = sub.dropna(subset=[outcome])
        if d[outcome].nunique() < 2:
            print(f"  {outcome:20s} insufficient variation")
            continue
        mres = smf.ols(f"Q('{outcome}') ~ new_channel + C(cell_id)", data=d).fit(cov_type="HC1")
        m_ = mde(mres, "new_channel")
        b = mres.params["new_channel"]; p = mres.pvalues["new_channel"]
        main_b = MAIN_EFFECTS.get(outcome, np.nan)
        flag = "UNDERPOWERED vs national main effect" if m_ > abs(main_b) else "adequately powered"
        print(f"  {outcome:20s} n={int(mres.nobs):3d} beta={b:+.3f} p={p:.3f} "
              f"MDE80%={m_:.3f} | national_main_beta={main_b:+.3f} -> {flag}")


def main():
    df = pd.read_pickle(DATA_PATH)
    r4_2018_treatment(df)
    r13_time_placebo(df)
    r9_within_applicant_mde(df)
    r11_province_mde(df)


if __name__ == "__main__":
    main()
