#!/usr/bin/env python3
"""Parse regional-trial fields from Chinese rice variety approval announcement texts.

Input : evidence/data/national_rice_varieties_raw.csv  (reconstructed from he-zhui/Rice_QA, jw/qa_data.json)
Output: evidence/data/national_rice_parsed.csv  + evidence/data/national_rice_parsed.report.md

Every numeric field is extracted by regex from the announcement text; nothing is imputed.
"""
import re, pandas as pd, numpy as np

SRC = 'evidence/data/national_rice_varieties_raw.csv'
OUT = 'evidence/data/national_rice_parsed.csv'
REP = 'evidence/data/national_rice_parsed.report.md'

df = pd.read_csv(SRC, encoding='utf-8-sig', dtype=str).fillna('')
def num(s):
    try: return float(s)
    except: return np.nan

def first(pattern, text, flags=0, group=1, conv=num):
    m = re.search(pattern, text, flags)
    return conv(m.group(group)) if m else (np.nan if conv is num else '')

recs = []
for _, r in df.iterrows():
    name = r['variety_name'] or r['品种名称']
    src = r['品种来源']; feat = r['特征特性']; yld = r['产量表现']; no = r['审定编号']
    alltxt = ' '.join([src, feat, yld, no])
    # approval number: prefer explicit column, else search in texts
    m = re.search(r'([一-龥]{1,2}审稻(?:\s*)?\d{4,10}|皖稻\d{4,10}|[一-龥]{1,2}审稻\d{4}\.\d+)', no) or re.search(r'审定编号[为：:]*([一-龥]{1,2}审稻\s*\d{4,10}|皖稻\d{4,10})', alltxt)
    appr = m.group(1).replace(' ', '') if m else ''
    year = first(r'((?:19|20)\d{2})', appr, conv=lambda x: int(x)) if appr else np.nan
    level = '国审' if appr.startswith('国审') else ('省审' if appr else '')
    province = '' if not appr or level == '国审' else appr[:1]
    # type
    is_hybrid = bool(re.search(r'不育系|杂交|恢复系|配组', src + feat))
    sys3 = bool(re.search(r'三系', src + feat)) or bool(re.search(r'[A-Za-z0-9一-龥]+A[”"’\']?\s*[与和×]', src))
    sys2 = bool(re.search(r'两系|光温敏|温敏|S[”"’\']?\s*[与和×]', src + feat))
    subsp = '籼' if re.search(r'籼', src + feat) else ('粳' if re.search(r'粳', src + feat) else '')
    season = first(r'(早稻|早籼|中稻|中籼|晚稻|晚籼|一季稻|单季|双季|再生)', feat + yld, conv=lambda x: x)
    region_group = first(r'参加(.{2,25}?组)(?:品种)?(?:区域试验|区试)', yld, conv=lambda x: x) or first(r'((?:长江|华南|武陵|黄淮|东北|京津|西南|长江上游|长江中下游)[^，。；,]{0,20}?组)', yld, conv=lambda x: x)
    # yields
    y2 = first(r'两年区域试验平均亩产\s*([\d.]+)\s*(?:千克|公斤|kg)', yld)
    if np.isnan(y2):
        y2 = first(r'两年(?:区试)?平均亩产\s*([\d.]+)', yld)
    gain = first(r'两年区域试验平均亩产[^。；;]*?比对照[^，,。；;]*?(?:增产|减产)\s*([\-\d.]+)\s*%', yld)
    if np.isnan(gain):
        gain = first(r'两年(?:区试)?平均亩产[^。；;]*?(?:增产|减产)\s*([\-\d.]+)\s*%', yld)
    dec = bool(re.search(r'两年(?:区域试验)?平均亩产[^。；;]*?减产', yld))
    if dec and not np.isnan(gain): gain = -abs(gain)
    ck = first(r'比对照\s*([^\s，,。；;增减]{2,15}?)\s*(?:增产|减产)', yld, conv=lambda x: x)
    y_prod = first(r'生产试验[^。；;]*?平均亩产\s*([\d.]+)', yld)
    gain_prod = first(r'生产试验[^。；;]*?(?:增产|减产)\s*([\-\d.]+)\s*%', yld)
    # duration
    dur = first(r'全生育期(?:平均)?\s*([\d.]+)\s*天', feat)
    dur_diff = first(r'全生育期[^。；;]*?比(?:对照)?[^，,。；;]*?(长|短)\s*([\d.]+)\s*天', feat, group=2)
    sgn = first(r'全生育期[^。；;]*?比(?:对照)?[^，,。；;]*?(长|短)\s*[\d.]+\s*天', feat, conv=lambda x: x)
    if sgn == '短' and not np.isnan(dur_diff): dur_diff = -dur_diff
    # agronomic
    height = first(r'株高\s*([\d.]+)\s*厘米', feat)
    panicles = first(r'(?:亩|每亩)有效穗(?:数)?\s*([\d.]+)\s*万', feat)
    panicle_len = first(r'穗长\s*([\d.]+)\s*厘米', feat)
    grains = first(r'每穗总粒数\s*([\d.]+)\s*粒', feat)
    setting = first(r'结实率\s*([\d.]+)\s*%', feat)
    tgw = first(r'千粒重\s*([\d.]+)\s*克', feat)
    # resistance
    blast_idx_all = re.findall(r'稻瘟病综合(?:抗)?指数(?:年度分别为|分别为|为)?\s*[:：]?\s*([\d.]+(?:\s*[、,，和]\s*[\d.]+)*)', feat)
    blast_vals = []
    for b in blast_idx_all:
        blast_vals += [num(v) for v in re.split(r'[、,，和]\s*', b)]
    blast_idx = np.nanmean(blast_vals) if blast_vals else np.nan
    blast_max = np.nanmax(blast_vals) if blast_vals else np.nan
    neck = first(r'(?:穗颈瘟|稻瘟)损失率最高级\s*(\d)\s*级', feat)
    blast_text = first(r'((?:高抗|抗|中抗|中感|感|高感)稻瘟病)', feat, conv=lambda x: x)
    blb = first(r'白叶枯病?\s*(\d)\s*级', feat)
    blb_text = first(r'((?:高抗|抗|中抗|中感|感|高感)白叶枯病)', feat, conv=lambda x: x)
    bph = first(r'褐飞虱\s*(\d)\s*级', feat)
    heat = first(r'(抽穗期?耐热性[^，,。；;]{1,6}|耐热性[^，,。；;]{1,6})', feat, conv=lambda x: x)
    cold = first(r'(耐冷性[^，,。；;]{1,6}|苗期耐寒[^，,。；;]{1,6})', feat, conv=lambda x: x)
    # quality
    head_rice = first(r'整精米率\s*([\d.]+)\s*%', feat)
    chalk_deg = first(r'垩白度\s*([\d.]+)\s*%', feat)
    chalk_rate = first(r'垩白粒率\s*([\d.]+)\s*%', feat)
    amylose = first(r'直链淀粉(?:含量)?\s*([\d.]+)\s*%', feat)
    gel = first(r'胶稠度\s*([\d.]+)\s*(?:毫米|mm)', feat)
    lw = first(r'长宽比\s*([\d.]+)', feat)
    alkali = first(r'碱消值\s*([\d.]+)', feat)
    # Announcements state a grade only when the variety qualifies; there is no
    # "fails the standard" wording anywhere in the corpus, so a missing grade means
    # either "not qualifying" or "not stated". The widened pattern below tolerates the
    # standard number that often sits between the standard name and the grade, e.g.
    # "达到农业行业《食用稻品种品质》（NY/T 593-2013）标准二级".
    q = re.search(r'(?:达到|达|符合|评定为|为)\s*(?:农业行业|农业部|国家)?\s*(?:标准)?\s*《?(?:食用稻品种品质|优质稻谷)》?[^。；;]{0,40}?([一二三1-3])\s*级', feat)
    if not q:
        q = re.search(r'(?:达到|达|符合)?(?:农业(?:行业|部)?标准?|国家标准|部颁?标准?|国标|部标|《[^》]*》标准?)[^。；;]{0,20}?(?:优质)?\s*([一二三1-3])\s*级', feat)
    q2 = re.search(r'米质(?:达到|达|为)?[^。；;]{0,30}?(优质|国标|部标)?\s*([一二三1-3])\s*级', feat)
    qmap = {'一': 1, '1': 1, '二': 2, '2': 2, '三': 3, '3': 3}
    quality_grade = qmap.get(q.group(1), np.nan) if q else (qmap.get(q2.group(2), np.nan) if q2 else np.nan)
    quality_std = first(r'(《食用稻品种品质》|《优质稻谷》|部颁|国标|国家标准|农业行业标准|部标)', feat, conv=lambda x: x)
    is_winall = bool(re.search(r'荃银', src + r['选育单位'] + r['申请者'] + r['育种者']))
    applicant = r['申请者'] or r['选育单位'] or r['育种者']
    recs.append(dict(row_index=r['row_index'], variety=name, approval_no=appr, approval_year=year, level=level, province=province,
        is_hybrid=is_hybrid, three_line=sys3, two_line=sys2, subspecies=subsp, season_hint=season, region_group=region_group,
        yield_2yr_kg_mu=y2, yield_gain_pct=gain, ck=ck, yield_prod_kg_mu=y_prod, gain_prod_pct=gain_prod,
        duration_d=dur, duration_diff_d=dur_diff, plant_height_cm=height, panicles_10k_mu=panicles, panicle_len_cm=panicle_len,
        grains_per_panicle=grains, seed_setting_pct=setting, tgw_g=tgw,
        blast_index_mean=blast_idx, blast_index_max=blast_max, neck_blast_loss_max_grade=neck, blast_text=blast_text,
        blb_grade=blb, blb_text=blb_text, bph_grade=bph, heat_text=heat, cold_text=cold,
        head_rice_pct=head_rice, chalkiness_deg_pct=chalk_deg, chalky_grain_pct=chalk_rate, amylose_pct=amylose, gel_mm=gel, lw_ratio=lw, alkali=alkali,
        quality_grade=quality_grade, quality_std=quality_std, is_winall=is_winall, applicant=applicant, source_text_len=len(alltxt)))

