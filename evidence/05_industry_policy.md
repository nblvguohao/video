# 维度5：产业与政策背景 + 股权/治理变化（荃银高科 / 中种集团 / 先正达）

- 维度：05_industry_policy（A 股权/治理；B 政策；C 行业数据；D 竞争对手）
- 检索次数：约 88 次（WebSearch 42 次，其中 39 次成功、3 次因会话检索配额耗尽被拒；Scholar Gateway 9 次；Undermind 11 次；PubMed 4 次；Amass 2 次；GitHub 代码检索 14 次；Hugging Face 1 次；Consensus 3 次、Elicit 1 次、WebFetch 1 次均因配额/代理限制失败）
- 来源数：约 95 个独立 URL / 文献条目（见各条目及第 E 节）
- 更新时间：2026-09-14
- 工具约束说明：容器内 WebFetch/curl 对 cninfo、sina、moa.gov.cn、huaon 等站点均被代理拦截（已实测 000/403），只能依赖 WebSearch 摘要与学术 MCP；WebSearch 会话配额在第 42 次查询时耗尽，因此 C 节的"再生稻分省面积、CR10、前十强名单"与 D 节的"垦丰种业"等未能完成核实，已在 F 节列为缺口。
- 置信度标注：高 = 检索摘要中直接出现公告/年报/官方原文数字；中 = 搜索工具或论文的综合表述；低 = 第三方研究笔记/间接推断（GitHub 第三方研报笔记仅作线索，均已注明）。

---

## 0. 关键结论速览（供论文背景段落使用）

1. **要约收购**：中种集团（先正达集团中国种子平台）于 2025-11-20 公告部分要约，价格 11.85 元/股、拟收购 189,466,350 股（20.00%），最高资金 22.45 亿元；要约期 2025-12-04 至 2026-01-05；最终 3,763 个账户共 297,787,643 股预受（超额，按比例收购），收购完成后中种集团持有 383,760,376 股、占总股本 **40.51%**（核实无误）。
2. **同业竞争承诺**：2021-12-10 中种集团承诺 5 年内（至 2026 年 1 月前后）解决与荃银高科的同业竞争；2026-01-14 荃银高科与中种集团签署《股权委托管理协议》，受托管理**中种农科 100% 股权**（整合原中国化工系境内水稻、小麦种子业务），托管期 3 年、年托管费 60 万元——以"托管"而非"注入"方式阶段性履约。
3. **先正达注入传闻**：2025-08 起市场（雪球、东方财富财富号等）流传"先正达拟将中国种子业务注入荃银高科"，截至 2026-09 未见公司公告确认资产注入；先正达集团筹划港股 IPO（传 2026 年 6 月保密递表、9–10 月上市、估值约 500 亿美元、募资 50–100 亿美元）。
4. **治理风险事件**：2026-06-26 荃银高科收到安徽证监局《行政处罚事先告知书》，因 2024 年年报少计提信用减值损失、虚增利润总额 1,871.51 万元（占当期披露利润总额 10.86%），公司拟被罚 300 万元，应敏杰、张琴各 150 万元，张庆一 130 万元；2026-06-30 起被实施其他风险警示，简称变更为 **ST荃银**。
5. **股权入股历程**：2018-11-15 中化现代农业以 8.85 元/股、总价 8.19 亿元协议受让 21.50%（9,252.0965 万股）成为第一大股东 → 2021-01 贾桂兰、王玉林将 8.23% 表决权委托给中化现代农业（合计可支配 29.73%），公司实控人变更为国务院国资委 → 2021-12 中化现代农业将股份无偿划转至中种集团 → 2025-11-19 解除一致行动（表决权 28.36%→20.51%）→ 2026-01 要约完成后 40.51%。
6. **政策主线**：2021-07 种业振兴行动方案（五大行动）；2022-03-01 新《种子法》建立实质性派生品种（EDV）制度；2024/2025/2026 中央一号文件连续提出"生物育种产业化扩面提速→继续推进→推进生物育种产业化"，2026 年文件首次写入"加快实施实质性派生品种制度""国家种业阵型企业梯度培育"。
7. **转基因产业化**：2023-12-07 农业农村部第 732 号公告首批审定 37 个转基因玉米、14 个转基因大豆品种；2023–2024 累计审定 64 玉米+17 大豆；2025 年第 947 号公告再审定 96 玉米+2 大豆，累计 **160 个转基因玉米、19 个转基因大豆**。2024 年示范省份 8 个（吉林、内蒙古、辽宁、河北全省放开），2025 年扩至 13 个省份；2024 年种植面积报道口径 1,000 万亩与 2,000 万亩以上并存（未统一）；2025 年预测 3,100 万–5,000 万亩以上。
8. **阵型企业**：2022-08 农业农村部办公厅遴选 69 家农作物种业阵型企业（19 家水稻小麦"强优势"、32 家玉米大豆等"补短板"、18 家"破难题"）；荃银高科被认定为"强优势"阵型企业（水稻）和"补短板"阵型企业（棉花）（来源：公司年报/官网，中置信度）。
9. **杂交稻种子供需**：2024 年杂交稻制种面积 192 万亩（-24 万亩），新产种子约 3.1 亿公斤；2024/25 年度总供给 41 万吨（含结转 10 万吨）、总需求 35 万吨（含出口 3 万吨）；2025 年制种面积回升至 225.4 万亩（+17.4%）；2024、2025 年供需比分别 178%、125%，行业处于去库存、价格低迷阶段；2026 年需求预计 3.3 亿公斤。
10. **行业集中度**：CR5 由 2019 年 9.6% 升至 2023 年 19.2%（Wang & Kang 2025）；此前多篇文献称前五强份额 <10%；CR10 具体值未找到。
11. **审定"井喷"**：2000 年国内审定水稻品种 279 个、玉米 150 个，2005 年起每年约 500 个，2017 年后急升，2021 年达水稻 2,287 个、玉米 3,779 个（Xiang et al. 2025，Agribusiness）；国审稻品种 2023 年 409 个、2024 年 405 个，2024 年国审稻中优质二级以上占 57%、杂交稻占 87.9%。
12. **再生稻**：文献口径全国再生稻面积 >120 万公顷（11 省市），潜在面积 >500 万公顷（Luo et al. 2025 引 Lin et al. 2024）；湖北再生稻已达 20 万公顷（Xia et al. 2022）；2025-02-22 新闻联播：农业农村部力争到 2030 年全国再生稻面积新增约 1,000 万亩。分省 2024/2025 年官方面积未能核实（缺口）。
13. **竞争对手 2025 年**（第三方研究笔记转引年报，低–中置信度，需以年报核对）：隆平高科营收 84.77 亿元、归母净利 1.66 亿元、玉米种子收入约 50.40 亿元；登海种业营收 11.02 亿元、归母净利 9,165 万元；大北农营收 291.19 亿元、归母净利 -6.42 亿元、种业收入 15.28 亿元（玉米 8.14 亿、水稻 5.62 亿）；国投丰乐（原丰乐种业）营收 29.03 亿元、归母净利 6,602 万元；神农种业（原神农科技）营收 2.49 亿元、扣非净利 434 万元；荃银高科营收 44.95 亿元、归母净利 -2.12 亿元。垦丰种业未找到。

---

## A. 股权/治理变化

### A1. 2016 年以来入股历程（中化现代农业 → 中种集团）

