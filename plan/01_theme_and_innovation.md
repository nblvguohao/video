# 01 最终主题与创新点（总设计师合成稿）

> 合成日期：2026-09-14
> 输入：四份提案 + 三份评审 + 主会话独立复算 + 本次总设计师实跑复核
> 本文件中标注「实跑」的全部数字，由本次会话在 `evidence/data/analysis_rice_channel.pkl` 上用 pandas/statsmodels 重新运行得到，脚本见 `02_research_route.md` §9。
> **纪律**：凡证据不足处一律写「提示性」或「不可判定」，不升级表述。

---

## 1. 题目

### 英文（主）
> **Who measures what enters the market? Self-organised variety trials and the third-party-assayed grain-quality gap in China's rice variety approvals, 2017–2022**

*Running title:* **Trial channels and third-party grain quality in Chinese rice approvals**

### 中文
> **谁在测量、什么进入市场？——自组织品种试验与中国水稻审定品种的第三方测定品质缺口（2017—2022）**

### 题目的自我约束
- 用 **gap**（缺口）而非 *effect / impact / caused by*：全文估计量是**进入者构成效应**（composition effect on the entering population），不是 ATE。
- 用 **third-party-assayed**：把主结果的适用范围限定在"由农业农村部指定机构按 NY/T 593 统一测定的稻米加工与外观品质"，**不**扩张为"所有第三方测定性状"（抗性性状方向相反，见 §9）。
- 窗口写 **2017–2022**（而非 2005–2022）：通道变量只在 2017 与 2019–2022 存在识别变异；2005–2016 只作背景与断点检验。

---

## 2. 一句话论点（one-sentence argument）

**在同一审定年份、同一生态试验组、同一对照品种的比较下，经申请人自组织试验进入国家审定的水稻品种，其由第三方指定机构统一测定的稻米加工与外观品质系统性更差（联合体臂：整精米率 −1.84 个百分点、垩白度 +1.11 个百分点、载明国家米质等级的概率 −12.2 个百分点，n=742/739/750），而其由申请人自己组织的试验测得的产量性状不降反略升；这一"随测量主体而变的符号分离"不能由"自组织通道的申请人育种能力更弱"解释——能力差异假说预测两类性状同向变差——因此本文把关注点从"改革开了多大的门"转向"门内由谁拿着尺子"。**

---

## 3. 英文摘要草稿（278 words）

> China's 2016 revision of the *Measures for the Administration of Crop Variety Approval* ended the state monopoly on variety-value testing: certified integrated seed firms may run their own "green-channel" trials, and consortia of five or more breeders may organise their own regional trials. Whether this changed *what* enters the seed market, rather than only *how much*, is unknown, because no previous study has observed which channel a variety actually passed through. We exploit a previously unused feature of the official approval announcements: each announcement names the trial in which the variety was tested, letting every record be assigned to the state-run unified trial, the green channel or a consortium trial. Using national rice approval records parsed from Ministry announcements, we compare self-organised with unified-trial entrants within the same approval year, the same ecological trial group and the same named check. Because the green channel (2017) and consortium trials (2019–2022) do not overlap in time, we estimate them as two separate treatments rather than one pooled "new channel". Consortium entrants show 1.84 percentage points lower head-rice percentage, 1.11 points higher chalkiness degree and a 12.2-point lower probability of carrying a stated national quality grade — all assayed by ministry-designated third-party laboratories under NY/T 593 — while the yield advantage recorded in the applicant's own trial is, if anything, higher (+0.55 points, suggestive only). Green-channel entrants (2017) likewise show higher chalkiness and a lower probability of a stated grade. The identification argument rests on this sign separation: a pure breeding-ability account predicts that both trait classes deteriorate together, whereas third-party grain quality deteriorates while applicant-measured performance does not. Results survive worst-case bounds, randomisation inference and dropping the focal firm. We report two results that cut against the narrative: bacterial-blight grades are *better* among self-organised entrants, and within-applicant comparisons are too under-powered to separate channel from self-selection.

