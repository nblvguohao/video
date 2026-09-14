# 维度 10：目标期刊预扫描（荃银高科主线 · 作物育种 + 种业产业/政策 交叉实证论文）

| 项 | 值 |
|---|---|
| 维度 | 10 — 目标期刊预扫描（Journal Pre-scan） |
| 更新时间 | 2026-09-14 |
| WebSearch 检索次数 | 41 次（本会话；配额约 200 次，余量充足） |
| 学术 MCP 调用 | Scholar Gateway semanticSearch × 2（结果落盘后解析） |
| 直接引用的独立来源 URL | 46 个（见文末「来源清单」） |
| 复用的既有证据文件 | `06_lit_breeding_refs.csv`（88 条）、`07_lit_seed_industry_refs.csv`（100 条）— 例文引文主要来自此二文件，已在维度 6/7 核验 |
| 工具约束 | 容器内 WebFetch/curl 对 letpub.com.cn、iikx.com、ablesci.com、scimagojr.com、fenqubiao.com、sciencedirect.com、zhihu、CSDN 等**全部返回 403 EGRESS_BLOCKED**（已实测，见下）。期刊官网 Guide for Authors 无法直接打开，全部格式信息来自 WebSearch 结果页的 AI 摘要，逐条标注置信度 |

> **实测拦截记录**（`curl -o /dev/null -w %{http_code}`，2026-09-14）：
> `www.ablesci.com:443`、`www.scimagojr.com:443`、`www.journalmetrics.org:443`、`zhuanlan.zhihu.com:443`、`www.fenqubiao.com:443`、`www.sciencedirect.com:443` 均 `curl: (56) CONNECT tunnel failed, response 403`；
> WebFetch 对 `blog.csdn.net`、`www.letpub.com.cn`、`www.iikx.com` 返回 `EGRESS_BLOCKED`。

---

## 0. 三条必须先说清楚的前提（影响本报告全部分区数据的解读）

### 0.1 「2025 年中科院分区表」是官方最后一版
- 2025 年分区表于 **2025 年 3 月 20 日**正式发布，"中国科学院文献情报中心发布《2025年度期刊分区表》，覆盖 SCIE、SSCI、A&HCI、ESCI 和 OAJ 五大数据库共 **21,772 本期刊**，共设置 **21 个大类**"（WebSearch 摘要，来源：instrument.com.cn / kejianyi.cn / academicenter.com）。
- 分区规则原话：「每个学科分类按照期刊超越指数的高低，依次划分为四个区，**前 5% 为该类 1 区，前 6%–20% 为 2 区，前 21%–50% 为 3 区，后 50% 为 4 区**」。
- **重要变更**：检索到「**自 2026 年起，中国科学院文献情报中心不再更新与发布期刊分区表**」；2026 年 3 月 24 日由"新锐学术"推出《**新锐期刊分区表**》，覆盖 22,299 种期刊 + 15 种会议论文集（来源：sohu.com/a/1001021312、zhuanlan.zhihu.com/p/2020046052250646232、academicenter.com/news/details/2036671685663072256）。
- **后果**：当前中文期刊导航站（ai4paper.pro、iikx.com、xueshu.com 等）普遍并列展示「**中科院基础版 X 区 / 中科院新锐版 Y 区**」两套标签，且多数站点在 2026 年 7 月后已把"最新升级版"字样指向 2026 新锐版。本报告中凡标注来源为 ai4paper 的分区，其"基础版"一栏**最接近但不等同于** 2025 年中科院升级版分区，**均标为"待确认（需机构账号登录 fenqubiao.com 核对 2025 年升级版原表）"**。

### 0.2 「2025 农林科学大类 2 区完整名单」未能获取——原因与已得部分名单
- 尝试 6 次不同检索式（含指定 CSDN/知乎/科检易原文页），WebSearch 的 AI 摘要**始终只返回发布公告与查询入口，不返回名单正文**。原话（多次复现）：
  > 「机构用户可登录分区表官网（www.fenqubiao.com）使用单位账号查询，个人用户在微信公众号"期刊分区表（fenqubiao）"的服务选项菜单栏"分区查询"中查看。」
- 承载完整名单的页面（blog.csdn.net/glldxh/article/details/146424374、zhuanlan.zhihu.com/p/31844723614、kejianyi.cn/news/detail/1729、blog.csdn.net/T0620514/article/details/147661518 的 Excel 附件）**全部被 egress 代理拦截**，无法下载。
- **因此：本报告不提供"2 区完整名单"，只提供按候选刊逐一核实得到的部分名单（见 §1），并明确标注这是"候选集内的分区结果"而非"大类全名单"。** 这是本次预扫描最主要的未完成项。

### 0.3 影响因子的年份口径
检索到的 IF 数值同时存在两代：**JCR 2024（2025 年 6 月发布）** 与 **JCR 2025（2026 年 6 月发布）**。多数站点当前展示的是后者（例：researcher.life 明确「Impact Factor: 7.9 (updated in June 2026)」用于 Field Crops Research；journalmetrics.org 对 Euphytica 写「impact factor is 1.8, released June 17, 2026 and based on 2025 citation data」）。本报告 CSV 的 `impact_factor` 列填写**检索到的最新值**，并在 notes 中注明年份口径与冲突值。

---

## 1. 农林科学大类分区名单（候选集内已核实部分）

> ⚠️ 这不是 2025 年中科院分区表农林科学大类的完整名单。这是"本次 32 本候选刊 + 检索过程中顺带确认的少数期刊"的分区汇总。完整名单获取方式见 §0.2。

### 1.1 农林科学 **大类 1 区**（含 Top 标记，候选集内）

| 期刊 | 大类 | 小类 | Top | 来源与原话 | 置信度 |
|---|---|---|---|---|---|
| Field Crops Research | 农林科学 1 区 | 农艺学 2 区 | 1区 Top（ai4paper） | 「在中科院最新升级版分区表中，该刊分区信息为大类学科：农林科学 1 区，小类学科：农艺学 2 区」；ai4paper：「中科院基础版1区 Top · 中科院新锐版1区 Top · JCR Q1 · 影响因子 7.9」 | 中高（两源一致） |
| Agricultural Systems | 农林科学 1 区 | 农业综合 1 区 | 1区 Top（ai4paper） | 「Agricultural Systems is classified as Category 1 (大类学科：农林科学1区)…小类学科：农业综合 1区」；ai4paper：「基础版1区 Top · 新锐版1区 Top · JCR Q1 · IF 6.2」 | 中高 |
| European Journal of Agronomy | 农林科学 1 区 | 农艺学（区未确认） | 1区 Top（ai4paper） | ai4paper：「基础版1区 Top · 新锐版1区 Top · JCR Q1 · 影响因子 6.7」 | 中 |
| Agronomy for Sustainable Development | 农林科学 1 区 | — | 1区 Top（ai4paper） | 「Agronomy for Sustainable Development is classified as 1区 in the agricultural sciences category」；ai4paper：「基础版1区 Top · 新锐版1区 Top · IF 8.2」 | 中 |
| Journal of Integrative Agriculture | 农林科学 1 区 | 农业综合 2 区 | 1区 Top（ai4paper 基础版）/ 新锐版 1 区（非 Top） | 「在中科院最新升级版分区表中，该刊分区信息为大类学科：农林科学1区，小类学科：农业综合 2区」；ai4paper：「基础版1区 Top · 新锐版1区 · JCR Q1 · IF 5.7」 | 中高（两源一致） |
| The Crop Journal | 农林科学 1 区 | — | 1区 Top | ai4paper：「基础版1区 Top · 新锐版1区 Top · JCR Q1 · 影响因子 6.7」；另一检索称「The Crop Journal has a 2025 CAS categorization of 1st tier TOP」 | 中 |
| Global Food Security | 农林科学 1 区 | — | 1区 Top | ai4paper（条目名 "Global Food Security-Agriculture Policy Economics and Environment"）：「基础版1区 Top · 新锐版1区 Top · JCR Q1 · IF 7.5」 | 中 |

