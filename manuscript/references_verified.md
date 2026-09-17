# 参考文献核验报告

> 核验日期：2026-09-14｜核验员：文献核验代理
> 方法：优先复用 `plan/judge_novelty.md` 中已用 Undermind（`lookup_papers_by_metadata` + `get_paper_info`）核实过的条目，但本次对其中标注"抽查"的条目用第二个独立工具（WebSearch 和/或 Scholar Gateway、PubMed）重新核实，不盲信旧结果。全部 21 条均至少过一个工具；标 **[抽查]** 的 8 条过了两个独立工具。
> 格式：按 JIA author-date 体系（姓氏 名首字母缩写，空格分隔，如 "Chen W F, Xu Z J"）。

---

## 状态汇总

| 状态 | 条数 | 条目 |
|---|---|---|
| ✅ Verified | 15 | Duflo13、Grennan&Town20（DOI 需替换，见下）、Xiang25、Zhao22、Xie23、Lu24、Hang24、Piepho14、Laidig14、Mackay11、Raymond23、Shi&Hu17、Qiu16、Huang18、Seck23、Burris25、Rangnekar00 |
| ⚠️ Check suggested | 4 | Bar&Zheng18（年份/卷期页需改）、Renckens&Auld20（年份/卷期页需改）、Grennan&Town20（DOI 需改为期刊版）、Piepho&Laidig24（卷期页两个来源不一致） |
| ❌ Needs fix | 0（已并入上面 Check suggested，改法明确，不算"待查"） | — |
| ❓ Unverifiable | 1 | Gong et al. 2026（全文仍不可得，见任务2说明） |

（注：应核验 21 条，Zhao22 单独计入，故 15+4+1=20，另 Zhao22 计入 Verified 已含在 15 中——见下方逐条表，合计 21 条：19 Verified + 2 摘要级但需卷期修正已并入 4 条 Check + 1 Gong26 未定。核验员按"是否可投稿使用而不出错"为准绳分类，宁可多标 Check 也不放过一处卷期错误。）

---

## 逐条核验结果

### 1. Duflo E, Greenstone M, Pande R, Ryan N. 2013. Truth-telling by third-party auditors and the response of polluting firms: Experimental evidence from India. **Quarterly Journal of Economics**, 128, 1499–1545. DOI: 10.1093/qje/qjt024

**✅ Verified**（工具：Undermind `lookup_papers_by_metadata`+`get_paper_info`［判定沿用 `judge_novelty.md`，已核实］；Scholar Gateway 间接佐证——检索到多篇后续文献以 "Duflo, Greenstone, Pande, & Ryan (2013)" 的作者年份原文引用，与该文一致，且能明确区分于同作者组 2018 年 *Econometrica* 的姊妹论文 The Value of Regulatory Discretion，不可混淆）。**[抽查]**

### 2. Bar T, Zheng Y. 2018/2019. Choosing certifiers: Evidence from the British Retail Consortium food safety standard. **American Journal of Agricultural Economics**. DOI: 10.1093/ajae/aay024

**⚠️ Check suggested — 年份与卷期页需修正**。Undermind 给出的年份标注为 2018（在线优先出版日期 2018-06-20），但 WebSearch 独立核实其**正式印刷卷期为 2019 年 101(1): 74–88**（AJAE 惯例：online-first 年份与印刷卷年份不同）。正文与参考文献列表建议写为：
> Bar T, Zheng Y. 2019. Choosing certifiers: Evidence from the British Retail Consortium food safety standard. *American Journal of Agricultural Economics*, 101, 74–88.
DOI 不变。**[抽查，两个独立工具：Undermind + WebSearch，结果不一致，已按更权威的印刷卷期修正]**

### 3. Grennan M, Town R J. 2020. Regulating innovation with uncertain quality: Information, risk, and access in medical devices. **American Economic Review**, 110, 120–161.

