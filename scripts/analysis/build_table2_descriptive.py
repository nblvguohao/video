"""
build_table2_descriptive.py

Builds Table 2 (descriptive statistics and balance, main analysis stratum)
for "Who measures what enters the market?" from analysis_rice_channel.pkl.

Sample: national approvals (国审), two dominant mid-season indica trial
groups, 2017 and 2019-2022 (n = 878: Unified 406 / Consortium 405 / Green 67)
-- identical stratum definition to estimate_channel_gap.py's load_main_stratum().

For each of the 17 outcome variables used in Table 3, reports mean, SD and
non-missing rate by channel arm (Unified / Consortium / Green).

Output: manuscript/tables/table2_descriptive_balance.md (replaces the
placeholder file).

Run: python3 scripts/analysis/build_table2_descriptive.py
"""
import numpy as np
import pandas as pd

DATA_PATH = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
OUT_PATH = "/home/user/video/manuscript/tables/table2_descriptive_balance.md"

TRIAL_GROUPS = ["长江中下游中籼迟熟", "长江上游中籼迟熟"]

OUTCOMES = [
    ("head_rice_pct",      "Head-rice percentage (%)"),
    ("chalkiness_deg_pct", "Chalkiness degree (%)"),
    ("quality_stated",     "Quality grade stated (0/1)"),
    ("quality_top2",       "Top-two quality grade (0/1)"),
    ("amylose_pct",        "Amylose content (%)"),
    ("gel_mm",             "Gel consistency (mm)"),
    ("lw_ratio",           "Grain length-width ratio"),
    ("neck_blast_ok",      "Neck-blast tolerance OK (0/1)"),
    ("blb_grade",          "Bacterial-blight grade"),
    ("yield_gain_pct",     "Regional-trial yield gain over check (pp)"),
    ("gain_prod_pct",      "Production-trial yield gain over check (pp)"),
    ("yield_2yr_kg_mu",    "Two-year regional-trial yield (kg/mu)"),
    ("duration_d",         "Growth duration (days)"),
    ("plant_height_cm",    "Plant height (cm)"),
    ("seed_setting_pct",   "Seed-setting percentage (%)"),
    ("tgw_g",              "Thousand-grain weight (g)"),
    ("grains_per_panicle", "Grains per panicle"),
]

ARMS = ["Unified", "Consortium", "Green"]


def load_main_stratum(df):
    m = df[
        (df.level == "国审")
        & (df.trial_group.isin(TRIAL_GROUPS))
        & (df.approval_year.isin([2017, 2019, 2020, 2021, 2022]))
    ].copy()
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    return m


def main():
    df = pd.read_pickle(DATA_PATH)
    m = load_main_stratum(df)
    n_by_arm = m.channel.value_counts().reindex(ARMS).fillna(0).astype(int)
    print("n by arm:", n_by_arm.to_dict())

    lines = []
    lines.append("# Table 2. Descriptive statistics and balance, main analysis stratum\n")
    lines.append(
        "Sample: national approvals (国审), two dominant mid-season indica trial groups "
        "(middle-and-lower-Yangtze; upper-Yangtze), 2017 and 2019-2022. "
        f"n = {n_by_arm.sum()} (Unified {n_by_arm['Unified']} / Consortium "
        f"{n_by_arm['Consortium']} / Green {n_by_arm['Green']}). "
        "Computed directly from `analysis_rice_channel.pkl` by "
        "`scripts/analysis/build_table2_descriptive.py`; means and SDs are reported "
        "on the non-missing observations for each cell, and the non-missing rate is "
        "reported separately so a reader can see where an arm's mean is based on a "
        "materially smaller effective sample (cf. Section 3.3 and Table 3's n columns).\n"
    )

    header = (
        "| Outcome | Unified mean (SD) | Consortium mean (SD) | Green mean (SD) "
        "| Unified % non-missing | Consortium % non-missing | Green % non-missing |"
    )
    sep = "|---|---|---|---|---|---|---|"
    lines.append(header)
    lines.append(sep)

    for col, label in OUTCOMES:
        row = [label]
        pct_row = []
        for arm in ARMS:
            sub = m[m.channel == arm]
            vals = pd.to_numeric(sub[col], errors="coerce")
            n_tot = len(sub)
            n_nm = vals.notna().sum()
            pct = 100.0 * n_nm / n_tot if n_tot > 0 else float("nan")
            if n_nm > 0:
                mean = vals.mean()
                sd = vals.std()
                row.append(f"{mean:.3f} ({sd:.3f})")
            else:
                row.append("--")
            pct_row.append(f"{pct:.1f}")
        lines.append("| " + " | ".join(row + pct_row) + " |")

    lines.append(
        "\nNotes: `quality_stated` and `neck_blast_ok` and `quality_top2` are 0/1 "
        "indicators; their \"mean\" is the proportion coded 1. `quality_stated` is "
        "non-missing by construction (100% in every arm) because it is defined as the "
        "union of two underlying fields (Section 3.3). Non-missing-rate imbalances of "
        "8 percentage points or more between Unified and Consortium are the same three "
        "flagged in Section 3.3/6.7 (Manski bounds, R7): `quality_top2`, "
        "`yield_gain_pct`, and `yield_2yr_kg_mu`. `bsys` (breeding-system fixed effect) "
        "and `trial_group` distributions by channel are reported in Table 1 and "
        "`table1_channel_by_year.csv`; they are not repeated here to avoid duplicating "
        "that table."
    )

    with open(OUT_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