### 1.2 农林科学（或相邻大类）**2 区**（候选集内）

| 期刊 | 大类 / 小类 | Top | 来源与原话 | 置信度 |
|---|---|---|---|---|
| **Rice Science** | 农林科学 2 区 | 否 | ai4paper：「中科院基础版2区 · 中科院新锐版2区 · JCR Q1 · 影响因子 7.4」 | 中高 |
| **Agriculture (MDPI)** | 农林科学 2 区（旧 2022 版为农林科学 3 区/农艺学 3 区） | 否 | 「in the 2022 CAS classification, the major discipline is 农林科学 and the minor discipline is 农艺学, both classified as 3区. However…the journal shows Q1 in JCR and 2区 in CAS classification for 农林科学」 | 中（口径不一，**待确认**） |
| **Agronomy (MDPI)** | 农林科学 2 区 | 否 | 「Agronomy-Basel is classified as Q1 in JCR and 2区 in CAS classification, with an impact factor of 3.3」 | 中（**待确认**，另一源给 IF 3.4） |
| **Plants (MDPI)** | 生物学 2 区 / 植物科学 2 区 | 否 | 「Plants-Basel has an impact factor of 4.7, Q1 in JCR, and 2区 in CAS classification for both the major discipline (生物学) and minor discipline (植物科学)」 | 中 |
| **Frontiers in Plant Science** | 2 区（基础版 2 区 · 新锐版 2 区） | 否 | ai4paper：「中科院基础版2区 · 中科院新锐版2区 · JCR Q1 · 影响因子 5.9」 | 中高 |
| **Journal of the Science of Food and Agriculture** | 新锐版 2 区（基础版待确认） | 否 | ai4paper 标题：「JOURNAL OF THE SCIENCE OF FOOD AND AGRICULTURE 是几区期刊？中科院新锐版2区」 | 中低 |
| **Molecular Breeding** | 基础版 3 区 / **新锐版 2 区** | 否 | 「MOLECULAR BREEDING is classified as 3区 in 中科院基础版 and 2区 in 中科院新锐版…impact factor 3.6, JCR Q1」 | 中 |
| **Frontiers in Sustainable Food Systems** | 基础版 3 区 / **新锐版 2 区** | 否 | 「中科院基础版3区，中科院新锐版2区，JCR Q2，影响因子 4.1」 | 中 |
| **China Agricultural Economic Review** | **经济学 2 区** / 农业经济与政策 2 区、经济学 2 区 | 否 | 「大类学科：经济学2区；小类学科：农业经济与政策 2区；经济学 2区；JCR分区等级为Q1」；ai4paper：「基础版2区 · 新锐版2区 · JCR Q1 · IF 4.4」 | 中高（两源一致） |
| **International Journal of Agricultural Sustainability** | 基础版 2 区 · 新锐版 2 区 | 否 | 「中科院基础版2区、中科院新锐版2区、影响因子5.9」 | 中 |
| **Agricultural and Food Economics** | 基础版 2 区 · 新锐版 2 区 | 否 | 「中科院基础版2区、中科院新锐版2区、影响因子5.4」 | 中 |
| **Outlook on Agriculture** | 基础版 2 区 · 新锐版 2 区 | 否 | 「中科院基础版2区、中科院新锐版2区、影响因子3.2」 | 中 |
| **Journal of Agronomy and Crop Science**（非候选，顺带） | 农林科学 2 区 / 农艺学 2 区 | 否 | 「中科院分区中属于农林科学2区；小类学科中属于 AGRONOMY 农艺学2区」 | 中 |

### 1.3 其余候选刊（3 区及以下 / 非农林大类）

| 期刊 | 分区 | 来源原话 | 置信度 |
|---|---|---|---|
| Food Policy | **经济学 1 区** | 「大类学科经济学1区，2025年影响因子为6.8」 | 中 |
| Journal of Rural Studies | **社会学 1 区** | 「大类学科社会学1区，2026年影响因子为5.7」 | 中 |
| Rice (Springer) | 农林科学（区未直接确认；Q1；OA 100% Gold） | 「Rice is published by Springer, with a 2026 impact factor of 5.8/Q1, is an open access journal (OA) with 100% Gold OA articles, classified under AGRONOMY」 | **待确认（分区）** |
| Food and Energy Security | 未检索到中科院分区 | 多次检索仅得 Wiley OA / CC-BY 说明 | **待确认** |
| Crop Science | 新锐版 3 区 | ai4paper 标题：「CROP SCIENCE 是几区期刊？中科院新锐版3区」；letpub 标题显示 IF 1.900 | 中低 |
| Euphytica | 农林科学 3 区 / 农艺学·园艺·植物科学 3 区；新锐版 3 区 | 「EUPHYTICA is classified as 3区 in 农林科学, and 3区 in Agronomy, Horticulture, Plant Science」；journalmetrics：「JCR Q2，IF 1.8（2026-06-17 发布）」 | 中 |
| Plant Breeding | 农林科学 3 区 / 农艺学 4 区；新锐版 3 区 | 「大类学科农林科学3区，小类学科 AGRONOMY 农艺学4区」 | 中 |
| Agronomy Journal | 农林科学 3 区 / 农艺学 3 区；新锐版 3 区 | 「大类学科农林科学3区，小类学科农艺学3区」；letpub 标题 IF 2.000 | 中 |
| Journal of Agricultural Science (Cambridge) | 新锐版 3 区 | ai4paper 标题：「JOURNAL OF AGRICULTURAL SCIENCE 是几区期刊？中科院新锐版3区」 | 中低 |
| Renewable Agriculture and Food Systems | 基础版 3 区 · 新锐版 3 区 | 「中科院基础版3区，中科院新锐版3区，JCR Q2，影响因子 2.4」 | 中 |
| Agribusiness | 基础版 3 区 · 新锐版 3 区 | 「中科院基础版3区、中科院新锐版3区、影响因子2.4」 | 中 |
| Frontiers of Agricultural Science and Engineering | 基础版 3 区 | 「中科院基础版3区，JCR Q1，影响因子 3.4」 | 中 |
| Plant Production Science | 未检索到中科院分区；JCR Q3 | 「2025 impact factor 1.3, JCR Q3, 5年平均 2.3」 | **待确认（分区）** |

---

## 2. 逐刊核实表（分区 / IF / JCR / 发文量 / OA & APC / 审稿周期）

> 说明：`—` = 本次未检索到；**待确认** = 存在冲突或仅单一弱来源。

### 2.1 作物科学 / 育种主干刊

