"""
Fig. 6 — germplasm concentration by trial channel, two panels.

(a) Lorenz-style concentration curves over sterile lines, one per channel and arm.
(b) Sterile-line HHI with bootstrap intervals, unified vs new channel, both arms.

Replaces the former firm-level mechanism figure.
"""
import re
import sys
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'scripts', 'analysis'))
from plot_style import apply as apply_style, COLOR_UNIFIED, COLOR_CONSORTIUM, COLOR_GREEN

apply_style()

RNG = np.random.default_rng(20260916)
B = 10000
OUT = 'manuscript/figures/fig6_germplasm_concentration'

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

def mother(s):
    return parents(s)[0]


def hhi(sr):
    v = sr.value_counts(); s = v / v.sum(); return float((s ** 2).sum())


d = pd.read_pickle('evidence/data/analysis_rice_channel.pkl')
n = d[d.level == '国审'].copy()
n['mother'] = n.pedigree.astype(str).str.replace(r'\s+', '', regex=True).apply(mother)
INDICA = ['长江中下游中籼迟熟', '长江上游中籼迟熟']
n = n[n.trial_group.isin(INDICA) & n.mother.notna()]

ARMS = [('Arm 1 (2019–2022)', 'Consortium', list(range(2019, 2023))),
        ('Arm 2 (2017)', 'Green', [2017])]
COL = {'Unified': COLOR_UNIFIED, 'Consortium': COLOR_CONSORTIUM, 'Green': COLOR_GREEN}

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

# --- panel (a): concentration curves ---
ax = axes[0]
for arm_lab, chan, yrs in ARMS:
    sub = n[n.approval_year.isin(yrs) & n.channel.isin([chan, 'Unified'])]
    for c in ['Unified', chan]:
        g = sub[sub.channel == c]
        if len(g) < 10:
            continue
        v = g.mother.value_counts().to_numpy()
        cum = np.cumsum(v) / v.sum()
        x = np.arange(1, len(v) + 1) / len(v)
        ls = '-' if 'Arm 1' in arm_lab else '--'
        ax.plot(np.concatenate([[0], x]), np.concatenate([[0], cum]),
                ls, color=COL[c], lw=1.9,
                label=f'{"Arm 1" if "Arm 1" in arm_lab else "Arm 2"} — {c}')
ax.plot([0, 1], [0, 1], ':', color='0.6', lw=1, label='even spread')
ax.set_xlabel('cumulative share of distinct sterile lines\n(most frequent first)')
ax.set_ylabel('cumulative share of approvals')
ax.set_title('(a) Concentration over sterile lines', fontsize=10, loc='left')
ax.legend(fontsize=6.5, loc='lower right', frameon=False)
ax.grid(alpha=.25)

# --- panel (b): HHI with bootstrap CIs ---
ax = axes[1]
pos, labels = [], []
i = 0
for arm_lab, chan, yrs in ARMS:
    sub = n[n.approval_year.isin(yrs) & n.channel.isin([chan, 'Unified'])]
    for c in ['Unified', chan]:
        g = sub[sub.channel == c]
        if len(g) < 10:
            continue
        obs = hhi(g.mother)
        boot = np.array([hhi(pd.Series(RNG.choice(g.mother.to_numpy(), len(g)))) for _ in range(B)])
        lo, hi = np.percentile(boot, [2.5, 97.5])
        # The percentile bootstrap interval for HHI need not bracket the point estimate
        # (resampling biases HHI upward), so the interval is drawn as its own segment
        # rather than as error bars hung off the observed value.
        ax.vlines(i, lo, hi, color=COL[c], lw=1.6)
        ax.hlines([lo, hi], i - 0.08, i + 0.08, color=COL[c], lw=1.4)
        ax.plot(i, obs, 'o', color=COL[c], ms=7, zorder=3)
        short = 'Arm 1\n2019–2022' if 'Arm 1' in arm_lab else 'Arm 2\n2017'
        pos.append(i); labels.append(f'{c}\n{short}')
        i += 1
    i += 0.6
ax.set_xticks(pos); ax.set_xticklabels(labels, fontsize=7.5)
ax.set_ylabel('sterile-line HHI (95% bootstrap CI)')
ax.set_title('(b) Concentration with uncertainty', fontsize=10, loc='left')
ax.grid(alpha=.25, axis='y')

fig.suptitle('Fig. 6. Germplasm concentration across resolved parental lines, by trial channel',
             fontsize=12, fontweight='bold', y=1.04)
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(f'{OUT}.{ext}', dpi=300, bbox_inches='tight')
print('wrote', OUT + '.png/.pdf')
