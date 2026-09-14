# 新颖性与理论贡献评审（Judge: Novelty）

> 评审日期：2026-09-14
> 评审角色：负责判断学术新颖性的资深审稿人
> 评审对象：`plan/proposals/proposal_A/B/C/D`
> **本评审的全部占位判断均经本次会话实际检索核实**，工具：Scholar Gateway semanticSearch（4 次）、Undermind search_papers（7 次）+ lookup_papers_by_metadata（1 次，8 篇）+ get_paper_info（4 次，共 17 篇）、WebSearch（5 次）。凡未能核实者已明确标注"未能核实"。
> 检索工作区：`5e132809-6b94-4d11-8477-afba425d64c1`（种业经济与制度）、`385b7dc6-71fd-4119-8804-9617797ede8d`（杂交稻育种）。
> 注：容器网络对出版社与 PKU CCAP 站点的直连被 egress allowlist 拦截（`curl` 返回 `Host not in allowlist`），故全部核实通过检索工具的元数据/摘要完成，未能取得 Xiang et al. 2025 与 Gong et al. 2026 的全文。

---

## 零、执行摘要（先给结论）

| 创新点 | 占位程度 | 一句话判定 |
|---|---|---|
| A-1 链式对照遗传增益分解 | **部分占位（偏严重）** | 「把官方区试产量趋势分解为遗传 / 非遗传两部分」是 Piepho–Laidig–Mackay 一脉的成熟方法学；「对照更替会污染遗传增益估计」已被 Raymond et al. 2023 与 Piepho & Laidig 2024 明确研究过。A 的真实增量只剩"**在只公开均产+具名对照+增产率的中国公告体制下如何恢复等价信息**"这一数据—方法匹配层 |
| A-2 DEA+Malmquist 性状前沿位移 | **确为空白（但属工具移植）** | DEA 用于品种评价有先例（单次试验的选择工具）；跨育种世代的 Malmquist 前沿分解未见先例 |
| A-3 谱系平台作为分析单元 | **部分占位** | Gong 2026 已统计不育系/恢复系；Shi & Hu 2017 已做种质来源份额；把亲本系当作"育种主体"的分析单元确属新用法，但属操作化创新而非理论创新 |
| B-1/D-1/D-2 下游一体化 → 品种性状组合 | **理论已占位，实证确为空白** | 纵向一体化改变产品属性选择在 IO 理论中已是成熟结论（Zanchettin & Mukherjee 2017 IJIO；Liu 2016 IJIO；Chambolle & Guignard 2025）；公私育种目标分化已有证据（Burris et al. 2025）。**但"用实测性状数据度量一体化企业的性状选择"检索不到任何先例** |
| B-3/D-3 增产率作为"约束"而非"目标" | **确为空白** | 未检索到把审定门槛与企业收益函数分离、并在数据上验证"相对增产率零趋势"的文献 |
| C-1 记录级审定试验通道变量 | **确为空白** | Xiang et al. 2025 经核实确为**问卷+许可交易数据+时期处理**，全文无任何通道变量；检索不到任何中英文文献使用过公告原文的"绿色通道/联合体"标注 |
| C-2 测量主体—性状方向不对称 | **逻辑已占位，设计与场景为空白** | 「谁测量决定报什么数」是 Duflo et al. 2013 QJE 的核心结论；但 C 的设计（同一份文书内自测性状与第三方测性状并存）与农业审定场景无先例 |
| C-3 荃银作为反例 | **确为空白** | 无任何同行评议论文以荃优/荃两优系列为研究对象（与 NOVELTY_ALERT §3 一致） |

**最佳方案：C**（total 8.15）。
**真正无可替代的创新点：C 的"记录级审定通道 + 同一文书内自测性状 vs 第三方测定性状"这一对变量。**（理由见第六节）

---

## 一、方案 A 的核心问题核实：链式/滚动对照遗传增益估计是否已有？

### 1.1 核实结论：**部分占位，且占位程度比提案自述严重得多**

提案 A §5 创新点 1 写道：

> "这四篇——也是本领域最权威的四个大样本——报告的全部是'绝对区试产量'或'原始比对照增产率'对年份的趋势，因而把遗传进展、对照更替与试验体系漂移混为一谈。**本文首次把三者分开**"

这句话在"中国水稻文献内部"成立，在"作物科学文献整体"**不成立**。本次检索确认存在一条完整的、被高度引用的方法学脉络，其研究对象正是"官方品种审定/区试系列的产量趋势分解"：

**最接近文献（按接近程度排序，全部经 Undermind `lookup_papers_by_metadata` + `get_paper_info` 核实其存在、期刊、年份、DOI）：**

1. **Piepho, H.-P., Laidig, F., Drobek, T., & Meyer, U. (2014). Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. *Theoretical and Applied Genetics*, 127, 1009–1018. DOI: 10.1007/s00122-014-2275-1**（64 次引用）
   — 标题即"**分解官方品种试验长期产量趋势中的遗传与非遗传来源**"。这就是 A 的 §7.1 第四步三项分解的原型。**A 提案通篇未引用此文**（只引了 Piepho 的 pbr.13240 与 Smith & Cullis），这是评审阶段必须补上的最严重遗漏。

2. **Laidig, F., Piepho, H.-P., Drobek, T., & Meyer, U. (2014). Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. *Theoretical and Applied Genetics*, 127, 2599–2617. DOI: 10.1007/s00122-014-2402-z**
   — 12 个作物、1983–2012 年德国官方 VCU 试验，同时给出遗传趋势、非遗传（农艺）趋势，并与农户实产趋势对比。结论："德国主要作物近 30 年的产量进展**主要来自遗传改良**，农艺因素贡献次要"。**这正是 A 想做的事，只是国家不同、且 A 的结论（只有 51 % 是遗传）与之相反**——这反而是 A 可以打的最好一张牌（见 §1.3 应对）。

3. **Mackay, I., Horwell, A., Garner, J., White, J., McKee, J., & Philpott, H. (2011). Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. *Theoretical and Applied Genetics*, 122, 225–238. DOI: 10.1007/s00122-010-1438-y**（203 次引用）
   — 英国 National List / Recommended List 1948–2007。结论：1982 年以来谷类与油菜的产量提升中 **≥88 % 可归于遗传改良**。

