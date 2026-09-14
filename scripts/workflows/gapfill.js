export const meta = {
  name: 'quanyin-gapfill',
  description: 'Fill evidence gaps named in args.gaps by targeted searching; append to evidence files',
  phases: [{ title: 'GapFill' }],
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
const SCHEMA = {
  type: 'object',
  properties: { file: { type: 'string' }, n_queries: { type: 'number' }, n_sources: { type: 'number' }, key_facts: { type: 'array', items: { type: 'string' } }, still_missing: { type: 'array', items: { type: 'string' } } },
  required: ['file', 'n_queries', 'n_sources', 'key_facts', 'still_missing'],
}
const gaps = (args && args.gaps) || []
phase('GapFill')
log(`Gap-fill: ${gaps.length} gaps`)
const filled = await parallel(gaps.map((g, i) => () =>
  agent(`你是补漏检索员。${ENV_NOTE}\n\nGap：${g.title}\n为什么需要：${g.why_needed}\n检索计划：${g.search_plan}\n\n执行至少 12 次针对性检索，把找到的内容写入 ${EV}/${(g.target_file || ('13_gapfill_' + (i + 1) + '.md')).split('/').pop()}：若文件已存在，用 Bash 的 cat >> 在文末追加一节 "## 补漏轮：${g.title}"（不要覆盖原有内容）；若不存在则新建。`,
    { label: `gapfill:${(g.title || '').slice(0, 30)}`, phase: 'GapFill', schema: SCHEMA })
))
return { filled: filled.filter(Boolean) }