**Journal of Integrative Agriculture (JIA)**
- 中科院：农林科学 1 区（小类 农业综合 2 区）；ai4paper 基础版 1 区 Top / 新锐版 1 区。
- IF：**5.7**（ai4paper，2026 口径）；另 journalmetrics.org 与 letpub 标题均写 **4.4**（2025 口径）→ 两代 JCR 并存。JCR Q1，「ranks Q1 (14/94) in Agriculture, Multidisciplinary」。
- 发文量：—（待确认）。
- OA/APC：KeAi 页面原话「**This journal does not charge open access fees to the authors. The open access fees are covered by JIA (CAAS).** However, CAAS will charge an Evaluating Fee for peer reviewed manuscript, and if the manuscript is accepted, it will also be charged for a Handling and Printing Fee.」另有来源称「up to 1000 USD」→ **实际收费项目待确认**（评审费 + 稿件处理/印刷费，非标准 APC）。
- 审稿周期：「publishes research articles in **12 weeks on an average**」；「acceptance to online publication period is **222 days**」；DOAJ 自报「submission to publication ~50 weeks」→ **数值分歧大，待确认**。

**The Crop Journal**
- 中科院：农林科学 1 区 Top（基础版 & 新锐版）。IF **6.7**，JCR Q1。
- 发文量：—。
- OA/APC：KeAi/Elsevier 混合，—（待确认）。
- 审稿周期：PJIP 原话「acceptance rate of **14%** and review speed of **10 days**」（"review speed 10 days" 疑为到首次决定的中位数或聚合站口径，**待确认**）。

**Rice Science**
- 中科院：农林科学 **2 区**（基础版 & 新锐版）。IF **7.4**（ai4paper，2026）/ **6.1**（journalmetrics，2025 口径）；JCR Q1；5 年 IF 5.6。
- 发文量：双月刊（bi-monthly），—。
- OA/APC：ai4paper 称「open access with **100% Gold OA** articles」；DOAJ 称「no publication fees (APCs)」；Elsevier OACS 称 OA 费用按作者情境个性化 → **冲突，待确认**（中国农科院水稻所主办，国内作者常报"无版面费"）。
- 审稿周期：journalmetrics「Submission to first decision **median of 6 days**」（极可能是 desk-decision 口径，**待确认**）。

**Field Crops Research**
- 中科院：农林科学 1 区 Top / 小类 农艺学 2 区。IF **7.9**（researcher.life，2026-06 更新）/ letpub 标题 **6.400**（旧）；CiteScore 10.5；JCR Q1；h-index 202。
- 发文量：**2025 年发表 377 篇**（researcher.life）。月刊。
- OA/APC：Hybrid + Open Access 均支持；APC 金额 —。
- 审稿周期：—（Elsevier journalissues 页未取到具体周数）。

**Agricultural Systems**
- 中科院：农林科学 1 区 Top / 农业综合 1 区。IF **6.2**（ai4paper）/ letpub 标题 6.100；CiteScore 9.7；SJR Q1；h-index 126。
- 发文量：月刊，—。
- OA/APC：Hybrid，—。
- 审稿周期：「**first review round for Agricultural Systems is 14.6 weeks**」（SciRev 口径）；另一聚合站给 "review speed 8 days"（不可信）→ 取 **≈14–15 周**，置信度中。

**European Journal of Agronomy**：农林科学 1 区 Top；IF 6.7（ai4paper）/ letpub 标题 5.500；其余 —。

**Agronomy for Sustainable Development**：农林科学 1 区 Top；IF **8.2**，5 年 IF 10.2，JCR Q1；其余 —。

**Rice (Springer/SpringerOpen)**
- 分区 **待确认**；IF **5.8**（2026 口径），Q1（Agronomy & Crop Science / Plant Science / Soil Science 均 Q1）；CiteScore 7.9；h-index 64（另一源 80）。
- OA/APC：全 OA，**APC = EUR 2390 / USD 2890 / GBP 1990**（Springer 官方页原话）；另有源给 €2690 → 以 2390 为主，标注可能已调价。
- 审稿周期：—。

**Food and Energy Security**：Wiley 全 OA，CC-BY；分区/IF/APC 均 **待确认**；提供 Free Format submission。

**Crop Science / Euphytica / Plant Breeding / Agronomy Journal / Molecular Breeding**：见 §1.3；APC 与审稿周期均 —。

**Plant Production Science**：IF 1.3，JCR Q3；分区待确认。→ **不建议**（分区过低，且偏栽培生理）。

**Frontiers of Agricultural Science and Engineering**：基础版 3 区，JCR Q1，IF 3.4。中国工程院主办、季刊、偏约稿综述，自由投稿录用不确定性高。

### 2.2 OA 快刊（MDPI / Frontiers）

**Agriculture (MDPI)**
- 分区 2 区（待确认）；IF **4.5**（2026 口径）；JCR Q1。
- OA/APC：全 OA，**CHF 2600**（2026 年 APC 表，官方页原话）。
- 审稿周期：**首次决定中位 18.8 天**（2026 上半年）。

**Agronomy (MDPI)**
- 分区 2 区（待确认）；IF **3.3–3.4**；JCR Q1。
- OA/APC：全 OA，**CHF 2600**（2026）。
- 审稿周期：**首次决定中位 17.7 天，接收到见刊 2.6 天**（官方 2026 上半年中位数）。

**Plants (MDPI)**：生物学/植物科学 2 区；IF 4.7（另源 4.1）；全 OA，APC 与 Agronomy 同量级（**待确认**）。

**Frontiers in Plant Science**
- 2 区（基础版 & 新锐版）；IF **5.9**；JCR Q1。
- OA/APC：**3,150 CHF**（A 型文章，含 Original Research）。
- Original Research 正文上限 **12,000 词**。

**Frontiers in Sustainable Food Systems**
- 基础版 3 区 / 新锐版 2 区；IF **4.1**；JCR Q2。
- OA/APC：**约 1,950 CHF**；有发展中国家 waiver 政策。

### 2.3 农经 / 产业政策刊

**China Agricultural Economic Review (CAER, Emerald)**
- 经济学 2 区（小类 农业经济与政策 2 区 / 经济学 2 区）；IF 4.4；JCR Q1。
- OA/APC：Emerald 混合，—（**待确认**）。
- 审稿周期：—（**待确认**）。

**Food Policy**：经济学 1 区；IF 6.8；Elsevier；其余 —。
**Journal of Rural Studies**：社会学 1 区；IF 5.7；Elsevier；其余 —。
**Agribusiness (Wiley)**：基础版/新锐版 3 区；IF 2.4；其余 —。
**Agricultural and Food Economics (Springer)**：2 区/2 区；IF 5.4；全 OA（APC 待确认）。
**International Journal of Agricultural Sustainability (T&F)**：2 区/2 区；IF 5.9；**自第 21 卷（2023）起转为全 OA**，APC 金额 **待确认**（官方页：「you may be asked to pay an Article Publishing Charge (APC)」）。
**Outlook on Agriculture (SAGE)**：2 区/2 区；IF 3.2；季刊。
**Global Food Security**：农林科学 1 区 Top；IF 7.5；以 short review / synthesis 为主。
**Renewable Agriculture and Food Systems (Cambridge)**：3 区/3 区；IF 2.4；JCR Q2。
**Journal of Agricultural Science (Cambridge)**：新锐版 3 区。

