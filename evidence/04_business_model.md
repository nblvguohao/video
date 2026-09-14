# 维度4：荃银高科商业模式演化——"种粮一体化"/订单农业/全产业链模式及其争议

- **维度**：04 商业模式演化（订单农业 / 种粮一体化 / 全产业链 / 数字化平台 / 海外 / 品牌渠道 / 争议）+ 同行对照
- **检索次数**：57 次工具调用（WebSearch 29 次，其中 21 次有效返回、8 次因会话配额 200/200 耗尽被拒；Scholar Gateway 3；Undermind 14；PubMed 2；Consensus 2（月配额耗尽）；Elicit 2（无 API 权限）；GitHub 代码检索 1；curl 4，仅 raw.githubusercontent.com 成功 1 次）
- **来源数**：52 个独立 URL/文献（见文末索引）
- **更新时间**：2026-09-14
- **附件**：`/home/user/video/evidence/04_order_grain_timeseries.csv`（订单粮食逐期收入/占比/毛利率）
- **置信度约定**：高 = 搜索摘要/文献中直接出现原文数字；中 = 搜索工具的综合表述或二手转述；低 = 由两个已知数推算或第三方非官方笔记。所有"推算"均已标注公式。

> 环境说明：本容器内 cninfo/巨潮/深交所/新浪/腾讯等站点均被代理拦截（对 2025 年报 PDF 的一次 curl 返回 `CONNECT tunnel failed 403`），所有中文数字均来自 WebSearch 自带的页面摘要，无法逐页核对原始 PDF。凡本文出现"未找到/未确认"，均为检索未命中，而非该事实不存在。

---

## 1. 检索日志（用于复现）

| # | 工具 | 检索词 | 结果 |
|---|---|---|---|
| 1 | WebSearch | 荃银高科 2025年半年度报告 订单粮食 收入 6.43亿 占比 毛利率 | 命中 2025 半年报 PDF 链接（cninfo 1224594091）、国信证券 2025-05-06 研报 |
| 2 | WebSearch | 荃银高科 种粮一体化 订单农业 模式 起点 2019 2020 | 命中界面新闻 2026-02-28 报道及转载 |
| 3 | WebSearch | 界面新闻 荃银高科 种粮一体化 外衣下的资本疑云 | 8 个转载源（界面/搜狐/网易/腾讯/新浪） |
| 4 | WebSearch | 荃银高科 光大银行 种粮一体化农业产业互联网平台 | 21经济网、央广网、经济日报、新华网、中证网 |
| 5 | WebSearch | 荃银高科 2024年年度报告 订单粮食 营业收入 毛利率 同比 | 腾讯新闻 2025-04-30、证券时报、每经 |
| 6 | WebSearch | 荃银高科 2025年年度报告 订单粮食 收入 毛利率 2026年4月 | 2025 年报 PDF（cninfo 1225192807）分产品毛利率 |
| 7 | WebSearch | 荃银高科 2026年半年度报告 订单粮食 营业收入 净利润 | 仅命中 2026 一季报；半年报未命中 |
| 8 | WebSearch | 荃银高科 2023年年度报告 订单粮食 收入 毛利率 青贮 面积 | 2023 年报摘要/全文、澎湃、证券之星 |
| 9 | WebSearch | 荃银高科 2022年年报 订单农业 订单粮食 收入 亿元 毛利率 | 每经 2023-02-17 |
| 10 | WebSearch | 荃银高科 2021年年报 订单粮食 收入 订单农业 优质稻 专用小麦 | 同花顺 2021 年报全文、证券时报 |
| 11 | WebSearch | 荃银高科 脆秆水稻 谷草兼用 种粮饲一体化 火花技术 农业农村部 | 科技部 ncsti 2021-10-27、投资者关系记录表 2023-10-10、种业商务网 |
| 12 | WebSearch | 荃银高科 证监会 立案调查 信息披露 违法违规 2025 | 界面、财联社、新浪、中国基金报 |
| 13 | WebSearch | 荃银高科 深交所 关注函 问询函 订单粮食 其他应收款 2025 2026 | 要约收购报告书 2025-12-22、证券时报"将被ST" |
| 14 | WebSearch | 荃银高科 2020年年报 订单粮食 收入 首次 订单农业 业务新增 | 界面 2021 年报道、天风 2020-12-10 深度 |
| 15 | WebSearch | 荃银高科 2025年半年报 订单粮食 44.54% 毛利率 -0.09% 种子业务 出口 | 21经济网 2025-11-21 |
| 16 | WebSearch | 荃银高科 2025年第三季度报告 订单粮食 营收 下滑 亏损 1.8亿 | 腾讯 2025-10-30、古东管家 |
| 17 | WebSearch | 荃银高科 2026年经营计划 产品结构调整 订单粮食 收缩 聚焦种业 | 农资与市场"19问荃银高科"、东方财富财富号（低置信） |
| 18 | WebSearch | 荃银高科 海外业务 东南亚 南亚 非洲 种子出口 合资公司 海外基地 | 界面 2024、安徽省政府新闻办 2023-04、证券时报 2023-08 |
| 19 | WebSearch | 荃银高科 回应 界面新闻 种粮一体化 资本疑云 澄清公告 | 未发现澄清公告 |
| 20 | WebSearch | 荃银高科 四川荃银生物 酒粮 酒厂 应收账款 保留意见 毕马威 贵州 | 董事会专项说明 2025-04-30、每经、新浪 2026-07-01 |
| 21 | WebSearch | 荃银高科 订单粮食 面积 万亩 优质稻 专用小麦 青贮玉米 合作社 省份 | 投资者关系记录表 2024-03-27 / 2024-08-27；无省份明细 |
| 22 | WebSearch | 荃银高科 2019年年报 订单农业 收入 1.8亿 订单粮食 首次开展 | 2019 年报（新浪 6122546）、天风深度 |
| 23 | WebSearch | 荃银高科 2021年 订单粮食 营业收入 亿元 占比 毛利率 同比增长 | 仅销量数据 |
| 24 | WebSearch | 荃银高科 2022年 订单粮食 青贮玉米 营业收入 8.94亿 毛利率 占比 | 2022 年报全文链接，摘要无该数字 |
| 25 | WebSearch | 荃银高科 2024年 订单粮食 毛利率 2.66% 青贮饲料 收入 分产品 | 分产品收入，无 2024 订单毛利率 |
| 26 | WebSearch | ST荃银 2026年上半年 半年度报告 营业收入 净利润 订单业务 2026年8月 | 未命中半年报；命中 ST/处罚新闻 |
| 27 | WebSearch | 荃银高科 行政处罚 730万 安徽证监局 ST 2026年 信用减值 贵州 | 财联社、中证网 2026-06-29、新浪 2026-07-01 |
| 28 | WebSearch | 中种集团 要约收购 荃银高科 2025年11月 溢价 同业竞争 中种农科 委托管理 | 腾讯、上证报、新浪 |
| 29 | WebSearch | 荃银高科 "66香" 品牌 米厂 烘干厂 产业一体化营销 | 农资与市场、东方财富财富号 |
| 30-37 | WebSearch（被拒） | 东亚前海深度/国信/天风研报评价、张琴中证网专访、安徽"5+8"试点、脆秆稻品种审定、2024 海外收入、海外合资公司 | **会话配额耗尽，未执行** |
| 38 | Scholar Gateway | Chinese seed companies contract farming/order agriculture integrate seed sales with grain purchase | 15 段落/8 篇，核心：Xie et al. 2023 *Agribusiness* |
| 39 | Scholar Gateway | Brittle culm rice mutant dual use grain and forage genes digestibility lodging | 15 段落/11 篇 |
| 40 | Scholar Gateway | digital agricultural industrial internet platforms and bank credit in contract farming China | 8 段落/6 篇 |
| 41-45 | Undermind search_papers ×5 | seed company-led contract farming；Winall/Longping 案例；同行订单农业；脆秆稻双用；合肥重离子脆秆突变体 | 见第 14 节 |
| 46-50 | Undermind get_paper_info ×5、inspect_deep_searches ×2 | DOI/摘要提取 | 见第 14 节 |
| 51-52 | PubMed search/metadata | brittle culm rice forage dual grain | 1 篇（高粱 SbBC1，间接） |
| 53 | GitHub search_code | "荃银高科" "订单粮食" | 7 个文件；关键：chess99/trading-os 研究笔记 2026-07-19；BilalBAI 2020H1 分部数据 |
| 54-57 | curl | cninfo PDF（403）；raw.githubusercontent（200）；github.com/raw 与 api.github.com（403） | — |