4. **Raymond, J., Mackay, I., Penfield, S., Lovett, A., Philpott, H., & Dorling, S. (2023). Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. *Field Crops Research*, 303, 109086. DOI: 10.1016/j.fcr.2023.109086**
   — **这是对 A 最危险的一篇。** 摘要原文（经 `get_paper_info` 核实）：
   > "Subsets of the winter wheat variety trials dataset were used to replicate shorter breeding cycles **to quantify the impact of the number and choice of long-term check varieties on estimating genetic gain**. … **we observed … a previously unobserved long-term increase in yield as varieties age in treated trials. This shows that yields of long-term check varieties cannot be assumed to be stable over time.** We found that **genetic gain estimates were highly sensitive to the long-term check varieties chosen**, whilst the inclusion of multiple checks decreased the standard error of the estimate."
   — 即：A 的 **R12（对照阶梯值随时间漂移）已被做过并已有明确答案**；A 的 R1（估计对对照选择极度敏感，0.12–0.67 % ∙ yr⁻¹）**恰好复现了 Ray23 已经报告过的性质**，而 A 把它写成自己的"弱点"，Ray23 把它写成自己的"发现"。

5. **Piepho, H.-P., & Laidig, F. (2024). How Many Checks Are Needed per Cycle in a Plant Breeding or Variety Testing Programme? *Plant Breeding*, 144(1). DOI: 10.1111/pbr.13240**
   — 摘要原文：
   > "One important use of checks is **to provide connectivity between years**, which facilitates comparison among genotypes of interest that are tested in different years. When long-term data are available, such comparisons **allow an assessment of realized genetic gain (RGG)**. … it is useful to employ a larger number of checks and **to keep the replacement rate low**."
   — 即："用对照把不同年份的试验**连起来**以估计遗传增益"正是这篇的主题；"**对照更替率**"正是这篇的自变量。A 的"链式对照（chained check）"这一术语是新的，**概念不是**。

6. 佐证性：Seck et al. 2023 *Rice* 16:61（DOI 10.1186/s12284-023-00677-6，29 项水稻遗传增益研究，均值 36.3 kg ha⁻¹ yr⁻¹）— A 已引，用法正确。

### 1.2 是否已有人用**中国品种审定公告**做过同类分解？

**核实结论：未检索到，判定为空白。**
- Undermind 语义检索（中国审定记录 + 主体 + 性状）返回的中国文献全部为省级品种试验的描述性分析（如 [Fen14b] 江西审定品种性状分析、[Jie10b] 北方水稻区试精确度评价），无任何一篇做遗传/非遗传分解。
- WebSearch 中文检索（"中国 品种审定公告 对照品种 更换 遗传增益 高估 区试 产量 趋势 分解"）只返回农业农村部公告与《主要农作物品种审定办法》原文，**其中确认了制度事实**："区域试验、生产试验的对照品种应当是同一生态类型区同期生产上推广应用的已审定品种……**并根据农业生产发展需要及时更换**"。这为 A 的问题设定提供了官方依据，但没有任何学术研究处理它。
- Lu24 / Han24 / Gong26 的摘要（下 §4 逐篇核实）确认三者均为**性状对年份的趋势/年代均值**，无对照校正。

### 1.3 A 的增量还剩多少？

**剩下的是真的，但比提案自述小一个量级：**

| 提案自述的增量 | 核实后的实际增量 |
|---|---|
| "首次把遗传进展、对照更替、试验漂移三者分开" | ❌ 国际上已做 12 年（Pie14/Lai14/Mac10） |
| "从公告文本反解对照产量并链接成阶梯的技巧此前未见" | ✅ **成立**。国际方法学全部要求逐点原始试验数据（Pie14 用 LMM on plot data；Mac10 用 NL/RL 原始试验）；中国公告只给"均产 + 具名对照 + 增产率"。**在这一数据结构下恢复等价信息，确未见先例** |
| "证明这会使遗传增益被高估约一倍" | ✅ **成立且是最有价值的一条**。Lai14/Mac10 的结论是"遗传占 ≥88 %"，A 的结论是"遗传只占 51–59 %"。**这个反差本身才是论文的卖点**，而不是"方法首创" |
| "对照品种阶梯的外部交叉验证闭合于 1 % 以内" | ✅ 成立，是可信度的强证据 |

**A-2（DEA + Malmquist 做性状前沿位移）核实结论：确为空白。**
Undermind 检索确认 DEA 用于品种评价有先例——[Has19] Hashemi et al. 2019, *Journal of Agricultural Science*（冬大麦品种 DEA 评价）、[Kit23] Kittipadakul et al. 2023, *Int. J. Innovation and Learning*（木薯品种 DEA）、[Aht20] Ahtikoski et al. 2020, *Scand. J. For. Res.*（用 DEA 评估林木育种目标），以及 GYT biplot 一脉（[Yan18] Yan & Frégeau-Reid 2018, *Scientific Reports*，214 次引用）——**但均为单次试验/少数基因型的选择工具**。把 DEA + Malmquist 用作**跨育种世代的多性状前沿位移测度**，未检索到先例。另注意 [Dea16] 喻亚平、余利丰 2016《我国农业育种研发效率的实证分析——基于 DEA-Malmquist 指数分析的视角》做的是**育种研发投入产出效率**（机构层），与 A 的"性状前沿"完全不同，但**标题极易被审稿人误认为撞车，必须在正文主动区分**。

**A-3 核实结论：部分占位。** Gong 2026 统计了不育系/恢复系的审定数量（见 §4.3），Shi & Hu 2017（*JIA* 16(10):2337–2345，DOI 10.1016/S2095-3119(16)61615-5，经 `get_paper_info` 核实摘要）追踪 IRRI 16.4 % / 日本 11.2 % 的种质贡献份额——但均未把亲本系作为**比较育种主体性状策略**的分析单元。属操作化创新，成立但分量有限。

---

## 二、方案 C 的核心问题核实：审定通道自我认证不对称

### 2.1 Xiang et al. 2025 的实际内容（核实完成）

**Xiang, C., Yang, R., Wang, X., & Huang, J. (2025). Impact of Seed Regulation Reform on Licensing Fees of Varieties in China. *Agribusiness*. DOI: 10.1002/agr.22020**（2025-01-15 online）

摘要原文关键句（经 Undermind `get_paper_info` full 核实）：
> "This study aims to analyze the impacts of the seed regulation reform on **the licensing fees of varieties** in China based on some **unique actual transaction data of variety licensing**. We employed a **nationwide in-person survey of seed companies** and used a multivariate analysis. … seed regulation reform in China led to an average decline of nearly half of the licensing fee of a variety. After the reform, the licensing prices of **conventional rice** varieties decreased the most, followed by maize varieties. By contrast, **the reform did not significantly affect the licensing fees of hybrid rice varieties**. The reform resulted in a 63% drop in licensing fee of a public-bred variety, while having no significant impact on that of private-bred varieties…"

