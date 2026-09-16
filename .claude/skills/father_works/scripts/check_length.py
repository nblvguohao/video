#!/usr/bin/env python3
"""篇幅体检：正文汉字数、表图数量、页数，并与参照论文对比。

写完初稿和每次修订后都跑一下。篇幅超标是中文农业期刊最常见的退修原因之一，
而且越晚发现越难改——等全文写完再砍，往往要动结构。

用法:
    python3 check_length.py manuscript.md [manuscript.pdf] [--ref 参照论文.txt ...]
    python3 check_length.py manuscript.md manuscript.pdf --target 3800

不传 --target 时用默认区间（省级农业科技期刊试验报告 3000~4500 汉字）。
传了参照论文就以参照论文的字数为基准，比默认区间更贴合目标刊物。
"""
import re
import subprocess
import sys

DEFAULT_LO, DEFAULT_HI = 3000, 4500


def hanzi(s):
    return len(re.findall(r'[一-鿿]', s))


def pdf_pages(path):
    try:
        out = subprocess.run(['pdfinfo', path], capture_output=True, text=True).stdout
        m = re.search(r'Pages:\s+(\d+)', out)
        return int(m.group(1)) if m else None
    except FileNotFoundError:
        return None


def main(argv):
    md_path = argv[1]
    pdf_path = next((a for a in argv[2:] if a.endswith('.pdf')), None)
    refs = []
    if '--ref' in argv:
        i = argv.index('--ref') + 1
        while i < len(argv) and not argv[i].startswith('--'):
            refs.append(argv[i]); i += 1
    target = None
    if '--target' in argv:
        target = int(argv[argv.index('--target') + 1])

    md = open(md_path, encoding='utf-8').read()

    # 分段统计：摘要之前是题名作者，参考文献之后不计入正文
    before_refs = re.split(r'\n\s*参考文献\s*\n', md)[0]
    # 摘要与英文摘要
    abs_cn = ''
    m = re.search(r'摘要(.*?)关键词', before_refs, re.S)
    if m:
        abs_cn = m.group(1)
    # 正文＝去掉摘要区之后的部分
    body = before_refs
    m2 = re.search(r'Key\s*words[^\n]*\n', before_refs)
    if m2:
        body = before_refs[m2.end():]

    n_body = hanzi(body)
    n_abs = hanzi(abs_cn)
    n_all = hanzi(md)

    tables = len(re.findall(r'^\s*表\s*\d+[　\s]', md, re.M))
    figs = len(re.findall(r'^\s*图\s*\d+[　\s]', md, re.M))
    nrefs = len(re.findall(r'^\s*\[\d+\]', md, re.M))

    print(f'正文汉字数        {n_body}')
    print(f'中文摘要汉字数    {n_abs}')
    print(f'全文汉字数        {n_all}')
    print(f'表 / 图 / 参考文献 {tables} / {figs} / {nrefs}')
    if pdf_path:
        p = pdf_pages(pdf_path)
        if p:
            print(f'A4 单栏页数       {p}  (期刊双栏约 {round(p * 0.45)}~{round(p * 0.5)} 个版面)')

    if refs:
        print('\n参照论文：')
        base = []
        for r in refs:
            try:
                n = hanzi(open(r, encoding='utf-8').read())
            except OSError:
                print(f'  {r}  读取失败'); continue
            base.append(n)
            print(f'  {r.split("/")[-1][:34]:36} {n} 字')
        if base:
            target = target or max(base)

    lo, hi = (int(target * 0.85), int(target * 1.15)) if target else (DEFAULT_LO, DEFAULT_HI)
    print(f'\n目标区间 {lo}~{hi} 汉字')
    if n_body < lo:
        print(f'  偏短 {lo - n_body} 字——内容可能不足以支撑一篇完整试验报告')
    elif n_body > hi:
        over = n_body - hi
        print(f'  超出 {over} 字（{over / hi * 100:.0f}%）。优先砍：正文复述表格的段落、'
              f'引言的地理背景铺陈、可合并的同维度表、独立成段的限定说明')
    else:
        print('  篇幅合适')

    if tables > 7:
        print(f'  表 {tables} 张偏多，考虑合并按处理排列的同维度表')
    if n_abs and not (250 <= n_abs <= 450):
        print(f'  中文摘要 {n_abs} 字，结构式摘要以 300~450 字为宜')


if __name__ == '__main__':
    main(sys.argv)
