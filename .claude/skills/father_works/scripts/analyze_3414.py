#!/usr/bin/env python3
"""3414 肥料效应试验的完整再分析。

输入 trial.json，输出 data.json。正文与表格的每个数字都应由此产生，不要手算。

trial.json 最小结构：
{
  "plot_area_m2": 30,
  "plot_yield_kg": [19.8, 20.5, ...],          # 14 个小区实收产量，按处理 1~14 顺序
  "level_rates": {"N": [0,135,270,405],        # 各因素 4 个水平的实际用量 kg/hm2
                  "P": [0,90,180,270],
                  "K": [0,112.5,225,337.5]},
  "prices": {"grain": 2.58,                     # 稻谷价格必填
             "N": 4.54, "P": 6.67, "K": 5.33},  # 养分单价；若给了 products 可省略
  "products": {                                 # 可选：由肥料实物价与养分含量推导养分单价，
    "N": {"price": 2.10, "content": 0.463},     # 比直接写养分单价更准（正文也按实物价交代）
    "P": {"price": 0.80, "content": 0.12},
    "K": {"price": 3.20, "content": 0.60}},
  "traits": {                                   # 可选，缺则跳过性状分析
     "株高": [...], "穗长": [...], "有效穗": [...],
     "每穗总粒数": [...], "每穗实粒数": [...],
     "结实率": [...], "千粒重": [...]
  },
  "traits_per_mu": ["有效穗"]                   # 可选：以"万/667m2"记录、需 ×15 换算的性状
}

用法: python3 analyze_3414.py trial.json data.json
"""
import json
import sys

import numpy as np
from scipy import stats

# "3414" 标准处理编码：各处理的 (N,P,K) 水平号，顺序即处理 1~14
CODES = [(0, 0, 0), (0, 2, 2), (1, 2, 2), (2, 0, 2), (2, 1, 2), (2, 2, 2), (2, 3, 2),
         (2, 2, 0), (2, 2, 1), (2, 2, 3), (3, 2, 2), (1, 1, 2), (1, 2, 1), (2, 1, 1)]

FULL, CK = 6, 1                                   # 全肥区、无肥区的处理号
OMIT = {'N': 2, 'P': 4, 'K': 8}                   # 各缺素区的处理号
SERIES = {'N': [2, 3, 6, 11], 'P': [4, 5, 6, 7], 'K': [8, 9, 6, 10]}  # 单因素序列(水平0→3)


