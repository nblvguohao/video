# 维度7：学术文献扫描 B——种业经济、制度与产业组织

- **维度**：07 种业经济 / 制度 / 产业组织（英文为主，兼顾中文核心期刊）
- **检索次数**：67 次（WebSearch 14 次[其中 5 次因会话配额用尽未执行]；Consensus 8 次[7 次成功，月度配额随后耗尽]；Scholar Gateway 12 次；Undermind search_papers 27 次 + deep search 2 次 + read_pdfs 1 次[配额超限失败]；PubMed 3 次检索 + 1 次元数据；Amass BiomedCore 1 次）
- **来源数**：约 165 条文献/文档（其中带 DOI 或稳定链接的 ≥ 120 条；核心相关条目 ≥ 60 条）
- **更新时间**：2026-09-14
- **工具限制说明**：Elicit 账号无 API 权限（不可用）；Consensus 月度 30 次配额在第 8 次查询后耗尽；WebSearch 会话配额（200 次，多子任务共享）在本维度第 10 次查询时耗尽；Undermind read_pdfs 用量超限（1 小时后重置），故未能读取全文提取更多原文数字；curl/WebFetch 未使用。
- **Undermind 工作区**（含 2 个 deep search、134 + 162 篇排序文献）：https://app.undermind.ai/projects/5e132809-6b94-4d11-8477-afba425d64c1
- **置信度标注**：高 = 摘要/正文段落中直接出现原文数字或结论；中 = 检索工具的综合表述或仅有标题/元数据；低 = 间接推断或来源不稳定。
- **期刊分区说明**：本环境无法访问 JCR/中科院分区表，"分区"均为基于领域常识的**估计**（标注"估"），投稿前须以最新中科院分区表核实。

---

## 0. 总体结论（供论文选题/引言使用）

1. **"种企主导的订单农业/种粮一体化"在英文文献中几乎是空白**：两个 Undermind deep search（各 134/162 篇）均确认，直接以"种子企业为链主"建模的只有 Xie et al. (2023, *Agribusiness*)，其余均为"公司+农户"/龙头企业/合作社文献的迁移。Deep search 摘要原话："China-specific evidence on seed-enterprise-led 'seed–grain integration' remains thin: [Xie23] is the closest direct study"；"The main gap is systematic evidence tracing a seed firm from variety choice and contracted production through buyback, processing, branding, and downstream margins"。（置信度：中；来源：Undermind deep search 结果摘要）
2. **制度改革的因果证据集中在许可费与 R&D**：Xiang et al. (2025, *Agribusiness*) 是目前唯一利用真实品种许可交易数据评估 2015 年《种子法》修订（审定制度改革）的实证；2021 年《种子法》EDV 制度、绿色通道/联合体试验、种业振兴行动均**无因果评估**，只有法学/政策评述。（置信度：高，见 §3）
3. **杂交稻面积下降的经济解释已有综述与微观证据**（Huang 2022 *Food Security*；Huang & Zou 2018 *FCR*；Peng 2016 《作物学报》；Yan et al. 2022），核心机制为：直播/机插提高用种量、杂交种子价高、常规稻优质稳产、机械化缩短生育期；微观证据显示杂交稻增产 4.86% 但净收入反而更低。（置信度：高，见 §5）
4. **市场结构**：中国种业集中度极低（上市种企合计国内份额年均 <10%，黄毅&柳思维 2015；CR5 从 2019 年 9.6% 升至 2023 年 19.2%，Wang & Kang 2025），并购整合后"集中度提升未自动转化为国际竞争力"。（置信度：高）
5. **荃银高科（Winall Hi-Tech）被英文文献直接点名**：Xie et al. (2023) 引用 Eastmoney (2022) 数据：荃银高科订单农业业务毛利率 3.56%（2018）→7.6%（2021），订单业务占营收比重 5.87%（2018）→28.73%（2021）；隆平高科与荃银高科均属 2022 年农业农村部认定的 53 家"龙头"种企。（置信度：高，原文段落）

---

## 1. 中国种业企业创新、商业化育种体系、"育繁推一体化"

### 1.1 关键事实

| # | 事实 | 来源（URL/DOI） | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 1.1 | 中国种子市场商业价值由 2000 年 250 亿元增至 2021 年 1280 亿元（引 MARA 2022），为仅次于美国的全球第二大种子市场 | Xiang et al. 2025, https://onlinelibrary.wiley.com/doi/10.1002/agr.22020 | 2025-01 | SG: "seed industry reform PVP variety registration concentration" | 高 |
| 1.2 | 2017–2019 年仅 42% 的种企只销售自育品种，58% 仍依赖外部育种机构；2017 年前 91% 的种企购买他人品种许可，2017 年后为 58% | 同上 | 2025-01 | 同上 | 高 |
| 1.3 | 2000 年首部《种子法》终结县/地/省级国有种子公司垄断，开启种业商业化；2015 年修订重点改革 VCU（审定）制度；具体改革措施 2016 年中落地，2017 年起审定品种数显著增加 | 同上（正文段落） | 2025-01 | 同上 | 高 |
| 1.4 | 2011 年国务院文件明确科研单位逐步退出商业化育种、企业为商业化育种主体，重点扶持"育繁推一体化"企业 | WebSearch 综合（福建省政府/农业农村厅/中国网报道） http://finance.china.com.cn/roll/20141218/2858710.shtml | 2014-12 | "育繁推一体化 种子企业 商业化育种 实证" | 中 |
| 1.5 | 2000–2024 年 96 项国家级种业政策经历"种业市场化→应对全球化→现代化与自立自强"三阶段；政策话语从营造市场环境转向种源"卡脖子"与科技自立 | Hu, Xiong & Jiang 2025, DOI 10.3390/agriculture15222383 | 2025-11-19 | Undermind: "seed industry revitalization action plan evaluation" | 高 |
| 1.6 | 2011 年以来种业整合政策使种企数量锐减、并购加速；形成中信集团—中化集团（先正达）—国投集团"三极"格局；CR5 由 2019 年 9.6% 升至 2023 年 19.2%，但"集中度提升未自动转化为国际竞争力" | Wang & Kang 2025, DOI 10.52819/jnes.2025.37.3.1 | 2025-12 | Undermind: "R&D intensity listed seed companies" | 高 |
| 1.7 | 私营农业 R&D 自 2000 年起因农业企业私有化快速增长；公共基础研究投入与私营 R&D 互补，公共技术开发投入则挤出私营 R&D | Hu, Liang, Pray, Huang & Jin 2011, JARE 36(2): 416–432 | 2011-08 | Undermind deep search | 高 |
| 1.8 | 2003 年农业企业农业研发投入相当于公共投入的 10% 以上（含技术密集型资本则达 30%）；调查 500 余家龙头企业 | Zhang, Fan & Qian 2005（IFPRI 会议论文） | 2005 | Undermind deep search | 中 |
| 1.9 | 政府补贴、与高校/院所或国企的 R&D 合作、既往专利活动提高企业生物技术 R&D 投入；已销售转基因产品的企业与国有企业投入更低（103 家农化/种子企业调查） | Deng, Hu, Pray & Jin 2019, DOI 10.1016/j.techfore.2019.07.011 | 2019-10 | Undermind | 高 |
| 1.10 | 中央补贴显著促进种企创新，地方补贴效果未获确认但提升企业当期经济绩效（2019 年种企面板） | Yao & Qiao 2023, DOI 10.3390/su15021049 | 2023-01 | Undermind deep search | 高 |
| 1.11 | 农业国企整体创新绩效最高，但在粮食主产区和种业中国企创新绩效并不优于民企（117 家农业上市公司 2004–2022） | Li Q. et al. 2025, Cogent Business & Management（Consensus） | 2025 | Consensus: "seed company R&D intensity performance" | 中 |
| 1.12 | 30 省育种 R&D 效率年均增长仅 1.9%，增长源于技术进步而非技术效率改善 | 喻亚平, 余利丰 2016 (DEA-Malmquist) | 2016 | Undermind deep search | 高（摘要原文） |

### 1.2 文献条目

1. Xu, S., Cao, C. 2025. Historical transitions of seed breeding in China: From socialist cooperation to joint research. *Journal of Rural Studies*, 114: 103592. DOI 10.1016/j.jrurstud.2025.103592. [Undermind/WebSearch; SSCI，估中科院 1–2 区；摘要不可得]
2. Li, J., Jiggins, J., Lammerts van Bueren, E.T., Leeuwis, C. 2012. Towards a regime change in the organization of the seed supply system in China. *Experimental Agriculture*, 49(1): 114–133. DOI 10.1017/S001447971200097X. [Undermind; SCI，估 3 区]
3. Xu, S. 2021. Rethinking the liberation of China's seed market: a comparative study of China's regulatory frameworks with EU and US. *Agroecology and Sustainable Food Systems*, 46(2): 251–272. DOI 10.1080/21683565.2021.1989104. [Undermind; SCI/SSCI，估 2–3 区] 结论：中国种业治理从类欧盟"预防型"转向类美国"强化法律手段的自治型"，将强化大型农企的全球权力、削弱种子主权。
4. Hu, S., Xiong, C., Jiang, D. 2025. Enhancing the marketization and globalization response capacity of policies: Evolution of China's seed industry policies since the 21st century. *Agriculture*, 15(22): 2383. DOI 10.3390/agriculture15222383. [Undermind; SCI，估 2–3 区]
5. Wang, N., Kang, S. 2025. China's seed industry restructuring policy and changes in corporate productivity. *Journal of Northeast Asian Economic Studies*（韩国东北亚经济学会）, 37(3). DOI 10.52819/jnes.2025.37.3.1. [Undermind; 非 SCI/SSCI]
6. Zheng, H., et al. 2021. Overview of the global crop seed industry and strategic thinking on its development in China. *Strategic Study of CAE (中国工程科学)*, 23(4). DOI 10.15302/J-SSCAE-2021.04.022. [Consensus/WebSearch; 中文核心/CSCD]
7. Hu, R., Huang, X., Mei, Y. 2025. The current status, challenges, and countermeasures of China's seed industry. *Modern Science*（工具索引名，期刊名待核）. DOI 10.3724/j.issn.1671-4342.20250067. [Consensus/Undermind] 结论：企业"多小散弱"、研发投入不足、种质资源利用低效，建议政府主体退出商业化育种、强化审定退出机制。
8. Yu, X., et al. 2020. Sustainable collaborative innovation between research institutions and seed enterprises in China. *Sustainability*, 12(2). DOI 未确认（Consensus 链接 https://consensus.app/papers/details/6d36124d79c750aeb41d63277d837f2b/）. [Consensus; SSCI/SCI，估 3 区] 533 名与种企合作的科研人员 SEM。
9. Hu, P., Shang, Q., Liu, W., Zhao, L. 2026. Level of industry–university–research cooperation and technological innovation performance in plant breeding enterprises: The moderating effects of absorptive capacity and government support. *Sustainability*, 18(7): 3562. DOI 10.3390/su18073562. [Undermind] 290 家育种企业问卷 SEM。
10. Liu, Z., Kemp, R., Jongsma, M., Huang, C., Dons, J., Omta, S. 2014. Key success factors of innovation projects of vegetable breeding companies in China. *IFAMR*, 17(4): 177–204. DOI 10.22004/AG.ECON.188714. [Undermind]
11. Zhang, N. 2023. The development of Chinese seed industry: From company value chain upgrading perspective. *Frontiers in Business, Economics and Management*, 10(1). DOI 10.54097/fbem.v10i1.9858. [Undermind; 非核心]
12. 公茂刚, 高心宇. 2025. 基于全产业链整合的现代种业创新发展机制与路径研究. *农业现代化研究*（网络首发）. DOI 10.13872/j.1000-0275.2025.0749. https://nyxdhyj.isa.ac.cn/cn/article/pdf/preview/10.13872/j.1000-0275.2025.0749.pdf [WebSearch; CSCD/北大核心]
13. Chen, C., Gao, J., Cao, H., Chen, W. 2024. Unpacking the agricultural innovation and diffusion for modernizing the smallholders in rural China: From the perspective of agricultural innovation system and its governance. *Journal of Rural Studies*, 110: 103385. DOI 10.1016/j.jrurstud.2024.103385. [Undermind; 估 1–2 区；摘要不可得]
14. Cao, H.-Y. 2015. Research of the integration mode of seed enterprise in China based on the value chain.（中文期刊，Semantic Scholar 链接 https://www.semanticscholar.org/paper/51c01e8686b02192203ffd22e1a92b885a21517f）[Undermind deep search] 结论：中国种业"育、繁、推、销"四环节分离，现阶段应横向整合优先、积极推进纵向整合。
15. 任婉婉 (Ren, W.-W.). 2013. Development bottleneck, strategic opportunities and American experience: A study of industrial chain extension in China's seed industry. *现代财经（天津财经大学学报）*. [Undermind deep search]
16. Rozelle, S., Pray, C., Huang, J. 1997. Agricultural research policy in China: Testing the limits of commercialization-led reform. *Comparative Economic Studies*, 39(2): 37–71. DOI 10.1057/ces.1997.8. [Undermind]
17. Hu, R., Liang, Q., Pray, C., Huang, J., Jin, Y. 2011. Privatization, public R&D policy, and private R&D investment in China's agriculture. *Journal of Agricultural and Resource Economics*, 36(2): 416–432. DOI 10.22004/AG.ECON.117213. [Undermind deep search; SSCI，估 3 区]
18. Zhang, H., Fan, S., Qian, K. 2005. The role of agribusiness firms in agricultural research: The case of China. IFPRI 会议论文. https://www.semanticscholar.org/paper/a7cf1548a0ea75af88a8014cf303a48df5f2fefa [Undermind]
19. Deng, H., Hu, R., Pray, C., Jin, Y. 2019. Impact of government policies on private R&D investment in agricultural biotechnology: Evidence from chemical and pesticide firms in China. *Technological Forecasting and Social Change*, 147. DOI 10.1016/j.techfore.2019.07.011. [Undermind; SSCI，估 1 区]
20. Jin, Y., Hu, Y., Pray, C., Hu, R. 2017. Impact of government science and technology policies with a focus on biotechnology research on commercial agricultural innovation in China. *China Agricultural Economic Review*, 9(3): 438–452. DOI 10.1108/CAER-05-2017-0096. [Undermind; SSCI，估 2 区] 公共生物技术专利数正向影响企业专利数；公共 R&D 支出无显著效应；跨国/上市企业专利更少。
21. Cai, J., Hu, R., Huang, J., Wang, X. 2017. Innovations in genetically modified agricultural technologies in China's public sector: Successes and challenges. *China Agricultural Economic Review*, 9(2): 317–330. DOI 10.1108/CAER-10-2016-0170. [Undermind] 197 个院所 487 个课题组；公共转基因专项"缺乏协调"。
22. Yao, B., Qiao, F. 2023. The heterogeneous effects of central and local subsidies on firms' innovation. *Sustainability*, 15(2): 1049. DOI 10.3390/su15021049. [Undermind]
23. Pray, C.E. 2001. Public-private sector linkages in research and development: Biotechnology and the seed industry in Brazil, China and India. *American Journal of Agricultural Economics*, 83(3): 742–747. DOI 10.1111/0002-9092.00201. [Undermind; 估 1 区]
24. Spielman, D.J., Kennedy, A. 2016. Towards better metrics and policymaking for seed system development: Insights from Asia's seed industry. *Agricultural Systems*, 147: 111–122. DOI 10.1016/j.agsy.2016.05.015. [Undermind; 估 1 区]
25. 喻亚平, 余利丰. 2016. 我国农业育种研发效率的实证分析——基于 DEA-Malmquist 指数分析的视角. （期刊名待核）, pp. 9–15. https://www.semanticscholar.org/paper/665cd9852833225d7ab16915710a8fa53d0b649a [Undermind]
26. Li, Q., et al. 2025. Firm ownership, institutional environment and agricultural innovation: evidence from China. *Cogent Business & Management*. DOI 未确认（https://consensus.app/papers/details/16016fa13b2353e585d518385f9c6c91/）. [Consensus]

