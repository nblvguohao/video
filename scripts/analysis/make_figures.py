"""
make_figures.py

Generates Fig. 2 (forest plot, main results), Fig. 6 (randomization
inference), and Fig. 7 (missingness balance) per plan/02_research_route.md
§7. All labels are in English; no external fonts required.

Run: python3 scripts/analysis/make_figures.py
"""
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from plot_style import apply as apply_style

warnings.filterwarnings("ignore")
apply_style()

DATA_PATH = "/home/user/video/evidence/data/analysis_rice_channel.pkl"
TABLE3_PATH = "/home/user/video/manuscript/tables/table3_main_results.csv"
FIG_DIR = "/home/user/video/manuscript/figures"
TRIAL_GROUPS = ["长江中下游中籼迟熟", "长江上游中籼迟熟"]

OUTCOME_LABELS = {
    "head_rice_pct": "Head rice rate (%)",
    "chalkiness_deg_pct": "Chalkiness degree (%)",
    "quality_stated": "Quality grade stated (0/1)",
    "quality_top2": "Quality grade 1-2 (0/1)",
    "amylose_pct": "Amylose (%)",
    "gel_mm": "Gel consistency (mm)",
    "lw_ratio": "Length-width ratio",
    "neck_blast_ok": "Neck blast OK (0/1)",
    "blb_grade": "Bacterial blight grade",
    "yield_gain_pct": "Yield gain vs check (pp, trial)",
    "gain_prod_pct": "Yield gain vs check (pp, production)",
    "yield_2yr_kg_mu": "2-yr trial yield (kg/mu)",
    "duration_d": "Growth duration (d)",
    "plant_height_cm": "Plant height (cm)",
    "seed_setting_pct": "Seed setting (%)",
    "tgw_g": "1000-grain weight (g)",
    "grains_per_panicle": "Grains per panicle",
}
OUTCOME_ORDER = list(OUTCOME_LABELS.keys())

COLOR_3RD = "#2166ac"   # blue: third-party assayed
COLOR_SELF = "#b2182b"  # red: applicant self-reported


# ---------------------------------------------------------------------------
# Fig. 2: forest plot of Table 3
# ---------------------------------------------------------------------------
def fig2_forest():
    t3 = pd.read_csv(TABLE3_PATH)
    fig, axes = plt.subplots(1, 2, figsize=(11, 7), sharey=True)
    arm_titles = {
        "Arm1_Consortium_vs_Unified": "Arm 1: Consortium vs Unified (2019-2022)",
        "Arm2_Green_vs_Unified": "Arm 2: Green vs Unified (2017)",
    }
    y_positions = {o: i for i, o in enumerate(reversed(OUTCOME_ORDER))}

    for ax, arm in zip(axes, ["Arm1_Consortium_vs_Unified", "Arm2_Green_vs_Unified"]):
        sub = t3[t3.arm == arm].set_index("outcome")
        for i, outcome in enumerate(OUTCOME_ORDER):
            if i % 2 == 0:
                ax.axhspan(i - 0.5, i + 0.5, color="#9a9aa5", alpha=0.07, zorder=0, lw=0)
        for outcome in OUTCOME_ORDER:
            if outcome not in sub.index:
                continue
            row = sub.loc[outcome]
            y = y_positions[outcome]
            color = COLOR_3RD if row.measurement_party == "3rd-party" else COLOR_SELF
            if pd.isna(row.beta):
                ax.text(0, y, "not estimable", va="center", ha="center", fontsize=7,
                        color="gray", style="italic")
                continue
            sig = row.get("p", 1.0) is not None and not pd.isna(row.get("p", None)) and row.get("p", 1.0) < 0.05
            ax.errorbar(row.beta, y, xerr=[[row.beta - row.ci_low], [row.ci_high - row.beta]],
                        fmt="o", color=color, ecolor=color, capsize=3.5, markersize=7 if sig else 5.5,
                        markeredgecolor="white", markeredgewidth=0.8, elinewidth=1.6, zorder=3)
        ax.axvline(0, color="#2a2a33", lw=1.0, ls="--", zorder=1)
        ax.set_title(arm_titles[arm], fontsize=10.5, fontweight="bold")
        ax.set_xlabel(r"$\beta$ (95% CI)")
        ax.grid(axis="x", alpha=0.5)
        ax.grid(axis="y", alpha=0)

    axes[0].set_yticks(list(y_positions.values()))
    axes[0].set_yticklabels([OUTCOME_LABELS[o] for o in reversed(OUTCOME_ORDER)], fontsize=8)

    handles = [plt.Line2D([0], [0], marker="o", color=COLOR_3RD, linestyle="", label="Third-party assayed"),
               plt.Line2D([0], [0], marker="o", color=COLOR_SELF, linestyle="", label="Applicant self-reported")]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle("Fig. 2. Trial-channel gap by outcome, both arms\n"
                  "(cell FE = year x trial group x check; arm 1 clustered SE, arm 2 HC1, n cells = 3)",
                  fontsize=10)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(f"{FIG_DIR}/fig2_forest_main.png", dpi=300, bbox_inches="tight")
    fig.savefig(f"{FIG_DIR}/fig2_forest_main.pdf", bbox_inches="tight")
    plt.close(fig)
    print("wrote fig2_forest_main.{png,pdf}")


