// 生成投稿用 docx：node build.js [refs-file] [out-file]
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, AlignmentType,
  BorderStyle, ImageRun, Footer, PageNumber, VerticalAlign, HeightRule, TabStopType,
} = require('docx');

const C = require('./content.js');
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json'), 'utf8'));
const REFS = require(path.resolve(process.argv[2] || './refs.js'));
const OUT = process.argv[3] || 'manuscript.docx';

// ---------- 字体与字号 ----------
const F_SONG = { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: '宋体', cs: 'Times New Roman' };
const F_HEI = { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: '黑体', cs: 'Times New Roman' };
const F_KAI = { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: '楷体', cs: 'Times New Roman' };
const F_TNR = { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: '宋体', cs: 'Times New Roman' };
const SZ = { xiaoer: 36, sanhao: 32, sihao: 28, xiaosi: 24, wuhao: 21, xiaowu: 18, liuhao: 15 };
const BLACK = '000000';

// ---------- 引用编号 ----------
const refIndex = new Map(); // key -> number
const refOrder = [];
function citeNumbers(keys) {
  const nums = keys.map(k => {
    const key = k.trim();
    if (!REFS.find(r => r.key === key)) throw new Error('未知文献键: ' + key);
    if (!refIndex.has(key)) { refIndex.set(key, refOrder.length + 1); refOrder.push(key); }
    return refIndex.get(key);
  });
  const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
  // 连续分组：[1-3,5]
  const parts = []; let i = 0;
  while (i < uniq.length) {
    let j = i; while (j + 1 < uniq.length && uniq[j + 1] === uniq[j] + 1) j++;
    if (j - i >= 1) parts.push(`${uniq[i]}-${uniq[j]}`);
    else for (let k = i; k <= j; k++) parts.push(String(uniq[k]));
    i = j + 1;
  }
  return '[' + parts.join(',') + ']';
}

// ---------- 行内标记解析 ----------
const TOKEN = /(\^\{[^}]*\}|_\{[^}]*\}|\*\{[^}]*\}|【[^】]*】|\[\[[^\]]*\]\])/g;
function runs(text, base) {
  const out = [];
  text = String(text).replace(/"([^"]*)"/g, '“$1”');
  text = text.replace(/－/g, '−');   // 全角连接号 -> 数学减号
  let last = 0; let m;
  const push = (t, extra) => { if (t) out.push(new TextRun(Object.assign({ text: t, font: base.font, size: base.size, bold: base.bold, italics: base.italics, color: BLACK }, extra || {}))); };
  while ((m = TOKEN.exec(text)) !== null) {
    push(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('^{')) push(tok.slice(2, -1), { superScript: true });
    else if (tok.startsWith('_{')) push(tok.slice(2, -1), { subScript: true });
    else if (tok.startsWith('*{')) push(tok.slice(2, -1), { italics: true });
    else if (tok.startsWith('【')) push(tok, { highlight: 'yellow' });
    else if (tok.startsWith('[[')) push(citeNumbers(tok.slice(2, -2).split(',')), { superScript: true });
    last = m.index + tok.length;
  }
  push(text.slice(last));
  return out;
}

// ---------- 段落工厂 ----------
const P = (text, o = {}) => new Paragraph(Object.assign({
  children: runs(text, { font: o.font || F_SONG, size: o.size || SZ.wuhao, bold: o.bold, italics: o.italics }),
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: Object.assign({ line: 360, lineRule: 'auto', before: 0, after: 0 }, o.spacing || {}),
  indent: o.indent === undefined ? { firstLine: 420 } : o.indent,
  keepNext: o.keepNext, keepLines: o.keepLines,
}, o.para || {}));

const body = [];
// 标题区
body.push(P(C.titleCN, { font: F_HEI, size: SZ.xiaoer, align: AlignmentType.CENTER, indent: {}, spacing: { before: 120, after: 200, line: 360 } }));
body.push(P(C.authorsCN, { font: F_KAI, size: SZ.xiaosi, align: AlignmentType.CENTER, indent: {}, spacing: { after: 60 } }));
body.push(P(C.affilCN, { font: F_SONG, size: SZ.xiaowu, align: AlignmentType.CENTER, indent: {}, spacing: { after: 160 } }));
// 摘要
body.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { line: 300, lineRule: 'auto', after: 40 }, children: [
  ...runs('摘要　', { font: F_HEI, size: SZ.xiaowu }), ...runs(C.abstractCN, { font: F_SONG, size: SZ.xiaowu })] }));