---

## 2. 种子企业主导的订单农业 / 纵向一体化 / 种粮一体化

### 2.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 2.1 | 三级供应链（种企—种植户—收购/加工商）模型：种企主导的订单农业"获得质量优势并提高利润"；**惩罚合同在质量与利润上表现最差**；收益分享比例（下游→上游）提高使全链利润上升；成本分担比例与全链利润关系非单调；以中国鲜食玉米产业为数值算例 | Xie, Yuan, Zhu & Li 2023, *Agribusiness* 39(4): 1173–1198, https://onlinelibrary.wiley.com/doi/abs/10.1002/agr.21823 | 2023 | WebSearch: "Contract farming led by a seed enterprise…10.1002/agr.21823"; SG; Undermind | 高 |
| 2.2 | 荃银高科（Winall Hi-Tech）订单农业毛利率由 2018 年 3.56% 升至 2021 年 7.6%；该业务占营收比重由 5.87%（2018）升至 28.73%（2021）（引 Eastmoney 2022） | Xie et al. 2023（正文 Background 段） | 2023 | SG 段落 | 高（论文转引二手数据） |
| 2.3 | 隆平高科作为鲜食玉米订单链主：播种前与收购/加工商签订合作意向，后者承诺以更高价格收购签约农户的优质鲜食玉米；隆平高科与荃银高科同属 2022 年农业农村部认定的 53 家"龙头"种企 | Xie et al. 2023（正文） | 2023 | SG 段落 | 高 |
| 2.4 | 中国订单农业面积由 2002 年 2180 万公顷增至 2020 年约 3333 万公顷，约占播种面积 20%；1.25 亿农户通过 1542 家龙头企业、220 万家合作社、87 万家家庭农场融入市场（引 MARA 2021） | Xie et al. 2023 | 2023 | SG 段落 | 高（转引） |
| 2.5 | 普通玉米用种成本 55.72 元/亩、用种量 1.94 kg/亩（约 29 元/kg）；优质杂交种售价 40–100 元/kg；鲜食玉米种子均价取 50 元/kg，种企单位生产成本约 42 元/kg（反推：售价×(1−8% 利润率−8.12% 研发强度)） | Xie et al. 2023（数值分析段） | 2023 | SG 段落 | 高 |
| 2.6 | 中国订单农业三大特征：对农村不平等影响不一、合约关系不稳定、相对其他替代组织缺乏竞争力；解释因素为强集体制度、国家积极支农、强大国内市场；农业向纵向一体化转向正在削弱这些条件 | Zhang Q.F. 2012, *J. Agrarian Change* 12(4): 460–483, DOI 10.1111/j.1471-0366.2012.00352.x | 2012-10 | SG | 高 |
| 2.7 | 企业视产品质量为签约首要动机，农户视价格稳定与市场准入为主要收益（村级与企业级调查） | Guo, Jolly & Zhu 2007, *Comparative Economic Studies* 49(2): 285–312, DOI 10.1057/palgrave.ces.8100202 | 2007 | Consensus/Undermind | 高 |
| 2.8 | 粮食订单低履约率：龙头企业建基地、免费供优质种与技术，但个体粮商以略高于合同价上门收购形成三方博弈；"两步结算"（先按合同价结算，再按企业利润返利）可使多数农户履约 | Luo, Fang & Wang 2013, *China: An International Journal* 11(3): 123–135, DOI 10.1353/chn.2013.0024 | 2013-12 | Undermind deep search | 高 |
| 2.9 | 关系合约框架下"龙头企业+农户"与"龙头企业+农场"在贴现因子足够高时均可达一次最优；价格高度波动时"龙头企业+农场"更优 | 聂辉华 2013（中国农业产业化的最优契约与模式） | 2013 | Undermind deep search | 高（摘要） |
| 2.10 | 五常大米订单农业：78 户；参与显著提高稻谷田头价与成本利润率；有机/绿色种植经验农户更可能参与 | Wu, Wu, Yin & Chien 2020, *JARQ* 54(2): 171–177, DOI 10.6090/jarq.54.171 | 2020-04 | Undermind | 高 |
| 2.11 | 安徽 2032 户小麦农户：参与产业化组织显著提高净收入，"农户+合作社/农业企业"模式增收效应最强，机制为土地生产率与议价能力 | Zhang, Wan & Liu 2023, *Scientific Reports*, DOI 10.1038/s41598-023-43879-0 | 2023-10 | Undermind | 高 |
| 2.12 | 山东 719 户小麦农户：一体化模式显著提高绿色技术效率，准一体化模式不显著；准一体化中合同收购价须高出当地均价 **19.3%** 以上才有调节效应 | Li & Wang 2024, *Front. Sustain. Food Syst.* 8: 1368997, DOI 10.3389/fsufs.2024.1368997 | 2024-05 | Undermind deep search | 高 |
| 2.13 | 河南 1039 户粮农（2022）：合作社/企业带动的合同参与提高农业绿色生产率，机制为农机、农资标准化、技术指导服务 | Zhang & Wu 2023, *Agriculture* 13(9): 1851, DOI 10.3390/agriculture13091851 | 2023-09 | Undermind | 高 |
| 2.14 | 保底价、奖金、长期合同显著提高履约率；风险规避/损失规避更强的农户更可能履约（皖苏果农田野实验） | Hou, Wu & Hou 2020, *IJERPH* 17(8): 2733, DOI 10.3390/ijerph17082733 | 2020-04 | Undermind/PubMed | 高 |
| 2.15 | 山东 286 户果农：46.1% 的农户实际交付企业果品不足其销量一半；交易地点远、延期结算降低履约；对龙头企业信任、合同溢价提高履约 | 郭亮 2015 | 2015 | Undermind deep search | 高（摘要） |
| 2.16 | 山东、山西、宁夏 1041 户（2009）：参与订单农业提高机械与雇工支出及亩均农业收入（三阶段回归纠正内生性） | 刘晓鸥, 邸元 2013 | 2013 | Undermind 中文检索 | 高（摘要） |
| 2.17 | 契约理论：动态激励（绩效工资+递延支付）使买方内化纵向与跨期外部性；买方长期视角下愿付更高价格保障农户长期生存 | Zhang W. et al. 2023, *POM* 32(7): 2049–2067, DOI 10.1111/poms.13956 | 2023 | Consensus/Undermind | 高 |
| 2.18 | "公司+农户"引入高价值产品后所有农户福利改善，但若高价值产品生产成本高则出现"不平等扩大型"均衡 | Chen & Chen 2021, *POM* 30(8): 2395–2419, DOI 10.1111/poms.13382 | 2021 | Consensus/Undermind | 高 |
| 2.19 | 越南乳业框架田野实验：低质惩罚推动投入增加、质量改善，稳定高质奖金效果更强 | Saenger, Qaim, Torero & Viceisza 2013, *Agricultural Economics* 44(3): 297–308, DOI 10.1111/agec.12012 | 2013 | Undermind | 高 |
| 2.20 | 种子市场化改革始于 2001 年《种子法》实施后，制种组织模式由行政命令统一安排分化为多种利益联结模式（江苏实证） | 冯德胜, 潘刚, 荆飞 2008 | 2008 | Undermind deep search | 高（摘要） |
| 2.21 | 订单履约困境根源是价格风险在双方分担不合理；"期货+订单"（黑龙江玉米案例）可分散企业事后价格风险 | 徐雪高, 沈杰 2010 | 2010 | Undermind deep search | 高（摘要） |
| 2.22 | 龙头企业—家庭农场—综合服务商三方演化博弈：补偿机制可激励龙头企业但过度惩罚侵蚀互惠；收益分享比例存在阈值效应 | Hu, Fang & Liu 2025, *Sustainability* 17(17): 7975, DOI 10.3390/su17177975 | 2025-09 | Undermind | 高 |

### 2.2 文献条目