| 时间 | 事件 | 关键数字 | 来源（URL / 日期） | 检索词 | 置信度 |
|---|---|---|---|---|---|
| 2016-04 | 股东中新融泽及其一致行动人因违规增持被证监会立案调查，并被荃银高科诉至法院（"股权争夺战"高潮） | — | 新京报 https://m.bjnews.com.cn/detail/154229370114207.html ；凤凰网 https://biz.ifeng.com/c/7hsPRCSxmnT | "中化现代农业 入股 荃银高科 2016 张琴 股权转让 历程" | 中 |
| 2018-11-15 | 中化现代农业有限公司与中新融泽、中新融鑫、西藏中新睿银、张琴、贾桂兰等 11 名股东签署股份转让协议，成为第一大股东（详式权益变动报告书称"战略性投资"） | 受让 9,252.0965 万股，占总股本 21.50%；8.85 元/股，总价款 8.19 亿元；张琴转让 2.26%、贾桂兰转让 1.5% | 证券日报 http://www.zqrb.cn/gscy/gongsi/2018-11-21/A1542767175374.html （2018-11-21）；凤凰网 https://biz.ifeng.com/c/7hsPRCSxmnT | "中化现代农业 2018年 协议受让 荃银高科 21.50% 8.85元 中新融泽 张琴" | 高 |
| 2021-01 | 股东贾桂兰、王玉林将所持全部股份表决权委托给中化现代农业；公司由无控股股东、无实控人变更为中化现代农业控股、国务院国资委实控 | 委托 35,405,962 股（8.23%）；现代农业可支配表决权 127,926,927 股（29.73%） | 荃银高科公告 2021-001 https://pdf.dfcfw.com/pdf/H2_AN202012311446022583_1.pdf ；福建农业农村厅转载 https://nynct.fujian.gov.cn/ztzl/xdzy/qyzc/202101/t20210114_5517719.htm （2021-01-14） | "荃银高科 2021年1月 表决权委托 贾桂兰 王玉林 中化现代农业 控股股东 持股比例" | 高 |
| 2021-12-10 | 现代农业、贾桂兰、王玉林与中种集团签署《表决权委托及一致行动协议的权利义务承继确认函》；现代农业将直接持有股份无偿划转至中种集团；中种集团在详式权益变动报告书中承诺 5 年内通过资产重组、业务调整、委托管理、设立合资公司等解决同业竞争 | 承诺期限至 2026 年 1 月前后（另一表述"剩余期限至 2026 年 12 月"） | 荃银高科公告 2021-081 https://qxb-pdf-osscache.qixin.com/AnBaseinfo/5dee8d02b4916119e02e7f14dd7281c9.PDF ；农资与市场 https://www.enongzi.com/news/details/9f24f1e7-2260-47fb-98cd-858174cf039f ；东方财富财富号 https://caifuhao.eastmoney.com/news/20260107094328341914670 | "中种集团 荃银高科 同业竞争承诺 2026年1月 延期 解决方案 公告" | 高（事件）/中（期限口径） |
| 2025-11-19 | 中种集团与贾桂兰、王玉林签署协议终止一致行动关系；不涉及持股数量变化 | 中种集团表决权比例由 28.36% 降至 20.51%；贾桂兰、王玉林承诺将合计 74,352,520 股不可撤销地用于预受要约 | 荃银高科公告 2025-039 http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2025/2025-11/2025-11-20/11624067.PDF ；中国基金报 https://www.chnfund.com/article/5283f6ef-50d1-66d8-ae6f-3a1db3457d67 | "荃银高科 解除一致行动关系 权益变动 2025年11月 贾桂兰 王玉林 中种集团 持股 20.51%" | 高 |

### A2. 中种集团要约收购（2025-11 至 2026-01）

| 项目 | 内容 | 来源 | 置信度 |
|---|---|---|---|
| 收购人 | 中国种子集团有限公司（中种集团；先正达集团种子业务平台；执行董事、党委书记应敏杰兼任荃银高科董事长） | 要约收购报告书 https://file.finance.qq.com/finance/hs/pdf/2025/12/03/1224843691.PDF （2025-12-03）；董事会致股东报告书 https://file.finance.qq.com/finance/hs/pdf/2025/12/22/1224891538.PDF （2025-12-22） | 高 |
| 首次公告 | 2025-11-20 披露《要约收购报告书摘要》（公告 2025-038） | 上海证券报 https://paper.cnstock.com/html/2025-11/21/content_2148635.htm （2025-11-21）；cninfo http://static.cninfo.com.cn/finalpage/2025-11-20/1224818286.PDF | 高 |
| 要约类型 | 部分要约、主动要约（非履行法定义务）、不以终止上市为目的 | 瑞财经 https://m.rccaijing.com/news-7414998422551983285.html | 高 |
| 要约价格 | 11.85 元/股；较停牌前收盘价溢价约 16.63%（媒体口径"溢价超 16%"；停牌前收盘价 10.16 元未在摘要中直接核实） | 新浪财经 https://finance.sina.com.cn/jjxw/2025-11-21/doc-infyeesh7066966.shtml （2025-11-21）；雪球 https://xueqiu.com/2889927689/348915943 | 高（价格）/中（溢价率） |
| 预定收购数量 | 189,466,350 股，占已发行股份 20.00% | 同上 | 高 |
| 所需资金 | 不超过 2,245,176,247.50 元；已存入 44,903.5 万元（20%）履约保证金；资金来源为中种集团自有资金 | 中金财务顾问报告 https://file.finance.qq.com/finance/hs/pdf/2025/12/03/1224843693.PDF | 高 |
| 要约期限 | 2025-12-04 至 2026-01-05 | 同上；界面新闻 https://m.jiemian.com/article/13845109.html （2026-01-05） | 高 |
| 预受结果 | 3,763 个账户、共 297,787,643 股预受要约，超过预定数量，按同等比例收购：收购数量 = 该股东预受股数 × (189,466,350 ÷ 预受总数) | 荃银高科结果公告（2026-01-08）；腾讯新闻 https://news.qq.com/rain/a/20260108A06JUQ00 ；界面 https://m.jiemian.com/article/13860836.html | 高 |
| 完成后持股 | 中种集团持有 383,760,376 股，占总股本 **40.51%**（"最高 40.51%"即实际达到的比例） | 同上；瑞财经 https://m.rccaijing.com/news-7414998422551983285.html | 高 |
| 锁定承诺 | 收购完成后 18 个月内不转让所持股份 | 瑞财经（同上） | 高 |
| 市场反应 | 公告次日市值单日上涨超 15 亿元 | 新浪财经（同上，2025-11-21） | 中 |
| 持续督导 | 中金公司出具 2025 年度及 2026 年第一季度持续督导意见（2026-05-09） | 深交所 https://disc.static.szse.cn/download/disc/disk03/finalpage/2026-05-09/8b20d51a-b44b-4831-8990-8492e8fbeeef.PDF | 高 |
| 法律意见 | 北京市中伦律师事务所法律意见书（2025-12） | http://static.cninfo.com.cn/finalpage/2025-12-03/1224843692.PDF | 高 |
| 收购动机（媒体解读） | 解决同业竞争承诺期限临近、增强控制权、为后续资产整合铺路 | 腾讯新闻 https://news.qq.com/rain/a/20251121A01OWL00 ；钛媒体 https://www.tmtpost.com/7775783.html | 中 |

### A3. 同业竞争解决方案：中种农科股权托管（2026-01-14）

- 2026-01-14 第五届董事会第三十次会议审议通过《关于控股股东履行承诺解决种子业务同业竞争问题暨关联交易的议案》；公司与中种集团签署《股权委托管理协议》，受托管理中种集团持有的**中种农科 100% 股权**。
- 中种农科整合了中国化工集团下属的境内水稻和小麦种子业务；托管期限 3 年，年托管费 60 万元。
- 来源：荃银高科公告 2026-014 https://file.finance.qq.com/finance/hs/pdf/2026/01/15/1224933358.PDF ；董事会决议 2026-006 https://file.finance.qq.com/finance/hs/pdf/2026/01/15/1224933356.PDF ；搜狐 https://www.sohu.com/a/992763572_115377 ；中国基金报 https://www.chnfund.com/article/5feca0cb-4fed-079f-bad2-3a1ecddac37f （2026-01-15）。检索词："荃银高科 股权委托管理协议 中种农科 2026年1月14日 托管 水稻 小麦 种子业务"。置信度：高。
- 解读（中）：市场普遍认为这是"两步走"整合的第一步（先托管、后注入），与先正达港股 IPO 前消除集团内同业竞争的需求相关（东方财富财富号 https://caifuhao.eastmoney.com/news/20260517051258397466450 ；https://caifuhao.eastmoney.com/news/20260604211850277816030 ，均为第三方观点，低置信度）。

### A4. 先正达拟注入种子业务的传闻与进展（2025-08 至今）

- 2025-08：雪球、东方财富财富号出现"先正达拟将中国种子业务注入荃银高科"的分析文章（https://xueqiu.com/2889927689/348915943 ；https://caifuhao.eastmoney.com/news/20250808114504090012770 ，2025-08-08）。**未检索到公司澄清公告或确认公告**（低置信度传闻）。
- 2025-11-25 财富号：认为注入预期"已进入实质性推进阶段"，依据是同业竞争承诺（https://caifuhao.eastmoney.com/news/20251125045344151653410 ，第三方观点）。
- 2026-01-14：以托管方式履约（见 A3），非资产注入。
- 先正达集团 IPO 背景：2021 年申报科创板，2023-03 撤回，2023-05 转报上交所主板并过会，后未推进；2026 年传最快 6 月以保密方式向港交所递表、9–10 月上市，估值或达 500 亿美元、集资 50–100 亿美元，中金、高盛为主承销（观点网 https://www.guandian.cn/m/show/559223 ；财富号 https://caifuhao.eastmoney.com/news/20260212190747053346870 ；https://emcreative.eastmoney.com/app_fortune/article/index.html?artCode=20260611160921019398650&postId=1725014605 ）。检索词："先正达集团 港股 IPO 2026 上市 进展 递交申请"。置信度：中（媒体报道，截至 2026-09-14 未见招股书检索结果）。
- 学术旁证：Li (2025) 分析中国化工收购先正达的动机与绩效（DOI 10.54097/6wc57v73，Undermind 检索，PDF 可得但本次读取配额受限）。

