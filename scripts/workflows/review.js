export const meta = {
  name: 'quanyin-review',
  description: 'Pre-submission review: 3 reviewer reports, format compliance, reference verification, number consistency; then revision, final consistency pass, DOCX/PDF build, submission package',
  phases: [{ title: 'Review' }, { title: 'Revise' }, { title: 'Final' }],
}
const ROOT = '/home/user/video'
const MS = ROOT + '/manuscript'
const SUB = ROOT + '/submission'
const REVIEWERS = [
  { id: 'R1', emphasis: '技术严谨性与数据可信度：方法与数据是否支持每个结论；统计报告是否完整；公开数据的偏差与内生性；单案例的一般性' },
  { id: 'R2', emphasis: '原创性与学术贡献：与最接近文献相比新在哪里（可用 Undermind/Scholar Gateway 核实）；框架/指标是否有理论基础；是否像企业宣传' },
  { id: 'R3', emphasis: '可读性与期刊契合：结构、逻辑流、图表质量与自明性、摘要是否反映全文、是否符合目标期刊范围与格式、非专业读者能否理解' },
]
const RSCHEMA = { type: 'object', properties: { id: { type: 'string' }, recommendation: { type: 'string' }, major: { type: 'array', items: { type: 'string' } }, minor: { type: 'array', items: { type: 'string' } }, unsupported_claims: { type: 'array', items: { type: 'string' } }, file: { type: 'string' } }, required: ['id', 'recommendation', 'major', 'minor', 'unsupported_claims', 'file'] }
const CSCHEMA = { type: 'object', properties: { check: { type: 'string' }, issues: { type: 'array', items: { type: 'string' } }, file: { type: 'string' } }, required: ['check', 'issues', 'file'] }
const version = (args && args.version) || 'v1'
phase('Review')
const reviews = await parallel([
  ...REVIEWERS.map(r => () => agent(`你是审稿人 ${r.id}（视角：${r.emphasis}）。只依据稿件与仓库中的证据评审，不得虚构。读 ${MS}/manuscript_${version}.md、${MS}/figure_table_list.md、${ROOT}/figures/ 中的图（用 Read 查看 PNG）、${ROOT}/plan/03_target_journal.md。按以下结构写 ${MS}/review/${r.id}_${version}.md：Overall assessment / Who would be interested and why / Major strengths / Major concerns（编号，具体到章节与句子）/ Technical failings that must be addressed / Assessment against journal criteria / Recommendation。返回结构化结果。`, { label: `review:${r.id}`, phase: 'Review', schema: RSCHEMA, effort: 'high' })),
  () => agent(`你是格式审查员。逐条对照 ${ROOT}/plan/04_format_spec.md 检查 ${MS}/manuscript_${version}.md：标题长度、摘要字数与结构、关键词数、Highlights、章节命名与顺序、图表编号/引用顺序/图题表题格式、单位与数字格式、缩写定义、声明部分（数据可用性、利益冲突、作者贡献、资助、致谢）是否齐全、参考文献格式与文内引用一致性、字数上限。把逐条检查表写入 ${MS}/review/format_check_${version}.md（列：条目、要求、现状、是否合规、修正建议）。返回 issues 列表。`, { label: 'check:format', phase: 'Review', schema: CSCHEMA, effort: 'medium' }),
  () => agent(`你是数字一致性审查员。用 Python/grep 提取 ${MS}/manuscript_${version}.md 中的全部数字型陈述（含摘要、正文、图题表题），逐条与 ${MS}/tables/*.md、${MS}/results_notes_*.md、${ROOT}/evidence/00_INDEX.md、${ROOT}/evidence/data/*.csv 对照（必要时重算）；检查摘要/结论中的数字与结果节一致、同一数字在不同位置一致、图中数据与表一致（读 PNG）。把清单写入 ${MS}/review/number_consistency_${version}.md（列：位置、陈述、出处、是否一致、修正）。返回不一致项。`, { label: 'check:numbers', phase: 'Review', schema: CSCHEMA, effort: 'high' }),
  () => agent(`你是参考文献核验员（多源交叉验证）。读取 ${MS}/manuscript_${version}.md 的 References 节，对每条文献用 ≥2 个独立来源核实（mcp__Undermind__lookup_papers_by_metadata、mcp__Undermind__search_papers、mcp__Scholar_Gateway__semanticSearch、mcp__PubMed__search_articles、mcp__Amass_Connector__search_amass_biomedcore_records、WebSearch（Consensus 与 Elicit 不可用）；用 ToolSearch 加载），逐字段比对作者/年份/题名/期刊/卷期页/DOI，按 🔴 Critical / 🟡 Warning / 🟢 Info 分级，给出 ✅ Verified / ⚠️ Check / ❌ Needs fix / ❓ Unverifiable。并检查：正文每个引用在列表中存在、列表每条在正文被引用、编号/排序符合格式规范。写 ${MS}/review/reference_check_${version}.md（汇总 + 逐条表 + 修正后的条目）。返回问题清单。`, { label: 'check:references', phase: 'Review', schema: CSCHEMA, effort: 'high' }),
])
const ok = reviews.filter(Boolean)
phase('Revise')
const rev = await agent(`你是修订负责人。读取 ${MS}/manuscript_${version}.md 与 ${MS}/review/ 下全部报告（三位审稿人、格式、数字一致性、参考文献核验）。写出 ${MS}/manuscript_v2.md：逐条落实所有 major/minor 意见与三类检查的修正（无法落实的在 ${MS}/review/response_to_reviews.md 中逐点说明理由），不得引入新的未核实数字或文献；删除任何不被证据支持的说法；保持图表编号与引用一致；更新 References。写 ${MS}/review/change_log_v1_to_v2.md（逐条：意见→修改位置→修改内容）。返回修改摘要。`,
  { label: 'revise', phase: 'Revise', effort: 'max' })