*（JIA 摘要上限 250 词：投稿时删去最后一句的第二半句与 "Green-channel entrants…" 一句的从句，压到 246 词；Rice Science 上限 350 词可全文保留。）*

---

## 4. 研究问题（3 个）

**RQ1（主问题｜通道 × 测量主体）**
在控制审定年份、生态试验组与对照品种后，经自组织试验（2017 绿色通道 / 2019–2022 联合体）进入国家审定的水稻品种，与经国家统一区试进入的品种，在**第三方指定机构统一测定的稻米品质性状**上是否存在系统缺口？该缺口的方向是否与**申请人自组织试验测定的产量性状**上的差异方向分离？

**RQ2（处理异质性｜两条通道不可合并）**
绿色通道（2017）与联合体（2019–2022）是两个在时间上几乎不重叠的处理。两者的缺口在方向、量级与性状构成上是否一致？把两者合并为单一"新通道"处理会造成什么误判？

**RQ3（机制个案｜反例检验）**
作为改革期国审份额上升最快的单一主体、育繁推一体化企业与水稻"强优势阵型"企业，荃银高科的通道选择与性状组合是否偏离同行？其偏离的方向能否排除"企业比科研单位更粗放"这一替代解释？（同时如实纳入该公司订单粮食业务毛利率约 −0.09%、2025 年归母净利 −2.12 亿元由盈转亏、2024 年报被出具保留意见、2026 年因虚假记载被罚 300 万元并变更为 ST 荃银等负面事实。）

---

## 5. 创新点（3 条）

### 创新点 1｜首个**记录级**审定试验通道处理变量：把"改革"从时期变量变成通道变量

**相对谁新**：相对于目前唯一对同一改革做实证评估的论文。

- **Xiang, C., Yang, R., Wang, X., & Huang, J. (2025). Impact of seed regulation reform on licensing fees of varieties in China. *Agribusiness*. DOI: 10.1002/agr.22020.**
  其处理变量是**时期**（改革前/后），数据是企业问卷 + 品种许可交易价格，结果变量是**许可费**；全文**没有任何通道变量**，无法区分"改革改变了价格"与"改革改变了进入者构成"。该文另一结论——**杂交稻品种的许可费不受改革显著影响**——恰是本文最干净的对话点：价格维度无效应 ≠ 进入者属性无变化。
- **Zhao, Y., Deng, H., Hu, R., & Xiong, C. (2022). Impact of government policies on seed innovation in China. *Agronomy*, 12(4), 917. DOI: 10.3390/agronomy12040917.**
  政策虚拟变量 × 年份的时间序列设定，处理同样是时期而非通道。

**增量**：审定公告的"产量表现"段落逐字载明试验名称（"参加长江中下游中籼迟熟组**绿色通道**区域试验"／"……**联合体**区域试验"／无限定词的统一区试）。实跑解析：国审 2017 年 88 条绿色通道、2019–2022 年 556 条联合体、同期统一区试 536 条（2018 年 233 条公告集体不载明通道词，单列处理）。这使"**同年 × 同试验组 × 同对照**"的记录级对照成为可能。

**诚实边界**：通道非随机分配；估计量是进入者构成效应，不是"把同一品种换一扇门"的因果效应。

---

### 创新点 2｜把"同一份文书内自测性状与第三方测定性状并存"做成**识别论证**，而不只是描述

**相对谁新**：相对于规制经济学中"自我认证削弱把关质量"的既有证据链。

- **Duflo, E., Greenstone, M., Pande, R., & Ryan, N. (2013). Truth-telling by third-party auditors and the response of polluting firms: experimental evidence from India. *Quarterly Journal of Economics*, 128(4), 1499–1545. DOI: 10.1093/qje/qjt024.**
  已用随机实验证明"由被监管方选择并付费的审计方系统性报出有利数字"。**但其设计是同一属性（排放量）由两方分别测量**；本文没有同一属性的双重测量，拥有的是**同一份文书内两类由不同主体测量的属性**。本文的证据强度弱于 Duflo et al.，但场景与可观测量完全不同，且不依赖实验。
