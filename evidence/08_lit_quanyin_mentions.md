# 维度 8：学术文献中荃银高科 / Winall / 荃银系品种的直接记载

| 项 | 内容 |
|---|---|
| 维度 | 08 — 学术文献中荃银高科（安徽荃银高科种业股份有限公司，300087，Winall Hi-Tech Seed Co., Ltd.）及其品种的直接记载 |
| 检索次数 | 53 次工具调用（WebSearch 40；Scholar Gateway semanticSearch 1；PubMed search_articles 2 + get_article_metadata 1；Undermind get_orientation/list_workspaces/launch_deep_search/inspect_deep_searches×3/search_papers/get_paper_info×2 = 9；Amass PatentCore 1（账户配额耗尽，未返回结果）） |
| 来源数（工具） | 4 类可用工具：WebSearch、Scholar Gateway（Wiley 全文语料）、PubMed（NCBI）、Undermind（全球学术语料 + 深度检索） |
| 找到条目数 | **47 条**（A 类国际期刊 14 条；B 类中文期刊/案例 33 条） |
| 可提取定量数据条目 | 24 条（见 `08_quanyin_lit_data.csv`） |
| 更新时间 | 2026-09-14 |

## 0. 检索策略与可信度说明

**检索式覆盖**：
- 英文/国际：`Anhui Winall Hi-tech Seed`、`Winall[Affiliation]`（PubMed）、`Quanyou / Quan9311A / Quan9311B / Quanyousimiao (QYSM) / Huiliangyou / Xinliangyou / Quanliangyou`、`contract farming seed enterprise China`、`ratoon rice variety screening China`。
- 中文：`荃优822 / 荃优华占 / 荃优1606 / 荃优607 / 荃优丝苗 / 荃9优 / 荃两优1606 / 荃两优851 / 荃两优丝苗 / 徽两优6号 / 徽两优898 / 徽两优882 / 徽两优丝苗 / 新两优6号 / 新两优223 / 新两优343 / 新两优901 / 新两优106` × `选育 / 栽培技术 / 区域试验 / 再生稻 / 直播 / 机插 / 氮肥 / 密度 / 稻米品质 / 稻瘟病抗性 / 耐热性`，以及 `荃银高科 + 案例 / 并购 / 订单农业 / 企业创新`。

**可信度分级（confidence 列）**：
- `high` = 通过 PubMed / DOI / 期刊官网直接取得完整著录（作者-年-题-刊-卷期页-DOI）。
- `medium` = 题名、作者、刊名、年份可确认，但卷/期/页码或 DOI 缺失（Undermind 索引未带完整著录，或中文刊网页未给出页码）。
- `low` = 仅通过二级索引（参考网/维普/科研之友摘要页）确认题名与年份，著录不完整；引用前须回 CNKI/维普核验。

**环境限制**：容器内 WebFetch/curl 对 CNKI、万方、维普、期刊官网全部被代理拦截，无法抓取原文页面核对页码；Amass PatentCore（专利检索）账户配额已耗尽（重置日 2026-09-30），**植物新品种权与专利维度本轮未能完成**（见 §6 Gaps）。

---

## 1. A 类：国际期刊中 Winall / 荃银品种的直接记载（14 条，全部 DOI 可验证）

### A1. 荃银高科作为**作者单位**的论文（PubMed `Winall[Affiliation]` 精确命中，6 条）

**A1-1** ⭐ 核心证据
> Zhang, C., Zhang, X., Zhao, X., Zhu, J., Chen, J., Zhou, Y., Wu, Y., Li, Z., Zheng, H., Wang, Y., Yan, Z., Fei, Q., Li, S., Chen, D., & Xu, C. (2022). Genomic Architecture of Yield Performance of an Elite Rice Hybrid Revealed by its Derived Recombinant Inbred Line and Their Backcross Hybrid Populations. **Rice (New York, N.Y.)**, 15(1): 49. DOI: 10.1186/s12284-022-00595-z

- **来源工具**：PubMed（PMID 36181551）+ get_article_metadata
- **角色**：**作者单位 + 研究对象品种**。作者中 Zhang Conghe（张聪聪）、Zhou Guixiang（周桂香）、Yan Zhi（严志）、Fei Qinyong（费勤勇）、Chen Jinjie（陈金节，通讯，m13505601533@163.com）署名 "Winall Hi-Tech Seed Co., Ltd., Hefei, 230088, Anhui, China"。
- **研究对象**：精英杂交稻组合 **荃优丝苗（Quan-you-si-miao, QYSM）**，构建 1061 份 RIL 与 1061 份 BCF1 群体，全基因组测序解析产量杂种优势遗传架构。
- **可提取数据**：群体规模 1061 RIL / 1061 BCF1；亲本为 **Quan9311B（荃9311B）× 五山丝苗（Wushansimiao）**。
- **意义**：这是**荃银高科科研人员署名的最高水平国际论文之一**，直接把公司主打品种荃优丝苗写进国际主流稻作期刊。

**A1-2** ⭐ 核心证据
> Zhang, C., Zhang, X., Zhao, X., ... Zheng, L. 见 A1-1 团队延伸；另见：Ren, Y., Fu, L., **Zhang, C.**, **Yang, W.**, **Zhou, G.**, Xu, T., Liu, W., Liu, C., & Zheng, L. (2026). A high-amylose maize starch hydrogel mask for stabilized encapsulation of thyme essential oil with Higuchi-controlled release. **International Journal of Biological Macromolecules**, 370: 152819. DOI: 10.1016/j.ijbiomac.2026.152819

- **来源工具**：PubMed（PMID 42219099）
- **角色**：**作者单位**（Winall Hi-Tech Seed Co., Ltd., Hefei 230088）。合肥工业大学食品与生物工程学院 + 荃银高科联合。
- **数据**：高直链玉米淀粉（HAMS）水凝胶，百里香精油释放 30 h 累积 30%，抑菌圈 22 mm（金黄色葡萄球菌）/20 mm（大肠杆菌）。
- **意义**：证明荃银高科**已把高直链玉米（功能型专用玉米）做成对外科研合作产出**，是"种业 → 食品/功能配料"的产业链延伸证据。

**A1-3**
> Fu, L., Ren, Y., **Zhang, C.**, **Yang, W.**, **Zhou, G.**, Xu, T., Liu, C., & Zheng, L. (2026). Caffeic acid-grafted high-amylose maize starch for self-stabilizing emulsion gels: efficient encapsulation and protection of pterostilbene. **Food Chemistry**, 520: 149832. DOI: 10.1016/j.foodchem.2026.149832

- **来源工具**：PubMed（PMID 42218866）；**角色**：作者单位（Winall Hi-Tech Seed Co., Ltd.）。
- **数据**：接枝度 4%/8%/12% 的咖啡酸接枝高直链玉米淀粉（Cf-HAMS），C-6 羟基共价接枝（NMR/FTIR/XPS 证实）。

**A1-4**
> Fu, L., Ren, Y., **Zhang, C.**, **Yang, W.**, Tian, Q., **Zhou, G.**, Xu, T., Liu, C., & Zheng, L. (2026). A novel Pickering emulsion stabilized solely by n-butyric acid-modified high-amylose corn starch for resveratrol delivery. **Carbohydrate Polymers**, 380: 125095. DOI: 10.1016/j.carbpol.2026.125095

