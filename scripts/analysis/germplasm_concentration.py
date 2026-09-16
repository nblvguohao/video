"""
Parental-line entity resolution and germplasm concentration by trial channel.

Intelligence-method component: the approval announcement's 品种来源 (variety source) field
records the cross that produced the variety, almost always as
    <female/sterile line> × <male/restorer line>
This script resolves that free-text field into two parental-line entities per record and
uses them to build a germplasm-concentration indicator (Herfindahl-Hirschman index over
parental lines, plus distinct-line counts and top-line share).

Substantive question: do self-organised channels draw on a narrower germplasm base than the
unified state trial? The two self-organised channels have opposite institutional structure
— the green channel is run by a single certified enterprise, consortium trials pool five or
more breeders — so they provide a within-paper check that the indicator tracks institutional
structure rather than noise.

Inference: HHI is a non-linear function of the sample, so differences are assessed by a
stratified bootstrap (resampling records within channel) and by a label permutation test.
Because distinct-line counts rise mechanically with n, the distinct-count comparison is
additionally rarefied to the smaller group's n.

Writes manuscript/tables/table_germplasm_concentration.csv.
"""
import re
import numpy as np
import pandas as pd

PKL = 'evidence/data/analysis_rice_channel.pkl'
OUT = 'manuscript/tables/table_germplasm_concentration.csv'
RNG = np.random.default_rng(20260916)
B = 10000

# --- parental-line extraction -------------------------------------------------
# We take only the FIRST cross: later crosses describe the parents' own ancestry.
# Announcements use several typographic conventions for the cross symbol and for hyphens
# inside line names, and some records carry a parenthetical alias before the cross. An
# earlier version of this extractor handled only the common cases, and its failures were
# CHANNEL-CORRELATED (green-channel records failed at 8.0% against the unified channel's
# 2.3%), which would have biased the Arm-2 comparison. This normalisation removes that.
_CH = r'[A-Za-z0-9\u4e00-\u9fff\u2160-\u217f\-]'   # includes Roman numerals (Ⅱ-32A etc.)
_PAT = re.compile(r'^["“]?(' + _CH + r'{2,14})["”]?×["“]?(' + _CH + r'{2,16})')
_SUBS = [('＊', '×'), ('✕', '×'), ('╳', '×'), ('Ｘ', '×'),
         ('－', '-'), ('–', '-'), ('—', '-'), ('～', '-')]


def _norm(s):
    s = re.sub(r'[（(][^）)]{0,20}[）)]', '', s)   # drop a parenthetical alias
    for a, b in _SUBS:
        s = s.replace(a, b)
    if '×' not in s:
        # Only treat x/X or a slash as the cross when no true cross symbol is present, so a
        # Latin x inside a line name is not mistaken for a separator.
        s = re.sub(r'(?<=[0-9A-Za-z\u4e00-\u9fff])[xX](?=[0-9A-Za-z\u4e00-\u9fff])', '×', s, count=1)
        s = s.replace('//', '×', 1)
        if '×' not in s:
            s = s.replace('/', '×', 1)
    return s


def parents(s):
    m = _PAT.match(_norm(str(s)))
    return (m.group(1), m.group(2)) if m else (None, None)


def hhi(series):
    v = series.value_counts()
    s = v / v.sum()
    return float((s ** 2).sum())


def rarefied_distinct(series, m, reps=400):
    """Expected distinct lines in a random subsample of size m."""
    a = series.to_numpy()
    if m >= len(a):
        return float(pd.Series(a).nunique())
    return float(np.mean([pd.unique(RNG.choice(a, m, replace=False)).size for _ in range(reps)]))


d = pd.read_pickle(PKL)
n = d[d.level == '国审'].copy()
ped = n.pedigree.astype(str).str.replace(r'\s+', '', regex=True)
pp = ped.apply(parents)
n['mother'] = [a for a, _ in pp]
n['father'] = [b for _, b in pp]
parsed = n.mother.notna()
print(f'parental-line extraction: {parsed.sum()}/{len(n)} national records '
      f'({parsed.mean()*100:.1f}%) resolved into two parents')

