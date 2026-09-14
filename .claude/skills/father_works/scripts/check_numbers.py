#!/usr/bin/env python3
"""核对正文里的每一个数字是否与 data.json 一致。

写作和修订之后都要跑。凭眼看必然漏，这类不一致是审稿人一眼能看见的硬伤。

用法:
    python3 check_numbers.py data.json manuscript.md [--strict] [--ignore 1.65,46.3]

做两件事：
1. 抽出正文里的数字，凡在 data.json 里找不到对应值的列出来，附上下文供人工确认。
   匹配是数值容差匹配（允许四舍五入），不是字符串匹配。
2. 检查未设重复情形下不该出现的统计学推断措辞。

未匹配的数字不一定是错的——可能来自原始资料（土壤 pH、肥料含量、播种日期）、
文献、标准号。逐条看上下文即可判断；确认无误的可用 --ignore 加入白名单。

--strict 时任何未匹配数字都以非零码退出，适合放进自动化流程。
"""
import json
import re
import sys


def collect_numbers(obj, acc):
    if isinstance(obj, dict):
        for v in obj.values():
            collect_numbers(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            collect_numbers(v, acc)
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        acc.add(float(obj))
    return acc


def matches(tok, values):
    """数值容差匹配：正文写 0.01097，data.json 里是 -0.010974，应判为一致。"""
    try:
        x = float(tok)
    except ValueError:
        return True
    dec = len(tok.split('.')[1]) if '.' in tok else 0
    for v in (x, -x):
        for d in values:
            if round(d, dec) == round(v, dec):
                return True
            # 正文常把 kg/hm² 写成整数，data.json 里是 .0
            if dec == 0 and abs(d - v) < 0.05:
                return True
    return False


FORBIDDEN = [
    (r'显著(提高|增加|影响|改善|差异)', '未设重复时不应使用"显著"描述处理间差异'),
    (r'差异(达)?(极)?显著', '未设重复无法做差异显著性检验'),
    (r'(进行|采用)方差分析', '未设重复不能做方差分析'),
    (r'(进行|采用)多重比较', '未设重复不能做多重比较'),
]
ALLOW_CONTEXT = ['相关', 'r=', '*r*', 'R2', 'R²', '回归', '未达显著', '不显著',
                 '未作差异显著性检验', '无法进行方差分析', '不使用"显著"',
                 '未进行方差分析和多重比较', '不作为', '仅用于']

# 结构性数字，不是数据：章节号、中图分类号、标准号、GB/T 编号、版本号
STRUCTURAL = re.compile(
    r'(^|[^\d.])('
    r'\d{1,2}\.\d{1,2}(?=\s*[　\s]*[^\d])'      # 章节号 1.1 / 2.4
    r'|7714|2911|1118|3414'                       # 常见标准号与试验方案名
    r')')


def main(argv):
    data_path, md_path = argv[1], argv[2]
    strict = '--strict' in argv
    ignore = set()
    if '--ignore' in argv:
        ignore = {s.strip() for s in argv[argv.index('--ignore') + 1].split(',')}

    values = collect_numbers(json.load(open(data_path, encoding='utf-8')), set())
    md = open(md_path, encoding='utf-8').read()

    # 表格与正文一起查；跳过标题行里的章节号
    lines = [l for l in md.split('\n')
             if not re.match(r'^\s*\*{0,2}\d+(\.\d+)*[　\s]', l)      # 章节标题
             and '{width=' not in l]                                   # pandoc 导出的图片属性行
    body = '\n'.join(lines)

    tokens = re.findall(r'(?<![\d.\-])(\d+\.\d+|\d{3,})(?![\d.])', body)
    unknown = {}
    for t in tokens:
        if t in ignore:
            continue
        if re.fullmatch(r'(19|20)\d{2}', t) or re.fullmatch(r'\d{6}', t):
            continue          # 年份、邮编
        if re.fullmatch(r'7714|2911|1118|3414|1000|10000', t):
            continue          # 标准号、换算常数
        if matches(t, values):
            continue
        unknown.setdefault(t, 0)
        unknown[t] += 1

    print(f"正文数字 {len(tokens)} 个，未能在 data.json 中匹配 {len(unknown)} 个")
    for t, n in sorted(unknown.items(), key=lambda kv: -kv[1]):
        m = re.search(r'.{0,30}' + re.escape(t) + r'.{0,30}', body)
        ctx = m.group(0).replace('\n', ' ') if m else ''
        print(f"  {t}  ×{n}   …{ctx}…")
    if unknown:
        print("  ^ 逐条看上下文：来自原始资料/文献/标准的属正常，"
              "应由 data.json 产生却对不上的是错误")

    print()
    issues = []
    for pat, why in FORBIDDEN:
        for m in re.finditer(pat, md):
            s = max(0, m.start() - 70)
            ctx = md[s:m.end() + 70].replace('\n', ' ')
            if any(a in ctx for a in ALLOW_CONTEXT):
                continue
            issues.append(f"  {why}\n      …{ctx}…")
    print(f"表述检查：{'发现 %d 处可疑' % len(issues) if issues else '未发现问题'}")
    print('\n'.join(issues))

    if strict and unknown:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