### A5. 董事会与管理层（2025–2026）

- 应敏杰：先正达集团中国副总裁、党委委员、种子业务单元总经理；中种集团执行董事、党委书记；荃银高科第五届董事会董事长兼战略与投资委员会主任（来源：中商情报网 https://s.askci.com/stock/executives/300087/b2b6a149641f6c66.shtml ；董事会致股东报告书）。置信度：高。
- 2025-12-22 第五届董事会第二十九次会议由应敏杰主持（东方财富股吧公告 https://guba.eastmoney.com/news,300087,1642681710.html ）。
- 2026-06：公司聘任 39 岁张晓强为副总经理；副董事长张琴年薪最高 149 万元（新浪财经 https://finance.sina.cn/2026-06-09/detail-iniauefa3396988.d.html ）。置信度：中。

### A6. ST 事件（2026-06）

| 项目 | 内容 | 来源 | 置信度 |
|---|---|---|---|
| 违法事实 | 2024 年年报未如实反映控股子公司四川荃银生物科技股份有限公司与贵州某公司的债权债务关系，在知悉信用风险情况下未单项计提坏账准备，导致 2024 年年报少计提信用减值损失 1,871.51 万元、虚增利润总额 1,871.51 万元，占当期披露利润总额 10.86% | 新浪 https://www.sina.cn/news/detail/5314147304870034.html ；财联社 https://www.cls.cn/detail/2410692 ；腾讯 https://news.qq.com/rain/a/20260626A0A09Q00 （2026-06-26） | 高 |
| 处罚 | 安徽证监局拟对公司警告并罚款 300 万元；应敏杰（时任董事长）、张琴（时任副董事长兼总经理）各警告并罚 150 万元；张庆一（时任董秘兼财务总监）警告并罚 130 万元；合计 730 万元 | 新浪财经 https://finance.sina.com.cn/wm/2026-07-01/doc-inifhmhu4291741.shtml ；中证网 https://www.cs.com.cn/ssgs/01/2026/06/29/detail_2026062910021106.html | 高 |
| 股票处理 | 2026-06-29 停牌一天，2026-06-30 起复牌并实施其他风险警示，简称"荃银高科"→"ST荃银" | 证券之星 https://stock.stockstar.com/IG2026062600042198.shtml ；银行联合信息网 http://www.unbank.info/static/pages/2064/563711.html | 高 |
| 退市风险 | 证监会/公司称未触及重大违法强制退市情形；2025 年审计意见为标准无保留意见（对比 2024 年年报曾被出具"保留意见"） | 财闻网 https://www.caiwennews.com/article/1512776.shtml ；每经 https://www.nbd.com.cn/articles/2025-04-30/3862483.html （2024 年报保留意见，2025-04-30） | 高/中 |
| 后续 | 2026-07-09 公司收到《行政处罚决定书》（第三方笔记转述） | GitHub 第三方研究笔记 chess99/trading-os research/companies/CN/300087/legacy/2026-07-19.md | 低 |

### A7. 荃银高科自身 2024/2025 财务背景（用于对照）

- 2024 年：营业总收入 47.09 亿元（+14.77%），归母净利润 1.14 亿元（-58.23%），毛利率下降 1.90 个百分点；水稻种子收入 18.58 亿元（+5.67%），玉米种子 5.89 亿元（+20.43%），订单粮食、青贮饲料 11.91 亿元（+44.22%）；原因：审定品种增加、同质化、竞争加剧致种子毛利率下降，加大科研投入，计提减值。来源：新浪 http://finance.sina.com.cn/stock/aiassist/yjbg/2025-04-29/doc-ineuwcvr4872895.shtml ；腾讯 https://news.qq.com/rain/a/20250430A02JBQ00 ；证券时报 https://www.stcn.com/article/detail/1741882.html 。置信度：高。
- 2025 年：营业收入 44.95 亿元（-4.55%），归母净利润 -2.12 亿元（-317.91%），扣非净利润 -3.07 亿元（-641.84%），经营现金流 +203.63%；水稻种子、小麦种子收入分别 -12.93%、-12.41%，玉米种子 +10.69%；研发投入资本化 0.35 亿元（资本化率 17.28%，-2.95 pct）；亏损原因：行业高库存、同质化竞争致价格与毛利率下降。来源：2025 年年报 https://static.cninfo.com.cn/finalpage/2026-04-25/1225192807.PDF （2026-04-25）；新浪 https://finance.sina.com.cn/stock/aigc/stockfs/2026-04-25/doc-inhvrtin4199111.shtml 。置信度：高。
- 补充（低置信度，GitHub 第三方笔记转引年报）：2025 年研发费用 1.68 亿元（+23.42%）；2025 年末归母净资产 16.86 亿元、货币资金 16.14 亿元；2026Q1 营收 6.97 亿元（-16.58%）、归母净利 1,138.51 万元（+418.29%）、扣非 -403.41 万元、经营现金流 -6.73 亿元。

---

## B. 政策背景

### B1. 种业振兴行动方案（2021-07）
- 2021 年 7 月中央全面深化改革委员会审议通过《种业振兴行动方案》，是 1962 年以来党中央、国务院首次对种业作出全面部署；提出把种源安全提升到国家安全战略高度，"破难题、补短板、强优势、控风险"。
- 五大行动：种质资源保护利用、创新攻关、企业扶优、基地提升、市场净化。总体安排"一年开好局、三年打基础、五年见成效、十年实现重大突破"。
- 来源：农业农村部 https://www.moa.gov.cn/ztzl/2021ncfzcj/202112/t20211224_6385443.htm （2021-12-24）；中国政府网 https://www.gov.cn/yaowen/liebiao/202406/content_6956168.htm （2024-06）；人民日报 https://paper.people.com.cn/rmrb/html/2024-08/18/nw.D110000renmrb_20240818_1-04.htm （2024-08-18）；吉林省政府 http://www.jl.gov.cn/szfzt/jlssxsxnyxdh/zcyt/202408/t20240821_3285176.html 。检索词："种业振兴行动方案 2021年7月 中央深改委 五大行动 …"。置信度：高。

### B2. 2022 年新《种子法》与实质性派生品种制度
- 2022-03-01 施行，为 2000 年颁布以来第四次修改。核心：(1) 建立实质性派生品种（EDV）制度——EDV 可申请并获得品种权，但以商业为目的利用时须征得原始品种权人同意；(2) 植物新品种权保护范围由繁殖材料延伸至收获材料，保护环节由生产、繁殖、销售扩展到为繁殖而进行的处理、许诺销售、进口、出口、储存等；(3) 加大假劣种子打击力度、完善侵权赔偿。
- 来源：贸促会 https://www.ccpit.org/a/20220209/20220209vs2z.html （2022-02-09）；共产党员网 https://www.12371.cn/2022/02/08/ARTI1644275366322927.shtml ；福建农业农村厅《实质性派生品种制度知识"10问"》解读 http://nynct.fujian.gov.cn/ztzl/xdzy/zcfg_6126/202404/t20240409_6425826.htm （2024-04-09）；植物新品种保护网 http://www.newpbr.com/index.php/article/757.mhtml 。置信度：高。
- 2026 年中央一号文件明确"加快实施实质性派生品种制度"（见 B3）。学术旁证：Qin & Su (2026, GM Crops & Food) 建议完善育种者权利与实质性派生品种规则并引入惩罚性赔偿（DOI 10.1080/21645698.2025.2610592）。