**判定：Xiang et al. 2025 不构成对 C 的占位，且是 C 最有价值的对话对象。**
- 数据：企业问卷 + 许可交易价格，**不是品种审定记录**；
- 处理：改革前/后的**时期**虚拟变量，**没有任何通道（绿色通道/联合体/统一区试）变量**；
- 结果变量：**许可费**，不是品种的客观属性；
- 更妙的是："**杂交稻品种许可费不受改革显著影响**"——C 的样本正是**籼型杂交稻**。C 可以直接写：Xiang et al. 在价格维度上对杂交稻找不到改革效应，本文在**进入者属性**维度上找到了；两者并不矛盾，而是说明改革的作用发生在"谁进来"而非"多少钱"。这是对该文非常干净的增量。

同时核实 Zhao, Y., Deng, H., Hu, R., & Xiong, C. (2022). Impact of government policies on seed innovation in China. *Agronomy*, 12(4), 917. DOI 10.3390/agronomy12040917 —— C 提案的描述（政策虚拟变量 × 年份的时间序列设定）与 `evidence/07` 的记录一致，未发现与通道变量相关的内容。

### 2.2 是否已有研究比较**同一审批制度内不同认证路径**下的客观产品属性？

**核实结论：在农业/品种审定领域确为空白；在规制经济学领域逻辑已被占位，但设计不同。**

**最接近文献（全部经 Undermind `get_paper_info` 核实）：**

1. **Duflo, E., Greenstone, M., Pande, R., & Ryan, N. (2013). Truth-telling by Third-party Auditors and the Response of Polluting Firms: Experimental Evidence from India. *Quarterly Journal of Economics*, 128(4), 1499–1545. DOI: 10.1093/qje/qjt024**
   — **这是对 C 最危险的一篇，而 C 提案完全没有引用。** 核心结论（经 WebSearch 核实）："the status quo system was largely corrupted, with **auditors systematically reporting plant emissions just below the standard, although true emissions were typically higher**"。即：**"由被监管方选择并付费的测量方会系统性地报出有利数字"这一命题，已经有 QJE 级别的随机实验证据。**
   — **但 Duflo et al. 的设计与 C 不同**：他们对**同一个属性**（排放量）同时拥有审计报告值与独立复测值；C 拥有的是**同一份文书内的两类不同属性**（申请人自测的产量/增产率 vs 第三方测的整精米率/垩白度）。C 的设计更弱（无法直接证明"同一数被两方测出不同值"），但场景全新且可观测量更丰富。

2. **"Certification Intermediaries: Evidence from the Medical Device Industry" (2015). DOI: 10.2139/ssrn.2554984**
   — FDA 允许私营第三方为部分医疗器械准备认证报告的自然实验；结论：该政策导致受影响器械的**不良事件显著增加**，且当认证方与制造商建立长期关系的收益更大时效应更强。
   — **这正是 C 提案创新点 2 所说的"只能观测事后不良事件，无法观测同一批次内不同认证路径下的产品客观属性"——该描述经核实准确。** C 在这一点上的自述是成立的。

3. **Bar, T., & Zheng, Y. (2018). Choosing Certifiers: Evidence from the British Retail Consortium Food Safety Standard. *American Journal of Agricultural Economics*. DOI: 10.1093/ajae/aay024**
   — **这是农经领域最接近的一篇，C 提案未引，必须补。** 摘要："Manufacturers prefer geographically close certifiers and **those that assigned a higher share of A grades in the previous months**. This behavior might provide an incentive for less stringent audits."
   — 与 C 的关系：Bar & Zheng 研究的是**认证方选择的内生性**（厂商挑宽松的认证机构），这恰好就是 C 的 R11 无法排除的自选择解释的农经版本。**C 必须正面引用它，并说明本文的两臂测量主体不对称为什么不能被纯自选择解释**（见 §5 应对）。

4. **Grennan, M., & Town, R. J. (2020). Regulating Innovation with Uncertain Quality: Information, Risk, and Access in Medical Devices. *American Economic Review*, 110(1), 120–161. DOI: 10.3386/w20981**
   — C 已引，用法正确（EU vs US 两个**制度之间**的比较，而非同一制度内的两条路径）。

5. **Renckens, S., & Auld, G. (2020). Time to certify: Explaining varying efficiency of private regulatory audits. *Regulation & Governance*, 14(4). DOI: 10.1111/rego.12362** — C 已引，成立。

6. 补充可引：**Lindeboom, M., van der Klaauw, B., & Vriend, S. (2020). Audit regimes in long-term care. *Journal of Economic Behavior and Organization*, 272–298.**（审计制度设计的田野证据）。

**关于"green channel variety registration China" / "consortium trials seed regulation" 的专门检索：**
- Undermind 语义检索（以 2016 年审定改革 + 绿色通道 + 联合体为 sample_abstract）返回 20 篇，唯一相关的是 **Xia25**（即 Xiang et al. 2025），其余全为省级品种试验的描述性中文文献。
- WebSearch 中文检索（"绿色通道 联合体试验 审定品种 品质 差异 比较 国家统一区试 水稻 整精米率"）只返回**政府文件**：四川农大玉米所《国家级水稻玉米品种审定绿色通道试验指南（试行）》、农业农村部办公厅《关于加强主要农作物品种绿色通道和联合体试验管理工作的通知》（2022-08-31，moa.gov.cn/govpublic/nybzzj1/202208/t20220831_6408232.htm）。**无任何学术研究。**
- **判定：C 的记录级通道变量确为空白，且 2022 年农业农村部的专项整治通知为该问题提供了官方背书的现实重要性。**

---

## 三、方案 B/D 的核心问题核实：下游一体化是否已与品种性状组合直接连接？

### 3.1 核实结论：**理论层面已被充分占位；实证层面（用实测性状数据）确为空白。**

**(a) 理论已占位** —— Undermind 检索"纵向一体化改变上游创新方向与产品属性选择"返回一个成熟的 IO 理论文献群：

- **Zanchettin, P., & Mukherjee, A. (2017). Vertical integration and product differentiation. *International Journal of Industrial Organization*, 54, 25–57. DOI: 10.1016/j.ijindorg.2017.07.004**
- **Liu, X. (2016). Vertical integration and innovation. *International Journal of Industrial Organization*, 47, 88–120. DOI: 10.1016/j.ijindorg.2016.02.002**（45 次引用）
- **Chambolle, C., & Guignard, M. (2025). Buyer Power and the Effect of Vertical Integration on Innovation. SSRN. DOI: 10.2139/ssrn.4341954**
- 另有 Mukherjee & Zanchettin (2007)、Sánchez (2010, endogenous quality choice under upstream market power) 等。

**含义**：B/D 的机制命题"一体化 → 内部化下游品质收益 → 改变产品属性选择"**在理论上不是新的**。B 提案 §5 创新点 3 只对比了 Lambert & Wilson (2003)、Taylor et al. (2005)、Adjemian et al. (2016) 这类**下游向上游一体化**的案例文献，**漏掉了整条 IJIO 理论脉络**。审稿人（尤其 CAER/JIA 的经济学审稿人）几乎必然指出这一点。B 与 D 都必须补引，并把定位改为"**为一个已有理论预测提供首个基于产品客观属性的实证检验**"，而不是"提出一个新机制"。

