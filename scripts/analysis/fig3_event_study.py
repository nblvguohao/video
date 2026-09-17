"""
fig3_event_study.py

Generates Fig. 3: year-by-year channel gap (self-organised minus Unified) for
head-rice percentage, chalkiness degree, stated quality grade, and
regional-trial yield gain over check, 2017 and 2019-2022. Reproduces the
exact coefficients/SEs in manuscript/tables/table_event_study_by_year.csv;
only the visual treatment is new: shaded 95% CI bands instead of bare error
bars, panels coloured by measuring party (matching Fig. 2's legend: blue =
third-party assayed, red = applicant self-reported), and a shared reference
band marking the post-2022 rectification.

Run: python3 scripts/analysis/fig3_event_study.py
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plot_style import apply, COLOR_3RD, COLOR_SELF

apply()

FIG_DIR = "/home/user/video/manuscript/figures"
ev = pd.read_csv("/home/user/video/manuscript/tables/table_event_study_by_year.csv")

PANELS = [
    ("head_rice_pct", "Head-rice recovery rate (%)", COLOR_3RD),
    ("chalkiness_deg_pct", "Chalkiness degree (%)", COLOR_3RD),
    ("quality_stated", "Stated quality grade (0/1)", COLOR_3RD),
    ("yield_gain_pct", "Yield gain over check (%)", COLOR_SELF),
]

fig, axes = plt.subplots(2, 2, figsize=(11, 8.6))

for ax, (trait, title, color) in zip(axes.flat, PANELS):
    d = ev[ev.trait == trait].sort_values("year")
    x = d.year.values
    beta = d.beta.values
    ci_lo = beta - 1.96 * d.se.values
    ci_hi = beta + 1.96 * d.se.values

    ax.fill_between(x, ci_lo, ci_hi, color=color, alpha=0.15, zorder=1, lw=0)
    ax.plot(x, beta, color=color, lw=2.0, marker="o", markersize=6.5,
            markerfacecolor=color, markeredgecolor="white", markeredgewidth=1.0, zorder=3)
    ax.axhline(0, color="#6b6b76", lw=1.0, ls="-", alpha=0.8, zorder=2)
    ax.axvspan(2017.5, 2018.5, color="#9a9aa5", alpha=0.10, zorder=0, lw=0)  # 2018 gap, excluded

    for xi, yi, p in zip(x, beta, d.p.values):
        if p < 0.05:
            ax.annotate("*", (xi, yi), xytext=(0, 9 if yi >= 0 else -16),
                        textcoords="offset points", ha="center", fontsize=13,
                        color=color, fontweight="bold")

    ax.set_title(title, fontsize=11.5)
    ax.set_xlabel("Approval year")
    ax.set_ylabel("New-channel − Unified (β, 95% CI)")
    ax.set_xticks([2017, 2019, 2020, 2021, 2022])

fig.suptitle(
    "Fig. 3. Year-by-year channel gap, self-organised minus Unified\n"
    "(shaded band = 95% CI; grey band = 2018, excluded; * marks p < 0.05; colour = measuring party as in Fig. 2)",
    fontsize=11.5, y=1.01,
)
handles = [
    plt.Line2D([0], [0], color=COLOR_3RD, lw=2.5, label="Third-party assayed"),
    plt.Line2D([0], [0], color=COLOR_SELF, lw=2.5, label="Applicant self-reported"),
]
fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=[0, 0.02, 1, 0.97])
fig.savefig(f"{FIG_DIR}/fig3_event_study.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{FIG_DIR}/fig3_event_study.pdf", bbox_inches="tight")
plt.close(fig)
print("wrote fig3_event_study.{png,pdf}")
