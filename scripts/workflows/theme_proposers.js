export const meta = {
  name: 'quanyin-theme-proposers',
  description: 'Independent proposers each draft a paper theme + innovation + data/method plan from the evidence base (angles in args.angles)',
  phases: [{ title: 'Propose' }],
}
const ROOT = '/home/user/video'
const EV = ROOT + '/evidence'
const PL = ROOT + '/plan/proposals'
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
  properties: {
    id: { type: 'string' },
    title_en: { type: 'string' },
    title_zh: { type: 'string' },
    research_questions: { type: 'array', items: { type: 'string' } },
    innovation: { type: 'string' },
    data_plan: { type: 'string' },
    methods: { type: 'string' },
    expected_figures_tables: { type: 'array', items: { type: 'string' } },
    target_journals: { type: 'array', items: { type: 'string' } },
    feasibility_1to10: { type: 'number' },
    novelty_1to10: { type: 'number' },
    main_risks: { type: 'array', items: { type: 'string' } },
    file: { type: 'string' },
  },
  required: ['id', 'title_en', 'title_zh', 'research_questions', 'innovation', 'data_plan', 'methods', 'expected_figures_tables', 'target_journals', 'feasibility_1to10', 'novelty_1to10', 'main_risks', 'file'],
}
const angles = (args && args.angles) || []
phase('Propose')
const props = await parallel(angles.map(a => () =>
  agent(`你是一位有丰富中科院 2 区农林科学期刊发表经验的研究者，负责从"${a.angle}"角度独立提出一个论文方案。${ENV_NOTE}

先读 ${EV}/00_INDEX.md，再按需精读 ${EV}/ 中相关文件（尤其 09_data_feasibility.md、02_varieties.md、01_company_financials.md、04_business_model.md、06/07 文献扫描、10_journal_prescan.md）。
硬约束：
1. 论文以荃银高科为主线（案例/数据核心），但必须回答一个具有一般意义的科学或产业问题（可推广到中国种业/杂交稻体系）。
2. 必须是研究型论文（有数据、有分析），不是纯综述或评论；所有数据必须来自证据库中已确认可获得的公开来源（品种审定公告、年报、统计年鉴、已发表文献），不得设想我们无法获得的田间试验或问卷。
3. 方法必须能在无法直接下载数据库的环境下实施（数据靠 WebSearch 摘要逐条获取 + 文献数据），并写明所需检索工作量（条目数）。
4. 目标期刊必须是 2025 中科院分区农林科学 2 区（可含小类），并说明该刊近年发表过的同类论文 2–3 篇作为"可发表性证据"。
5. 创新点要明确：新框架/新指标/新数据集/新发现，各用一句话说清"与已有文献相比新在哪里"，并引用 2–3 篇最接近的已有文献说明差异。
6. 诚实评估风险：数据缺口、审稿人可能的质疑（如"单一企业案例的一般性"）、以及应对策略。

把方案写入 ${PL}/proposal_${a.id}.md（中文为主，标题与摘要用英文），包含：题目（英/中）、摘要（英文 250 词）、研究问题、创新点、数据方案（变量、来源、样本量、获取方式）、方法（统计模型/指标）、预期图表清单（≥6）、论文结构、目标期刊（首选+备选）、可行性与新颖性自评分（1–10）、风险与对策。`,
    { label: `propose:${a.id}`, phase: 'Propose', schema: SCHEMA, effort: 'high' })
))
return { proposals: props.filter(Boolean) }