**(b) 公私育种目标分化已占位** ——
**Burris, L., Nalley, L., De Steur, H., Durand-Morat, A., Tack, J., Yang, W., & Lusk, J. (2025). The divergence of the public and private plant breeding sectors with implications for climate change. *npj Science of Plants*. DOI: 10.1038/s44383-025-00013-5**
摘要核实：**583 位植物科学家（其中 257 位育种家）的问卷**，研究公私育种部门的目标分化。
— D 提案对该文的描述（"用的是问卷中的自述偏好"）**经核实准确**，D 的"显示性偏好 vs 陈述性偏好"区分成立。
— 但注意：**"公私育种主体的目标不同"这一结论本身已由 Bur25 建立**。D 的 H3（科研单位符号完全相反）因此**不是发现，只是复现**；D 必须把 H3 定位为"对 Burris et al. 陈述性结论的显示性验证"，而不是自己的独立贡献。

**(c) 实证空白成立** —— 三次不同措辞的 Undermind 语义检索（下游加工商契约如何改变育种目标；用申请人身份解释审定品种实测性状；纵向边界与产品属性）**均未返回任何一篇把企业纵向边界与品种实测性状数据直接连接的实证研究**。返回的最接近者全部是：
- 合同设计理论（[Goo10] Goodhue, Mohapatra & Rausser 2010, *AJAE* 92(5):1283–1293, Interactions Between Incentive Instruments: Contracts and Quality in Processing Tomatoes；[Yu22b] Yu, Bonroy & Bouamra-Mechemache 2022, *AJAE*；[And19] Anderson & Monjardino 2019, *EJOR*）——**都在"合同如何激励农户交出高品质"这一层，没有一篇上溯到"企业先育出什么品种"**；
- 供应链品质可观测性（[Ken98] Kennett, Rehman & Brooks 1998, *Supply Chain Management* 3(3):157–166，加拿大磨粉小麦的身份保持；[Wil07] Wilson, Dahl & Johnson 2007, *CJAE* 55(3):315–326）——定性案例；
- 品种耐用性与专有性（[Ran00] Rangnekar, D. 2000. *Planned Obsolescence and Plant Breeding: Empirical Evidence from Wheat Breeding in the UK (1965-1995)*；无 DOI，Semantic Scholar: 27190a41a4f18125173f34c349c822bc820163fa）——**这篇值得 B/D 引用**：它论证育种商通过降低品种耐用性（弱化广谱抗病性）来实现收益占有，是"企业收益函数塑造性状选择"最早的实证先例，逻辑与 B/D 同构但方向相反（缩短品种寿命 vs 提升加工品质）。**B/D 都没有引，这是一个可以显著提升论文理论纵深的遗漏。**

### 3.2 B 与 D 之间的关系

B 与 D 是**同一个想法的两个版本**，核心自变量、因变量、数据层、焦点企业完全相同。差别是：
- B 把重心放在"一体化深度排序 + 官方定等奖励什么 + 会计分解"（更像 IO 论文）；
- D 把重心放在"**监管性状 vs 收益性状**的二分 + M4 堆叠单参数 λ = +0.570 SD"（更像机制检验论文）。

**D 的 M4 堆叠设计确实优于 B 的分性状森林图**：它把机制压缩成一个参数，且该参数在剔除绝对产量后仍成立，并通过了合并组安慰剂（p=0.104）。**如果最终不选 C，应当以 D 为骨架、把 B 的 §7.3（官方定等 logit：奖励加工净度而不奖励细长粒型）与 §7.7（会计分解）并入 D 的 Discussion。**两者不应分别投稿。

### 3.3 一个必须指出的内部矛盾

- **B §7.1 实测**：荃银垩白度 **−2.04 pp（p<0.001）**（申请人字段样本 n≈690）
- **D §8.1 实测**：荃银垩白度 **−0.688 pp（p=0.0013）**（谱系规则全层 n≈1,336）
- **D §8.2 样外复制**：一体化同行垩白度 **+0.159 pp（p=0.602，方向相反）**

同一家企业、同一个性状、同一个数据集，两个方案给出相差 3 倍的系数，而机制的旗舰性状在样外复制中方向反转。**这是审稿人最容易抓住的一处**，必须在合并方案时统一口径并给出解释（样本层不同 vs 识别规则不同），否则两篇稿件若先后投出会互相拆台。

---

## 四、共同问题核实：Lu24 / Han(Hang)24 / Gong 2026 的确切内容

三篇**全部存在且已核实**（Undermind `lookup_papers_by_metadata` 全部命中，`get_paper_info` 取得元数据）。

### 4.1 Lu Y. et al. 2024 — **确认存在，内容与提案描述一致**

**Lu, Y., Tang, Y., Zhang, J., Liu, S., Liang, X., Li, M., & Li, R. (2024). Variations and Trends in Rice Quality across Different Types of Approved Varieties in China, 1978–2022. *Agronomy*, 14(6), 1234. DOI: 10.3390/agronomy14061234**（11 次引用）

摘要核实：17,785 个审定品种的**品质性状**，分五类（籼常规/籼杂/粳常规/粳杂/籼粳杂）比较差异与趋势。结论：整精米率普遍上升、垩白度与垩白粒率下降、直链淀粉下降、胶稠度改善。
**与各方案的重叠度**：
- A：**中**。A 的 §7.2 性状趋势部分与之重叠，但 A 的前沿/交换率框架是 Lu24 没有的。A 的应对（"靠框架而非结果取胜"）正确。
- B/D：**低**。Lu24 完全无主体维度。B/D 的自述（"它们解释时间，本文解释主体"）**成立**。
- C：**低**。无制度变量。

### 4.2 Hang S. et al. 2024 — **确认存在；注意作者姓氏是 Hang 不是 Han**

**Hang, S., Wang, Q., Wang, Y., & Xiang, H. (2024). Evolution of Rice Cultivar Performance Across China: A Multi-Dimensional Study on Yield and Agronomic Characteristics over Three Decades. *Agronomy*, 14(12), 2780. DOI: 10.3390/agronomy14122780**（5 次引用）