### B3. 中央一号文件涉种内容（2024–2026）
| 年份 | 涉种关键表述 | 来源 | 置信度 |
|---|---|---|---|
| 2024 | "加快推进种业振兴行动，完善联合研发和应用协作机制，加大种源关键核心技术攻关，加快选育推广生产急需的自主优良品种。开展重大品种研发推广应用一体化试点。推动生物育种产业化扩面提速。" | 新京报全文 https://m.bjnews.com.cn/detail/1706953937129067.html （2024-02-03）；川观新闻 https://cbgc.scol.com.cn/news/6189701 | 高 |
| 2025 | "以科技创新引领先进生产要素集聚，因地制宜发展农业新质生产力……培育农业科技领军企业；深入实施种业振兴行动，发挥'南繁硅谷'等重大农业科研平台作用，加快攻克一批突破性品种；继续推进生物育种产业化。"（生物育种连续第五年写入） | 七一网全文 https://m.12371.gov.cn/content/2025-02/23/content_484970.html ；新京报 https://m.bjnews.com.cn/detail/1738926531129602.html （2025-02-07） | 高 |
| 2026 | "深入实施种业振兴行动，加快选育和推广突破性品种，推进生物育种产业化"；"加强种质资源精准鉴定和创制利用，实施农作物种质资源改良计划，加强国家种业阵型企业梯度培育，深入推进国家育种联合攻关和畜禽遗传改良计划，加快选育推广高油高产大豆、耐密宜机收玉米、优质抗病小麦等突破性新品种"；"持续推进南繁硅谷、黑龙江大豆等国家育制种基地建设"；"强化种业知识产权保护，严厉打击假冒伪劣、套牌侵权……加快实施实质性派生品种制度" | 北京市农业农村局全文 https://nyncj.beijing.gov.cn/nyj/snxx/zwyw/743919914/index.html ；新浪全文 https://finance.sina.com.cn/stock/roll/2026-02-03/doc-inhkpvfe3682932.shtml （2026-02-03）；界面 https://www.jiemian.com/article/13978597.html | 高 |
- 历史脉络（中）：2021 年"加快实施农业生物育种重大科技项目"→2022 年"启动农业生物育种重大项目"→2023 年"全面实施生物育种重大项目，加快玉米大豆生物育种产业化步伐"→2024 年"扩面提速"（川观新闻，同上）。

### B4. 生物育种产业化（转基因玉米/大豆，2021–2026）
| 时间 | 事件/数字 | 来源 | 置信度 |
|---|---|---|---|
| 2021–2023 | 转基因玉米大豆产业化应用试点三年；2021 年在内蒙古兴安盟科右前旗等地商业化种植 66 ha（Quan et al. 2026）；2023 年试点扩展到 5 个省区 20 个县 | 1921.org.cn https://www.1921.org.cn/jrgz/2024/01/24/detailed_2024012437632.html ；Quan et al. 2026 Pest Manag Sci DOI 10.1002/ps.70796 | 高 |
| 2023 | 东北转基因玉米种植面积达 250,000 ha（Quan et al. 2026） | 同上（Scholar Gateway） | 高（文献） |
| 2023-10-17 | 种业管理司公示初审通过 37 个转基因玉米、14 个转基因大豆品种 | 新浪 https://finance.sina.cn/2023-10-30/detail-imzswrkn0562760.d.html ；前瞻 https://t.qianzhan.com/caijing/detail/231018-98a970f7.html | 高 |
| 2023-12-07 | 农业农村部第 732 号公告：裕丰303D 等 37 个转基因玉米、脉育526 等 14 个转基因大豆品种通过第五届国家品审委第四次会议审定 | 新浪 https://finance.sina.com.cn/jjxw/2023-12-08/doc-imzxhwtv7274350.shtml ；北大现代农学院 https://www.saas.pku.edu.cn/xwzx/zhxw/afc2e642be0d4bcab91764beea12a1b4.htm | 高 |
| 2023-12-25 | 首批转基因玉米大豆种子生产经营许可证：85 家企业获证，其中 26 家企业涉及 37 个转基因玉米、10 个转基因大豆品种 | 同上；GitHub 镜像 nuz007/qqnews 2023-12-27 | 高 |
| 2024 | 进入为期 3 年的产业化示范阶段；允许种植省份 8 个（吉林、内蒙古、辽宁、河北全省放开，云南、四川、广西、甘肃部分区域）；面积口径不一：约 1,000 万亩（证券时报/新浪引述） vs "扩大至 2,000 万亩以上"（农药协会标准网/种业商务网） | 证券时报 https://www.stcn.com/article/detail/1367879.html （2024-10）；新浪 https://finance.sina.com.cn/jjxw/2024-10-25/doc-incttsxz5763677.shtml ；农药工业协会 https://bz.ccpia.org.cn/xil52c/202502/7fc51cc834cde39de1c9eaf0db242842.html ；农业农村部 https://www.moa.gov.cn/ztzl/zjyqwgz/ckzl/202411/t20241126_6466932.htm | 中（面积口径冲突，未解决） |
| 2024 | 第二批审定 27 个转基因玉米、3 个转基因大豆；2023–2024 累计审定 64 玉米 + 17 大豆；2024 年安全证书批准清单（二）（三） | 世界农化网 https://cn.agropages.com/News/NewsDetail---32568.htm ；农业农村部 https://www.moa.gov.cn/ztzl/zjyqwgz/spxx/202412/t20241231_6468714.htm ；华泰研报 https://file.iyanbao.com/pdf/89b62-54ef436b-73ae-4d7a-9858-7f2e1b381717.pdf | 高 |
| 2025-04-09 | 第三批初审公示 97 个转基因玉米、2 个转基因大豆 | 腾讯 https://news.qq.com/rain/a/20250409A09QO600 ；新浪 https://finance.sina.com.cn/roll/2025-04-09/doc-inespimz3113136.shtml | 高 |
| 2025 | 农业农村部第 947 号公告审定华皖763D 等 96 个转基因玉米、交育1号GS 等 2 个转基因大豆；累计三批 160 个转基因玉米、19 个转基因大豆通过国审；多家企业获转基因玉米种子生产经营许可证 | 农药协会标准网（同上）；种业商务网 https://www.chinaseed114.com/news/29/news_140887.html （2025 年终盘点） | 高 |
| 2025 | 获准种植省份扩至 13 个（黑龙江、吉林、内蒙古、辽宁、河北、山东、河南、安徽、四川、云南、广西、甘肃、江苏）；面积预测：约 3,100 万亩（报告大厅）/4,500 万亩（网易）/"突破 5,000 万亩"（种业商务网）；第三方研报称"预计 5,000 万亩，大北农丰脉性状市占率 60%，隆平/先正达/大北农过审品种 19/12/15 个" | https://m.chinabgao.com/freereport/101253.html ；https://c.m.163.com/news/a/JFNVE6CM0511D74L.html ；https://www.chinaseed114.com/news/28/news_136011.html ；GitHub Ronchy2000/Gator-Investment-Research reports/155.md（2025-06-13 鳄鱼派研报） | 中/低 |
| 2026 | 大北农 2026-05-08 投资者调研：预计 2026 年国内转基因玉米推广面积占比超 60%；赤峰市 2026 年生物育种产业化重大技术协同推广项目筛选 54 个转基因玉米品种比对试验 | 新浪 https://finance.sina.com.cn/stock/aigc/jgdy/2026-05-08/doc-inhxewcz7576514.shtml ；赤峰市政府 http://www.chifeng.gov.cn/ywdt/bmdt/202605/t20260515_2766301.html | 中 |
- 学术综述：Mou et al. (2025, GM Crops & Food 16:450–481) 系统回顾中国转基因主粮作物商业化的监管里程碑（DOI 10.1080/21645698.2025.2520664）；Quan et al. (2026, Pest Manag Sci 82:7286–7297) 报告东北转基因玉米商业化降低虫害、产量损失与农药用量。

### B5. 国家南繁硅谷
- 《国家南繁硅谷建设规划（2023—2030 年）》由农业农村部、国家发改委、财政部、自然资源部、海关总署联合印发，2024-01-31 在三亚召开发布会；目标：到 2025 年国家级种业创新基地初步建成，到 2030 年南繁硅谷全面建成；四大定位：国家级种业创新基地、种业高质量发展新引擎、种业科技国际合作大平台、种业深化改革开放试验区；以崖州湾实验室、南繁科研育种基地为平台。
- 来源：中国政府网 https://www.gov.cn/lianbo/bumen/202401/content_6929295.htm （2024-01）；海南省政府 https://www.hainan.gov.cn/hainan/5309/202402/97b736b2bdd04811a496edd5bd74331f.shtml ；海南科技厅 https://dost.hainan.gov.cn/kjxw/mtjj/202402/t20240205_3589720.html 。置信度：高。规划中具体面积指标未在摘要中出现（未确认）。