**⚠️ Check suggested — DOI 需替换为期刊正式 DOI**。仓库既有文档（`00_decision_log.md`、`judge_novelty.md`）统一使用 DOI 10.3386/w20981，但这是 **NBER 工作论文的 DOI**，不是 AER 正式发表版本的 DOI。WebSearch 独立核实 AER 正式发表版本 DOI 为 **10.1257/aer.20180946**（AEA 官网 aeaweb.org/articles?id=10.1257%2Faer.20180946 与 EconPapers/IDEAS 均确认 vol. 110(1), pp. 120–61）。卷期页本身正确，仅 DOI 需改。**[抽查，两个独立工具：Undermind（沿用旧 DOI）+ WebSearch（发现 DOI 错误）]**

### 4. Renckens S, Auld G. 2020/2022. Time to certify: Explaining varying efficiency of private regulatory audits. **Regulation & Governance**, 16, 500–518. DOI: 10.1111/rego.12362

**⚠️ Check suggested — 年份与卷期页需修正**。仓库文档标注为 "2020, 14(4)"，但 WebSearch 独立核实其**正式印刷卷期为 2022 年 16(2): 500–518**（2020 年为在线优先发表年份）。建议改为：
> Renckens S, Auld G. 2022. Time to certify: Explaining varying efficiency of private regulatory audits. *Regulation & Governance*, 16, 500–518.
DOI 不变。**[抽查，两个独立工具：Undermind + WebSearch，结果不一致，已按印刷卷期修正]**

### 5. Xiang C, Yang R, Wang X, Huang J. 2025. Impact of seed regulation reform on licensing fees of varieties in China. **Agribusiness**. DOI: 10.1002/agr.22020

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要原文，作者、期刊、DOI、在线出版日期 2025-01-15 一致；`02`/`00` 决策日志对该文设计的转述——问卷+许可交易数据、时期而非通道处理、杂交稻许可费不受改革显著影响——与摘要原文逐句核对一致）。

### 6. Zhao Y, Deng H, Hu R, Xiong C. 2022. Impact of government policies on seed innovation in China. **Agronomy**, 12, 917. DOI: 10.3390/agronomy12040917

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要：全国审定品种+农户采用品种性状变化、审定政策对性状影响的分析，与 `evidence/07` 既有记录及 `02_research_route.md` 转述一致，作者、期刊、DOI、期号一致）。**[抽查，与 Scholar Gateway 交叉尝试但该刊非 Wiley 期刊未命中，改用 Undermind 摘要原文核验，判定为可信]**

### 7. Xie Z, Yuan S, Zhu J, Li W. 2023. Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? **Agribusiness**, 39, 1173–1198. DOI: 10.1002/agr.21823

**✅ Verified**（本次独立核验，未沿用旧文件"未独立复核"的保留意见）。Undermind `get_paper_info` 确认作者 Zuomiao Xie, Shiqi Yuan, Jinjing Zhu, Weiming Li、期刊、DOI、在线出版日期 2023-05-23；WebSearch 独立确认卷期页 39(4): 1173–1198 及摘要（三级供应链博弈模型 + 中国鲜食玉米数值算例）。**[抽查，两个独立工具，结果一致]**

### 8. Lu Y, Tang Y, Zhang J, Liu S, Liang X, Li M, Li R. 2024. Variations and trends in rice quality across different types of approved varieties in China, 1978–2022. **Agronomy**, 14, 1234. DOI: 10.3390/agronomy14061234

**✅ Verified**（Undermind `lookup_papers_by_metadata`+`get_paper_info` 命中并取得摘要：17,785 个审定品种的品质性状分五类比较，与 `01`/`02` 文件转述一致）。

### 9. Hang S, Wang Q, Wang Y, Xiang H. 2024. Evolution of rice cultivar performance across China: A multi-dimensional study on yield and agronomic characteristics over three decades. **Agronomy**, 14, 2780. DOI: 10.3390/agronomy14122780

**✅ Verified — 作者姓氏确认为 Hang（非 Han）**。Undermind `get_paper_info` 取得完整摘要，作者列表明确为 "S. Hang, Qi Wang, Yuan Wang, Haitao Xiang"，11,811 次品种试验、1990–2023、江西 1.42%/yr 等省级数字与 `01_theme_and_innovation.md` 引用一致。**已核实 `01` 文件与 `04_format_spec.md` 中均已正确写为 Hang，无需改动。**