- **Bar, T., & Zheng, Y. (2019). Choosing certifiers: evidence from the British Retail Consortium food safety standard. *American Journal of Agricultural Economics*, 101(1), 74–88. DOI: 10.1093/ajae/aay024.**
  厂商偏好地理邻近、且此前给出更高 A 级比例的认证机构——即"认证方选择的内生性"。这正是本文 R11 组内检验无法排除的自选择解释的农经版本，必须正面引用并说明本文的符号分离为何不能被纯自选择解释。
- **Grennan, M., & Town, R. J. (2020). Regulating innovation with uncertain quality: information, risk, and access in medical devices. *American Economic Review*, 110(1), 120–161. DOI: 10.1257/aer.20180946.**
  比较的是**两个制度之间**（EU vs US），而非同一制度内的两条路径。
- **Renckens, S., & Auld, G. (2022). Time to certify: explaining varying efficiency of private regulatory audits. *Regulation & Governance*, 16(2), 500–518. DOI: 10.1111/rego.12362.**

**增量（识别论证本身）**：纯"申请人育种能力差异"假说预测两类性状**同向变差**。实跑结果是**符号分离**：第三方测定的加工与外观品质更差（整精米率 −1.84 pp，p<0.0001；垩白度 +1.11 pp，p=0.012），而申请人自测的产量优势不降反升（区试增产率 +0.55 pp，p=0.020；生产试验增产率 +0.92 pp，p<0.0001）。能力差异假说无法产生这个符号分离；能产生它的只有"两类性状由不同主体测量"或"两条通道的申报门槛不同"。**这句话必须写进摘要与方法节，不得留在讨论。**

---

### 创新点 3｜把改革拆成**两个处理**，并证伪"2016 时间断点归因"；焦点企业作为**反例**而非主角

**相对谁新**：相对于"审定品种性状长期演变"这一已被占位的文献群，以及以同一家企业为对象的产业组织论文。

- **Lu, Y., Tang, Y., Zhang, J., Liu, S., Liang, X., Li, M., & Li, R. (2024). Variations and trends in rice quality across different types of approved varieties in China, 1978–2022. *Agronomy*, 14(6), 1234. DOI: 10.3390/agronomy14061234.**
- **Hang, S., Wang, Q., Wang, Y., & Xiang, H. (2024). Evolution of rice cultivar performance across China: a multi-dimensional study on yield and agronomic characteristics over three decades. *Agronomy*, 14(12), 2780. DOI: 10.3390/agronomy14122780.**（注意作者姓氏是 **Hang**，不是 Han）
- **Gong, J., Zhang, X., Zhang, J., Zeng, B., Zhang, X., Xu, X., … Xie, H.-A. (2026). Three-line hybrid rice in China: sustained improvements in yield, quality, and resistance over fifty years. *Rice Science*. DOI: 10.1016/j.rsci.2026.04.004.**（摘要未能独立取得全文，正文引用其具体数字前必须先核对）
- **Xie, Z., Yuan, S., Zhu, J., & Li, W. (2023). Contract farming led by a seed enterprise and incentives to produce high quality: which contract design performs best? *Agribusiness*, 39(4), 1173–1198. DOI: 10.1002/agr.21823.**（以荃银高科的订单农业为对象，博弈模型 + 数值算例，无品种级数据）

**增量 A（两个处理）**：主会话复算与本次实跑共同确认，绿色通道集中于 2017、联合体自 2019 起，**时间上基本不重叠**；且两臂在若干性状上方向不同（2017 绿色通道的生产试验增产率 **−1.04 pp，p=0.014**，与联合体臂的 +0.92 pp 相反）。把两者合并为单一"新通道"会制造一个不存在的平均处理。本文分臂估计，并明确报告"合并设定只作为参考行，不作为主结论"。

