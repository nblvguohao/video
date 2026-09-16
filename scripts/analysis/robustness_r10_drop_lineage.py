"""
R10: drop the dominant germplasm lineage.

Re-runs the Arm-1 headline specification after removing every record whose resolved sterile
(female) line is the most prevalent sterile line in the estimation stratum. This replaces an
earlier version of R10 that dropped records linked to one named company; the paper no longer
conducts any analysis at the level of a named organisation, and the check is now defined on
germplasm rather than on corporate identity.

Uses the same specification, cell construction and covariance choice as the main estimates
(scripts/analysis/estimate_channel_gap.py): Y ~ new_channel + C(cell_id) + C(bsys), cells
defined as year x trial_group x check, clustered on cell when at least 5 cells identify.

Writes manuscript/tables/table_r10_drop_lineage.csv.
"""
import re
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

sys.path.insert(0, 'scripts/analysis')
from estimate_channel_gap import load_main_stratum, build_arm, fit_one  # noqa: E402

PKL = 'evidence/data/analysis_rice_channel.pkl'
OUT = 'manuscript/tables/table_r10_drop_lineage.csv'

_CH = r'[A-Za-z0-9一-鿿Ⅰ-ⅿ\-]'
_PAT = re.compile(r'^["“]?(' + _CH + r'{2,14})["”]?×["“]?(' + _CH + r'{2,16})')
_SUBS = [('＊', '×'), ('✕', '×'), ('╳', '×'), ('Ｘ', '×'),
         ('－', '-'), ('–', '-'), ('—', '-'), ('～', '-')]


def _norm(s):
    s = re.sub(r'[（(][^）)]{0,20}[）)]', '', s)
    for a, b in _SUBS:
        s = s.replace(a, b)
    if '×' not in s:
        s = re.sub(r'(?<=[0-9A-Za-z一-鿿])[xX](?=[0-9A-Za-z一-鿿])', '×', s, count=1)
        s = s.replace('//', '×', 1)
        if '×' not in s:
            s = s.replace('/', '×', 1)
    return s


def mother(s):
    m = _PAT.match(_norm(str(s)))
    return m.group(1) if m else None


OUTCOMES = ['head_rice_pct', 'chalkiness_deg_pct', 'quality_stated']

d = pd.read_pickle(PKL)
d['mother'] = d.pedigree.astype(str).str.replace(r'\s+', '', regex=True).apply(mother)
main = load_main_stratum(d)

top = main.mother.value_counts().idxmax()
n_top = int((main.mother == top).sum())
print(f'most prevalent sterile line in the estimation stratum: {top} '
      f'({n_top} of {len(main)} records, {n_top/len(main)*100:.1f}%)')

rows = []
for label, frame in [('full', main), ('drop_top_lineage', main[main.mother != top])]:
    arm1 = build_arm(frame, 1)
    for o in OUTCOMES:
        r = fit_one(arm1, o)
        if r is None:
            continue
        rows.append(dict(sample=label, outcome=o, beta=r['beta'], se=r['se'],
                         p=r['p'], n=r['n'], se_type=r['se_type']))

t = pd.DataFrame(rows)
print()
print(t.to_string(index=False))
t.to_csv(OUT, index=False)
print('\nwrote', OUT)
print('\ndropped line:', top, '| records removed from the stratum:', n_top)