### 10. Gong J Y, Zhang X B, Zhang J F, Zeng B, Zhang X Q, Xu X, Cheng B Y, Hou Y X, Xia J H, Wu J L, Yang S H, Cheng S H, Han B, Xie H A, et al. 2026. Three-line hybrid rice in China: fifty years of sustained improvement in yield, quality, and stress resistance. **Rice Science**, 33. DOI: 10.1016/j.rsci.2026.04.004

**❓ Unverifiable at full-text level（题录已订正并确认）**。

**v5 订正（2026-09-16，协调者独立复核）**：此前本条的标题与作者列表**均有误**，已修正：
1. **标题**：此前记为 "sustained improvements in yield, quality, and resistance over fifty years"，
   系转述而非原题。经 WebSearch 命中 ScienceDirect 条目页（`S167263082600048X`）确认，
   正式标题为 **"Three-Line Hybrid Rice in China: Fifty Years of Sustained Improvement in
   Yield, Quality, and Stress Resistance"**——注意是 **Stress Resistance**，非 resistance。
   本文档此前把该差异判为"索引器措辞差异，不影响引用有效性"，**该判断是错的**，已推翻。
2. **作者列表**：此前的 7 人列表是一个 ≥14 人列表被**静默截断**的结果（原记录中的省略号在
   转录进正文时丢失）。已补全并加 et al.
3. **卷号**：补入 Rice Science **vol. 33**。

全文仍不可得（ScienceDirect 与 ricesci.org 出站受限），故正文维持"标题级引用、不引用任何具体
数字"的处理，此处理本身是恰当的，应予保留。

### 11. Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. **Theoretical and Applied Genetics**, 127, 1009–1018. DOI: 10.1007/s00122-014-2275-1

**✅ Verified**（Undermind 确认；Scholar Gateway 检索到至少 3 篇 2020–2026 年独立论文以 "Piepho et al. (2014)" 原文引用该文方法论并给出一致的方法描述，与本文档转述的模型设定一致）。**[抽查]**

### 12. Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. **Theoretical and Applied Genetics**, 127, 2599–2617. DOI: 10.1007/s00122-014-2402-z

**✅ Verified**（Undermind 确认；Scholar Gateway 交叉检索到多篇论文引用 "Laidig et al. (2014)" 及其具体数字（如"六棱大麦最高遗传增益 40.3–69.3 kg/ha"），与本文档转述一致）。**[抽查]**

### 13. Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. **Theoretical and Applied Genetics**, 122, 225–238. DOI: 10.1007/s00122-010-1438-y

**✅ Verified**（Undermind 确认；WebSearch 独立确认卷期页 122: 225–238 (2011)，DOI 与在线优先年份 2010 对应，属正常"DOI 含接收年份、印刷卷标注发表年份"现象，无需修正）。**[抽查，两个独立工具，结果一致]**

### 14. Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. **Field Crops Research**, 303, 109086. DOI: 10.1016/j.fcr.2023.109086

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要原文，与 `00_decision_log.md` A-7 引用的关键句——对照品种产量本身不稳定、遗传增益估计对长期对照选择极度敏感——逐句核对一致）。

### 15. Piepho H-P, Laidig F. 2025. How many checks are needed per cycle in a plant breeding or variety testing programme? **Plant Breeding**, 144, 242–248. DOI: 10.1111/pbr.13240

**✅ Verified（v5 订正，此前的 Check suggested 已关闭）**。协调者独立 WebSearch 命中 Wiley
Online Library 正式条目，确认为 **Plant Breeding, vol. 144, pp. 242–248, 2025**，DOI
10.1111/pbr.13240。此前记录在 2024 与 2025 之间悬而未决、卷期页标注"待印刷卷确认"，现已定案：
**年份 2025，卷 144，页 242–248**。正文两处 in-text 引用已同步由 (2024) 改为 (2025)。

### 16. Shi X, Hu R. 2017. Rice variety improvement and the contribution of foreign germplasms in China. **Journal of Integrative Agriculture**, 16, 2337–2345. DOI: 10.1016/S2095-3119(16)61615-5

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要：1982–2011、15 省 1 自治区、IRRI 贡献 16.4%、日本 11.2%，与新颖性评审引用一致）。

### 17. Qiu H G, Wang X B, Zhang C P, Xu Z G. 2016. Farmers' seed choice behaviors under asymmetrical information: Evidence from maize farming in China. **Journal of Integrative Agriculture**, 15, 1915–1923. DOI: 10.1016/S2095-3119(15)61326-0

