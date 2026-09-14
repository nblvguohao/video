export const meta = {
  name: 'quanyin-evidence-sweep-part',
  description: 'Parameterized evidence sweep on Winall Hi-tech (荃银高科): runs the dimensions named in args.dims, writes evidence/*.md, then adversarially verifies decision-critical facts',
  phases: [
    { title: 'Sweep', detail: 'evidence dimensions from args.dims' },
    { title: 'Verify', detail: 'skeptic re-check of top facts' },
  ],
}

const ROOT = '/home/user/video'
const EV = ROOT + '/evidence'

const ENV_NOTE = `
工具与环境约束（必须遵守）：
- 容器内 curl/WebFetch 对几乎所有站点被代理拦截；但 github.com 可访问：可 `git clone --depth 1` 公开仓库、WebFetch raw.githubusercontent.com 文件（已有年报文本仓库 IamBusy/audit、品种审定汇编 he-zhui/Rice_QA 等先例）。
- WebSearch 可用且结果自带页面摘要，但每个代理会话有配额（约 200 次，且可能提前耗尽）：先列出最有价值的查询再执行，措辞具体（主体+年份+指标），避免重复。
- 学术工具：mcp__Consensus__search 本月配额已耗尽、mcp__Elicit__* 无 API 权限——不要调用。可用：mcp__Undermind__*（先 get_orientation；search_papers / launch_deep_search / lookup_papers_by_metadata / read_pdfs 读开放获取 PDF）、mcp__Scholar_Gateway__semanticSearch（返回长文本，用 grep/Read 分块）、mcp__PubMed__*、mcp__Amass_Connector__search_amass_biomedcore_records、mcp__bioRxiv__*、mcp__Hugging_Face__hf_fs。用 ToolSearch 按名加载后调用。
- 严禁编造任何数字、品种名、项目名、文献。找不到就写"未找到/未确认"。每条事实附来源 URL、日期、检索词、置信度（高=原文数字直接出现；中=工具综合表述；低=推断）。文献给完整引文与 DOI。
- 输出用 UTF-8 写入指定路径（Bash heredoc / python / Write）。
`

const SWEEP_SCHEMA = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    n_queries: { type: 'number' },
    n_sources: { type: 'number' },
    key_facts: { type: 'array', items: { type: 'string' }, description: '10-25 most decision-relevant facts, each with number + source URL' },
    gaps: { type: 'array', items: { type: 'string' } },
  },
  required: ['file', 'n_queries', 'n_sources', 'key_facts', 'gaps'],
}

