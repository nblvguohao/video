"""
fig4_breakpoint_scan.py

Generates Fig. 4: unknown-breakpoint (sup-Wald) scan, Wald statistic by
candidate break year (2009-2019), one line per trait, peak years annotated.
Reproduces the exact statistics in
manuscript/tables/table_breakpoint_scan_full.csv; only the visual treatment
is new: a fixed, distinguishable categorical palette (in place of the
previous ad hoc qualitative cycle), a shaded pre-/post-2016-reform split, and
consistent peak-year markers for every trait.

Run: python3 scripts/analysis/fig4_breakpoint_scan.py
"""
import pandas as pd
import matplotlib.pyplot as plt
from plot_style import apply, TRAIT_PALETTE

apply()

FIG_DIR = "/home/user/video/manuscript/figures"
scan = pd.read_csv("/home/user/video/manuscript/tables/table_breakpoint_scan_full.csv")

TRAITS = [
    ("yield_2yr_kg_mu", "Trial yield (kg/mu)"),
    ("head_rice_pct", "Head-rice recovery rate (%)"),
    ("chalkiness_deg_pct", "Chalkiness degree (%)"),
    ("quality_top2_var", "Stated top-2 quality grade (0/1)"),
    ("yield_gain_pct", "Yield gain over check (%)"),
    ("duration_d", "Growth duration (days)"),
]

fig, ax = plt.subplots(figsize=(11, 7.2))
ax.axvspan(2008.6, 2016, color="#9a9aa5", alpha=0.07, zorder=0, lw=0)
ax.axvspan(2016, 2019.4, color="#d9720a", alpha=0.05, zorder=0, lw=0)
ax.axvline(2016, color="#6b6b76", lw=1.3, ls=(0, (5, 3)), alpha=0.7, zorder=1)

for key, label in TRAITS:
    d = scan[scan.trait == key].sort_values("tau")
    color = TRAIT_PALETTE[key]
    ax.plot(d.tau, d.wald, color=color, lw=2.2, marker="o", markersize=6,
            markerfacecolor=color, markeredgecolor="white", markeredgewidth=0.9,
            label=label, zorder=3)
    peak_row = d.loc[d.wald.idxmax()]
    ax.scatter([peak_row.tau], [peak_row.wald], s=140, facecolor=color,
               edgecolor="#1a1a22", linewidth=1.3, zorder=5)
    ax.annotate(
        f"{int(peak_row.tau)}", (peak_row.tau, peak_row.wald),
        xytext=(6, 8), textcoords="offset points", fontsize=9, color=color, fontweight="bold",
    )

ax.set_ylim(bottom=-8)
ax.text(2016.07, ax.get_ylim()[1] * 0.97, "2016 reform", fontsize=8.5, color="#6b6b76",
        va="top", ha="left")
ax.set_xlabel("Candidate breakpoint year")
ax.set_ylabel("sup-Wald statistic (level + trend shift, HC1)")
ax.set_title("Fig. 4. Unknown-breakpoint (sup-Wald) scan by trait, national arm-1/arm-2 layer 2005–2022",
             fontsize=12.5, pad=14)
ax.legend(loc="upper left", frameon=False, fontsize=9.3, ncol=1)
fig.tight_layout()
fig.savefig(f"{FIG_DIR}/fig4_breakpoint_scan.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{FIG_DIR}/fig4_breakpoint_scan.pdf", bbox_inches="tight")
plt.close(fig)
print("wrote fig4_breakpoint_scan.{png,pdf}")