---

## 3. 范围契合度 + 可发表性证据（例文完整引文）

> 例文来源：本项目已核验的 `06_lit_breeding_refs.csv` / `07_lit_seed_industry_refs.csv`（维度 6/7 产物），加本次 Scholar Gateway 检索补充。每条含作者、年份、题名、刊名、卷期页、DOI。

### 3.1 契合度最高（既发"审定/区试数据性状演变"，又发"种业产业与政策"）

#### Journal of Integrative Agriculture — 契合度 9/10
**范围判断**：JIA 明确列出 Crop Science、Agro-Ecosystem and Environment 等核心栏目，同时长期刊发中国种业制度与农户行为的实证经济学论文（见下 2 条），是本文"育种性状演变 + 企业/科研单位主体差异"最自然的落点。企业深度案例需包装为"主体异质性分析中的代表性案例"。
**例文**：
1. Shi X., Hu R. (2017). Rice variety improvement and the contribution of foreign germplasms in China. *Journal of Integrative Agriculture*, 16(10), 2337–2345. DOI: 10.1016/S2095-3119(16)61615-5 —— **直接同类：基于中国水稻品种改良的品种级分析**。
2. Qiu H., Wang X., Zhang C., Xu Z. (2016). Farmers' seed choice behaviors under asymmetrical information: Evidence from maize farming in China. *Journal of Integrative Agriculture*, 15(8), 1915–1923. DOI: 10.1016/S2095-3119(15)61326-0 —— **种业经济学实证**。
3. Ma G., Yuan L. (2015). Hybrid rice achievements, development and prospect in China. *Journal of Integrative Agriculture*, 14(2), 197–205. DOI: 10.1016/S2095-3119(14)60922-9。
（另：Huang Z. et al. (2018). One size fits all? Contract farming among broiler producers in China. *JIA*, 17(2), 473–482. DOI: 10.1016/S2095-3119(17)61752-0 —— **订单农业主题在 JIA 有先例**，对本文"种粮一体化/订单农业"章节是关键的可发表性证据。）
**格式**：
- 文章类型：Commentary / Review / **Research Article** / Short Communication（≤2,500 词，≤2 图表）/ Letter（≤1,500 词，1 图 1 表）。Research Article **未规定字数上限**（原话：guide 只对 Short Communication 与 Letter 规定上限）。
- 摘要：**非结构式，≤250 词**（「a concise and factual abstract which does not exceed 250 words」；Elsevier 通用页另提"可用小标题的结构式摘要"→ 以 JIA 自有 250 词无结构为准）。
- 关键词：**3–6 个**（「provide 3 to 6 keywords…避免含 and/of 的多词词组」）。
- Highlights：Elsevier 平台鼓励，非强制（**待确认**是否必填）。Graphical Abstract：鼓励提供，单独文件，**最小 531 × 1328 px (h × w)**，5 × 13 cm @96 dpi 可读。
- 正文结构固定：Title → Abstract & Keywords → Introduction → Materials and Methods → Results → Discussion → Conclusion → Acknowledgements → References。
- 参考文献：**作者-年份（Harvard）**。原话：「Author-year citations are required…such as **(Crews and Davies 1986)** or **Crews and Davies (1986)**. Where there are more than two authors, only the first should be named followed by **et al.**」注意：**年份前无逗号**，这是 JIA 的特殊点。
  示例（期刊论文，按 JIA 风格推演，**格式细节待与官方样例核对**）：
  `Shi X, Hu R. 2017. Rice variety improvement and the contribution of foreign germplasms in China. Journal of Integrative Agriculture, 16, 2337–2345.`
- 投稿系统：**http://www.ChinaAgriSci.com**（编辑部：北京中关村南大街 12 号，jia_journal@caas.cn）。ScienceDirect/KeAi 同步托管。

#### China Agricultural Economic Review — 契合度 9/10（若把文章重心放在"育种主体差异 + 企业战略与财务后果"）
**范围判断**：CAER 是"中国农业经济 + 种业政策 + 订单农业"三主题重合度最高的刊，且对"用官方公告/行政数据构建面板"的方法高度友好。弱点：对纯农艺性状（稻瘟病抗性等级演变）的容忍度低，需把性状数据转成"技术进步/创新产出"的经济学变量。
**例文**：
1. Jin Y., Hu Y., Pray C., Hu R. (2017). Impact of government science and technology policies with a focus on biotechnology research on commercial agricultural innovation in China. *China Agricultural Economic Review*, 9(3), 438–452. DOI: 10.1108/CAER-05-2017-0096。
2. Zheng S., Xu P., Wang Z. (2012). Farmers' adoption of new plant varieties under variety property right protection: Evidence from rural China. *China Agricultural Economic Review*, 4(1), 124–140. DOI: 10.1108/17561371211196810。
3. Deng H., Hu R., Huang J., Pray C., Jin Y., Li Z. (2017). Attitudes toward GM foods, biotechnology R&D investment and lobbying activities among agribusiness firms in the food, feed, chemical and seed industries in China. *China Agricultural Economic Review*, 9(3), 385–396. DOI: 10.1108/CAER-10-2016-0162 —— **企业层面 R&D 投入实证**，与本文荃银研发投入分析同构。
（订单农业先例：Wang H., Zhang Y., Wu L. (2011). *CAER*, 3(4), 489–505. DOI: 10.1108/17561371111192347；Ma W., Abdulai A. (2016). *CAER*, 8(1), 2–21. DOI: 10.1108/CAER-04-2015-0035。）
**格式**（Emerald 通用 + CAER 页）：
- 参考文献：**Harvard（作者-年份）**（原话：「The journal uses the Harvard reference style」）。
- 关键词：**最多 6 个**（「up to 6 short, relevant keywords」）。
- 字数：「Word counts include all text, figures and tables, with approximately **280 words allowed for each figure or table**」——具体上限值 **待确认**（Emerald 常见 8,000–10,000 词含图表）。
- 摘要：Emerald 惯例为**结构化摘要**（Purpose / Design-methodology-approach / Findings / Originality-value），CAER 是否强制 **待确认**。
- 语言/格式：仅接受 UK 或 US 英语；正文须为 Microsoft Word。
- 投稿系统：Emerald 自有系统（ScholarOne 口径 **待确认**）。
- 示例（Harvard）：`Jin, Y., Hu, Y., Pray, C. and Hu, R. (2017), "Impact of government science and technology policies…", China Agricultural Economic Review, Vol. 9 No. 3, pp. 438-452.`

### 3.2 契合度较高