def ols(X, y):
    """最小二乘 + 回归显著性。返回 (系数, R2, 校正R2, F, P, 残差自由度)。"""
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ b
    ss_res = float((resid ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    n, p = X.shape
    df_r = n - p
    r2 = 1 - ss_res / ss_tot if ss_tot else float('nan')
    adj = 1 - (1 - r2) * (n - 1) / df_r if df_r > 0 else float('nan')
    if df_r > 0 and p > 1 and ss_res > 0:
        f = ((ss_tot - ss_res) / (p - 1)) / (ss_res / df_r)
        pv = float(1 - stats.f.cdf(f, p - 1, df_r))
    else:
        f = pv = float('nan')
    return b, r2, adj, float(f), pv, df_r


def main(inp, outp='data.json'):
    t = json.load(open(inp, encoding='utf-8'))
    area = t['plot_area_m2']
    plot = np.array(t['plot_yield_kg'], dtype=float)
    lv = {k: np.array(v, dtype=float) for k, v in t['level_rates'].items()}
    pr = dict(t['prices'])
    # 给了肥料实物价与养分含量时，据此推导养分单价——避免四舍五入后的养分单价带来累积误差
    for fac, d in t.get('products', {}).items():
        pr[fac] = d['price'] / d['content']
    out_prices = {k: (round(v, 2) if isinstance(v, float) else v) for k, v in pr.items()}

    # 小区产量 -> kg/hm2。这是全文所有产量数字的唯一来源。
    factor = 10000.0 / area
    y = plot * factor
    N = np.array([lv['N'][c[0]] for c in CODES])
    P = np.array([lv['P'][c[1]] for c in CODES])
    K = np.array([lv['K'][c[2]] for c in CODES])
    labels = [f"N{c[0]}P{c[1]}K{c[2]}" for c in CODES]

    out = {'plot_area_m2': area, 'yield_factor': round(factor, 4), 'prices': out_prices,
           # 小区称量 0.1 kg 对应的产量分辨率——讨论"处理间差异是否可判别"时要用
           'resolution_kg_hm2': round(0.1 * factor, 1)}

    # ---- 逐处理：产量、增产、经济效益 ----
    ck = y[CK - 1]
    rows = []
    for i in range(14):
        cost = N[i] * pr['N'] + P[i] * pr['P'] + K[i] * pr['K']
        val = y[i] * pr['grain']
        inc = y[i] - ck
        incval = inc * pr['grain']
        rows.append({
            'no': i + 1, 'label': labels[i], 'N': N[i], 'P': P[i], 'K': K[i],
            'plot_kg': plot[i], 'y_hm2': round(y[i], 1),
            'inc_vs_ck': round(inc, 1), 'inc_pct': round(inc / ck * 100, 1), 'rank': 0,
            'value': round(val, 1), 'cost': round(cost, 1), 'net': round(val - cost, 1),
            'incval': round(incval, 1), 'incnet': round(incval - cost, 1),
            'ratio': (round(incval / cost, 2) if cost > 0 else None),
        })
    for r, i in enumerate(sorted(range(14), key=lambda i: -y[i])):
        rows[i]['rank'] = r + 1

    # 性状并入行；以"万/667m2"记录的性状换算为"万/hm2"
    per_mu = set(t.get('traits_per_mu', []))
    traits = {k: np.array(v, dtype=float) for k, v in t.get('traits', {}).items()}
    for k in list(traits):
        if k in per_mu:
            traits[k] = traits[k] * 15
        for i in range(14):
            rows[i][k] = round(float(traits[k][i]), 1)
    out['rows'] = rows
    out['trait_range'] = {k: [float(v.min()), float(v.max())] for k, v in traits.items()}

    # ---- 三元二次方程 + 典型性检验 ----
    X3 = np.column_stack([np.ones(14), N, P, K, N**2, P**2, K**2, N*P, N*K, P*K])
    b, r2, adj, f, pv, dfr = ols(X3, y)
    H = np.array([[2*b[4], b[7], b[8]], [b[7], 2*b[5], b[9]], [b[8], b[9], 2*b[6]]])
    eig = np.linalg.eigvals(H)
    try:
        stat = np.linalg.solve(H, -b[1:4])
    except np.linalg.LinAlgError:
        stat = np.array([float('nan')] * 3)
    hi = [lv['N'].max(), lv['P'].max(), lv['K'].max()]
    in_range = [bool(0 <= s <= h) for s, h in zip(stat, hi)]
    out['ternary'] = {
        'coef': [round(float(v), 6) for v in b], 'R2': round(r2, 4), 'adj_R2': round(adj, 4),
        'F': round(f, 3), 'p': round(pv, 4), 'df_res': dfr,
        'stationary': [round(float(v), 1) for v in stat],
        'stationary_in_range': in_range,
        'eigH': [round(float(v), 5) for v in eig],
        # 典型性：驻点须为极大值点（Hessian 负定）且落在试验范围内
        'is_maximum': bool(np.all(eig < 0)),
        'typical': bool(np.all(eig < 0) and all(in_range)),
    }

    # ---- 单因素：一元二次、线性、线性加平台 ----
    single, lin, lpp = {}, {}, {}
    rate_of = {'N': N, 'P': P, 'K': K}
    for fac, seq in SERIES.items():
        idx = [i - 1 for i in seq]
        x = rate_of[fac][idx]
        yy = y[idx]

        X1 = np.column_stack([np.ones(4), x, x**2])
        b1, r21, _, f1, p1, _ = ols(X1, yy)
        xmax = -b1[1] / (2 * b1[2]) if b1[2] else float('nan')
        ymax = b1[0] + b1[1] * xmax + b1[2] * xmax ** 2 if b1[2] else float('nan')
        xeco = (pr[fac] / pr['grain'] - b1[1]) / (2 * b1[2]) if b1[2] else float('nan')
        single[fac] = {
            'x': [float(v) for v in x], 'y': [round(float(v), 1) for v in yy],
            'coef': [round(float(v), 6) for v in b1], 'R2': round(r21, 4),
            'F': round(f1, 2), 'p': round(p1, 3),
            'xmax': round(float(xmax), 1), 'ymax': round(float(ymax), 1),
            'xeco': round(float(xeco), 1),
            # 典型：一次项为正、二次项为负（符合报酬递减）
            'typical': bool(b1[1] > 0 and b1[2] < 0),
            'xmax_in_range': bool(0 <= xmax <= x.max()),
        }

        A = np.column_stack([np.ones(4), x])
        c, *_ = np.linalg.lstsq(A, yy, rcond=None)
        ssr = float(((yy - A @ c) ** 2).sum())
        sst = float(((yy - yy.mean()) ** 2).sum())
        lin[fac] = {'a': round(float(c[0]), 1), 'b': round(float(c[1]), 3),
                    'R2': round(1 - ssr / sst, 4),
                    'r': round(float(np.corrcoef(x, yy)[0, 1]), 4)}

        # 线性加平台：产量出现平台时比一元二次更贴合
        best = None
        for x0 in np.linspace(x[1], x[-1], 400):
            A2 = np.column_stack([np.ones(4), np.minimum(x, x0)])
            c2, *_ = np.linalg.lstsq(A2, yy, rcond=None)
            ss = float(((yy - A2 @ c2) ** 2).sum())
            if best is None or ss < best[0]:
                best = (ss, float(x0), c2)
        ss, x0, c2 = best
        lpp[fac] = {'a': round(float(c2[0]), 1), 'b': round(float(c2[1]), 3),
                    'x0': round(x0, 1), 'plateau': round(float(c2[0] + c2[1] * x0), 1),
                    'R2': round(1 - ss / sst, 4)}
    out['single'], out['linear'], out['lpp'] = single, lin, lpp

    # ---- 土壤供肥能力：缺素区相对产量、贡献率、农学效率 ----
    full = y[FULL - 1]
    dfc = {}
    for fac, tr in OMIT.items():
        amt = rate_of[fac][FULL - 1]
        dfc[fac] = {'treat': tr, 'yield': round(float(y[tr - 1]), 1),
                    'rel': round(float(y[tr - 1] / full * 100), 1),
                    'contrib': round(float((full - y[tr - 1]) / full * 100), 1),
                    'ae': round(float((full - y[tr - 1]) / amt), 2) if amt else None}
    dfc['CK'] = {'treat': CK, 'yield': round(float(ck), 1),
                 'rel': round(float(ck / full * 100), 1),
                 'contrib': round(float((full - ck) / full * 100), 1)}
    # 以最高产处理为基数的相对产量：审稿人常问基数敏感性，先算好备用
    best_t = int(max(range(14), key=lambda i: y[i]))
    dfc['_alt_base'] = {'treat': best_t + 1,
                        **{f: round(float(y[OMIT[f] - 1] / y[best_t] * 100), 1) for f in OMIT}}
    out['deficiency'] = dfc

    # ---- 相邻水平间的边际效益 ----
    mg = []
    for fac, seq in SERIES.items():
        rates = rate_of[fac]
        for j in range(1, 4):
            a, bq = seq[j - 1] - 1, seq[j] - 1
            dy = float(y[bq] - y[a])
            dcost = float((rates[bq] - rates[a]) * pr[fac])
            mg.append({'f': fac, 'from': j - 1, 'to': j, 'dy': round(dy, 1),
                       'dval': round(dy * pr['grain'], 1), 'cost': round(dcost, 1),
                       'ratio': round(dy * pr['grain'] / dcost, 2) if dcost else None})
    out['marginal'] = mg

    # ---- 产量与性状的相关分析（n=14, df=12）----
    if traits:
        cor = {}
        for k, v in traits.items():
            r = float(np.corrcoef(v, y)[0, 1])
            tv = r * np.sqrt(12 / (1 - r * r)) if abs(r) < 1 else float('inf')
            cor[k] = {'r': round(r, 3),
                      'p': round(float(2 * (1 - stats.t.cdf(abs(tv), 12))), 4)}
        out['corr'] = cor
        out['corr_crit'] = {'n': 14, 'df': 12, 'r05': 0.532, 'r01': 0.661}

    json.dump(out, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # 把需要在正文里如实交代的判断直接打出来，避免写作时想当然
    tern = out['ternary']
    print(f"产量 {min(r['y_hm2'] for r in rows)}~{max(r['y_hm2'] for r in rows)} kg/hm2，"
          f"最高为处理{best_t + 1}；小区 0.1 kg = {out['resolution_kg_hm2']} kg/hm2")
    print(f"三元二次：R2={tern['R2']} 校正R2={tern['adj_R2']} F={tern['F']} P={tern['p']} "
          f"df残={tern['df_res']}；驻点{tern['stationary']} 在范围内={tern['stationary_in_range']}；"
          f"特征值{tern['eigH']} -> {'通过' if tern['typical'] else '未通过'}典型性检验")
    for fac in ('N', 'P', 'K'):
        s = single[fac]
        print(f"  {fac}: R2={s['R2']} F={s['F']} P={s['p']} "
              f"{'典型' if s['typical'] else '非典型'} 最高产量点{s['xmax']}"
              f"{'' if s['xmax_in_range'] else '(超出试验范围)'}；"
              f"线性加平台 拐点{lpp[fac]['x0']} R2={lpp[fac]['R2']}")
    print("相对产量 " + "，".join(f"缺{f} {dfc[f]['rel']}%" for f in OMIT)
          + f"；无肥区 {dfc['CK']['rel']}%")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'data.json')
