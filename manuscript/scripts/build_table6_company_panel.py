"""
Table 6: Winall (荃银高科) + comparator listed seed companies, 2015-2025.
Observed vs estimated (推算) values are flagged in a dedicated column.
Sources: evidence/company_panel.csv, evidence/04_order_grain_timeseries.csv,
         evidence/05_competitor_financials.csv, evidence/01_company_financials.md
"""
import pandas as pd
import numpy as np

cp = pd.read_csv("/home/user/video/evidence/company_panel.csv")
og = pd.read_csv("/home/user/video/evidence/04_order_grain_timeseries.csv")
comp = pd.read_csv("/home/user/video/evidence/05_competitor_financials.csv",
                    engine="python", on_bad_lines="warn")
# Row 2 (荃银(ST荃银) 2025) has a stray unquoted comma inside the rd_note field
# ("研发费用1.68亿(+23.42%,第三方笔记)") that breaks the column count; python engine
# with on_bad_lines='warn' drops it, so re-add it manually with the correct 11 fields.
manual_fixes = []
if not (comp["company"] == "荃银高科(ST荃银)").any():
    manual_fixes.append({
        "company": "荃银高科(ST荃银)", "ticker": 300087, "fiscal_year": 2025,
        "revenue_100m_CNY": 44.95, "revenue_yoy": "-4.55%",
        "net_profit_attrib_100m_CNY": -2.12, "net_profit_yoy": "-317.91%",
        "seed_segment_note": "水稻种子-12.93%；小麦种子-12.41%；玉米种子+10.69%；扣非-3.07亿",
        "rd_note": "研发资本化0.35亿(资本化率17.28%)；研发费用1.68亿(+23.42%，第三方笔记)",
        "source": "https://static.cninfo.com.cn/finalpage/2026-04-25/1225192807.PDF",
        "confidence": "高(主指标)/低(研发费用)",
    })
if not (comp["company"] == "隆平高科").any():
    manual_fixes.append({
        "company": "隆平高科", "ticker": "000998", "fiscal_year": 2025,
        "revenue_100m_CNY": 84.77, "revenue_yoy": "-1.0%",
        "net_profit_attrib_100m_CNY": 1.66, "net_profit_yoy": np.nan,
        "seed_segment_note": "玉米种子收入约50.40亿；2025年完成12亿元定增(中信农业)",
        "rd_note": "2019年研发投入4.2亿(13.15%，旧数据)",
        "source": ("GitHub chess99/trading-os 000998/2026-07-11.md 转引 "
                   "https://pdf.dfcfw.com/pdf/H3_AP202604211821362286_1.pdf"),
        "confidence": "低-中",
    })
if manual_fixes:
    comp = pd.concat([comp, pd.DataFrame(manual_fixes)], ignore_index=True)

rows = []

# ---------- Winall (荃银高科), 2015-2025 (FY), plus 2026 Q1 as a memo row ----------
og = og.set_index("period")