- **来源工具**：PubMed（PMID 41832010）；**角色**：作者单位。**数据**：取代度 DS ≈ 0.1/0.2/0.3。

**A1-5**
> Zhang, X., Hu, C., Ma, K., Geng, X., Zhang, Y., Yao, G., & **Zhang, C.**（Winall Hi-Tech Seed Co., Ltd, Hefei 231283）… (2024). Persulfidation and phosphorylation of transcription factor SlWRKY6 differentially regulate tomato fruit ripening. **Plant Physiology**, 196(1): 210–227. DOI: 10.1093/plphys/kiae271

- **来源工具**：PubMed（PMID 38728423）；**角色**：作者单位（注意此处邮编 231283，为荃银高科另一注册地）。

**A1-6**
> Sun, Y., Yao, G., Li, X., Li, H., Zhao, X., Hu, C., **Zhang, C.**（Department of Agriculture Sciences, Winall Hi-Tech Seed Co., Ltd, Hefei 230009）, & Zhang, H. (2023). E3 ligase BRG3 persulfidation delays tomato ripening by reducing ubiquitination of the repressor WRKY71. **Plant Physiology**, 192(1): 616–632. DOI: 10.1093/plphys/kiad070

- **来源工具**：PubMed（PMID 36732924）；**角色**：作者单位，明确署 "Department of Agriculture Sciences, Winall Hi-Tech Seed Co., Ltd"（荃银高科农科院/农业科学部）。

### A2. 荃银高科作为**品种权人 / 致谢方 / 材料来源**（3 条）

**A2-1** ⭐ 核心证据（品种权归属）
> Fang, Y., Li, Q., Feng, Q., Wang, A., Wang, H., Zhang, Y., Zheng, G., Kang, Y., Liu, D., Xie, H., Zhou, G., Yang, J., Zhang, C., & Fan, L. (2025). Genome-Assisted Breeding of an Elite Sterile Line From Restorer Line for Hybrid Rice. **Plant Biotechnology Journal**, 24(2): 523–525. DOI: 10.1111/pbi.70367

- **来源工具**：Scholar Gateway（Wiley 全文）+ PubMed（PMID 40946172）
- **角色**：**品种权/审定权属人**。原文利益冲突声明：*"KYSM has been awarded the Certification of National Market Access with the registration number **GSD20233095** and is owned by Shanghai ZKW Molecular Breeding Technology Co. Ltd **and Winall Hi-tech Seed Co. Ltd**."*；不育系 Huke1B 品种权号 **CNA20201002638**（上海中科荃银所有），Huke1A 与 KYSM 品种权申请审查中。
- **可提取数据**：品种 **KYSM** 国家审定号 GSD20233095；Huke1B 植物新品种权 CNA20201002638；Huke1A 基因组数据 NCBI BioProject **PRJNA1307643**。
- **意义**：**唯一一条在国际期刊正文中明确写出荃银高科品种权共有的记载**，且反映公司与上海中科荃银（中科院系合资平台）的"基因组辅助育种"合作路线。

**A2-2** ⭐（材料来源，直接列出荃银系品种）
> Jin, C., Zhou, X., He, M., Li, C., Cai, Z., Zhou, L., Qi, H., & Zhang, C. (2024). A novel method combining deep learning with the Kennard–Stone algorithm for training dataset selection for image-based rice seed variety identification. **Journal of the Science of Food and Agriculture**, 104(13): 8332–8342. DOI: 10.1002/jsfa.13668

- **来源工具**：Scholar Gateway
- **角色**：**材料来源**。20 个商品化优质杂交稻品种种子（安徽、四川、湖北、湖南、江苏采购），Table 1 中安徽来源的荃银系/安徽系品种包括：**Qliangyou1606（荃两优1606）6000 粒、Quanliangyou1606（荃两优1606 另一批）6000 粒、Quanliangyou325（荃两优325，湖北）6000 粒、Huiliangyou001（徽两优001）6000 粒、Huiliangyou636（徽两优636）5900 粒、Huiliangyou996（徽两优996）6000 粒、Huiliangyousimiao（徽两优丝苗）5999 粒、Qlymxiangxinzhan 6000 粒、Liangyou8106（两优8106，荃银选育）6000 粒**。
- **可提取数据**：每品种种子数 5900–6100 粒；高光谱成像 FX10（400–1000 nm）；原始图像 30×30 px，EDSR 超分至 120×120 px。
- **意义**：荃银系品种已成为**品种真实性/种子表型 AI 识别研究的标准样本集**——可用于论证品种的市场代表性。

**A2-3**
> Mintoo, A. A., Zhang, H., Chen, C., Moniruzzaman, M., Deng, T., Anam, M., Emdadul Huque, Q. M., Guang, X., Wang, P., Zhong, Z., Han, P., Khatun, A., Awal, T. M., Gao, Q., & Liang, X. (2019). Draft genome of the river water buffalo. **Ecology and Evolution**, 9(6): 3378–3388. DOI: 10.1002/ece3.4965

- **来源工具**：Scholar Gateway
- **角色**：**致谢方**。致谢原文：*"We express our sincere thanks to Mr. **Jiang Sanqiao (Winall Seed Co. Ltd., Anhui, China)** … for their contribution, assistance, and for making dialog between Lal Teer and BGI-Shenzhen, China."*
- **意义**：反映荃银高科**海外（孟加拉 Lal Teer）业务网络**在国际科研合作中的中介角色——支持"走出去"叙事。

### A3. 荃银高科作为**经济学/管理学案例**（3 条）

**A3-1** ⭐⭐ 最强案例证据
> Xie, Z., Yuan, S., Zhu, J., & Li, W. (2023). Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? **Agribusiness**, 39(4): 1173–1198. DOI: 10.1002/agr.21823

- **来源工具**：Scholar Gateway（Wiley 全文，正文段落已获取）
- **角色**：**案例企业**。原文：*"Apart from Longping Hi-Tech, **Winall Hi-Tech** is also actively promoting the seed company-led agri-food contract farming business."*
- **可提取数据（正文原文）**：
  - 荃银高科订单农业（contract farming）**毛利率由 2018 年 3.56% 升至 2021 年 7.6%**；
  - 订单农业业务**收入占比由 2018 年 5.87% 升至 2021 年 28.73%**（数据源标注 Eastmoney 2022）；
  - Table 2 同业对比（2021 年销售额，百万美元 / 注册资本，百万美元）：中农发种业 526/150；隆平高科 489/183；丰乐种业 366/85；**荃银高科 356/63**；敦煌种业 129/73；大北农 78/583。荃银作物：**Maize, special wheat and rice（玉米、专用小麦、水稻）**。
- **意义**：这是**目前唯一在 SSCI 农业经济期刊正文中给出荃银高科订单农业量化指标的文献**，是"种粮一体化/订单农业"主线的关键引文。

**A3-2** ⭐
> Zhong, N., Cheng, Y., & Luo, Y. (2017). **Growth Strategy of Win-All Hi-Tech Seed Co., Ltd.** 复旦大学管理案例库（FUDAN Case）. DOI: 10.12156/FUDAN.CASE201200802

- **来源工具**：Undermind deep search + get_paper_info（show_doi）
- **角色**：**整篇以荃银高科为案例主体的管理学教学案例**（复旦案例中心）。摘要在索引中不可得。
- **意义**：唯一检索到的**以公司为唯一主体的成长战略案例**，可作为"企业战略"维度的直接引用；建议向复旦案例中心购买/索取全文核验年份（索引显示 2017-12-01，但 DOI 内含 "CASE2012008"，实际首版可能为 2012 年，**须核验**）。
- **confidence**：medium（DOI 可验证，刊名/年份需核）