### B6. 种业企业扶优行动与国家种业阵型企业
- 2022-08 农业农村部办公厅《关于扶持国家种业阵型企业发展的通知》：从全国 3 万余家种业企业中遴选 69 家农作物、86 家畜禽、121 家水产种业企业（媒体统称 270 家），构建"破难题、补短板、强优势"阵型。69 家农作物企业中：19 家聚焦水稻、小麦构建"强优势"阵型，32 家聚焦玉米、大豆、棉花、油菜、马铃薯构建"补短板"阵型，18 家构建"破难题"阵型。
- 来源：农业农村部 https://www.moa.gov.cn/govpublic/nybzzj1/202208/t20220810_6406693.htm ；https://zys.moa.gov.cn/gzdt/202208/t20220804_6406334.htm ；腾讯 https://news.qq.com/rain/a/20220810A03EUK00 ；新浪 https://finance.sina.com.cn/jjxw/2022-08-13/doc-imizmscv6017083.shtml 。置信度：高。
- **荃银高科入选情况**：公司被认定为"中国种业领军企业、'强优势'阵型企业（水稻）、'补短板'阵型企业（棉花）、农业国际贸易高质量发展基地"（来源：公司 2023 年年报摘要/2024、2025 半年报及安徽省政府新闻办 http://fbh.anhuinews.com/tjcfd/cxah/202304/t20230412_6791628.html ；公司官网 http://www.winallseed.com/list/71.html ）。检索词："荃银高科 入选 国家种业阵型企业 强优势 水稻 安徽 名单 2022"。置信度：中（未直接看到农业农村部名单原文）。
- 2025 年未检索到阵型企业名单调整/新增的官方通知（未找到）。2026 年一号文件提出"加强国家种业阵型企业梯度培育"。
- 扶优导向：打造航母型领军企业、"隐形冠军"企业和专业化平台企业；推动科研单位、金融机构、种业基地与阵型企业对接（农业农村部通知，同上）。

### B7. 品种审定绿色通道 / 联合体试验
- 《主要农作物品种审定办法》（2016 年农业部令第 4 号，2016-08-15 施行，替代 2001/2007/2014 版；2022 年再次修订）：育繁推一体化企业可自行开展试验（"绿色通道"）；企业联合体、科企联合体、科研单位联合体可自行组织区域试验，联合体成员≥5 家、签订合作协议、权利平等责任对等，同一试验区域内一个法人只能参加一个联合体；参加自主试验和联合体试验的品种不再参加国家/省级统一区试。
- 来源：农业农村部 https://www.moa.gov.cn/gk/nyncbgzk/gzk/202210/P020221012660321003677.pdf ；中国政府网 https://www.gov.cn/zhengce/2022-01/21/content_5721398.htm ；司法部 https://www.moj.gov.cn/pub/sfbgw/flfggz/flfggzbmgz/201607/t20160726_145876.html 。置信度：高。
- 效果（文献）：Xiang et al. (2025, Agribusiness) 指出 2015 年底修订种子法并增加三条试验渠道后，审定品种数量显著增加：2000 年玉米 150 个、水稻 279 个，2005 年起十余年维持约 500 个/年，2017 年起急升，2021 年达玉米 3,779 个、水稻 2,287 个（DOI 10.1002/agr.22020）。置信度：高（文献原文）。
- 国审稻数量：2023 年 409 个，2024 年 405 个；2024 年国审稻优质二级以上占 57%、杂交稻占 87.9%；2021 年修订水稻、玉米审定标准（提高产量、品质、抗性要求）后 2021–2023 年审定数量明显下降。来源：天鸿种子网 https://seed-china.com/Info.aspx?Id=53616&ModelId=1 ；种业商务网 https://www.chinaseed114.com/news/26/news_129758.html 。置信度：中。2025 年国审数量未找到。

---

## C. 行业数据

### C1. 杂交水稻种植面积与占比（文献口径）
- 中国水稻面积 30.08 百万公顷，常规稻与杂交稻面积大致相当（Ye et al. 2022, New Phytologist, DOI 10.1111/nph.18500，引 FAO）。
- 杂交稻占水稻总面积约 53%（Hu et al. 2016，转引自 Zhou et al. 2024 Plant Biotechnol J, DOI 10.1111/pbi.14322）；"近年约 1.67×10^7 hm²、超过 50%"（Xin et al. 2023 Plant Breeding 143:83–85, DOI 10.1111/pbr.13083，口径偏旧）；两系杂交稻年种植约 300 万 ha（Li et al. 2023 Plant Breeding 143:96–104, DOI 10.1111/pbr.13134）。
- 杂交稻面积下降趋势：Huang (2021) "The decreasing area of hybrid rice production in China: causes and potential effects on Chinese rice self-sufficiency", Food Security 13:267–272, DOI 10.1007/s12571-021-01199-z（Undermind 检索；摘要与年度数字未能获取，需原文核对）。
- 2015–2025 逐年杂交稻种植面积序列：**未找到**（Web 配额耗尽；建议查《中国农业统计资料》/全国农技中心年度种子供需报告）。

### C2. 杂交稻种子制种面积、产量、库存、需求（全国农技中心口径）
| 年度 | 制种面积 | 新产种子 | 总供给 | 需求 | 结转/有效库存 | 供需比 | 来源 | 置信度 |
|---|---|---|---|---|---|---|---|---|
| 2024 | 192 万亩（-24 万亩；12.8 万 ha，-11%） | 约 3.1 亿公斤（-0.3 亿公斤） | 2024/25 年度 41 万吨 | 35 万吨（含出口 3 万吨；较 2023/24 +30%，因集中育秧、机插亩用种量↑） | 结转 10 万吨 | 178% | 新浪 https://finance.sina.com.cn/money/future/wemedia/2024-12-02/doc-incxzrau5637850.shtml （2024-12-02）；前瞻 https://www.qianzhan.com/analyst/detail/220/260323-7b32f614.html （2026-03-23）；华经 https://www.huaon.com/channel/trend/1173272.html | 高 |
| 2025 | 225.4 万亩（+17.4%） | 预计亩产高于上年 | — | 2026 年商品种需求预计 3.3 亿公斤（含出口约 0.3 亿公斤） | 上年有效库存约 0.91 亿公斤 | 125% | 华经（同上）；搜狐 https://www.sohu.com/a/931478963_120950077 ；财富号 https://caifuhao.eastmoney.com/news/20260604164701889812730 | 中 |
- 制种大省：2024 年福建杂交稻制种 60.39 万亩、产量 1.1 亿公斤，连续七年全国第一；江西 57.9 万亩居第二（搜狐，同上）。置信度：中。
- 价格与"内卷"：2024 年杂交稻种子供应充足、仍处去库存阶段；预计 2025 年竞争激烈、价格延续低迷并维持同等水平；2026 年"品种分化极其剧烈"，传统品种受陈种清库存和同质化竞争制约、价格上行空间有限，制种总费用预计下降 5%–10%（种业商务网 https://www.chinaseed114.com/news/27/news_134738.html ；华经，同上；前瞻 https://www.qianzhan.com/analyst/detail/220/260408-0697f783.html ）。置信度：中。
- 荃银年报佐证：2024 年"审定品种增加、同质化程度高、竞争加剧"致种子毛利率下降；2025 年"行业高库存、同质化竞争加剧致产品价格与毛利率下降"（见 A7）。

### C3. 水稻直播 / 机插比例
- 江西 2015 年约 60% 早稻采用直播；湖南机插比例由 2019 年 34% 升至 2023 年 54%，江苏 2023 年超过 75%；政府补贴倾向机插而非直播；直播稻较移栽减产约 6%（中国数据 meta 分析，Liao et al. 2024）—— Liu & Huang (2026) Agronomy Journal 118(3), DOI 10.1002/agj2.70407。置信度：高（文献）。
- 长江流域 1,002 户调查中约 79% 采用直播（Zhang & Hu 2022, Agriculture 12:1439, DOI 10.3390/agriculture12091439）。
- 全国农技中心：集中育秧和机插推广使杂交稻亩用种量平均提高约 10%（新浪 2024-12-02，同上）。
- 全国机械化率历史口径：2012 年机械化种植约 8.92×10^6 ha，其中 >85% 为机插（He et al. 2018 Agron J 110:104–114, DOI 10.2134/agronj2017.06.0334）；另有"仅 33.7% 水稻面积机械化种植"的早期口径（Xing et al. 2025 J Sci Food Agric, DOI 10.1002/jsfa.70273）。
- 全国最新直播/机插/人工移栽比例：**未找到**（缺口）。

