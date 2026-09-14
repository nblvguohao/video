# 格式合规审查 — manuscript_v1.md vs 04_format_spec.md

审查日期：2026-09-14｜审查员：格式与数字一致性审查员
方法：逐条对照 `plan/04_format_spec.md`，用 grep/awk/python 对 `manuscript_v1.md` 做字符/字数统计，人工核对结构与措辞。

| # | 条目 | 要求（04_format_spec.md） | 现状 | 合规 | 修正建议 |
|---|---|---|---|---|---|
| 1 | 文章类型 | Research Article | 未标注文章类型字段，但结构符合 | ⚠️ 部分 | 投稿模板/系统字段中需显式选择 "Research Article"（正文本身不必声明，非阻塞项） |
| 2 | 章节顺序 | Intro→Institutional background→Data→Empirical strategy→Results→Robustness→Mechanism→Discussion→Conclusion→Ack→COI→Data availability→CRediT→References | 实际顺序：1 Intro, 2 Institutional background, 3 Data, 4 Empirical strategy, 5 Results, 6 Robustness, 7 Mechanism, 8 Discussion, 9 Conclusion, Acknowledgements, Conflict of interest, Data availability statement, CRediT, **Ethical approval**, References | ⚠️ 基本合规，一处顺序偏差 | `Ethical approval` 被放在 CRediT 之后、References 之前；官方顺序（spec 第9行）是 "...Conflict of interest → Ethical approval → References"，且 spec 第10行给出的本文 9+4 节声明顺序是 Ack/COI/Data availability/CRediT（未含 Ethical approval 位置）。建议将 Ethical approval 移到 Conflict of interest 之后、Data availability statement 之前，以贴合官方模板顺序 |
| 3 | 字数 | 8,000–10,000 词（经验值，含摘要与参考文献列表之外正文） | 实测正文（不含 References）约 **14,563 词**，超出上限约 45%–82% | ❌ 不合规 | 需大幅删减；`integration_log.md` §12 已自行标记此项未处理。建议优先精简 Robustness 15 项检查的完整展开、§4.1 的两个被拒 DID 设计描述 |
| 4 | 标题 | 用 gap 而非 effect/impact/caused by；third-party-assayed 限定范围 | 标题为 "Who measures what enters the market? Self-organised variety trials and the third-party-assayed grain-quality gap..." | ✅ 合规 | 无 |
| 5 | 摘要结构与字数 | 结构式，≤250 词 | 实测 **249 词**（草稿要求投稿前删到 246 词以内的目标未达成，但仍 ≤250 硬性上限） | ✅ 合规（硬指标）／⚠️ 未达内部目标 246 词 | 若要严格执行 04 文件里写的"目标 246 词以内"，需再删 3 词以上；否则仅需满足期刊 ≤250 硬性要求即可，无需改 |
| 6 | 关键词数量 | 3–6 个，避免含 and/of 的多词短语 | 6 个：variety approval; third-party certification; self-organised trials; rice quality; seed regulation; China | ✅ 合规 | 无 |
| 7 | Highlights 数量 | 3–5 条 | 5 条 | ✅ 合规 | 无 |
| 8 | Highlights 长度 | 每条 ≤85 字符（含空格） | 逐条字符数（`awk`/python len）：79 / 71 / 78 / 77 / 83 | ✅ 全部合规 | 无 |
| 9 | 估计量表述禁用词 | 禁止 effect of / caused by / impact of 描述因果 | 全文搜索到的 "effect of" 用例均出现在否定句或统计学 MDE 语境中（"not the effect of...", "do not estimate...a causal effect", "MDE... against a national effect of X pp"），未见违规的因果断言用法 | ✅ 合规 | 无 |
| 10 | 禁用词（造假/操纵） | 不出现 fraud/manipulation | 第 367 行使用 "fabricated or manipulated"（否定句），第 370 行**直接引用了** "fraud" 和 "manipulation" 两个词本身（作为元陈述："words such as 'fraud' or 'manipulation' do not appear"），第 606 行使用 "fabrication or manipulation"（否定句） | ⚠️ 边界情形 | 三处均为否定/元陈述而非坐实指控，语义上合规；但字面上 "fraud"、"manipulation"、"fabricated"、"manipulated"、"fabrication" 确实作为词汇出现在正文中。若审稿人/编辑对"不出现"做字面理解，建议将第 370 行改写为不直接引用这两个词（如："this paper does not use language alleging deliberate misconduct"），以避免争议 |
| 11 | 荃银篇幅 ≤15% | Winall 段落不超过全文 15% | 第 7 节（Mechanism）实测 937 词 / 全文 14,563 词 = **6.43%** | ✅ 合规，且留有余量 | 无 |
| 12 | 荃银正/负面须同段呈现 | 每次正面表述须同段/紧邻段落给出负毛利/2025转亏/2024保留意见/2026罚款ST | 第 566 段（financial facts）确实包含：2.66%→−0.09%→−1.31% 毛利率、2025 净利润 −212M（同比 −317.91%）、2024 年报保留意见、2026 罚款 30 万元、ST Winall；且该段紧接第 564 段的正面结果（渠道选择、内部业绩优势） | ✅ 合规 | 无 |
| 13 | 禁止收益折算 | 不把系数换算为企业收益/加工价值 | 第 566 段末尾明确声明 "does not convert the quality-grade coefficients above into any implied revenue, processing value, or cost saving" | ✅ 合规 | 无 |
| 14 | 禁止排序修辞 | 不写"按一体化深度排序" | 全文搜索未命中类似表述；第 572 段明确声明本节不对"整合程度排序"做任何断言 | ✅ 合规 | 无 |
| 15 | Non-claims 独立小节 | 须作为独立小节写入第4节末 | §4.7 "What this paper does not claim"，位于 Empirical strategy 节末尾，12 条逐一编号（First…Finally），与 `01_theme_and_innovation.md` §8 的 12 条基本对应 | ✅ 合规 | 无 |
| 16 | CF1–CF8 冲突证据登记 | 全部须如实呈现在正文 | 逐条核对：CF1（白叶枯更优）✅ Arm1 −0.190 在 §5.2/Table3；Arm2 −0.562 仅见于 Table 3，正文未单独提及数值（Discussion 第606行有笼统提及"disease-resistance grading moves the other way"）——⚠️部分；CF2（绿色通道生产试验增产更低）✅ §5.3；CF3（绿色通道区试增产不可估计）✅ §5.3；CF4（米质1/2级 Manski 符号不稳）✅ §6.6；CF5（组内检验多反号）✅ §6.10（但具体数值用了本次实跑的 +0.780 而非旧版 +3.68，见 number_consistency.md）；CF6（省审复制不显著）✅ §6.11/§8.2；CF7（株高安慰剂显著，移出安慰剂集合）✅ §6.8；CF8（"载明米质等级"是缺失指示）✅ §3.3 | ⚠️ 基本合规，CF1 的 Arm2 数值未在正文散文中单独点出 | 建议在 §5.3 或 Discussion 中补一句明确给出 Arm2 白叶枯病系数 −0.562（p=0.074, n=82），使 CF1 的两臂数值都在正文散文中出现，不仅停留在 Table 3 |
| 17 | 图表编号连续、首次提及顺序与编号一致 | 编号连续，正文首次提及顺序须与编号顺序一致 | 实测 Fig.1(L108)→Fig.2(L444)→Fig.3(L466)→Fig.4(L470)→Fig.5(L504)→Fig.6(L508)→Fig.7(L564)，Table 1(L109/180)→2(L182)→3(L184)→4(L554)→5(L564)→6(L566)→7(L570)，全部严格递增 | ✅ 合规 | 无 |
| 18 | 图表编号是否与 figure_table_list.md 一致 | 二者需一致 | Fig/Table 内容、来源文件、首引位置与 `figure_table_list.md` 完全一致（含 integration_log.md §2 的重编号说明） | ✅ 合规 | 无 |
| 19 | 投稿压缩至 6 图 5 表 | 04_format_spec.md §5：投稿时应压缩至正文 6 图 5 表 | manuscript_v1.md 正文实际引用 **7 图 7 表**（Fig.1–7、Table1–7），未压缩；`figure_table_list.md` 自身也承认 "7 main-text figures above the stated 6-figure target" 且 "9→6 by removing only 2 数字不闭合"，未指定砍哪一表 | ❌ 不合规（已知未决项） | 需作者团队在投稿前决定：从 Fig.1–7 中选 1 幅移入 Supplementary（`figure_table_list.md` 建议候选：并入 Fig.3 到 Fig.2，或将 Fig.6 缺失性哑铃图移为纯表格呈现）；并从 Table1–7 中选 2 张移入 Supplementary（无现成候选，需作者决定） |
| 20 | 图片格式 | 不接受 GIF/BMP/PICT/WPG 等 | 实际文件均为 .png/.pdf（`ls manuscript/figures/`） | ✅ 合规 | 无 |
| 21 | 非线性调整须图注声明 | gamma 校正等须声明 | 未见任何图注涉及非线性变换，图表也未使用 log/gamma 轴（森林图为线性 β 轴） | ✅ 不适用/合规 | 无 |
| 22 | 中文标签不用于图内 | 图内标签统一英文 | Fig.2（已读取）标签全为英文；其余图未逐一渲染核查，但 caption 文字（figure_table_list.md）均为英文 | ✅ 合规（抽查 Fig.2） | 建议投稿前逐一截图核对 Fig.1/3/4/5/6/7 图内标签是否全英文（本次仅核查了 Fig.2） |
| 23 | 单位：产量 kg/亩，首次出现括注 kg/hm² | 首次出现需换算括注 | 全文出现 "kg/mu" 多处（如 L413, L450, L508, L512, L570），**全文未出现任何 "kg/hm²" 或 1/15 换算括注** | ❌ 不合规 | 需在首次出现 kg/mu 处（§3 Data 或 §5.2 首次出现，如 L450）补充 "(1 kg/mu ≈ 15 kg/hm²)" 或等效括注 |
| 24 | 百分比性状统一用 pp | 组间差异统一用 percentage points (pp) | 全文一致使用 "percentage points (pp)"／"pp"（如 head-rice, chalkiness, quality_stated 等），未见与"相对百分比变化"混淆的用法 | ✅ 合规 | 无 |
| 25 | 统计量报告：点估计+95%CI+p值；多重比较报 BH-FDR q 值；聚类标准误注明聚类层级与聚类数 | 见左 | 主表结果普遍报告 β/95% CI/p（如 L448, L450）；§6.4 报告 BH-q 值；聚类层级与聚类数在正文（"cluster(cell,G=10)"，Table3）与 §4.3（"clustered at the level of c when an arm has at least five effective clusters"）中均说明 | ✅ 合规 | 无 |
| 26 | 显著性不得只用星号系统，须报告精确 p 值 | 见左 | 全文均以 "p = 0.XXX" / "p < 0.0001" 形式报告，未见星号系统 | ✅ 合规 | 无 |
| 27 | 声明部分：Acknowledgements | 占位，投稿前补充 | 存在，占位符 "[Author to complete...]" | ✅ 合规（占位符待填） | 投稿前补充实际内容 |
| 28 | 声明部分：Conflict of interest | 必须声明，无冲突需写明确句 | "The authors declare no conflict of interest." | ✅ 合规 | 无 |
| 29 | 声明部分：Data availability statement | 措辞须符合 K11（只公开脚本/字段字典/记录ID，不分发数据表） | 与 spec 提供的示例措辞逐句一致 | ✅ 合规 | `[repository link]` 占位符投稿前需替换为真实仓库链接 |
| 30 | 声明部分：CRediT | 占位，按 CRediT 体系填写 | 存在，9 类角色全部列出且均为占位符 | ✅ 合规（占位符待填） | 投稿前补充作者姓名 |
| 31 | 声明部分：Ethical approval | 不涉及人类/动物实验可写 Not applicable | "Not applicable. This study did not involve human participants or animal experiments..." | ✅ 内容合规／⚠️ 位置见条目2 | 无（内容层面），位置建议见条目2 |
| 32 | 参考文献体系：author-date | (Author, Year) 或 Author (Year)；三位以上用 et al. | 全文 11 处引用均符合此格式（Bar and Zheng (2019)/Duflo et al. (2013) 等） | ✅ 合规 | 无 |
| 33 | 参考文献列表：字母顺序，期刊全称，鼓励附 DOI | 见左 | 11 条按姓氏字母序排列（Bar→Duflo→Grennan→Laidig→Mackay→Piepho(2024)→Piepho et al.(2014)→Raymond→Renckens→Xiang→Zhao），期刊名均为全称；**全部未附 DOI**（DOI 为"鼓励"非强制） | ✅ 基本合规 | DOI 为软性建议，可选择性补充以提高检索便利性，非阻塞项 |
| 34 | 参考文献官方示例格式核对 | "Chen W F, Xu Z J, Zhang L B..." 格式 | 抽查全部 11 条，姓氏+空格分隔名字缩写、年份、题名、期刊全称、卷、页码格式基本一致；但 **Piepho H-P, Laidig F. 2024. ...Plant Breeding.**（无卷期页）与 **Xiang C, Yang R, Wang X, Huang J. 2025. ...Agribusiness.**（无卷期页）两条缺失卷/期/页码 | ⚠️ 部分不合规 | 这两条均为在线优先出版、正式印刷卷期尚未确定（`references_verified.md` 已标注），投稿前需按 CrossRef/期刊官网核对最终印刷卷期页并补全，否则不符合官方格式要求 |
| 35 | 必引文献清单（04_format_spec.md §6 十篇特定文献） | Duflo13/Bar&Zheng18/Grennan20/Renckens20/Xiang25/Zhao22/Xie23/Lu24/Hang24/Gong26/Piepho14/Laidig14/Mackay11/Raymond23/Piepho&Laidig24/Shi&Hu17/Qiu16/Huang18/Seck23/Burris25/Rangnekar00 全部须引用 | 参考文献列表与正文实际只包含 **11 篇**（Bar&Zheng19, Duflo13, Grennan20, Laidig14, Mackay11, Piepho&Laidig24, Piepho14, Raymond23, Renckens&Auld22, Xiang25, Zhao22）；清单中另外 **10 篇**（Xie23, Lu24, Hang24, Gong26, Shi&Hu17, Qiu16, Huang18, Seck23, Burris25, Rangnekar00）**完全未出现**在正文或参考文献列表中 | ❌ 不合规 | 这不是简单的格式补引用问题——`integration_log.md` §8 及本审查（part C）已确认这 10 篇在 12 份分节草稿中从未被引用过。若按 04_format_spec.md §6 的"必引"要求，需要在 Introduction/Discussion 中撰写与之对话的新段落（尤其 Lu24/Hang24/Gong26 涉及品质性状长期趋势，与本文结构断点分析和讨论直接相关），这是**内容缺口，需退回撰写阶段补写**，而非仅调整参考文献列表格式，详见 `reference_check.md` |
| 36 | 提交系统/APC/投稿信 | ChinaAgriSci.com；2026起 $1,800 APC；投稿信要点 | manuscript_v1.md 本身不含投稿信/提交平台信息（属另外文件范畴） | 不适用 | 无需在正文中处理，供投稿阶段核对 `03_target_journal.md`/`submission/cover_letter.md` |

## 汇总
- **不合规（❌）：3 条**（字数超限；kg/hm² 单位换算缺失；必引文献清单 10 篇完全未引用）
- **部分合规/边界情形（⚠️）：6 条**（Ethical approval 位置；摘要未达内部 246 词目标但满足硬指标 250；fraud/manipulation 字面出现；CF1 Arm2 数值未见散文；图表压缩至 6/5 未完成；两条参考文献缺卷期页）
- **合规（✅）：约 27 条**

最严重的三项：
1. **必引文献清单 10 篇从未被引用**——这是内容层面的缺口，不只是格式问题（详见 reference_check.md）。
2. **正文字数超标约 45%–82%**（14,563 词 vs 8,000–10,000 词guideline），需要实质性删减。
3. **投稿图表压缩（9→6图/7→5表）未执行**，且 `figure_table_list.md` 自己承认这一压缩指令在数字上就无法闭合，需作者团队明确决策。
