# 参考文献核验 — manuscript_v1.md References vs references_verified.md

审查日期：2026-09-14｜审查员：格式与数字一致性审查员

## 1. 正文引用标记 ↔ 参考文献列表 双向核对

### 1a. 正文每个 (Author, Year) 标记是否在列表中有对应条目

全文提取到 11 个不同的引用（去重后）：

| 正文引用 | 参考文献列表中对应条目 | 存在 |
|---|---|---|
| Bar and Zheng (2019) | Bar T, Zheng Y. 2019. ...AJAE, 101, 74–88. | ✅ |
| Duflo et al. (2013) | Duflo E, Greenstone M, Pande R, Ryan N. 2013. ...QJE, 128, 1499–1545. | ✅ |
| Grennan and Town (2020) | Grennan M, Town R J. 2020. ...AER, 110, 120–161. | ✅ |
| Laidig et al. (2014) | Laidig F, Piepho H-P, Drobek T, Meyer U. 2014. ...TAG, 127, 2599–2617. | ✅ |
| Mackay et al. (2011) | Mackay I, Horwell A, Garner J, White J, McKee J, Philpott H. 2011. ...TAG, 122, 225–238. | ✅ |
| Piepho and Laidig (2024) | Piepho H-P, Laidig F. 2024. ...Plant Breeding. | ✅（但卷期页缺失，见 format_check.md #34） |
| Piepho et al. (2014) | Piepho H-P, Laidig F, Drobek T, Meyer U. 2014. ...TAG, 127, 1009–1018. | ✅ |
| Raymond et al. (2023) | Raymond J, Mackay I, Penfield S, Lovett A, Philpott H, Dorling S. 2023. ...Field Crops Research, 303, 109086. | ✅ |
| Renckens and Auld (2022) | Renckens S, Auld G. 2022. ...Regulation & Governance, 16, 500–518. | ✅ |
| Xiang et al. (2025) | Xiang C, Yang R, Wang X, Huang J. 2025. ...Agribusiness. | ✅（卷期页待定，在线优先） |
| Zhao et al. (2022) | Zhao Y, Deng H, Hu R, Xiong C. 2022. ...Agronomy, 12, 917. | ✅ |

**全部 11 个正文引用标记都能在参考文献列表中找到对应条目，无"引用了但列表中缺失"的情况。**

### 1b. 参考文献列表每条是否被正文引用（JIA 规范：未引用应删除）

参考文献列表共 11 条，逐条核对：**全部 11 条均在正文中被引用**（见上表反向对照），**没有列表中存在但正文未引用的"僵尸条目"**。这一点符合 JIA "不得放置未引用文献"的规范。

## 2. integration_log.md 提到的 10 篇"从未被引用"文献 — 独立核实

`integration_log.md` §8 声称：`04_format_spec.md` §6 的必引清单中有 10 篇——Xie et al. (2023)、Lu et al. (2024)、Hang et al. (2024)、Gong et al. (2026)、Shi and Hu (2017)、Qiu et al. (2016)、Huang et al. (2018)、Seck et al. (2023)、Burris et al. (2025)、Rangnekar (2000)——虽然在 `references_verified.md` 中被核实为真实、可引用的文献，但从未在 12 份分节草稿正文中被引用过。

**独立核实结果：属实。** 对 manuscript_v1.md 全文做逐词搜索，确认：

| 文献 | 正文中出现（任意形式：作者名、年份、标题片段） | 参考文献列表中出现 |
|---|---|---|
| Xie Z et al. 2023 (Agribusiness, contract farming) | ❌ 未出现 | ❌ 未出现 |
| Lu Y et al. 2024 (Agronomy, 品质性状变化 1978-2022) | ❌ 未出现 | ❌ 未出现 |
| Hang S et al. 2024 (Agronomy, 品种表现演变 30年) | ❌ 未出现 | ❌ 未出现 |
| Gong J et al. 2026 (Rice Science, 三系杂交稻50年改良) | ❌ 未出现 | ❌ 未出现 |
| Shi X, Hu R 2017 (JIA, 外来种质贡献) | ❌ 未出现 | ❌ 未出现 |
| Qiu H G et al. 2016 (JIA, 农户信息不对称种子选择) | ❌ 未出现 | ❌ 未出现 |
| Huang Z Y et al. 2018 (JIA, 合同养殖) | ❌ 未出现 | ❌ 未出现 |
| Seck F et al. 2023 (Rice, 育种项目实现遗传增益) | ❌ 未出现 | ❌ 未出现 |
| Burris L et al. 2025 (npj Science of Plants, 公私育种分化) | ❌ 未出现 | ❌ 未出现 |
| Rangnekar D 2000 (计划报废与英国小麦育种) | ❌ 未出现 | ❌ 未出现 |