body.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { line: 300, lineRule: 'auto', after: 40 }, children: [
  ...runs('关键词　', { font: F_HEI, size: SZ.xiaowu }), ...runs(C.keywordsCN, { font: F_SONG, size: SZ.xiaowu })] }));
body.push(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { line: 300, lineRule: 'auto', after: 200 }, children: [
  ...runs('中图分类号　', { font: F_HEI, size: SZ.xiaowu }), ...runs(C.clc + '　　', { font: F_SONG, size: SZ.xiaowu }),
  ...runs('文献标识码　', { font: F_HEI, size: SZ.xiaowu }), ...runs(C.docCode, { font: F_SONG, size: SZ.xiaowu })] }));
// 英文
body.push(P(C.titleEN, { font: F_TNR, size: SZ.xiaosi, bold: true, align: AlignmentType.CENTER, indent: {}, spacing: { after: 80, line: 300 } }));
body.push(P(C.authorsEN, { font: F_TNR, size: SZ.xiaowu, align: AlignmentType.CENTER, indent: {}, spacing: { after: 40, line: 300 } }));
body.push(P(C.affilEN, { font: F_TNR, size: SZ.xiaowu, align: AlignmentType.CENTER, indent: {}, spacing: { after: 120, line: 300 } }));
body.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { line: 300, lineRule: 'auto', after: 40 }, children: [
  ...runs('Abstract　', { font: F_TNR, size: SZ.xiaowu, bold: true }), ...runs(C.abstractEN, { font: F_TNR, size: SZ.xiaowu })] }));
body.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { line: 300, lineRule: 'auto', after: 240 }, children: [
  ...runs('Key words　', { font: F_TNR, size: SZ.xiaowu, bold: true }), ...runs(C.keywordsEN, { font: F_TNR, size: SZ.xiaowu })] }));

// ---------- 表格 ----------
const TEXT_W = 11906 - 2 * 1700; // A4 宽 − 左右页边距
function cellRuns(text, opts = {}) {
  return runs(String(text), { font: F_SONG, size: SZ.xiaowu, bold: opts.bold });
}
function threeLineTable(header, rows, widths, opts = {}) {
  // header: array of rows; 单元格可为字符串或 {t, cs, rs}，{gap:n} 表示被上行 rowSpan 占用的列
  const total = widths.reduce((a, b) => a + b, 0);
  const cw = widths.map(w => Math.round(w / total * TEXT_W));
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  const thick = { style: BorderStyle.SINGLE, size: 12, color: BLACK };
  const thin = { style: BorderStyle.SINGLE, size: 6, color: BLACK };
  const nHead = header.length; const nAll = nHead + rows.length;
  const mk = (cells, ri) => {
    let col = 0; const children = [];
    for (const raw of cells) {
      const c = (typeof raw === 'object' && raw !== null) ? raw : { t: raw };
      if (c.gap) { col += c.gap; continue; }
      const cs = c.cs || 1, rs = c.rs || 1;
      const width = cw.slice(col, col + cs).reduce((a, b) => a + b, 0);
      const lastRowOfCell = ri + rs - 1;
      children.push(new TableCell({
        width: { size: width, type: WidthType.DXA },
        columnSpan: cs > 1 ? cs : undefined, rowSpan: rs > 1 ? rs : undefined,
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 20, bottom: 20, left: 40, right: 40 },
        borders: { left: none, right: none,
          top: ri === 0 ? thick : none,
          bottom: lastRowOfCell === nHead - 1 ? thin : (lastRowOfCell === nAll - 1 ? thick : none) },
        children: [new Paragraph({ alignment: (opts.leftCols || []).includes(col) ? AlignmentType.LEFT : AlignmentType.CENTER,
          keepNext: ri < nAll - 1, keepLines: true,
          spacing: { line: 240, lineRule: 'auto', before: 0, after: 0 }, children: cellRuns(c.t) })],
      }));
      col += cs;
    }
    return new TableRow({ cantSplit: true, tableHeader: ri < nHead, children });
  };
  const allRows = [...header.map((h, i) => mk(h, i)), ...rows.map((r, i) => mk(r, nHead + i))];
  return new Table({ rows: allRows, width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: cw, alignment: AlignmentType.CENTER });
}
const caption = t => P(t, { font: F_HEI, size: SZ.xiaowu, align: AlignmentType.CENTER, indent: {}, spacing: { before: 120, after: 60, line: 240 }, keepNext: true });
const note = t => t ? P(t, { font: F_SONG, size: SZ.xiaowu, align: AlignmentType.LEFT, indent: {}, spacing: { before: 40, after: 160, line: 240 } }) : P('', { indent: {}, spacing: { after: 100, line: 240 } });