**增量 B（证伪时间断点归因）**：未知断点 sup-Wald 扫描显示，**只有绝对区试亩产的断点落在 2017**，而品质性状的断点普遍早于改革（2009–2015），比对照增产率二十年间既无趋势也无断点。因此把 2016 年前后的品质跃升整体归功于（或归咎于）审定改革是错误归因。这对 Lu24 / Hang24 / Gong26 一类"按年代读趋势"的做法是一条方法学提醒。

**增量 C（企业作为反例）**：荃银高科在 2017 与 2019–2022 年的 166 条国审记录中 **60.2% 走国家统一区试**（其余申请人 47.5%，实跑复现），且在统一通道内部其品种整精米率 **+2.22 pp（p<0.0001）**、载明米质等级概率 **+9.7 pp（p=0.0014）**、垩白度 −0.50 pp（p=0.058）。若"新通道品质更差"仅源于"企业比科研单位更粗放"，最典型的一体化企业应当最像新通道；事实相反。

---

## 6. 论文类型与目标读者

- **类型**：Research Article（实证 / 准实验政策评估，含一个机制个案节）。不是综述，不是评论。
- **一级读者**：种业制度与品种审定政策研究者、农业政策评估者、农业经济学家。
- **二级读者**：水稻育种家与品质育种研究者（关心"公告里的品质数字该怎么读"）。
- **三级读者**：规制经济学 / 认证与审计文献读者（自我认证 vs 第三方认证）。
- **写作口径**：农艺性状必须同时给出农学含义（整精米率＝加工得率、垩白度＝外观品质）与经济学含义（可认证、可加工、可收储的产品属性），以便三类读者都能读完。

---

## 7. 为什么荃银高科是合适的案例

1. **它是改革期的最大单一受益者**：在长江中下游 + 上游中籼迟熟层，其国审份额由 2005–2015 年的 0–12% 升至 2022–2024 年的 23%/31%/31%。若通道开放"让谁都能进来"，它是最应该被这一叙事解释的主体。
2. **它同时满足两个"本应最大化利用绿色通道"的条件**：育繁推一体化企业（有资格自行组织绿色通道试验）+ 农业农村部 2022 年"强优势阵型"企业。**它是绿色通道设计时心目中的典型用户。**
3. **实测结果与该预期相反**（60.2% vs 47.5% 走统一通道），因此它在本文中承担的是**识别功能**：排除"新通道品质差 = 企业比科研单位粗放"这一替代解释。
4. **主结论不依赖它**：剔除荃银全部记录后，联合体臂主结果仍成立（整精米率 −1.20，p=0.019；垩白度 +1.05，p=0.041；载明等级 −11.6 pp，p=0.016；实跑）。**审稿人即使全盘否定荃银章节，论文主体依然完整。**
5. **它的负面事实与本文主题同构**：2024 年报虚假记载被罚 300 万元、变更为 ST 荃银——"企业自报信息的可靠性"正是全文"自报测量 vs 第三方测量"的公司治理镜像，是讨论章节的天然收束，而不是公关负担。
6. **它的学术足迹几乎空白**：荃两优 6019、荃两优丝苗、徽两优 882 无任何学术记载，荃优华占极弱；对其国审品种组合的系统量化刻画本身即为空白（须注意：**"徽两优"系列不是荃银品系**，属安徽省农科院水稻所；国际文献中的 "Huazhan" 组合多数不是荃银品种，只有荃优华占属荃银）。

### 如何避免"企业软文"观感——**七条硬性写作规则**

