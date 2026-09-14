# 数字一致性审查 — manuscript_v1.md

审查日期：2026-09-14｜审查员：格式与数字一致性审查员
方法：grep/python 提取全部数字型陈述，与 `manuscript/tables/*.csv`、`manuscript/results_notes_*.md`、`manuscript/integration_log.md`、`evidence/*` 逐条比对；对 `integration_log.md` 声称已解决的冲突独立复核，不采信其结论本身。

## 1. 摘要 vs Results 一致性

| 位置 | 陈述 | 出处对照 | 是否一致 | 修正 |
|---|---|---|---|---|
| Abstract | 1.84 pp lower head-rice, 1.11 pp higher chalkiness, 12.2-pt lower quality-grade probability, +0.55 yield（suggestive only） | Results §5.2：−1.844 / +1.108 / −0.122(12.2pp) / +0.554（Table 3 精确值 −1.8441/1.1085/−0.1219/0.5534） | ✅ 一致（摘要取整/正文取三位小数，符合惯例） | 无 |
| Abstract | "green-channel entrants likewise show higher chalkiness" | Results §5.3：Arm2 chalkiness +2.809pp（Table 3: 2.8087） | ✅ 一致 | 无 |
| Abstract | "Bacterial-blight grades are better...among self-organised entrants" | §5.2：Arm1 blb_grade −0.190 (Table3: −0.1902)；Arm2 −0.562（Table3，未在摘要区分两臂，摘要笼统表述可接受） | ✅ 一致 | 无 |

## 2. 全文同一数字跨位置一致性核查

### 2.1 关键核查对象 A：企业 vs 科研单位系数（区试亩产、千粒重）

**发现：integration_log.md §10 的"已统一"声明不属实——不是因为全文出现了两套不同数字，而是因为全文统一使用的数字与本次实际重跑得到的真实结果（`table7_enterprise_vs_public.csv` 与 `results_notes_mechanism.md`）不一致。**

| 出处 | 区试亩产 (yield, kg/mu) | 千粒重 (TGW, g) | n | 备注 |
|---|---|---|---|---|
| `manuscript_v1.md` §4.7 Non-claim 8（L413-414） | **+3.18, p=0.035** | **+0.96, p=0.025** | （未列 n，行文中"n=632"在 L570 出现） | 与规划文档数字一致 |
| `manuscript_v1.md` §7 Mechanism（L570，即 integration_log 声称"已改为一致"处） | **+3.18, p=0.035** | **+0.96, p=0.025** | **632** | 与 §4.7 一致（integration_log 的"统一"确实做到了——两处manuscript正文本身互相一致） |
| **`manuscript/tables/table7_enterprise_vs_public.csv`（本次实际计算输出的表，Table 7 本身！）** | **+4.179117, p=0.02728** | **+1.193025, p=0.003013** | **408 / 411** | **这是论文自己引用为 Table 7 的数据源文件，数字与正文完全不同** |
| `manuscript/results_notes_mechanism.md` §4（本次实跑记录，标题即"Table 7"分析） | **+4.18, p=0.027** | **+1.19, p=0.003** | 408/411 | 明确写道："this run's sample (n=408–412) does not reach n=632 under any sample construction tried here...this discrepancy is flagged rather than papered over" |
| `02_research_route.md` §5 C11 / `00_decision_log.md`（旧规划文档，非本次实跑） | +3.18, p=0.035 | +0.96, p=0.025 | 632 | 这是**计划阶段的目标/占位数字**，先于任何实际回归运行 |

**结论：manuscript_v1.md 全文（§4.7 与 §7）确实统一使用了同一套数字（+3.18/+0.96, n=632），这一点 integration_log.md 没有说谎；但这套"统一"后的数字与论文自己的数据源文件 `table7_enterprise_vs_public.csv`（即正文引用为 Table 7 的那张表）以及本次实跑记录 `results_notes_mechanism.md` 完全不符（真实值为 +4.18/+1.19, n=408–412）。也就是说，integration_log.md §10 把"哪一版是正确的"这件事判断反了：它把旧规划阶段的占位/目标数字当作"真值"保留下来，而把本次实际重新计算出来、并保存为 Table 7 CSV 的数字当作"错误值"丢弃了。这是一个比"两处不一致"更严重的问题——现在全文是内部一致的，但与其自己的原始数据表（Table 7）不一致，且 n=632 在任何已知的样本构造下都无法复现（`results_notes_mechanism.md` 明确说明"the exact filter behind the plan's n=632 could not be reverse-engineered"）。** | 需要作者团队决定：(a) 若 Table 7 CSV（+4.18/+1.19, n=408-412）是本次分析的真实输出，则正文 §4.7 与 §7 均需改为这套数字，且 Table 7 本身应保持为其数据源；或 (b) 若 n=632 版本另有可靠来源，需先复现该口径并重新生成 Table 7 CSV，使表与文一致。当前状态下 Table 7（图表）与正文陈述互相矛盾，这是提交前必须解决的硬伤，而不是简单的四舍五入差异 |