27. Xie, Z., Yuan, S., Zhu, J., Li, W. 2023. Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? *Agribusiness*, 39(4): 1173–1198. DOI 10.1002/agr.21823. [WebSearch/SG/Consensus/Undermind; SSCI，估 2–3 区（农经）] **核心文献**。
28. Guo, H., Jolly, R.W., Zhu, J. 2007. Contract farming in China: Perspectives of farm households and agribusiness firms. *Comparative Economic Studies*, 49(2): 285–312. DOI 10.1057/palgrave.ces.8100202. [Consensus/Undermind]
29. Guo, H., Jolly, R.W. 2008. Contractual arrangements and enforcement in transition agriculture: Theory and evidence from China. *Food Policy*, 33(6): 570–575. DOI 10.1016/j.foodpol.2008.04.003. [Undermind deep search; 估 1 区]
30. Zhang, Q.F. 2012. The political economy of contract farming in China's agrarian transition. *Journal of Agrarian Change*, 12(4): 460–483. DOI 10.1111/j.1471-0366.2012.00352.x. [SG/Undermind; SSCI，估 1–2 区]
31. Wang, H.H., Wang, Y., Delgado, M.S. 2014. The transition to modern agriculture: Contract farming in developing economies. *American Journal of Agricultural Economics*, 96(5): 1257–1271. DOI 10.1093/ajae/aau036. [SG/Undermind; 估 1 区] 以中国为案例的订单农业实证综述。
32. Miyata, S., Minot, N., Hu, D. 2009. Impact of contract farming on income: Linking small farmers, packers, and supermarkets in China. *World Development*, 37(11): 1781–1790. DOI 10.1016/j.worlddev.2008.08.025. [Undermind; 估 1 区]
33. Jia, X., Huang, J. 2011. Contractual arrangements between farmer cooperatives and buyers in China. *Food Policy*, 36(5): 656–666. DOI 10.1016/j.foodpol.2011.06.007. [Undermind; 摘要不可得]
34. Wang, H., Zhang, Y., Wu, L. 2011. Is contract farming a risk management instrument for Chinese farmers? Evidence from a survey of vegetable farmers in Shandong. *China Agricultural Economic Review*, 3(4): 489–505. DOI 10.1108/17561371111192347. [Undermind] 结论：农户签约动机是寻求更优报价与降低交易成本而非价格风险管理；风险偏好者反而更多签约。
35. Luo, Y., Fang, X., Wang, H.H. 2013. The problem of low contract compliance rate in grain transactions in China. *China: An International Journal*, 11(3): 123–135. DOI 10.1353/chn.2013.0024. [Undermind]
36. 聂辉华 (Nie, H.). 2013. The optimal agricultural contracts and the models of agricultural industrialization in China. https://www.semanticscholar.org/paper/01bd8159496e69a3466613a8c8da94542a50d679 [Undermind]
37. Wu, W., Wu, G., Yin, C., Chien, H. 2020. Impact of contract farming on farmers' income: A case of Wuchang rice in China. *JARQ – Japan Agricultural Research Quarterly*, 54(2): 171–177. DOI 10.6090/jarq.54.171. [Undermind; SCI，估 4 区]
38. Li, J.-J., Li, J.-P., Xiao, Q., Wu, H., Liu, D. 2026. Premium procurement channel access and farm-gate prices: evidence from rice farmers in China. *Food Policy*, 103132. DOI 10.1016/j.foodpol.2026.103132. [Undermind; 估 1 区；摘要不可得] ——与"优质优价渠道"最直接相关的新文献。
39. Zhang, X., Wan, X., Liu, P. 2023. The impact of participation in agricultural industry organizational models on crop yields: evidence from Chinese wheat growers. *Scientific Reports*, 13. DOI 10.1038/s41598-023-43879-0. [Undermind; 估 2–3 区]
40. Li, Q., Wang, Z. 2024. Impact of contract farming on green technological efficiency of farmers: a comparative study of two contract organizational models. *Frontiers in Sustainable Food Systems*, 8: 1368997. DOI 10.3389/fsufs.2024.1368997. [Undermind; 估 2–3 区]
41. Zhang, H., Wu, D. 2023. The impact of rural industrial integration on agricultural green productivity based on the contract choice perspective of farmers. *Agriculture*, 13(9): 1851. DOI 10.3390/agriculture13091851. [Undermind]
42. Hou, J., Wu, L., Hou, B. 2020. Risk attitude, contract arrangements and enforcement in food safety governance: A China's agri-food supply chain scenario. *IJERPH*, 17(8): 2733. DOI 10.3390/ijerph17082733. [Undermind/PubMed]
43. Wan, J., Zeng, L., Ao, J. 2018. Specific investment, relational governance and cooperation risk: from the perspective of farmers in China's "Company+Farmers" alliance. *Applied Economics*, 51(7): 676–686. DOI 10.1080/00036846.2018.1508868. [Undermind; SSCI，估 3 区]
44. Fu, S., Zhan, Y., Ouyang, J., Ding, Y., Tan, K., Fu, L. 2020. Power, supply chain integration and quality performance of agricultural products: evidence from contract farming in China. *Production Planning & Control*, 31(14): 1119–1135. DOI 10.1080/09537287.2020.1794074. [Consensus/Undermind; 78 家企业 + 321 户]
45. Fu, S., Lin, J., Sun, L. 2013. An empirical examination of the stability of the alliance of "a company+farmers": From the perspective of farmers. *Chinese Management Studies*, 7(3): 382–402. DOI 10.1108/CMS-09-2012-0134. [Undermind]
46. Fu, S., He, G., Wang, Q., Huo, B., Ding, Y. 2022. Power use, cooperative behavior and alliance performance: evidence from contract farming supply chains in China. *Industrial Management & Data Systems*, 122(3): 794–820. DOI 10.1108/imds-11-2021-0661. [Undermind] 202 家企业 + 462 户对偶数据。
47. Li, Y., Xu, Y. 2024. How China's agribusiness achieves reciprocal symbiosis with farmers? A comparative analysis of the investment sector. *Agribusiness*, 40. DOI 10.1002/agr.21957. [Undermind] 109 个农企下乡案例 csQCA。
48. Chen, J., Chen, Y.-J. 2021. The impact of contract farming on agricultural product supply in developing economies. *Production and Operations Management*, 30(8): 2395–2419. DOI 10.1111/poms.13382. [Consensus/Undermind; 估 1–2 区（管理）]
49. Zhang, W., et al. 2023. Dynamic incentives for sustainable contract farming. *Production and Operations Management*, 32(7): 2049–2067. DOI 10.1111/poms.13956. [Consensus/Undermind]
50. Saenger, C., Qaim, M., Torero, M., Viceisza, A. 2013. Contract farming and smallholder incentives to produce high quality: experimental evidence from the Vietnamese dairy sector. *Agricultural Economics*, 44(3): 297–308. DOI 10.1111/agec.12012. [Undermind; 估 2 区]
51. Goodhue, R.E. 2011. Food quality: The design of incentive contracts. *Annual Review of Resource Economics*, 3: 119–140. DOI 10.1146/annurev-resource-040709-135037. [Undermind; 估 1 区]
52. Goodhue, R.E., Mohapatra, S., Rausser, G.C. 2010. Interactions between incentive instruments: Contracts and quality in processing tomatoes. *AJAE*, 92(5): 1283–1293. DOI 10.1093/ajae/aaq061. [Undermind]
53. Hueth, B., Ligon, E. 2002. Estimation of an efficient tomato contract. *European Review of Agricultural Economics*, 29(2): 237–253. DOI 10.1093/eurrag/29.2.237. [Undermind]
54. Yu, J., Bonroy, O., Bouamra-Mechemache, Z. 2022. Quality and quantity incentives under downstream contracts: A role for agricultural cooperatives? *AJAE*. DOI 10.1111/ajae.12352. [Undermind; 摘要不可得]
55. Bellemare, M.F. 2012. As you sow, so shall you reap: The welfare impacts of contract farming. *World Development*, 40(7): 1418–1434. DOI 10.1016/j.worlddev.2011.12.008. [Undermind]
56. Maertens, M., Vande Velde, K. 2017. Contract-farming in staple food chains: The case of rice in Benin. *World Development*, 95: 73–87. DOI 10.1016/j.worlddev.2017.02.011. [Undermind]
57. Ton, G., Desiere, S., Vellema, W., Weituschat, S., D'Haese, M. 2017. The effectiveness of contract farming for raising income of smallholder farmers in low- and middle-income countries: a systematic review. *Campbell Systematic Reviews*, 13(1): 1–131. DOI 10.4073/csr.2017.13. [SG] 75 份报告，22 份（26 个干预）进入 meta 分析。
58. Li, J., Qing, P., Hu, W., Li, M. 2021. Contract farming, community effect, and farmer valuation of biofortified crop varieties in China: The case of high-zinc wheat. *Review of Development Economics*, 26(2): 1035–1055. DOI 10.1111/rode.12847. [SG/Undermind] 订单农业显著提高农户对高锌小麦品种的估值。
59. Hu, R., Fang, H., Liu, W. 2025. How do vertical alliances form in agricultural supply chains? An evolutionary game analysis based on Chinese experience. *Sustainability*, 17(17): 7975. DOI 10.3390/su17177975. [Undermind]
60. 刘晓鸥, 邸元. 2013. 订单农业对农户农业生产的影响——基于三省（区）1041 个农户调查数据的分析. （期刊名工具未给出，疑为《中国农村经济》2013 年第 4 期，待核）, pp. 48–59. https://www.semanticscholar.org/paper/679230338cbbf76d2dd071d74bb17466bbaf3ae7 [Undermind]
61. 冯德胜, 潘刚, 荆飞. 2008. 种子公司与制种农户利益联接机制调查与分析——基于江苏省的实证研究. pp. 61–62. https://www.semanticscholar.org/paper/fdc192a2029831067c3ade956dac35fe68b23702 [Undermind]
62. 徐雪高, 沈杰. 2010. 订单农业履约困境的根源及发展方向——以黑龙江省某企业"期货+订单"为例. pp. 45–49. https://www.semanticscholar.org/paper/9ef4fca145444f760c95a169d978f0be8cc6aa22 [Undermind]
63. 郭亮. 2015. 订单交易成本、关系信任对农户履约行为的影响——以山东省 286 户果农调查数据为例. pp. 56–61. https://www.semanticscholar.org/paper/57c9a020c3bbd5e35782f76249df2814e07d6220 [Undermind]
64. 郭红东. 2005. 农业龙头企业与农户订单安排及履约机制研究（专著）. https://www.semanticscholar.org/paper/656315cc69016b4f6f2de1455c329c766ed964ff [Undermind]
65. Ma, W., Abdulai, A. 2016. Linking apple farmers to markets: Determinants and impacts of marketing contracts in China. *China Agricultural Economic Review*, 8(1): 2–21. DOI 10.1108/CAER-04-2015-0035. [Undermind] 书面合同提高净收益，口头合同相反。
66. Zhang, H., Ma, W. 2024. Marketing contracts and technical efficiency of citrus production. *China Agricultural Economic Review*. DOI 10.1108/caer-10-2023-0280. [Undermind] 书面/口头合同用户技术效率分别高 18.3%/10.5%。
67. Cai, R., Ma, W. 2015. Trust, transaction costs, and contract enforcement: evidence from apple farmers in China. *British Food Journal*, 117(10): 2598–2608. DOI 10.1108/BFJ-10-2014-0335. [Undermind]
68. Sun, X., et al. 2023. Promotion effect of agricultural production trusteeship on high-quality production of grain—Evidence from the perspective of farm households. *Agronomy*, 13(8): 2024. DOI 10.3390/agronomy13082024. [Undermind] 五个粮食主产省 PSM：托管后优质粮食生产水平提高 0.292（+87.4%）；农资供应服务 ATT 最高（0.287）。
69. Abler, D., Yu, X., Chen, D. 2011. Endogenous matching and contractual choice between agricultural processors and farmers in China. AAEA. DOI 10.22004/ag.econ.103805. [Undermind] 2003 年农业部加工企业调查；签约农户数越多越倾向"合作契约"。
70. Zylbersztajn, D., Farina, E. 1999. Strictly coordinated food-systems: Exploring the limits of the Coasian firm. *IFAMR*, 2(2): 249–265. DOI 10.1016/S1096-7508(00)00014-8. [Undermind]
71. Zhang, X., Aramyan, L. 2009. A conceptual framework for supply chain governance: An application to agri-food chains in China. *China Agricultural Economic Review*, 1(2): 136–154. DOI 10.1108/17561370910927408. [Undermind]
72. Zhang, L., Li, G., He, H. 2018. Controlling corporate power in China: Case studies of seed companies and water distribution. *American Journal of Economics and Sociology*, 77(2): 511–540. DOI 10.1111/ajes.12210. [SG] 种子供应中的企业租金与潜在腐败案例。
73. Zhang, J., Busck, A., Kristensen, S.B.P. 2025. Integrating farmers into contract farming in peripheral rural areas in China. *Land*, 14(5): 976. DOI 10.3390/land14050976. [Undermind]
74. Huang, P.C.C. 2012. China's new-age small farms and their vertical integration: Agribusiness or co-ops? *Rural China*, 8(1): 11–30. DOI 10.1163/22136746-00801002. [Undermind]
75. Simmons, P., Winters, P., Patrick, I. 2005. An analysis of contract farming in East Java, Bali, and Lombok, Indonesia. *Agricultural Economics*, 33(s3): 513–525. DOI 10.1111/j.1574-0864.2005.00096.x. [SG] 含玉米制种、水稻制种合同的参与与毛利效应。
76. Schewe, R.L., Stuart, D. 2016. Why don't they just change? Contract farming, informational influence, and barriers to agricultural climate change mitigation. *Rural Sociology*, 82(2): 226–262. DOI 10.1111/ruso.12122. [SG] 美国制种玉米合同农户。
77. Veettil, P.C., et al. 2021. Group contracts and sustainability: Experimental evidence from smallholder seed production. *PLoS ONE*. DOI 未确认（https://consensus.app/papers/details/4411cc6094a05d38a1297830fd64561c/）. [Consensus]

