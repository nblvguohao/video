import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

df = pd.read_pickle("/home/user/video/evidence/data/analysis_rice_channel.pkl")
national = df[df.level == "国审"].copy()

fig = plt.figure(figsize=(11, 11))
gs = fig.add_gridspec(3, 1, height_ratios=[1, 1.1, 1], hspace=0.55)

# =====================================================================
# Panel (a): Winall's national approval share and channel composition, by year
# =====================================================================
ax_a = fig.add_subplot(gs[0])

years = list(range(2015, 2025))
w = national[national.winall]
tot_by_year = national.groupby("approval_year").size()
w_by_year = w.groupby("approval_year").size()
share = (w_by_year / tot_by_year * 100).reindex(years).fillna(0)

ch_counts = w.groupby(["approval_year", "channel"]).size().unstack(fill_value=0).reindex(years, fill_value=0)
for c in ["Unified", "Consortium", "Green"]:
    if c not in ch_counts.columns:
        ch_counts[c] = 0
ch_counts = ch_counts[["Unified", "Consortium", "Green"]]

ax_a2 = ax_a.twinx()
colors = {"Unified": "#4C72B0", "Consortium": "#DD8452", "Green": "#55A868"}
bottom = np.zeros(len(years))
for c in ["Unified", "Consortium", "Green"]:
    ax_a.bar(years, ch_counts[c].values, bottom=bottom, color=colors[c], label=f"{c} channel (count)", width=0.6)
    bottom += ch_counts[c].values

ax_a2.plot(years, share.values, color="black", marker="o", markersize=4, linewidth=1.5,
           label="Winall share of national approvals (%)")
ax_a2.set_ylabel("Winall share of national\napprovals in that year (%)")
ax_a.set_ylabel("Winall national-approval\nrecords by channel (count)")
ax_a.set_xlabel("Approval year")
ax_a.set_title("(a) Winall national-approval share and channel composition, 2015–2024\n"
                "(Green channel: 2017 only; Consortium: 2019–2022 — the two arms do not overlap in time)",
                fontsize=9, loc="left")
ax_a.set_xticks(years)
h1, l1 = ax_a.get_legend_handles_labels()
h2, l2 = ax_a2.get_legend_handles_labels()
ax_a.legend(h1 + h2, l1 + l2, fontsize=7, loc="upper left", frameon=False, ncol=2)

# =====================================================================
# Panel (b): forest plot of within-channel trait gaps (Winall vs others),
#            Unified subsample vs New(Consortium+Green) subsample
# =====================================================================
ax_b = fig.add_subplot(gs[1])

tab5 = pd.read_csv("/home/user/video/manuscript/tables/table5_winall_positioning.csv")
label_map = {
    "head_rice_pct": "Head-rice % (third-party)",
    "quality_stated": "Quality grade stated (0/1, third-party)",
    "chalkiness_deg_pct": "Chalkiness % (third-party)",
}
tab5["outcome_label_short"] = tab5["outcome"].map(label_map)

order = ["Head-rice % (third-party)", "Quality grade stated (0/1, third-party)",
         "Chalkiness % (third-party)"]
y_positions = {lab: i for i, lab in enumerate(order)}

offset = {"Unified": 0.15, "New(Consortium+Green)": -0.15}
marker = {"Unified": "o", "New(Consortium+Green)": "s"}
color_sub = {"Unified": "#4C72B0", "New(Consortium+Green)": "#DD8452"}

for _, row in tab5.iterrows():
    lab = row["outcome_label_short"]
    if lab not in y_positions:
        continue
    y = y_positions[lab] + offset[row["channel_subsample"]]
    ci = 1.96 * row["se"]
    ax_b.errorbar(row["rho"], y, xerr=ci, fmt=marker[row["channel_subsample"]],
                  color=color_sub[row["channel_subsample"]], capsize=3, markersize=6,
                  label=row["channel_subsample"])

ax_b.axvline(0, color="grey", linewidth=0.8, linestyle="--")
ax_b.set_yticks(list(y_positions.values()))
ax_b.set_yticklabels(list(y_positions.keys()))
ax_b.set_xlabel("Winall − others gap (ρ), 95% CI, within-channel comparison")
ax_b.set_title("(b) Winall's within-channel trait gap: Unified subsample vs New-channel subsample\n"
                "(positive quality-grade coefficient = more likely to state a grade; "
                "positive chalkiness = worse appearance)",
                fontsize=9, loc="left")
handles, labels = ax_b.get_legend_handles_labels()
uniq = dict(zip(labels, handles))
ax_b.legend(uniq.values(), uniq.keys(), fontsize=7, loc="best", frameon=False)