摘要核实：**11,811 次品种试验，1990–2023**，产量与关键农艺性状（生育期、株高、每穗粒数、千粒重、有效穗、结实率）的时空演变；分省年增幅（江西 1.42 %/yr，吉林 0.16 %，黑龙江 0.45 %）。
**关键核实结果（对 A 极重要）**：Hang24 报告的是**绝对试验产量对年份的百分比趋势**，摘要中**没有任何对照校正的痕迹**。这印证了 A 的批评是真实的——江西 1.42 %/yr 是 A 所说的"表观趋势"量级（A 自己测得长江流域 0.774 %/yr 表观、0.398 %/yr 链式校正后）。**A 应当在正文中把 Hang24 的省级数字作为"未校正估计"的代表逐个列出，这是 A 最有说服力的对话方式。**
- NOVELTY_ALERT 把它写作 "Han24"，**引用时必须改为 Hang（S. Hang）**，否则参考文献会错。

### 4.3 Gong J. et al. 2026 — **确认存在，但摘要不可得**

**Gong, J., Zhang, X., Zhang, J., Zeng, B., Zhang, X., Xu, X., … Xie, H.-A. (2026). Three-Line Hybrid Rice in China: Sustained Improvements in Yield, Quality, and Resistance Over Fifty Years. *Rice Science*. DOI: 10.1016/j.rsci.2026.04.004**（2026-04-01，13 位作者，通讯疑为谢华安）

**核实边界（如实声明）**：Undermind 返回 "Abstract unavailable"；WebFetch/curl 对 ScienceDirect 与 rice science 站点被 egress allowlist 拦截；`evidence/06_lit_breeding.md` 中的数字（1,493 个三系杂交稻、1984–1993 年 7,275 → 8,004 kg/hm²、+10.0 %）来自本项目此前的 WebSearch/Consensus 检索，**本次评审未能独立复核这些具体数值**。
**因此：所有方案在 cover letter 与正文中引用 Gong 2026 的具体数字前，必须取得全文核对。** 目前可确定的只有标题、期刊、年份、DOI 与作者列表——标题本身（"Sustained Improvements in Yield, Quality, and Resistance Over Fifty Years"）已足以支撑"三系杂交稻五十年性状改良回顾"这一定性判断。

**与各方案的重叠度**：
- **A：高（最高）**。同期刊、同题材、同数据类型。A 的应对（把 Gong26 作为方法学论证的靶标与致敬对象，并限定在籼型杂交中稻 × 长江流域 × 2005–2022）是正确的，但**风险实际上高于 A 自评**：若 Gong26 的审稿人/作者正是 A 的审稿人，"你只是把我们的均产比较换了个算法"会是第一反应。
- **B：中低**。B 只需在 §8 风险 R8 中点名区分。
- **C：低**。C 不做性状趋势，只做通道对照。**C 是四个方案中唯一与 Gong26 完全不撞车的**——这也是 C 提案"不推荐 Rice Science"的判断正确的原因。
- **D：中低**。同 B。

### 4.4 顺带核实的其他共用文献

- **Shi, X., & Hu, R. (2017). Rice variety improvement and the contribution of foreign germplasms in China. *Journal of Integrative Agriculture*, 16(10), 2337–2345. DOI: 10.1016/S2095-3119(16)61615-5** — 核实成立。摘要确认：1982–2011、15 省 1 自治区、IRRI 贡献 16.4 %、日本 11.2 %；**明确报告"1990 年代以来新育成品种的病虫抗性下降"**。这一点 A/B/C/D 都没用上，但它是"育种目标在性状间重新配置"的直接中国先例，**B/D 应当引用它作为"性状取舍确实发生过"的历史背书**。
- **Li, L., Zhang, L., & Wang, X. (2024). Research on the Dynamic Evaluation of the Competitiveness of Listed Seed Enterprises in China. *Agriculture*, 14(8), 1213.** — 核实成立（B/C 已引）。
- **Xie, Z., Yuan, S., Zhu, J., & Li, W. (2023). *Agribusiness*, 39(4): 1173–1198. DOI 10.1002/agr.21823** — 本次未独立复核（`evidence/07` 与 NOVELTY_ALERT 已有高置信度记录），沿用既有判断：博弈模型 + 鲜食玉米数值算例，荃银只在 Background 作二手财务例证，无品种级数据。

---

## 五、逐方案评分与"审稿人最可能用来否定它的那一句话"

### 5.1 评分表

> 权重：total = novelty×0.25 + feasibility×0.30 + fit×0.20 + rigor×0.15 + generality×0.10

| 方案 | novelty | feasibility | fit | rigor | generality | **total** | 排名 |
|---|---|---|---|---|---|---|---|
| **A** 作物科学 / 链式对照 | 6 | 8 | 8 | 7 | 8 | **7.35** | 2 |
| **B** 产业组织 / 纵向一体化 | 6 | 8 | 6 | 6 | 5 | **6.50** | 4 |
| **C** 政策评估 / 审定通道 | **8** | **9** | 8 | 7 | 8 | **8.15** | **1** |
| **D** 机制整合 / 收益函数 | 7 | 8 | 7 | 6 | 6 | **7.05** | 3 |

**评分理由逐项：**

**A**
- *novelty 6*：核心创新点 1 的概念被 Pie14/Lai14/Mac10/Ray23/Pie24 占位（见 §1），只剩数据—方法匹配层；创新点 2 确为空白但属工具移植；创新点 3 属操作化创新。自评 8 分偏高 **2 分**。
- *feasibility 8*：全部已跑通，无需新数据；扣分在对照阶梯最弱一环（汕优 63↔II 优 838 仅 1 条记录）。
- *fit 8*：Rice Science / FCR 命中度高，硬指标（2 区）达标，且方案本身不含财务内容，与刊物口味吻合。
- *rigor 7*：分解恒等式闭合检验、两条独立交叉验证（1.0 %/0.8 %）、R1–R12 完整；但主结论的敏感性区间 **15–86 %** 跨度达 5.7 倍，"约一半不是遗传"这一标题级断言的统计支撑弱于其修辞强度。
- *generality 8*：方法可移植到任何采用公告制审定的国家与作物，四个方案中最高。

**B**
- *novelty 6*：实证空白成立，但理论已被 IJIO 一脉占位（§3.1a），焦点企业已被 Xie23 占位，公私分化已被 Bur25 占位。自评 7 分基本合理，略高。
- *feasibility 8*：数据在手、全部跑通。
- *fit 6*：CAER 主题命中，但"农艺 + 财务"的缝合体裁（B 自己的 R7 风险）在任何一本刊都是硬伤；B 自己排除了 Agribusiness（3 区）这个**主题最同构**的去处，剩下的都是次优匹配。
- *rigor 6*：事件研究全面零结果、反向因果 B 路径"承认最难排除"、前沿只解释 15 % 的增产率劣势、申请人字段 2016–18/2021 全缺。
- *generality 5*：单一深度一体化企业 + 中国制度特定，最低。

