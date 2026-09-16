"""
R17: does the quality-grading standard in force differ by trial channel?

Records state their grain-quality grade under one of two standards — GB/T 《优质稻谷》
and NY/T 593 《食用稻品种品质》 — and the mix shifts sharply across the study window
(GB/T dominates 2017, NY/T dominates 2019-2022). Arm 2 sits in 2017 and Arm 1 in
2019-2022, so if channel correlated with standard, the quality outcomes would not be
comparable across the contrast.

This check asks whether, *within each arm's own window*, the standard used differs by
channel. If it does not, the year x trial-group x check fixed effects absorb the switch.

Writes manuscript/tables/table_r17_standard_composition.csv.
"""
import pandas as pd

PKL = 'evidence/data/analysis_rice_channel.pkl'
OUT = 'manuscript/tables/table_r17_standard_composition.csv'

d = pd.read_pickle(PKL)
nat = d[d.level == '国审'].copy()

ARMS = {
    'Arm1_Consortium_vs_Unified': ('Consortium', list(range(2019, 2023))),
    'Arm2_Green_vs_Unified':      ('Green',      [2017]),
}

rows = []
for arm, (chan, yrs) in ARMS.items():
    sub = nat[nat.approval_year.isin(yrs) & nat.channel.isin([chan, 'Unified'])].copy()
    sub['std'] = sub.quality_std.fillna('none')
    # collapse the handful of legacy labels into the two standards of interest
    sub['std'] = sub['std'].replace({'国标': '《优质稻谷》', '部颁': '《食用稻品种品质》',
                                     '部标': '《食用稻品种品质》'})
    for grp, label in [('Unified', 'Unified'), (chan, 'new channel')]:
        g = sub[sub.channel == grp]
        n = len(g)
        if not n:
            continue
        vc = g['std'].value_counts()
        graded = n - int(vc.get('none', 0))
        rows.append(dict(
            arm=arm, group=label, n=n,
            n_no_stated_standard=int(vc.get('none', 0)),
            share_no_stated_standard=round(int(vc.get('none', 0)) / n, 4),
            n_GBT_youzhi_daogu=int(vc.get('《优质稻谷》', 0)),
            n_NYT593_shiyong_dao=int(vc.get('《食用稻品种品质》', 0)),
            # among graded records only: which standard was applied
            share_NYT593_among_graded=round(int(vc.get('《食用稻品种品质》', 0)) / graded, 4) if graded else None,
        ))

t = pd.DataFrame(rows)
t.to_csv(OUT, index=False)
print(t.to_string(index=False))
print('\nwrote', OUT)

# headline contrast the check reproduces: the channel gap in whether ANY grade is stated
print('\nRaw gap in share with no stated standard (new channel - Unified):')
for arm in ARMS:
    a = t[t.arm == arm].set_index('group')['share_no_stated_standard']
    print(f'  {arm}: {a["new channel"] - a["Unified"]:+.4f}')