out = pd.DataFrame(recs)
out.to_csv(OUT, index=False, encoding='utf-8-sig')
num_cols = [c for c in out.columns if out[c].dtype != object and c not in ('row_index',)]
cov = (out[num_cols].notna().mean() * 100).round(1)
lines = ['# national_rice_parsed.csv — parsing report', '', f'- rows: {len(out)}', f'- 国审 rows: {(out.level=="国审").sum()}, 省审 rows: {(out.level=="省审").sum()}, no approval no.: {(out.level=="").sum()}',
         f'- Winall-affiliated rows (荃银 in source/applicant): {int(out.is_winall.sum())} (国审 {int(((out.level=="国审")&out.is_winall).sum())})', '',
         '## Field coverage (% non-missing, all rows)', cov.to_string(), '',
         '## Field coverage (% non-missing, 国审 rows with approval year >= 2005)']
sub = out[(out.level == '国审') & (out.approval_year >= 2005)]
lines.append((sub[num_cols].notna().mean() * 100).round(1).to_string())
lines += ['', '## 国审 rows by year', out[out.level == '国审'].approval_year.value_counts().sort_index().to_string(),
          '', '## Winall rows by year (all levels)', out[out.is_winall].approval_year.value_counts().sort_index().to_string(),
          '', '## Notes', '- Parsed by regex from announcement text (品种来源/特征特性/产量表现); no imputation.',
          '- Source: he-zhui/Rice_QA (GitHub), jw/qa_data.json, derived from rice_extracted_fields.csv (approval announcements).',
          '- Coverage of 2023–2025 approvals is thin in the source; supplement Winall 2023–2025 varieties from MARA announcements via WebSearch.']
open(REP, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines[:12]))
print(out[out.is_winall & (out.level == '国审')][['variety', 'approval_no', 'yield_2yr_kg_mu', 'yield_gain_pct', 'duration_d', 'blast_index_mean', 'quality_grade']].head(12).to_string())