---

## 3. 种业政策与制度改革（Seed Law、PVP/EDV、品种审定、许可费、种业振兴、生物育种商业化治理）

### 3.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 3.1 | 种子管理制度改革（2015 年《种子法》修订、2016 年中落地）使品种许可费**平均下降近一半**；常规稻品种许可价降幅最大，其次玉米；**杂交稻品种许可费无显著影响**；公共育成品种许可费下降 63%，私营育成品种无显著影响；小型种企与非国企支付的许可费分别下降 62% 与 65%，大型种企与国企不显著；更新、更高产、独占许可的品种许可费显著更高 | Xiang, Yang, Wang & Huang 2025, *Agribusiness*, DOI 10.1002/agr.22020（PKU CCAP 全文 PDF: http://www.ccap.pku.edu.cn/docs//2025-12/c35ae861620b4f79bb416f3685f064e1.pdf） | 2025-01-15 | WebSearch/Consensus/SG/Undermind | 高 |
| 3.2 | 一次性固定许可费（upfront lump-sum）是最常用的许可方式；许可合同三种形式：一次性固定费、产量提成、二者组合；87%（75/86）品种许可由注册资本 <5000 万元的种企购买，15%（13/86）由国企购买 | 同上（正文 Table 2/3 段） | 2025 | SG 段落 | 高 |
| 3.3 | 中国 PVP 制度自 1997 年建立；PVP 申请呈现"期权"特征——申请与维持权利是对未来品种销售收益流的期权 | Koo, Pardey, Qian & Zhang 2006, *Agricultural Economics* 35(1): 35–48, DOI 10.1111/j.1574-0862.2006.00137.x | 2006 | SG/Undermind | 高 |
| 3.4 | 受 PVP 保护的水稻品种在种植面积更小的情况下价格更高（创造可提取租金） | Hu & Pray 2006（Impacts of PBR on rice seed prices and variety adoption）; Hu et al. 2006（Impact of PBR on technology availability） | 2006 | Undermind deep search 摘要综合 | 中 |
| 3.5 | 国家品种审定政策显著提高审定水稻品种产量性状，但对抗病性有负向影响；良种补贴提高采用品种的品质但降低产量；审定品种品质持续改善而农户采用品种品质呈下降趋势（四十年数据） | Zhao, Deng, Hu & Xiong 2022, *Agronomy* 12(4): 917, DOI 10.3390/agronomy12040917 | 2022-04 | Undermind | 高 |
| 3.6 | 2016 年 1 月 1 日实施的新《种子法》缩小主要农作物审定范围、确立大型种企绿色通道审定制度、建立品种登记框架 | 韩伟, 牛家坤 2016 | 2016 | Undermind deep search | 高（摘要） |
| 3.7 | 品种试验三类：国家统一试验、绿色通道试验（2014 年起，面向育繁推一体化企业）、联合体试验（2016 年起）；2022 年起农业农村部对绿色通道/联合体试验开展专项整治；2024 年 3 月国家品审办通报第三批整治处理结果 | 农业农村部 http://www.moa.gov.cn/xw/zwdt/202209/t20220901_6408346.htm ；中国政府网 https://www.gov.cn/lianbo/bumen/202403/content_6940381.htm ；种业管理司 http://www.zys.moa.gov.cn/gsgg/202410/t20241009_6463875.htm | 2022-09 / 2024-03 / 2024-10 | WebSearch: "品种审定制度改革 绿色通道 联合体试验" | 高（政府文件） |
| 3.8 | 派生品种（EDV）对中国水稻自主创新的影响：原始品种溢出促进自主创新；派生品种未对原始创新造成负面影响；溢出主要在公共科研机构之间及从公共机构到企业，企业对外溢出很少 | 詹金涛 (Zhan, J.) 2013, 南京农业大学学报（社科版） | 2013 | Undermind deep search | 高（摘要） |
| 3.9 | 中国作为 UPOV1978 成员，正通过《种子法》引入 EDV 制度；EDV 阈值需按作物逐一研究 | Smith 2021, *Agronomy*（预印本 DOI 10.20944/preprints202105.0398.v1） | 2021 | Consensus | 中 |
| 3.10 | 中国 NBT（基因编辑）监管处于欧盟"过程导向"与美/阿"产品导向"之间的中间状态；制度障碍包括产学研利益联结弱、审批路径依赖传统转基因逻辑、PVP/EDV 规则未及时响应 NBT、消费者信任不足；建议差异化风险审查、完善 EDV 与惩罚性赔偿 | Qin & Su 2026, *GM Crops & Food*, DOI 10.1080/21645698.2025.2610592 | 2026-01-12 | Consensus/PubMed/Undermind | 高 |
| 3.11 | 2021 年中国启动首个转基因粮食作物商业化种植试点并随后扩大；此前仅商业化抗虫棉与抗病毒木瓜；GMO 安全监管分四阶段：探索（1993–2000）、发展（2001–2010）、完善（2011–2020）、当前（2021–） | Mou et al. 2025, *GM Crops & Food* 16(1): 450–481, DOI 10.1080/21645698.2025.2520664; Liang et al. 2022, *aBIOTECH* 3: 237–249, DOI 10.1007/s42994-022-00086-1 | 2025-06 / 2022-12 | Undermind/PubMed | 高 |
| 3.12 | 111 家种企（2019 年调查）：开展基因编辑研究的公司有限且多为大企业；约 55% 经理愿意开发/销售 SDN-1/SDN-2 产品，46% 支持 SDN-3；大企业、研究人员学历高、有转基因投资经验、与公共机构合作的企业更可能投资基因编辑 | Kang, Deng, Pray & Hu 2022, *GM Crops & Food* 13(1): 309–326, DOI 10.1080/21645698.2022.2140567 | 2022-11 | Undermind deep search | 高 |
| 3.13 | 160 名食品/饲料/农化/种子企业经理（2013–14）：多数担忧转基因食品；1/3 企业投资生物技术 R&D；<15% 经理曾游说政府 | Deng et al. 2017, *CAER* 9(3): 385–396, DOI 10.1108/CAER-10-2016-0162 | 2017-08 | Undermind deep search | 高 |
| 3.14 | 2021 年 12 月《种子法》修正与 2015 年修法：美国 USDA/FAS GAIN 报告有专门解读 | USDA FAS GAIN "China Amends Seed Law to Develop Seed Industry" (2015-12-01); "Planting Seeds Annual 2025" (CH2026-0017) https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Planting+Seeds+Annual+2025_Beijing_China+-+People%27s+Republic+of_CH2026-0017.pdf | 2015-12 / 2026 | WebSearch | 中（仅标题） |
| 3.15 | 最高法"黄华占"案：独占许可人有诉权；侵权赔偿可按许可费倍数计算，最高 300 万元法定赔偿（《种子法》第 73 条） | IIC 2023 案例报道（Consensus） | 2023 | Consensus | 中 |
| 3.16 | 2021 年 12 月新修《种子法》引入 EDV、加大惩罚性赔偿——本次检索**未找到任何因果评估论文**，仅法学评述（Xie & Huang 2025; Yu & Liu 2025; Gao 2025） | — | — | Undermind: "2021 amendment Seed Law EDV" | 高（缺口） |

### 3.2 文献条目

78. Xiang, C., Yang, R., Wang, X., Huang, J. 2025. Impact of seed regulation reform on licensing fees of varieties in China. *Agribusiness* (early view). DOI 10.1002/agr.22020. [WebSearch/Consensus/SG/Undermind; 估 2–3 区] **核心文献**。
79. Koo, B., Pardey, P.G., Qian, K., Zhang, Y. 2006. An option perspective on generating and maintaining plant variety rights in China. *Agricultural Economics*, 35(1): 35–48. DOI 10.1111/j.1574-0862.2006.00137.x. [SG/Undermind; 估 2 区]
80. Hu, R., Pray, C., Huang, J., Rozelle, S., Fan, C., Zhang, C. 2009. Reforming intellectual property rights and the Bt cotton seed industry in China: Who benefits from policy reform? *Research Policy*, 38(5): 793–801. DOI 10.1016/j.respol.2008.12.008. [Undermind deep search; 估 1 区]
81. Hu, R., et al. 2006. The determinants of plant variety protection applications in China. *Chinese Journal of Population Resources and Environment*, 4(4): 53–62. DOI 10.1080/10042857.2007.10677502. [Undermind]
82. Zheng, S., Xu, P., Wang, Z. 2012. Farmers' adoption of new plant varieties under variety property right protection: Evidence from rural China. *China Agricultural Economic Review*, 4(1): 124–140. DOI 10.1108/17561371211196810. [Undermind] 22 省 341 户；经销商声誉与农户口碑显著。
83. Zhao, Y., Deng, H., Hu, R., Xiong, C. 2022. Impact of government policies on seed innovation in China. *Agronomy*, 12(4): 917. DOI 10.3390/agronomy12040917. [Undermind; 估 2 区]
84. 詹金涛. 2013. UPOV 派生品种制度对中国农业自主创新的影响：基于水稻新品种的实证. *南京农业大学学报（社会科学版）*. https://www.semanticscholar.org/paper/07ad4bc10cd674642bb2bb1faff167132de0a317 [Undermind]
85. 韩伟, 牛家坤. 2016. 新修正《种子法》规定的农作物品种审定与登记制度. pp. 19–20. [Undermind]
86. 李媛辉. 2015. 对农作物品种审定制度的再思考——演变、评述、反思与展望. pp. 120–125. [Undermind]；李媛辉, 董川玉. 2014. 论我国《种子法》的修改与完善——以品种审定制度为视角. pp. 57–64. [Undermind]
87. Qin, Y., Su, K. 2026. From lab to market: industrialization barriers and regulation optimization for new breeding technologies in China. *GM Crops & Food*, 17(1). DOI 10.1080/21645698.2025.2610592. [Consensus/PubMed; SCI，估 3 区]
88. Xie, S., Huang, L. 2025. Research on the intellectual property protection of genetically modified crops in China. *Biotechnology Law Report*, 44(5): 304–311. [Consensus/Undermind]
89. Yu, F., Liu, X. 2025. The institutional responses to new plant variety protection in China in the context of big data. *Frontiers in Plant Science*, 16: 1633734. DOI 10.3389/fpls.2025.1633734. [Consensus/Amass/Undermind; 估 2 区]
90. Smith, J.S.C. 2021. The future of essentially derived variety (EDV) status: Predominantly more explanations or essential change. *Agronomy*（预印本 DOI 10.20944/preprints202105.0398.v1；期刊版 DOI 待核）. [Consensus/Undermind]
91. Bostyn, S. 2021. Towards a fair scope of protection for plant breeders' rights in an era of new breeding techniques: Proposals for a modernization of the essentially derived variety concept. *Agronomy*, 11(8): 1511. DOI 10.3390/agronomy11081511. [Consensus/Undermind]
92. Rapela, M. 2025. Essentially derived varieties in the age of genome editing: Striking a balance between innovation and protection. *The Journal of World Intellectual Property*. DOI 未确认. [Consensus]
93. Prasanna, P., et al. 2023. Essentially derived variety concept in plant variety rights protection system: underlying economic theories, and issues in implementation. *Agricultural Economics Research Review*, 36(1): 77–86. DOI 10.5958/0974-0279.2023.00006.X. [Consensus/Undermind]
94. Hervouet, A., Lemarié, S. 2024. Farm-saved seed, royalty rates, and innovation in plant breeding. *AJAE*. DOI 10.1111/ajae.12489. [Undermind; 估 1 区] 六种农民自留种提成制度的福利比较。
95. Kolady, D.E., Spielman, D.J., Cavalieri, A. 2012. The impact of seed policy reforms and intellectual property rights on crop productivity in India. *Journal of Agricultural Economics*, 63(2): 361–384. DOI 10.1111/j.1477-9552.2012.00335.x. [SG; 估 2 区]
96. Thomson, R. 2014. The yield of plant variety protection. *AJAE*, 97(3): 762–785. DOI 10.1093/ajae/aau099. [SG]
97. Mou, T.-H., Song, Q., Liu, Y., Song, J. 2025. Initiating the commercialization of genetically modified staple crops in China: domestic biotechnological advancements, regulatory milestones, and governance frameworks. *GM Crops & Food*, 16(1): 450–481. DOI 10.1080/21645698.2025.2520664. [Undermind/PubMed]
98. Liang, J., et al. 2022. The evolution of China's regulation of agricultural biotechnology. *aBIOTECH*, 3(4): 237–249. DOI 10.1007/s42994-022-00086-1. [Undermind/PubMed]
99. Liang, J., et al. 2025. Agricultural biotechnology in China: product development, commercialization, and perspectives. *aBIOTECH*, 6: 284–310. DOI 10.1007/s42994-025-00209-4. [Undermind] 提及 1986 年 863 计划、2008 年转基因重大专项、2022 年生物育种国家科技重大专项。
100. Xiao, Z., Kerr, W.A. 2022. Biotechnology in China – regulation, investment, and delayed commercialization. *GM Crops & Food*, 13(1): 86–96. DOI 10.1080/21645698.2022.2068336. [Undermind]
101. Xiao, Z., Kerr, W.A. 2022. The political economy of China's GMO commercialization dilemma. *Food and Energy Security*, 11(3): e409. DOI 10.1002/fes3.409. [SG/Undermind; 估 1–2 区]
102. Kang, Y., Deng, H., Pray, C., Hu, R. 2022. Managers' attitudes toward gene-editing technology and companies' R&D investment in gene-editing: the case of Chinese seed companies. *GM Crops & Food*, 13(1): 309–326. DOI 10.1080/21645698.2022.2140567. [Undermind]
103. Jin, Y., Smeets Kristkova, Z., Wesseler, J.H.H. 2025. Welfare impacts of China's regulatory change toward genome-edited crops. *Trends in Biotechnology*, 43. DOI 10.1016/j.tibtech.2025.04.010. [Undermind/PubMed; 估 1 区]
104. Yang, F., Zheng, K., Yao, Y. 2024. China's regulatory change toward genome-edited crops. *Trends in Biotechnology*. DOI 10.1016/j.tibtech.2023.12.008. [Undermind]
105. Sun, M., et al. 2024. Commercial genetically modified corn and soybean are poised following pilot planting in China. *Molecular Plant*, 17. DOI 10.1016/j.molp.2024.03.005. [Undermind; 估 1 区]
106. Zhu, J.-K. 2022. The future of gene-edited crops in China. *National Science Review*, 9. DOI 10.1093/nsr/nwac063. [Undermind]
107. Deng, H., Hu, R., Huang, J., Pray, C., Jin, Y., Li, Z. 2017. Attitudes toward GM foods, biotechnology R&D investment and lobbying activities among agribusiness firms in the food, feed, chemical and seed industries in China. *CAER*, 9(3): 385–396. DOI 10.1108/CAER-10-2016-0162. [Undermind]
108. Deng, H., et al. 2020. Determinants of firm-level lobbying and government responsiveness in agricultural biotechnology in China. *Review of Policy Research*, 37(2): 201–220. DOI 10.1111/ropr.12363. [Undermind]
109. Pray, C., Huang, J., Hu, R., Deng, H., Yang, J., Morin, X. 2018. Prospects for cultivation of genetically engineered food crops in China. *Global Food Security*, 16: 133–137. DOI 10.1016/j.gfs.2018.01.003. [Undermind; 估 1 区]
110. Li, N., Yu, X. 2019. Gaming the regulatory system for genetically modified crops in China. *Biotechnology Law Report*, 38(4): 229–236. DOI 10.1089/blr.2019.29128.nl. [Undermind]
111. Xu, S. 2025. Implications of biotechnology development for research and agriculture in China: neoliberalism, the state, and science. *Agroecology and Sustainable Food Systems*, 49(6): 858–880. DOI 10.1080/21683565.2025.2539337. [Undermind]
112. Liu, L.-J., Cao, C. 2014. Who owns the intellectual property rights to Chinese genetically modified rice? Evidence from patent portfolio analysis. *Biotechnology Law Report*, 33(5): 181–192. DOI 10.1089/blr.2014.9971. [Undermind]
113. Hou, Y. 2019. Protecting new plant varieties in China and its major problems. In: *Innovation, Economic Development, and Intellectual Property in India and China*. DOI 10.1007/978-981-13-8102-7_14. [Undermind]
114. Spielman, D.J., Ward, P.S., Kolady, D.E., Ar-Rashid, H. 2016. Public incentives, private investment, and outlooks for hybrid rice in Bangladesh and India. *Applied Economic Perspectives and Policy*, 39(1): 154–176. DOI 10.1093/aepp/ppw001. [SG]
115. 案例：最高人民法院"黄华占"水稻品种侵权案（Case No. Zui Gao Fa Zhi Min Zhong …）. 2023. *IIC – International Review of Intellectual Property and Competition Law*. [Consensus] 

