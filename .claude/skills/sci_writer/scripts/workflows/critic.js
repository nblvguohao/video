export const meta = {
  name: 'critic',
  description: 'Completeness critic over evidence/: finds the most important gaps for the paper and writes 12_critic_round1.md',
  phases: [{ title: 'Critic' }],
}
const EV = '/home/user/video/evidence'
const ENV_NOTE = `
工具与环境约束（必须遵守）：
- 容器内 curl/WebFetch 对几乎所有站点被代理拦截；但 github.com 可访问：可用 "git clone --depth 1" 克隆公开仓库、用 WebFetch 读 raw.githubusercontent.com 文件（已有年报文本仓库 IamBusy/audit、品种审定汇编 he-zhui/Rice_QA 等先例）。
- WebSearch 可用且结果自带页面摘要，但每个代理会话有配额（约 200 次，且可能提前耗尽）：先列出最有价值的查询再执行，措辞具体（主体+年份+指标），避免重复。
- 学术工具：mcp__Consensus__search 本月配额已耗尽、mcp__Elicit__* 无 API 权限——不要调用。可用：mcp__Undermind__*（先 get_orientation；search_papers / launch_deep_search / lookup_papers_by_metadata / read_pdfs 读开放获取 PDF）、mcp__Scholar_Gateway__semanticSearch（返回长文本，用 grep/Read 分块）、mcp__PubMed__*、mcp__Amass_Connector__search_amass_biomedcore_records、mcp__bioRxiv__*、mcp__Hugging_Face__hf_fs。用 ToolSearch 按名加载后调用。
- 严禁编造任何数字、品种名、项目名、文献。找不到就写"未找到/未确认"。每条事实附来源 URL、日期、检索词、置信度（高=原文数字直接出现；中=工具综合表述；低=推断）。文献给完整引文与 DOI。
- 输出用 UTF-8 写入指定路径（Bash heredoc / python / Write）。
`
const CRITIC = {
  type: 'object',
  properties: {
    gaps: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, why_needed: { type: 'string' }, search_plan: { type: 'string' }, target_file: { type: 'string' } }, required: ['title', 'why_needed', 'search_plan', 'target_file'] } },
    overall_assessment: { type: 'string' },
    contradictions: { type: 'array', items: { type: 'string' } },
  },
  required: ['gaps', 'overall_assessment', 'contradictions'],
}
phase('Critic')
const critic = await agent(`你是"完整性批评者"。${ENV_NOTE}\n\n通读 ${EV}/ 下所有 .md 与 .csv 文件（用 Bash: ls -la ${EV}; 逐个 cat，大文件分段）。目标论文：以荃银高科为主线、可投中科院农林科学 2 区期刊的研究型论文（候选主题：企业主导的杂交稻育种管线的品种级演变 + 种粮一体化/订单农业的产业链耦合，含定量分析；也可能是再生稻品种适宜性或种业政策/治理主题——不要预设）。\n请找出：(1) 缺失的关键事实/数据（尤其是能支撑定量分析的品种级、年度级数据）；(2) 证据薄弱或相互矛盾之处（列入 contradictions）；(3) 文献覆盖的空白（方法学范本、理论框架、同类企业案例）；(4) 未查的来源类型（交易所问询函、投资者关系记录表、券商深度报告、政府项目立项公示、专利/品种权数据库、全国农技中心品种推广数据）。输出最多 ${(args && args.max_gaps) || 8} 个最重要的 gap，每个给出可执行的检索计划（具体检索词）和目标文件名（沿用现有编号文件或新建 13_gapfill_<主题>.md）。把评估同时写入 ${EV}/12_critic_round1.md。`,
  { label: 'critic:round1', phase: 'Critic', schema: CRITIC, effort: 'high' })
return critic
