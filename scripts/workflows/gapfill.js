export const meta = {
  name: 'quanyin-gapfill',
  description: 'Fill evidence gaps named in args.gaps by targeted searching; append to evidence files',
  phases: [{ title: 'GapFill' }],
}
const EV = '/home/user/video/evidence'
const ENV_NOTE = `
环境与工具约束（必须遵守）：
- 容器内 curl/WebFetch 对几乎所有站点被代理拦截（github.com 除外），不要浪费调用。
- WebSearch 可用且结果自带页面内容摘要——中文新闻/公告/年报数字的唯一渠道；请用大量具体查询。
- 学术 MCP：mcp__Consensus__search、mcp__Scholar_Gateway__semanticSearch、mcp__Elicit__search_papers、mcp__PubMed__*、mcp__Undermind__*（先 get_orientation）、mcp__Amass_Connector__*、mcp__Hugging_Face__hf_fs；用 ToolSearch 按名加载。
- 严禁编造。每条事实附来源 URL、日期、检索词、置信度（高/中/低）。文献给完整引文与 DOI。`
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
