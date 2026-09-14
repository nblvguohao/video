# evidence/data — 数据集说明

## national_rice_varieties_raw.csv
- 来源：GitHub 公开仓库 `he-zhui/Rice_QA`（`jw/qa_data.json`，52,247 条问答对，字段 `source = rice_extracted_fields.csv`），由本项目脚本按 `row_index × field_name` 还原为品种级表（7,883 行）。
- 内容：水稻品种审定公告原文字段（品种名称、品种来源、特征特性、产量表现、审定编号、选育/申请单位、栽培技术要点、适宜区域），覆盖国审与多省省审，审定年份 1999–2025（2023–2025 覆盖稀疏）。
- 一手来源：农业农村部（原农业部）国家农作物品种审定公告及各省审定公告；GitHub 仓库仅为汇编与获取途径。仓库未附许可证；论文中以官方公告为数据来源并注明汇编途径。
- 获取方式：`git clone --depth 1 https://github.com/he-zhui/Rice_QA`（2026-09-14）。

## national_rice_parsed.csv（由 scripts/parse_variety_texts.py 生成）
- 用正则从公告文本抽取：审定编号/年份/级别、类型（籼粳、两系/三系）、区试组别、两年区试平均亩产与增产%、对照、生产试验产量、全生育期、株高、有效穗、穗粒数、结实率、千粒重、稻瘟病综合指数与损失率最高级、白叶枯/褐飞虱等级、米质指标（整精米率、垩白度、直链淀粉、胶稠度、长宽比）与米质等级、是否荃银关联（品种来源/选育单位/申请者含“荃银”）。
- 无任何插补；字段覆盖率见 national_rice_parsed.report.md。
- 已知局限：稻瘟病综合指数仅部分公告给出；米质等级表述多样，需人工抽检；2023–2025 品种需用 WebSearch 从公告补充。