# ---------------------------------------------------------------------------
# Fig. 6: randomization inference (permute channel label within cell, x500)
# ---------------------------------------------------------------------------
def fig6_randomization():
    df = pd.read_pickle(DATA_PATH)
    m = df[(df.level == "国审") & (df.trial_group.isin(TRIAL_GROUPS)) &
           (df.approval_year.isin([2017, 2019, 2020, 2021, 2022]))].copy()
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    m["quality_top2"] = m["quality_top2"]
    m["approval_year"] = m.approval_year.astype(int)
    m["cell"] = m.approval_year.astype(str) + "|" + m.trial_group.astype(str) + "|" + m.ck_n.astype(str)

    sub = m[(m.approval_year.isin([2019, 2020, 2021, 2022])) &
            (m.channel.isin(["Unified", "Consortium"]))].copy()
    sub["new_channel"] = (sub.channel == "Consortium").astype(int)
    keep = sub.groupby("cell")["new_channel"].transform("nunique") == 2
    sub = sub[keep].copy()
    sub["cell_id"] = pd.factorize(sub.cell)[0]

    panels = [
        ("head_rice_pct", "Head rice rate (%)"),
        ("chalkiness_deg_pct", "Chalkiness degree (%)"),
        ("yield_gain_pct", "Yield gain vs check (pp, trial)"),
        ("quality_top2", "Quality grade 1-2 (0/1)"),
    ]
    rng = np.random.default_rng(20260914)
    n_perm = 500

    fig, axes = plt.subplots(2, 2, figsize=(9, 7))
    for ax, (outcome, label) in zip(axes.flat, panels):
        dd = sub.dropna(subset=[outcome, "bsys"]).copy()
        f = f"Q('{outcome}') ~ new_channel + C(cell_id) + C(bsys)"
        obs = smf.ols(f, data=dd).fit().params["new_channel"]
        null = np.empty(n_perm)
        for i in range(n_perm):
            dd2 = dd.copy()
            dd2["new_channel"] = dd2.groupby("cell_id")["new_channel"].transform(
                lambda s: rng.permutation(s.values))
            null[i] = smf.ols(f, data=dd2).fit().params["new_channel"]
        ri_p = (np.sum(np.abs(null) >= abs(obs)) + 1) / (n_perm + 1)
        ax.hist(null, bins=40, color="#bdbdbd", edgecolor="white")
        ax.axvline(obs, color=COLOR_3RD if outcome != "yield_gain_pct" else COLOR_SELF,
                   lw=2, label=f"observed = {obs:+.3f}\nRI p = {ri_p:.3f}")
        ax.axvline(0, color="black", lw=0.6, ls=":")
        ax.set_title(label, fontsize=10)
        ax.legend(fontsize=8, loc="upper left" if obs < 0 else "upper right")
        ax.set_xlabel(r"permuted $\beta$ (within-cell reshuffle, x500)")
    fig.suptitle("Fig. 5. Randomization inference: null distribution vs observed coefficient\n"
                  "(Arm 1, Consortium vs Unified, channel label permuted within cell)", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(f"{FIG_DIR}/fig6_randomization.png", dpi=300, bbox_inches="tight")
    fig.savefig(f"{FIG_DIR}/fig6_randomization.pdf", bbox_inches="tight")
    plt.close(fig)
    print("wrote fig6_randomization.{png,pdf}")


# ---------------------------------------------------------------------------
# Fig. 7: missingness balance dumbbell plot
# ---------------------------------------------------------------------------
def fig7_missingness():
    df = pd.read_pickle(DATA_PATH)
    m = df[(df.level == "国审") & (df.trial_group.isin(TRIAL_GROUPS)) &
           (df.approval_year.isin([2017, 2019, 2020, 2021, 2022]))].copy()
    m["quality_stated"] = (m.quality_grade.notna() | m.quality_std.notna()).astype(int)
    m["approval_year"] = m.approval_year.astype(int)

    arm1 = m[(m.approval_year.isin([2019, 2020, 2021, 2022])) &
             (m.channel.isin(["Unified", "Consortium"]))]

    rows = []
    for outcome in OUTCOME_ORDER:
        cons = arm1.loc[arm1.channel == "Consortium", outcome].notna().mean() * 100
        unif = arm1.loc[arm1.channel == "Unified", outcome].notna().mean() * 100
        rows.append((outcome, unif, cons))
    dat = pd.DataFrame(rows, columns=["outcome", "unified_pct", "consortium_pct"])
    dat["gap"] = (dat.consortium_pct - dat.unified_pct).abs()
    dat = dat.sort_values("unified_pct").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(8, 7))
    y = np.arange(len(dat))
    for i, r in dat.iterrows():
        flagged = r.gap >= 8
        color = "#d95f02" if flagged else "#7570b3"
        ax.plot([r.unified_pct, r.consortium_pct], [i, i], color=color, lw=1.5, zorder=1)
    ax.scatter(dat.unified_pct, y, color="#1b9e77", label="Unified", zorder=2, s=45)
    ax.scatter(dat.consortium_pct, y, color="#d95f02", label="Consortium", zorder=2, s=45)
    ax.set_yticks(y)
    ax.set_yticklabels([OUTCOME_LABELS[o] for o in dat.outcome], fontsize=8)
    ax.set_xlabel("Non-missing rate (%), Arm 1 sample")
    ax.set_xlim(0, 105)
    ax.grid(axis="x", alpha=0.3)
    ax.legend(loc="lower right", fontsize=9)
    ax.set_title("Supplementary Fig. S1. Missingness balance across arms (Arm 1, 2019-2022)\n"
                 "orange line = imbalance >= 8pp (flagged in Robustness / Manski bounds)", fontsize=10)
    fig.tight_layout()
    fig.savefig(f"{FIG_DIR}/fig7_missingness_balance.png", dpi=300, bbox_inches="tight")
    fig.savefig(f"{FIG_DIR}/fig7_missingness_balance.pdf", bbox_inches="tight")
    plt.close(fig)
    print("wrote fig7_missingness_balance.{png,pdf}")
    print(dat.round(1).to_string(index=False))


if __name__ == "__main__":
    fig2_forest()
    fig6_randomization()
    fig7_missingness()
