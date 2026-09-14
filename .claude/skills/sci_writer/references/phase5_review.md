# Phase 5 详解：投稿前审查

## 四条并行审查线

1. **多视角审稿人**（建议 3 位，视角互不重叠，例如"技术严谨性与数据可信度"、"原创性与是否像宣传/理论贡献"、"可读性与期刊契合度"）。输出结构参考 `nature-reviewer` 技能：Overall assessment / Major strengths / Major concerns（具体到章节与句子）/ Technical failings that must be addressed / Assessment against journal criteria / Recommendation。只依据稿件与仓库证据评审，不得虚构实验、引用或审稿人身份。

2. **格式合规审查**：逐条对照 `04_format_spec.md` 检查标题长度、摘要字数与结构、关键词数、Highlights、章节命名与顺序、图表编号与首次引用顺序、单位与数字格式、缩写定义、声明部分是否齐全、参考文献格式与文内引用一致性、字数上限。产出逐条检查表（条目/要求/现状/是否合规/修正建议）。

3. **数字一致性审查**：提取正文中全部数字型陈述（含摘要、正文、图题表题），逐条与结果文件/表格/证据索引对照（必要时重算），检查摘要与结论中的数字是否与结果节一致、同一数字在不同位置是否一致、图中数据是否与表一致。产出清单（位置/陈述/出处/是否一致/修正）。

4. **参考文献多源核验**：借用 `nature-ref-verifier` 的方法——对每条文献用至少两个独立来源核实，逐字段比对，按严重程度分级（Critical/Warning/Info），给出 Verified/Check suggested/Needs fix/Unverifiable 的综合判定；同时检查正文引用与文献列表的一一对应。

## 修订

一位"修订负责人"通读全部四条审查线的报告，逐条落实（无法落实的意见要在响应文档里逐点说明理由，不能沉默跳过），不得在修订过程中引入新的未核实数字或文献，写详细的变更日志（意见→修改位置→修改内容），确保这是可追溯的。

## 终审校对（历史版本一致性）

- 用 diff 比对修订前后版本，确认改动与变更日志一致、没有意外的删改。
- 确认四条审查线提出的问题全部关闭（或在响应文档里有明确的不修改理由）。
- 检查语言：去除 AI 腔、句长控制、术语前后一致。
- 运行构建脚本生成投稿格式的 DOCX/PDF（见下），并**实际打开生成的文件抽查排版**（图片是否正确嵌入、表格是否错位、页码是否正常）——不要假设脚本跑完没报错就等于排版正确。

## 构建投稿文件

用本技能自带的 `scripts/build_docx.py` 与 `scripts/build_pdf.py`：

```bash
python3 build_docx.py manuscript_v2.md submission/manuscript.docx --pdf --line-numbers
# 如果容器里没有可用的 LibreOffice（很常见），--pdf 会自动跳过转换并提示改用：
python3 build_pdf.py manuscript_v2.md submission/manuscript.pdf
```

`build_pdf.py` 不依赖 LibreOffice，用 PyMuPDF 的 Story 排版引擎直接渲染，在容器环境里更可靠。两个脚本都支持 Markdown 的标题、段落、粗斜体、上下标、行内代码、图片+图注、表格、列表；图片路径按相对路径在项目根目录/manuscript 目录下解析。

## 投稿包

`submission/`：cover_letter.md（致编辑，说明贡献、契合度、无重复投稿、利益冲突声明）、highlights.md（若期刊要求）、declarations.md（数据可用性/利益冲突/作者贡献/资助/致谢/AI 工具使用声明占位）、submission_checklist.md（对照期刊清单逐项打勾，未完成项标注需作者补充的内容如单位/ORCID/资助号）、figure_captions.md 与 tables.md（若期刊要求单独提供）、VERSION_HISTORY.md（版本差异摘要、各审查报告索引、对应的 git 提交）。
