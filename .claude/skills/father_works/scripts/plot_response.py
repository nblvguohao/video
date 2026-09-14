#!/usr/bin/env python3
"""氮磷钾单因素肥料效应三合一图。读 analyze_3414.py 输出的 data.json，产出 fig1.png/pdf。

用法: python3 plot_response.py data.json [fig1]

图中同时画一元二次拟合曲线（虚线）与线性/线性加平台拟合曲线（实线），配实测点。
氮固定用线性加平台，磷、钾根据是否更贴合平台形态选择——若某因素的线性加平台 R²
明显高于一元二次（如高出 0.02 以上），说明该因素也出现了平台，改用线性加平台；
否则用普通线性。这样图与正文 2.4.2 的表述自动保持一致，不需要手动判断。

坐标轴标目统一写"量/单位"斜线式（如 kg/hm²），不要与正文表格的单位写法不一致——
这是期刊格式评审最容易挑出的一条，见 references/journal-format.md。
"""
import json
import sys

import matplotlib
import numpy as np

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402


def main(data_path, out_stem='fig1'):
    d = json.load(open(data_path, encoding='utf-8'))

    plt.rcParams['font.family'] = ['Liberation Serif', 'WenQuanYi Zen Hei', 'DejaVu Sans']
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['mathtext.fontset'] = 'stix'

    factors = [f for f in ('N', 'P', 'K') if f in d.get('single', {})]
    labels = {'N': '施N量', 'P': '施P₂O₅量', 'K': '施K₂O量'}
    tags = 'abcdefgh'

    fig, axes = plt.subplots(1, len(factors), figsize=(17 / 2.54, 6.2 / 2.54), dpi=600)
    if len(factors) == 1:
        axes = [axes]

    all_y = [v for f in factors for v in d['single'][f]['y']]
    ylo = 500 * ((min(all_y) - 300) // 500)
    yhi = 500 * ((max(all_y) + 500) // 500 + 1)

    for ax, f, tag in zip(axes, factors, tags):
        s = d['single'][f]
        x = np.array(s['x'])
        y = np.array(s['y'])
        b = s['coef']
        xx = np.linspace(0, x.max(), 200)

        ax.plot(xx, b[0] + b[1] * xx + b[2] * xx ** 2, '--', color='0.35', lw=0.9, label='一元二次')

        lpp = d.get('lpp', {}).get(f)
        lin = d.get('linear', {}).get(f)
        # 平台更贴合时用线性加平台，否则用普通线性；两者都没有就跳过第二条曲线
        use_lpp = lpp and (not lin or lpp['R2'] - lin['R2'] > 0.02)
        if use_lpp:
            yy = np.where(xx < lpp['x0'], lpp['a'] + lpp['b'] * xx, lpp['plateau'])
            ax.plot(xx, yy, '-', color='k', lw=0.9, label='线性加平台')
        elif lin:
            ax.plot(xx, lin['a'] + lin['b'] * xx, '-', color='k', lw=0.9, label='线性')

        ax.plot(x, y, 'o', ms=3.5, mfc='k', mec='k', label='实测值')
        ax.set_xlabel(f'{labels[f]}/(kg/hm²)', fontsize=7.5)
        ax.set_ylabel('产量/(kg/hm²)', fontsize=7.5)
        ax.set_ylim(ylo, yhi)
        ax.set_xlim(-0.04 * x.max(), 1.06 * x.max())
        ax.set_xticks(x)
        ax.tick_params(labelsize=7, direction='in', length=2.5)
        ax.text(0.03, 0.92, f'({tag})', transform=ax.transAxes, fontsize=8)
        ax.legend(fontsize=6.2, frameon=False, loc='lower right', handlelength=1.6)
        for sp in ax.spines.values():
            sp.set_linewidth(0.6)

    plt.tight_layout(pad=0.4, w_pad=0.8)
    plt.savefig(f'{out_stem}.png', dpi=600)
    plt.savefig(f'{out_stem}.pdf')
    print(f'已生成 {out_stem}.png / {out_stem}.pdf')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'fig1')