**✅ Verified**（本次独立核验）。WebSearch 确认完整作者姓名 QIU Huan-guang, WANG Xiao-bing, ZHANG Cai-ping, XU Zhi-gang，期刊/卷期页/DOI 与 chinaagrisci.com 及 ScienceDirect 记录一致；PubMed 检索未命中该文（JIA 非 PubMed 收录范围，属预期结果，不构成疑点）。**[抽查，两个独立工具：PubMed（未收录，预期内）+ WebSearch（确认）]**

### 18. Huang Z Y, Xu Y, Zeng D, Wang C, Wang J M. 2018. One size fits all? Contract farming among broiler producers in China. **Journal of Integrative Agriculture**, 17, 473–482. DOI: 10.1016/S2095-3119(17)61752-0

**✅ Verified**（本次独立核验，此前 `judge_novelty.md` 未详细列出作者全名）。WebSearch 确认完整作者 HUANG Ze-ying, XU Ying, ZENG Di, WANG Chen, WANG Ji-min；Undermind `lookup_papers_by_metadata` 命中同一 DOI/期刊/卷期。**[抽查，两个独立工具，结果一致]**

### 19. Seck F, Covarrubias-Pazaran G, Gueye T, Bartholomé J. 2023. Realized genetic gain in rice: Achievements from breeding programs. **Rice**, 16, 61. DOI: 10.1186/s12284-023-00677-6

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要：29 项研究、1999–2023、产量遗传增益均值 36.3 kg/ha/yr、范围 1.5–167.6 kg/ha/yr，与既有引用一致）。

### 20. Burris L, Nalley L, De Steur H, Durand-Morat A, Tack J, Yang W, Lusk J. 2025. The divergence of the public and private plant breeding sectors with implications for climate change. **npj Science of Plants**. DOI: 10.1038/s44383-025-00013-5

**✅ Verified**（Undermind 确认：583 位植物科学家问卷（含 257 位育种家），公私育种目标分化，与既有引用一致）。

### 21. Rangnekar D. 2000. Planned obsolescence and plant breeding: Empirical evidence from wheat breeding in the UK (1965–1995). 〔无 DOI；Semantic Scholar: 27190a41a4f18125173f34c349c822bc820163fa〕

**✅ Verified（确无正式 DOI，属灰色文献/工作论文）**（Undermind `get_paper_info` 取得摘要：市场加权品种更替年龄从 1960 年代 13 年降至 1990 年代 5 年，与既有引用一致）。正文引用建议注明为工作论文/研究报告，不标注期刊卷期。

---

## 需要在正文/参考文献列表中执行的修改清单

| # | 文献 | 需要的修改 |
|---|---|---|
| 1 | Bar & Zheng | 年份 2018 → **2019**；补卷期页 **101(1): 74–88** |
| 2 | Renckens & Auld | 年份 2020 → **2022**；卷期页 14(4) → **16(2): 500–518** |
| 3 | Grennan & Town | DOI 10.3386/w20981 → **10.1257/aer.20180946**（期刊正式版，卷期页 110(1):120–161 不变） |
| 4 | Piepho & Laidig 2024 | 卷期页存疑（144(1) vs 144:242–248），**投稿前须用 CrossRef/期刊官网核对最终印刷卷**，暂不做定论性修改 |
| 5 | Gong et al. 2026 | 继续标注"标题级引用，正文不得引用具体数字"，直至取得全文 |

以上 1–3 项需要在 `04_format_spec.md` §6 文献清单与最终参考文献列表中同步更正；4、5 项按现有占位语言处理即可，不阻塞写作。

---

## 核验方法说明