**A3-3**（背景对照，未直接点名荃银）
> Deng, H., Yu, C., Jin, Y., Pray, C., Liu, C., & Deng, L. (2025). How is China shaping global food supply chains? Insights from the seed industry. **European Review of Agricultural Economics**, jbaf017. DOI: 10.1093/erae/jbaf017

- **来源工具**：Undermind search_papers
- **角色**：中国种业全球化背景文献，重点分析中国化工/先正达与隆平高科；**摘要中未点名荃银高科**，仅可作背景引用。
- **confidence**：high（著录）/ 但"荃银直接记载"= **未找到**

### A4. 荃银亲本 / 品种作为试验材料的国际论文（2 条）

**A4-1** ⭐
> Zafar, S., You, A., Zhang, X., Zhu, J., Chen, D., Shen, X., Wu, Y., Zhu, J., Zhang, Y., & Xu, C. (2022). Genetic dissection of grain traits and their corresponding heterosis in an elite hybrid. **Frontiers in Plant Science**, 13: 977349. DOI: 10.3389/fpls.2022.977349

- **来源工具**：PubMed（PMID 36275576）
- **角色**：**材料来源（荃银核心亲本）**。1061 份 RIL 群体来自 **Quan9311B（荃9311B，荃银高科不育系荃9311A 的保持系）× 五山丝苗（Wushansimiao）**，即荃优丝苗的衍生群体。
- **可提取数据**：1061 RIL；粒形/粒重 QTL 定位与杂种优势解析。

**A4-2**（品种集合可能含荃银系，需核）
> Cheng, X., Xu, K., Fan, X., Zhang, S., Xia, D., Wang, Y., Ye, X., Liu, Y., Wang, C., & Wu, B. (2022). Effects of Variations in the Chemical Composition of Individual Rice Grains on the Eating Quality of Hybrid Indica Rice Based on Near-Infrared Spectroscopy. **Foods**, 11(17): 2634. DOI: 10.3390/foods11172634

- **来源工具**：PubMed（PMID 36076819）
- **角色**：143 个杂交籼稻品种单粒直链淀粉（SGAC）与单粒蛋白（SGPC）近红外测定的食味品质研究；**品种清单未在摘要中列出，是否含荃优/徽两优系列待核全文**。
- **confidence**：low（作为"荃银品种记载"）/ high（著录本身）

---

## 2. B 类：中文期刊中荃银品种的选育报告与田间试验（33 条）

> 说明：以下条目中，标 ⭐ 者为可提取定量数据的关键条目。Undermind 返回的中文条目多缺卷/期/页，已如实标注。

### B1. 品种选育与不育系报告（公司自有技术体系）