**C**
- *novelty 8*：记录级通道变量经三路检索确认为空白；测量主体不对称的设计与场景为空白（逻辑被 Duflo13 占位，但那是不同设计、不同领域）；**外加一个未被提案充分标价的独立贡献**——sup-Wald 断点扫描证明"品质改善的断点在 2009–2015，早于 2016 改革；只有绝对产量的断点在 2017；比对照增产率二十年既无趋势也无断点"，这是对**两种流行叙事同时证伪**，方法论价值独立于主结果。
- *feasibility 9*：通道变量解析成功率 100 %、主结果与 R1–R12 全部跑通、Manski 界与 500 次随机化推断已完成。四个方案中唯一接近"只剩写作"的。
- *fit 8*：JIA 在任何分区口径下都是农林 1 区，风险最低；两条腿（品种级分析 + 制度经济学）都有该刊先例。
- *rigor 7*：主结果有 Manski 界符号稳定性（整精米率 [−1.832, −1.304]、垩白度 [+1.261, +1.530]）与随机化 p<0.002 支撑，且 R9（剔除荃银后仍显著）证明结论不依赖焦点企业；**扣分在 R11 组内检验（14 家申请人、64 条记录，CI 极宽）与 R12 省级复制失败**——这两项决定了 C 永远无法宣称 ATE。
- *generality 8*：设计可移植到任何"部分自组织测量 + 部分统一测量"的审批制度（EU VCU、医疗器械、车辆型式认证、食品安全认证）。

**D**
- *novelty 7*：与 B 同源，但 M4 堆叠单参数（λ = +0.570 SD, p<0.0001）与"监管性状 vs 收益性状"二分是超出 B 的框架增量，且解释了一个真实悖论（绝对产量 +4.38 kg/亩/yr vs 相对增产率零趋势）。自评 7.5 基本准确。
- *feasibility 8*：同 B。
- *fit 7*：JIA 契合度好于 B（机制论文比缝合论文更容易过），但机制框架要写到作物科学读者能读懂是实打实的写作成本。
- *rigor 6*：**焦点企业安慰剂检验失败**（株高 −1.36 cm p=0.0006、穗长 −0.37 p=0.0001、有效穗 −0.82 p=0.0044）；**旗舰性状垩白度在样外复制中方向反转**（+0.159, p=0.602）；H1 时间维度自认"不可判定"；INT 编码只有 4 家母公司 83 条记录。诚实度极高，但诚实不能替代证据。
- *generality 6*：略高于 B（因为已有 4 家同行的样外复制与合并组安慰剂通过）。

### 5.2 最佳方案：**C**

理由（三条）：
1. **唯一一个"新变量"而非"新算法"的方案。** A/B/D 都是在同一批性状数据上换模型；C 从公告原文里**造出了一个此前无人拥有的处理变量**。新变量的护城河远高于新模型。
2. **唯一一个与 Gong 2026 完全不撞车的方案。** A 正面撞车、B/D 侧面撞车。
3. **可行性最高且结论对焦点企业不敏感。** R9（剔除荃银全部品种后整精米率 −1.068 p=0.020、垩白度 +1.417 p=0.006、增产率 +0.593 p=0.011）意味着即使审稿人全盘否定荃银章节，论文主体依然完整——这是四个方案中唯一具备这一性质的。

---

## 六、"审稿人最可能用来否定各方案的那一句话"及应对

### A

> **"Piepho & Laidig (2014, TAG) 与 Mackay et al. (2011, TAG) 早已把官方品种试验的产量趋势分解为遗传与非遗传成分，Raymond et al. (2023, FCR) 更已证明遗传增益估计对长期对照的选择极度敏感、且对照产量本身并不稳定——所以你的'链式对照'是在用更差的数据重做一个已解决的问题，而你自己的敏感性区间（0.12–0.67 % ∙ yr⁻¹）宽到无法支撑'一半不是遗传增益'这个标题。"**

**应对（按优先级）：**
1. **改写定位，从"首创方法"改为"首次量化"。** 题目与摘要的断言应当是"**中国公告制审定数据的表观产量趋势有多少不是遗传增益**"，而不是"我提出了一种新估计量"。Introduction 第一段就引 Pie14/Lai14/Mac10，明确写"本文把这一成熟框架移植到一个此前无法应用它的数据结构上"。
2. **把 Lai14/Mac10 的"遗传占 ≥88 %"与本文的"51–59 %"做成核心对照。** 这个跨国反差本身就是最强的卖点，而且它恰好是**制度性的**（德英的官方试验体系用固定长期对照，中国用滚动对照），直接支撑 A §4.3 的政策建议（固定长期对照 + 滚动对照并行）。这一条如果写好，A 的 novelty 可以从 6 提到 7–8。
3. **把 R12 从"自我怀疑"改写为"复现 Ray23 的已知性质"**，并引用 Ray23 说明"对照产量随时间上升"在英国也被观测到，因此本文的 +0.445 % ∙ yr⁻¹ 漂移不是中国数据的病，而是一个已知现象在中国的量级。
4. **主结果一律用 2007–2022 窗口（0.465 % ∙ yr⁻¹、59 %）**，2005–2006 只进附录；R4（用 4,780 条省审数据独立重估对照阶梯）必须在投稿前完成，否则 R1 会被审稿人直接引用来否定标题。
5. 补引 [Dea16]（DEA-Malmquist 做育种研发效率）并主动区分，防止被误判撞车。

### B

> **"你只有一家深度一体化企业，事件研究是零结果，你自己也承认无法排除'先有品质育种能力才敢向下游延伸'——所以你拥有的只是一家公司的种质血缘与其商业模式之间的横截面相关，而 Xie et al. (2023) 已经用这家公司写过一篇了。"**

**应对：**
1. **彻底放弃因果语言**，全文用 "objective-function alignment"（B 自己已提出，但只在 §7.5 出现，必须上升到标题与摘要层）。
2. **把 §12 附录的"下一步"提到正文之前完成**：用 5–6 家上市种企的分部数据构造**连续型一体化强度 `INT_share_{i,t−5}`**，把 n=1 的哑变量升级为剂量—反应面板。**这是 B 唯一能把 generality 从 5 提到 7 的动作，且必须在投稿前做完，不能写成 future work。**
3. **主结果改以 H3（科研单位符号完全相反：产量 +6.77 kg/亩 p=0.0008、整精米率 −1.65 p=0.0076）领衔**——"产量更高但品质更差"这种**方向性权衡**是"资源差异"假说无法产生的，这是 B/D 手上最强的一个识别论证，但两个方案都把它埋在后面。
4. 补引 Zanchettin & Mukherjee (2017)、Liu (2016)、Rangnekar (2000)，把论文重新定位为"对一个已有理论预测的首个产品属性层实证"。
5. **与 D 合并，不要分别投稿**（理由见 §3.2、§3.3）。

### C