---

## 2. 商业模式演化时间线（2018–2026）

| 时间 | 事件 | 来源 | 置信度 |
|---|---|---|---|
| 2018 | 订单/合同农业业务已存在：占营收 5.87%、毛利率 3.56%（Xie et al. 2023 引东方财富 2022 数据） | https://doi.org/10.1002/agr.21823 | 中 |
| 2019 | 年报口径"订单粮食业务"收入 1.81 亿元，占营收 15.65%（营收 11.54 亿）。天风 2020-12-10 深度称"订单粮食业务自 19 年开展以来迅速发展" | https://pdf.dfcfw.com/pdf/H3_AP202012111439137324_1.pdf ；http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=300087&id=6122546 | 中 |
| 2020-07-13 | 业绩预告：2020H1 净利 800–1200 万（上年同期 -422.18 万），"主要原因系种子销售收入及订单粮食业务收入同期增加，毛利增加" | GitHub 镜像的新浪快讯 2020-07-14（peter678007/json01）；界面新闻同日报道 | 高 |
| 2020H1 | 分部数据：订单粮食业务收入 295,705,187 元，占 H1 总收入 561,624,439 元的 52.65%；水稻 227,412,872 元（40.49%） | GitHub: BilalBAI/tyc-core-aaoifi-results `2020/XSHE/300087_XSHE_2020.json`（第三方整理，口径疑为 2020H1） | 中 |
| 2020 全年 | 订单粮食 4.2 亿元，占 26.2%，同比 +132.45%；营收 16.02 亿（+38.85%），归母净利 1.34 亿（+41.2%）。每经称"自 2020 年开始，公司主营业务新增订单农业业务" | https://www.jiemian.com/article/5711493.html ；https://www.nbd.com.cn/articles/2023-02-17/2674072.html | 中 |
| 2021 | 订单粮食销量 26,561.52 万公斤（+71.58%）；种子销量 10,066.79 万公斤（+51.84%）。Xie et al.：订单业务占比 28.73%、毛利率 7.6% | https://m.10jqka.com.cn/sn/20220328/35103085.shtml ；https://doi.org/10.1002/agr.21823 | 中 |
| 2021-10 | 中科院合肥物质科学研究院与荃银高科签约，"谷草兼用"脆秆水稻关键基因及技术**独家转让**荃银高科 | https://www.ncsti.gov.cn/kjdt/kjrd/202110/t20211027_49997.html | 高 |
| 2022 | 营收 34.91 亿（+38.51%），归母净利 2.33 亿（+38.05%）；订单农业"已成为公司核心业务之一，主要包括订单粮食业务、青贮玉米业务、酿酒专用粮品种产业链业务" | https://www.nbd.com.cn/articles/2023-02-17/2674072.html | 高 |
| 2023-06/08 | 与光大银行合肥分行、科技企业共建"种粮一体化农业产业互联网平台"；"皖美·光大种业贷"上线；成为安徽省"5+8 种粮一体化"互联网平台建设试点单位 | https://finance.cnr.cn/jjgd/20230610/t20230610_526282666.shtml ；https://www.21jingji.com/article/20230809/herald/b955bbb1419a679d269ca5ef3657fcfa.html | 高 |
| 2023 | 营收 41.03 亿（+17.54%）、归母净利 2.74 亿（+17.37%）；订单粮食 7.07 亿、毛利率 4.89%（-1.14pp）；订单农业合计 8.26 亿（-7.60%）；种子销量 2.02 亿公斤 | 2023 年报全文（新浪 9892532）；https://stock.stockstar.com/RB2024032400000208.shtml ；知识铺转载 2024-04-10 | 高 |
| 2024 | "谷草兼用"脆秆水稻种粮饲一体化技术入选农业农村部 2024 年农业"火花技术"成果库；公司建立"种粮一体化"数字化平台 | https://www.chinaseed114.com/news/27/news_133543.html | 中 |
| 2024 | 营收 47.09 亿（+14.77%），归母净利 1.14 亿（-58.23%）；订单粮食+青贮饲料 11.91 亿（+44.22%，增速最快分部）；综合毛利率 25.01%（-7.07pp） | https://news.qq.com/rain/a/20250430A02JBQ00 ；https://www.stcn.com/article/detail/1741882.html | 高 |
| 2025-04-30 | 毕马威对 2024 年报出具**保留意见**（四川荃银生物酒粮应收账款、贵州某公司其他应收款、部分存货） | http://static.cninfo.com.cn/finalpage/2025-04-30/1223414132.PDF ；https://www.nbd.com.cn/articles/2025-04-30/3862483.html | 高 |
| 2025H1 | 订单粮食收入 6.43 亿，占比由年初 25.3% 升至 44.54%，成为第一大板块，毛利率 **-0.09%** | https://www.jiemian.com/article/14045116.html（引 2025 半年报） | 中 |
| 2025-11-20 | 控股股东中种集团宣布部分要约收购 20%（1.89 亿股，11.85 元/股，溢价 16.63%，≤22.45 亿元），承诺 5 年内解决水稻/小麦同业竞争 | https://paper.cnstock.com/html/2025-11/21/content_2148635.htm ；https://news.qq.com/rain/a/20251121A01OWL00 | 高 |
| 2026-01-14 | 与中种集团签署《股权委托管理协议》，受托管理中种农科 100% 股权 | 东方财富财富号 2026-04-01（转述）；GitHub 笔记引 2026 一季报 | 中 |
| 2026-01-30 | 收到证监会《立案告知书》（涉嫌信披违法违规）；同日发布会计差错更正公告；董事会换届（姜业奎董事长、宋维波总经理、刘俊茹财务总监） | https://finance.sina.com.cn/jjxw/2026-01-30/doc-inhkazcf0485362.shtml ；GitHub 笔记 | 高/中 |
| 2026-02-28 | 界面新闻《财说｜荃银高科"种粮一体化"外衣下的资本疑云》 | https://www.jiemian.com/article/14045116.html | 高 |
| 2026-04-25 | 2025 年报：营收 44.95 亿（-4.55%），归母净利 -2.12 亿（上市 15 年首亏）；订单粮食 9.81 亿、毛利率 -1.31%；2026Q1 订单业务收入 -37.28% | https://static.cninfo.com.cn/finalpage/2026-04-25/1225192807.PDF ；https://finance.sina.com.cn/stock/aigc/stockfs/2026-04-25/doc-inhvrtiq7652602.shtml | 高 |
| 2026-06-26→06-30 | 安徽证监局预处罚合计 730 万元；股票 6-29 停牌一天，6-30 起实施其他风险警示，简称"ST荃银" | https://www.cls.cn/detail/2410692 ；https://www.stcn.com/article/detail/3983540.html | 高 |
| 2026-07-09 | 收到《行政处罚决定书》（GitHub 笔记引东方财富公告 AN202607101826875086） | https://data.eastmoney.com/notices/detail/300087/AN202607101826875086.html | 中 |
| 2026H1 | **半年报数据未找到**（应于 2026-08-29 前后披露） | — | 未找到 |