| # | 规则 | 具体做法 |
|---|---|---|
| W1 | **篇幅上限** | 荃银相关内容（正文 + 图表 + 讨论）**不得超过全文 15%**；机制章节最多 1 节 + 1 图 + 1 表。 |
| W2 | **角色声明前置** | 在 Introduction 与机制章节首段各写一次：*"Winall enters this paper as a counter-case that rules out an alternative explanation, not as a source of the main result."* |
| W3 | **主结果免疫性必须可见** | 剔除荃银的稳健性（R9）放**正文表**，不放附录。 |
| W4 | **负面事实与正面事实同段呈现** | 凡出现"荃银品质更优"的句子，同段或紧邻段必须给出订单粮食毛利率约 −0.09%、2025 年归母净利 −2.12 亿元、2024 年报保留意见与 300 万元罚款 / ST 变更。不得分置于不同章节。 |
| W5 | **禁止收益折算** | 不把回归系数折算成企业收益/加工价值（这正是提案 D 被编辑评审点名"像 ST 公司投资者说明会"的做法）。 |
| W6 | **禁止排序修辞** | 不写"按一体化深度排序"；统计评审已用安慰剂企业检验（湖南希望种业的品质倾斜大于荃银）证伪该排序。 |
| W7 | **不使用公司叙述作为证据** | 公司年报/投资者关系表述只作为**待检验的行业叙事**引用（如"审定品种同质化"），且必须给出本文的检验结果，不得作为论据。 |

---

## 8. 本文**不主张**的事项清单（Non-claims）

> 本清单须以一个独立小节（"What this paper does not claim"）写入论文第 4 节末，并在 Limitations 呼应。

1. **不主张因果**。β 是"同一年份—生态—对照门框下，从两扇门进来的品种属性差多少"（进入者构成效应），**不是**"把同一个品种换一扇门会怎样"的平均处理效应。组内（同一申请人跨通道）检验只有约 10–14 家申请人、26–64 条记录，CI 极宽，点估计甚至与主设定反号——这是**检验力不足**，不是反证，但也意味着本文**无法分离通道效应与申请人自选择**。
2. **不主张自组织试验的产量数据造假**。全文不出现"造假 / 操纵 / fraud / manipulation"。统一表述：*"consistent with measurement discretion in self-organised trials, though channel self-selection cannot be ruled out."*
3. **不主张 2016 年改革导致了品质下降**。相反，本文的断点扫描证据表明品质改善的结构断点早于改革（2009–2015），把品质变化整体归因于 2016 年是错误归因。本文估计的是**同年内两条通道之间的缺口**，不是改革前后的时间效应。
4. **不主张"第三方测定的性状一律更差"**。实跑显示自组织通道品种的**白叶枯病级反而更好**（联合体臂 −0.190，p<0.0001，n=519；2017 绿色通道臂 −0.562，p=0.074，n=82；主会话在其设定下得 −0.457，p=0.002），穗颈瘟无差异。主结论严格限定为**稻米加工与外观品质**（整精米率、垩白度、米质等级），并把抗性结果如实报告。
5. **不主张自报增产率系统性更高**。该半边只是**提示性**：联合体臂 +0.55 pp（p=0.020）与 +0.92 pp 生产试验（p<0.0001）方向一致；但 2017 绿色通道臂的生产试验增产率为 **−1.04 pp（p=0.014）**，方向相反；且 **2017 年统一区试臂的区试增产率覆盖率仅 1.9%（1/52），该臂的区试增产率在本设计下不可估计**。合并设定 p=0.089（主会话）。因此摘要只写 "if anything, higher (suggestive only)"。
6. **不主张品质缺口等于农户或消费者福利损失**。本文无农户采纳、推广面积、种子价格与消费端数据，不评估福利。
7. **不主张审定数量的变化**。公告汇编是样本而非普查（2023 年 85/409、2024 年 61/405、2025 年仅 2 条），因此**审定数量不作为任何结果变量**，数量只作背景描述并注明覆盖率。
8. **不主张省级层面同样成立**。省审复制未得到显著结果（整精米率 −0.134，p=0.93 等）；两种解释（检验力不足 / 效应集中在奖励最大的国审层）并列，不做偏袒。
9. **不主张"企业普遍优于科研单位"或反之**。在本文主分析层（两大籼稻试验组、2005–2022、有申请人字段的年份，n=632）实跑：科研单位相对企业区试亩产 +3.18 kg/亩（p=0.035）、千粒重 +0.96 g（p=0.025），垩白度 +0.94（p=0.066）、整精米率 −0.84（p=0.114）方向与既有探索性结果一致但**不显著**。因此本文只把"企业 vs 科研单位的性状分工"作为**描述性、方向性**的背景事实呈现，不作为结论。
10. **不主张荃银的品质路线在财务上成功**。相反，本文明确呈现其订单粮食业务的负毛利与 2025 年由盈转亏，并把"品质差异化战略的财务可持续性存疑"写为结论的一部分。
11. **不主张品种同质化正在加剧或减轻**（若保留该节）。稀疏化亲本多样性与性状空间检验均为零结果（p=0.141 / 0.171），只作为对流行行业叙事的证伪，不作为正面发现。
12. **不主张汇编数据等同于官方全集**。一手来源是农业农村部公告，GitHub 汇编 `he-zhui/Rice_QA` 仅为获取途径；投稿前须完成 50 条随机记录与官方公告原文的逐字段人工复核并在 Methods 报告一致率。