> **"通道是自选择的：走联合体试验的本来就是育种能力较弱的申请人，所以你测到的是申请人质量差异而不是测量主体差异；你自己的 R11（组内检验）和 R12（省级复制）都没能排除这一点。"**

**应对（这是 C 唯一真正的软肋，必须写得比审稿人更狠）：**
1. **把不对称本身做成识别论证，而不只是描述。** 纯粹的"申请人能力差异"假说预测：弱申请人的品种在**所有**性状上都更差。而实测是：第三方测的品质**更差**（整精米率 −1.68、垩白度 +1.34），申请人自测的增产率**更好**（+0.55）。**能力差异假说无法解释这个符号反转**；能解释它的只有"测量主体不同"或"两条通道的申报门槛不同"。这一句话应当写进 Abstract 与 §4.2，而不是留在 Discussion。
2. **补引 Duflo et al. (2013, QJE) 与 Bar & Zheng (2018, AJAE)**，并明确写出本文与它们的设计差异（Duflo：同一属性两方测量 + 随机实验；Bar & Zheng：认证方选择的内生性；本文：同一文书内两类属性、非实验）。**不引这两篇是当前提案最大的文献漏洞**——尤其 Bar & Zheng 就是 AJAE 的农经论文，审稿人一定知道。
3. **R11 必须配功效分析**：给出"现有 14 家申请人 / 64 条记录在 80 % 功效下能侦测的最小效应量"，并证明它大于主设定的 1.68 pp。把"无法拒绝"改写为"设计本身不具备拒绝能力"。
4. **R12 重构为异质性发现**（C 已提出，做法正确）："效应集中在奖品最大的国审层"，并给出省级样本的 MDE。
5. **性状安慰剂的株高 +0.96 cm（p=0.011）是个隐患**——审稿人会说"你的安慰剂也显著了"。建议改用一组更彻底无商业价值的性状（如结实率、有效穗）重做，或把株高重新归类为"与新通道高秆大穗选型一致的辅助证据"并移出安慰剂集合（C 已倾向后者，但必须在方法节**预先声明**，不能事后解释）。
6. 明确引用 Xiang et al. (2025) 的"杂交稻许可费不受改革影响"作为本文的互补证据（价格维度无效应 ≠ 进入者构成无变化）。

### D

> **"你的安慰剂性状在焦点企业上全线失败（株高、穗长、有效穗都显著），旗舰性状垩白度在剔除荃银后方向反转、p=0.60，而你的一体化哑变量只建立在 4 家母公司、83 条记录上——所以你捕捉的很可能是一个育种程序的种质血缘签名，不是经济激励。"**

**应对：**
1. **把 M4 的 λ = +0.570 SD 作为唯一的标题级数字**（它通过了合并组安慰剂 p=0.104，且在剔除绝对产量后成立），把分性状结果全部降级为支撑证据。
2. **预注册式地把主假设收缩到"整精米率 + 粒型 + 相对增产率"三项**，把垩白度移出主假设集合并在正文说明理由（它在焦点企业与同行组之间不一致，是探索性结果）。**现在 D 把垩白度写在摘要里是自找麻烦。**
3. **立刻执行 R1 的第 ③ 项"同血缘对照"**：把含荃系亲本但由其他单位申请的品种单列一组。若其血缘性状（株高、穗长）保留而品质优势消失，安慰剂失败问题即被彻底化解。**这是技术上最便宜、收益最大的一个补做，只需加一个分组变量。**
4. **执行 R7 的"改革后 × 一体化"三重差分**（D 自评"数据已具备、本次未运行"）。2016/17 改革把增产率从目标降为约束，对所有主体同时生效，只有一体化主体有动机把释放的选择空间投向品质——这是 D 手上**唯一可能接近外生性**的设计。
5. 补引 Zanchettin & Mukherjee (2017)、Liu (2016)、Rangnekar (2000)、Shi & Hu (2017)。

---

## 七、真正无可替代的那一个创新点

**是 C 的：审定公告原文中同时存在（i）逐字载明的试验通道（国家统一区试 / 绿色通道 / 联合体）与（ii）由不同主体测量的两类性状——申请人自组织试验测定的产量与比对照增产率、农业农村部指定机构按 NY/T 593 统一测定的整精米率与垩白度。**

**为什么它无可替代：**

1. **它是一个数据资产，不是一个分析选择。** A 的链式对照、A 的 DEA、B/D 的回归设定，任何一个掌握同一批审定数据的团队都能在两周内复现或超越；而"通道 + 测量主体"这对变量必须从公告原文的"产量表现"段落里逐条解析出来（正则：`绿色通道|自主试验` → Green，`联合体` → Consortium，其余 → Unified），且只有在意识到"这两类性状由不同主体测量"之后才有分析价值。这一步认知本身就是贡献。

2. **它不能被任何现有设计从外部生产出来。** Xiang et al. (2025) 有真实的许可交易数据、有全国企业问卷、有 Jikun Huang 的团队资源——**仍然做不出这个变量**，因为他们的数据单位是企业与交易，不是审定记录。Duflo et al. (2013) 有随机实验，但他们必须**自己出钱另雇审计员复测**才能得到"同一属性的两个测量"；中国的审定制度**免费**提供了一个近似物。

3. **它同时支撑一个正面结论与一个负面结论，且两者互相加固。** 正面：自组织通道进入者在第三方测定的品质上差 1.68/1.34 pp（Manski 界符号稳定），在自测的增产率上反而好 0.55 pp。负面：sup-Wald 扫描显示品质改善的断点普遍在 2009–2015 年、早于 2016 改革，而比对照增产率二十年无趋势无断点——**"把品质变化归因于 2016 年改革"在这批数据上是错误归因**。一个数据资产同时证伪了官方叙事（改革提高品种质量）与行业叙事（改革降低品种质量），并解释了为什么必须用同年通道对照而不是时间断点。

4. **它的外部效度最高。** "谁来测量决定了什么进入市场"这一问题在 EU 的 VCU 制度、医疗器械的公告机构（notified bodies）、车辆型式认证、食品安全第三方认证中全部存在，但几乎没有哪个制度像中国品种审定这样，把两类测量主体的产出**并排印在同一份公开文书上**。这使得 C 有资格在 Discussion 中对整个"认证中介"文献说话，而不只是对中国种业说话。

**最后提醒一句：C 的这个创新点有一个时间窗。** 2022 年农业农村部已对绿色通道/联合体试验启动专项整治，2024 年 3 月通报第三批整治处理结果；C 的 Fig. 3 逐年通道差已显示垩白度差距从 2017 年的 +3.00 收敛到 2022 年的 +0.84。**如果整治使两条通道趋同，这个变量的识别变异会消失。现在不做，以后做不了。**

---

## 附：本评审核实过的全部文献（完整引文与 DOI）