---

## 3. 模式描述

### 3.1 官方定义（年报语言，2021–2025 各期一致）
> 公司利用自身品种、技术、品牌等优势，与粮食加工企业、养殖企业等相关品牌公司确定农产品需求订单，优先采购荃银品种产出的农产品，并在具备条件的种植区域与合作社、种植大户等合作，确定大田种植订单、提供专用种子及配套技术服务；种植结束后，收购合作社、种植大户等的农产品定向销售给粮食加工企业、养殖企业等相关品牌公司。

- 来源：2021 年报（同花顺 https://m.10jqka.com.cn/sn/20220328/35103085.shtml ）、2025 半年报（cninfo 1224594091）、投资者关系记录表 2024-03-27（http://static.cninfo.com.cn/finalpage/2024-03-27/1219429418.PDF ）。置信度：高。
- 三类子业务（2022 年报口径）：**订单粮食业务、青贮玉米业务、酿酒专用粮品种产业链业务**（每经 2023-02-17；高）。
- 作物：专用小麦、优质水稻、青贮玉米（2021/2023 年报）；酿酒专用粮为高粱、小麦（四川荃银生物向古蔺、仁怀、赤水酒厂销售高粱和小麦——界面 2026-02-28；中）。

### 3.2 "品种 + 品牌 + 资本"
- 2022、2023 年报："公司通过'品种+品牌+资本'，与产业链粮食加工企业、养殖企业等相关品牌公司合作，发展专用小麦、优质水稻、青贮玉米等订单农业业务。"（每经 2023-02-17；2023 年报摘要 http://static.cninfo.com.cn/finalpage/2024-03-23/1219389373.PDF ；高）
- 学术定义：Xie et al. (2023) 称之为 "seed company-led agri-food contract farming"，即三层供应链（种子企业—种植者—采购/加工商）中由纵向一体化的种子企业充当链主（https://doi.org/10.1002/agr.21823 ；高）。

### 3.3 "荃银高科 + 科技企业 + 产业合作伙伴 + 金融伙伴"：种粮一体化农业产业互联网平台
- 平台"借助工业互联网的思维，充分发挥种子在农业生产中的核心地位"，连接种植端、加工端、销售端、服务端（央广网 2023-06-10 https://finance.cnr.cn/jjgd/20230610/t20230610_526282666.shtml ；高）。
- 金融嵌入："皖美·光大种业贷"在平台上线，农户可申请最高 **50 万元**、利率低于其他涉农贷款的信用贷款（21经济网 2023-08-09；中国电子银行网 https://www.cebnet.com.cn/20230810/102899846.html ；高）。
- 规模：安徽省"5+8 种粮一体化"互联网平台建设试点单位；平台已上线 **6000 多户**涉农主体，累计交易 **40 亿元以上**（新华网客户端 https://app.xinhuanet.com/news/article.html?articleId=f29d068672df3569d532ee8204900605 ；新华网 2025-02-27 http://www.news.cn/money/20250227/b00ced75781e444db9f7e9e53ec1bd8c/c.html ；中——数据时点未明）。
- 光大银行合肥分行另为荃银收购新疆祥丰生物科技 70% 股权提供累计 **2 亿元**并购额度（经济日报 2023-07-05 http://paper.ce.cn/pad/content/202307/05/content_276902.html ；高）。
- 2024 年半年度新闻："公司建立'种粮一体化'数字化平台"（种业商务网 https://www.chinaseed114.com/news/27/news_133543.html ；中）。
- 高管表述：张琴（副董事长、总经理）"服务国家粮食安全战略 向世界种业前十强挺进"（中证网 2025-05-28 https://www.cs.com.cn/ssgs/gsxw/202505/t20250528_6493796.html ；仅标题，内容未抓取）。

---

## 4. 订单粮食业务逐年收入 / 占比 / 毛利率（2018–2026Q1）

| 期间 | 总营收（亿元） | 订单粮食收入（亿元） | 占比 | 毛利率 | 归母净利（亿元） | 备注 | 置信度 |
|---|---|---|---|---|---|---|---|
| 2018 | — | — | 5.87% | 3.56% | — | Xie et al. 2023 口径 | 中 |
| 2019 | 11.54 | 1.81 | 15.65% | — | — | 天风/东亚前海综合 | 中 |
| 2020 | 16.02 | 4.20 | 26.2% | — | 1.34 | +132.45%；H1 即 2.96–2.98 亿 | 中 |
| 2021 | ≈25.20（推算：34.91/1.3851） | ≈7.24（推算：25.20×28.73%） | 28.73% | 7.6% | — | 销量 26,561.52 万公斤 | 低（推算） |
| 2022 | 34.91 | ≈8.94（推算：8.26/(1-7.60%)，订单农业口径） | ≈25.6% | — | 2.33 | 2022 年报数字未直接命中 | 低（推算） |
| 2023 | 41.03 | 7.07（订单粮食）/ 8.26（订单农业） | 17.2% / 20.1%（推算） | **4.89%**（-1.14pp） | 2.74 | 综合毛利率 26.91%；水稻种子 42.80%、玉米 25.29%、小麦 13.79% | 高 |
| 2024 | 47.09 | 11.91（订单粮食+青贮饲料） | 25.3% | ≈2.66%（推算：-1.31%+3.97pp） | 1.14 | 综合毛利率 25.01% | 高/推算 |
| 2025H1 | ≈14.44（推算：6.43/0.4454） | 6.43 | **44.54%** | **-0.09%** | — | 第一大板块 | 中 |
| 2025Q1-3 | 19.30（-5.9%） | — | — | — | -1.80 | Q3 单季营收 4.98 亿（-22.8%）、亏 1.39 亿；销售净利率 -13.18% | 高 |
| 2025FY | 44.95（-4.55%） | **9.81**（981,414,760.16 元；成本 994,255,695.14 元） | ≈21.8%（推算）；含青贮饲料 11.82 亿 = 26.30% | **-1.31%**（-3.97pp） | -2.12（扣非 -3.07） | 农业业务毛利率 20.90%；水稻种子 39.46%、玉米 22.90%（-10.26pp） | 高 |
| 2026Q1 | 6.97（-16.58%） | — | — | — | 0.1139（+418.29%；扣非 -0.0403） | 种子业务收入 +11.74%，**订单业务收入 -37.28%**；经营现金流 -6.73 亿 | 高 |
| 2026H1 | 未找到 | 未找到 | — | — | — | — | 未找到 |

数据来源：2019 天风 2020-12-10（https://pdf.dfcfw.com/pdf/H3_AP202012111439137324_1.pdf ）；2020 界面（https://www.jiemian.com/article/5711493.html ）；2021 同花顺年报全文；2022 每经；2023 年报全文（http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2024/2024-3/2024-03-23/9892532.PDF ）；2024 腾讯新闻 2025-04-30；2025H1 界面 2026-02-28；2025Q3 腾讯 2025-10-30（https://news.qq.com/rain/a/20251030A03WUP00 ）；2025FY 年报全文（https://static.cninfo.com.cn/finalpage/2026-04-25/1225192807.PDF ）+ GitHub 笔记（水稻种子 16.18 亿/36.00%、玉米 6.52 亿/14.51%、小麦 3.23 亿/7.19%、订单粮食/青贮 11.82 亿/26.30%、种子主业约 27.92 亿、研发费用 1.68 亿 +23.42%、经营现金流 1.99 亿、年末货币资金 16.14 亿）；2026Q1 新浪 AI 财报解读（https://finance.sina.com.cn/stock/aigc/stockfs/2026-04-25/doc-inhvrtiq7652602.shtml ）。