---

## 4. 跨国并购与国有种业整合、企业集中度

### 4.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 4.1 | 中化/中国化工、隆平高科等国企全球扩张正在改变全球粮食供应链；中国当前全球影响"有限，主要影响南美玉米种子市场"，但持续国际合作意味着长期影响潜力 | Deng, Yu, Jin, Pray, Liu & Deng 2025, *European Review of Agricultural Economics*, DOI 10.1093/erae/jbaf017 | 2025-07-02 | Undermind | 高 |
| 4.2 | 中国化工 2016 年 2 月报价 430 亿美元收购先正达（一说总成本 440 亿美元，2017 年完成）；主要动机是获得可持续的技术创新能力与国际监管话语权（如全球登记证） | Li C. 2025, *Journal of Innovation and Development*, DOI 10.54097/6wc57v73；ICS 2017 https://www.icsin.org/publications/acquisition-of-syngenta-by-chemchina-implications-and-lessons-for-india | 2025 / 2017 | Consensus/WebSearch | 中 |
| 4.3 | 2015–2017 年全球农化"六巨头"垄断 70% 农药与 50% 种子市场；2020 年"四巨头"（Bayer、BASF、Corteva、Sinochem）约占全球种子销售 51%、农化 62%（ETC Group 2022）；2021 年中化与中国化工合并形成全球第三大种企（以先正达运营） | Li C. 2025; Gliessman 2023, *Agroecology and Sustainable Food Systems* 47(5): 643–645, DOI 10.1080/21683565.2023.2182526 | 2025 / 2023 | Consensus | 中 |
| 4.4 | OECD 数据：种子市场集中度因作物与国家差异大，**没有系统性证据表明集中对价格或创新有害** | Deconinck 2019, *Global Food Security* 23: 135–138, DOI 10.1016/j.gfs.2019.05.001; Deconinck 2020, *Annual Review of Resource Economics* 12: 129–147, DOI 10.1146/annurev-resource-102319-100751 | 2019 / 2020 | Consensus/Undermind | 高 |
| 4.5 | 2006–2013 年国际种业市场被前 4 名种业集团寡头垄断（约占国际市场 1/2）；国内上市种企对国内种业市场占有率（CR、HHI）"相当低，年均占有率之和不到 10%" | 黄毅, 柳思维 2015. 国际种业垄断：理论解释、实证测算及趋势, pp. 79–91 | 2015 | Undermind deep search | 高（摘要） |
| 4.6 | 中国对国内种业进行并购控制（反垄断审查）有专门法律评述 | Emch & Xie 2020, Chinese Merger Control in the Agriculture Sector | 2020 | Undermind | 低（仅标题） |
| 4.7 | 巴基斯坦、塔吉克斯坦：中国种企杂交种正替代本地常规种，带来风险与利润/控制权集中——"种子体制新自由主义化"的一部分 | Spies 2025, *Journal of Peasant Studies* 52(5): 1295–1322, DOI 10.1080/03066150.2025.2462762 | 2025-03 | Undermind | 高 |
| 4.8 | 中国国内粮食种子市场结构与高度集中的全球市场不同；解释因素：党国的自力更生理念、通过法律限制外资种企的国内控制、对美国粮食体制的历史自主性 | Gaudreau 2019（博士论文） | 2019 | Undermind deep search | 高（摘要） |
| 4.9 | 全球 9 家最大种企 2008–2015 年 DEA：总体技术效率仅上升 0.8%；企业规模与效率无实质关系 | Smart, Ait Sidhoum & Sauer 2021, *Managerial and Decision Economics* 43(6): 2133–2147, DOI 10.1002/mde.3514 | 2021 | SG | 高 |

### 4.2 文献条目

116. Deng, H., Yu, C., Jin, Y., Pray, C., Liu, C., Deng, L. 2025. How is China shaping global food supply chains? Insights from the seed industry. *European Review of Agricultural Economics*. DOI 10.1093/erae/jbaf017. [Undermind; 估 1 区] **核心文献**。
117. Deconinck, K. 2020. Concentration in seed and biotech markets: Extent, causes, and impacts. *Annual Review of Resource Economics*, 12: 129–147. DOI 10.1146/annurev-resource-102319-100751. [Consensus/Undermind]
118. Deconinck, K. 2019. New evidence on concentration in seed markets. *Global Food Security*, 23: 135–138. DOI 10.1016/j.gfs.2019.05.001. [Consensus/Undermind]
119. Clapp, J. 2021. The problem with growing corporate concentration and power in the global food system. *Nature Food*, 2: 404–408. DOI 未确认（https://consensus.app/papers/details/ab35eaece7c55364b5946c64f5db1ae7/）. [Consensus; 估 1 区]
120. Bonny, S. 2017. Corporate concentration and technological change in the global seed industry. *Sustainability*, 9(9): 1632. DOI 未确认. [Consensus]
121. Lianos, I., Katalevsky, D., Ivanov, A. 2016. The global seed market, competition law and intellectual property rights: untying the Gordian knot. SSRN. DOI 10.2139/ssrn.2773422. [Consensus/Undermind]
122. Li, C. 2025. The motivations and performance of China National Chemical Corporation's multinational acquisition of Syngenta. *Journal of Innovation and Development*. DOI 10.54097/6wc57v73. [Consensus/Undermind; 非核心]
123. Gaudreau, M. 2019. Constructing China's national food security: Power, grain seed markets, and the global political economy. PhD thesis. https://www.semanticscholar.org/paper/b670f9ba63110edd5b07f2c0ae5973298a800750 [Undermind]
124. 黄毅, 柳思维. 2015. 国际种业垄断：理论解释、实证测算及趋势. pp. 79–91. https://www.semanticscholar.org/paper/13afe1d91d2e82f3c0efc32a7c542b2fbb0743a3 [Undermind]
125. Gliessman, S. 2023. The stories of seed sovereignty. *Agroecology and Sustainable Food Systems*, 47(5): 643–645. DOI 10.1080/21683565.2023.2182526. [Consensus]
126. Spies, M. 2025. Local seed systems and Global China: the spread of Chinese hybrid seeds in Pakistan and Tajikistan. *Journal of Peasant Studies*, 52(5): 1295–1322. DOI 10.1080/03066150.2025.2462762. [Undermind; 估 1 区]
127. Anderson, B.C., Sheldon, I.M. 2017. R&D concentration under endogenous fixed costs: Evidence from genetically modified corn seed. *AJAE*, 99(5): 1265–1286. DOI 10.1093/ajae/aax036. [SG]
128. Marco, A.C., Rausser, G.C. 2008. The role of patent rights in mergers: Consolidation in plant biotechnology. *AJAE*, 90(1): 133–151. DOI 10.1111/j.1467-8276.2007.01046.x. [SG]
129. Howard, P.H. 2015. Intellectual property and consolidation in the seed industry. *Crop Science*, 55(6): 2489–2495. DOI 10.2135/cropsci2014.09.0669. [SG]
130. Smart, R.D., Ait Sidhoum, A., Sauer, J. 2021. Decomposition of efficiency in the global seed industry: A nonparametric approach. *Managerial and Decision Economics*, 43(6): 2133–2147. DOI 10.1002/mde.3514. [SG]
131. Schneider, M. 2017. Dragon head enterprises and the state of agribusiness in China. *Journal of Agrarian Change*, 17(1): 3–21. DOI 10.1111/joac.12151. [Consensus/SG; 估 1–2 区]
132. Berndt, C., et al. 2025. The generics revolution and the new economic geography of the global pesticide industry. *Journal of Agrarian Change*. DOI 10.1111/joac.70007. [Undermind]
133. Moschini, G., Perry, E.D. 2026. Innovation, licensing, and competition: Evidence from genetically engineered crops. *Journal of Industrial Economics*, 74(2): 161–180. DOI 10.1111/joie.70016. [SG] 转基因性状许可与竞争的最新实证（美国）。
134. USDA ERS. 2019. Mergers in seeds and agricultural chemicals: What happened? *Amber Waves*. https://www.ers.usda.gov/amber-waves/2019/february/mergers-in-seeds-and-agricultural-chemicals-what-happened [WebSearch]
135. Emch, A., Xie, L. 2020. Chinese merger control in the agriculture sector. https://www.semanticscholar.org/paper/f568cced91cddea44d6c5df493843549cbb65f2f [Undermind]

