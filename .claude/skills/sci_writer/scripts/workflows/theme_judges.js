export const meta = {
  name: 'quanyin-theme-judges',
  description: 'Judge panel scores proposals from 3 lenses, then a synthesizer writes the final theme, innovation, argument map and research route',
  phases: [{ title: 'Judge' }, { title: 'Synthesize' }],
}
const ROOT = '/home/user/video'
const EV = ROOT + '/evidence'
const PL = ROOT + '/plan'
const ENV_NOTE = `
工具与环境约束（必须遵守）：
- 容器内 curl/WebFetch 对几乎所有站点被代理拦截；但 github.com 可访问：可用 "git clone --depth 1" 克隆公开仓库、用 WebFetch 读 raw.githubusercontent.com 文件（已有年报文本仓库 IamBusy/audit、品种审定汇编 he-zhui/Rice_QA 等先例）。
- WebSearch 可用且结果自带页面摘要，但每个代理会话有配额（约 200 次，且可能提前耗尽）：先列出最有价值的查询再执行，措辞具体（主体+年份+指标），避免重复。
- 学术工具：mcp__Consensus__search 本月配额已耗尽、mcp__Elicit__* 无 API 权限——不要调用。可用：mcp__Undermind__*（先 get_orientation；search_papers / launch_deep_search / lookup_papers_by_metadata / read_pdfs 读开放获取 PDF）、mcp__Scholar_Gateway__semanticSearch（返回长文本，用 grep/Read 分块）、mcp__PubMed__*、mcp__Amass_Connector__search_amass_biomedcore_records、mcp__bioRxiv__*、mcp__Hugging_Face__hf_fs。用 ToolSearch 按名加载后调用。
- 严禁编造任何数字、品种名、项目名、文献。找不到就写"未找到/未确认"。每条事实附来源 URL、日期、检索词、置信度（高=原文数字直接出现；中=工具综合表述；低=推断）。文献给完整引文与 DOI。
- 输出用 UTF-8 写入指定路径（Bash heredoc / python / Write）。
`
const JUDGE = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    scores: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, novelty: { type: 'number' }, feasibility: { type: 'number' }, fit_cas_q2: { type: 'number' }, rigor: { type: 'number' }, generality: { type: 'number' }, total: { type: 'number' }, comment: { type: 'string' } }, required: ['id', 'novelty', 'feasibility', 'fit_cas_q2', 'rigor', 'generality', 'total', 'comment'] } },
    best_id: { type: 'string' },
    graft_ideas: { type: 'array', items: { type: 'string' } },
  },
  required: ['lens', 'scores', 'best_id', 'graft_ideas'],
}
const LENSES = [
  { id: 'editor', desc: '中科院 2 区农林科学期刊的责任编辑/审稿人视角：范围契合、读者兴趣、单一企业案例的一般性、是否像"软文"（企业宣传风险）、方法是否达到该刊常见标准' },
  { id: 'data', desc: '数据可得性与研究诚信视角：每个变量能否在本环境（仅 WebSearch 摘要 + 文献）真实获得？样本量是否足够？是否存在被迫编造/估算的风险？统计方法与数据结构是否匹配？' },
  { id: 'novelty', desc: '学术新颖性与理论贡献视角：与最接近的 3–5 篇已有文献相比（可用 Undermind/Scholar Gateway 核实），创新点是否真实、是否可被审稿人一句话否定；框架/指标/数据集的原创性' },
]
const proposals = (args && args.proposals) || []
phase('Judge')
const judges = await parallel(LENSES.map(l => () =>
  agent(`你是评审团成员，视角：${l.desc}。${ENV_NOTE}\n\n读取 ${PL}/proposals/ 下所有 proposal_*.md（ls; cat），并参考 ${EV}/00_INDEX.md 与 ${EV}/09_data_feasibility.md。对每个方案按 5 维打分（各 1–10：novelty、feasibility、fit_cas_q2、rigor、generality），total 为加权（feasibility×0.3 + novelty×0.25 + fit×0.2 + rigor×0.15 + generality×0.1，满分 10），给出一句话评语；指出最佳方案 id，并列出其他方案中值得嫁接的想法（graft_ideas）。把你的评审写入 ${PL}/judge_${l.id}.md。`,
    { label: `judge:${l.id}`, phase: 'Judge', schema: JUDGE, effort: 'high' })
))
const jOk = judges.filter(Boolean)
// aggregate
const agg = {}
for (const j of jOk) for (const s of j.scores) { agg[s.id] = agg[s.id] || { id: s.id, sum: 0, n: 0 }; agg[s.id].sum += s.total; agg[s.id].n += 1 }
const ranking = Object.values(agg).map(a => ({ id: a.id, mean: a.sum / a.n })).sort((a, b) => b.mean - a.mean)
log(`Ranking: ${ranking.map(r => r.id + '=' + r.mean.toFixed(2)).join(', ')}`)

phase('Synthesize')
const synth = await agent(`你是论文总设计师。${ENV_NOTE}\n\n评审团排名（均分）：${JSON.stringify(ranking)}\n评审细节：${JSON.stringify(jOk.map(j => ({ lens: j.lens, best: j.best_id, graft: j.graft_ideas, scores: j.scores.map(s => ({ id: s.id, total: s.total, c: s.comment })) }))).slice(0, 20000)}\n\n读取 ${PL}/proposals/ 全部方案与 ${PL}/judge_*.md，以排名第一的方案为骨架，嫁接其他方案的最佳想法，写出以下文件（中文为主，英文题名/摘要）：\n1) ${PL}/01_theme_and_innovation.md：最终题目（英/中）、一句话论点（one-sentence argument）、研究问题（3 个以内）、创新点（3 条，各说明"相对谁新"并引用最接近文献）、论文类型与目标读者、为什么荃银高科是合适的案例（并说明如何避免"企业软文"观感：客观呈现负面证据如订单粮食负毛利、争议报道）。\n2) ${PL}/02_research_route.md：数据方案（变量定义表：变量、单位、来源、获取方式、预计样本量、置信度）、方法（模型/指标公式、稳健性检验）、图表清单（编号、内容、数据来源、绘制方式），论证地图（argument map：claim → evidence → 图表/文献）、各章节契约（purpose / allowed claims / forbidden claims / inputs），风险登记与应对，工作分解（数据采集任务清单：需要检索的条目列表与数量，可分配给多个代理并行）。\n3) ${PL}/00_decision_log.md：评审团结果、被否方案及原因、待人工确认事项。\n严格遵守：只使用证据库确认可获得的数据；标明每个待采集数据的检索方式与预估条数。返回 01_theme_and_innovation.md 的全文。`,
  { label: 'synthesize', phase: 'Synthesize', effort: 'max' })
return { ranking, theme: synth }