**核实结论**：任务给定的"2025H1 订单粮食收入 6.43 亿、占比 44.54%、毛利率 -0.09%"三项数字与界面新闻原文一致（该文引自 2025 半年报），但本次未能打开半年报 PDF 逐页核对，置信度为中。另一 F10 数据页给出"订单粮食、青贮玉米占 44.79%，水稻种子 25.38%，玉米种子 9.39%，小麦种子 0.61%"（搜狐证券 https://q.stock.sohu.com/cn/300087/index.shtml ；口径疑为 2025H1 主营业务收入，与 44.54% 略有差异，低）。

**毛利率轨迹**：3.56%（2018）→ 7.6%（2021）→ 4.89%（2023）→ ≈2.66%（2024）→ -0.09%（2025H1）→ -1.31%（2025FY）。界面新闻评论："订单粮食业务本质上是粮食贸易，技术含量低、毛利率本身就不高，但像荃银高科这样做到负毛利的，在行业内十分罕见。"

---

## 5. 订单面积、品种、合作方、省份

| 项目 | 检索结果 | 来源 | 置信度 |
|---|---|---|---|
| 订单面积 | **未找到**公司披露的订单种植面积（万亩）；仅有 2023 年"种子推广面积 8000 万亩、可产粮食 850 亿斤"的品种推广口径 | 投资者关系记录表 2024-08-27（https://file.finance.qq.com/finance/hs/pdf/2024/08/27/1221007812.PDF ） | 中 |
| 品种类别 | 专用小麦、优质水稻、青贮玉米、酿酒专用粮（高粱/小麦）、脆秆稻（谷草兼用） | 年报；界面；ncsti | 高 |
| 具体品种名 | **未找到**订单业务对应的具体审定品种名（如脆秆稻品种名）；WebSearch 配额耗尽前未能检索 | — | 未找到 |
| 合作方类型 | 粮食加工企业、养殖企业、"相关品牌公司"、合作社、种植大户、米厂、烘干厂（2026 "66香"）、酒厂（古蔺/仁怀/赤水三家） | 年报；界面；农资与市场 | 高 |
| 隆平高科对照的加工商 | Xie et al. 表 3 列出隆平高科订单农业的下游企业：国穗食品、稻香实业、新禾食品、腾宏实业、瑞丰食品、金沙河面业等，收购价高于市场价 0.011–0.04 美元/kg | https://doi.org/10.1002/agr.21823 | 高 |
| 业务主体 | 四川荃银生物（酒粮）；新疆祥丰生物（70% 股权，光大 2 亿并购额度）；界面称公司有 25 家子公司及关联企业，涉及种业、粮油贸易、生物科技、棉花种植 | 界面 2026-02-28；经济日报 2023-07-05 | 中 |
| 省份 | 安徽（平台试点、"5+8"）、四川/贵州（酒粮）、新疆（祥丰/棉花）；其余省份明细**未找到** | 同上 | 中 |
| 客户集中度 | 未找到前五大客户明细 | — | 未找到 |

---

## 6. "谷草兼用"脆秆水稻种粮饲一体化技术

**产业事实**
- 2021-10：中科院合肥物质科学研究院与荃银高科举行"谷草兼用"脆秆水稻关键基因及技术**独家转让**签约暨示范活动（科技部 ncsti 2021-10-27 https://www.ncsti.gov.cn/kjdt/kjrd/202110/t20211027_49997.html ；高）。
- 双方共建脆秆水稻生产示范区，联合开展脆秆种质资源及重要基因的饲用应用研究，"解决脆秆水稻谷草兼用产业化关键问题"（投资者关系记录表 2023-10-10 https://pdf.dfcfw.com/pdf/H2_AN202310101601126822_1.pdf ；高）。
- 2024：该技术入选农业农村部 2024 年农业"火花技术"成果库（种业商务网 2024-08 https://www.chinaseed114.com/news/27/news_133543.html ；中）。
- 示范面积、品种审定名、饲用销售收入：**未找到**。

**科学背景（学术检索，供论文引用）**
- 合肥研究院团队用重离子束诱变获得脆秆突变体：Jiang H. et al. 2020（bc17，武运粳 7 号重离子辐照，纤维素 -22.7%、半纤维素 +45.76%，单隐性核基因，定位于 7 号染色体 162 kb）；吴跃进 2012（bc9311-1，离子束辐照 9311，定位 1 号染色体）。
- 饲用价值证据：Su et al. 2012（OsCesA4 突变脆秆稻秸秆有效降解率 DM 31.4% vs 26.7%）；Phonkompaeng et al. 2025（脆秆稻秸秆替代 25% 百慕大草饲喂荷斯坦牛，DM/CP 消化率提升）；Sawasdee et al. 2024（IR64 脆秆系 CesA7 突变，育成抗病脆秆品种用于反刍动物饲喂）；杨长杰 2011（中国奶牛，脆秆稻 NDF/ADF 瘤胃降解率显著提高）。
- 倒伏/产量权衡：Feng et al. 2013 报告 10 个脆秆突变体单株穗重不变、有效穗增加、生物量提高且抗倒伏更强；Zhao et al. 2025 *JIPB* 与 Gao et al. 2026 *PCE* 指出传统脆秆突变体多伴随不利表型、难以直接用于生产——这正是"脆而不倒"基因转让的技术意义所在。
- 详细条目见第 14 节。

---

## 7. 争议：界面新闻《"种粮一体化"外衣下的资本疑云》（2026-02-28）及监管链条

### 7.1 界面新闻核心指控
- 原文：https://www.jiemian.com/article/14045116.html （转载：搜狐 https://www.sohu.com/a/991121870_313745 、网易 https://www.163.com/dy/article/KMSSCMSK0534A4SC.html 、腾讯 https://view.inews.qq.com/a/20260228A07I8S00 、新浪 https://finance.sina.com.cn/jjxw/2026-02-28/doc-inhpktnn6892613.shtml ）
- 要点（置信度高，均为摘要直接引述）：
  1. 2024 年营收 +14.77% 至 47.09 亿，归母净利 -58.23% 至 1.14 亿；2025 前三季营收 -5.9%，亏损 1.8 亿，销售净利率 -13.18%；毛利率十年间从 40% 高位跌至不足 12%。
  2. 订单粮食 2025H1 占比由年初 25.3% 升至 44.54%、规模 6.43 亿、毛利率 -0.09%；"低毛利甚至负毛利业务的急速扩张……营造了'种粮一体化'的产业假象，实际上在持续侵蚀公司的利润根基"。
  3. 25 家子公司及关联企业、业务多元（种业、粮油贸易、生物科技、棉花种植），"便于隐蔽资金流动"。
  4. 四川荃银生物 2023 年向古蔺、仁怀、赤水三家酒厂销售高粱和小麦，年末确认应收 3,277.59 万元；毕马威函证无回函或金额不符、物流单据缺失、无法实地走访；2024 年荃银生物与酒厂及贵州某公司签债权转让协议，但母公司未将应收重分类、未单项计提。
  5. 2024 年母公司报表"其他应收款"12.92 亿（+68%），合并报表仅 0.61 亿，差额 12.31 亿——文章将其解读为资金流向子公司的"疑云"。
- **公司回应/澄清公告：未找到**（检索词 #19）。**交易所针对该报道的关注函/问询函：未找到**（检索词 #13）。

### 7.2 审计保留意见（2025-04-30）
- 毕马威华振对 2024 年度报表出具保留意见；保留事项涉及荃银生物与三家酒厂酒粮销售相关应收账款、与贵州某公司的其他应收款，以及部分存货账面价值审计范围受限（董事会专项说明 http://static.cninfo.com.cn/finalpage/2025-04-30/1223414132.PDF ；每经 https://www.nbd.com.cn/articles/2025-04-30/3862483.html ；证券时报 https://www.stcn.com/article/detail/1765879.html ；高）。