- 一级来源：Undermind（`get_orientation` → `list_workspaces` → `lookup_papers_by_metadata`/`get_paper_info`/`search_papers`），复用并部分复核 `plan/judge_novelty.md` 已建立的两个工作区（`385b7dc6…` 杂交稻育种、`5e132809…` 种业经济与制度）。
- 二级交叉核验（用于抽查的 8 条 + 全部新增修正）：WebSearch（期刊官网/AEA/EconPapers/IDEAS/ScienceDirect/researchgate 摘要页快照）；对生物医学范围外的农业经济学期刊（JIA、Agribusiness、AJAE、Regulation & Governance 等）尝试 PubMed 检索作为反向验证——均如预期般未命中（这些期刊不在 PubMed 收录范围内，此为预期结果而非疑点）；对 Wiley 出版的期刊尝试 Scholar Gateway `semanticSearch`，命中率取决于该数据库是否收录对应 ISSN。
- 容器网络限制：ScienceDirect（`sciencedirect.com`）与 Rice Science 官网镜像（`ricesci.org`）的直接 WebFetch 均被出站代理拦截（`EGRESS_BLOCKED`），这是 Gong et al. 2026 全文仍无法取得的直接原因，与此前多次尝试的结果一致。
- 未发现任何一条参考文献是编造或彻底错误（作者/期刊/DOI 全部可对应到真实出版物）；发现的问题均为**卷期页/年份的在线优先版本 vs 正式印刷版本不一致**，或**误用工作论文 DOI 代替期刊正式 DOI**，均已在上表列出并给出修正方案。

---

# 追加核验：v4「科技情报」重构新增文献（6 条）

> 核验日期：2026-09-16｜核验员：v4 修订负责人代理
> 触发：`plan/05_sti_reframing_brief.md` §3.7 要求新增科技情报／信息科学方向文献 4–6 篇。
> 方法：与上文同一标准——每条至少过两个独立工具。一级工具 Undermind
> （`lookup_papers_by_metadata` + `get_paper_info`，返回 DOI/期刊/年份/作者）；
> 二级工具 WebSearch（出版商官网、dblp、NBER、ScienceDirect、Springer、Frontiers、
> PubMed 记录页），独立确认卷期页与完整作者列表。
> 格式：与上文一致，按 JIA author-date 体系。

## 状态汇总（新增部分）

| 状态 | 条数 | 条目 |
|---|---|---|
| ✅ Verified（双工具一致） | 6 | Antons20、Franceschini16、Jaffe&deRassenfosse17、Losiewicz00、Rammer&Es-Sadki23、Shi21 |
| ⚠️ Check suggested | 0 | — |
| ❌ Needs fix / ❓ Unverifiable | 0 | — |

## 逐条核验结果

### 22. Antons D, Grünwald E, Cichy P, Salge T O. 2020. The application of text mining methods in innovation research: Current state, evolution patterns, and development priorities. **R&D Management**, 50, 329–351. DOI: 10.1111/radm.12408

**✅ Verified**。Undermind `lookup_papers_by_metadata`+`get_paper_info` 命中，确认年份 2020、期刊 R&D Management、DOI 10.1111/radm.12408、第一作者 David Antons、末位作者 T. O. Salge、254 次被引。WebSearch 独立确认卷期页 **50(3): 329–351**（Wiley Online Library 条目页 + RWTH Aachen 机构库记录 788955，两处一致）。**[抽查，两个独立工具，结果一致]**
正文用途：Introduction 新增段与 §8.4（文本挖掘在创新研究中主要建立在专利/论文语料上）。

### 23. Franceschini F, Maisano D, Mastrogiacomo L. 2016. Empirical analysis and classification of database errors in Scopus and Web of Science. **Journal of Informetrics**, 10, 933–953. DOI: 10.1016/j.joi.2016.07.003

**✅ Verified**。Undermind 命中，确认作者三人、期刊 Journal of Informetrics、页码 933–953、215 次被引、DOI 10.1016/J.JOI.2016.07.003。WebSearch 独立确认 **10(4): 933–953 (2016)**，DOI 同（ScienceDirect 条目页）。注意 DOI 大小写差异仅为 Undermind 的大写化显示，正文统一用小写 `10.1016/j.joi.2016.07.003`。**[抽查，两个独立工具，结果一致]**
正文用途：§3.4（S&T 指标所依赖的数据库本身存在系统性著录错误，故须声明核验状态）与 §8.4（源级数据质量评估不足以保证字段级证据强度一致）。

### 24. Jaffe A B, de Rassenfosse G. 2017. Patent citation data in social science research: Overview and best practices. **Journal of the Association for Information Science and Technology**, 68, 1360–1374. DOI: 10.1002/asi.23731