# The concentration comparison must run on the SAME stratum as the main estimates: national
# approvals in the two dominant mid-season indica trial groups. Computing it over all 26
# national trial groups pools ecologically unrelated breeding pools and inflates the contrast.
INDICA = ['长江中下游中籼迟熟', '长江上游中籼迟熟']
n = n[n.trial_group.isin(INDICA)].copy()
print('restricted to the two dominant indica trial groups: n =', len(n))

# Per-channel extraction coverage. Reported because unbalanced extraction failure would
# confound the concentration contrast; this is the diagnostic that caught the earlier
# extractor's channel-correlated failures.
cov_rows = []
for _arm, (_ch, _yrs) in {'Arm1_Consortium_vs_Unified': ('Consortium', list(range(2019, 2023))),
                          'Arm2_Green_vs_Unified': ('Green', [2017])}.items():
    _s = n[n.approval_year.isin(_yrs) & n.channel.isin([_ch, 'Unified'])]
    for _c in ['Unified', _ch]:
        _g = _s[_s.channel == _c]
        if not len(_g):
            continue
        cov_rows.append(dict(arm=_arm, group=_c, n=len(_g),
                             resolved=int(_g.mother.notna().sum()),
                             coverage=round(_g.mother.notna().mean(), 4)))
cov = pd.DataFrame(cov_rows)
print('\nextraction coverage by channel (must be balanced):')
print(cov.to_string(index=False))

ARMS = {'Arm1_Consortium_vs_Unified': ('Consortium', list(range(2019, 2023))),
        'Arm2_Green_vs_Unified':      ('Green',      [2017])}

rows, tests = [], []
for arm, (chan, yrs) in ARMS.items():
    sub = n[parsed & n.approval_year.isin(yrs) & n.channel.isin([chan, 'Unified'])]
    a = sub[sub.channel == 'Unified']
    b = sub[sub.channel == chan]
    if len(a) < 10 or len(b) < 10:
        continue
    m = min(len(a), len(b))
    for label, g in [('Unified', a), ('new channel', b)]:
        mv = g.mother.value_counts()
        rows.append(dict(
            arm=arm, group=label, n=len(g),
            distinct_sterile_lines=int(g.mother.nunique()),
            distinct_sterile_rarefied=round(rarefied_distinct(g.mother, m), 1),
            hhi_sterile=round(hhi(g.mother), 5),
            top_sterile_share=round(mv.iloc[0] / len(g), 4),
            distinct_restorer_lines=int(g.father.nunique()),
            hhi_restorer=round(hhi(g.father), 5),
        ))

    # bootstrap CI for the HHI difference (new channel - unified)
    obs = hhi(b.mother) - hhi(a.mother)
    boot = np.array([hhi(pd.Series(RNG.choice(b.mother.to_numpy(), len(b)))) -
                     hhi(pd.Series(RNG.choice(a.mother.to_numpy(), len(a)))) for _ in range(B)])
    lo, hi = np.percentile(boot, [2.5, 97.5])
    # permutation test on the channel label
    pool = pd.concat([a.mother, b.mother]).to_numpy()
    perm = np.empty(B)
    for i in range(B):
        RNG.shuffle(pool)
        perm[i] = hhi(pd.Series(pool[:len(b)])) - hhi(pd.Series(pool[len(b):]))
    # (1 + count) / (1 + B): the uncorrected proportion can return exactly zero.
    p = float((1 + (np.abs(perm) >= abs(obs)).sum()) / (1 + B))
    tests.append(dict(arm=arm, statistic='hhi_sterile_diff_new_minus_unified',
                      observed=round(obs, 5), ci_low=round(lo, 5), ci_high=round(hi, 5),
                      perm_p=round(p, 4), n_unified=len(a), n_new=len(b)))

t = pd.DataFrame(rows)
tt = pd.DataFrame(tests)
print('\n', t.to_string(index=False), sep='')
print('\n', tt.to_string(index=False), sep='')
pd.concat([t.assign(block='descriptive'), tt.assign(block='inference'),
           cov.assign(block='coverage')], ignore_index=True).to_csv(OUT, index=False)
print('\nwrote', OUT)