### 7.3 证监会立案 → 处罚 → ST
- 2026-01-30 收到《立案告知书》（新浪 https://finance.sina.com.cn/jjxw/2026-01-30/doc-inhkazcf0485362.shtml ；界面 https://m.jiemian.com/article/13961286_uc.html ）；同日业绩预告 2025 年亏损 1.8–2.7 亿，归因于"种子行业高库存、同质化竞争加剧及自然灾害"。
- 违规事实：2024 年报未如实反映荃银生物与贵州某公司债权债务关系，知悉信用风险仍未单项计提，少计提信用减值损失 **1,871.51 万元**，虚增利润总额 1,871.51 万元，占当期披露利润总额 **10.86%**（财联社 https://www.cls.cn/detail/2410692 ；高）。
- 处罚：公司警告+罚款 300 万；时任董事长应敏杰 150 万；时任副董事长兼总经理张琴 150 万；时任董秘兼财务总监张庆一 130 万，合计 **730 万元**（中证网 2026-06-29 https://www.cs.com.cn/ssgs/01/2026/06/29/detail_2026062910021106.html ；新浪 2026-07-01 https://finance.sina.com.cn/wm/2026-07-01/doc-inifhmhu4291741.shtml ；高）。
- ST：2026-06-29 停牌一天，6-30 起实施其他风险警示，简称"ST荃银"（证券时报 https://www.stcn.com/article/detail/3983540.html ）；证监会认定不触及重大违法强制退市（财闻网 https://www.caiwennews.com/article/1512776.shtml ；中）。
- 2025 年报审计意见恢复为标准无保留（GitHub 笔记；中）。

### 7.4 治理背景：中种集团要约收购与同业竞争
- 2025-11-20：中种集团拟部分要约收购 1.89 亿股（20%），11.85 元/股（较 10.16 元溢价 16.63%），资金 ≤22.45 亿元；完成后最多持股 3.84 亿股（40.51%）（上证报 https://paper.cnstock.com/html/2025-11/21/content_2148635.htm ；新浪 https://finance.sina.com.cn/jjxw/2025-11-21/doc-infyeesh7066966.shtml ；高）。
- 承诺自前次权益变动起 5 年内以资产重组、业务调整、委托管理、设立合资公司等方式解决境内水稻/小麦种子同业竞争（腾讯 https://news.qq.com/rain/a/20251121A01OWL00 ；高）。
- 2026-01-14 受托管理中种农科 100% 股权（中）。
- 董事会关于要约收购致全体股东报告书 2025-12-22：https://file.finance.qq.com/finance/hs/pdf/2025/12/22/1224891538.PDF

---

## 8. 分析师与第三方对该模式的评价

| 来源 | 时间 | 观点 | 置信度 |
|---|---|---|---|
| 天风证券深度《荃银高科》 | 2020-12-10 | "订单粮食业务自 19 年开展以来迅速发展"（正面：拉动种子销售） https://pdf.dfcfw.com/pdf/H3_AP202012111439137324_1.pdf | 中 |
| 每经 | 2023-02-17 | "订单农业拉动种子销售……不仅拉动了种子的销售，还增加了粮食贸易收入，促使近年来业绩快速增长" https://www.nbd.com.cn/articles/2023-02-17/2674072.html | 高 |
| 东亚前海深度《周期与成长共振，未来发展可期》 | 日期未取 | 标题级信息，正文未抓取 https://m.cls.cn/detail/831200 | 低 |
| 国信证券 | 2025-05-06 | 评级"优于大市"；2025Q1 营收 8.35 亿（+24.13%）"主要得益于订单粮食及出口业务收入增长" https://pdf.dfcfw.com/pdf/H3_AP202505061668417051_1.pdf | 中 |
| 天风证券半年报/季报点评 | 2024-08-27 / 2024-10-26 | 链接命中，内容未抓取 https://pdf.dfcfw.com/pdf/H3_AP202408281639505371_1.pdf ；https://pdf.dfcfw.com/pdf/H3_AP202410271640528018_1.pdf | 低 |
| 新浪"鹰眼预警" | 2025-05-01 | 营业收入与净利润变动背离 https://finance.sina.com.cn/stock/yyyj/2025-05-01/doc-ineuypas6796530.shtml | 中 |
| 界面新闻 | 2026-02-28 | 负面（见第 7 节） | 高 |
| 农资与市场《19问荃银高科！内卷承压下如何稳销量、稳市占》 | 2026 | 公司答投资者问，涉及 "66香"、产业一体化营销 https://www.enongzi.com/news/details?id=8c6eccf9-8f90-4eee-b884-9c3e61451324 | 中 |
| GitHub 第三方研究笔记（chess99/trading-os，2026-07-19） | 2026-07-19 | "订单粮食、青贮饲料收入 11.82 亿元但毛利率低，是报表质量拖累项"；"订单粮食等非核心业务应收缩或提升周转，否则继续稀释 ROE"；核心种业 P/S 估值时"订单粮食不应给高倍数" | 低（非官方） |
| 东方财富财富号（多篇，2026-04/05） | 2026 | 声称 2026Q1 毛利率回升至 19.93%、目标修复至 25% 以上、"三年打造三个大单品" | 低（自媒体） |

学术评价：Xie et al. (2023) 以荃银为例说明种企主导订单农业"获得质量优势并通过快速响应外部需求变化、协调内部技术能力改善利润"，并记录其订单业务占比与毛利率 2018→2021 双升——**该结论的数据窗口止于 2021 年，未覆盖 2023 年以后毛利率转负的阶段**，这是论文可以指出的文献缺口。

---

## 9. 海外业务

| 事实 | 来源 | 置信度 |
|---|---|---|
| 出口覆盖东南亚、南亚、非洲；国外分支机构 4 家；出口覆盖 20 多个国家与地区 | 安徽省政府新闻办 2023-04-12 http://fbh.anhuinews.com/tjcfd/cxah/202304/t20230412_6791628.html | 高 |
| 2023 年出口各类农作物种子 1,108.35 万公斤（+32.95%），海外收入占营收 6.96% | 界面 https://m.jiemian.com/article/10954149.html ；2023 年报摘要 | 高 |
| 2024 年业务覆盖东南亚、南亚、中亚及非洲 30 多个国家与地区；拓展哈萨克斯坦、乌兹别克斯坦等中亚市场 | 百度百科/公司官网转述 https://www.winallseed.com/ | 中 |
| 巴基斯坦、孟加拉国、菲律宾三大杂交稻市场占有率领先；首批中国农业对外合作百强企业；世界银行非洲扶贫项目种子供应商 | 公司官网"荃银风采" http://www.winallseed.com/list/71.html | 中（企业自述） |
| 2023H1 营收 14.11 亿，"出口海外表现不俗" | 证券时报 2023-08 https://stcn.com/article/detail/1298622.html | 中 |
| 2024/2025 海外收入绝对值、合资公司名单、"安徽荃银海外基地"细节 | **未找到**（配额耗尽前未能检索） | 未找到 |
| 2026 年海外"战略深化与项目延期" | 东方财富财富号 2026-04-14 | 低 |

---

## 10. 种子营销渠道与"荃银"品牌

- 品牌：主推杂交水稻品种（"荃优"系列等，具体品种名未在本次检索中确认）；订单模式中"优先采购荃银品种产出的农产品"是品牌—品种—粮食的绑定机制（年报；高）。
- 2026 新举措："66香"品牌，联合米厂、烘干厂打造产业一体化营销模式，"增强客户粘性、保障品种推广规模"（农资与市场 19 问；东方财富财富号；中）。"三年打造三个大单品"（财富号引 2026-04-29 公告；低）。
- 渠道数据（经销商数量、直销/经销比例、线上渠道）：**未找到**。

---

## 11. 2026 年经营计划与产品结构调整