### C4. 再生稻面积
| 范围 | 数字 | 来源 | 置信度 |
|---|---|---|---|
| 全国 | 11 个省市种植再生稻超过 120 万公顷（福建、江西、浙江、湖南、湖北、安徽、江苏、四川、重庆、云南、贵州）；潜在面积 >500 万公顷，再生季 4,000–6,000 kg/hm² 可年增产 200–300 亿公斤 | Luo et al. 2025 Ecology and Evolution 15(12), DOI 10.1002/ece3.72724（引 Lin et al. 2024） | 高（文献） |
| 全国目标 | 农业农村部：2025 年继续扩大再生稻种植面积，制定再生稻全产业链问题清单，力争到 2030 年全国再生稻面积新增 1,000 万亩左右 | 央视《新闻联播》2025-02-22（GitHub 镜像 DuckBurnIncense/xin-wen-lian-bo news/20250222.md；原文 https://tv.cctv.com/2025/02/22/VIDEo1F9E7opr59A0YMREXWS250222.shtml ） | 高 |
| 湖北 | 再生稻已增至 200,000 ha | Xia et al. 2022 Agronomy Journal 114(4):2352–2363, DOI 10.1002/agj2.21099 | 高（文献，年份口径约 2020） |
| 湖北/湖南/江西 | 省级综述：Wang, Cui & Huang 2023 (Hubei), Wang et al. 2023 (Hunan), Xiong et al. 2023 (Jiangxi), 均载于 Crop and Environment | DOI 10.1016/j.crope.2023.02.002；10.1016/j.crope.2023.05.002；10.1016/j.crope.2023.04.005（Undermind；摘要未获取） | 中 |
| 适宜区 | 当前气候情景下潜在适宜区 193.90×10^4 km²（占国土 20.19%），高适宜区集中于四川盆地、重庆西部、湖北南部东部、湖南中东部、江西中北部等 | Luo et al. 2025（同上） | 高 |
| 经济性 | 再生稻两季 ~15 t/ha/yr，较中稻增收 4,500–6,000 kg/ha、增净收入 7,500–11,000 元/ha，省种省工省水，化肥减 30–50%、农药减 40% | Lin 2019 J Integr Agric, DOI 10.1016/S2095-3119(19)62568-2 | 高（文献） |
- 湖南、安徽、四川、福建 2024/2025 年分省官方面积：**未找到**（Web 配额耗尽）。

### C5. 优质稻比例与超级稻认定
- 优质稻：2024 年国审稻品种中优质二级以上占 57%（天鸿种子网，见 B7）；全国优质稻种植比例官方数字未找到。文献：Lu et al. (2024, Agronomy 14:1234) 分析 17,785 个审定水稻品种品质趋势，显示 40 年来品质总体改善（DOI 10.3390/agronomy14061234）；Zeng et al. (2019, J Cereal Sci) 分析 2007–2017 华南优质稻品种品质变化（DOI 10.1016/j.jcs.2019.03.015）。
- 超级稻：截至 2023 年农业农村部确认的超级稻品种共 129 个（Zheng et al. 2023 J Integr Plant Biol 66:532–545, DOI 10.1111/jipb.13598）；"130 个"（Zhu et al. 2020 Crop Sci 60:1556–1568, DOI 10.1002/csc2.20150，引 ricedata.cn）；2018 年超级稻年种植面积超 8.67 百万 ha、占水稻面积 30%，累计超 1.3 亿 ha（Zheng et al. 2023 引福建稻麦科技 2018）；近年年种植面积约 900 万 ha（Bin Rahman & Zhang 2022 Food Energy Secur 12(2), DOI 10.1002/fes3.390，引 Chen et al. 2017）。置信度：高（文献）。2024/2025 年最新认定数未找到。

### C6. 种业企业集中度与前十强
- CR5：2019 年 9.6% → 2023 年 19.2%，形成"中信集团、中化集团、国投集团"三极格局；2011 年以来扶优政策后企业数量大幅减少、并购加速（Wang & Kang 2025, DOI 10.52819/jnes.2025.37.3.1，Undermind）。置信度：高（文献摘要）。
- 早期口径：2000–2009 年种子企业由 2,300 余家增至 8,700 余家（Miao et al. 2026 Agribusiness, DOI 10.1002/agr.70065）；2016 年后企业数量增长放缓、集中度开始提高，前五强市场份额 <10%（Luo et al. 2022 Mobile Information Systems, DOI 10.1155/2022/9905894）。
- **CR10 具体数值与"前十强企业名单及收入"：未找到**。部分线索：Xie et al. (2023, Agribusiness 39:1173–1198, DOI 10.1002/agr.21823) 表 2 列出 2021 年销售额（百万美元）：中农发种业 526、隆平高科 489、丰乐种业 366、荃银高科 356、敦煌种业 129、大北农（种业）78；同文指出荃银高科订单农业毛利率由 2018 年 3.56% 升至 2021 年 7.6%，收入占比由 5.87% 升至 28.73%。置信度：中（文献表格，口径需核）。

---

## D. 竞争对手同期关键数字（2024/2025）

> 说明：Web 配额耗尽后，以下 2025 年数字主要来自 GitHub 第三方研究笔记（chess99/trading-os，2026-07 编写，自称转引各公司 2025 年年报/年报摘要并附 cninfo/dfcfw 链接），置信度为**低–中**，论文引用前须以公司年报原文核对。

| 公司 | 2024 | 2025 | 研发/其他 | 来源 | 置信度 |
|---|---|---|---|---|---|
| 隆平高科（000998） | — | 营收 84.77 亿元（-1.0%），归母净利 1.66 亿元，玉米种子收入约 50.40 亿元；2025 年完成 12 亿元定增（认购方中信农业，净额 11.8753 亿元），年末资产负债率 59.50%；2026Q1 营收 -35.56%、归母净利 -1.31 亿元 | 2019 年研发投入 4.2 亿元、占营收 13.15%（时代周报，旧数据） | GitHub chess99/trading-os 000998/2026-07-11.md、300087/2026-07-19.md（转引年报点评 https://pdf.dfcfw.com/pdf/H3_AP202604211821362286_1.pdf ） | 低–中 |
| 登海种业（002041） | — | 营收 11.02 亿元（-11.5%），归母净利 9,165.34 万元（+61.9%）；2025H1 营收 3.69 亿元、净利 3,511 万元；Q4 单季收入 5.88 亿元；2026Q1 净利 3,373.76 万元（+37.16%）；2025 年启动转基因大豆"登海豆 1 号"产业化试点 | 利润 93% 以上来自玉米杂交种 | 同上 002041/2026-07-12.md（转引 https://www.sohu.com/a/1013085868_122021998 ） | 低–中 |
| 大北农（002385） | — | 营收 291.19 亿元（-10.46%），归母净利 -6.42 亿元，扣非 -8.37 亿元；种业产品收入 15.28 亿元（玉米 8.14 亿、水稻 5.62 亿）；2026Q1 种业收入约 2.98 亿元；2026-05 称 2026 年转基因玉米推广面积占比将超 60% | 转基因性状（丰脉）市占率约 60%（第三方研报） | 同上 002385/2026-07-12.md（转引年报摘要 https://static.cninfo.com.cn/finalpage/2026-04-24/1225171414.PDF ）；新浪 2026-05-08 调研 | 低–中 |
| 国投丰乐 / 丰乐种业（000713） | 2024 年转基因玉米种子销售 700 万公斤，带动玉米种子收入 +23.41%（第三方研报） | 营收 29.03 亿元（-0.79%），归母净利 6,602.10 万元（-5.47%），扣非 6,666.52 万元（+29.21%），经营现金流 2.92 亿元（玉米制种面积减少）；2025 年更名"国投丰乐"；2026Q1 营收 4.86 亿元（-11.27%）、净利 -1,675.28 万元 | — | 同上 000713/2026-07-11.md；GitHub Ronchy2000 鳄鱼派研报 2025-06-13 | 低–中 |
| 神农种业 / 神农科技（300189） | — | 营收 2.49 亿元；归母净利 1.07 亿元（主要为长期股权投资处置与公允价值变动），扣非 434.16 万元；2026Q1 营收 2,811.54 万元（+213.56%）、净利 -649.95 万元 | — | 同上 300189/2026-07-13.md | 低–中 |
| 垦丰种业（北大荒垦丰，新三板 831888） | — | **未找到** 2024/2025 数字 | — | — | — |
| 荃银高科（300087，对照） | 营收 47.09 亿元，归母净利 1.14 亿元 | 营收 44.95 亿元，归母净利 -2.12 亿元；研发费用 1.68 亿元（+23.42%，第三方） | 见 A7 | 高 |
| 其他参照 | — | 农发种业种子业务收入 6.22 亿元（毛利率 27.89%）；敦煌种业营收 11.34 亿元、归母净利 4,725.14 万元；万向德农营收 1.98 亿元、净利 554 万元 | — | 同上 600313、600354、600371 笔记 | 低 |