phase('Final')
const fin = await parallel([
  () => agent(`你是终审校对。对 ${MS}/manuscript_v2.md 做最终一致性与格式复核（对照 ${ROOT}/plan/04_format_spec.md、${MS}/review/format_check_${version}.md、${MS}/review/number_consistency_${version}.md、${MS}/review/reference_check_${version}.md），确认所有问题已关闭；用 diff 比较 v1 与 v2 确认改动与 change_log 一致、无意外删改（历史版本一致性）；检查英文语言（去 AI 腔、句长、术语一致）。直接修正遗留小问题并记录到 ${MS}/review/final_proof_log.md。然后运行 python3 ${ROOT}/scripts/build_docx.py（若不存在则用 python-docx 编写：读取 manuscript_v2.md 生成 ${SUB}/manuscript.docx，含标题、作者占位、摘要、正文、图（插入 figures/*.png）、表、参考文献，字体 Times New Roman 12pt 双倍行距、行号可选），并用 soffice --headless --convert-to pdf 生成 ${SUB}/manuscript.pdf；用 Read 打开 PDF 抽查排版。返回校对日志摘要。`, { label: 'final:proof+build', phase: 'Final', effort: 'high' }),
  () => agent(`你是投稿包制作者。读 ${ROOT}/plan/03_target_journal.md、${ROOT}/plan/04_format_spec.md、${MS}/manuscript_v2.md。生成：${SUB}/cover_letter.md（致编辑，说明贡献、契合度、无重复投稿、利益冲突声明、建议审稿人栏留空）、${SUB}/highlights.md（若期刊需要）、${SUB}/declarations.md（数据可用性、利益冲突、作者贡献 CRediT 占位、资助占位、致谢占位、AI 工具使用声明）、${SUB}/submission_checklist.md（对照期刊清单逐项打勾，未完成项标注需作者补充的内容：作者信息、单位、ORCID、资助号等）、${SUB}/figure_captions.md 与 ${SUB}/tables.md（按期刊要求单独提供）、${SUB}/VERSION_HISTORY.md（v1→v2 差异摘要、各审查报告索引、git 提交对应关系）。返回文件清单。`, { label: 'final:package', phase: 'Final', effort: 'medium' }),
])
return { reviews: ok.map(r => ({ id: r.id || r.check, n: (r.major || r.issues || []).length })), revise: (rev || '').slice(0, 3000), final: fin.filter(Boolean).map(f => (f || '').slice(0, 1500)) }