**B1-1** ⭐⭐
> 张聪聪. (2011). 荃银高科浅褐色颖壳标记品种研究 [Study on Winall Hi-tech Seed Co., Ltd.'s Varieties with Light Brown Glume Marker]. **园艺与种苗 (Horticulture & Seed)**. 卷期页未获取.
- 工具：Undermind deep search（semanticscholar: 3babbcfb206fc137cf767021767d246bd3b03c4b）
- **角色**：**整篇以荃银高科技术体系为主题**。摘要给出公司技术史实：2003 年安徽荃银农业高科技研究所申报"隐性标记杂交水稻亲本及品种选育方法"获**国家知识产权局专利保护**；2005 年育成**首个带隐性颖壳色标记的两系不育系"新安S"**；以新安S为母本配组 **新两优4号、新两优6号、新两优901、新两优343、新两优106** 等系列，均通过国家或省级审定；**新两优6号 2006 年被农业部认定为首批超级稻**。
- **可提取数据**：专利年份 2003；新安S 育成年 2005；超级稻认定年 2006。
- confidence：medium（无卷期页）

**B1-2** ⭐
> 林纲（Chen Lin 索引名）等. (2007). 带浅褐色颖壳标记的籼型两用核不育系新安S的选育 [Breeding of Indica PTGMS Line Xin'an S with Light Brown Glume Marker]. **杂交水稻 (Hybrid Rice)**. 卷期页未获取.
- 工具：Undermind（semanticscholar: 618bd0ed49da4d607330d8c84436939000b2ac32）
- **角色**：荃银（安徽荃银农业高科技研究所）**核心不育系选育报告**。
- **可提取数据**：新安S = 广占63-4S × M95（爪哇型浅褐颖壳，隐性基因控制）；2005 年 3 月安徽省技术鉴定；合肥不育期 **>30 d**；**育性转换起点温度 CSIT ≤ 23.5 ℃**（14.5 h 日长）；**稻瘟病抗性 1 级、白叶枯病 5 级**；新两优6号（新安S/皖恢6号）2005-03 安徽审定、2006-01 江苏审定、2006 年农业部超级稻。
- confidence：medium

**B1-3**
> 杨联松 等. (2012). 籼稻光敏核不育系1892S的选育及其应用研究 [Study on the Breeding of Indica Rice PGMS Line 1892S and Its Application]. 刊名未获取.
- 工具：Undermind（semanticscholar: 6cb8ca0acec330655fe149ef397f8d18b3038dbd）
- **角色**：**徽两优系列母本 1892S**（安徽省农科院水稻所育成，荃银高科为徽两优系列主要配组与推广方）的选育报告。
- **可提取数据**：2004-08 安徽技术鉴定；不育期花粉不育度与套袋自交不育度 **99.97%**，不育率 100%；**起点温度 23.5 ℃**；不育期 >30 d；异交结实率 **>60%**；米质达 GB/T 17891-1999 三级；配组 皖稻153（2005-01 安徽审定、2008-02 广西引种、2008-04 国审、2009 湖北审定）、**徽两优3号（2007-03 安徽审定）、徽两优6号（安徽审定，2012 报国家审定）**、两优996（2012 报国审）。
- confidence：medium

**B1-4** ⭐
> 高俊香, 罗干, 黄建华, 高景春, 王宗启. (2017). 杂交中籼新品种荃优822选育及高产栽培. **安徽农业科学**, 45(12): 15–16.
- 工具：WebSearch（agrijournal.com.cn 中国农业期刊集成服务平台 + 参考网）
- **角色**：**荃优822 选育报告**。作者单位：安徽省新民种业有限公司、五河县农业委员会、安徽省皖农种业有限公司。
- **可提取数据**：荃优822 = **荃9311A × YR0822**（荃9311A 为荃银高科不育系）。
- confidence：high（卷期页齐全，DOI 无）

**B1-5**
> 彭金华（Peng Jin-ha 索引名）. (2014). 籼型杂交稻新品种两优8106特征特性及高产栽培技术探讨 [Discussion on Characteristics and High Yield Cultivation Techniques of New Indica Hybrid Rice Variety Liangyou 8106]. **园艺与种苗 (Horticulture & Seed)**.
- 工具：Undermind（6bec9ea5cf4bdb96b2fcca5da6fa1038d6e4b48d）
- **角色**：品种选育/栽培报告。摘要明确 **"bred by Anhui Quanyin Tech Seed Co., Ltd."（安徽荃银高科选育）**，2012 年**国家审定**；适宜赣南、湖南、浙江、湖北及安徽长江以南。
- confidence：medium

**B1-6**
> 杨连松 等. (2012). 两系中籼徽两优6号高产制种技术操作规程 [Seed Production Techniques Operating Rules of Two-line Medium Indica Rice Huiliangyou No.6]. 刊名未获取.
- 工具：Undermind（86f7acceaf2d19adde4329033c206cbf680b57cf）
- **角色**：徽两优6号**制种技术规程**（制种基地选择、播期、苗床、花期预测与调节、去杂、收晒）。
- confidence：medium

**B1-7 ~ B1-11**（参考网索引确认题名与年份，著录待核；confidence = low）
- 高产籼型三系杂交稻**荃优8016**的特征特性及高产栽培技术（2023）。摘要要点：高产稳产、适应性广、米质普通、**中感稻瘟病、耐热性较强**，穗粒数多、千粒重高为增产因素。
- 优质高产抗倒抗病中籼杂交稻**荃两优2118**的选育及应用（2021）。
- 香型杂交中籼稻**荃香优89**特征特性及高产制种技术（2025）。
- **荃优全赢丝苗**高产栽培技术（2021）。摘要要点：分蘖力强、茎秆粗壮弹性好、穗大粒多、米质优、**耐热性好、结实率高、综合抗性好**。
- 王庆永, 刘莉, 王凯. (2016). 两系杂交中籼稻"荃优丝苗"直播高产栽培技术. 刊名未获取, p. 67.（Undermind: 454df7699482aeded585efad73771cc5d84ff87d）——**唯一检索到的荃银品种"直播栽培"专题文献**。

### B2. 品种在区域/县域**比较与筛选试验**中的表现（可提取产量数据）

**B2-1** ⭐⭐ 关键
> 肖群英, 张天术, 杨迎春, 彭英刚, 杨高江, 向安明. (2023). 2022年武陵山区杂交水稻新品种比较试验. **农业科技通讯**, (5): 79–82.
- 工具：WebSearch（维普 + 参考网 + 科研之友三源交叉）
- **角色**：**荃银品种为主的多品种田间比较试验**。12 个杂交稻新品种参试，其中 **荃优822、荃优丝苗、荃优1606、荃优919** 为荃银系。
- **可提取数据**：试验地点 **武陵山区**，年份 **2022**；表现突出的 9 个品种产量 **9442.5–10543.5 kg/hm²**，比对照**瑞优399 增产 6.17%–18.55%**。
- confidence：high

**B2-2** ⭐⭐
> 侯章梅 等. (2023). 宿迁市2021年杂交中籼稻品种安全性测试. **大麦与谷类科学**, 40(1): 43–47.
- 工具：WebSearch（dmkx.cbpt.cnki.net 期刊官网 + PDF 题名页）
- **角色**：荃银系品种为参试材料。
- **可提取数据**：地点 **江苏宿迁**，年份 **2021**；综合表现较好、适宜宿迁推广的品种含 **徽两优001、荃9优220、徽两优华占、徽两优粤禾丝苗、徽两优996**（另有9优粤禾丝苗、千香优220、徽两优福星占）；**荃两优851 抽穗期偏晚，开花灌浆期遇低温存在风险**，属产量 **≥10500 kg/hm²** 组。
- confidence：high（卷期页齐全）

**B2-3** ⭐
> 吴才君 等. (2022). 2021年高邮市杂交水稻新品种安全性测试. **大麦与谷类科学**, 39(4): 46–51.
- 工具：WebSearch（期刊官网 PDF）
- **可提取数据**：地点 **江苏高邮市汤庄镇**，年份 **2021**；**14 个品种**参试，对照 **丰两优四号**；考察适应性、抗逆性、产量潜力。（荃银系具体品种名与产量需回原文核）
- confidence：high（著录）/ medium（荃银品种归属）

**B2-4** ⭐⭐
> 方玉民（Fang Yu-min）. (2014). 霍山县杂交水稻新品种种植试验研究 [Study of Plant Experiment of New Hybrid Rice Cultivars in Huoshan]. **安徽农业科学 (Journal of Anhui Agricultural Sciences)**.
- 工具：Undermind（4d306b284f0c060c7015f10a40caff59bf0a8440）
- **可提取数据**：地点 **安徽霍山**；参试 徽两优898、丰两优四号、**新两优6号**、丰两优九号、皖稻153、Y两优1号、盛两优5814，对照 **Ⅱ优838**；
  - **徽两优898 产量最高 10938.3 kg/hm²**，显著高于对照；
  - 全生育期**比对照早 7 d**；**株高 124 cm**；**单穴有效穗 11.5**；**结实率 86.7%（最高）**；
  - **稻瘟病抗性强（strong resistance to rice blast）**。
- confidence：medium（无卷期页）

**B2-5** ⭐
> 李金宝（Li Jin-ba）. (2015). 2014年来安县叉河镇水稻新品种比较试验 [Comparative Study on New Rice Varieties in Chahe Town of Lai'an County in 2014]. **园艺与种苗 (Horticulture & Seed)**.
- 工具：Undermind（0ee722bd65602a7b5fba2437e9b170dd9aa89ea6）
- **可提取数据**：地点 **安徽来安县叉河镇**，年份 2014；**新两优343、徽两优996** 被列为"高产超级稻类型"，建议在高肥管理田块作主推品种大面积种植；**新两优1671** 被列为"订单农业品种（contract farming species）"；**徽两优6号** 列入可大面积种植品种。
- **意义**：**文献中直接出现"订单农业品种"分类**，与荃银订单农业主线呼应。
- confidence：medium

**B2-6** ⭐
> 姚松（Song Yao）. (2011). 徽两优6号特征特性、凤台县种植产量及高产栽培技术. **安徽农业科学 (Journal of Anhui Agricultural Sciences)**.
- 工具：Undermind（a7b7c1a65c0aad5823e2eec0b34efcc3815ddf02）
- **可提取数据**：地点 **安徽凤台县**，年份 **2009**；**有效穗 262.80×10⁴/hm²；每穗总粒数 197.1；每穗实粒数 168.5；结实率 85.5%；千粒重 28.0 g；理论产量 12.40 t/hm²**。徽两优6号 2008 年安徽审定，**2010 年农业部认定超级稻**。
- confidence：medium

**B2-7** ⭐
> 李军. (2013). 徽两优6号700 kg/667m² 高产栽培技术. **安徽农学通报 (Anhui Agricultural Science Bulletin)**, pp. 36–37.
- 工具：Undermind（8aa60e148cee8efceadf12d26359ee21bf647330）
- **可提取数据**：地点 **安徽安庆**；目标产量 **700 kg/667m²（=10500 kg/hm²）**；技术要点：适期播种、合理密植、好气灌溉、科学施肥、病虫防治。
- confidence：medium

**B2-8** ⭐
> 郎祥东（Lang Xiang-don）. (2014). 铜陵县杂交中籼稻新组合筛选鉴定试验 [Test of Selection and Evaluation of New Hybrid Middle-season Indica Rice Combinations in Tongling County]. **安徽农业科学**.
- 工具：Undermind（f29e4d1591d5bc8253ddd003a003676bb1bfd171）
- **可提取数据**：地点 **安徽铜陵**；12 个组合，对照 Ⅱ优838；**徽两优348 产量第 1，比 CK 增产 10.93%，米质 5 级**；**徽两优932/徽两优928 比 CK 增产 6.62%**（原文表述有出入，须核）。
- confidence：medium

**B2-9**
> 郭林. (2012). 水稻新品种（中籼组）展示试验评述. 刊名未获取, pp. 60–61.
- 工具：Undermind（823cfe85aa3c4e6c81c87a4196734c30f1fdd933）
- **可提取数据**：**徽两优6号超级稻**与新两优6380、广两优4号、徽两优3号"产量高、米质优、综合性状好"，可作沿江地区主推品种。安徽省每县主推品种压缩至 3–5 个。
- confidence：medium

**B2-10**
> 刘晓霞（Liu Xiao-xia）. (2010). 优质杂交水稻品种筛选试验 [High-quality Hybrid Rice Varieties Screening]. 刊名未获取.
- 工具：Undermind（29ecfcdd26aebf8eb2a48f2286703dd2875384e3）
- **可提取数据**：地点 **湖南常德市**；**徽两优6号**与 C两优501、陆香8258、安两优9808、两优273、Ⅱ优339 一并被评为经济性状好、综合性状优良、适宜大面积推广。
- confidence：medium

**B2-11**
> 杨安中（An-Zhong Yang）. (2014). 不同杂交水稻品种主要性状与产量研究 [Studies on the Main Properties and Yields of Different Hybrid Rice Varieties]. 刊名未获取.
- 工具：Undermind（81fffdd54a1f207ef3541e8a9db2ff6981cf43ab）
- **可提取数据**：随机区组，11 个杂交稻品种；**对照品种为新两优6号**；**徽两优6号全生育期 161 d（最长）**；淮两优1141 实产最高，与 CK 新两优6号差异极显著。地点：沿淮地区。
- confidence：medium

**B2-12**
> 曹伟波（Cao Wei-bo）. (2006). 杂交水稻新品种比较试验 [Comparison experiments on new hybrid rice varieties]. **广西农业科学 (Guangxi Agricultural Sciences)**.
- 工具：Undermind（024abd8ce033804226fd909b951146241c22c829）
- **可提取数据**：地点 **广西灵山县**；14 个品种，对照 培杂双七；生育期 130–151 d；含 **新两优6号** 在内的 8 个品种比 CK 增产 **2.03%–20.34%**。
- confidence：medium

**B2-13**
> 卢金榕（Lu Jin-ron）. (2015). 优质早稻杂交水稻新品种比较试验 [Comparison test of new high-quality early hybrid rice varieties]. **福建农业科技 (Fujian Agricultural Science and Technology)**.
- 工具：Undermind（a7a228af1be95d9c663cb01e01da1e9c70c2c9d8）
- **可提取数据**：地点 **福建永定县**，年份 **2014**；5 个优质早稻品种，对照 T78优2155；**"荃优1093"综合表现列第 2**（次于福两优2155），可进一步示范。
- confidence：medium

**B2-14**
> 游年顺（You Nian-shun）. (2010). 杂交稻新组合荃优527在韶关市的试种表现及主要栽培技术 [Trial Results and Main Cultivation Techniques of Hybrid Rice Combination Quanyou 527 at Shaoguan City]. **福建稻麦科技 (Fujian Science and Technology of Rice and Wheat)**.
- 工具：Undermind（b6a78b03782e22bd885d8e6b058363ddc2f13b8c）
- **角色**：**"荃优"冠名品种最早的县域试种报告之一**；地点 **广东韶关**，晚稻季。
- confidence：medium

**B2-15** ⭐
> 林增贵. (2017). 荃优822在永安市试种表现及高产栽培技术. **福建稻麦科技**, 35(3): 56–57.
- 工具：WebSearch（参考网 + 交叉检索）
- **可提取数据**：地点 **福建永安市贡川镇南坂村、红安村**，年份 **2016**；单季稻试种 **670 m²**，瓜后稻 **810.5 m²**；品种来源"安徽荃银高科种业股份有限公司和安徽省皖农种业有限公司选育"，**2016 年湖北省审定（鄂审稻2016016）**。田间表现：株型适中挺拔、分蘖力强、长势旺、剑叶短宽挺、适应性强、后期转色好、产量高、米质优。
- confidence：high（卷期页齐全）

**B2-16**
> 李维伯. (2019). 荃优822在上杭县作中稻种植表现及高产栽培技术. **农业开发与装备**, (9): 164.
- 工具：WebSearch（维普 + 交叉）
- 作者单位：福建龙岩市上杭县湖洋农技站。地点 **福建上杭县**。
- confidence：medium（页码为单页 164，须核）

**B2-17**（题名确认，著录待核；confidence = low）
> 荃优822在福安市的种植表现及高产栽培技术. **上海农业科技**, 2018(4).
> 荃优822在尤溪县作中稻种植表现及高产栽培技术. (2017). 刊名待核.
> 杂交水稻荃优822在华南作晚稻种植的特征特性及栽培技术. (2020). 刊名待核.
> 杂交水稻新品种荃优822的特征特性及两段育秧栽培技术. 刊名待核（长江文库索引）.

**B2-18** ⭐
> 佚名. 松桃县水稻新品种筛选试验. 中国农业期刊集成服务平台索引（gid=021396DB-DD24-4C29-952F-98377E2F40B7），刊名年期待核.
- **可提取数据**：**荃优华占 产量 536.00 kg/667m²（= 8040 kg/hm²）**；地点 **贵州松桃县**；同时记录株高、穗长、有效穗、穗实粒数、结实率、千粒重。
- confidence：low（著录不全，但数据明确）

**B2-19**
> 佚名. 荃优607在宁化县种植表现及高产栽培技术. (2023). 参考网索引，刊名年期待核.
- **可提取数据**：地点 **福建宁化县石壁镇陂下村**，年份 **2019**；中稻**机插**试种 **0.12 hm²**；**全田实割单产 9.873 t/hm²**，对照 **广8优165 为 7.743 t/hm²**，**增产 2.13 t/hm²，增幅 27.5%**，在 **42 个参试新品种中列第 2**。2020 年列入农业农村部水稻绿色高质高效创建项目重点示范。品种由**中国种子集团有限公司 + 安徽荃银高科种业股份有限公司共同育成**，2020 年国家审定，2022-01 获福建省第八批引种备案。
- confidence：medium（数据具体，著录待核）

**B2-20**
> 佚名. 福建松溪县优质杂交稻荃优607的种植表现及高产栽培技术. 科研之友索引（scholarmate S/JjARZk），刊名年期待核.
- confidence：low

### B3. 再生稻（ratoon rice）试验中的荃银品种（本主线最重要的一组）

**B3-1** ⭐⭐ 关键
> 佚名（作者待核）. (2026). 水分管理和品种类型对再生稻产量和稻米品质的影响. **作物学报**. DOI: 10.3724/SP.J.1006.2026.52021（网络首发 2025-11-11）
- 工具：WebSearch（zwxb.chinacrops.org 期刊官网 + 图表页）
- **角色**：**荃优607、荃优粤农丝苗作为"优质稻"处理品种**。
- **可提取数据**：地点 **湖北蕲春、浠水**，年份 **2023**；三个节水抗旱稻（旱优8200、旱优116、旱优73）× 三个优质稻（**箴两优郢香丝苗、荃优粤农丝苗、荃优607**），对照 **两优6326**；两种水分管理（常规灌溉 vs 节水灌溉）。
  - 节水灌溉比常规灌溉**头季减少灌溉水 76%、再生季减少 85%**，产量与加工/外观/蒸煮食味品质**无显著差异**；
  - **优质稻头季产量 8.54 t/hm²、再生季产量 5.88 t/hm²**，与普通稻相当；
  - 优质稻**整精米率分别高 13.5 和 20.6 个百分点**，垩白显著降低。
- **意义**：**中文一区刊（作物学报）中荃银品种作为核心试验材料、且有完整产量+品质数据的最佳条目**。
- confidence：high（DOI 可验证；作者名单待补）

**B3-2** ⭐⭐
> 李淑云（Shu-Yun Li）. (2026). 政和县不同育型品种与移栽密度对再生稻产量、发苗能力影响研究. **农业科学 (Hans Journal of Agricultural Sciences)**, 9(7). DOI: 10.32629/as.v9i7.4153（2026-07-31）
- 工具：Undermind deep search + get_paper_info
- **角色**：**荃优607 作为"籼型三系"代表品种**，二因素裂区试验主区。
- **可提取数据**：地点 **福建政和县半山区**，年份 **2025**（2 月 28 日播种，4 月 5 日移栽）；
  - 品种主区：甬优1540（籼粳型）、**荃优607（籼型三系）**、隆两优534（籼型两系）；
  - 密度副区：D1 30×13 cm、D2 30×15 cm、D3 30×18 cm、D4 30×21 cm；
  - 结论：中密度 D3（30×18 cm）各品种产量均最佳；**荃优607 适配 30×18 ~ 30×21 cm 区间**；甬优1540 再生苗成苗率最高 85.3%。
- **意义**：**唯一一条"荃银品种 × 移栽密度 × 再生稻"的正交/裂区试验**，直接支持"密度—再生力"论证。
- confidence：high（DOI 可验证）

**B3-3** ⭐⭐
> 刘环, 杜斌, 刘章勇, 何文静, 邱先进, 邢丹英, 徐建龙. (2015). 江汉平原"一种两收"优良水稻品种筛选. 刊名未获取, pp. 30–35.
- 工具：Undermind（1ca7b1b72c89e367bee622c2682f879d280ce497）
- **可提取数据**：地点 **湖北江汉平原**；**14 个品种**，对照 丰两优香1号；
  - 供试品种**两季总产 810.72–1111.3 kg/667m²，平均 959.07 kg/667m²**（= 12.16–16.67 t/hm²，均值 14.39 t/hm²）；
  - 对照丰两优香1号 **1005.02 kg/667m²**；广两优1128 **1111.3 kg/667m²** 显著高于 CK；
  - **C两优华占、两优6326、新两优223、新两优6号、准两优527 均高于 CK（未达显著）**，判定为**适宜江汉平原再生稻品种**。
- confidence：medium（无刊名卷期）

**B3-4** ⭐
> 涂军明（Tu Jun-min）. (2014). 高产再生稻品种筛选试验 [Screening Experiment of High-yield Ratooning Rice Varieties]. 刊名未获取.
- 工具：Undermind（fd203446f95e8eb3b30b189bff5a55b522acdea1）
- **可提取数据**：**13 个水稻品种**；结论：**两优6326、新两优223、新两优6号可作再生稻品种**；丰两优1号、黄华占、天优华占需加强生产管理。
- confidence：medium

**B3-5**
> 肖秋生（Qiu-Sheng Xiao）. (2012). 杂交中稻—再生稻品种筛选试验 [Selection Experiment of Hybrid Middle Rice-Ratoon Rice Varieties]. **湖北农业科学 (Hubei Agricultural Sciences)**.
- 工具：Undermind（5bc973e43a3301cd46f535e06025a0774aa04f67）
- **可提取数据**：地点 **湖北蕲春**；8 个杂交中稻品种；两季产量 盛两优5814、K优AG、**新两优233（原文"Xiniangyou 233"，疑为新两优233）** 极显著高于 CK，适宜作再生稻。
- confidence：low（品种名转写存疑，须核原文）

**B3-6**
> 梁娟英, 李明龙. (2009). 干旱地区超级稻再生栽培试验 [Experiment on ratoon cultivation of super rice in drought region]. 刊名未获取.
- 工具：Undermind（a61b809a7977d12c55dc63f109059b26ecccdde9）
- **可提取数据**：地点 **广西钦州市**；7 个超级稻品种再生栽培；早稻产量 两优培九 > Y两优1号 > **新两优6号**；结论推荐中浙优1号与两优培九。
- confidence：medium

**B3-7**
> 佚名. 洪湖市再生稻适应性品种筛选. (2025). 参考网索引，刊名年期待核.
- **可提取数据**：地点 **湖北洪湖市**；**荃优822 头季成熟较晚但产量最高**；高产品种组：荃优822、隆晶优1212、九两优粤禾丝苗、箴两优郢香丝苗、丰两优香1号；最终推荐隆晶优1212 与 丰两优香1号进一步推广。
- confidence：low（著录不全；网络摘要中"968.6 kg/667m²"数值存疑，**不予采信**）

### B4. 双季稻 / 示范 / 制种类

**B4-1**
> 张云虎（Zhang Yun-hu）. (2012). 双季稻新组合新两优106在黄山市的示范及高产栽培技术. 刊名未获取.
- 工具：Undermind（09772e84481be1765966931568d98c37b308c25f）
- 地点 **安徽黄山市**；高产、优质、抗倒的大面积示范总结。confidence：medium

**B4-2**
> 黄传众, 范启包. (2011). 高产优质两系杂交稻"新两优343"高产栽培技术. 刊名未获取, p. 40.
- 工具：Undermind（82eeeeb2972b0aea33320d899f0dbd3d4c033948）
- 地点 **福建松溪县**，年份 **2009–2010**；表现高产稳产、抗病性强、抗逆性好、适应性广、落色好、叶青籽黄、出米率高、米质优良。confidence：medium

### B5. 品质与衍生品种谱系

**B5-1** ⭐
> 何秀英, 刘维, 陆展华, 王晓飞, 王石光, 方志强, 巫浩翔, 陈浩. (2022). 广东优质稻粤农丝苗的衍生品种及其特征特性研究. **广东农业科学**, 49(9). DOI: 10.16768/j.issn.1004-874X.2022.09.007
- 工具：WebSearch（gdnykx.gdaas.cn 期刊官网）
- **角色**：**荃优粤农丝苗、徽两优粤农丝苗等荃银×广东农科院合作衍生品种的系统比较**。
- **可提取数据**：粤农丝苗衍生品种**区域试验产量均比对照增产，增幅 0.46%–10.98%**；**品质指标均达优质标准**；抗倒力与耐热性鉴定中"**除徽两优粤农丝苗外，其他品种耐热性表现为较强或强**"；**荃优粤农丝苗已成为当地主栽品种**。
- confidence：high（DOI 可验证；页码待补）

**B5-2**（品种审定公告级数据，非期刊论文，仅作交叉校验）
- **荃优丝苗**（三系，荃广A × 五山丝苗）：长江中下游一季中稻全生育期 127.5 d，比丰两优四号早熟 5.3 d；糙米率 80.6%、整精米率 68.1%、粒长 6.6 mm、长宽比 3.3、垩白度 0.5%、透明度 1 级、碱消值 7.0 级、胶稠度 76 mm、直链淀粉 16.4%，达 NY/T 593-2021 二级；**稻瘟病综合指数两年 3.3 / 3.6，穗颈瘟损失率最高 5 级，中感稻瘟病**；2021 年区试亩产 624.0 kg（+2.2%），2022 年续试 621.9 kg（+4.0%），两年平均 623.0 kg（+3.1%）。
- **荃优1606**（荃9311A × YR1606，国审稻20206016）：长江上游/中下游区试分别增产 5.0% / 3.75%，生产试验增产 4.48% / 5.94%；整精米率、垩白度、直链淀粉达《食用稻品种品质》一级。
- **荃两优1606**：2018/2019 区试平均亩产 637.15 / 664.84 kg，均增产 >2%；整精米率 66.0%、垩白度 1.2%、直链淀粉 16.0%，达二级。
- **荃优822**：2014–2015 湖北中稻区试两年平均亩产 665.80 kg（比丰两优四号 +3.84%）；2019 长江中下游中籼迟熟组区试 669.89 kg/亩（+5.89%），2020 续试 623.54 kg/亩（+4.93%）。
- **荃9优607**（江苏红旗种业 + 安徽荃银高科 + 江苏沿海农科所）：2017–2018 长江中下游区试两年平均 640.4 kg/亩（比丰两优四号 +5.5%）；2019 生产试验 656.7 kg/亩（+6.0%）；全生育期 131.3 d，株高 128.8 cm，穗长 24.4 cm，米质三级。
- **荃9优063**：2018 长江上游区试 682.16 kg/亩（+9.09%），2019 年 662.57 kg/亩（+5.30%）。
- **徽两优丝苗**（安徽荃银高科 + 安徽省农科院水稻所 + 广东省农科院水稻所，1892S × 五山丝苗）：长江中下游一季中稻全生育期 136.1 d，有效穗 243 万/hm²，株高 111.6 cm，穗长 23.6 cm，每穗总粒数 202.2，结实率 83.6%，千粒重 22.9 g。
- **徽两优898**（1892S × YR0822）：稻瘟病、白叶枯病抗性中等，**褐飞虱抗性较高**。
- 来源：品种审定公告 / RiceData / 种业商务网（**非学术文献**，confidence = medium，仅供与文献数据交叉校验，正文引用须用审定公告原件）。

### B6. 其他相关（荃银品种未直接出现但同域）
- 刘环等以外的江汉平原、蕲春、洪湖再生稻文献群（B3 系列）构成"再生稻品种筛选"完整证据链。
- 安徽省十种水稻主栽品种对褐飞虱的抗性鉴定（安徽省农科院机构知识库索引）——**疑含徽两优/新两优系列，全文未获取，未确认**。

---

## 3. 按任务清单的品种覆盖情况

| 品种 | 学术文献直接记载 | 最佳证据 |
|---|---|---|
| 荃优822 | ✅ 有（≥6 篇） | B2-1 武陵山区比较试验（9442.5–10543.5 kg/hm²）；B1-4 选育报告；B2-15 永安市 |
| 荃优华占 | ⚠️ 弱（1 条，著录不全） | B2-18 松桃县 536.00 kg/667m² |
| 荃优1606 | ✅ 有（1 篇试验 + 审定数据） | B2-1 武陵山区 |
| 荃优607 | ✅ 有（3 篇，含 2 篇高质量） | B3-1 作物学报再生稻；B3-2 政和县密度试验；B2-19 宁化县 9.873 t/hm² |
| 荃优丝苗 | ✅ 有（国际 + 中文） | **A1-1 Rice 2022（国际，基因组）**；B2-1；B1-11 直播栽培 |
| 荃9优系列 | ⚠️ 弱（B2-2 提及荃9优220） | B2-2 宿迁测试 |
| 荃两优6019 | ❌ **未找到** | — |
| 荃两优851 | ⚠️ 弱（1 条） | B2-2 宿迁测试（抽穗偏晚，低温风险，≥10500 kg/hm²组） |
| 荃两优1606 | ✅ 有（国际材料集） | A2-2 JSFA 2024 高光谱种子识别 |
| 荃两优丝苗 | ❌ 学术文献**未找到**（仅品种数据库） | — |
| 徽两优6号 | ✅ 有（≥6 篇） | B2-6 凤台 12.40 t/hm²；B2-7 700 kg/667m²；B1-6 制种规程 |
| 徽两优898 | ✅ 有（2 篇） | B2-4 霍山 10938.3 kg/hm²；氮肥试验 9296.4 kg/hm²（见下） |
| 徽两优882 | ❌ **未找到**（仅示范/推广新闻） | — |
| 徽两优丝苗 | ✅ 有（国际材料集） | A2-2 JSFA 2024（Huiliangyousimiao） |
| 新两优6号 | ✅ 有（≥6 篇） | B1-1/B1-2 超级稻认定；B2-12 广西 +2.03~20.34%；B3-3/B3-4 再生稻 |
| 新两优223 | ✅ 有（2 篇再生稻） | B3-3 江汉平原；B3-4 再生稻筛选 |
| 新两优343 | ✅ 有（2 篇） | B4-2 松溪县；B2-5 来安县 |
| 新两优901 | ⚠️ 仅在 B1-1 品种谱系中被列名 | B1-1 |
| 新两优106 | ✅ 有（1 篇） | B4-1 黄山市示范 |

**额外重要条目（氮肥试验）**
> 佚名. 氮肥用量对徽两优898生长及产量的影响. 科研之友索引（scholarmate S/egrP4v），刊名年期待核.
- **可提取数据**：**N 210 kg/hm² 处理经济产量最高，达 9296.4 kg/hm²**；经济产量随施氮量先增后降。
- **意义**：**唯一一条荃银系品种的氮肥梯度试验**。confidence：low（著录不全，数据明确，须回 CNKI 核）

---

## 4. 关键发现（供论文引用的 15 条）

1. **荃银高科科研人员已在国际主流期刊以公司为第一署名单位发文**：Zhang et al. 2022, *Rice* 15:49（DOI 10.1186/s12284-022-00595-z），5 位作者署 Winall Hi-Tech Seed Co., Ltd.，通讯作者陈金节；研究对象即公司主打品种**荃优丝苗（QYSM）**。
2. **荃优丝苗的遗传解析规模为 1061 RIL + 1061 BCF1**，亲本为 **Quan9311B × 五山丝苗**（同上 + Zafar et al. 2022, *Front Plant Sci* 13:977349, DOI 10.3389/fpls.2022.977349）。
3. **荃银高科是国审品种 KYSM 的共有权人**（GSD20233095，与上海中科荃银共有），相关不育系 Huke1B 持有植物新品种权 CNA20201002638 —— Fang et al. 2025, *Plant Biotechnol J* 24(2):523-525, DOI 10.1111/pbi.70367。
4. **荃银订单农业的唯一学术量化记载**：毛利率 2018 年 3.56% → 2021 年 7.6%；收入占比 5.87% → 28.73% —— Xie et al. 2023, *Agribusiness* 39(4):1173-1198, DOI 10.1002/agr.21823。
5. **同文给出 2021 年同业规模对比**：荃银高科销售额 356 百万美元 / 注册资本 63 百万美元，居隆平高科（489/183）与丰乐种业（366/85）之后（同上）。
6. **存在一篇以荃银高科为唯一主体的管理学案例**：Zhong, Cheng & Luo, *Growth Strategy of Win-All Hi-Tech Seed Co., Ltd.*, 复旦案例库, DOI 10.12156/FUDAN.CASE201200802。
7. **荃优607 是再生稻研究的活跃材料**：作物学报 2026（DOI 10.3724/SP.J.1006.2026.52021）湖北蕲春/浠水 2023 年试验中，优质稻组（含荃优607、荃优粤农丝苗）头季 8.54 t/hm²、再生季 5.88 t/hm²，**整精米率比普通稻高 13.5 / 20.6 个百分点**，节水灌溉使头季/再生季灌溉水分别减少 76% / 85% 而产量品质无显著差异。
8. **荃优607 的最优移栽密度已被量化**：李淑云 2026, *农业科学* 9(7), DOI 10.32629/as.v9i7.4153 —— 福建政和县 2025 年裂区试验，荃优607 适配 **30×18 ~ 30×21 cm**，中密度处理产量最佳。
9. **荃优607 县域机插实测增产幅度极高**：福建宁化县 2019 年机插实割 **9.873 t/hm²**，对照广8优165 **7.743 t/hm²**，**增幅 27.5%，42 个参试品种列第 2**（参考网索引，著录待核）。
10. **荃优系列在武陵山区比较试验中整体领先**：肖群英等 2023, *农业科技通讯* (5):79-82 —— 2022 年 12 品种，荃优822 等 9 品种 **9442.5–10543.5 kg/hm²**，比对照瑞优399 **增产 6.17%–18.55%**。
11. **徽两优898 曾在县域试验中产量与抗性双第一**：方玉民 2014, *安徽农业科学* —— 安徽霍山 **10938.3 kg/hm²**，结实率 86.7%，稻瘟病抗性强，生育期比 Ⅱ优838 早 7 d。
12. **徽两优6号在安徽凤台的高产群体结构**：姚松 2011, *安徽农业科学* —— 有效穗 262.80×10⁴/hm²、每穗总粒 197.1、结实率 85.5%、千粒重 28.0 g、理论产量 **12.40 t/hm²**；2010 年农业部超级稻。
13. **新两优6号是首批（2006）农业部认定超级稻，且为荃银"隐性颖壳标记"防伪技术体系的第一个产品**：张聪聪 2011, *园艺与种苗*；林纲等 2007, *杂交水稻*（新安S：CSIT ≤ 23.5 ℃，稻瘟病 1 级，白叶枯 5 级）。
14. **新两优223 / 新两优6号被独立研究判定为适宜江汉平原"一种两收"**：刘环等 2015, pp.30-35 —— 14 品种两季总产 **810.72–1111.3 kg/667m²（均值 959.07）**，新两优223、新两优6号均高于对照丰两优香1号（1005.02 kg/667m²）。
15. **荃银系品种已进入国际种子表型 AI 数据集**：Jin et al. 2024, *J Sci Food Agric* 104(13):8332-8342, DOI 10.1002/jsfa.13668 —— 20 品种商用优质杂交稻中含荃两优1606、徽两优001/636/996/丝苗、两优8106 等，每品种约 6000 粒。
16.（补）**粤农丝苗衍生品种（含荃优粤农丝苗）区域试验增幅 0.46%–10.98%，品质均达优质标准，耐热性多为"较强/强"**：何秀英等 2022, *广东农业科学* 49(9), DOI 10.16768/j.issn.1004-874X.2022.09.007。
17.（补）**唯一的氮肥梯度数据**：徽两优898 在 N 210 kg/hm² 时经济产量最高 **9296.4 kg/hm²**，呈先增后降（科研之友索引，著录待核）。

---

## 5. 与论文主线的可用性评估

| 论文可能章节 | 可直接引用的文献 | 强度 |
|---|---|---|
| 企业创新能力（研发产出） | A1-1、A1-2~A1-6、A2-1 | 强（6 篇公司署名国际论文 + 1 条品种权） |
| 品种市场代表性 | A2-2（AI 数据集）、B2-1/B2-2/B2-3/B2-4/B2-5 | 强 |
| 再生稻适应性 | B3-1（作物学报）、B3-2、B3-3、B3-4、B3-7 | 强 |
| 稻米品质 | B3-1、B5-1、A4-2（待核） | 中 |
| 稻瘟病/抗逆 | B2-4、B1-2、B5-1（耐热）、B5-2（审定数据） | 中 |
| 氮肥/密度栽培响应 | B3-2（密度）、氮肥试验条目 | 弱—中（仅 2 条） |
| 订单农业/种粮一体化 | **A3-1（Agribusiness 2023）**、A3-2（复旦案例）、B2-5（"订单农业品种"分类） | 中—强（但仅 1 篇高质量实证） |
| 种业并购/资本 | A3-3（背景）、Undermind 检出的中国种业重组文献群 | 弱（无以荃银为对象的并购实证论文） |

---

## 6. Gaps（检索已尽但仍缺失的部分）

1. **专利与植物新品种权维度整体缺失**。Amass PatentCore 账户配额已耗尽（重置 2026-09-30），Google Patents / CNIPA / 农业农村部植物新品种保护办公室网站在本容器内被代理拦截。**唯一取得的品种权号来自 A2-1 论文正文（CNA20201002638、GSD20233095）**。建议：配额恢复后以 `assignee=Winall` / `安徽荃银高科` 重跑 PatentCore；或人工查 CNIPA 与 `www.cnpvp.cn`。
2. **荃两优6019、荃两优丝苗、徽两优882 在学术文献中未找到任何直接记载**——仅见于品种审定公告与种业商务网等非学术源。
3. **荃优华占**学术记载极弱：仅 1 条县域筛选试验（著录不全）。国际文献中的 "Huazhan" 类组合几乎全为晶两优华占/隆两优华占/天优华占，**非荃银品种**，引用时须严格区分。
4. **无"荃银品种 × 稻瘟病人工接种抗性鉴定"的专题论文**。现有抗性信息全部来自品种审定公告的抗性综合指数，或试验报告中的定性描述（"抗性强""中感"）。
5. **无"荃银品种 × 耐热性（高温结实率）"的专题论文**。仅 B5-1（广东农科院，粤农丝苗衍生品种耐热性分级）与若干栽培报告的定性表述"耐热性较强"。
6. **无"荃银品种 × 机械化直播"的量化试验论文**。仅 B1-11（荃优丝苗直播高产栽培技术，1 页技术文，无试验设计）。
7. **缺少以荃银高科并购（河北新纪元、杨凌登峰、四川三新等）为对象的学术论文**。检索到的只有公司公告与券商研报；管理学案例仅 A3-2 一篇（且年份存疑）。
8. **卷/期/页码缺口**：Undermind 返回的 20 余条中文条目普遍缺少完整著录（Semantic Scholar 对中文刊索引不全）。本容器无法访问 CNKI/万方/维普原文页。**建议在有网络的环境用 CNKI 按题名逐条补齐**，本文件已用 `confidence` 标注全部待核条目。
9. **Scholar Gateway 语料局限**：该工具只覆盖 Wiley 全文，Elsevier/Springer/MDPI 需靠 PubMed 补；而 PubMed 不收录中国农学类中文刊与多数农艺学英文刊（如 *Field Crops Research*、*Agronomy*），本轮**未能对 Elsevier 农艺期刊做 affiliation 级检索**，可能遗漏 1–3 篇。

---

## 7. 数据文件

可提取定量数据的条目已整理至 **`/home/user/video/evidence/08_quanyin_lit_data.csv`**（24 行，列：variety, study_ref, doi, role, site, year, trait, value, unit, note, confidence）。
