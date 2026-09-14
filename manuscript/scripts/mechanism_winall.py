"""
Group D tasks: Winall (荃银高科) mechanism section — quantitative analysis.
Produces:
  - Logit: Pr(NewChannel) ~ Winall + year x trial_group FE  (national, 2017+2019-2022)
  - Within-channel positioning regressions (Unified subsample; New subsample) for Winall
  - R10 robustness: drop all Winall records, re-run arm-1 main spec
  - Descriptive Public vs Enterprise regression (Table 7)
  - Company panel assembly (Table 6)
All numbers printed and written to CSV under manuscript/tables/.
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.width", 140)

DATA = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
OUTDIR = "/home/user/video/manuscript/tables"

df = pd.read_pickle(DATA)

# ---------- construct cell fixed effect ----------
df["cell"] = (df["approval_year"].astype("Int64").astype(str) + "|" +
              df["trial_group"].astype(str) + "|" +
              df["ck_n"].astype(str))

# "quality_stated" = 1 if the announcement states a national/industry quality grade
# (quality_grade non-missing), 0 otherwise. Defined for every record -> no missingness
# by construction (this is what 02_research_route.md calls the "载明行为" indicator).
df["quality_stated"] = df["quality_grade"].notna().astype(int)

national = df[df.level == "国审"].copy()

# main analysis sample restricted to the two major indica trial groups (arm 1 window)
two_indica = national[national.region_group.isin(
    ["长江中下游中籼迟熟组", "长江上游中籼迟熟组"])].copy()

arm1_years = [2019, 2020, 2021, 2022]
arm1 = two_indica[(two_indica.approval_year.isin(arm1_years)) &
                   (two_indica.channel.isin(["Unified", "Consortium"]))].copy()
arm1["new_channel"] = (arm1.channel == "Consortium").astype(int)

# drop singleton cells (no within-cell variation in channel)
def drop_singleton_cells(d, cellcol="cell", treat="new_channel"):
    g = d.groupby(cellcol)[treat].nunique()
    keep_cells = g[g > 1].index
    return d[d[cellcol].isin(keep_cells)].copy()

arm1_id = drop_singleton_cells(arm1)

print("=" * 80)
print("SANITY CHECKS")
print("=" * 80)
print("national 2017+2019-2022 n =", national[national.approval_year.isin([2017,2019,2020,2021,2022])].shape[0])

winall_nat = national[national.approval_year.isin([2017,2019,2020,2021,2022])]
w = winall_nat[winall_nat.winall]
o = winall_nat[~winall_nat.winall]
print(f"Winall n={len(w)}, Unified share={ (w.channel=='Unified').mean():.4f}")
print(f"Others n={len(o)}, Unified share={ (o.channel=='Unified').mean():.4f}")

# =====================================================================
# TASK 1: Winall channel-choice logit
#   Pr(NewChannel) = Λ(α·Winall + year × trial_group FE)
#   sample: national, 2017 + 2019-2022, two major indica trial groups
# =====================================================================
print("\n" + "=" * 80)
print("TASK 1: Winall channel-choice Logit (two indica trial groups, 2017+2019-2022)")
print("=" * 80)

logit_years = [2017, 2019, 2020, 2021, 2022]
logit_sample = two_indica[two_indica.approval_year.isin(logit_years)].copy()
logit_sample["new_channel"] = logit_sample["new_channel"].astype(int)
logit_sample["yxg"] = (logit_sample["approval_year"].astype(int).astype(str) + "_" +
                        logit_sample["trial_group"].astype(str))

print("Logit sample (two indica groups) n =", len(logit_sample))
print("Winall n =", logit_sample.winall.sum(), " share unified (winall) =",
      (logit_sample.loc[logit_sample.winall, "channel"] == "Unified").mean())
print("share unified (others) =",
      (logit_sample.loc[~logit_sample.winall, "channel"] == "Unified").mean())

# drop yxg singleton categories (no variation) to allow FE logit to converge
vc = logit_sample["yxg"].value_counts()
keep = vc[vc >= 2].index
logit_fe_sample = logit_sample[logit_sample.yxg.isin(keep)].copy()

def get_param_name(model, base="winall"):
    for name in model.params.index:
        if name == base or name.startswith(base + "["):
            return name
    return None

try:
    logit_fe_sample["winall_i"] = logit_fe_sample["winall"].astype(int)
    m1 = smf.logit("new_channel ~ winall_i + C(yxg)", data=logit_fe_sample).fit(disp=0, maxiter=200)
    pn = get_param_name(m1, "winall_i")
    print(m1.summary2().tables[1].loc[[pn]])
    or_winall = np.exp(m1.params[pn])
    print("Odds ratio (winall) =", or_winall)
except Exception as e:
    print("Full-sample FE logit failed:", e)
    m1 = None
    pn = None

# Also replicate the headline descriptive comparison at national level, all region groups
# (this is what §7 Increment C actually reports: n=166 vs n=1101)
all_nat = national[national.approval_year.isin(logit_years)].copy()
all_nat["new_channel"] = all_nat["new_channel"].astype(int)
all_nat["yxg"] = (all_nat["approval_year"].astype(int).astype(str) + "_" +
                   all_nat["trial_group"].astype(str))
w_all = all_nat[all_nat.winall]
o_all = all_nat[~all_nat.winall]
print("\n--- Descriptive replication (all national region groups, matches Increment C) ---")
print(f"Winall n={len(w_all)}, % Unified = {(w_all.channel=='Unified').mean()*100:.1f}%")
print(f"Others n={len(o_all)}, % Unified = {(o_all.channel=='Unified').mean()*100:.1f}%")

vc2 = all_nat["yxg"].value_counts()
keep2 = vc2[vc2 >= 2].index
all_nat_fe = all_nat[all_nat.yxg.isin(keep2)].copy()
all_nat_fe["winall_i"] = all_nat_fe["winall"].astype(int)
try:
    m1b = smf.logit("new_channel ~ winall_i + C(yxg)", data=all_nat_fe).fit(disp=0, maxiter=300)
    pnb = get_param_name(m1b, "winall_i")
    print(m1b.summary2().tables[1].loc[[pnb]])
    print("Odds ratio (winall, all-groups sample) =", np.exp(m1b.params[pnb]))
except Exception as e:
    print("All-groups FE logit failed:", e)
    m1b = None
    pnb = None

# Simple (no-FE) logit as a robustness/plain-vanilla cross check
all_nat["winall_i"] = all_nat["winall"].astype(int)
m1_simple = smf.logit("new_channel ~ winall_i", data=all_nat).fit(disp=0)
print("\nSimple logit (no FE), all national 2017+2019-2022:")
print(m1_simple.summary2().tables[1])
print("Odds ratio =", np.exp(m1_simple.params["winall_i"]))

# =====================================================================
# TASK 2: within-channel positioning regressions for Winall
#   Y = rho*Winall + cell FE + bsys FE, separately in Unified and New (Consortium+Green) subsamples
#   sample: national, two major indica trial groups, 2017+2019-2022 (arm-1 window definition)
# =====================================================================
print("\n" + "=" * 80)
print("TASK 2: Within-channel positioning regressions (Winall)")
print("=" * 80)
print("Sample: national approvals, ALL trial groups, reform window (2017 + 2019-2022).")
print("This is the specification that reproduces the plan's headline Table 5 numbers")
print("most closely; the two-indica-group restriction (arm-1 window) is reported as a")
print("robustness variant below.")

pos_years = [2017, 2019, 2020, 2021, 2022]
pos_sample = national[national.approval_year.isin(pos_years)].copy()

unified_sub = pos_sample[pos_sample.channel == "Unified"].copy()
new_sub = pos_sample[pos_sample.channel.isin(["Consortium", "Green"])].copy()

def cell_nonsingleton(d, cellcol="cell"):
    g = d.groupby(cellcol)["winall"].nunique()
    keep_cells = g[g > 1].index
    return d[d[cellcol].isin(keep_cells)].copy()

outcomes = {
    "head_rice_pct": "整精米率 (head-rice %)",
    "quality_stated": "载明国家米质等级 (quality grade stated, 0/1)",
    "chalkiness_deg_pct": "垩白度 (chalkiness %)",
}

results_tab5 = []

for label, sub in [("Unified", unified_sub), ("New(Consortium+Green)", new_sub)]:
    sub_id = cell_nonsingleton(sub)
    print(f"\n--- {label} subsample, n(before cell-drop)={len(sub)}, n(after)={len(sub_id)} ---")
    for outc, desc in outcomes.items():
        d = sub_id.dropna(subset=[outc, "winall", "cell", "bsys"]).copy()
        if d["winall"].nunique() < 2 or len(d) < 10:
            print(f"  {outc}: insufficient variation/n, skipped (n={len(d)})")
            continue
        try:
            model = smf.ols(f"{outc} ~ winall + C(cell) + C(bsys)", data=d).fit(
                cov_type="cluster", cov_kwds={"groups": d["cell"]})
            coef = model.params.get("winall[T.True]", model.params.get("winall", np.nan))
            se = model.bse.get("winall[T.True]", model.bse.get("winall", np.nan))
            pval = model.pvalues.get("winall[T.True]", model.pvalues.get("winall", np.nan))
            n = int(model.nobs)
        except Exception as e:
            print(f"  {outc}: model failed ({e})")
            continue
        print(f"  {outc} ({desc}): rho={coef:.4f}, se={se:.4f}, p={pval:.4g}, n={n}")
        results_tab5.append(dict(channel_subsample=label, outcome=outc, outcome_label=desc,
                                  rho=coef, se=se, p=pval, n=n))

tab5 = pd.DataFrame(results_tab5)
tab5.to_csv(f"{OUTDIR}/table5_winall_positioning.csv", index=False)
print("\nSaved:", f"{OUTDIR}/table5_winall_positioning.csv")
print(tab5)

# =====================================================================
# TASK 1b: also save channel-choice descriptive + logit table
# =====================================================================
logit_rows = []
logit_rows.append(dict(spec="descriptive_share_unified_all_national_groups",
                        group="Winall", n=len(w_all), share_unified=(w_all.channel=='Unified').mean()))
logit_rows.append(dict(spec="descriptive_share_unified_all_national_groups",
                        group="Others", n=len(o_all), share_unified=(o_all.channel=='Unified').mean()))
if m1b is not None:
    logit_rows.append(dict(spec="logit_FE_yeartrialgroup_all_national_groups",
                            group="Winall coefficient (alpha)", n=int(m1b.nobs),
                            coef=m1b.params[pnb], se=m1b.bse[pnb], p=m1b.pvalues[pnb],
                            odds_ratio=np.exp(m1b.params[pnb])))
if m1 is not None:
    logit_rows.append(dict(spec="logit_FE_yeartrialgroup_two_indica_groups",
                            group="Winall coefficient (alpha)", n=int(m1.nobs),
                            coef=m1.params[pn], se=m1.bse[pn], p=m1.pvalues[pn],
                            odds_ratio=np.exp(m1.params[pn])))
logit_rows.append(dict(spec="logit_no_FE_all_national_groups",
                        group="Winall coefficient (alpha)", n=int(m1_simple.nobs),
                        coef=m1_simple.params["winall_i"], se=m1_simple.bse["winall_i"],
                        p=m1_simple.pvalues["winall_i"], odds_ratio=np.exp(m1_simple.params["winall_i"])))
logit_tab = pd.DataFrame(logit_rows)
logit_tab.to_csv(f"{OUTDIR}/table5b_winall_channel_choice_logit.csv", index=False)
print("\nSaved:", f"{OUTDIR}/table5b_winall_channel_choice_logit.csv")
print(logit_tab)

# =====================================================================
# TASK 3: R10 robustness — drop all Winall records, re-run arm-1 main spec
# =====================================================================
print("\n" + "=" * 80)
print("TASK 3: R10 robustness (drop Winall, arm 1 main spec)")
print("=" * 80)

arm1_nowinall = arm1_id[~arm1_id.winall].copy()
arm1_nowinall = drop_singleton_cells(arm1_nowinall)
print("arm1 (Consortium vs Unified) n after dropping Winall & singleton cells:", len(arm1_nowinall))

r10_outcomes = {
    "head_rice_pct": "整精米率 (head-rice %)",
    "chalkiness_deg_pct": "垩白度 (chalkiness %)",
    "quality_stated": "载明国家米质等级 (0/1)",
}
r10_rows = []
for outc, desc in r10_outcomes.items():
    d = arm1_nowinall.dropna(subset=[outc, "new_channel", "cell", "bsys"]).copy()
    try:
        model = smf.ols(f"{outc} ~ new_channel + C(cell) + C(bsys)", data=d).fit(
            cov_type="cluster", cov_kwds={"groups": d["cell"]})
        coef = model.params.get("new_channel", np.nan)
        se = model.bse.get("new_channel", np.nan)
        pval = model.pvalues.get("new_channel", np.nan)
        n = int(model.nobs)
    except Exception as e:
        print(f"{outc}: failed {e}")
        continue
    print(f"{outc}: beta={coef:.4f} (se={se:.4f}), p={pval:.4g}, n={n}")
    r10_rows.append(dict(outcome=outc, outcome_label=desc, beta=coef, se=se, p=pval, n=n))

r10_tab = pd.DataFrame(r10_rows)
r10_tab.to_csv(f"{OUTDIR}/table_r10_drop_winall_robustness.csv", index=False)
print("\nSaved:", f"{OUTDIR}/table_r10_drop_winall_robustness.csv")

# =====================================================================
# TASK 4: Public vs Enterprise descriptive regression (Table 7)
#   Y = theta*Public + year x trial_group FE + bsys FE
#   sample: main analysis layer, two indica groups, years with applicant_type labeled
# =====================================================================
print("\n" + "=" * 80)
print("TASK 4: Enterprise vs Public descriptive regression (Table 7)")
print("=" * 80)

# main analysis layer per plan: national, two large indica trial groups, 2005-2022, years with applicant field
main_layer = two_indica[two_indica.approval_year.between(2005, 2022)].copy()
main_layer = main_layer[main_layer.applicant_type.isin(["Public", "Enterprise"])].copy()
main_layer["public"] = (main_layer.applicant_type == "Public").astype(int)
main_layer["yxg"] = (main_layer["approval_year"].astype(int).astype(str) + "_" +
                      main_layer["trial_group"].astype(str))

print("Table7 sample n =", len(main_layer))
print(main_layer["applicant_type"].value_counts())

t7_outcomes = {
    "yield_2yr_kg_mu": "区试亩产 (regional-trial yield, kg/mu)",
    "tgw_g": "千粒重 (1000-grain weight, g)",
    "chalkiness_deg_pct": "垩白度 (chalkiness, %)",
    "head_rice_pct": "整精米率 (head-rice %)",
}
t7_rows = []
for outc, desc in t7_outcomes.items():
    d = main_layer.dropna(subset=[outc, "public", "yxg", "bsys"]).copy()
    vc3 = d["yxg"].value_counts()
    d = d[d.yxg.isin(vc3[vc3 >= 2].index)]
    try:
        model = smf.ols(f"{outc} ~ public + C(yxg) + C(bsys)", data=d).fit(
            cov_type="cluster", cov_kwds={"groups": d["yxg"]})
        coef = model.params.get("public", np.nan)
        se = model.bse.get("public", np.nan)
        pval = model.pvalues.get("public", np.nan)
        n = int(model.nobs)
    except Exception as e:
        print(f"{outc}: failed {e}")
        continue
    print(f"{outc} ({desc}): theta={coef:.4f} (se={se:.4f}), p={pval:.4g}, n={n}")
    t7_rows.append(dict(outcome=outc, outcome_label=desc, theta=coef, se=se, p=pval, n=n))

t7_tab = pd.DataFrame(t7_rows)
t7_tab.to_csv(f"{OUTDIR}/table7_enterprise_vs_public.csv", index=False)
print("\nSaved:", f"{OUTDIR}/table7_enterprise_vs_public.csv")

print("\nALL TASKS 1-4 DONE.")
