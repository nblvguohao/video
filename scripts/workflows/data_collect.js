export const meta = {
  name: 'quanyin-data-collect',
  description: 'Collect the datasets named in args.tasks (each a chunk of variety-level / year-level records) via WebSearch and literature tools; write CSV chunks; then a merger validates and consolidates',
  phases: [{ title: 'Collect' }, { title: 'Merge' }],
}
const ROOT = '/home/user/video'
const DATA = ROOT + '/evidence/data'
const ENV_NOTE = `
环境与工具约束（必须遵守）：
- 容器内 curl/WebFetch 对几乎所有站点被代理拦截（github.com 除外），不要浪费调用。
- WebSearch 可用且结果自带页面内容摘要——请用非常具体的查询（品种名 + 审定编号 + "区试" + "亩产" + "米质" + "稻瘟病"），一个品种拿不到就换 2–3 种措辞（如加 "国审稻" "审定公告" "品种简介" "特征特性"）。
- 学术 MCP（Consensus、Scholar Gateway、Elicit、PubMed、Undermind、Amass；用 ToolSearch 加载）可用于从已发表论文中取数。
- 严禁编造或"合理估计"任何数值。拿不到的字段留空（不要填 0 或平均值），并在 note 列写明尝试过的检索词。每条记录必须有 source_url（可多个，用 | 分隔）与 confidence（high/medium/low）。
- 数值统一单位：产量 kg/亩（若来源为 kg/hm² 请换算并在 note 注明），生育期 天，增产 %。
- 用 Python (pandas) 或 Bash 把结果写成 UTF-8 CSV（表头固定为任务给定的列名），不要用 Excel。`
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
