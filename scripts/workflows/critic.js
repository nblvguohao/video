export const meta = {
  name: 'quanyin-critic',
  description: 'Completeness critic over evidence/: finds the most important gaps for the paper and writes 12_critic_round1.md',
  phases: [{ title: 'Critic' }],
}
const EV = '/home/user/video/evidence'
const ENV_NOTE = `工具约束：容器内 WebFetch/curl 对几乎所有站点被拦截（github.com 除外）；WebSearch 可用且带页面摘要；学术 MCP（Consensus、Scholar Gateway、Elicit、PubMed、Undermind、Amass）可用（用 ToolSearch 加载）。严禁编造。`
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