**结论：这 10 篇确实既不在正文中，也（正确地）不在参考文献列表中——这符合"未引用文献不应列入参考文献列表"的 JIA 规范本身，integration_log.md 在这一步的处理（不强行塞入列表）是对的。** 但这只解决了"列表格式是否干净"的问题，没有解决更根本的问题（见第 3 节）。

## 3. 这是否说明存在实质性内容缺口？—— 是，需要退回撰写阶段

对这 10 篇文献的主题与本文相关章节做了逐一比对，发现其中至少 6 篇与本文论证直接相关，缺席造成了可识别的论证/文献对话缺口，而不仅仅是"漏引用"：

| 文献 | 主题 | 本应对话的章节 | 缺口性质 |
|---|---|---|---|
| **Lu et al. 2024** | 1978–2022 中国审定品种品质性状的分类变化趋势（17,785个品种） | §5.6（结构断点：head-rice 2015年断点、chalkiness 2009年断点）、§8.2（讨论"the identified variation disappearing?"） | 本文自己发现并强调"品质性状的结构性断点早于2016年改革"，这正是 Lu et al. (2024) 研究的同一现象（品质性状的长期趋势），但正文完全没有与之对话，是**实质性文献对话缺失**，不是格式问题 |
| **Hang et al. 2024** | 1990–2023 全国品种产量与农艺性状演变（11,811次试验） | §5.6、§6.14（chained-check遗传增益分析） | 同上，本文用国外（德国/英国）遗传增益文献（Piepho, Laidig, Mackay, Raymond）做方法论支撑，却未引用同类的**中国水稻**长期趋势研究，是方法论对话的明显缺口 |
| **Gong et al. 2026** | 三系杂交稻50年持续改良（产量、品质、抗性） | §1 Introduction（本文杂交稻背景）、§5.6 | 虽仍是"标题级引用"（全文未核实），但其主题与本文核心问题（品质与产量性状的长期演变）高度相关，是背景文献的缺口 |
| **Qiu et al. 2016** | 信息不对称下农户种子选择行为 | §8.1（自我认证文献综述）、Discussion 关于"measurement discretion" | 本文核心论点是"谁测量什么"影响市场信息，Qiu et al. 讨论的正是种子市场中的信息不对称问题，是最贴近本文理论框架但缺失的一篇，属**实质性理论对话缺口** |
| **Xie et al. 2023** | 种子企业主导的合同种植与品质激励设计 | §7 Mechanism（荃银订单粮食业务） | 本文第7节详细讨论荃银的"订单粮食"业务及其财务困境，Xie et al. (2023) 恰是研究"种子企业主导合同种植品质激励"的论文（且 `table6_company_panel.csv` 的数据来源之一还援引了 Xie et al. 2023 的荃银订单粮食毛利率数据！），却在正文中完全没有被引用或讨论，是**证据链断裂**：数据用了这篇文献的数字，正文却不引用这篇文献 |
| **Shi and Hu 2017 / Huang et al. 2018 / Seck et al. 2023 / Burris et al. 2025 / Rangnekar 2000** | 分别为外来种质贡献、合同养殖、水稻遗传增益、公私育种分化、计划报废式育种 | Introduction/Discussion 背景铺垫 | 相关性略弱于上述5篇，但仍属于"必引清单"圈定的背景文献，缺席会削弱 Introduction 对研究背景的完整性 |

**特别值得指出的证据链问题**：`manuscript/tables/table6_company_panel.csv` 中 2018/2021 年荃银订单粮食毛利率和占比数据的备注明确写着"来自Xie et al. 2023 Agribusiness"，也就是说**论文的 Table 6 数据事实上依赖 Xie et al. (2023) 作为一手数据来源**，但正文引用列表里完全没有这篇文献——这不只是"该引未引"的遗漏，而是**数据溯源链条不完整**：读者无法从正文追溯到 Table 6 中部分数字的真实出处。这一条建议单独标记为高优先级修复项。

