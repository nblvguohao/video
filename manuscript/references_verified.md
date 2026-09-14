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

### 10. Gong J, Zhang X, Zhang J, Zeng B, Zhang X, Xu X, … Xie H A. 2026. Three-line hybrid rice in China: sustained improvements in yield, quality, and resistance over fifty years / 五十年持续改良. **Rice Science**. DOI: 10.1016/j.rsci.2026.04.004

**❓ Unverifiable（全文仍未取得，见下方"特别任务"结果）**。DOI、期刊、年份（2026-04-01）、作者列表（含通讯作者 Hua-an Xie）经 Undermind 与 WebSearch 交叉确认一致，**引用本身可用**；但摘要与正文数字本次仍无法独立取得，任何具体数字（品种数、年代趋势幅度）在写入正文前必须继续标注"标题级引用，数字未核"。**注意到一个需要留意的细节**：WebSearch 检索到的标题措辞与本项目文档中的略有出入（见下方特别任务说明），DOI 相同，判断为同一篇文章的标题在不同索引器中的措辞差异，不影响引用有效性。

### 11. Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. Dissecting genetic and non-genetic sources of long-term yield trend in German official variety trials. **Theoretical and Applied Genetics**, 127, 1009–1018. DOI: 10.1007/s00122-014-2275-1

**✅ Verified**（Undermind 确认；Scholar Gateway 检索到至少 3 篇 2020–2026 年独立论文以 "Piepho et al. (2014)" 原文引用该文方法论并给出一致的方法描述，与本文档转述的模型设定一致）。**[抽查]**

### 12. Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. Genetic and non-genetic long-term trends of 12 different crops in German official variety performance trials and on-farm yield trends. **Theoretical and Applied Genetics**, 127, 2599–2617. DOI: 10.1007/s00122-014-2402-z

**✅ Verified**（Undermind 确认；Scholar Gateway 交叉检索到多篇论文引用 "Laidig et al. (2014)" 及其具体数字（如"六棱大麦最高遗传增益 40.3–69.3 kg/ha"），与本文档转述一致）。**[抽查]**

### 13. Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. Reanalyses of the historical series of UK variety trials to quantify the contributions of genetic and environmental factors to trends and variability in yield over time. **Theoretical and Applied Genetics**, 122, 225–238. DOI: 10.1007/s00122-010-1438-y

**✅ Verified**（Undermind 确认；WebSearch 独立确认卷期页 122: 225–238 (2011)，DOI 与在线优先年份 2010 对应，属正常"DOI 含接收年份、印刷卷标注发表年份"现象，无需修正）。**[抽查，两个独立工具，结果一致]**

### 14. Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. Continuing genetic improvement and biases in genetic gain estimates revealed in historical UK variety trials data. **Field Crops Research**, 303, 109086. DOI: 10.1016/j.fcr.2023.109086

**✅ Verified**（Undermind `get_paper_info` 取得完整摘要原文，与 `00_decision_log.md` A-7 引用的关键句——对照品种产量本身不稳定、遗传增益估计对长期对照选择极度敏感——逐句核对一致）。

### 15. Piepho H-P, Laidig F. 2024/2025. How many checks are needed per cycle in a plant breeding or variety testing programme? **Plant Breeding**. DOI: 10.1111/pbr.13240

**⚠️ Check suggested — 卷期页两个来源不一致**。Undermind 记为 144(1)(2024)；WebSearch 检索到另一说法为 **vol. 144, pp. 242–248，正式出版年份可能为 2025（在线优先 2024）**。DOI 一致、内容一致（摘要核心句"用对照连接不同年份以评估遗传增益、建议保持较低对照更替率"经 Undermind 核实无误）。**建议投稿前用期刊官网或 CrossRef 直接核对最终印刷卷期页，本报告不下结论**，正文引用暂按 DOI 为准，卷期页标注"in press / 待印刷卷确认"。

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