#### Agriculture (MDPI) — 契合度 8/10
**范围判断**：同时接受"品种性状演变的数据分析"与"种业政策演进 / 龙头企业—农户纵向协作"两类稿件，是本文**唯一一本同时有两类直接先例、且审稿快**的刊。风险是分区标注不稳（2 区/3 区口径冲突）与 APC。
**例文**：
1. Hu S., Xiong C., Jiang D. (2025). Enhancing the marketization and globalization response capacity of policies: Evolution of China's seed industry policies since the 21st century. *Agriculture*, 15(22), 2383. DOI: 10.3390/agriculture15222383。
2. Li L., Zhang L., Wang X. (2024). Research on the dynamic evaluation of the competitiveness of listed seed enterprises in China. *Agriculture*, 14(8), 1213. DOI: 10.3390/agriculture14081213 —— **上市种企竞争力定量评价，与荃银高科案例同构**。
3. Li W. et al. (2023). Factors influencing farmers' vertical collaboration in the agri-chain guided by leading enterprises: A study of the table grape industry in China. *Agriculture*, 13(10), 1915. DOI: 10.3390/agriculture13101915 —— **龙头企业纵向一体化**。
**格式**：摘要约 **200 词**；关键词 **3–10 个**；APC **CHF 2600**（2026）；首次决定中位 **18.8 天**；参考文献 **编号制（ACS-like，方括号 [1]）**。示例：`1. Hu, S.; Xiong, C.; Jiang, D. Enhancing the marketization and globalization response capacity of policies. Agriculture 2025, 15, 2383.` 投稿系统：MDPI SuSy（susy.mdpi.com）。Graphical Abstract 可选，无 Highlights 强制。

#### Agronomy (MDPI) — 契合度 8/10
**范围判断**：本项目检索到的"中国水稻审定品种性状演变"论文**最密集**的刊（11 条中 5 条是直接同类），且设有 "Economics and Policy in the Agricultural Transition" 类专刊，可同时容纳产业分析。
**例文**：
1. Zou Y. et al. (2024). Evaluation of Breeding Progress and Agronomic Traits for Japonica Rice in Anhui Province, China (2005–2024). *Agronomy*, 14(12), 2957. DOI: 10.3390/agronomy14122957 —— **安徽省 + 2005–2024 区间，与本文数据集时空范围几乎完全重合**。
2. Hang S. et al. (2024). Evolution of Rice Cultivar Performance Across China: A Multi-Dimensional Study on Yield and Agronomic Characteristics over Three Decades. *Agronomy*, 14(12), 2780. DOI: 10.3390/agronomy14122780 —— 摘要原话：「utilized data from **11,811 cultivar trials** conducted between 1990 and 2023」，**证明该刊接受大规模区试/审定数据的性状演变分析**。
3. Lu Y. et al. (2024). Variations and Trends in Rice Quality across Different Types of Approved Varieties in China, 1978–2022. *Agronomy*, 14(6), 1234. DOI: 10.3390/agronomy14061234 —— **"国审品种 + 稻米品质趋势"直接同题**。
（政策侧先例：Zhao Y., Deng H., Hu R., Xiong C. (2022). Impact of government policies on seed innovation in China. *Agronomy*, 12(4), 917. DOI: 10.3390/agronomy12040917。）
**格式**：同 Agriculture（摘要 ~200 词、关键词 3–10、编号制参考文献、SuSy 投稿），APC **CHF 2600**，首次决定中位 **17.7 天**，接收到见刊 **2.6 天**。

#### Rice Science — 契合度 8/10
**范围判断**：水稻专刊，对"三系/两系杂交稻五十年产量—品质—抗性同步改良"这类长时段品种级综述与实证有明确先例；但对企业财务与供应链战略的容忍度低，需将产业部分压缩为讨论。
**例文**：
1. Gong J. et al. (2026). Three-Line Hybrid Rice in China: Sustained Improvements in Yield, Quality, and Resistance Over Fifty Years. *Rice Science*（2026-04 在线，卷期页待补）. DOI: 10.1016/j.rsci.2026.04.004 —— **与本文核心分析框架几乎一致，是最强的可发表性证据，同时也是最强的"撞车风险"**。
2. Xiao N., Wu Y., Li A. (2020). Strategy for Use of Rice Blast Resistance Genes in Rice Molecular Breeding. *Rice Science*, 27, 263–277. DOI: 10.1016/j.rsci.2020.05.003。
3. Cao L. et al. (2010). Breeding Methodology and Practice of Super Rice in China. *Rice Science*（卷期页待补）。
**格式**：标题 ≤30 词；running title <80 字符；**摘要 ≤350 词**；**关键词 3–8 个**；参考文献 **author-date 体系**（原话：「Rice Science uses the author-date system for citing references, and only published or in-press literatures may be cited」）；Elsevier 在线投稿（ricesci.org 亦有指南）。Highlights/Graphical Abstract **待确认**。

#### Frontiers in Sustainable Food Systems — 契合度 8/10
**范围判断**：设 "Agricultural and Food Economics"、"Land, Livelihoods and Food Security" 等 section，同时已发表"杂交稻扩散与产量效应"和"龙头企业引导农户"的实证——是本文**跨学科定位最宽容**的刊。分区（新锐 2 区 / 基础 3 区）是代价。
**例文**：
1. Wang Q., Bin B., Wang H. (2023). Dynamic diffusion of hybrid rice varieties and the effect on rice production: evidence from China. *Frontiers in Sustainable Food Systems*, 7, 1071234. DOI: 10.3389/fsufs.2023.1071234。
2. Yan Z. et al. (2022). An economic assessment of adoption of hybrid rice: Micro-level evidence from southern China. *Frontiers in Sustainable Food Systems*, 6, 1066657. DOI: 10.3389/fsufs.2022.1066657。
3. Liu C., Li W., You Y., Yang Q., Li M. (2025). Research on leading agricultural enterprises guiding farmers' participation in pre-production quality and safety control: evidence from the Yangtze River Delta Region of China. *Frontiers in Sustainable Food Systems*, 9, 1615223. DOI: 10.3389/fsufs.2025.1615223。
（品种改良先例：Wang H. et al. (2022). Grain yield improvement in high-quality rice varieties released in southern China from 2007 to 2017. *Front. Sustain. Food Syst.*, 6, 986655. DOI: 10.3389/fsufs.2022.986655。）
**格式**：APC **≈1,950 CHF**；Original Research 属 A 型；Frontiers 参考文献默认 **编号制（Frontiers reference style）**，摘要上限与关键词数 **待确认**；投稿系统：Frontiers 自有平台。

### 3.3 契合度中等 / 有条件