**遗传增益方法学（对 A）**
1. Piepho, H.-P., Laidig, F., Drobek, T., & Meyer, U. (2014). Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. *Theoretical and Applied Genetics*, 127, 1009–1018. DOI: 10.1007/s00122-014-2275-1
2. Laidig, F., Piepho, H.-P., Drobek, T., & Meyer, U. (2014). Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. *Theoretical and Applied Genetics*, 127, 2599–2617. DOI: 10.1007/s00122-014-2402-z
3. Mackay, I., Horwell, A., Garner, J., White, J., McKee, J., & Philpott, H. (2011). Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. *Theoretical and Applied Genetics*, 122, 225–238. DOI: 10.1007/s00122-010-1438-y
4. Raymond, J., Mackay, I., Penfield, S., Lovett, A., Philpott, H., & Dorling, S. (2023). Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. *Field Crops Research*, 303, 109086. DOI: 10.1016/j.fcr.2023.109086
5. Piepho, H.-P., & Laidig, F. (2024). How Many Checks Are Needed per Cycle in a Plant Breeding or Variety Testing Programme? *Plant Breeding*, 144(1). DOI: 10.1111/pbr.13240
6. Seck, F., Covarrubias-Pazaran, G., Gueye, T., & Bartholomé, J. (2023). Realized Genetic Gain in Rice: Achievements from Breeding Programs. *Rice*, 16, 61. DOI: 10.1186/s12284-023-00677-6

**中国审定品种性状文献（共同）**
7. Lu, Y., Tang, Y., Zhang, J., Liu, S., Liang, X., Li, M., & Li, R. (2024). Variations and Trends in Rice Quality across Different Types of Approved Varieties in China, 1978–2022. *Agronomy*, 14(6), 1234. DOI: 10.3390/agronomy14061234
8. Hang, S., Wang, Q., Wang, Y., & Xiang, H. (2024). Evolution of Rice Cultivar Performance Across China: A Multi-Dimensional Study on Yield and Agronomic Characteristics over Three Decades. *Agronomy*, 14(12), 2780. DOI: 10.3390/agronomy14122780
9. Gong, J., Zhang, X., Zhang, J., Zeng, B., Zhang, X., Xu, X., … Xie, H.-A. (2026). Three-Line Hybrid Rice in China: Sustained Improvements in Yield, Quality, and Resistance Over Fifty Years. *Rice Science*. DOI: 10.1016/j.rsci.2026.04.004 〔**摘要未能取得，具体数值待核**〕
10. Shi, X., & Hu, R. (2017). Rice variety improvement and the contribution of foreign germplasms in China. *Journal of Integrative Agriculture*, 16(10), 2337–2345. DOI: 10.1016/S2095-3119(16)61615-5

**规制与认证（对 C）**
11. Duflo, E., Greenstone, M., Pande, R., & Ryan, N. (2013). Truth-telling by Third-party Auditors and the Response of Polluting Firms: Experimental Evidence from India. *Quarterly Journal of Economics*, 128(4), 1499–1545. DOI: 10.1093/qje/qjt024
12. Bar, T., & Zheng, Y. (2018). Choosing Certifiers: Evidence from the British Retail Consortium Food Safety Standard. *American Journal of Agricultural Economics*. DOI: 10.1093/ajae/aay024
13. Grennan, M., & Town, R. J. (2020). Regulating Innovation with Uncertain Quality: Information, Risk, and Access in Medical Devices. *American Economic Review*, 110(1), 120–161. DOI: 10.3386/w20981
14. Certification Intermediaries: Evidence from the Medical Device Industry (2015). SSRN. DOI: 10.2139/ssrn.2554984
15. Renckens, S., & Auld, G. (2020). Time to certify: Explaining varying efficiency of private regulatory audits. *Regulation & Governance*, 14(4). DOI: 10.1111/rego.12362
16. Xiang, C., Yang, R., Wang, X., & Huang, J. (2025). Impact of Seed Regulation Reform on Licensing Fees of Varieties in China. *Agribusiness*. DOI: 10.1002/agr.22020

**纵向一体化与育种目标（对 B/D）**
17. Zanchettin, P., & Mukherjee, A. (2017). Vertical integration and product differentiation. *International Journal of Industrial Organization*, 54, 25–57. DOI: 10.1016/j.ijindorg.2017.07.004
18. Liu, X. (2016). Vertical integration and innovation. *International Journal of Industrial Organization*, 47, 88–120. DOI: 10.1016/j.ijindorg.2016.02.002
19. Chambolle, C., & Guignard, M. (2025). Buyer Power and the Effect of Vertical Integration on Innovation. SSRN. DOI: 10.2139/ssrn.4341954
20. Burris, L., Nalley, L., De Steur, H., Durand-Morat, A., Tack, J., Yang, W., & Lusk, J. (2025). The divergence of the public and private plant breeding sectors with implications for climate change. *npj Science of Plants*. DOI: 10.1038/s44383-025-00013-5
21. Rangnekar, D. (2000). Planned Obsolescence and Plant Breeding: Empirical Evidence from Wheat Breeding in the UK (1965–1995). 〔无 DOI；Semantic Scholar: 27190a41a4f18125173f34c349c822bc820163fa〕
22. Goodhue, R., Mohapatra, S., & Rausser, G. (2010). Interactions Between Incentive Instruments: Contracts and Quality in Processing Tomatoes. *American Journal of Agricultural Economics*, 92(5), 1283–1293.
23. Kennett, J., Fulton, M., Molder, P., & Brooks, H. (1998). Supply chain management: the case of a UK baker preserving the identity of Canadian milling wheat. *Supply Chain Management*, 3(3), 157–166.
24. Xie, Z., Yuan, S., Zhu, J., & Li, W. (2023). Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? *Agribusiness*, 39(4), 1173–1198. DOI: 10.1002/agr.21823 〔本次未独立复核，沿用 `evidence/07` 与 NOVELTY_ALERT 的高置信度记录〕

**DEA / 多性状评价（对 A-2）**
25. Yan, W., & Frégeau-Reid, J. (2018). Genotype by Yield*Trait (GYT) Biplot: a Novel Approach for Genotype Selection based on Multiple Traits. *Scientific Reports*.
26. Hashemi, M., et al. (2019). Evaluating Winter Barley Cultivar Using Data Envelopment Analysis Models. *Journal of Agricultural Science*.
27. Ahtikoski, A., et al. (2020). Financial assessment of alternative breeding goals using stand-level optimization and data envelopment analysis. *Scandinavian Journal of Forest Research*, 262–273.
28. 喻亚平, 余利丰 (2016). 我国农业育种研发效率的实证分析——基于 DEA-Malmquist 指数分析的视角. 9–15.〔**标题极易被误认为与 A-2 撞车，须主动区分**〕