---

## E. 文献条目（学术工具检索）

格式：作者. 年份. 标题. 期刊, 卷(期): 页. DOI.（工具）

1. Huang M. 2021. The decreasing area of hybrid rice production in China: causes and potential effects on Chinese rice self-sufficiency. Food Security, 13: 267–272. DOI 10.1007/s12571-021-01199-z.（Undermind）
2. Huang M. 2022. Hybrid breeding and cultivar diversity in rice production in China. Agricultural & Environmental Letters, 7(1). DOI 10.1002/ael2.20074.（Undermind；安徽、湖南、江西、四川杂交稻品种多样性接近饱和，提示"过度育种"）
3. Li J, Luo X, Zhou K. 2023. Research and development of hybrid rice in China. Plant Breeding, 143(1): 96–104. DOI 10.1111/pbr.13134.（Scholar Gateway）
4. Zheng X, Wei F, Cheng C, Qian Q. 2023. A historical review of hybrid rice breeding. Journal of Integrative Plant Biology, 66(3): 532–545. DOI 10.1111/jipb.13598.（Scholar Gateway/Undermind）
5. Xin Y, Zhang Z, Huang J, Luo L. 2023. Yuan Longping, a great world hunger fighter. Plant Breeding, 143(1): 83–85. DOI 10.1111/pbr.13083.（Scholar Gateway）
6. Ye J, et al. 2022. Genomic insight into genetic changes and shaping of major inbred rice cultivars in China. New Phytologist, 236(6): 2311–2326. DOI 10.1111/nph.18500.（Scholar Gateway）
7. Zhou L, et al. 2024. Temperature and light reverse the fertility of rice P/TGMS line ostms19 via reactive oxygen species homeostasis. Plant Biotechnology Journal, 22(7): 2020–2032. DOI 10.1111/pbi.14322.（Scholar Gateway；引杂交稻占 53%）
8. Liu K, Huang M. 2026. Assessments of rice establishment methods adapted to shrinking farming workforces in southern China. Agronomy Journal, 118(3). DOI 10.1002/agj2.70407.（Scholar Gateway）
9. Zhang C, Hu R. 2022. Adoption of direct seeding, yield and fertilizer use in rice production: empirical evidence from China. Agriculture, 12(9): 1439. DOI 10.3390/agriculture12091439.（Undermind）
10. Huang M, et al. 2021. Yield performance of inbred rice grown under labor-saving crop establishment methods. Agronomy Journal, 113(6): 5126–5132. DOI 10.1002/agj2.20769.（Scholar Gateway）
11. He H, et al. 2018. Effects of nursery tray and transplanting methods on rice yield. Agronomy Journal, 110(1): 104–114. DOI 10.2134/agronj2017.06.0334.（Scholar Gateway）
12. Luo W, et al. 2025. Study on the suitable area of ratoon rice in China under climate change. Ecology and Evolution, 15(12). DOI 10.1002/ece3.72724.（Scholar Gateway/Amass/Undermind）
13. Xia F, et al. 2022. Productivity and water use of ratoon rice cropping systems with water-saving, drought-resistant rice. Agronomy Journal, 114(4): 2352–2363. DOI 10.1002/agj2.21099.（Scholar Gateway）
14. Lin W. 2019. Developmental status and problems of rice ratooning. Journal of Integrative Agriculture, 18(1). DOI 10.1016/S2095-3119(19)62568-2.（Undermind）
15. Lin W-X, et al. 2024. Research status and prospect of ratoon rice in China under mechanically harvested condition. 应用生态学报, 35(3): 827–836. DOI 10.13287/j.1001-9332.202403.008.（PubMed PMID 38646771）
16. Wu W, et al. 2023. Ratoon rice system of production: a rapid growth pattern of multiple cropping in China: a review. Plants, 12(19): 3446. DOI 10.3390/plants12193446.（Undermind/Amass）
17. Chen T, et al. 2024. Studies and prospectives of mechanically harvested ratooning rice in China. Technology in Agronomy. DOI 10.48130/tia-0024-0012.（Undermind）
18. Xu F, et al. 2021. The ratoon rice system with high yield and high efficiency in China: progress, trend of theory and technology. Field Crops Research, 272: 108282. DOI 10.1016/j.fcr.2021.108282.（Undermind）
19. Yu X, et al. 2022. Predicting potential cultivation region and paddy area for ratoon rice production in China using Maxent model. Field Crops Research, 275: 108372. DOI 10.1016/j.fcr.2021.108372.（Undermind）
20. Wang F, Cui K, Huang J. 2023. Research and practice of ratoon rice in Hubei Province of China. Crop and Environment. DOI 10.1016/j.crope.2023.02.002.（Undermind）
21. Wang W, et al. 2023. Progress and challenges of rice ratooning technology in Hunan Province, China. Crop and Environment. DOI 10.1016/j.crope.2023.05.002.（Undermind）
22. Xiong L, et al. 2023. Ratoon rice cultivation in Jiangxi Province, China. Crop and Environment. DOI 10.1016/j.crope.2023.04.005.（Undermind）
23. Wang W, et al. 2020. Ratoon rice technology: a green and resource-efficient way for rice production. Advances in Agronomy, 159: 135–167. DOI 10.1016/bs.agron.2019.07.006.（Undermind）
24. Saito K, Dossou-Yovo E, Ibrahim A. 2024. Ratoon rice research: review and prospect for the tropics. Field Crops Research, 314: 109414. DOI 10.1016/j.fcr.2024.109414.（Amass）
25. Huang M, Chen J, Cao F. 2022. Estimating the expected planting area of double- and single-season rice in the Hunan-Jiangxi region of China by 2030. Scientific Reports, 12: 6183. DOI 10.1038/s41598-022-10357-y.（Amass）
26. Bin Rahman ANMR, Zhang J. 2022. Trends in rice research: 2030 and beyond. Food and Energy Security, 12(2). DOI 10.1002/fes3.390.（Scholar Gateway）
27. Zhu K, et al. 2020. Agronomic and physiological performance of an indica–japonica rice variety with a high yield and high nitrogen use efficiency. Crop Science, 60(3): 1556–1568. DOI 10.1002/csc2.20150.（Scholar Gateway）
28. Lu Y, et al. 2024. Variations and trends in rice quality across different types of approved varieties in China, 1978–2022. Agronomy, 14(6): 1234. DOI 10.3390/agronomy14061234.（Undermind）
29. Zeng Y, et al. 2019. Changes in the rice grain quality of different high-quality rice varieties released in southern China from 2007 to 2017. Journal of Cereal Science, 87. DOI 10.1016/j.jcs.2019.03.015.（Undermind）
30. Xiang C, Yang R, Wang X, Huang J. 2025. Impact of seed regulation reform on licensing fees of varieties in China. Agribusiness. DOI 10.1002/agr.22020.（Scholar Gateway/Undermind）
31. Xie Z, Yuan S, Zhu J, Li W. 2023. Contract farming led by a seed enterprise and incentives to produce high quality: which contract design performs best? Agribusiness, 39(4): 1173–1198. DOI 10.1002/agr.21823.（Scholar Gateway）
32. Miao B, et al. 2026. Farmers' willingness to pay a premium for certified maize seeds in China. Agribusiness. DOI 10.1002/agr.70065.（Scholar Gateway）
33. Luo X, Zhou Y, Kumar Reddy MP. 2022. Potential food security risks and countermeasures under the background of seed industry innovation based on Industry 4.0. Mobile Information Systems, 2022: 9905894. DOI 10.1155/2022/9905894.（Scholar Gateway；注意期刊质量一般）
34. Wang N, Kang S. 2025. China's seed industry restructuring policy and changes in corporate productivity. Journal of Northeast Asian Economic Studies (Northeast Asia Economic Association of Korea), 37(3). DOI 10.52819/jnes.2025.37.3.1.（Undermind）
35. Wang N, et al. 2025. Efficiency evaluation of the world's top ten seed companies: static and dynamic analysis in the context of global consolidation and sustainability challenges. Sustainability, 17(8): 3346. DOI 10.3390/su17083346.（Undermind）
36. Xu S. 2021. Rethinking the liberation of China's seed market: a comparative study of China's regulatory frameworks with EU and US. Agroecology and Sustainable Food Systems, 46(2): 251–272. DOI 10.1080/21683565.2021.1989104.（Undermind）
37. Mou T-H, Song Q, Liu Y, Song J. 2025. Initiating the commercialization of genetically modified staple crops in China: domestic biotechnological advancements, regulatory milestones, and governance frameworks. GM Crops & Food, 16: 450–481. DOI 10.1080/21645698.2025.2520664.（Undermind）
38. Qin Y, Su K. 2026. From lab to market: industrialization barriers and regulation optimization for new breeding technologies in China. GM Crops & Food. DOI 10.1080/21645698.2025.2610592.（Undermind）
39. Quan Y, et al. 2026. Commercial planting of genetically modified maize lowers pest damage, yield loss and pesticide usage in Northeast China. Pest Management Science, 82(8): 7286–7297. DOI 10.1002/ps.70796.（Scholar Gateway）
40. Li C. 2025. The motivations and performance of China National Chemical Corporation's multinational acquisition of Syngenta. Journal of Innovation and Development. DOI 10.54097/6wc57v73.（Undermind）
41. Wang Q, Bin B, Wang H. 2023. Dynamic diffusion of hybrid rice varieties and the effect on rice production: evidence from China. Frontiers in Sustainable Food Systems, 7: 1071234. DOI 10.3389/fsufs.2023.1071234.（Undermind）
42. Xu L, Yuan S, Man J. 2020. Changes in rice yield and yield stability in China during the past six decades. Journal of the Science of Food and Agriculture, 100(8): 3560–3569. DOI 10.1002/jsfa.10385.（Scholar Gateway；1949–2015 水稻面积 25.7→30.2 Mha，单产 1,865→6,891 kg/ha）