for _, r in cp.iterrows():
    year = r["year"]
    period = r["period"]
    if period != "FY":
        continue  # keep annual rows only for the main panel; 2026 Q1 reported separately below
    key = str(int(year))
    og_row = og.loc[key] if key in og.index else None

    revenue_100m = r["revenue_yuan"] / 1e8 if pd.notna(r["revenue_yuan"]) else np.nan
    rd_100m = r["rd_investment_yuan"] / 1e8 if pd.notna(r["rd_investment_yuan"]) else np.nan
    rd_intensity = r["rd_share_of_revenue_pct"] if pd.notna(r.get("rd_share_of_revenue_pct")) else (
        rd_100m / revenue_100m * 100 if pd.notna(rd_100m) and pd.notna(revenue_100m) and revenue_100m != 0 else np.nan
    )
    approved_total = r["national_approved_total"]
    net_profit_100m = r["parent_net_profit_yuan"] / 1e8 if pd.notna(r["parent_net_profit_yuan"]) else np.nan
    gm = r["gross_margin_pct"]

    order_grain_rev_100m = np.nan
    order_grain_share = np.nan
    order_grain_gm = np.nan
    og_value_type = "not available"
    og_note = ""
    if og_row is not None:
        raw_rev = og_row["order_grain_revenue_100m_yuan"]
        raw_share = og_row["order_grain_share_pct"]
        raw_gm = og_row["order_grain_gross_margin_pct"]
        any_flagged = any("推算" in str(v) for v in (raw_rev, raw_share, raw_gm))
        try:
            order_grain_rev_100m = float(str(raw_rev).replace("(推算)", "").strip())
        except (ValueError, TypeError):
            order_grain_rev_100m = np.nan
        order_grain_share = raw_share
        order_grain_gm = raw_gm
        og_value_type = "estimated (推算) — see note" if any_flagged else "observed"
        og_note = og_row.get("note", "")

    rows.append(dict(
        company="荃银高科 (Winall Hi-tech Seed, 300087)",
        year=int(year),
        revenue_100m_CNY=round(revenue_100m, 2) if pd.notna(revenue_100m) else np.nan,
        gross_margin_pct=gm,
        net_profit_attrib_100m_CNY=round(net_profit_100m, 2) if pd.notna(net_profit_100m) else np.nan,
        rd_investment_100m_CNY=round(rd_100m, 3) if pd.notna(rd_100m) else np.nan,
        rd_intensity_pct_of_revenue=round(rd_intensity, 2) if pd.notna(rd_intensity) else np.nan,
        national_approved_varieties=approved_total,
        order_grain_revenue_100m_CNY=order_grain_rev_100m,
        order_grain_share_of_revenue_pct=order_grain_share,
        order_grain_gross_margin_pct=order_grain_gm,
        value_type_order_grain=og_value_type,
        note=og_note if isinstance(og_note, str) else "",
        source="evidence/company_panel.csv; evidence/04_order_grain_timeseries.csv; evidence/01_company_financials.md",
    ))

# ---------- 2026 Q1 memo row (not annual, kept for context on the ST/ tender-offer timing) ----------
q1 = cp[cp.period == "Q1"].iloc[0]
rows.append(dict(
    company="荃银高科 (Winall Hi-tech Seed, 300087) [2026Q1, memo row - not FY]",
    year=2026,
    revenue_100m_CNY=round(q1["revenue_yuan"] / 1e8, 2),
    gross_margin_pct=q1["gross_margin_pct"],
    net_profit_attrib_100m_CNY=round(q1["parent_net_profit_yuan"] / 1e8, 4),
    rd_investment_100m_CNY=np.nan,
    rd_intensity_pct_of_revenue=np.nan,
    national_approved_varieties=np.nan,
    order_grain_revenue_100m_CNY=np.nan,
    order_grain_share_of_revenue_pct=np.nan,
    order_grain_gross_margin_pct=np.nan,
    value_type_order_grain="not available",
    note="2026Q1 only, not a fiscal year; order-grain business revenue -37.28% YoY per notes",
    source="evidence/company_panel.csv",
))

# ---------- Comparator companies, single most-recent observed year (2024/2025, as reported) ----------
for _, r in comp.iterrows():
    if r["company"].startswith("荃银"):
        continue  # already covered above with the full multi-year panel
    fy = r["fiscal_year"]
    try:
        fy_val = int(fy)
    except (ValueError, TypeError):
        fy_val = str(fy) if pd.notna(fy) else np.nan  # e.g. "2024/2025" or missing
    rows.append(dict(
        company=f"{r['company']} ({r['ticker']})",
        year=fy_val,
        revenue_100m_CNY=r["revenue_100m_CNY"],
        gross_margin_pct=np.nan,
        net_profit_attrib_100m_CNY=r["net_profit_attrib_100m_CNY"],
        rd_investment_100m_CNY=np.nan,
        rd_intensity_pct_of_revenue=np.nan,
        national_approved_varieties=np.nan,
        order_grain_revenue_100m_CNY=np.nan,
        order_grain_share_of_revenue_pct=np.nan,
        order_grain_gross_margin_pct=np.nan,
        value_type_order_grain="not applicable (no order-grain segment reported)",
        note=str(r["seed_segment_note"]) + " | R&D: " + str(r["rd_note"]),
        source=f"{r['source']} (confidence: {r['confidence']})",
    ))

tab6 = pd.DataFrame(rows)
tab6.to_csv("/home/user/video/manuscript/tables/table6_company_panel.csv", index=False)
print(tab6.to_string(index=False))
print("\nSaved: manuscript/tables/table6_company_panel.csv, n rows =", len(tab6))
print("\nEstimated (推算) order-grain rows:",
      tab6[tab6.value_type_order_grain.str.startswith("estimated", na=False)][["company", "year"]].to_string(index=False))