const rows = D.rows;
const neg = s => String(s).replace(/^-/, '－');
const f1 = v => (typeof v === 'number' ? neg(v.toFixed(1)) : v);
const f2 = v => neg(v.toFixed(2));
const sup2 = 'hm^{2}';
const tableBuilders = {
  t1: () => threeLineTable(
    [[{ t: '处理编号', rs: 2 }, { t: '处理', rs: 2 }, { t: '施肥水平', cs: 3 }, { t: '施肥量/(kg/' + sup2 + ')', cs: 3 }], [{ gap: 2 }, 'N', 'P_{2}O_{5}', 'K_{2}O', 'N', 'P_{2}O_{5}', 'K_{2}O']],
    rows.map(r => [r.no, `N_{${r.label[1]}}P_{${r.label[3]}}K_{${r.label[5]}}`, r.label[1], r.label[3], r.label[5], f1(r.N), f1(r.P), f1(r.K)]),
    [1.1, 1.3, 0.8, 0.8, 0.8, 1.2, 1.2, 1.2]),
  t2: () => threeLineTable(
    [['处理', '株高/cm', '穗长/cm', '有效穗数/(万穗/' + sup2 + ')', '每穗总粒数/粒', '每穗实粒数/粒', '结实率/%', '千粒重/g']],
    rows.map(r => [r.no, f1(r.ph), f1(r.pl), f1(r.eff_hm2), f1(r.tot), f1(r.fg), f1(r.sr), f1(r.tgw)]),
    [0.8, 1, 1, 1.4, 1.3, 1.3, 1, 1]),
  t3: () => threeLineTable(
    [['处理', '施肥组合', '小区产量/kg', '折合产量/(kg/' + sup2 + ')', '比CK增产/(kg/' + sup2 + ')', '增产率/%', '位次']],
    rows.map(r => [r.no, `N_{${r.label[1]}}P_{${r.label[3]}}K_{${r.label[5]}}`, f1(r.plot_kg), f1(r.y_hm2), f1(r.inc_vs_ck), f1(r.inc_pct), r.rank]),
    [0.8, 1.1, 1.1, 1.4, 1.5, 1, 0.8]),
  t4: () => {
    const de = D.deficiency; const full = rows[5].y_hm2;
    const grade = v => v < 50 ? '极低' : v <= 75 ? '低' : v <= 95 ? '中' : '高';
    return threeLineTable(
      [['处理', '类型', '产量/(kg/' + sup2 + ')', '相对产量/%', '养分丰缺等级', '肥料贡献率/%', '农学效率/(kg/kg)']],
      [
        ['1', '无肥区（N_{0}P_{0}K_{0}）', f1(de.CK.yield), f1(de.CK.rel), '—', '—', '—'],
        ['2', '缺氮区（N_{0}P_{2}K_{2}）', f1(de.N.yield), f1(de.N.rel), grade(de.N.rel), f1(de.N.contrib), de.N.ae.toFixed(2)],
        ['4', '缺磷区（N_{2}P_{0}K_{2}）', f1(de.P.yield), f1(de.P.rel), grade(de.P.rel), f1(de.P.contrib), de.P.ae.toFixed(2)],
        ['8', '缺钾区（N_{2}P_{2}K_{0}）', f1(de.K.yield), f1(de.K.rel), grade(de.K.rel), f1(de.K.contrib), de.K.ae.toFixed(2)],
        ['6', '全肥区（N_{2}P_{2}K_{2}）', f1(full), '100.0', '—', '—', '—'],
      ],
      [0.6, 1.9, 1.3, 1.1, 1.2, 1.4, 1.4]);
  },
  t5: () => {
    const s = D.single; const l = D.N_lpp; const pl = D.P_lin; const kl = D.K_lin;
    const q = (c) => `*{y}=${c[0].toFixed(2)}${c[1] >= 0 ? '+' : '－'}${Math.abs(c[1]).toFixed(4)}*{x}${c[2] >= 0 ? '+' : '－'}${Math.abs(c[2]).toFixed(5)}*{x}^{2}`;
    return threeLineTable(
      [['因素', '模型', '效应方程', '*{R}^{2}', '*{F}', '*{P}', '典型性', '最高产量施肥量/(kg/' + sup2 + ')', '最高产量/(kg/' + sup2 + ')']],
      [
        ['N', '一元二次', q(s.N.coef), s.N.R2.toFixed(4), s.N.F.toFixed(2), s.N.p.toFixed(3), '典型', f1(s.N.xmax) + '^{b}', f1(s.N.ymax) + '^{b}'],
        ['N', '线性加平台', `*{y}=${l.a.toFixed(1)}+${l.b.toFixed(3)}*{x}（*{x}<${l.x0.toFixed(1)}）；*{y}=${l.plateau.toFixed(1)}（*{x}≥${l.x0.toFixed(1)}）`, l.R2.toFixed(4), '—', '—', '—', f1(l.x0), f1(l.plateau)],
        ['P_{2}O_{5}', '一元二次', q(s.P.coef), s.P.R2.toFixed(4), s.P.F.toFixed(2), s.P.p.toFixed(3), '典型', f1(s.P.xmax) + '^{b}', f1(s.P.ymax) + '^{b}'],
        ['P_{2}O_{5}', '线性', `*{y}=${pl.a.toFixed(1)}+${pl.b.toFixed(3)}*{x}`, pl.R2.toFixed(4), '—', '—', '—', '—', '—'],
        ['K_{2}O', '一元二次', q(s.K.coef), s.K.R2.toFixed(4), s.K.F.toFixed(2), s.K.p.toFixed(3), '非典型', '—', '—'],
        ['K_{2}O', '线性', `*{y}=${kl.a.toFixed(1)}+${kl.b.toFixed(3)}*{x}`, kl.R2.toFixed(4), '—', '—', '—', '—', '—'],
      ],
      [0.6, 0.9, 3.0, 0.7, 0.6, 0.6, 0.8, 1.2, 1.1], { leftCols: [2] });
  },
  t6: () => threeLineTable(
    [['因素', '施肥水平变化', '边际产量/(kg/' + sup2 + ')', '边际产值/(元/' + sup2 + ')', '边际肥料成本/(元/' + sup2 + ')', '边际产投比']],
    D.marginal.map(m => [m.f === 'N' ? 'N' : (m.f === 'P' ? 'P_{2}O_{5}' : 'K_{2}O'), `${m.f}${m.from}→${m.f}${m.to}`, f1(m.dy), f1(m.dval), f1(m.cost), f2(m.ratio)]),
    [0.8, 1.2, 1.3, 1.3, 1.5, 1.0]),
  t7: () => threeLineTable(
    [['处理', '产量/(kg/' + sup2 + ')', '产值/(元/' + sup2 + ')', '肥料成本/(元/' + sup2 + ')', '纯收益/(元/' + sup2 + ')', '增产值/(元/' + sup2 + ')', '增收/(元/' + sup2 + ')', '产投比']],
    rows.map(r => [r.no, f1(r.y_hm2), f1(r.value), f1(r.cost), f1(r.net), f1(r.incval), f1(r.incnet), r.ratio === null ? '—' : f2(r.ratio)]),
    [0.7, 1.2, 1.2, 1.3, 1.2, 1.2, 1.2, 0.9]),
};
const tableNotesExtra = {
  t4: '　氮磷钾肥综合贡献率为28.3%［=（全肥区产量－无肥区产量）/全肥区产量×100］。因各单养分贡献率系分别以相应缺素区计算，养分间存在交互作用，三者之和（45.3%）与综合贡献率含义不同，不可相加比较。',
  t5: '　*{F}、*{P}由4个施肥水平的产量拟合求得，残差自由度仅为1，各回归方程均未达显著水平，方程仅用于描述趋势。典型性检验仅适用于一元二次方程（一次项系数为正、二次项系数为负），线性及线性加平台模型不适用。^{b}由方程外推所得，超出试验设计范围，无实际农学意义，不作为推荐施肥依据。',
};