---

## F. 未找到 / 未确认（缺口清单）

1. 先正达/中种集团**正式**的种子业务注入荃银高科方案（重组预案、停牌公告）——截至 2026-09-14 仅有托管协议与市场传闻。
2. 先正达集团港股招股说明书或正式递表公告（仅媒体传闻）。
3. 要约收购停牌前收盘价 10.16 元及溢价 16.63% 的原文核实（摘要仅见"溢价超 16%"）。
4. 2025 年国家种业阵型企业名单调整/新增的官方文件；荃银高科入选"强优势（水稻）/补短板（棉花）"的农业农村部原始名单页面。
5. 2024 年转基因玉米实际种植面积的官方统一口径（1,000 万亩 vs 2,000 万亩以上）；2025 年实际面积（仅预测 3,100–5,000 万亩）；2026 年实际面积/省份清单。
6. 全国杂交水稻种植面积 2015–2025 逐年序列（含占比）；全国杂交稻种子需求量逐年序列（仅有 2024/25、2025/26 年度）。
7. 杂交稻种子期末库存逐年数字（仅 2024/25 结转 10 万吨、2025 有效库存 0.91 亿公斤）。
8. 全国及湖北、湖南、安徽、四川、福建 2024/2025 年再生稻面积官方数字（仅文献 >120 万 ha 与湖北 20 万 ha、全国 2030 年新增 1,000 万亩目标）。
9. 全国水稻直播、机插、人工移栽最新比例（仅省级/样本口径）。
10. 全国优质稻种植比例官方数字；超级稻 2024/2025 年最新认定数（文献口径至 2023 年 129/130 个）。
11. 种业 CR10 与"前十强企业名单及收入"（仅 CR5 9.6%→19.2% 和 2021 年部分企业销售额）。
12. 竞争对手 2024 年完整数字（隆平高科、登海、大北农、丰乐、神农、垦丰）与 2025 年**年报原文**核对；垦丰种业 2024/2025 完全未找到；各公司种子销量（万公斤）与研发投入 2024/2025 数字未找到。
13. 2025 年国审水稻品种数量。
14. 《国家南繁硅谷建设规划》中的面积等量化指标。

---

## G. 检索日志（主要检索词）

WebSearch（39 次成功）："中国种子集团 荃银高科 要约收购 2025年11月 要约价格 收购比例"；"荃银高科 要约收购报告书 中种集团 40.51%"；"荃银高科 要约收购 结果公告 2026年1月 预受要约 股份数量"；"先正达集团 注入种子业务 荃银高科 2025年8月 传闻 澄清公告"；"中化现代农业 入股 荃银高科 2016 张琴 股权转让 历程"；"ST荃银 被实施其他风险警示 原因 2026"；"中种集团 荃银高科 同业竞争承诺 2026年1月 延期 解决方案 公告"；"先正达集团 中国种子业务 注入 荃银高科 2026 进展 重组 停牌"；"荃银高科 2025年年度报告 营业收入 净利润 种子销量 研发投入"；"中化现代农业 2018年 协议受让 荃银高科 21.50% 8.85元 中新融泽 张琴"；"荃银高科 2021年1月 表决权委托 贾桂兰 王玉林 中化现代农业 控股股东 持股比例"；"中种集团 荃银高科 要约收购 溢价 16.63% 停牌前收盘价 10.16元 资金来源 自有资金"；"荃银高科 股权委托管理协议 中种农科 2026年1月14日 托管 水稻 小麦 种子业务"；"荃银高科 行政处罚决定书 安徽证监局 2026 虚增利润 1871.51万元 罚款 张琴"；"先正达集团 港股 IPO 2026 上市 进展 递交申请"；"中种集团 荃银高科 董事长 应敏杰 先正达中国 董事会改组 2025"；"荃银高科 解除一致行动关系 权益变动 2025年11月 …"；"荃银高科 2024年年度报告 营业收入 47.09亿 净利润 种子 订单粮食"；"种业振兴行动方案 2021年7月 中央深改委 五大行动 …"；"新种子法 2022年3月1日施行 实质性派生品种制度 EDV …"；"2024年中央一号文件 种业 生物育种 产业化扩面提速 原文"；"2025年中央一号文件 种业振兴 生物育种 农业科技领军企业 原文内容"；"2026年中央一号文件 种业 内容 生物育种 种源 全文"；"转基因玉米大豆品种审定 2023年12月 首批 37个玉米 14个大豆 …"；"转基因玉米 2024年 推广面积 万亩 省份 …"；"2025年 转基因玉米 推广面积 万亩 种植省份 产业化 农业农村部"；"转基因玉米 2025年 实际种植面积 万亩 …三年示范"；"2026年 转基因玉米 推广 面积 省份 扩大 亿亩 …"；"国家南繁硅谷建设规划 2023-2030年 三亚 崖州湾 种业 面积 万亩"；"国家种业阵型企业 69家 名单 荃银高科 破难题 补短板 强优势 阵型 2022年8月"；"主要农作物品种审定 绿色通道 联合体试验 政策 2014 2016 办法 审定数量 井喷 水稻"；"国家级水稻品种审定数量 2023年 2024年 2025年 …"；"种业企业扶优行动 国家种业阵型企业 2025 新增 名单 调整 农业农村部"；"转基因玉米 品种审定 2024年 第二批 第三批 累计 数量 160个 大豆 19个"；"荃银高科 入选 国家种业阵型企业 强优势 水稻 安徽 名单 2022"；"全国杂交水稻 种植面积 亿亩 2024年 2025年 杂交稻种子需求量 亿公斤 下降"；"杂交水稻 制种面积 万亩 2024年 2025年 制种产量 亿公斤 期末库存 …"；"2025年 杂交稻种子 库存 高企 价格 内卷 降价 种业 竞争 分析"；"2026年 杂交水稻种子 供需 制种面积 库存 价格 下滑 …"。被配额拒绝："全国 再生稻 面积 万亩 2024年 2025年 湖北 湖南 四川 安徽 福建"；"湖北 再生稻 面积 2025年 万亩 全国第一 目标"；"安徽 再生稻 面积 2025年 万亩 发展规划"。

学术工具：Scholar Gateway 9 次（再生稻面积；杂交稻面积趋势；直播/机插比例；种业集中度；超级稻数量；再生稻分省；转基因玉米面积；审定数量）；Undermind search_papers 6 次 + get_paper_info 3 次（read_pdfs 2 次因配额失败）；PubMed 4 次；Amass BiomedCore 2 次；GitHub code search 14 次（竞争对手 2025 财务、再生稻面积、超级稻、CR10、转基因面积）；Hugging Face 数据集检索 1 次（无结果）；Consensus 3 次、Elicit 1 次（配额/权限失败）；WebFetch 1 次（huaon.com，代理拦截）。