- **Field Crops Research（9/10 分区，6/10 契合）**：11 条例文全部是再生稻、机械化栽培、产量生理，**无一条是"审定数据驱动的性状演变"或"种业产业"**。典型例文：Huang M., Zou Y. (2018). Integrating mechanization with agronomy and breeding to ensure food security in China. *Field Crops Research*, 224, 22–27. DOI: 10.1016/j.fcr.2018.05.001。→ 若投，必须把论文重写为"性状演变对大田生产力的意义"，删去企业财务部分。格式：摘要 ≤**400 词**；**Highlights 必需**（独立文件，3–5 条，每条 ≤85 字符含空格）；鼓励 Graphical Abstract；要求 CRediT 与 Data Availability；参考文献格式 **待确认（两源冲突：scispace 模板称 elsarticle-num 编号制，而 FCR 已刊论文正文普遍为作者-年份 Harvard——投稿前必须核对官方 Guide for Authors）**；Editorial Manager 投稿。
- **The Crop Journal（10/10 分区，5/10 契合）**：仅 1 条相关例文（Liao C. et al. (2021). Innovation and development of the third-generation hybrid rice technology. *The Crop Journal*. DOI: 10.1016/J.CJ.2021.02.003），且该刊以分子/遗传机制为主，产业与政策几乎不发。格式：**摘要 200–300 词 + 3–5 关键词**；Research paper **正文 ≤7,000 词、约 7 个图表、参考文献 ≤70**；投稿系统 **https://www.editorialmanager.com/cj/default.aspx**；录用率 **14%**。
- **Agricultural Systems（9/10 分区，7/10 契合）**：有 Spielman D.J., Kennedy A. (2016). Towards better metrics and policymaking for seed system development: Insights from Asia's seed industry. *Agricultural Systems*, 147, 111–122. DOI: 10.1016/j.agsy.2016.05.015 —— **"种业体系度量与政策"直接先例**；另 Reardon T. et al. (2019). *Agricultural Systems*, 172, 47–59. DOI: 10.1016/j.agsy.2018.01.022。格式：摘要约 **250 词**；Research paper **≤8,000 词**（Short communication 4,000 / Perspective 2,000 / Comment 1,000）；**要求 Highlights + Graphical Abstract + CRediT + Data Availability**；首轮评审 **≈14.6 周**。风险：该刊偏"系统建模/情景分析"，纯描述性趋势分析易被拒。
- **Frontiers in Plant Science（2 区，6/10 契合）**：有 4 条"中国审定品种产量/品质演变"例文，最具代表：Li R. et al. (2019). Exploring the Relationships Between Yield and Yield-Related Traits for Rice Varieties Released in China From 1978 to 2017. *Frontiers in Plant Science*, 10, 543. DOI: 10.3389/fpls.2019.00543；Fan J.-J. et al. (2024). Phenotypic evolution of appearance quality and cooking and taste quality of hybrid rice over the past 40 years in China. *Front. Plant Sci.*, 15, 1512760. DOI: 10.3389/fpls.2024.1512760。→ **育种部分极契合，但企业/产业链部分必须完全删除**。APC 3,150 CHF，Original Research ≤12,000 词。
- **Rice (Springer)（分区待确认，5/10 契合）**：9 条例文全是分子/抗性/制种技术，唯一相关是 Seck F. et al. (2023). Realized Genetic Gain in Rice: Achievements from Breeding Programs. *Rice*, 16. DOI: 10.1186/s12284-023-00677-6。APC EUR 2390。
- **Agribusiness（3 区，8/10 契合但分区低）**：**种业企业主题最密集的经济学刊**。关键例文：Xie Z., Yuan S., Zhu J., Li W. (2023). Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? *Agribusiness*, 39(4), 1173–1198. DOI: 10.1002/agr.21823 —— **"种企主导的订单农业"与荃银"种粮一体化"直接对应**；Xiang C., Yang R., Wang X., Huang J. (2025). Impact of seed regulation reform on licensing fees of varieties in China. *Agribusiness*. DOI: 10.1002/agr.22020；Su Z., Zhang M., Sun J., Wu W. (2022). Agribusiness diversification and technological innovation efficiency: A U-shaped relationship. *Agribusiness*, 39(2), 322–346. DOI: 10.1002/agr.21785 —— **上市农企多元化与创新效率，正是荃银"纵向延伸 + 财务后果"的对标文献**。→ 契合度极高，但中科院 3 区，不满足"2 区"硬指标。
- **Food and Energy Security（分区待确认，6/10）**：Li X. et al. (2021). Inter-annual climate variability constrains rice genetic improvement in China. *Food and Energy Security*, 10(4). DOI: 10.1002/FES3.299 —— 直接同类。
- **Food Policy（经济学 1 区，7/10）**：Li J.-J. et al. (2026). Premium procurement channel access and farm-gate prices: evidence from rice farmers in China. *Food Policy*, 103132. DOI: 10.1016/j.foodpol.2026.103132 —— **优质稻订单收购渠道，与"订单农业"高度相关**。门槛高、要求强因果识别，单一企业案例难过审。
- **Journal of Rural Studies（社会学 1 区，6/10）**：Xu S., Cao C. (2025). Historical transitions of seed breeding in China: From socialist cooperation to joint research. *Journal of Rural Studies*, 114, 103592. DOI: 10.1016/j.jrurstud.2025.103592 —— **中国育种体制史**，定性传统强，定量品种数据分析非其主流。
- **Crop Science（3 区，6/10）**：接受遗传增益分析且有中国样本：Yang H. et al. (2021). Genetic progress in grain yield radiation and nitrogen use efficiency of dryland winter wheat in Southwest China since 1965. *Crop Science*, 61(6), 4255–4272. DOI: 10.1002/csc2.20608；Liu M. et al. (2021). Genetic progress in grain yield and the associated physiological traits of popular wheat in southwestern China from 1969 to 2012. *Crop Science*, 61(3), 1971–1986. DOI: 10.1002/csc2.20448。
- **Plant Breeding（3 区，6/10）**：Achilli A. et al. (2025). Genetic Gains in Durum Wheat Across the Globe: Yield, Quality and Adapting for Variable Weather Patterns. *Plant Breeding*, 145(1), 142–165. DOI: 10.1111/pbr.70029。
- **Molecular Breeding（新锐 2 区，4/10）**：分子标记/基因聚合为主（Wang K. et al. (2025). DOI: 10.1007/s11032-025-01555-3），不适合本文。
- **Global Food Security（1 区 Top，5/10）**：Deconinck K. (2019). New evidence on concentration in seed markets. *Global Food Security*, 23, 135–138. DOI: 10.1016/j.gfs.2019.05.001 —— 种业集中度短评。该刊以 short synthesis 为主，不接受长篇原创实证。
- **Agricultural and Food Economics（2 区，7/10）**：Kala-Satheesh H.K. et al. (2024). Seed market dynamics and diffusion of new wheat varieties in Bihar, India: a supply-side perspective. *Agricultural and Food Economics*, 12. DOI: 10.1186/s40100-024-00330-w —— **种子市场供给侧视角**，与本文"育种主体差异"呼应。
- **JSFA（新锐 2 区，4/10）**：品质化学为主（Yuan S. et al. (2022). *JSFA*, 102(15), 7259–7267. DOI: 10.1002/jsfa.12091）。
- **Agronomy Journal（3 区）**：Liu K., Huang M. (2026). *Agronomy Journal*, 118(3). DOI: 10.1002/agj2.70407。
- **Plants（2 区，3/10）**、**Euphytica（3 区，4/10）**、**J. Agric. Sci. Cambridge（3 区）**、**Renewable Agriculture and Food Systems（3 区）**、**Plant Production Science（Q3）**、**Frontiers of Agricultural Science and Engineering（3 区，季刊多约稿）**：均不推荐为首投。
- **Outlook on Agriculture（2 区）/ International Journal of Agricultural Sustainability（2 区）**：**本次未检索到任何"中国种业/杂交稻/品种审定数据"同类例文**，可发表性证据 = 无。IJAS 官方原话更明确排斥本文的数据类型：「**IJAS tends not to publish technical or experimental findings, derived from field or laboratory based studies, unless they explicitly and comprehensively discuss the sustainability aspects**」→ 除非把全文重写为可持续性论证，否则不建议。Outlook on Agriculture 原话：「welcomes perspectives, reviews and original research papers on current developments in agricultural research for development」，字数/摘要/参考文献细节 **待确认**。

---

## 4. 初步推荐前 5 名