// ---------- 正文 ----------
for (const b of C.body) {
  if (b.type === 'p') body.push(P(b.text));
  else if (b.type === 'h1') body.push(P(b.text, { font: F_HEI, bold: true, size: SZ.xiaosi, align: AlignmentType.LEFT, indent: {}, spacing: { before: 160, after: 80 }, keepNext: true }));
  else if (b.type === 'h2') body.push(P(b.text, { font: F_HEI, bold: true, size: SZ.wuhao, align: AlignmentType.LEFT, indent: {}, spacing: { before: 100, after: 40 }, keepNext: true }));
  else if (b.type === 'h3') body.push(P(b.text, { font: F_HEI, size: SZ.wuhao, align: AlignmentType.LEFT, indent: {}, spacing: { before: 60, after: 20 }, keepNext: true }));
  else if (b.type === 'eq') body.push(P(b.text, { align: AlignmentType.CENTER, indent: {}, spacing: { before: 40, after: 40 } }));
  else if (b.type === 'table') {
    const t = C.tables[b.id];
    body.push(caption(t.caption));
    body.push(tableBuilders[b.id]());
    body.push(note((t.note || '') + (tableNotesExtra[b.id] || '')));
  } else if (b.type === 'figure') {
    const f = C.figures[b.id];
    const img = fs.readFileSync(path.join(__dirname, f.file));
    const w = 642, h = Math.round(642 * 1464 / 4015);
    body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 40 }, keepNext: true,
      children: [new ImageRun({ type: 'png', data: img, transformation: { width: w, height: h } })] }));
    body.push(P(f.caption, { font: F_HEI, size: SZ.xiaowu, align: AlignmentType.CENTER, indent: {}, spacing: { after: 160, line: 240 } }));
  }
}