- 六大目标："抓党建、明战略、强研发、提经营、优管理、促协同"（财富号转述 2025 年报"2026 年经营计划"；低-中）。
- 产品结构：聚焦差异化优势品种、高附加值品种（高产、抗逆、特优质），提升溢价能力；种子业务收入占比提升（2026Q1 种子 +11.74%、订单 -37.28%）；GitHub 笔记称 2026Q1 毛利率修复，财富号称 19.93%（低）。
- 同业竞争整合：受托管理中种农科（水稻、小麦）（中）。
- 官方年报"2026 年经营计划"原文：**未直接抓取**（PDF 被拦截）。

---

## 12. 同行对照：订单农业 / 种粮一体化模式

| 企业 | 检索到的证据 | 规模/数字 | 来源 | 置信度 |
|---|---|---|---|---|
| 隆平高科 | Xie et al. 2023：与荃银并列为"种企主导订单农业"的代表；表 3 列出其下游加工商（国穗、稻香、新禾、腾宏、瑞丰、金沙河面业等）及高于市场价 0.011–0.04 美元/kg 的收购溢价；表 2：注册资本 1.83 亿美元、2021 销售 4.89 亿美元，作物玉米、水稻 | 订单业务收入/占比：未找到 | https://doi.org/10.1002/agr.21823 | 高（学术） |
| 中农发种业（农发种业，600313） | Xie et al. 表 2 列为实施种企主导订单农业的企业：注册资本 1.5 亿美元、2021 销售 5.26 亿美元，作物玉米、水稻、专用小麦、谷子、高粱（规模最大） | 2026Q1 营收 16.53 亿、归母净利 1,897 万（GitHub 笔记，低） | 同上 | 高/低 |
| 丰乐种业 | 表 2：注册资本 0.85 亿美元、2021 销售 3.66 亿美元，芝麻、棉花 | — | 同上 | 高 |
| 敦煌种业 | 表 2：0.73 亿美元、1.29 亿美元，小麦 | — | 同上 | 高 |
| 大北农 | 表 2：注册资本 5.83 亿美元、2021 种业销售 0.78 亿美元，转基因玉米和大豆；未见其"种粮一体化"订单粮食业务证据 | — | 同上 | 高 |
| 中种集团（荃银控股股东，中化系） | 未检索到其订单农业规模；与荃银在境内水稻、小麦存在同业竞争，5 年内整合 | — | 上证报 2025-11-21 | 中 |
| 垦丰种业（北大荒集团） | **未找到**（配额耗尽前未检索） | — | — | 未找到 |
| 登海种业 | Xie et al. 表 2 未列入；GitHub 笔记：2025 营收 11.02 亿、归母净利 9,165 万，"表现更稳但体量较小"；未见订单农业业务 | — | GitHub 笔记（低） | 低 |
| 隆平高科 2026Q1 | 收入 -35.56%、亏损 1.31 亿（GitHub 笔记引券商摘要 https://pdf.dfcfw.com/pdf/H3_AP202604211821362286_1.pdf ） | — | 低 | 低 |

**对比要点（供论文）**：（1）在 Xie et al. 的 6 家样本中，荃银是唯一将订单业务做到营收占比 >25% 且后期毛利转负的企业；（2）隆平高科的订单农业以"加工商溢价收购"为特征、公司本身不大规模持有粮食贸易收入（据表 3 推断，低）；（3）垦丰/登海/大北农的公开证据不足，需后续补检索 2024–2025 年报"分产品"表。

---

## 13. 与理论框架的对接（供第 2 阶段凝炼主题）

- 治理结构：Xie et al. 引 Williamson (1985) 的三种治理结构（纵向一体化/现货市场/混合形态），订单农业属"混合形态"，将生产风险外部化给种植者并控制供给与质量；荃银模式的特殊之处是种企同时承担粮食贸易的存货与应收风险，导致混合形态向"准纵向一体化"漂移，但缺乏加工端利润。
- 农业上市公司"背农"与多元化：刘晓云等（2013）发现农业上市公司扩展新业务有助于规避风险、促进收入增长；邵桂荣（2007）则发现非农经营整体拖累绩效；王瑜、綦好东（2014）发现纵向农工一体化企业 ROE、总资产周转率高于非一体化企业。荃银 2019–2025 的轨迹（收入扩张—毛利转负—ROE -11.63%）为这两派结论提供了一个时间序列上的反例/检验案例。
- 供应链金融：Yi, Wang & Chen (2021, *POM*) 与 Luo et al. (2021, *Complexity*) 的"平台/核心企业担保融资"模型，可用于解释"种业贷 + 产业互联网平台"的设计逻辑；Wang, Zhang & Bai (2026, *J. Econ. Surveys*) 系统综述指出此类平台金融的风险在于"不可持续的商业模式"。

---

## 14. 文献条目（格式：作者. 年份. 标题. 期刊, 卷(期): 页. DOI. 工具）

**A. 种企主导订单农业 / 合同农业（中国）**
1. Xie, Z., Yuan, S., Zhu, J., & Li, W. 2023. Contract farming led by a seed enterprise and incentives to produce high quality: Which contract design performs best? *Agribusiness*, 39(4): 1173–1198. DOI: 10.1002/agr.21823. [Scholar Gateway] —— 直接以荃银高科、隆平高科为案例；含 2018/2021 荃银订单业务占比与毛利率。
2. Zhang, Q. F. 2012. The political economy of contract farming in China's agrarian transition. *Journal of Agrarian Change*, 12(4): 460–483. DOI: 10.1111/j.1471-0366.2012.00352.x. [Scholar Gateway]
3. Chen, J., & Chen, Y. 2021. The impact of contract farming on agricultural product supply in developing economies. *Production and Operations Management*, 30(8): 2395–2419. DOI: 10.1111/poms.13382. [Scholar Gateway]
4. Li, J., Qing, P., Hu, W., & Li, M. 2021. Contract farming, community effect, and farmer valuation of biofortified crop varieties in China: The case of high-zinc wheat. *Review of Development Economics*, 26(2): 1035–1055. DOI: 10.1111/rode.12847. [Scholar Gateway]
5. Peng, H., & Pang, T. 2019. Optimal strategies for a three-level contract-farming supply chain with subsidy. *International Journal of Production Economics*, 216: 274–286. DOI: 10.1016/j.ijpe.2019.06.011. [Undermind]（卷页据 DOI 常规著录，未经核对）
6. Liao, C., Lu, Q., & Lin, L. 2023. Coordinating a three-level contract farming supply chain with option contracts considering risk-averse farmer and retailer. *PLOS ONE*, 18(1): e0279115. DOI: 10.1371/journal.pone.0279115. [Undermind]
7. Shi, L., Pang, T., & Peng, H. 2022. Production and green technology investment strategy for contract-farming supply chain under yield insurance. *Journal of the Operational Research Society*, 74(1): 225–238. DOI: 10.1080/01605682.2022.2033141. [Undermind]
8. Liu, X., Shen, X., You, M., & Zhen, L. 2020. Study on coordination and optimization of contract farming supply chain based on uncertain conditions. *Scientific Programming*, 2020: 8858812. DOI: 10.1155/2020/8858812. [Scholar Gateway]
9. Hofman, I. 2024. Seeds of empire or seeds of friendship? The politics of the diffusion of Chinese cotton seeds in Tajikistan. *Journal of Agrarian Change*, 24(2). DOI: 10.1111/joac.12581. [Scholar Gateway]（中国种企海外订单农业失败案例：大禾种子塔吉克斯坦 2014）
10. Abdul-Rahaman, A., & Abdulai, A. 2019. Vertical coordination mechanisms and farm performance amongst smallholder rice farmers in northern Ghana. *Agribusiness*, 36(2): 259–280. DOI: 10.1002/agr.21628. [Scholar Gateway]