| 排名 | 期刊 | 分区（口径） | IF | 审稿周期 | 格式负担 | 证据强度 | 一句话理由 |
|---|---|---|---|---|---|---|---|
| **1** | **Journal of Integrative Agriculture** | 农林科学 **1 区**（小类农业综合 2 区） | 5.7 / 4.4 | ~12 周（存疑） | 中（250 词摘要、3–6 关键词、作者-年份、无强制 Highlights） | **强**（品种改良 + 种子选择行为 + 订单农业三类先例齐全） | 唯一同时容纳"品种级性状演变""育种主体差异""企业-农户订单"三块内容，且是中国农科院主办、对中国行政数据集最友好的 1 区刊 |
| **2** | **Agronomy (MDPI)** | 农林科学 **2 区**（待确认） | 3.3–3.4 | **首次决定 17.7 天** | 低（200 词摘要、编号制、无 Highlights） | **最强**（"国审品种 1978–2022 品质趋势""安徽 2005–2024 育种进展""11,811 个区试数据"三篇几乎同题同域） | 同类论文命中率最高、周期最短、格式负担最轻，是把 2,400 个国审品种数据集变现的最稳路径，代价是 CHF 2600 与 MDPI 声誉折价 |
| **3** | **China Agricultural Economic Review** | **经济学 2 区**（农业经济与政策 2 区） | 4.4 | 待确认 | 中（Harvard、≤6 关键词、可能需结构化摘要） | **强**（种业政策/品种权/企业 R&D/订单农业四类先例） | 若把主线定为"育种主体差异 + 企业纵向一体化的财务后果"，这是分区达标且能完整保留荃银案例与财务分析的最佳刊 |
| **4** | **Rice Science** | 农林科学 **2 区** | 7.4 / 6.1 | 待确认（首次决定中位 6 天存疑） | 中（350 词摘要、3–8 关键词、作者-年份） | **强但撞车**（Gong et al. 2026 三系杂交稻五十年产量-品质-抗性同题） | 水稻专刊 + 2 区 + 高 IF + 可能零版面费，性状演变部分完美落位；须用"企业 vs 科研单位主体差异"作为与 Gong et al. (2026) 的差异化卖点 |
| **5** | **Agriculture (MDPI)** | 农林科学 **2 区**（待确认） | 4.5 | **首次决定 18.8 天** | 低 | **强**（种业政策演进 2025 + 上市种企竞争力评价 2024 + 龙头企业纵向协作 2023） | 产业/政策侧例文比 Agronomy 更贴近"上市种企 + 纵向一体化"，可完整承载荃银案例；与 Agronomy 互为备选，按稿件重心（农艺 vs 产业）二选一 |

**备选第 6**：Frontiers in Sustainable Food Systems（新锐 2 区 / 基础 3 区，APC ≈1,950 CHF）——跨学科容忍度最高、杂交稻扩散与龙头企业两类先例齐全，适合"分区可放宽、要求一次通过"的场景。
**证据最强但分区不达标**：Agribusiness（3 区）——"种企主导订单农业"（DOI: 10.1002/agr.21823）与"农企多元化-创新效率 U 型"（DOI: 10.1002/agr.21785）是全表与本文产业部分最同构的两篇，若评价体系允许 3 区，命中率最高。

### 各刊主要风险

| 期刊 | 主要风险 |
|---|---|
| **JIA** | ① **主体差异（企业 vs 科研单位）的因果识别**：审稿人会问"企业育成品种表现更好，是选育能力差异还是申报策略/试点选择差异？"需要至少一个准实验设计或选择性偏误检验。② 单一企业深度案例与前半段全国面板分析**在方法论上割裂**，易被要求拆成两篇。③ 审稿周期报道值离散（12 周 vs 222 天 vs 50 周），时间风险不可控。④ 收费结构不透明（评审费 + 处理印刷费）。 |
| **Agronomy (MDPI)** | ① **与 Zou et al. (2024, 安徽 japonica 2005–2024)、Lu et al. (2024, 国审品种品质 1978–2022) 高度重叠**，新颖性会被直接质询，必须以"企业 vs 科研单位主体维度 + 抗性等级 + 荃银案例"三点立异。② MDPI 在部分中国高校/评审语境中被折价，且"2 区"标注在 2025 官方升级版中**尚未确证**（2022 版为 3 区）——若单位以官方表为准，存在踩空风险。③ APC CHF 2600。④ 产业链/财务部分在农艺刊里显得突兀。 |
| **CAER** | ① **单一企业案例的一般性**是该刊审稿人最标准的攻击点——需明确定位为"理论抽样的极端案例"，并补充同行业 3–5 家上市种企的对照面板（项目已有 `05_competitor_financials.csv`，应前置使用）。② 财务后果分析若只有荃银一家时间序列，**内生性/反向因果**（是业绩好才做一体化，还是一体化带来业绩）必须处理。③ 农艺性状指标需全部翻译为经济学可解释变量，否则会被认为"两篇论文缝合"。④ Emerald 结构化摘要与字数上限待确认，可能返工。 |
| **Rice Science** | ① **与 Gong et al. (2026) 正面撞车**（同刊、同题材、2026 年 4 月刚发），编辑很可能以"重复"直接退稿——必须在 cover letter 里逐点说明差异。② 企业战略/财务内容基本无法保留，需整体砍掉或压成讨论段。③ OA/版面费三源冲突，需投前致函编辑部确认。④ "首次决定中位 6 天"若为 desk-reject 口径，实际是高退稿风险信号。 |
| **Agriculture (MDPI)** | ① 与 Agronomy 同属 MDPI，分区口径同样待确证（2022 版 3 区）。② 育种/农艺性状深度分析在该刊例文中较少，前半段品种数据可能被认为"不够 Agriculture"。③ APC CHF 2600。④ 快审带来的"水刊"标签风险。 |
| **（共性）单一企业案例风险** | 所有刊的共同攻击面。缓解方案：把荃银高科定位为"**对照全国面板得到的主体差异假说的机制验证案例**"，而非独立结论来源；并用已有的 `05_competitor_financials.csv`（竞争对手财务）与 `company_panel.csv` 构造至少 1 组对照，把 n=1 提升为 n=5±。 |

---

## 5. 仍待确认清单（按优先级）

