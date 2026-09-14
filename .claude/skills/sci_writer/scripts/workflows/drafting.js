export const meta = {
  name: 'drafting',
  description: 'Draft manuscript sections in parallel under section contracts and the target-journal format spec; integrate into manuscript_v1.md; build the reference list',
  phases: [{ title: 'Draft' }, { title: 'Integrate' }, { title: 'References' }],
}
const ROOT = (args && args.root) || '/ABSOLUTE/PATH/TO/YOUR/PROJECT' // set via Workflow({args:{root: ...}}) or edit this default before running
const MS = ROOT + '/manuscript'
const STYLE = `写作规范（Nature 系刊风格 + 目标期刊格式）：
- 先立论点：每段首句为主张句，随后证据（数字+图表/引用），末句给边界或含义；不写空泛过渡句。
- 主张不得超出证据：results_notes 中标注"不能支持"的说法不得出现；用 "suggests/indicates/is consistent with" 等与证据强度匹配的措辞；单一企业案例的一般性要在 Discussion 明确界定。
- 数字与图表：正文中的每个数字必须能在 manuscript/tables/ 或 results_notes 或 evidence/00_INDEX.md 找到出处；图表编号连续，正文首次提及顺序与编号一致。
- 引用：文内引用格式按 plan/04_format_spec.md；只引用 evidence/06、07、08 文献扫描或本轮用学术工具核实过的文献（给完整引文与 DOI），写在段落末尾的 [REF: 作者 年份 DOI] 标记中，由整合阶段统一编号。
- 语言：英文，简洁（平均句长 ≤ 25 词），避免 AI 腔（不用 "delve", "landscape", "underscore", "pivotal", "in the realm of" 等），不使用破折号堆砌，术语首次出现给定义（如 seed–grain integration, ratoon rice）。
- 企业名称统一为 "Winall Hi-tech Seed Co., Ltd. (hereafter Winall)"，品种名用汉语拼音 + 中文括注一次（e.g., Quanliangyou 6019 (荃两优6019)）。
- 客观性：负面证据（如订单粮食业务负毛利、媒体质疑、杂交稻面积下降）必须如实呈现；不得出现营销式表述。`
const SCHEMA = { type: 'object', properties: { section: { type: 'string' }, file: { type: 'string' }, words: { type: 'number' }, refs_used: { type: 'array', items: { type: 'string' } }, figures_cited: { type: 'array', items: { type: 'string' } }, unsupported_claims_removed: { type: 'array', items: { type: 'string' } } }, required: ['section', 'file', 'words', 'refs_used', 'figures_cited', 'unsupported_claims_removed'] }
const SECTIONS = (args && args.sections) || [
  { id: 'intro', name: 'Introduction', hint: '背景→缺口→本文问题与贡献（3 段到 5 段），末段明确研究问题与创新点，引用 15–25 篇' },
  { id: 'methods', name: 'Materials and Methods', hint: '案例背景与数据来源（公开披露、审定公告、文献），变量定义与单位，样本与时间范围，统计方法与稳健性，数据可用性；可复现' },
  { id: 'results', name: 'Results', hint: '严格按 results_notes 与图表；每个小节对应一个研究问题；只陈述结果不做过度解释' },
  { id: 'discussion', name: 'Discussion and Conclusions', hint: '与文献对话（相同/不同/为什么）、机制解释、政策与产业含义、局限（单案例、公开数据、内生性）、结论段' },
  { id: 'front', name: 'Title, Abstract, Keywords, Highlights', hint: '按期刊格式：标题≤期刊上限，摘要字数与结构按规范，关键词数按规范，Highlights（若期刊要求）每条≤85 字符' },
]
phase('Draft')
const drafts = await parallel(SECTIONS.map(s => () =>
  agent(`你是论文撰写者，负责 ${s.name}。${STYLE}\n\n必读：${ROOT}/plan/01_theme_and_innovation.md、${ROOT}/plan/02_research_route.md（论证地图与本节契约）、${ROOT}/plan/04_format_spec.md、${MS}/results_notes_*.md、${MS}/tables/*.md、${ROOT}/evidence/00_INDEX.md；按需读 evidence/06、07、08 文献文件与其他证据文件。\n要点：${s.hint}\n\n把本节写入 ${MS}/sections/${s.id}.md（英文；图表以 "Fig. X"/"Table X" 引用；引用用 [REF: …] 标记）。返回结构化结果，包括你因证据不足而删除的说法。`,
    { label: `draft:${s.id}`, phase: 'Draft', schema: SCHEMA, effort: 'high' })
))
phase('Integrate')
const integ = await agent(`你是整合编辑。${STYLE}\n\n把 ${MS}/sections/ 下各节按期刊要求的顺序（读 ${ROOT}/plan/04_format_spec.md）合并为 ${MS}/manuscript_v1.md：统一标题层级、图表编号与首次提及顺序、术语与缩写（首次定义）、公司/品种命名、数字格式（千分位、小数位、单位）；把所有 [REF: …] 标记收集为去重的文献清单（${MS}/references_raw.md，每条含作者、年份、题名、期刊、卷期页、DOI、在文中出现的位置），并在正文中暂以 [n] 或 (Author, year) 形式（按格式规范）替换；生成图表清单 ${MS}/figure_table_list.md（编号、标题、文件、正文首次引用位置）；写 ${MS}/integration_log.md 记录改动与发现的不一致（如数字冲突）。返回 manuscript_v1.md 的字数统计与不一致清单。`,
  { label: 'integrate', phase: 'Integrate', effort: 'high' })
phase('References')
const refs = await agent(`你是参考文献编辑。读取 ${MS}/references_raw.md 与 ${ROOT}/plan/04_format_spec.md。对每条文献：用学术工具（mcp__Undermind__lookup_papers_by_metadata / mcp__Undermind__search_papers / mcp__Scholar_Gateway__semanticSearch / mcp__PubMed__search_articles / mcp__Amass_Connector__search_amass_biomedcore_records（Consensus 与 Elicit 不可用），用 ToolSearch 加载；WebSearch 兜底）核实作者、年份、题名、期刊、卷期页、DOI；标记 Verified / Check / Needs fix / Unverifiable；无法核实的文献从正文中移除引用并在日志说明。按期刊格式生成 ${MS}/references_formatted.md，并把它作为 References 节替换进 ${MS}/manuscript_v1.md（保持正文引用与文献列表一一对应、编号连续或作者-年份排序正确）。写 ${MS}/reference_verification_v1.md（统计与逐条状态）。返回统计摘要。`,
  { label: 'references', phase: 'References', effort: 'high' })
return { drafts: drafts.filter(Boolean).map(d => ({ s: d.section, words: d.words })), integration: (integ || '').slice(0, 4000), refs: (refs || '').slice(0, 4000) }