**B. 农业上市公司多元化 / 纵向一体化绩效（中文）**
11. 王瑜, 綦好东. 2014. 农工一体化企业价值链：纵向一体化收益与盈利模式重构——基于A股上市公司的分析. （期刊名未取）: 103–109. 无 DOI；Semantic Scholar: https://www.semanticscholar.org/paper/9bbe4385e0eb666b6867e15aecd09dd8c48f6e58 [Undermind]
12. 刘晓云, 应瑞瑶, 李明. 2013. 新业务、多元化与公司绩效——基于农业上市公司与非农业上市公司的比较. （期刊名未取）: 60–73. 无 DOI；https://www.semanticscholar.org/paper/fbe040774fca76c21d424c7fb019fdc58fbd2698 [Undermind]
13. Shao, G. (邵桂荣). 2007. Non-agricultural operations and the operation performance of the listed agricultural companies. *Journal of Finance and Economics*. 无 DOI；https://www.semanticscholar.org/paper/053d382c26309dcca69dcca2f9d5c5d9 [Undermind]（链接以 Undermind 返回为准：053d382c26309dcca2f9d5c5d9c3ec1bd8c0f1676ec7）
14. Zhang, X. (张学伟). 2012. The relationship between performance and non-core business of seed industry listed companies. *Economic Geography*. 无 DOI；https://www.semanticscholar.org/paper/986615adf947c9b06eb3dcacb71aa53a9e36f043 [Undermind]
15. Zhong, N., Cheng, Y., & Luo, Y. 2017. Growth Strategy of Win-All Hi-Tech Seed Co., Ltd. 复旦大学管理案例. DOI: 10.12156/FUDAN.CASE201200802. [Undermind]（荃银高科增长战略教学案例，摘要不可得）
16. Cao, H. (曹海亚). 2015. Research of the integration mode of seed enterprise in China based on the value chain. https://www.semanticscholar.org/paper/51c01e8686b02192203ffd22e1a92b885a21517f [Undermind]
17. Zhang, N. 2023. The development of Chinese seed industry: From company value chain upgrading perspective. *Frontiers in Business, Economics and Management*, 10(1). DOI: 10.54097/fbem.v10i1.9858. [Undermind]

**C. 供应链金融 / 平台金融**
18. Yi, Z., Wang, Y., & Chen, Y. 2021. Financing an agricultural supply chain with a capital-constrained smallholder farmer in developing economies. *Production and Operations Management*, 30(7): 2102–2121. DOI: 10.1111/poms.13357. [Scholar Gateway]
19. Luo, Y., Deng, T., Wei, Q., Xiao, G., Ling, Q., & Xin, B. 2021. Optimal financing decision in a contract food supply chain with capital constraint. *Complexity*, 2021: 8925102. DOI: 10.1155/2021/8925102. [Scholar Gateway]
20. Wang, H., Zhang, R., & Bai, X. 2026. How financial innovation shapes agricultural value chain development and resilience: A systematic literature review. *Journal of Economic Surveys*, online first. DOI: 10.1111/joes.70130. [Scholar Gateway]
21. Liu, L., Wang, Y., Teng, M., & Lu, C. 2025. The impact of agricultural digital transformation on income inequality: Evidence from rural China. *Agribusiness*, online first. DOI: 10.1002/agr.70049. [Scholar Gateway]

**D. 脆秆水稻谷草兼用**
22. Jiang, H., Ye, Y., He, D., Ren, Y., Yang, Y., Xie, J., … Liu, B. 2020. Identification and gene localization of a novel rice brittle culm mutant bc17. *Acta Agronomica Sinica*（作物学报）, 47(1)（2021 卷期）. DOI: 10.3724/SP.J.1006.2021.02025. [Undermind]（中科院合肥研究院，重离子诱变）
23. 吴跃进 (Wu, Y.-J.) 等. 2012. Characterizations and gene mapping of a brittle culm and leaf mutant in indica rice（bc9311-1，离子束诱变）. 无 DOI；https://www.semanticscholar.org/paper/afea22558a07fd9670db198b80c2a3377389cacd [Undermind]
24. Su, Y., Zhao, G., Wei, Z., Yan, C., & Liu, S. 2012. Mutation of cellulose synthase gene improves the nutritive value of rice straw. *Asian-Australasian Journal of Animal Sciences*, 25(6): 800–805. DOI: 10.5713/ajas.2011.11409. [Undermind]
25. Phonkompaeng, A., Boonchu, P., Sawasdee, A., Rangubhet, K., Kongmun, P., Dhital, B., Wang, C., & Chiang, H. 2025. Evaluation of brittle rice straw as a novel roughage resource for enhancing the performance of Holstein cows. *Animal Science Journal*, 96: e70091. DOI: 10.1111/asj.70091. [Scholar Gateway/Undermind]
26. Sawasdee, A., Tsai, T.-H., Liao, W., & Wang, C.-S. 2024. Identification of the CesA7 gene encodes brittleness mutation derived from IR64 variety and breeding for ruminant feeding. *Agriculture*, 14(5): 706. DOI: 10.3390/agriculture14050706. [Undermind]
27. Sawasdee, A., et al. 2024. Characterization of cell wall compositions of sodium azide-induced brittle mutant lines in IR64 variety and its potential application. *Plants*, 13(23): 3303. DOI: 10.3390/plants13233303. [Undermind]
28. Feng, Y.-Q., Zou, W.-H., Liu, F., … Peng, L. 2013. Studies on biological characterization of rice brittle culm mutants and their biomass degradation efficiency. *Journal of Agricultural Science and Technology*（中国农业科技导报）, 15: 77–83. 无 DOI [Undermind]
29. 杨长杰 (Yang, C.-J.). 2011. Study on rumen degradability characteristics of brittleness mutation rice by cows. *China Dairy Cattle*（中国奶牛）. 无 DOI [Undermind]
30. Zhang, B., & Zhou, Y. 2010. Rice brittleness mutants: A way to open the 'black box' of monocot cell wall biosynthesis. *Journal of Integrative Plant Biology*, 53(2): 136–142. DOI: 10.1111/j.1744-7909.2010.01011.x. [Scholar Gateway]
31. Zhang, M., Zhang, B., Qian, Q., Yu, Y., Li, R., Zhang, J., Liu, X., Zeng, D., Li, J., & Zhou, Y. 2010. Brittle Culm 12, a dual-targeting kinesin-4 protein, controls cell-cycle progression and wall properties in rice. *The Plant Journal*, 63(2): 312–328. DOI: 10.1111/j.1365-313X.2010.04238.x. [Scholar Gateway]
32. Duan, Z., Wang, J., Bai, L., Zhao, Z., & Chen, K. 2008. Anatomical and chemical alterations but not photosynthetic dynamics and apoplastic transport changes are involved in the brittleness culm mutation of rice. *Journal of Integrative Plant Biology*, 50(12): 1508–1517. DOI: 10.1111/j.1744-7909.2008.00718.x. [Scholar Gateway]
33. Zhao, Y., Wang, X., Gao, J., … Zhang, Z. 2025. The MYB61–STRONG2 module regulates culm diameter and lodging resistance in rice. *Journal of Integrative Plant Biology*, 67(2): 243–257. DOI: 10.1111/jipb.13830. [Scholar Gateway]
34. Gao, J., Zhao, Y., Zhao, Z., … Li, Z. 2026. Knockout of RRS1 enhances culm mechanical strength and grain yield in rice. *Plant, Cell & Environment*, 49(9): 6859–6872. DOI: 10.1111/pce.70661. [Scholar Gateway]
35. Cao, X., Zhou, T., Sun, Y., … Ni, J. 2024. Identification and gene cloning of a brittle culm mutant (bc22) in rice. *Agriculture*, 14(2): 235. DOI: 10.3390/agriculture14020235. [Undermind]
36. Rao, Y., Yang, Y., Xin, D., … Zeng, D. 2013. Characterization and cloning of a brittle culm mutant (bc88) in rice. *Chinese Science Bulletin*, 58: 3000–3006. DOI: 10.1007/s11434-013-5806-2. [Undermind]
37. Li, P., Liu, Y., Tan, W., … Cai, H. 2019. Brittle Culm 1 encodes a COBRA-like protein involved in secondary cell wall cellulose biosynthesis in sorghum. *Plant & Cell Physiology*, 60(4): 788–801. DOI: 10.1093/pcp/pcy246. [PubMed]（According to PubMed；高粱同源基因，间接）