---

## 5. 品种采纳、农户品种选择、杂交稻面积下降的经济解释

### 5.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 5.1 | 杂交稻较常规稻增产约 10%，但 1995 年以来中国杂交稻种植面积**下降 25%（约 500 万公顷）**；下降既由技术因素也由社会经济因素造成；面积下降并未对提高单产造成额外压力 | Huang M. 2022, *Food Security* 14(1): 267–272, DOI 10.1007/s12571-021-01199-z, https://link.springer.com/article/10.1007/s12571-021-01199-z | 2021-08（在线）/2022 | Consensus/WebSearch/Undermind | 高 |
| 5.2 | 超级杂交稻面积不足全国水稻面积 8%；杂交稻面积自 1996 年持续下降；原因是由人工移栽转向直播与机插——用种量上升、杂种优势形态学优势（穗型）削弱，农户转向更便宜的常规稻；缩短秧龄期/生育期也损失产量 | Huang & Zou 2018, *Field Crops Research* 224: 22–27, DOI 10.1016/j.fcr.2018.05.001 | 2018 | Consensus/Undermind | 高 |
| 5.3 | 转型时期杂交稻困境：育种策略与种子生产经营方式未适应转型期生产特点，加之优质、稳产常规稻品种的压力，杂交稻推广面积在局部地区下降 | 彭少兵 2016. 转型时期杂交水稻的困境与出路. *作物学报* 42(3): 313–319, DOI 10.3724/SP.J.1006.2016.00313, https://zwxb.chinacrops.org/article/2016/0496-3490-42-3-313.html | 2016 | WebSearch/Undermind | 高 |
| 5.4 | 南方四省地块—农户数据（ESR）：杂交稻约占中国稻作面积 28%；同一杂交稻地块上采用者产量高 4.86%，常规稻地块若改种杂交稻产量+4.72%；但杂交稻采用者**净收入低 43.61%**，常规稻地块改种杂交稻净收入 −10.95%——高种子成本、管理与品质问题 | Yan et al. 2022, *Front. Sustain. Food Syst.* 6: 1066657, DOI 10.3389/fsufs.2022.1066657 | 2022 | Consensus/Undermind | 高 |
| 5.5 | 1984–2011 省级数据 GTWR：杂交稻采用对稻谷生产的效应随时间递减；湖南对其他省份存在溢出/挤出效应 | Wang, Bin & Wang 2023, *Front. Sustain. Food Syst.* 7: 1071234, DOI 10.3389/fsufs.2023.1071234 | 2023-05 | Consensus/Undermind | 高 |
| 5.6 | 2024/25 年度中国杂交水稻制种面积 12.8 万公顷，同比下降 11%；常规水稻种子产量 138 万吨，较 2023/24 上升约 7% | 前瞻产业研究院（新浪财经转载）https://finance.sina.com.cn/roll/2026-03-23/doc-inhrynru2402679.shtml | 2026-03-23 | WebSearch: "杂交稻面积下降 原因 常规稻" | 中（行业报告） |
| 5.7 | 湖南水稻研究所：1998–2013 年双季稻经济产量仅提升 5%，一季稻提升 20%（农民不愿种双季稻的根本原因） | 人民网 2015 http://politics.people.com.cn/n/2015/0929/c1001-27645292.html | 2015-09-29 | 同上 | 中 |
| 5.8 | 广东 1990–2020 年审定的 982 个水稻品种：杂交稻产量 6.98 t/hm² > 常规稻 6.50 t/hm²；常规稻在整精米率、垩白上优于杂交稻 | Yang H. et al. 2025, *Frontiers in Agronomy* | 2025 | Consensus | 高 |
| 5.9 | 2010 年审定的籼型超级常规稻"金农丝苗"比 1978 年"桂朝 2 号"增产 18%，比超级杂交稻"Y 两优 900"低 6% | Tao Z. et al. 2022, *Agronomy* | 2022 | Consensus | 高 |
| 5.10 | 834 户玉米农户 CVM：农户愿为认证玉米种支付 **31.78%** 溢价；仅 12.71% 的受访农户熟悉认证种子 | Miao et al. 2026, *Agribusiness*, DOI 10.1002/agr.70065, https://onlinelibrary.wiley.com/doi/10.1002/agr.70065 | 2026 | SG/WebSearch | 高 |
| 5.11 | 玉米主产四省农户：新品种采用主因是期望更高产量，信息缺乏者的首要动机是降低生产风险 | Qiu, Wang, Zhang & Xu 2016, *JIA* 15(8): 1915–1923, DOI 10.1016/S2095-3119(15)61326-0 | 2016-08 | Undermind | 高 |
| 5.12 | 640 户玉米农户 4 年面板：预期坏天气时农户减少新品种、增加老品种面积（缺乏新品种耐候性信息），以产量潜力换取风险降低 | Bai, Xu, Qiu & Liu 2015, *AJARE* 59(2): 242–257, DOI 10.1111/1467-8489.12056 | 2015 | Undermind | 高 |
| 5.13 | 四川 402 户：稻谷产量与销路、农技员推广、亲友购种行为正向影响新品种采用；种子公司推荐影响方向不定 | Li, Liu & Deng 2010, *CAER* 2(4): 456–471, DOI 10.1108/17561371011097759 | 2010 | Undermind | 高 |
| 5.14 | 江西 660 户职业粮农（TAM-TPB）：感知行为控制对种植优质稻意愿影响最大，其次感知有用性 | Zhang B. et al. 2025, *Frontiers in Nutrition* 12: 1535720, DOI 10.3389/fnut.2025.1535720 | 2025-07 | Undermind | 高 |
| 5.15 | 2004 年起最低收购价等稻谷支持政策显著提高早/晚籼稻面积（DID） | Jin, Gardebroek & Heerink 2024, *Food Security* 16: 705–719, DOI 10.1007/s12571-024-01447-y | 2024-04 | Undermind | 高 |
| 5.16 | 粮食最低收购价政策抬高市场价、削弱市场定价机制并阻碍价格空间传导（时变 DID + STR） | Tan et al. 2024, *CAER*, DOI 10.1108/caer-06-2023-0159 | 2024-04 | Undermind | 高 |

### 5.2 文献条目

136. Huang, M. 2022. The decreasing area of hybrid rice production in China: causes and potential effects on Chinese rice self-sufficiency. *Food Security*, 14(1): 267–272. DOI 10.1007/s12571-021-01199-z. [Consensus/WebSearch/Undermind; 估 1 区] **核心文献**。
137. Huang, M., Zou, Y. 2018. Integrating mechanization with agronomy and breeding to ensure food security in China. *Field Crops Research*, 224: 22–27. DOI 10.1016/j.fcr.2018.05.001. [Consensus/Undermind; 估 1 区]
138. 彭少兵. 2016. 转型时期杂交水稻的困境与出路. *作物学报*, 42(3): 313–319. DOI 10.3724/SP.J.1006.2016.00313. [WebSearch/Undermind; 中文核心/CSCD]
139. Yan, Z., et al. 2022. An economic assessment of adoption of hybrid rice: Micro-level evidence from southern China. *Frontiers in Sustainable Food Systems*, 6: 1066657. DOI 10.3389/fsufs.2022.1066657. [Consensus/Undermind]
140. Wang, Q., Bin, B., Wang, H. 2023. Dynamic diffusion of hybrid rice varieties and the effect on rice production: evidence from China. *Frontiers in Sustainable Food Systems*, 7: 1071234. DOI 10.3389/fsufs.2023.1071234. [Consensus/Undermind]
141. Lin, J.Y. 1991. The household responsibility system reform and the adoption of hybrid rice in China. *Journal of Development Economics*, 36(2): 353–372. DOI 10.1016/0304-3878(91)90041-S. [Undermind; 估 1 区]
142. Lin, J.Y. 1994. Impact of hybrid rice on input demand and productivity. *Agricultural Economics*, 10(2): 153–164. DOI 10.1016/0169-5150(94)90004-3. [SG/Undermind]
143. Tao, Z., et al. 2022. Changes in grain yield and yield attributes due to cultivar development in indica inbred rice in China. *Agronomy*. DOI 未确认（https://consensus.app/papers/details/763e7d905b835a3babf615db431b33a4/）. [Consensus]
144. Yang, H., et al. 2025. Temporal changes in grain yield and quality of rice varieties released in Guangdong Province, China (1990–2020). *Frontiers in Agronomy*. DOI 未确认（https://consensus.app/papers/details/98b74415a4745f67a7042432fc3fd85c/）. [Consensus]
145. Qiu, H., Wang, X., Zhang, C., Xu, Z. 2016. Farmers' seed choice behaviors under asymmetrical information: Evidence from maize farming in China. *Journal of Integrative Agriculture*, 15(8): 1915–1923. DOI 10.1016/S2095-3119(15)61326-0. [Undermind; 估 1 区]
146. Li, D., Liu, M., Deng, G. 2010. Willingness and determinants of farmers' adoption of new rice varieties. *China Agricultural Economic Review*, 2(4): 456–471. DOI 10.1108/17561371011097759. [Undermind]
147. Bai, J., Xu, Z., Qiu, H., Liu, H. 2015. Optimising seed portfolios to cope ex ante with risks from bad weather: evidence from a recent maize farmer survey in China. *AJARE*, 59(2): 242–257. DOI 10.1111/1467-8489.12056. [Undermind; 估 2 区]
148. Miao, B., Liu, Y., Chen, H., Zhang, R., Zhu, W., Huang, Y., Hu, X. 2026. Farmers' willingness to pay a premium for certified maize seeds in China. *Agribusiness* (early view). DOI 10.1002/agr.70065. [SG/WebSearch]
149. Zhang, B., Cai, Y., Hu, Z., Xie, N., Li, J. 2025. Research on farmers' willingness to grow high-quality rice based on the TAM-TPB model: evidence from China. *Frontiers in Nutrition*, 12: 1535720. DOI 10.3389/fnut.2025.1535720. [Undermind]
150. Liu, E.M. 2013. Time to change what to sow: Risk preferences and technology adoption decisions of cotton farmers in China. *Review of Economics and Statistics*, 95(4): 1386–1403. DOI 10.1162/REST_a_00295. [Undermind; 估 1 区]
151. Smale, M., et al. 2003. Determinants of spatial diversity in modern wheat: examples from Australia and China. *Agricultural Economics*, 28(1): 13–26. DOI 10.1111/j.1574-0862.2003.tb00131.x. [Undermind]
152. Nguyen Chau, T., Scrimgeour, F. 2021. Productivity impacts of hybrid rice seeds in Vietnam. *Journal of Agricultural Economics*, 73(2): 414–429. DOI 10.1111/1477-9552.12458. [SG/Consensus] 杂交稻对高产常规稻无生产率优势；技术效率缺口 35%。
153. Mottaleb, K.A., Mohanty, S., Nelson, A. 2014. Factors influencing hybrid rice adoption: a Bangladesh case. *AJARE*, 59(2): 258–274. DOI 10.1111/1467-8489.12060. [SG/Consensus]
154. Jin, Y., Gardebroek, C., Heerink, N. 2024. The impact of Chinese rice support policies on rice acreages. *Food Security*, 16: 705–719. DOI 10.1007/s12571-024-01447-y. [Undermind]
155. Tan, Y., Yue, R., Chen, L., Li, C., Chen, K. 2024. Grain price support policy and the distortion of market price. *China Agricultural Economic Review*. DOI 10.1108/caer-06-2023-0159. [Undermind]
156. Zheng, X., Liu, W., Xu, Z., Ying, R., Ye, C. 2018. Restructuring grain production in China: regional heterogeneity and its causality. *China Agricultural Economic Review*, 10(4). DOI 10.1108/CAER-01-2017-0008. [Undermind]
157. Ito, J., Li, X. 2023. Interplay between China's grain self-sufficiency policy shifts and interregional, intertemporal productivity differences. *Food Policy*, 117: 102446. DOI 10.1016/j.foodpol.2023.102446. [Undermind; 估 1 区；摘要不可得]
158. 前瞻产业研究院. 2026. 2025 年中国水稻种子行业发展情况分析：杂交水稻种子产量下降. 新浪财经 https://finance.sina.com.cn/roll/2026-03-23/doc-inhrynru2402679.shtml [WebSearch]
159. 农小蜂. 2024. 2024 年中国水稻种子数据分析报告. https://www.abeedata.com/home/data/productdetail/id/481.html [WebSearch; 仅标题]

