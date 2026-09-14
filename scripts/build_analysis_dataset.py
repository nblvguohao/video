#!/usr/bin/env python3
"""Build the analysis-ready dataset of nationally approved rice varieties.

Input : evidence/data/national_rice_parsed.csv (regex-parsed announcement fields)
Output: evidence/data/analysis_national_rice.csv + .report.md

Steps: deduplicate by approval number, normalise ecological region / season /
breeding system, classify the applicant as enterprise / public / joint, flag
Winall-affiliated records, and derive a quality class. Nothing is imputed.
"""
import re, sys
import numpy as np
import pandas as pd

SRC = 'evidence/data/national_rice_parsed.csv'
OUT = 'evidence/data/analysis_national_rice.csv'
REP = 'evidence/data/analysis_national_rice.report.md'

d = pd.read_csv(SRC, encoding='utf-8-sig')
n0 = len(d)
d = d[d.level == '国审'].copy()
n1 = len(d)

# ---- 1. deduplicate by approval number: keep the most complete record -------
d['_completeness'] = d.notna().sum(axis=1)
d['_namelen'] = d.variety.astype(str).str.len()          # prefer the short canonical name
d = (d.sort_values(['_completeness', '_namelen'], ascending=[False, True])
       .drop_duplicates(subset='approval_no', keep='first'))
n2 = len(d)

# ---- 2. normalise ecological region ----------------------------------------
def macro_region(s):
    s = str(s)
    if re.search(r'长江上游', s): return 'Upper Yangtze'
    if re.search(r'长江中下游', s): return 'Middle-Lower Yangtze'
    if re.search(r'华南', s): return 'South China'
    if re.search(r'黄淮|北方|东北|京津|辽|吉|黑', s): return 'North/Huanghuai'
    if re.search(r'武陵', s): return 'Wuling Mountains'
    if re.search(r'西南|云贵', s): return 'Southwest'
    return 'Other/Unspecified'
d['region'] = d.region_group.map(macro_region)

# ---- 3. normalise season ----------------------------------------------------
def season(row):
    s = f"{row.region_group} {row.season_hint}"
    if re.search(r'晚籼|晚粳|感光晚|晚稻', s): return 'Late'
    if re.search(r'早籼|早粳|早稻', s): return 'Early'
    if re.search(r'中籼|中稻|单季|一季|麦茬|粳稻组|中晚熟', s): return 'Single/Mid'
    return 'Unspecified'
d['season'] = d.apply(season, axis=1)

# ---- 4. breeding system -----------------------------------------------------
def bsys(row):
    if row.two_line and not row.three_line: return 'Two-line hybrid'
    if row.three_line and not row.two_line: return 'Three-line hybrid'
    if row.two_line and row.three_line: return 'Hybrid (unclear)'
    if row.is_hybrid: return 'Hybrid (unclear)'
    return 'Inbred/Other'
d['breeding_system'] = d.apply(bsys, axis=1)

# ---- 5. applicant type ------------------------------------------------------
ENT = r'公司|种业|集团|有限|股份'
PUB = r'农业科学院|农科院|大学|学院|研究所|科学院|农业厅|技术推广|研究中心|农科所'
def org_type(s):
    s = str(s)
    if s.strip() in ('', 'nan'): return 'Unknown'
    ent, pub = bool(re.search(ENT, s)), bool(re.search(PUB, s))
    if ent and pub: return 'Joint'
    if ent: return 'Enterprise'
    if pub: return 'Public'
    return 'Unknown'
d['applicant'] = d.applicant.fillna('').astype(str)
d['applicant_type'] = d.applicant.map(org_type)
# number of co-applicants (separators used in announcements)
d['n_applicants'] = d.applicant.apply(lambda s: 0 if not s.strip() else len(re.split(r'[、,，;；/]', s)))

# ---- 6. quality class -------------------------------------------------------
# 1-3 = graded under the national/industry standard; NaN = not reported as a grade
d['quality_top2'] = np.where(d.quality_grade.notna(), (d.quality_grade <= 2).astype(float), np.nan)

# ---- 7. resistance flags ----------------------------------------------------
# neck-blast loss grade <= 5 is the usual "not highly susceptible" threshold
d['neck_blast_ok'] = np.where(d.neck_blast_loss_max_grade.notna(),
                              (d.neck_blast_loss_max_grade <= 5).astype(float), np.nan)
d['blast_susceptible_text'] = d.blast_text.astype(str).str.contains('高感|感稻瘟', na=False)

# ---- 8. sanity filters (flag, do not drop) ---------------------------------
d['flag_yield_outlier'] = (~d.yield_2yr_kg_mu.between(250, 1000)) & d.yield_2yr_kg_mu.notna()
d['flag_duration_outlier'] = (~d.duration_d.between(80, 200)) & d.duration_d.notna()

d = d.drop(columns=['_completeness', '_namelen'])
d = d.sort_values(['approval_year', 'approval_no'])
d.to_csv(OUT, index=False, encoding='utf-8-sig')

# ---- report -----------------------------------------------------------------
L = []
L.append('# analysis_national_rice.csv — build report\n')
L.append(f'- source rows: {n0} → 国审 rows: {n1} → after dedup by approval number: {n2}')
L.append(f'- approval years: {int(d.approval_year.min())}–{int(d.approval_year.max())} '
         f'({d.approval_year.isna().sum()} rows without a parsable year)')
L.append(f'- Winall-affiliated records: {int(d.is_winall.sum())}')
L.append(f'- flagged yield outliers: {int(d.flag_yield_outlier.sum())}; duration outliers: {int(d.flag_duration_outlier.sum())}\n')
L.append('## Records per year by applicant type')
L.append(pd.crosstab(d.approval_year.astype('Int64'), d.applicant_type).to_string())
L.append('\n## Records by region')
L.append(d.region.value_counts().to_string())
L.append('\n## Records by season')
L.append(d.season.value_counts().to_string())
L.append('\n## Records by breeding system')
L.append(d.breeding_system.value_counts().to_string())
L.append('\n## Key variable coverage (% non-missing)')
keys = ['yield_2yr_kg_mu', 'yield_gain_pct', 'duration_d', 'plant_height_cm', 'panicles_10k_mu',
        'grains_per_panicle', 'seed_setting_pct', 'tgw_g', 'head_rice_pct', 'chalkiness_deg_pct',
        'amylose_pct', 'gel_mm', 'lw_ratio', 'quality_grade', 'neck_blast_loss_max_grade',
        'blast_index_mean', 'blb_grade', 'bph_grade']
L.append((d[keys].notna().mean() * 100).round(1).to_string())
L.append('\n## Winall records per year')
L.append(d[d.is_winall].approval_year.astype('Int64').value_counts().sort_index().to_string())
L.append('\n## Caveats')
L.append('- Applicant fields are absent from the source compilation for 2016, 2017, 2018 and 2021; '
         'those years appear entirely as applicant_type = Unknown and Winall records there are not identifiable.')
L.append('- Each row is one approval (variety x ecological region), not one variety: a variety approved '
         'for several regions contributes several rows, each with its own regional-trial data.')
L.append('- All values are parsed verbatim from announcement text; missing values are left empty.')
open(REP, 'w', encoding='utf-8').write('\n'.join(L))
print('\n'.join(L[:40]))
print('\nwrote', OUT, d.shape)