const ALL_DIMS = {
  financials: { file: '01_company_financials.md', verify: true, prompt: `维度1：荃银高科（安徽荃银高科种业股份有限公司，300087，英文 Winall Hi-tech Seed）2015–2026 年公司披露数据的时间序列。
目标：为论文构建一张"公司层面面板表"。逐年（至少 2018–2025 每年 + 2026 中报/一季报）检索并记录：营业收入、归母净利润、分产品收入与毛利率（水稻种子、玉米种子、小麦种子、其他种子、订单粮食/农产品贸易、其他）、种子销量（万公斤/亿公斤）、推广面积（万亩）、研发投入金额与占种子收入比例、研发人员数、审定品种数（国审/省审，水稻/玉米/小麦）、植物新品种权授权数、库存/存货、应收账款、海外收入、员工数、子公司数。来源优先：年报/半年报/季报摘要（cninfo/szse 在搜索结果中的摘要）、券商研报（东亚前海、华安、国信、太平洋等）、财经媒体（界面、财新、证券时报、每经、东方财富、同花顺、雪球）。
输出：evidence/01_company_financials.md，包含一张 Markdown 长表（年份为行、指标为列），每个单元格后括注来源编号；文末给来源清单。同时把面板表写成 evidence/company_panel.csv（year 为行，指标为列，缺失留空）。` },
  varieties: { file: '02_varieties.md', verify: true, prompt: `维度2：荃银高科及控股子公司的品种组合与育种成果（重点：杂交水稻；兼顾玉米、小麦、转基因/生物育种）。
目标：(a) 逐年（2010–2025）国审/省审品种数量；(b) 尽可能完整的国审杂交稻品种名单（系列：荃优、荃两优、徽两优、新两优、丰两优、两优、荃丰优、荃早优、荃晶优、荃9优、荃优华占、荃优822、荃优丝苗、荃两优 6019、荃两优 1606、荃两优 851、荃优 1606 等——请以检索结果为准，不要猜），含审定编号、审定年份、适宜区域、类型（三系/两系、籼/粳、早/中/晚）；(c) 入选农业农村部超级稻的品种及年份（如 新两优 6 号、荃优 822、荃两优 6019 …以检索为准）；(d) 推广面积/年销量领先品种（全国农技中心"推广面积前 10 / 超 10 万亩品种"、中国种业大数据平台）；(e) 再生稻专用/适宜品种（荃优 822、荃两优 851 等是否被各省列为再生稻推荐品种）；(f) 机械化直播/轻简化适宜品种；(g) "谷草兼用"脆秆水稻（种粮饲一体化）技术与品种；(h) 转基因/生物育种玉米进展（是否有转基因玉米品种审定、与先正达/中种的合作、性状来源）；(i) 玉米、小麦主要品种；(j) 品种权、专利数量。
特别任务：对至少 10 个荃银杂交稻国审品种，检索其审定公告中的区试数据（两年区试平均亩产、比对照增产 %、生育期、米质等级、稻瘟病综合指数/抗性、白叶枯病、耐热/耐冷等），并记录字段获取成功率——这是后续"品种层面数据集"可行性的关键。
输出：evidence/02_varieties.md，附 Markdown 表格；并把品种级数据同时写成 evidence/varieties_probe.csv（列：variety,approval_no,year,type,region,yield_kg_per_mu,yield_gain_pct,duration_d,quality_grade,blast_index,super_rice,ratoon_recommended,source_url,confidence）。` },
  rd_projects: { file: '03_rd_projects.md', verify: true, prompt: `维度3：荃银高科的研发体系、承担/参与/申报的科研项目与合作网络（重点 2020–2026）。
检索并记录：荃银农业科学院及各研究所；国家企业技术中心、农业农村部杂交稻新品种创制重点实验室、安徽省重点实验室/工程研究中心/院士工作站/博士后工作站；承担或参与的国家重点研发计划项目/课题（如"主要农作物生物育种""再生稻""水稻高产优质""种业自主创新"等专项，项目编号、牵头单位、年份、经费如有）；国家/安徽省种业振兴项目、"揭榜挂帅"、生物育种产业化试点、国家水稻产业技术体系岗位/综合试验站；与中国水稻研究所、中国农科院作科所、华中农大、安徽农大、安徽省农科院、万建民/谢华安/张启发/李家洋 等院士团队的合作及联合实验室；2025 年安徽省再生稻品种选育与生产技术研讨会的背景、参会院士、结论；国家/省部级科技奖励（国家科技进步奖、安徽省科技进步奖、神农奖等）；主要学术论文/专利成果（如公司科研人员发表的论文）；2025–2026 年新申报或立项的项目、参与的标准制定；海外研发基地。
输出：evidence/03_rd_projects.md，以时间线 + 项目表形式呈现。` },
  business_model: { file: '04_business_model.md', verify: true, prompt: `维度4：荃银高科的商业模式演化，特别是"种粮一体化"/订单农业/全产业链模式，以及其争议。
检索并记录：订单农业的起点、模式描述（"品种+品牌+资本"、"荃银高科+科技企业+产业合作伙伴+金融伙伴"、与光大银行的种粮一体化农业产业互联网平台、数字化平台）；订单粮食业务逐年收入、占比、毛利率（2019–2026H1，如 2025H1 订单粮食收入 6.43 亿、占比 44.54%、毛利率 -0.09% 等，请核实）；订单面积、品种（专用小麦、优质稻、青贮玉米、脆秆稻）、合作方（粮食加工企业、养殖企业、地方政府、合作社）、涉及省份；"谷草兼用"脆秆水稻种粮饲一体化技术（农业农村部 2024 年农业"火花技术"）；界面新闻 2026-02-28《"种粮一体化"外衣下的资本疑云》及公司回应/交易所问询函（如有）；分析师对该模式的评价；海外业务（东南亚、南亚、非洲的种子出口/合资公司、安徽荃银海外基地）；种子营销渠道与"荃银"品牌；产品结构调整（2026 年经营计划）。
同时检索同行对照：隆平高科、垦丰种业、中种集团、大北农、登海种业是否有类似订单农业/种粮一体化模式及其规模，便于论文做企业对比。
输出：evidence/04_business_model.md。` },
  industry_policy: { file: '05_industry_policy.md', verify: true, prompt: `维度5：产业与政策背景 + 股权/治理变化。
(A) 中国种子集团（先正达集团）对荃银高科的要约收购（2025-11 至 2026-01）：背景、要约价、比例（最高 40.51%？请核实）、完成结果、持股比例变化、同业竞争解决承诺、先正达拟注入种子业务的传闻与进展（2025-08 及之后）、中化/先正达 2016 年以来入股历程（中化现代农业→中种集团）。
(B) 政策：2021 种业振兴行动方案、2022 新《种子法》（实质性派生品种制度）、2024–2026 中央一号文件涉种内容、生物育种产业化（2023–2026 转基因玉米大豆品种审定与推广省份/面积）、国家南繁硅谷、种业企业扶优行动（国家种业阵型企业名单：荃银是否入选补短板/破难题/强优势阵型）、品种审定绿色通道/联合体试验。
(C) 行业数据：全国杂交水稻种植面积与种子需求量趋势（2015–2025）、杂交稻种子制种面积与产量、种子库存、种子价格"内卷"、水稻直播/机插比例、再生稻面积（全国及湖北/湖南/安徽/四川/福建）、优质稻比例、超级稻认定数量；种业企业集中度（CR10）、前十强企业名单与收入。
(D) 竞争对手同期关键数字：隆平高科、垦丰、登海、大北农、丰乐、神农科技 2024/2025 营收、种子销量、研发投入。
输出：evidence/05_industry_policy.md。` },
  lit_breeding: { file: '06_lit_breeding.md', verify: false, prompt: `维度6：学术文献扫描 A——育种与农艺（英文为主，兼顾中文）。
主题：(1) 基于品种审定/区试数据分析中国杂交稻遗传增益、产量-品质-抗性演变趋势的论文（方法学范本，如 Rice Science 2026 "Three-Line Hybrid Rice in China: Sustained Improvements…"、Field Crops Research/Crop Journal/JIA 上的 genetic gain 研究）；(2) 企业选育杂交稻品种的表现评价；(3) 再生稻（ratoon rice）农艺、品种适宜性、产量稳定性、经济效益、温室气体等（FCR、Agronomy for Sustainable Development、Frontiers in Plant Science、Rice Science、JIA 近 5 年）；(4) 机械化直播/机插对杂交稻品种选择的影响（Huang M. 等）；(5) 优质稻与稻米品质育种趋势；(6) 谷草兼用/脆秆水稻（brittle culm rice for forage）；(7) 超级稻计划回顾；(8) 稻瘟病抗性基因导入与广谱抗性；(9) 杂交稻制种机械化与第三代技术；(10) 转基因玉米在中国的产业化研究。
工具：Consensus、Scholar Gateway（自然语言长问句）、Elicit、Undermind（先 get_orientation，再 launch_deep_search 1–2 个主题，如 "genetic gain analysis of Chinese hybrid rice varieties using regional trial / variety approval data"）。每篇给出完整引文（作者、年份、题名、期刊、卷期页、DOI）与 1–2 句核心发现；至少 40 篇；标注可作为方法学范本的论文。
输出：evidence/06_lit_breeding.md。` },
  lit_seed_industry: { file: '07_lit_seed_industry.md', verify: false, prompt: `维度7：学术文献扫描 B——种业经济、制度与产业组织（英文为主，兼顾中文核心期刊）。
主题：(1) 中国种业企业创新、商业化育种体系（commercial breeding system）、"育繁推一体化"；(2) 种子企业主导的订单农业/contract farming（例：Agribusiness 期刊 "Contract farming led by a seed enterprise and incentives to produce high quality" DOI 10.1002/agr.21823）、纵向一体化、种粮一体化/value chain integration 的理论与实证；(3) 种业政策与制度改革：Seed Law、PVP/EDV、品种审定改革、licensing fees（例 DOI 10.1002/agr.22020）、种业振兴、biotech commercialization 治理（GM Crops & Food 2026）；(4) 跨国并购与国有种业整合（ChemChina–Syngenta、中种集团）、企业集中度；(5) 品种采纳、农户品种选择、杂交稻面积下降的经济解释；(6) 创新系统/产业链视角的农业技术扩散模型；(7) 中国种业企业 R&D 强度与绩效的实证；(8) 农业龙头企业带动小农的效应（CAER、Food Policy、World Development、JIA、Journal of Rural Studies、Agricultural Systems）。
工具：Consensus、Scholar Gateway、Elicit、Undermind deep search（如 "vertical integration of seed enterprises into grain production and contract farming in China"）。至少 40 篇，完整引文，标注期刊及其可能的分区。
输出：evidence/07_lit_seed_industry.md。` },
  lit_quanyin: { file: '08_lit_quanyin_mentions.md', verify: false, prompt: `维度8：学术文献中关于荃银高科/Winall/荃银品种的直接记载。
检索：(1) 英文文献中 "Winall" / "Quanyin" / "Anhui Winall Hi-tech Seed" 作为作者单位、材料来源或案例；(2) 荃银品种在田间试验/农艺研究中的出现：如 Quanyou 822 / 荃优822、Quanliangyou 851/6019/1606、Xinliangyou 6 / 新两优6号、Huiliangyou / 徽两优、Fengliangyou / 丰两优 系列，尤其再生稻（ratoon）试验、直播试验、氮肥试验、品质研究中的产量数据；(3) 中文核心期刊（中国水稻科学、作物学报、杂交水稻、中国稻米、安徽农业科学 等）中荃银品种选育报告（"xx 的选育及栽培技术"）与公司作者论文；(4) 关于荃银高科的案例研究/管理学/经济学论文（企业创新、种粮一体化、并购案例）。
工具：WebSearch（中文，如 "荃优822 再生稻 产量 试验"）、Consensus、Scholar Gateway、Elicit、PubMed、Amass BiomedCore、Undermind find_papers/深搜。每条记录：引文、荃银品种/公司在文中的角色、可提取的数据（产量、品质等）。目标 ≥30 条。
输出：evidence/08_lit_quanyin_mentions.md。` },
  data_feasibility: { file: '09_data_feasibility.md', verify: false, prompt: `维度9：数据可行性探针——论文若要有定量核心，数据从哪来？
请系统测试并记录以下每条渠道的可行性、样例数据和覆盖率估计：
(1) 通过 WebSearch 获取国家品种审定公告（农业农村部公告）中单个品种的区试数据：随机选 8 个荃银国审杂交稻品种（跨 2012、2016、2019、2021、2023、2025 年份）+ 4 个同期其他企业品种，逐一检索"品种名 国审 审定编号 区试 亩产 米质 稻瘟病"，记录每个字段是否能拿到；估算对 200+ 品种做全覆盖的可行性；
(2) 中国水稻数据中心 ricedata.cn、种业大数据平台 seed.agridata.cn 在搜索摘要中是否暴露结构化数据；
(3) Hugging Face 数据集（用 mcp__Hugging_Face__hf_fs search hf://datasets "rice variety China" / "品种审定" / "hybrid rice" 等）；GitHub 上是否有公开的中国水稻品种审定数据集（用 WebSearch "github 国审 水稻 品种 数据集 csv"）；github.com 的 raw 文件可以 WebFetch；
(4) 开放获取论文的补充数据：例如 Rice Science 2026 三系杂交稻 50 年论文、Crop Journal / FCR 的 genetic gain 论文是否有可下载的品种级数据；用 Undermind read_pdfs 或 PubMed/Amass 全文接口读取 OA 论文，评估能否提取表格数据；
(5) 国家统计局/农业农村部公开统计（再生稻面积、杂交稻面积、种子销量）在搜索摘要中的可得性；
(6) 荃银年报中的品种级/区域级披露（分省收入？主要品种销量？）。
最后给出：推荐的"可行数据集方案"（A/B/C 三案），每案的样本量、变量、获取工作量估算（需多少次检索）与风险。
输出：evidence/09_data_feasibility.md + 样例 CSV evidence/probe_samples.csv。` },
  journal_prescan: { file: '10_journal_prescan.md', verify: false, prompt: `维度10：目标期刊预扫描（中科院 2025 年分区表，农林科学大类 2 区）。
用 WebSearch 获取 2025 年（2025-03-20 发布）中科院分区表农林科学大类中 2 区期刊名单（尽可能完整，含小类分区与 Top 标记），并特别核实以下期刊的 2025 大类分区/小类分区/影响因子/年发文量/审稿周期/是否 OA 及 APC：Journal of Integrative Agriculture、Rice Science、The Crop Journal、Field Crops Research、Agricultural Systems、Agronomy for Sustainable Development、European Journal of Agronomy、Plant Production Science、Frontiers of Agricultural Science and Engineering、China Agricultural Economic Review、Food Policy、Agribusiness、Journal of Rural Studies、Agriculture (MDPI)、Agronomy (MDPI)、Plants (MDPI)、Frontiers in Plant Science、Frontiers in Sustainable Food Systems、Journal of the Science of Food and Agriculture、Crop Science、Euphytica、Plant Breeding、Agronomy Journal、Agricultural Economics、Journal of Agricultural Economics、Food and Energy Security、Sustainability、Land、Journal of Agricultural and Food Chemistry、Rice、Molecular Breeding、Plant Cell Reports、Journal of Plant Registrations、Agricultural and Food Economics、International Journal of Agricultural Sustainability、Outlook on Agriculture、Journal of Agricultural Science (Cambridge)、Renewable Agriculture and Food Systems、Agroecology and Sustainable Food Systems。
对每个 2 区候选期刊简要记录：范围（是否接受种业/产业链/政策/案例+定量的论文）、文章类型与字数上限、参考文献格式、投稿系统、近 2 年是否发表过中国种业/杂交稻/再生稻/订单农业相关论文（各给 1–3 篇例文引文）。给出初步推荐前 5 名及理由。
输出：evidence/10_journal_prescan.md。` },
}