---

## 15. 未找到 / 待补（Gaps）

1. 2026 年半年报（订单粮食收入、占比、毛利率、经营现金流）——预计 2026-08-29 前后披露，本次未命中。
2. 2021、2022 年报"分产品"表中的订单粮食收入与毛利率原文（现为推算）。
3. 2024 年报订单粮食单项毛利率原文（现由 2025 年报同比数推算 ≈2.66%）。
4. 订单种植面积（万亩）、分省份布局、订单品种审定名（含脆秆稻品种名）、脆秆稻示范面积与饲用销量。
5. 公司对界面新闻报道的回应/澄清公告；交易所针对订单粮食或母公司其他应收款 12.92 亿的关注函/问询函及回函。
6. 2025 年报"2026 年经营计划"原文；"66香"品牌 2026-04-29 公告原文；"三年三个大单品"品种名。
7. 海外：2024/2025 海外收入绝对值与占比、出口量；海外合资公司/子公司名单与所在国；"安徽荃银海外基地"。
8. 分析师研报正文：东亚前海深度、国信 2025-05-06、天风 2024 点评中对订单农业的具体评价与盈利预测拆分。
9. 张琴 2025-05-28 中证网专访中关于"种粮一体化"的原话。
10. 安徽省"5+8 种粮一体化"平台试点的政策文件（省农业农村厅）、平台 6000 户/40 亿元的统计时点。
11. 同行：垦丰种业、登海种业、大北农、中种集团 2023–2025 年报中是否存在订单粮食/粮食贸易分部及其收入、毛利率；隆平高科订单农业收入规模。
12. 荃银高科前五大客户、订单粮食应收账款账龄、存货中"订单粮食"余额。
13. 母公司其他应收款 12.92 亿的对象明细（子公司往来）。
14. 投资者索赔进展与预计负债。

---

## 16. 来源索引（52 项）

新闻/公告类：
1. https://www.jiemian.com/article/14045116.html （界面 2026-02-28）
2. https://www.sohu.com/a/991121870_313745
3. https://www.163.com/dy/article/KMSSCMSK0534A4SC.html
4. https://view.inews.qq.com/a/20260228A07I8S00
5. https://finance.sina.com.cn/jjxw/2026-02-28/doc-inhpktnn6892613.shtml
6. https://www.jiemian.com/article/5711493.html （界面 2021，2020 年报）
7. https://m.jiemian.com/article/10954149.html （界面 2024，2023 海外）
8. https://m.jiemian.com/article/13961286_uc.html （界面 2026-01-30 立案）
9. https://www.nbd.com.cn/articles/2023-02-17/2674072.html
10. https://www.nbd.com.cn/articles/2025-04-30/3862483.html
11. https://news.qq.com/rain/a/20250430A02JBQ00
12. https://news.qq.com/rain/a/20251030A03WUP00
13. https://news.qq.com/rain/a/20251121A01OWL00
14. https://www.stcn.com/article/detail/1741882.html
15. https://www.stcn.com/article/detail/1765879.html
16. https://www.stcn.com/article/detail/3983540.html
17. https://stcn.com/article/detail/1298622.html
18. https://www.cls.cn/detail/2410692
19. https://www.cs.com.cn/ssgs/01/2026/06/29/detail_2026062910021106.html
20. https://www.cs.com.cn/ssgs/gsxw/202505/t20250528_6493796.html
21. https://finance.sina.com.cn/wm/2026-07-01/doc-inifhmhu4291741.shtml
22. https://finance.sina.com.cn/jjxw/2026-01-30/doc-inhkazcf0485362.shtml
23. https://finance.sina.com.cn/jjxw/2025-11-21/doc-infyeesh7066966.shtml
24. https://finance.sina.com.cn/stock/aigc/stockfs/2026-04-25/doc-inhvrtiq7652602.shtml
25. https://finance.sina.com.cn/stock/yyyj/2025-05-01/doc-ineuypas6796530.shtml
26. https://paper.cnstock.com/html/2025-11/21/content_2148635.htm
27. https://www.21jingji.com/article/20230809/herald/b955bbb1419a679d269ca5ef3657fcfa.html
28. https://finance.cnr.cn/jjgd/20230610/t20230610_526282666.shtml
29. http://paper.ce.cn/pad/content/202307/05/content_276902.html
30. http://www.news.cn/money/20250227/b00ced75781e444db9f7e9e53ec1bd8c/c.html
31. https://app.xinhuanet.com/news/article.html?articleId=f29d068672df3569d532ee8204900605
32. https://www.cebnet.com.cn/20230810/102899846.html
33. https://www.ncsti.gov.cn/kjdt/kjrd/202110/t20211027_49997.html
34. https://www.chinaseed114.com/news/27/news_133543.html
35. https://www.enongzi.com/news/details?id=8c6eccf9-8f90-4eee-b884-9c3e61451324
36. http://fbh.anhuinews.com/tjcfd/cxah/202304/t20230412_6791628.html
37. http://www.winallseed.com/list/71.html
38. https://www.thepaper.cn/newsDetail_forward_26794590
39. https://stock.stockstar.com/RB2024032400000208.shtml
40. https://www.caiwennews.com/article/1512776.shtml

公告/研报 PDF：
41. https://static.cninfo.com.cn/finalpage/2026-04-25/1225192807.PDF （2025 年报）
42. http://static.cninfo.com.cn/finalpage/2025-08-28/1224594091.PDF （2025 半年报）
43. http://static.cninfo.com.cn/finalpage/2025-10-30/1224760510.PDF （2025 三季报）
44. http://static.cninfo.com.cn/finalpage/2025-04-30/1223414132.PDF （保留意见专项说明）
45. http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2024/2024-3/2024-03-23/9892532.PDF （2023 年报）
46. http://static.cninfo.com.cn/finalpage/2024-03-27/1219429418.PDF ；https://file.finance.qq.com/finance/hs/pdf/2024/08/27/1221007812.PDF ；https://pdf.dfcfw.com/pdf/H2_AN202310101601126822_1.pdf （投资者关系记录表 ×3）
47. https://pdf.dfcfw.com/pdf/H3_AP202012111439137324_1.pdf （天风 2020-12-10）；https://pdf.dfcfw.com/pdf/H3_AP202505061668417051_1.pdf （国信 2025-05-06）；https://m.cls.cn/detail/831200 （东亚前海）
48. https://file.finance.qq.com/finance/hs/pdf/2025/12/22/1224891538.PDF （要约收购报告书）
49. https://m.10jqka.com.cn/sn/20220328/35103085.shtml （2021 年报）

GitHub 镜像：
50. https://raw.githubusercontent.com/chess99/trading-os/082cb5a3d5c7f2c3ddc2058f5728bcc1d3c5fff9/research/companies/CN/300087/legacy/2026-07-19.md （第三方研究笔记，含 2025 年报分部、2026-07-09 处罚决定书）
51. https://github.com/BilalBAI/tyc-core-aaoifi-results（2020/XSHE/300087_XSHE_2020.json，2020H1 分部）
52. https://github.com/peter678007/json01（sina_news_txt/daily/2020-07-14.txt，2020H1 业绩预告快讯）

学术：见第 14 节 37 条（Scholar Gateway、Undermind、PubMed）。