---

## 6. 创新系统 / 产业链视角的农业技术扩散模型

### 6.1 关键事实与文献条目（合并）

160. Zilberman, D., Lu, L., Reardon, T. 2017. Innovation-induced food supply chain design. *Food Policy*, 83: 289–297. DOI 10.1016/j.foodpol.2017.03.010. [Undermind; 估 1 区] 创新者选择供应链设计（自建/合同/市场）以推广新产品/技术——与"种企主导链"直接对应。（置信度：中，仅题录）
161. Zilberman, D., et al. 2022. From the laboratory to the consumer: Innovation, supply chain, and adoption with applications to natural resources. *PNAS*, 119(23): e2115880119. DOI 10.1073/pnas.2115880119. [Undermind; 估 1 区]
162. Reardon, T., et al. 2019. Rapid transformation of food systems in developing regions: Highlighting the role of agricultural research & innovations. *Agricultural Systems*, 172: 47–59. DOI 10.1016/j.agsy.2018.01.022. [Undermind; 估 1 区]
163. Kuijpers, R., Swinnen, J. 2016. Value chains and technology transfer to agriculture in developing and emerging economies. *AJAE*, 98(5): 1403–1418. DOI 10.1093/ajae/aaw069. [SG; 估 1 区] 价值链作为技术转移渠道的理论模型。
164. Devaux, A., Torero, M., Donovan, J., Horton, D. 2018. Agricultural innovation and inclusive value-chain development: a review. *Journal of Agribusiness in Developing and Emerging Economies*, 8(1): 99–123. DOI 10.1108/JADEE-06-2017-0065. [Undermind]
165. Spielman, D.J. 2005. Innovation systems perspectives on developing-country agriculture: A critical review. ISNAR Discussion Paper 2. DOI 10.22004/ag.econ.59692. [Undermind]
166. Klerkx, L., Gildemacher, P. 2012. The role of innovation brokers in agricultural innovation systems. In: *Agricultural Innovation Systems: An Investment Sourcebook*, World Bank. [Undermind; 仅题录]
167. Anandajayasekeram, P., Gebremedhin, B. 2009. Integrating innovation systems perspective and value chain analysis in agricultural research for development. ILRI. [Undermind]
168. Khed, V.D., Jaleta, M., Krishna, V.V. 2024. Wheat seed delivery pathways and varietal turnover in eastern India. *Agribusiness*, 42(3): 1145–1173. DOI 10.1002/agr.21971. [SG/Undermind] 7648 户；品种选择先于种子来源选择（双向因果，IV）。（置信度：高）
169. Kala-Satheesh, H.K., et al. 2024. Seed market dynamics and diffusion of new wheat varieties in Bihar, India: a supply-side perspective. *Agricultural and Food Economics*, 12. DOI 10.1186/s40100-024-00330-w. [Undermind] 200 家私营种子经销商；品种丰富度与销量正相关。
170. Rutsaert, P., Donovan, J. 2020. Sticking with the old seed: Input value chains and the challenges to deliver genetic gains to smallholder maize farmers. *Outlook on Agriculture*, 49(1): 39–49. DOI 10.1177/0030727019900520. [Undermind]
171. Jin, S., Bluemling, B., Mol, A.P.J. 2015. Information, trust and pesticide overuse: Interactions between retailers and cotton farmers in China. *NJAS – Wageningen Journal of Life Sciences*, 72–73: 23–32. DOI 10.1016/j.njas.2014.10.003. [Undermind] 农资零售商作为信息源。
172. Wang, H., Chen, B., Huang, Z. 2026. Agricultural technology extension reform and productivity growth: Evidence from rural China. *Journal of Rural Studies*. DOI 10.1016/j.jrurstud.2026.104064. [Undermind; 摘要不可得]
173. Liverpool-Tasie, L.S.O., et al. 2025. Private sector promotion of agricultural technologies: Experimental evidence from Nigeria. *Journal of Environmental Economics and Management*. DOI 10.1016/j.jeem.2025.103201. [Undermind]
174. Mulungu, K., et al. 2026. Small seed packs, big potential? Effect of seed packs on knowledge and adoption of improved crop varieties. *Journal of Agricultural Economics*, 77(2): 750–770. DOI 10.1111/1477-9552.70040. [SG/Undermind]
175. Arora, A., Bansal, S. 2012. Diffusion of Bt cotton in India: Impact of seed prices and varietal approval. *Applied Economic Perspectives and Policy*, 34(1): 102–118. DOI 10.1093/aepp/ppr038. [Undermind] 品种审定与种价对扩散的影响（可迁移方法）。
176. Qian, J., Zhao, Z. 2017. Estimating the contribution of new seed cultivars to increases in crop yields: A case study for corn. *Sustainability*, 9(7): 1282. DOI 10.3390/su9071282. [Undermind]
177. Alene, A.D., Manyong, V.M. 2007. Farmer-to-farmer technology diffusion and yield variation among adopters: the case of improved cowpea in northern Nigeria. *Agricultural Economics*, 35(2): 203–211. DOI 10.1111/j.1574-0862.2006.00153.x. [SG]
178. Chen, C., et al. 2024（见条目 13）— 中国农业创新体系治理视角的小农现代化。

---

## 7. 中国种业企业 R&D 强度与绩效的实证

### 7.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 7.1 | 中国上市种企 2013–2022 面板（滞后回归）：R&D 强度与专利对当期 ROE 显著负向；R&D 强度滞后两期对 ROE 显著正向；专利滞后三期正向不显著；供应链集中度弱化 R&D 强度的短期负效应 | Zhang, Talib & Ahmad 2025, *Edelweiss Applied Science and Technology* 9(3), DOI 10.55214/25768484.v9i3.5179 | 2025 | Consensus/Undermind | 高（摘要；期刊非核心） |
| 7.2 | 49 家上市种企 2015–2022（GPCA + Q 型聚类）：整体竞争力上升；前十强在运营与技术创新能力上有优势但成长性与生产效率不足；竞争力排序：小麦种企 > 其他 > 瓜菜 > 玉米 > 水稻种企；与国际巨头差距在研发投入、规模与市场份额、产业布局 | Li, Zhang & Wang 2024, *Agriculture* 14(8): 1213, DOI 10.3390/agriculture14081213 | 2024-07 | Consensus/Undermind | 高 |
| 7.3 | 2019–2023 上市种企 DEA-fsQCA：创新效率整体有较大提升空间；技术研发阶段效率高于成果转化阶段；创新能力提升需多条件组合（人才/管理/规模/政府协作） | Mo et al. 2025, *Heliyon* 11: e42914, DOI 10.1016/j.heliyon.2025.e42914 | 2025-02 | Consensus/PubMed | 高 |
| 7.4 | 19 家上市种企三阶段 DEA：剔除环境因素后 R&D 效率与规模效率显著下降，63% 企业处于规模报酬递增 | Yan L. 2020, *J. Phys.: Conf. Ser.* 1549: 042040, DOI 10.1088/1742-6596/1549/4/042040 | 2020 | Consensus/Undermind | 高（非核心） |
| 7.5 | 101 家中国农业上市公司 2012–2019（Tobit）：多元化与技术创新效率呈 U 型关系；R&D 投资年均增长率 10.04% | Su, Zhang, Sun & Wu 2022, *Agribusiness* 39(2): 322–346, DOI 10.1002/agr.21785 | 2022 | SG | 高 |
| 7.6 | 上市种企财务支持效率（能耗与碳排视角，三阶段 DEA-Tobit） | ESPR 2023, DOI 10.1007/s11356-023-26303-y | 2023-03 | PubMed | 中（仅摘要） |
| 7.7 | 2012–2021 省级面板：种业创新促进粮食绿色 TFP（绿色技术进步与效率均正向）；资源错配负向调节 | Gong et al. 2023, *Journal of Cleaner Production* | 2023 | Consensus | 中 |
| 7.8 | 31 省 2013–2023 粮食作物育种技术创新（创新链四阶段、熵权/Dagum/Markov）：主销区高于主产区与产销平衡区；区域差异显著但缩小 | Shen & Cui 2026, *Scientific Reports* | 2026 | Consensus | 中 |
| 7.9 | 中国农业上市公司 R&D 强度对短期盈利负向、对长期企业价值正向（385 家民企 1540 观测） | Leung et al. 2021, *Journal of Business Research* | 2021 | Consensus | 中（非种业） |

### 7.2 文献条目

179. Mo, M., et al. 2025. Analysis of technology innovation efficiency and its impact factors based on DEA-fsQCA method: Evidence from listed seed companies in China. *Heliyon*, 11: e42914. DOI 10.1016/j.heliyon.2025.e42914. [Consensus/PubMed; 估 3 区]
180. Li, L., Zhang, L., Wang, X. 2024. Research on the dynamic evaluation of the competitiveness of listed seed enterprises in China. *Agriculture*, 14(8): 1213. DOI 10.3390/agriculture14081213. [Consensus/Undermind]
181. Zhang, N., Talib, Z., Ahmad, M. 2025. Impact of technological innovation on the performance of Chinese listed seed companies: The moderating role of supply chain concentration. *Edelweiss Applied Science and Technology*, 9(3). DOI 10.55214/25768484.v9i3.5179. [Consensus/Undermind; 非核心]
182. Zhang, N., Ahmad, M., Talib, Z. 2024. The impact of technological innovation policy on the performance of Chinese listed seed companies: The mediator role of R&D investment. *Pakistan Journal of Life and Social Sciences*. [Consensus; 非核心]
183. Yan, L. 2020. Research on R&D efficiency evaluation of Chinese seed industry listed companies based on three-stage DEA model. *Journal of Physics: Conference Series*, 1549: 042040. DOI 10.1088/1742-6596/1549/4/042040. [Consensus/Undermind]
184. Su, Z., Zhang, M., Sun, J., Wu, W. 2022. Agribusiness diversification and technological innovation efficiency: A U-shaped relationship. *Agribusiness*, 39(2): 322–346. DOI 10.1002/agr.21785. [SG]
185. Gong, S., et al. 2023. Does seed industry innovation in developing countries contribute to sustainable development of grain green production? Evidence from China. *Journal of Cleaner Production*. DOI 未确认（https://consensus.app/papers/details/cddd55f1b71953af8b736d0ae108c25c/）. [Consensus; 估 1 区]
186. Shen, J., Cui, B. 2026. Measurement, regional disparities, and dynamic evolution of food crop breeding technology innovation in China. *Scientific Reports*. DOI 未确认（https://consensus.app/papers/details/86e20f23ff695e60be1511fd81a711be/）. [Consensus]
187. Xiong, et al. 2023. Analysis of financial support efficiency and influencing factors of listed seed companies from the perspective of energy consumption and carbon emissions. *Environmental Science and Pollution Research*. DOI 10.1007/s11356-023-26303-y. [PubMed; 作者待核]
188. Leung, T.Y., et al. 2021. Differences in the impact of R&D intensity and R&D internationalization on firm performance – Mediating role of innovation performance. *Journal of Business Research*. [Consensus; 非种业对照]
189. 陈燕娟 (Chen, Y.-J.). 2011. Intellectual property protection and strategies to enhance international competitiveness of China seed industry. *农业现代化研究*. [Undermind]
190. Fei, J. 2010. Seed market structure and agricultural production performance: A case study on major regional corn seed markets in China. *南京农业大学学报*. [Undermind]; Li, T. 2010. Empirical studies on the impact of variety rights protection on concentration ratio of China's seed industry. *南京农业大学学报*. [Undermind]

---

## 8. 农业龙头企业带动小农的效应（CAER、Food Policy、WD、JIA、JRS、Agricultural Systems 等）

### 8.1 关键事实