---

## 9. 本文必须如实报告的"与叙事冲突"结果（Conflicting-evidence register）

| # | 冲突结果 | 实跑数值 | 写在哪里 |
|---|---|---|---|
| CF1 | 自组织通道品种的**白叶枯病级更好**（更抗） | 联合体臂 −0.190（p<0.0001, n=519）；2017 绿色通道臂 −0.562（p=0.074, n=82） | Results 主表 + Discussion 单独一段 |
| CF2 | 2017 绿色通道臂**生产试验增产率更低** | −1.04 pp（p=0.014, n=112），与联合体臂 +0.92 pp 相反 | Results §两臂对照表 |
| CF3 | 2017 绿色通道臂的**区试增产率不可估计** | 统一区试臂覆盖率 1.9%（1/52）；扩至全部试验组也只有 7/145 | Data §缺失结构，并在 Results 标注 "not estimable" |
| CF4 | **米质一/二级**在最坏情形界下符号不稳 | Manski 界 [−0.253, +0.088]（实跑），故降为次要结果，主结果用 100% 定义的"载明米质等级" | Robustness §界 |
| CF5 | **组内（同一申请人跨通道）检验点估计多与主设定反号** | 整精米率 +3.68（95% CI [−1.65, +9.02]）等；n≈26 条 | Results 正文表 + Non-claims |
| CF6 | **省审复制不显著** | 整精米率 −0.134（p=0.93）等 | Robustness 正文 |
| CF7 | **株高安慰剂显著** | +0.95 cm（p=0.044，联合体臂） | 方法节**预先声明**株高属"与高秆大穗选型一致的辅助证据"，移出安慰剂集合；安慰剂改用结实率（−0.20，p=0.43）与千粒重（+0.14，p=0.59） |
| CF8 | **"载明米质等级"在数学上是米质等级的缺失指示** | 与缺失率差 −14.8 pp 是同一个数 | 必须表述为"公告载明行为"，并报告控制公告文本长度与非缺失字段数后系数反而增强（−0.169, p=0.0001） |

---

## 10. 与被否方案的关系（一句话）

本文以提案 C 为骨架；嫁接提案 A 的"对照阶梯"作为一个 ~600 词的稳健性小节（并如实引用 Piepho 等既有文献与其不确定性区间）；保留提案 B/D 的"企业 vs 科研单位性状分工"作为**描述性背景**；**不采用** B/D 的一体化因果机制主张。详见 `00_decision_log.md`。