**判断：这不只是参考文献列表的格式问题，而是需要退回撰写阶段补写的内容缺口。** 具体建议：
1. **Table 6 数据来源引用（高优先级/阻塞性）**：§7 Mechanism 中凡是引用了源自 Xie et al. (2023) 的荃银订单粮食数字（毛利率、占比），必须显式标注 "(Xie et al., 2023)"，否则构成数据溯源缺失，这在同行评审中很可能被要求补充说明数据出处。
2. **§5.6/§8.2 结构断点与品质长期趋势讨论**：建议补写 1-2 句，将 Lu et al. (2024) 与 Hang et al. (2024) 的中国全国性长期趋势证据与本文的断点发现相联系（例如比较断点年份是否与其报告的性状拐点吻合）。
3. **§8.1 自我认证文献综述**：建议补写一句将 Qiu et al. (2016) 的信息不对称框架纳入讨论，加强本文"谁测量"论点的理论定位。
4. 其余 4 篇（Shi&Hu17、Huang18、Seck23、Burris25、Rangnekar00）以及 Gong et al. (2026)（仍待取得全文）优先级较低，可视撰写篇幅约束选择性补写，但若最终仍不引用，则应从 `04_format_spec.md` §6 的"必引清单"中正式移除，避免清单本身长期挂着无法兑现的承诺。

这些改动涉及新增论证句子，超出了"参考文献核验/格式核验"的职责范围，**建议将 items 2-3（Lu/Hang/Gong 断点讨论、Qiu 信息不对称理论对话）作为独立任务退回给撰写阶段（Introduction 或 Discussion 的补写任务），而不是由本次核验直接代写。**

## 4. 参考文献格式复核（与 references_verified.md 交叉，聚焦是否已应用其建议的修正）

| # | 文献 | references_verified.md 建议 | manuscript_v1.md 实际状态 | 已应用 |
|---|---|---|---|---|
| 1 | Bar & Zheng | 2019, 101(1):74–88 | "Bar T, Zheng Y. 2019. ...101, 74–88." | ✅ 已应用 |
| 2 | Renckens & Auld | 2022, 16(2):500–518 | "Renckens S, Auld G. 2022. ...16, 500–518." | ✅ 已应用 |
| 3 | Grennan & Town | DOI改为期刊正式版（正文不含DOI，无法核对，但卷期页110,120–161已正确） | "Grennan M, Town R J. 2020. ...110, 120–161."（无DOI字段可查） | ✅ 卷期页已正确；DOI字段本身在参考文献列表中未出现（见format_check.md #33，DOI为可选项） |
| 4 | Piepho & Laidig 2024 | 卷期页存疑，投稿前需用CrossRef核对，暂不下结论 | "Piepho H-P, Laidig F. 2024. ...Plant Breeding."（无卷期页） | ⚠️ 待定，与核验报告的"不下结论"状态一致，非本次核验范围内可解决的问题 |
| 5 | Gong et al. 2026 | 继续标注"标题级引用，正文不得引用具体数字" | 全文未引用此文献（见第2节） | 不适用（因为根本没引用，谈不上违反"不得引用具体数字"的限制） |

## 5. 汇总

- **格式层面 issue：0 条**（正文引用与列表严格一一对应，无孤立引用、无未引用条目残留在列表中）
- **内容缺口 issue：6 条**（Lu24、Hang24、Gong26、Qiu16、Xie23 五篇的实质性缺席，以及 Table 6 数据溯源链条断裂这一项衍生问题）
- **格式细节遗留 issue：1 条**（Piepho & Laidig 2024 卷期页仍待 CrossRef 核对，非本次可解决）

**最严重的三条：**
1. **Table 6（荃银财务面板）部分数据点明确注明来自 Xie et al. (2023)，但该文献从未出现在正文引用或参考文献列表中——这是数据溯源链条的断裂，建议列为投稿前的阻塞项，需要在 §7 补一处显式引用。**
2. **§5.6/§8.2 关于品质性状长期趋势和结构断点的讨论，完全没有与同主题的中国水稻长期趋势文献（Lu et al. 2024、Hang et al. 2024）对话，只引用了德国/英国的遗传增益方法论文献——这是实质性的文献综述缺口，需要退回 Introduction/Discussion 撰写阶段补写，而不是简单地在参考文献列表里加几行。**
3. **§8.1 自我认证文献综述未纳入 Qiu et al. (2016) 的信息不对称理论框架，是本文核心论证（"谁测量什么"）最贴近的理论对话对象之一，缺席削弱了理论定位的完整性，同样建议退回撰写阶段处理。**