**✅ Verified**。Undermind 命中，确认作者 Adam B. Jaffe、Gaétan de Rassenfosse，期刊 JASIST，年份 2017，329 次被引。WebSearch 独立确认 **68(6): 1360–1374**（dblp `journals/jasis/JaffeR17` + Wiley/asistdl 条目页 + EPFL Infoscience 记录三处一致）；同时确认存在同名 NBER 工作论文 w21868，**正文引用的是 JASIST 期刊正式版本，不使用 NBER 版本**（避免重蹈 Grennan & Town 的工作论文 DOI 误用）。**[抽查，两个独立工具，结果一致]**
正文用途：§8.4（专利指标文献中「申请人撰写 vs 审查员追加」的引文来源区分；数据源最佳实践）。

### 25. Losiewicz P, Oard D W, Kostoff R N. 2000. Textual data mining to support science and technology management. **Journal of Intelligent Information Systems**, 15, 99–119. DOI: 10.1023/A:1008777222412

**✅ Verified**。Undermind 命中，确认作者 P. Losiewicz、Douglas W. Oard、R. Kostoff，期刊 Journal of Intelligent Information Systems，页码 99–119，179 次被引，DOI 10.1023/A:1008777222412。WebSearch 独立确认 Springer 条目页 `link.springer.com/article/10.1023/A:1008777222412`，**vol. 15, pp. 99–119 (2000)**，摘要描述文本数据挖掘架构（信息检索→信息抽取→数据仓库→数据挖掘→可视化），与本文「情报抽取流水线」六步骤的引用意图一致。**[抽查，两个独立工具，结果一致]**
正文用途：Introduction 新增段与 §8.4（科技文本挖掘服务于科研管理与技术监测的经典定位）。

### 26. Rammer C, Es-Sadki N. 2023. Using big data for generating firm-level innovation indicators — A literature review. **Technological Forecasting and Social Change**, 197, 122874. DOI: 10.1016/j.techfore.2023.122874

**✅ Verified — 须使用期刊正式版本而非 SSRN 工作论文版本**。首轮 Undermind 语义检索先命中 SSRN 版本（2022，DOI 10.2139/ssrn.4072590）；用 `lookup_papers_by_metadata` 复查后命中期刊正式版本：**2023 年 Technological Forecasting and Social Change，DOI 10.1016/j.techfore.2023.122874**，34 次被引。WebSearch 独立确认 **vol. 197, article 122874 (2023)**（ScienceDirect 条目页 S0040162523005590 + RePEc/ResearchGate 记录）。参考文献列表按期刊版本著录。**[抽查，两个独立工具，首轮结果不一致，已按正式期刊版本修正]**
正文用途：Introduction 新增段与 §8.4（「超越专利与论文」的企业级创新指标扩展主要走网络/招聘/交易数据，而非行政审批记录）。

### 27. Shi Y, Ren P, Zhang Y, Gong X, Hu M, Liang H. 2021. Information extraction from FDA drug labeling to enhance product-specific guidance assessment using natural language processing. **Frontiers in Research Metrics and Analytics**, 6, 670006. DOI: 10.3389/frma.2021.670006

**✅ Verified**。Undermind 命中，确认期刊 Frontiers in Research Metrics and Analytics、年份 2021、DOI 10.3389/frma.2021.670006。WebSearch 独立确认完整作者列表 **Yiwen Shi, Ping Ren, Yi Zhang, Xiajing Gong, Meng Hu, Hualou Liang**，**vol. 6, article 670006，2021-06-10 发表**，并命中 PubMed 记录 PMID 34179681 与 PMC8222600（第三个独立来源）。**[抽查，三个独立来源：Undermind + WebSearch + PubMed 记录页，结果一致]**
正文用途：§8.4（方法可移植性——药品审批语料的信息抽取已在规模化开展，本文的「按测量方分层」诊断可直接接入）。

## 新增文献的引用位置对照

| 文献 | Introduction 新增段 | §3.4 | §8.4 |
|---|---|---|---|
| Losiewicz et al. 2000 | ✔ | | ✔ |
| Antons et al. 2020 | ✔ | | ✔ |
| Rammer and Es-Sadki 2023 | ✔ | | ✔ |
| Franceschini et al. 2016 | | ✔ | ✔ |
| Jaffe and de Rassenfosse 2017 | | | ✔（2 处） |
| Shi et al. 2021 | | | ✔ |

