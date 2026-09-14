export const meta = {
  name: 'quanyin-analysis',
  description: 'Run the quantitative analyses of the research route on collected data: scripts, figures, tables, results notes; then independent reproduction check',
  phases: [{ title: 'Analyze' }, { title: 'Reproduce' }],
}
const ROOT = '/home/user/video'
const NOTE = `工具与规范：Python 3.11，已装 pandas/numpy/scipy/matplotlib（中文字体用 'WenQuanYi Zen Hei'，但论文图表一律用英文标签）；图存 ${ROOT}/figures/（PNG 300 dpi + 同名 PDF），脚本存 ${ROOT}/scripts/analysis/（每个脚本可独立运行：python3 script.py），表格以 Markdown 写入 ${ROOT}/manuscript/tables/。所有数据只能来自 ${ROOT}/evidence/data/ 与 ${ROOT}/evidence/*.csv；严禁伪造或插补数据；样本量、缺失处理、统计检验（含 p 值/置信区间/效应量）必须如实报告。图表遵循期刊规范（读取 ${ROOT}/plan/04_format_spec.md）：无图题在图内、字体≥8pt、色盲友好配色、单栏宽 ~85–90 mm 双栏 ~170–180 mm。`
const SCHEMA = { type: 'object', properties: { scripts: { type: 'array', items: { type: 'string' } }, figures: { type: 'array', items: { type: 'string' } }, tables: { type: 'array', items: { type: 'string' } }, notes_file: { type: 'string' }, key_results: { type: 'array', items: { type: 'string' } }, caveats: { type: 'array', items: { type: 'string' } } }, required: ['scripts', 'figures', 'tables', 'notes_file', 'key_results', 'caveats'] }
const blocks = (args && args.blocks) || []
phase('Analyze')
const out = await parallel(blocks.map(b => () =>
  agent(`你是定量分析员。${NOTE}\n\n先读 ${ROOT}/plan/02_research_route.md（方法、图表清单、论证地图）与 ${ROOT}/evidence/data/ 下的 *.report.md 了解数据状况。\n\n分析块 ${b.id}：${b.instructions}\n\n产出：脚本、图（编号按 route 中的图表清单）、表、以及 ${ROOT}/manuscript/results_notes_${b.id}.md（每个结果一段：数字、检验、对应图表、解释边界；并列出"不能支持的说法"）。返回结构化结果。`,
    { label: `analyze:${b.id}`, phase: 'Analyze', schema: SCHEMA, effort: 'high' })
))
const ok = out.filter(Boolean)
phase('Reproduce')
const rep = await agent(`你是独立复现员。${NOTE}\n\n对 ${ROOT}/scripts/analysis/ 下每个脚本：清空 ${ROOT}/figures/ 中对应输出后重新运行（python3），确认无错误、图表文件生成、结果数字与 ${ROOT}/manuscript/results_notes_*.md 中一致（逐个数字对照，容差 0.5%）。检查：样本量陈述是否与 CSV 行数一致；是否有静默丢弃缺失值而未报告；统计方法是否与数据结构匹配（如时间趋势用回归斜率并报告 CI；组间比较用合适检验；多重比较说明）。把复现报告写入 ${ROOT}/manuscript/reproduction_report.md，列出不一致项并直接修正 results_notes（保留原文并标注修正）。返回报告全文。`,
  { label: 'reproduce', phase: 'Reproduce', effort: 'high' })
return { blocks: ok.map(o => ({ notes: o.notes_file, figs: o.figures, tables: o.tables, key: o.key_results })), reproduction: (rep || '').slice(0, 6000) }