// ---------- 参考文献 ----------
body.push(P('参考文献', { font: F_HEI, size: SZ.xiaosi, align: AlignmentType.LEFT, indent: {}, spacing: { before: 200, after: 80 }, keepNext: true }));
const uncited = REFS.filter(r => !refIndex.has(r.key)).map(r => r.key);
if (uncited.length) console.warn('警告：未被引用的文献键：' + uncited.join(', '));
refOrder.forEach((key, i) => {
  const r = REFS.find(x => x.key === key);
  body.push(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { line: 276, lineRule: 'auto', after: 0 },
    indent: { left: 480, hanging: 480 },
    children: [...runs(`[${i + 1}]`, { font: F_SONG, size: SZ.xiaowu }), new TextRun({ text: '\t', font: F_SONG, size: SZ.xiaowu }), ...runs(r.text, { font: F_SONG, size: SZ.xiaowu })],
    tabStops: [{ type: TabStopType.LEFT, position: 480 }] }));
});

// ---------- 页脚（首页脚注 + 页码） ----------
const firstFooter = new Footer({ children: [
  new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 6, color: BLACK, space: 1 } }, spacing: { before: 0, after: 0 }, children: [] }),
  P(C.fund, { font: F_SONG, size: SZ.liuhao, align: AlignmentType.LEFT, indent: {}, spacing: { line: 240, after: 0 } }),
  P(C.bio, { font: F_SONG, size: SZ.liuhao, align: AlignmentType.LEFT, indent: {}, spacing: { line: 240, after: 0 } }),
  P(C.received, { font: F_SONG, size: SZ.liuhao, align: AlignmentType.LEFT, indent: {}, spacing: { line: 240, after: 0 } }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 }, children: [new TextRun({ children: [PageNumber.CURRENT], font: F_TNR, size: SZ.xiaowu })] }),
] });
const defaultFooter = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: F_TNR, size: SZ.xiaowu })] })] });

const doc = new Document({
  creator: '', title: C.titleCN,
  styles: { default: { document: { run: { font: F_SONG, size: SZ.wuhao, color: BLACK } } } },
  sections: [{
    properties: { titlePage: true, page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1700, right: 1700, footer: 600 } } },
    footers: { first: firstFooter, default: defaultFooter },
    children: body,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('写出', OUT, '文献', refOrder.length, '条'); });
