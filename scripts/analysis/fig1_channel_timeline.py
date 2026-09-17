"""
fig1_channel_timeline.py

Generates Fig. 1: 2005-2022 national rice approvals by trial channel, stacked
area chart with institutional-timeline markers. Reproduces the exact counts
in manuscript/tables/table1_channel_by_year.csv; only the visual treatment is
new (shaded institutional eras, softened area fills, a cleaner annotation
band instead of overlapping rotated text).

Run: python3 scripts/analysis/fig1_channel_timeline.py
"""
import pandas as pd
import matplotlib.pyplot as plt
from plot_style import apply, COLOR_UNIFIED, COLOR_GREEN, COLOR_CONSORTIUM, COLOR_SELF

apply()

FIG_DIR = "/home/user/video/manuscript/figures"
t1 = pd.read_csv("/home/user/video/manuscript/tables/table1_channel_by_year.csv")
t1.columns = [c.strip().lstrip("﻿") for c in t1.columns]

years = t1["approval_year"].values
unified = t1["Unified"].values
green = t1["Green"].values
consortium = t1["Consortium"].values

fig, ax = plt.subplots(figsize=(10, 6.2))

# institutional eras, shaded behind the data (pre-reform / green-channel-only / consortium era)
ax.axvspan(2004.4, 2014, color="#9a9aa5", alpha=0.05, zorder=0, lw=0)
ax.axvspan(2014, 2019, color=COLOR_GREEN, alpha=0.05, zorder=0, lw=0)
ax.axvspan(2019, 2023.0, color=COLOR_CONSORTIUM, alpha=0.05, zorder=0, lw=0)

ax.stackplot(
    years, unified, green, consortium,
    colors=[COLOR_UNIFIED, COLOR_GREEN, COLOR_CONSORTIUM],
    alpha=0.88, edgecolor="white", linewidth=0.6,
    labels=["Unified (national uniform trial)", "Green channel (self-organised)", "Consortium (joint trial)"],
)
# a crisp top line on the stack total for definition
total = unified + green + consortium
ax.plot(years, total, color="#2a2a33", lw=1.1, alpha=0.6, zorder=3)

events = [
    (2014, "2014: green channel opens", COLOR_GREEN),
    (2016.62, "2016-08-15: revised Approval Measures (consortium trials)", COLOR_CONSORTIUM),
    (2021, "2021: approval standards raised", "#6b6b76"),
    (2022.16, "2022-03-01: EDV regime (new Seed Law)", "#6b6b76"),
    (2022.75, "2022-08-31: MOA rectification notice", COLOR_SELF),
]
peak = max(total)
badge_y = peak * 1.14
for i, (x, label, color) in enumerate(events, start=1):
    ax.axvline(x, color=color, lw=1.1, ls=(0, (4, 2)), alpha=0.75, zorder=2, ymax=0.86)
    ax.scatter([x], [badge_y], s=230, color=color, zorder=5, edgecolor="white", linewidth=1.2)
    ax.text(x, badge_y, str(i), ha="center", va="center", fontsize=9.5, color="white",
            fontweight="bold", zorder=6)

ax.set_xlim(2004.4, 2023.0)
ax.set_ylim(0, peak * 1.28)

legend_lines = "\n".join(f"{i}  {label}" for i, (_, label, _) in enumerate(events, start=1))
ax.text(
    0.015, 0.60, legend_lines, transform=ax.transAxes, ha="left", va="top",
    fontsize=8.3, linespacing=1.9, color="#2a2a33",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="#d8d8e0", linewidth=0.8, alpha=0.92),
)
ax.set_xlabel("Approval year")
ax.set_ylabel("Number of nationally approved rice varieties")
ax.set_title("National rice variety approvals by trial channel, 2005–2022", pad=14)
leg = ax.legend(loc="upper left", frameon=False, fontsize=9.5)
ax.grid(axis="y", alpha=0.6)
ax.grid(axis="x", alpha=0)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

fig.savefig(f"{FIG_DIR}/fig1_channel_stacked.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{FIG_DIR}/fig1_channel_stacked.pdf", bbox_inches="tight")
plt.close(fig)
print("wrote fig1_channel_stacked.{png,pdf}")