# =====================================================================
# Panel (c): order-grain revenue share and R&D intensity over time,
#            hollow markers = estimated (推算) values; vertical lines = 2025 loss / ST event
# =====================================================================
ax_c = fig.add_subplot(gs[2])

og = pd.read_csv("/home/user/video/evidence/04_order_grain_timeseries.csv")
cp = pd.read_csv("/home/user/video/evidence/company_panel.csv")
cp_fy = cp[cp.period == "FY"].copy()
cp_fy["rd_intensity_pct"] = cp_fy["rd_share_of_revenue_pct"]
# fill R&D intensity from investment/revenue where the direct % field is missing
mask = cp_fy["rd_intensity_pct"].isna() & cp_fy["rd_investment_yuan"].notna()
cp_fy.loc[mask, "rd_intensity_pct"] = (cp_fy.loc[mask, "rd_investment_yuan"] /
                                        cp_fy.loc[mask, "revenue_yuan"] * 100)

def parse_period_to_year(p):
    # "2015".."2025" -> that year; "2025H1" -> 2025.5 (mid-year); "2025Q1-Q3" -> 2025.75
    if p.endswith("H1"):
        return float(p[:-2]) + 0.5
    if "Q1-Q3" in p:
        return float(p.split("Q1-Q3")[0]) + 0.75
    if p.endswith("Q1"):
        return float(p[:-2]) + 0.15
    try:
        return float(p)
    except ValueError:
        return np.nan

og["x"] = og["period"].apply(parse_period_to_year)
og["is_estimated"] = og.apply(
    lambda r: any("推算" in str(r[c]) for c in
                  ["order_grain_revenue_100m_yuan", "order_grain_share_pct", "order_grain_gross_margin_pct"]),
    axis=1)
og["share_clean"] = og["order_grain_share_pct"].astype(str).str.replace(r"\(推算\)", "", regex=True)
og["share_clean"] = pd.to_numeric(og["share_clean"], errors="coerce")

obs = og[~og.is_estimated]
est = og[og.is_estimated]
ax_c.plot(og.sort_values("x")["x"], og.sort_values("x")["share_clean"], color="#DD8452", linewidth=1, alpha=0.6, zorder=1)
ax_c.scatter(obs["x"], obs["share_clean"], marker="o", color="#DD8452", s=40,
             label="Order-grain revenue share (%) — observed", zorder=3)
ax_c.scatter(est["x"], est["share_clean"], marker="o", facecolors="none", edgecolors="#DD8452",
             s=60, linewidths=1.5, label="Order-grain revenue share (%) — estimated (imputed)", zorder=3)
ax_c.set_ylabel("Order-grain revenue\nshare of total revenue (%)", color="#DD8452")
ax_c.tick_params(axis="y", labelcolor="#DD8452")
ax_c.set_xlabel("Year")

ax_c2 = ax_c.twinx()
ax_c2.plot(cp_fy["year"], cp_fy["rd_intensity_pct"], color="#4C72B0", marker="^", markersize=5,
           linewidth=1.2, label="R&D intensity (% of revenue) — observed")
ax_c2.set_ylabel("R&D investment\n(% of revenue)", color="#4C72B0")
ax_c2.tick_params(axis="y", labelcolor="#4C72B0")

ax_c.set_xlim(2014.3, 2027.3)

# annotate 2025 loss and 2026 ST event
ax_c.axvline(2025, color="red", linestyle=":", linewidth=1.2)
ax_c.text(2025.15, 8, "2025: net loss\n(-212M CNY,\nturned from profit)",
          color="red", fontsize=7, va="bottom", ha="left")
ax_c.axvline(2026.0, color="darkred", linestyle="-.", linewidth=1.2)
ax_c.text(2026.15, 20, "2026-06: fined &\nrenamed ST Winall",
          color="darkred", fontsize=7, va="bottom", ha="left")

ax_c.set_title("(c) Order-grain revenue share and R&D intensity, 2015–2025\n"
                "(hollow markers = estimated/imputed values; vertical lines = 2025 loss and 2026 ST/penalty event)",
                fontsize=9, loc="left")

h1, l1 = ax_c.get_legend_handles_labels()
h2, l2 = ax_c2.get_legend_handles_labels()
ax_c.legend(h1 + h2, l1 + l2, fontsize=7, loc="upper center", frameon=False, ncol=1,
            bbox_to_anchor=(0.27, 1.02))

fig.suptitle("Figure 5. Winall Hi-tech Seed as a counter-case: channel choice, within-channel trait gap, and financial context\n"
             "Winall enters this paper as a counter-case that rules out an alternative explanation, not as a source of the main result.",
             fontsize=10, y=0.995)

fig.savefig("/home/user/video/manuscript/figures/fig5_winall_mechanism.png", dpi=200, bbox_inches="tight")
print("Saved figure to manuscript/figures/fig5_winall_mechanism.png")