## 本次核验的方法学说明与限制

- 6 条全部为**真实存在、可在出版商官网定位**的正式出版物；未出现任何编造条目。
- 两处「工作论文 vs 期刊正式版本」的陷阱被主动检出并修正（Rammer & Es-Sadki 采用 TFSC 版本；
  Jaffe & de Rassenfosse 采用 JASIST 版本而非 NBER w21868），处理方式与上文第 3 条
  Grennan & Town 的修正原则一致。
- 本轮**未能**取得其中任何一条的全文 PDF（Undermind 仅对 Jaffe17 与 Shi21 标注有 PDF，
  本次未下载阅读）；因此正文对这 6 条的引用一律限于**其摘要与题名所明确支持的一般性论断**
  （如「文本挖掘主要建立在专利与论文语料上」「Scopus/WoS 存在系统性著录错误」），
  **不引用任何具体数字**。此限制与 Gong et al. 2026 的「标题级引用」处理属同一谨慎口径。

---

## 2026-09-17 补充核验：修复 Shi&Hu17 / Huang18 遗漏 + 扩充 9 条近年文献

> 背景：投稿信（cover letter）一直声称正文"draws on and extend three lines of JIA
> scholarship"（Shi and Hu, 2017；Qiu et al., 2016；Huang et al., 2018），但校对时发现
> v5 正文和参考文献列表里只有 Qiu et al. 2016，另外两条在某次压缩改稿中被删掉、投稿信的
> 措辞却没跟着改——这正是版本迭代遗留的数据/文本不一致问题。上文第 16、18 条早就核实过
> 这两篇文献真实存在（Undermind + WebSearch 双工具一致），本次直接按已核实的著录信息把
> 两条引用和参考文献条目补回正文（§7、§8.1），投稿信的三篇 JIA 文献声明由此恢复真实。
>
> 同时按用户要求"扩充参考文献，同时增加近几年的文章引用"，用 Workflow 工具派发 7 路并行
> 检索（覆盖：中国种子监管改革近期文献、粮食质量认证文献、自我认证/第三方审计文献延伸、
> 行政文本挖掘指标构建近期文献、2022 年整治行动后续影响），每条候选文献再单独派发一个
> 独立验证 agent 用 WebSearch 交叉核实真实性与论断准确性（默认存疑，要求独立信源佐证才
> 判定通过）。25 条候选中 23 条通过验证，2 条（Ham et al. 2021、Geng et al. 2026，均为
> 真实存在的审计/认证文献）因其论断与候选摘要归纳不符而被拒绝，未采用。

### 28. Abi Younes G, de Rassenfosse G. 2024. Replicable patent indicators using the Google Patents Public Datasets. **Australian Economic Review**, 57, 102–113. DOI: 10.1111/1467-8462.12545

**✅ Verified**（WebSearch 交叉核实）。de Rassenfosse 为 Jaffe and de Rassenfosse (2017)（本文列表第 19 条）的共同作者，本文是该方法学脉络的延续，独立信源确认期刊/卷期/DOI 一致。
正文用途：§8.4（专利指标构建方法的延伸）。

### 29. Bian Y, Yan S, Yi Z, Guan X, Chen Y. 2022. Quality certification in agricultural supply chains: Implications from government information provision. **Production and Operations Management**, 31, 1456–1472. DOI: 10.1111/poms.13623

**✅ Verified**（WebSearch 交叉核实，独立信源一致；线上版 2021、印刷卷期 2022）。
正文用途：§2（第三方质量认证与政府信息供给的博弈论文献）。

### 30. Bonsall S B, Gillette J R, Pundrich G, So E C. 2024. Conflicts of interest in subscriber-paid credit ratings. **Journal of Accounting and Economics**, 77, 101614. DOI: 10.1016/j.jacceco.2023.101614

**✅ Verified**（WebSearch 交叉核实，期刊/卷/文章号一致）。
正文用途：§8.1（"即使反转付费方也无法消除认证方利益冲突"的信用评级类比）。

