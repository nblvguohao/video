// 由结构化字段生成 GB/T 7714-2015（顺序编码制）著录字符串
// 用法：node mkrefs.js refs_map.json > refs.js
const fs = require('fs');
const map = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); // [{key, type:'J'|'S'|'M', authors:[], title, journal, year, volume, issue, pages, org, stdno, publisher, city}]

function authorsStr(a) {
  const arr = (a || []).map(s => s.trim()).filter(Boolean);
  if (arr.length > 3) return arr.slice(0, 3).join(', ') + ', 等';
  return arr.join(', ');
}
function fmt(r) {
  const t = r.type || 'J';
  if (t === 'J') {
    let s = `${authorsStr(r.authors)}. ${r.title}[J]. ${r.journal}, ${r.year}`;
    if (r.volume && r.issue) s += `, ${r.volume}(${r.issue})`;
    else if (r.volume) s += `, ${r.volume}`;
    else if (r.issue) s += `(${r.issue})`;
    if (r.pages) s += `: ${r.pages}`;
    return s + '.';
  }
  if (t === 'S') {
    // 机构. 标准名称: 标准号[S]. 出版地: 出版社, 年.
    let s = `${r.org}. ${r.title}${r.stdno ? ': ' + r.stdno : ''}[S]. `;
    if (r.city && r.publisher) s += `${r.city}: ${r.publisher}, `;
    return s + `${r.year}.`;
  }
  if (t === 'M') {
    return `${authorsStr(r.authors)}. ${r.title}[M]. ${r.city}: ${r.publisher}, ${r.year}${r.pages ? ': ' + r.pages : ''}.`;
  }
  if (t === 'EB') {
    const upd = r.date ? `(${r.date})` : '';
    return `${r.org || authorsStr(r.authors)}. ${r.title}[EB/OL]. ${upd}[${r.cited || ''}]. ${r.url}.`;
  }
  throw new Error('unknown type ' + t);
}
const out = map.map(r => ({ key: r.key, text: fmt(r), evidence: r.evidence_urls || [] }));
process.stdout.write('module.exports = ' + JSON.stringify(out, null, 1) + ';\n');