1. **【最高】2025 年中科院分区表农林科学大类 1 区 / 2 区完整名单**——本次无法获取（页面全被 egress 拦截）。需人工：微信公众号「期刊分区表（fenqubiao）」→ 服务 → 分区查询；或机构账号登录 www.fenqubiao.com 下载升级版 Excel。
2. **【最高】候选刊在 2025 年官方升级版中的准确大类/小类/Top 标记**——本报告的 "基础版/新锐版" 标签来自第三方站点（ai4paper.pro、iikx.com），**不等于官方 2025 表**。尤其需复核：Agriculture (MDPI)、Agronomy (MDPI)、Rice Science、JSFA、Molecular Breeding、Frontiers in Sustainable Food Systems 的 2 区归属。
3. **【高】Field Crops Research 参考文献格式**——两源冲突（scispace 模板 "elsarticle-num" 编号制 vs 已刊论文的作者-年份）。以官方 Guide for Authors 为准。
4. **【高】CAER 的字数上限与摘要是否必须结构化**、投稿系统是否为 ScholarOne。
5. **【高】Rice Science 的 OA 状态与版面费**（DOAJ"无 APC" vs Elsevier OACS"个性化 OA 费用" vs ai4paper"100% Gold OA"三源冲突）。
6. **【中】JIA 的实际收费**（Evaluating Fee + Handling and Printing Fee 的金额）与 Research Article 是否有隐性篇幅上限；Highlights 是否必填。
7. **【中】各刊年发文量**：仅取到 Field Crops Research 2025 年 **377 篇**；JIA、The Crop Journal、Rice Science、Agricultural Systems、CAER、Agronomy/Agriculture (MDPI) 的年发文量均未取到。
8. **【中】平均审稿周期**：Agricultural Systems ≈14.6 周（首轮）、Agronomy 17.7 天、Agriculture 18.8 天为较可信；JIA、The Crop Journal、Rice Science、FCR、CAER 的数值缺失或互相矛盾。
9. **【中】Food and Energy Security、Rice (Springer)、Plant Production Science 的中科院分区**。
10. **【中】Outlook on Agriculture 与 IJAS 的字数/摘要/参考文献细则**，以及 IJAS 转 OA 后的 APC 金额。
11. **【低】MDPI Plants 的 APC**；Frontiers 各刊摘要字数上限；Global Food Security 的文章类型限制。
12. **【方法论】** 建议在正式投稿前，用机构 VPN 打开目标刊官方 Guide for Authors 与 fenqubiao.com，对本表逐行复核；本报告所有"中/中低"置信度项均不应直接写入投稿材料。

---

## 6. 来源清单（本次检索直接引用/据以生成 AI 摘要的页面）

**分区表与规则**
1. https://www.instrument.com.cn/news/20250320/773513.shtml
2. https://blog.csdn.net/glldxh/article/details/146424374 （被拦截，仅标题/摘要）
3. https://zhuanlan.zhihu.com/p/31844723614 （被拦截）
4. https://zhuanlan.zhihu.com/p/31570250378
5. https://zhuanlan.zhihu.com/p/31717079536
6. https://www.kejianyi.cn/news/detail/1729
7. https://www.academicenter.com/news/details/1902920599305723904.html
8. https://www.uconf.com/news/2933
9. https://blog.csdn.net/T0620514/article/details/147661518
10. https://www.fenqubiao.com/ ；https://www.fenqubiao.com/landing.html
11. https://www.sohu.com/a/1001021312_121252874 （2026 新锐分区表）
12. https://zhuanlan.zhihu.com/p/2020046052250646232
13. https://www.academicenter.com/news/details/2036671685663072256.html
14. https://lib.qau.edu.cn/content/fwqkdh/9a26517ab3a54017a98da330cf3e5082

**期刊分区/指标聚合站**
15. https://ai4paper.pro/journal/rice-science/
16. https://ai4paper.pro/journal/crop-journal/
17. https://ai4paper.pro/journal/journal-of-integrative-agriculture/
18. https://ai4paper.pro/journal/field-crops-research/
19. https://ai4paper.pro/journal/agricultural-systems/
20. https://ai4paper.pro/journal/european-journal-of-agronomy/
21. https://ai4paper.pro/journal/agronomy-for-sustainable-development/
22. https://ai4paper.pro/journal/global-food-security-agriculture-policy-economics-and-environment/
23. https://ai4paper.pro/journal/china-agricultural-economic-review/
24. https://ai4paper.pro/journal/frontiers-in-plant-science/
25. https://ai4paper.pro/journal/frontiers-in-sustainable-food-systems/
26. https://ai4paper.pro/journal/international-journal-of-agricultural-sustainability/
27. https://ai4paper.pro/journal/agricultural-and-food-economics/
28. https://ai4paper.pro/journal/outlook-on-agriculture/
29. https://ai4paper.pro/journal/agribusiness/
30. https://ai4paper.pro/journal/renewable-agriculture-and-food-systems/
31. https://ai4paper.pro/journal/frontiers-of-agricultural-science-and-engineering/
32. https://ai4paper.pro/journal/molecular-breeding/ ；https://ai4paper.pro/journal/euphytica/ ；https://ai4paper.pro/journal/crop-science/ ；https://ai4paper.pro/journal/plant-breeding/ ；https://ai4paper.pro/journal/agronomy-journal/ ；https://ai4paper.pro/journal/journal-of-agricultural-science/ ；https://ai4paper.pro/journal/journal-of-the-science-of-food-and-agriculture/
33. https://researcher.life/journal/field-crops-research/9554
34. https://www.journalmetrics.org/journal/journal-of-integrative-agriculture ；/rice-science ；/euphytica
35. https://www.iikx.com/sci/agriculture/12474.html （FCR，被拦截，仅摘要）
36. https://www.iikx.com/sci/agriculture/9997.html （Agricultural Systems）
37. https://www.pjip.org/journal/1006456/the-crop-journal ；https://www.pjip.org/journal/1005879/journal-of-integrative-agriculture
38. https://scirev.org/journal/agricultural-systems/

**Guide for Authors / 投稿与费用**
39. https://www.sciencedirect.com/journal/journal-of-integrative-agriculture/publish/guide-for-authors ；https://www.keaipublishing.com/en/journals/journal-of-integrative-agriculture/guide-for-authors/ ；https://www.chinaagrisci.com/Jwk_zgnykxen/EN/column/column23.shtml
40. https://www.keaipublishing.com/en/journals/journal-of-integrative-agriculture/open-access/
41. https://www.sciencedirect.com/journal/rice-science/publish/guide-for-authors ；http://www.ricesci.org/EN/column/column6.shtml ；http://www.ricesci.org/fileup/1672-6308/ITEM/20230528165324.pdf
42. https://www.sciencedirect.com/journal/field-crops-research/publish/guide-for-authors
43. https://www.keaipublishing.com/en/journals/the-crop-journal/guide-for-authors/ ；https://www.editorialmanager.com/cj/default.aspx
44. https://www.sciencedirect.com/journal/agricultural-systems/publish/guide-for-authors
45. https://www.emeraldgrouppublishing.com/journal/caer ；https://www.emerald.com/caer
46. https://www.mdpi.com/journal/agronomy/apc ；https://www.mdpi.com/journal/agriculture/apc ；https://www.mdpi.com/about/apc-2026 ；https://www.mdpi.com/journal/agronomy/instructions ；https://www.mdpi.com/journal/agriculture/instructions
47. https://www.frontiersin.org/journals/sustainable-food-systems/for-authors/publishing-fees ；https://www.frontiersin.org/journals/plant-science/for-authors/article-types ；https://www.frontiersin.org/journals/plant-science/for-authors/publishing-fees
48. https://thericejournal.springeropen.com/submission-guidelines/fees-and-funding ；https://link.springer.com/journal/12284/submission-guidelines
49. https://journals.sagepub.com/author-instructions/oag ；https://journals.sagepub.com/home/OAG
50. https://www.tandfonline.com/journals/tags20/about-this-journal
51. https://onlinelibrary.wiley.com/page/journal/20483694/homepage/forauthors.html

**例文来源（复用已核验证据）**
52. `/home/user/video/evidence/06_lit_breeding_refs.csv`（88 条，维度 6）
53. `/home/user/video/evidence/07_lit_seed_industry_refs.csv`（100 条，维度 7）
54. Scholar Gateway semanticSearch ×2（落盘：`mcp-Scholar_Gateway-semanticSearch-1789405141133.txt` / `-1789405142338.txt`）