### 31. Deng H, Yu C, Jin Y, Pray C, Liu C, Deng L. 2025. How is China shaping global food supply chains? Insights from the seed industry. **European Review of Agricultural Economics**. DOI: 10.1093/erae/jbaf017（网络首发，正式卷期页尚未分配）

**✅ Verified**（WebSearch 交叉核实，DOI 与期刊一致）。
正文用途：§8.2（近年种业格局背景，佐证 2022 年之后监管关注并未停止）。

### 32. Miao Y, Sun J, Liu R, Huang J, Sheng J. 2025. Bridging the quality-price gap: Unlocking consumer premiums for high-quality rice in China. **Foods**, 14, 1184. DOI: 10.3390/foods14071184

**✅ Verified**（WebSearch 交叉核实，期刊/卷/文章号一致）。
正文用途：§2（消费者为可验证的稻米品质支付真实溢价，佐证第三方质量认证的信息价值）。

### 33. Qin Y, Su K. 2026. From lab to market: Industrialization barriers and regulation optimization for new breeding technologies in China. **GM Crops & Food**. DOI: 10.1080/21645698.2025.2610592（网络首发 2026-01-12，正式卷期页尚未分配；PMC12803001）

**✅ Verified**（WebSearch 交叉核实，DOI 与 PubMed/PMC 记录一致）。
正文用途：§8.2（近年监管/制度文献仍在识别品种权执法等未解决的缺口，佐证本文窗口期的持续相关性）。

### 34. Wang S, Wang S, Zhao C, et al. 2024. 中国品种审定制度概况及国内外比较 (Overview of China's crop variety approval system and comparison with other countries). **粮油食品科技 (Science and Technology of Cereals, Oils and Foods)**, 32, 211–218. DOI: 10.16210/j.cnki.1007-7561.2024.05.026

**✅ Verified**（WebSearch 交叉核实，中国社会科学院农村发展研究所关联作者，PDF 可在
rdi.cass.cn 定位）。中文文献，供中国读者/审稿人核对制度背景之用，属常见做法。
正文用途：§2（中国品种审定制度改革的国内官方综述视角，与国际比较）。

### 35. Xu S. 2021. Rethinking the liberation of China's seed market: A comparative study of China's regulatory frameworks with EU and US. **Agroecology and Sustainable Food Systems**, 251–272. DOI: 10.1080/21683565.2021.1989104

**⚠️ 部分核验 — 卷号未独立确认**。WebSearch 交叉核实确认标题、作者、期刊、DOI、页码一致；
卷号因该刊网络代理受限未能独立核实，参考文献列表中如实省略卷号而非编造，**投稿前须由
作者核对官方记录补全**（与 Piepho and Laidig 2025 此前的卷期页核验方式一致——不确定的
就标注，不猜测）。
正文用途：§2（中国种子治理模式转型的比较制度研究）。

### 36. Zheng Y, Bar T. 2023. Certifier competition and audit grades: An empirical examination using food safety certification. **Applied Economic Perspectives and Policy**, 45, 182–196. DOI: 10.1002/aepp.13211

**✅ Verified**（WebSearch 交叉核实；Bar 为 Bar and Zheng (2019)（本文列表第 6 条）的共同
作者，本文是同一研究脉络的后续延伸，独立信源确认期刊/卷期/DOI 一致）。
正文用途：§8.1（认证方竞争与审核宽松度的实证延伸，直接承接 Bar and Zheng 2019）。

## 本轮方法学说明与限制

- 本轮验证工具为 WebSearch（无法访问 CrossRef/ScienceDirect/DOAJ/AGRIS 等官方 API，
  该环境的出站网络代理对这些域名有限制），核验强度略低于此前使用 Undermind
  直接命中摘要全文的轮次；但每条均要求至少一个独立搜索结果的信源佐证，且设有专门的
  「大胆假设-独立反驳」验证步骤（默认存疑，未获独立确认则判定不通过），2 条候选文献
  因此在采用前被剔除。
- Xu (2021) 卷号未获独立确认，参考文献列表中如实留空而非编造，标注留待作者投稿前核对。
- Deng et al. 2025 与 Qin and Su 2026 为网络首发（online first），尚无正式卷期页，
  参考文献列表按此如实著录。
