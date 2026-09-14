export const meta = {
  name: 'quanyin-evidence-index',
  description: 'Build evidence/00_INDEX.md summarizing all evidence files, core numbers, datasets, exemplar literature, and contradictions',
  phases: [{ title: 'Index' }],
}
const EV = '/home/user/video/evidence'
phase('Index')
const index = await agent(`通读 ${EV}/ 下全部文件（ls -la; 逐个 cat，大文件分段读完），写出 ${EV}/00_INDEX.md：(1) 每个文件一段摘要（≤150 字）+ 来源数；(2) "论文可用的核心数字速查表"（公司面板、品种数、超级稻、再生稻、订单农业、要约收购、研发投入、行业数据），每个数字附来源文件与置信度，并标注核查文件（11_fact_verification_*.md）中被质疑的条目；(3) "可用数据集清单"（列出 evidence/ 下所有 CSV 的字段与行数，用 Bash wc -l / head 查看）；(4) "方法学范本文献"与"理论框架文献"各列 8–12 篇（完整引文+DOI）；(5) 已知矛盾与待人工确认事项；(6) 对论文主题的初步可行性评估（3–5 条候选方向，各 2 句）。用中文，UTF-8。完成后返回 00_INDEX.md 全文。`,
  { label: 'index', phase: 'Index', effort: 'high' })
return { index }