const dimKeys = (args && args.dims) || Object.keys(ALL_DIMS)
const partName = (args && args.part) || 'part'
const DIMS = dimKeys.map(k => ({ key: k, ...ALL_DIMS[k] }))

phase('Sweep')
log(`Part ${partName}: sweeping ${DIMS.map(d => d.key).join(', ')}`)
const sweep = await parallel(DIMS.map(d => () =>
  agent(`你是一名严谨的农业科研情报分析员。${ENV_NOTE}\n\n任务：\n${d.prompt}\n\n把完整结果写入 ${EV}/${d.file}（若有 CSV 也写入 ${EV}/）。完成后以结构化对象返回：file、n_queries、n_sources、key_facts（10–25 条，含数字与来源 URL）、gaps（你没找到但论文可能需要的信息）。`,
    { label: `sweep:${d.key}`, phase: 'Sweep', schema: SWEEP_SCHEMA })
))
const sweepOk = sweep.filter(Boolean)
log(`Part ${partName}: sweep done ${sweepOk.length}/${DIMS.length}`)

phase('Verify')
const critical = []
for (let i = 0; i < DIMS.length; i++) {
  const r = sweep[i]
  if (!r || !DIMS[i].verify) continue
  critical.push(...(r.key_facts || []).slice(0, 5).map(f => ({ dimKey: DIMS[i].key, file: DIMS[i].file, fact: f })))
}
log(`Part ${partName}: verifying ${critical.length} facts (1 skeptic each)`)
const VERDICT = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },
    corrected_fact: { type: 'string' },
    evidence_url: { type: 'string' },
    note: { type: 'string' },
  },
  required: ['refuted', 'corrected_fact', 'evidence_url', 'note'],
}
const verified = await pipeline(critical,
  c => agent(`你是持怀疑态度的事实核查员。${ENV_NOTE}\n\n待核查事实（维度 ${c.dimKey}）：\n"${c.fact}"\n\n用至少 3 次不同措辞的 WebSearch 独立核实数字、年份、主体是否准确（优先一手公告/年报摘要，其次独立媒体/研报）。若不确定，默认 refuted=true 并说明。若数字有误，给出 corrected_fact（带来源 URL）。不要改写事实的含义，只核对。`,
      { label: `verify:${c.dimKey}`, phase: 'Verify', schema: VERDICT, effort: 'high' })
    .then(v => ({ ...c, verdict: v }))
)
const verifiedOk = verified.filter(Boolean).filter(v => v.verdict)
const flagged = verifiedOk.filter(v => v.verdict.refuted)
log(`Part ${partName}: ${flagged.length}/${verifiedOk.length} facts flagged`)

if (verifiedOk.length) {
  await agent(`把下面的核查结果写成 ${EV}/11_fact_verification_${partName}.md（UTF-8 Markdown）：表格列：维度、原事实、refuted、corrected_fact、evidence_url、note；末尾汇总"需要修正的条目"。然后用 Bash 在对应 evidence 文件（${EV}/<file>）末尾追加一节 "## 核查提示（自动）"，逐条列出被标记 refuted 的事实与更正（不要删除或改写原文）。\n\n核查结果 JSON：\n${JSON.stringify(verifiedOk, null, 1).slice(0, 60000)}`,
    { label: `write:verification:${partName}`, phase: 'Verify', effort: 'low' })
}

return {
  part: partName,
  dims_ok: sweepOk.map(r => ({ file: r.file, n_queries: r.n_queries, n_sources: r.n_sources, n_gaps: (r.gaps || []).length })),
  gaps: sweepOk.flatMap(r => (r.gaps || []).map(g => ({ file: r.file, gap: g }))),
  checked: verifiedOk.length,
  flagged: flagged.map(f => ({ dim: f.dimKey, fact: f.fact, corrected: f.verdict.corrected_fact, note: f.verdict.note })),
}