同段落中未受影响、且与 Table 7 CSV 一致的两个系数：chalkiness (+0.94→CSV 1.0099≈+1.01，p=0.066 vs CSV 0.100，**方向一致但正文四舍五入到 +0.94 与 CSV 的 1.01 不严格相等，p 值 0.066 vs 0.100 也不同**——同样反映正文用的是旧规划数字而非 CSV 实跑值）与 head-rice (−0.84, p=0.114 vs CSV −1.2196, p=0.0701)。**四个系数中没有一个与 Table 7 CSV 的实跑数字精确匹配**，全部偏向旧规划文档的目标数字。

### 2.2 关键核查对象 B：R10 剔除荃银系数

| 出处 | head-rice | chalkiness | quality_stated | n |
|---|---|---|---|---|
| `manuscript_v1.md` §6.9（L520） | −1.368pp, p=0.006, n=602 | +0.940pp, p=0.034, n=599 | −0.104, p=0.011, n=609 | 602/599/609 |
| `manuscript_v1.md` §7 Mechanism（L568） | −1.368pp, p=0.006, n=602 | +0.940pp, p=0.034, n=599 | −0.104, p=0.011, n=609 | 602/599/609 |
| `manuscript/tables/table_r10_drop_winall_robustness.csv`（实跑输出） | −1.36763, p=0.005657 | +0.93990, p=0.033813 | −0.10449, p=0.010592 | 602/599/609 |

**结论：R10 剔除荃银系数在 §6.9 与 §7 两处完全一致，且与实跑 CSV 数字精确匹配（四舍五入误差在正常范围内）。integration_log.md 关于此项的表述准确，这一处的"统一"声明属实，与要求的 −1.368/+0.940/−0.104 版本完全吻合。** | 无需修正 |

### 2.3 其他跨位置重复数字抽查（均一致）

| 数字 | 出现位置 | 是否一致 |
|---|---|---|
| head-rice −1.844pp (Arm1) | Abstract, §3(引言总结), §4.5, §5.2, §6.3(R4), §6.5(RI), §6.6(Manski邻近值), Table3 | ✅ 全部一致 |
| chalkiness +1.108pp (Arm1) | Abstract, §4.5, §5.2, §6.3, §6.5, Table3 | ✅ 一致 |
| quality_stated −0.122 (Arm1) | Abstract(12.2pt), §4.5(−0.122), §5.2, §6.3, Table3(−0.1219) | ✅ 一致（摘要取整合理） |
| production-trial yield gain +0.919 (Arm1) vs −1.036 (Arm2) | §4.3, §4.5, §5.2, §5.3, §6.1(R1), §6.9, Table3 | ✅ 各处符号/量值一致 |
| Winall channel share 60.2%/47.5%, n=166/1101 | §7 正文, Table5b | ✅ 一致 |
| Winall logit α=−0.728, OR=0.483 | §7 正文（−0.728, 0.483） vs Table5b（−0.7276, 0.48306） | ✅ 一致（四舍五入） |
| Winall within-Unified positioning +2.212/+9.8pt/−0.692 | §7 正文 vs Table5 (2.2116/9.77/−0.6916) | ✅ 一致 |
| 结构断点年份：head-rice 2015, chalkiness 2009, yield 2017 | §5.6 正文 vs `table_breakpoint_scan_full.csv`（未逐行核对但年份、Wald统计量在正文自洽） | ✅ 内部一致 |
| 省审复制 n=495 vs 旧规划 n=452/n=318 | §6.11 正文自行披露差异（"n=495...differ from an n=452...prior planning notes"） | ⚠️ 已被正文主动披露为未决问题，非隐藏冲突 | 无需额外修正，正文已如实报告 |

## 3. 图与表的数字一致性（Fig.2 森林图 vs Table 3）

已读取 `figures/fig2_forest_main.png` 并与 `table3_main_results.csv` 逐条比对：

- Arm1 head-rice 点估计约 −1.8、95% CI 约[−2.6,−1.0] → 与 CSV（−1.844, [−2.636,−1.052]）**一致**。
- Arm1 chalkiness 点估计约 +1.1、CI 约[0.2,2.0] → 与 CSV（1.108,[0.248,1.969]）**一致**。
- Arm2 head-rice 点估计约 0、CI 跨零 → 与 CSV（−0.391, [−1.676,0.894], 不显著）**一致**。
- Arm2 amylose 落在图中 blue markers 负值区（约−1.5） → 与 CSV（−1.520）**一致**。
- Arm1/Arm2 的 self-reported（红色）与 third-party（蓝色）着色与文字描述的"colour-coded by measuring party"一致。

**结论：Fig.2 与 Table 3 数字视觉/量级一致，未发现矛盾。**（仅核查主森林图 Fig.2，其余 6 幅图因任务范围限制未逐一像素级核对，建议后续审查补充 Fig.4/Fig.7 与对应表/数字的核对。）

## 4. 独立发现：荃银 2026 年罚款金额存在数量级错误（新发现，非任务预设的两个核查点，但在实跑排查中发现）

| 出处 | 罚款金额 |
|---|---|
| `manuscript_v1.md` §7（L566） | **"fined 300,000 CNY"**（30万元） |
| `evidence/05_industry_policy.md`（一手来源，安徽证监局处罚事先告知书） | **300 万元**（合计公司300万+个人730万，公司部分即300万元＝3,000,000 CNY） |
| `plan/01_theme_and_innovation.md` W4、`plan/BRIEF.md`、`manuscript/tables/table_negative_facts_timeline.csv` | 均为 **300万元** |
| `manuscript/results_notes_mechanism.md` L184 | "2026 fined 300万元" |

**结论：manuscript_v1.md 把"300万元"错误折算/误写为 "300,000 CNY"，实际应为 "3,000,000 CNY"（或直接写 "CNY 3 million" / "RMB 3 million"），少了一个数量级（10倍误差）。这是一个明确的数值错误，且与规划文档、证据文件、本次实跑记录三方来源都能对上，说明这是撰写/整合阶段引入的孤立错误，而非来源本身有歧义。** | 需立即改为 "3,000,000 CNY" 或 "3 million CNY"，同时保留"10.86% of disclosed profit"和罚款事由不变（这两项与 300万元同一处披露，数字本身正确） |

## 5. 汇总

| 类别 | 数量 |
|---|---|
| 审查覆盖的重复/跨位置数字组 | 约 15 组 |
| 发现问题 | **2 项实质性数值错误/不一致** + 1 项已知未决（provincial n差异，正文已自行披露） |

**最严重的三条：**

1. **企业 vs 科研单位系数（区试亩产、千粒重）：全文虽已"内部统一"为 +3.18/p=0.035、+0.96/p=0.025（§4.7 与 §7 两处一致），但这套数字与论文自己作为 Table 7 数据源的 `table7_enterprise_vs_public.csv`（真实实跑值 +4.18/p=0.027、+1.19/p=0.003，n=408–412 而非 632）完全不符。integration_log.md 关于"已按实跑版本统一"的表述是**不准确的**——它实际上统一到了旧规划文档的目标值，而不是本次真正跑出来的表格数字。这意味着 Table 7（图表本身）与引用它的两段正文互相矛盾，是提交前必须解决的硬伤。
2. **2026 年罚款金额数量级错误**："300,000 CNY" 应为 "3,000,000 CNY"（300万元），相差10倍，所有一手证据文件（evidence/05_industry_policy.md）、规划文档（01_theme_and_innovation.md、BRIEF.md）、时间线表（table_negative_facts_timeline.csv）均为300万元，仅正文两处（§7 一处，`sections/mechanism.md`同源一处）写错。
3. R10 剔除荃银系数（−1.368/+0.940/−0.104）**核实为真——integration_log.md 关于此项的"已统一"声明属实**，全文两处引用与实跑 CSV 完全吻合，可作为对照，说明并非所有 integration_log 的"已解决"声明都不可信，需要逐条独立核查而非一概否定或一概采信。
