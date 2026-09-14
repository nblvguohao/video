export const meta = {
  name: 'quanyin-journal-eval',
  description: 'Evaluate candidate CAS-Q2 agriculture journals against the chosen theme; pick target and write the format spec',
  phases: [{ title: 'Evaluate' }, { title: 'Decide' }],
}
const ROOT = '/home/user/video'
const EV = ROOT + '/evidence'
const PL = ROOT + '/plan'
const ENV_NOTE = `工具约束：WebFetch/curl 几乎全被拦截（github.com 除外）；WebSearch 可用且带页面摘要（可查期刊官网 Guide for Authors 的摘要、中科院分区、影响因子、近年文章）；学术 MCP（Consensus、Scholar Gateway、Elicit、Undermind）可用于找该刊近 3 年的同类论文。严禁编造分区/影响因子；不确定则标注"待确认"并给出检索到的原话。`
const JSCHEMA = {
  type: 'object',
  properties: {
    journal: { type: 'string' }, cas_2025_major: { type: 'string' }, cas_2025_minor: { type: 'string' }, is_top: { type: 'boolean' }, impact_factor: { type: 'string' },
    scope_fit_1to10: { type: 'number' }, evidence_of_fit: { type: 'array', items: { type: 'string' } },
    article_types: { type: 'string' }, word_limit: { type: 'string' }, abstract_rules: { type: 'string' }, reference_style: { type: 'string' }, figure_rules: { type: 'string' }, sections_required: { type: 'string' }, apc_oa: { type: 'string' }, review_time: { type: 'string' },
    risks: { type: 'array', items: { type: 'string' } }, file: { type: 'string' },
  },
  required: ['journal', 'cas_2025_major', 'cas_2025_minor', 'is_top', 'impact_factor', 'scope_fit_1to10', 'evidence_of_fit', 'article_types', 'word_limit', 'abstract_rules', 'reference_style', 'figure_rules', 'sections_required', 'apc_oa', 'review_time', 'risks', 'file'],
}
const cands = (args && args.candidates) || []
phase('Evaluate')
const evals = await parallel(cands.map(j => () =>
  agent(`你是期刊评估员。${ENV_NOTE}\n\n先读 ${PL}/01_theme_and_innovation.md 与 ${PL}/02_research_route.md 了解论文主题、数据与方法。然后深入评估期刊《${j}》：\n(1) 2025 年中科院分区（大类农林科学分区、小类分区、是否 Top）、最新影响因子、JCR 分区、年发文量、中国作者比例；\n(2) 范围契合度：用 Consensus/Scholar Gateway/Elicit/WebSearch 找该刊 2022–2026 年发表的与本论文最接近的 3–5 篇论文（完整引文+DOI），说明相似点；该刊是否接受"企业案例+公开数据的定量分析"类型；\n(3) 投稿格式要求（来自 Guide for Authors 的检索摘要）：文章类型与字数上限、摘要结构与字数、关键词数、章节结构（是否要求 Highlights / Graphical abstract / 结构化摘要）、参考文献格式（作者-年份或编号；给出 1 条期刊文章与 1 条图书的示例格式）、图表要求（分辨率、格式、彩色费用）、单位/统计报告要求、数据可用性/利益冲突/作者贡献声明要求、投稿系统、APC/OA 政策、平均审稿周期；\n(4) 风险：与本文主题的偏离、拒稿常见原因、是否在预警名单。\n把评估写入 ${PL}/journals/eval_${j.replace(/[^A-Za-z0-9]+/g, '_')}.md。`,
    { label: `eval:${j.slice(0, 30)}`, phase: 'Evaluate', schema: JSCHEMA, effort: 'high' })
))
const ok = evals.filter(Boolean)
phase('Decide')
const decision = await agent(`你是投稿策略顾问。${ENV_NOTE}\n\n候选期刊评估摘要：${JSON.stringify(ok.map(e => ({ j: e.journal, major: e.cas_2025_major, minor: e.cas_2025_minor, top: e.is_top, if: e.impact_factor, fit: e.scope_fit_1to10, risks: e.risks })))}\n\n读取 ${PL}/journals/ 下全部评估文件与 ${PL}/01_theme_and_innovation.md。写出：\n1) ${PL}/03_target_journal.md：候选期刊对比表（分区、IF、契合度、格式负担、审稿周期、风险）、最终选择（首选 + 2 个备选）及理由、对论文定位/标题/摘要的针对性调整建议。\n2) ${PL}/04_format_spec.md：首选期刊的完整撰写规范清单（文章类型、字数、标题/摘要/关键词/Highlights 规则、章节结构与命名、图表规范、参考文献格式与文内引用格式（附 5 条示例：期刊论文、图书、章节、报告/公告、网页）、单位与统计表述、声明部分（数据可用性、利益冲突、作者贡献、致谢、资助）、投稿清单）。所有条目注明来源（检索到的 Guide for Authors 原话或 URL）；不确定项标"待确认"。\n返回 03_target_journal.md 全文。`,
  { label: 'decide', phase: 'Decide', effort: 'high' })
return { evals: ok.map(e => ({ journal: e.journal, major: e.cas_2025_major, minor: e.cas_2025_minor, fit: e.scope_fit_1to10 })), decision }