| # | 事实 | 来源 | 发布日期 | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 8.1 | 龙头企业是国家—私人精英共同打造的国内农业综合企业部门，兼具国家—私人混合形式，倾向边缘化外资跨国公司（生猪部门） | Schneider 2017, *JAC* 17(1): 3–21, DOI 10.1111/joac.12151 | 2016/2017 | Consensus/SG | 高 |
| 8.2 | "龙头企业+小农"传统契约不完全、难避机会主义；"龙头企业+合作社+小农"提高紧密性与稳定性；"企业一体化"为价值链高级阶段，价值链最终趋向企业一体化（博弈模型） | Jin Q. et al. 2024, *Agriculture* 14(3): 437, DOI 10.3390/agriculture14030437 | 2024 | Consensus/Undermind | 高 |
| 8.3 | 11 省 1194 户（2019）联立方程：农业价值链通过促进土地转入、增加生产性投资、降低非农就业比重提高农户收入 | Jin Q. et al. 2025, *Food and Energy Security* | 2025 | Consensus | 中 |
| 8.4 | 山东、陕西 355 户苹果农：龙头企业对产量与利润无显著影响（合作社有）；不提供更高价格 | Moustier 2018 | 2018 | Consensus/Undermind | 中 |
| 8.5 | 全球综述：农企"包容性商业"总体趋向更排他（政府削减支农、标准提高、企业精简） | German et al. 2020, *World Development* 134 | 2020 | Consensus | 中 |
| 8.6 | 长三角鲜食葡萄：龙头企业可促进农户纵向协作，fsQCA 识别 4 条路径、3 类组态（风险规避型、资源约束型、负担减轻型） | Li W. et al. 2023, *Agriculture* 13(10): 1915, DOI 10.3390/agriculture13101915 | 2023-09 | Undermind | 高 |
| 8.7 | 长三角龙头企业引导农户参与产前质量安全控制：村企合作、三产融合、机械化、数字化、农技推广五种行为组态；三类驱动（产业融合、数智、土地托管） | Liu C. et al. 2025, *FSFS* 9: 1615223, DOI 10.3389/fsufs.2025.1615223 | 2025-07 | Undermind | 高 |
| 8.8 | 肉鸡"公司+农户"：合同类型与农户风险偏好共同影响技术采用（*China Economic Review*）；不同规模肉鸡户对合同形式偏好不同（"one size fits all?"，*JIA*） | Mao et al. 2019, DOI 10.1016/j.chieco.2018.10.014; Huang Z. et al. 2018, *JIA* 17(2): 473–482, DOI 10.1016/S2095-3119(17)61752-0 | 2019 / 2018 | Undermind | 中（题录） |
| 8.9 | 农业产业化联合体是中国农村纵向产业融合的高级形态，其纵向一体化组织边界源于中间品市场的产品定价与交易成本（安徽案例） | 王志刚, 于滨铜 2019. 农业产业化联合体概念内涵、组织边界与增效机制：安徽案例举证. *中国农村经济* 2019(2). https://zgncjj.ajcass.com/UploadFile/Issue/jgdkj4tg.pdf | 2019-02 | WebSearch: "种粮一体化 OR 订单粮食 纵向一体化 中国农村经济" | 高（期刊 PDF） |
| 8.10 | 农民合作社通过内部横向一体化替代外部纵向一体化，降低外部化服务不确定性与交易费用；参与合作社显著提升种粮效益（10 省数据） | 西南大学学报（自然科学版）2024, 46(10), DOI 10.13718/j.cnki.xdzk.2024.10.010 | 2024-10 | 同上 | 中 |

### 8.2 文献条目

191. Jin, Q., et al. 2024. Exploring cooperative mechanisms in the Chinese agricultural value chain: A game model analysis based on leading enterprises and small farmers. *Agriculture*, 14(3): 437. DOI 10.3390/agriculture14030437. [Consensus/Undermind]
192. Jin, Q., et al. 2025. Unlocking rural prosperity: How agricultural value chains drive farmer income growth in China. *Food and Energy Security*. DOI 未确认（https://consensus.app/papers/details/965f429f909959c1aa0b038042207d19/）. [Consensus]
193. Moustier, P. 2018. Are dragon-head companies heading agricultural development in China? The case of apple chains. https://www.semanticscholar.org/paper/179158d10e1da3bb1287963f808d2b3ae3c41a6b [Consensus/Undermind]
194. German, L., et al. 2020. "Inclusive business" in agriculture: Evidence from the evolution of agricultural value chains. *World Development*, 134: 105018. DOI 未确认. [Consensus]
195. Li, W., et al. 2023. Factors influencing farmers' vertical collaboration in the agri-chain guided by leading enterprises: A study of the table grape industry in China. *Agriculture*, 13(10): 1915. DOI 10.3390/agriculture13101915. [Undermind]
196. Liu, C., Li, W., You, Y., Yang, Q., Li, M. 2025. Research on leading agricultural enterprises guiding farmers' participation in pre-production quality and safety control: evidence from the Yangtze River Delta Region of China. *Frontiers in Sustainable Food Systems*, 9: 1615223. DOI 10.3389/fsufs.2025.1615223. [Undermind]
197. Mao, H., et al. 2019. Risk preferences, production contracts and technology adoption by broiler farmers in China. *China Economic Review*, 54. DOI 10.1016/j.chieco.2018.10.014. [Undermind; 估 1 区]
198. Huang, Z., et al. 2018. One size fits all? Contract farming among broiler producers in China. *Journal of Integrative Agriculture*, 17(2): 473–482. DOI 10.1016/S2095-3119(17)61752-0. [Undermind]
199. Ma, W., Abdulai, A. 2017. The economic impacts of agricultural cooperatives on smallholder farmers in rural China. *Agribusiness*, 33(4): 537–551. DOI 10.1002/agr.21522. [Undermind]
200. Hoken, H., Su, Q. 2018. Measuring the effect of agricultural cooperatives on household income: Case study of a rice-producing cooperative in China. *Agribusiness*, 34(4): 831–846. DOI 10.1002/agr.21554. [SG/Undermind]
201. Wang, J., et al. 2024. Impact of rural industrial integration on farmers' income: Evidence from agricultural counties in China. *Journal of Asian Economics*. [Consensus]
202. 王志刚, 于滨铜. 2019. 农业产业化联合体概念内涵、组织边界与增效机制：安徽案例举证. *中国农村经济*, 2019(2). https://zgncjj.ajcass.com/UploadFile/Issue/jgdkj4tg.pdf [WebSearch; CSSCI]
203. Mi, Q., Li, X., Gao, J. 2020. How to improve the welfare of smallholders through agricultural production outsourcing: Evidence from cotton farmers in Xinjiang, Northwest China. *Journal of Cleaner Production*, 120636. DOI 10.1016/j.jclepro.2020.120636. [Undermind]
204. Sun, D., Rickaille, M., Xu, Z. 2018. Determinants and impacts of outsourcing pest and disease management. *China Agricultural Economic Review*. DOI 10.1108/caer-01-2017-0011. [Undermind]

---

## 9. 期刊分区估计表（投稿前须核实）

| 期刊 | 索引 | 估计分区（中科院/JCR，"估"） |
|---|---|---|
| American Journal of Agricultural Economics; Food Policy; World Development; Journal of Rural Studies; Agricultural Systems; Journal of Development Economics; PNAS; Nature Food; Research Policy; Annual Review of Resource Economics; European Review of Agricultural Economics; Journal of Peasant Studies; Journal of Agrarian Change; Field Crops Research; Trends in Biotechnology; Molecular Plant; Global Food Security; Food Security; China Economic Review; Technological Forecasting & Social Change | SSCI/SCI | 估 1 区 / Q1 |
| China Agricultural Economic Review; Agricultural Economics; Journal of Agricultural Economics; AJARE; Agribusiness; Applied Economic Perspectives and Policy; Journal of Integrative Agriculture; Production and Operations Management; Agronomy; Agriculture (MDPI); Frontiers in Sustainable Food Systems; Frontiers in Plant Science; Review of Development Economics; Scientific Reports | SSCI/SCI | 估 2–3 区 / Q1–Q2 |
| Sustainability; Heliyon; IJERPH; GM Crops & Food; Land; JARQ; Managerial and Decision Economics; Applied Economics; Chinese Management Studies; British Food Journal | SSCI/SCI | 估 3–4 区 / Q2–Q3 |
| 中国农村经济; 农业经济问题; 农业技术经济; 作物学报; 农业现代化研究; 南京农业大学学报（社科版） | CSSCI/CSCD | 中文核心 |
| Edelweiss Applied Science and Technology; Pakistan J. Life & Social Sciences; Journal of Innovation and Development; Frontiers in Business, Economics and Management; J. Phys.: Conf. Ser. | 非核心 | 不建议作为主要支撑 |

---

## 10. 缺口（Gaps）——论文可能需要但本次未找到/未确认

1. **荃银高科/隆平高科"种粮一体化"的同行评审实证**：仅 Xie et al. (2023) 以数值算例方式引用二手财务数据（荃银订单业务毛利率 3.56%→7.6%、占比 5.87%→28.73%），无以企业年报或订单基地微观数据为基础的学术评估；需结合维度 1–6 的年报数字。
2. **2021 年《种子法》修正（EDV、惩罚性赔偿）的因果评估**：未找到任何计量评估，仅法学评述；品种同质化/"仿种子"清理效果亦无实证。
3. **品种审定改革（绿色通道 2014、联合体试验 2016）对审定品种数量"井喷"的定量研究**：仅政策文件与 Xiang et al. 提及"2017 年起审定品种数显著增加"；缺年度审定数量序列与 DID 类研究。
4. **中文核心期刊（《中国农村经济》《农业经济问题》《农业技术经济》）关于"订单粮食/种粮一体化"的近五年论文**：WebSearch 配额耗尽、CNKI 不可访问，仅找到王志刚&于滨铜 (2019) 与刘晓鸥&邸元 (2013)；需 CNKI 补检"种业企业 订单农业""种粮一体化""优质稻 订单 溢价"。
5. **杂交稻面积份额的权威年度序列（2015 年后）**：仅有 Huang (2022) 的"1995 年以来 −25%"与 Yan (2022) 的"约 28%"；需全国农技中心/国家统计数据。
6. **Xu & Cao (2025, JRS)、Li et al. (2026, Food Policy)、Jia & Huang (2011)、Guo & Jolly (2008)、Chen et al. (2024, JRS)、Ito & Li (2023)** 摘要不可得（工具限制），须下载全文核实其可引用结论。
7. **ChemChina–Syngenta 并购对中国国内种子市场（价格、创新、市场份额）的影响**：仅 Deng et al. (2025, ERAE) 从全球视角讨论，国内影响无实证。
8. **种企主导订单农业的全国规模**（面积、农户数、涉及品种）：无官方或学术统计；仅 Xie 转引 MARA 2021 的订单农业总面积与经营主体数。
9. **期刊分区**：本环境无法核实中科院分区表，所有分区均为估计。
10. **部分 Consensus 条目缺 DOI**（Clapp 2021; Bonny 2017; Gong et al. 2023; German et al. 2020; Jin et al. 2025 FES; Tao et al. 2022; Yang et al. 2025; Yu et al. 2020; Veettil et al. 2021），投稿前需补齐。

---

## 附：检索记录摘要

- WebSearch（成功 9 条）："Contract farming led by a seed enterprise… agr.21823"；"Agribusiness 10.1002/agr.22020 seed licensing fees"；"育繁推一体化 种子企业 商业化育种 实证"；"杂交稻面积下降 原因 常规稻 经济分析"；"ChemChina Syngenta acquisition seed industry concentration"；""seed industry" China "commercial breeding" CAER OR JIA"；"种粮一体化 OR 订单粮食 种业企业 纵向一体化 中国农村经济"；"品种审定制度改革 绿色通道 联合体试验"；""hybrid rice" China area decline Huang Min Food Security"。
- Consensus（成功 7 条）：contract farming seed enterprise；commercial breeding system China；PVP/EDV/Seed Law licensing；hybrid rice area decline；seed company R&D intensity；dragon head enterprises smallholder；seed industry mergers concentration。
- Scholar Gateway（12 条）：种企纵向一体化与订单；杂交稻面积下降；种业改革/PVP/审定/集中度；龙头企业与订单效应；全球种业并购与 IPR；创新系统/价值链扩散；农户品种选择；发展中国家种业政策改革；全产业链种粮一体化；转基因玉米大豆商业化与性状许可；上市种企 R&D 与绩效；制种组织与制种农户。
- Undermind（27 条 search_papers + 2 deep search）：涵盖上述全部 8 个主题及中文表述（订单农业/种粮一体化、育繁推一体化）。
- PubMed（3 条）：seed industry China policy；contract farming China；GM commercialization China（GM Crops & Food/aBIOTECH/Trends Biotech/Mol Plant/NSR）。
- Amass BiomedCore（1 条）：seed industry policy reform commercial breeding PVP。
