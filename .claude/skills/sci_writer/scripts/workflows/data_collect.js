export const meta = {
  name: 'data-collect',
  description: 'Collect the datasets named in args.tasks (each a chunk of variety-level / year-level records) via WebSearch and literature tools; write CSV chunks; then a merger validates and consolidates',
  phases: [{ title: 'Collect' }, { title: 'Merge' }],
}
const ROOT = (args && args.root) || '/ABSOLUTE/PATH/TO/YOUR/PROJECT' // set via Workflow({args:{root: ...}}) or edit this default before running
const DATA = ROOT + '/evidence/data'
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
  properties: { task_id: { type: 'string' }, file: { type: 'string' }, n_records: { type: 'number' }, n_complete: { type: 'number' }, field_coverage: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } },
  required: ['task_id', 'file', 'n_records', 'n_complete', 'field_coverage', 'problems'],
}
const tasks = (args && args.tasks) || []
const part = (args && args.part) || 'p'
phase('Collect')
log(`Part ${part}: ${tasks.length} collection tasks`)
const res = await parallel(tasks.map(t => () =>
  agent(`你是数据采集员。${ENV_NOTE}\n\n先读 ${ROOT}/plan/02_research_route.md 中的变量定义表以理解字段含义。\n\n任务 ${t.id}：${t.instructions}\n目标文件：${DATA}/${t.output_csv}\n固定列名：${t.columns}\n${t.items ? '待采集条目：' + JSON.stringify(t.items) : ''}\n\n完成后返回：task_id、file、n_records、n_complete（关键字段齐全的记录数）、field_coverage（每个字段的非空比例）、problems。`,
    { label: `collect:${t.id}`, phase: 'Collect', schema: SCHEMA })
))
const ok = res.filter(Boolean)
phase('Merge')
const merge = await agent(`你是数据管理员。用 Python/pandas 读取 ${DATA}/ 下本轮产生的 CSV 分块（${ok.map(r => r.file).join(', ')}），执行：(1) 去重（同一品种/年份保留信息最全且 confidence 最高者）；(2) 字段类型与单位检查（产量、生育期、增产%为数值；单位换算异常值标记）；(3) 合并为 ${DATA}/${(args && args.merged_csv) || 'merged_' + part + '.csv'}；(4) 生成 ${DATA}/${(args && args.merged_csv) || 'merged_' + part + '.csv'}.report.md：记录数、字段覆盖率、confidence 分布、异常值清单、缺失最多的字段及建议补采清单（品种名列表）。不要修改任何原始数值；不要填补缺失。返回报告全文。`,
  { label: `merge:${part}`, phase: 'Merge', effort: 'medium' })
return { part, tasks: ok, merge_report: (merge || '').slice(0, 6000) }
