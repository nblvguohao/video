#!/usr/bin/env python3
"""Build a journal-style DOCX (and optionally PDF) from a Markdown manuscript.

Usage: python3 scripts/build_docx.py manuscript/manuscript_v2.md submission/manuscript.docx [--pdf] [--line-numbers]

Supported Markdown subset: #/##/### headings, paragraphs, **bold**, *italic*, superscript ^x^,
subscript ~x~, pipe tables, images ![caption](path), bullet lists, numbered lists, horizontal rules.
Figures are embedded at 160 mm width max; captions taken from the image alt text or the following
line starting with "Fig." / "Figure".
"""
import re, sys, os, subprocess
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Lightweight LaTeX-inline-math renderer (see scripts/build_pdf.py for the
# rationale). Not a full TeX engine - it recognises exactly the constructs
# used in manuscript_v2.md (\text{}, \mathbb{1}, Greek letters, \times, \sim,
# \ge/\le, \Pr, braced/bare sub- and superscripts) and renders them as plain
# Unicode, so $...$/$$...$$ source is never printed verbatim.
# ---------------------------------------------------------------------------
_GREEK = {
    'varepsilon': '\u03b5', 'epsilon': '\u03b5', 'alpha': '\u03b1', 'beta': '\u03b2',
    'gamma': '\u03b3', 'delta': '\u03b4', 'theta': '\u03b8', 'rho': '\u03c1',
    'sigma': '\u03c3', 'Lambda': '\u039b', 'Gamma': '\u0393', 'Delta': '\u0394', 'mu': '\u03bc',
}
_SUBS = {'0': '\u2080', '1': '\u2081', '2': '\u2082', '3': '\u2083', '4': '\u2084',
         '5': '\u2085', '6': '\u2086', '7': '\u2087', '8': '\u2088', '9': '\u2089',
         'i': '\u1d62', 't': '\u209c', 'b': '\u1d66', 'g': '\u1d4d', 'y': '\u1d67',
         'c': '\u1d9c', 'n': '\u2099', 'x': '\u2093'}

def _render_math(m):
    s = m.group(1).strip()
    s = re.sub(r'\\text\{([^{}]*)\}', lambda mm: mm.group(1).replace('\\_', '_'), s)
    s = re.sub(r'\\mathbb\{1\}', '\U0001d7d9', s)
    for name in sorted(_GREEK, key=len, reverse=True):
        s = re.sub(r'\\' + name + r'(?![A-Za-z])', _GREEK[name], s)
    s = s.replace('\\times', '\u00d7').replace('\\sim', '~').replace('\\ge', '\u2265')
    s = s.replace('\\Pr', 'Pr').replace('\\le', '\u2264')
    s = re.sub(r'\\[,;!]', '', s)
    s = s.replace('\\\\', '')
    s = re.sub(r'_\{([^{}]*)\}', r'_(\1)', s)
    s = re.sub(r'\^\{([^{}]*)\}', r'^(\1)', s)
    s = re.sub(r'([A-Za-z\u0391-\u03c90-9)])_([A-Za-z0-9])(?![A-Za-z0-9_(])',
               lambda mm: mm.group(1) + _SUBS.get(mm.group(2), '_' + mm.group(2)), s)
    s = s.replace('\\;', ' ').replace('\\,', '')
    return re.sub(r'\s+', ' ', s).strip()

def strip_latex_math(text):
    text = re.sub(r'\$\$(.+?)\$\$', _render_math, text, flags=re.S)
    text = re.sub(r'\$([^$]+?)\$', _render_math, text, flags=re.S)
    return text

def add_line_numbering(section):
    sectPr = section._sectPr
    ln = OxmlElement('w:lnNumType')
    ln.set(qn('w:countBy'), '1')
    ln.set(qn('w:restart'), 'continuous')
    sectPr.append(ln)

INLINE = re.compile(r'(\*\*.+?\*\*|\*.+?\*|\^.+?\^|~.+?~|`.+?`)')

def add_runs(par, text, base_size=12):
    parts = INLINE.split(text)
    for p in parts:
        if not p:
            continue
        if p.startswith('**') and p.endswith('**') and len(p) > 4:
            r = par.add_run(p[2:-2]); r.bold = True
        elif p.startswith('*') and p.endswith('*') and len(p) > 2:
            r = par.add_run(p[1:-1]); r.italic = True
        elif p.startswith('^') and p.endswith('^') and len(p) > 2:
            r = par.add_run(p[1:-1]); r.font.superscript = True
        elif p.startswith('~') and p.endswith('~') and len(p) > 2:
            r = par.add_run(p[1:-1]); r.font.subscript = True
        elif p.startswith('`') and p.endswith('`') and len(p) > 2:
            r = par.add_run(p[1:-1]); r.font.name = 'Courier New'
        else:
            r = par.add_run(p)
        r.font.size = Pt(base_size)
        r.font.name = 'Times New Roman'
        r._element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

def set_par(par, spacing=2.0, align=None, first_indent=None, space_after=6):
    pf = par.paragraph_format
    pf.line_spacing = spacing
    pf.space_after = Pt(space_after)
    if align is not None:
        par.alignment = align
    if first_indent is not None:
        pf.first_line_indent = Mm(first_indent)

def resolve(path):
    if os.path.isabs(path):
        return path
    for base in (os.getcwd(), ROOT, os.path.join(ROOT, 'manuscript')):
        cand = os.path.join(base, path)
        if os.path.exists(cand):
            return cand
    return path

def build(md_path, out_path, pdf=False, line_numbers=False):
    with open(md_path, encoding='utf-8') as f:
        lines = strip_latex_math(f.read()).splitlines()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
        setattr(sec, m, Mm(25))
    if line_numbers:
        add_line_numbering(sec)
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'; style.font.size = Pt(12)
    style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

    i = 0; n = len(lines); first_heading = True
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1; continue
        if line.startswith('<!--'):
            while i < n and '-->' not in lines[i]:
                i += 1
            i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            level = len(m.group(1)); text = m.group(2).strip()
            if level == 1 and first_heading:
                p = doc.add_paragraph(); add_runs(p, text, 14)
                for r in p.runs: r.bold = True
                set_par(p, 1.5, WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
                first_heading = False
            else:
                p = doc.add_paragraph(); add_runs(p, text, 12 if level > 1 else 13)
                for r in p.runs: r.bold = True
                if level >= 3:
                    for r in p.runs: r.italic = True
                set_par(p, 2.0, WD_ALIGN_PARAGRAPH.LEFT, space_after=6)
                p.paragraph_format.keep_with_next = True
            i += 1; continue
        if re.match(r'^-{3,}$', line):
            i += 1; continue
        m = re.match(r'^!\[(.*?)\]\((.*?)\)', line)
        if m:
            alt, path = m.group(1), resolve(m.group(2))
            if os.path.exists(path):
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                try:
                    p.add_run().add_picture(path, width=Mm(160))
                except Exception as e:
                    add_runs(p, f'[figure missing: {path}: {e}]')
            else:
                p = doc.add_paragraph(); add_runs(p, f'[figure not found: {path}]')
            i += 1
            # caption: alt or next non-empty line beginning with Fig
            cap = alt
            if i < n and re.match(r'^\s*(\*\*)?(Fig\.|Figure)', lines[i]):
                cap = lines[i].strip(); i += 1
            if cap:
                p = doc.add_paragraph(); add_runs(p, cap, 11); set_par(p, 1.15, WD_ALIGN_PARAGRAPH.LEFT, space_after=12)
            continue
        if line.lstrip().startswith('|') and i + 1 < n and re.match(r'^\s*\|?\s*:?-{2,}', lines[i + 1]):
            rows = []
            while i < n and lines[i].lstrip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells); i += 1
            rows = [r for r in rows if not all(re.match(r'^:?-{2,}:?$', c) for c in r)]
            if rows:
                ncol = max(len(r) for r in rows)
                t = doc.add_table(rows=len(rows), cols=ncol)
                t.style = 'Table Grid'
                for ri, r in enumerate(rows):
                    for ci in range(ncol):
                        cell = t.cell(ri, ci); cell.text = ''
                        p = cell.paragraphs[0]
                        add_runs(p, r[ci] if ci < len(r) else '', 10)
                        set_par(p, 1.0, space_after=0)
                        if ri == 0:
                            for run in p.runs: run.bold = True
                doc.add_paragraph()
            continue
        m = re.match(r'^\s*[-*]\s+(.*)$', line)
        if m:
            p = doc.add_paragraph(style='List Bullet'); add_runs(p, m.group(1)); set_par(p, 1.5, space_after=2)
            i += 1; continue
        m = re.match(r'^\s*\d+[.)]\s+(.*)$', line)
        if m and not re.match(r'^\s*\d+\.\s+[A-Z][^.]{0,60}$', line):
            p = doc.add_paragraph(style='List Number'); add_runs(p, m.group(1)); set_par(p, 1.5, space_after=2)
            i += 1; continue
        # paragraph: merge consecutive lines
        buf = [line.strip()]
        i += 1
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4}\s|!\[|\||\s*[-*]\s|\s*\d+[.)]\s|-{3,}$|<!--)', lines[i]):
            buf.append(lines[i].strip()); i += 1
        text = ' '.join(buf)
        p = doc.add_paragraph(); add_runs(p, text)
        is_caption = bool(re.match(r'^(\*\*)?(Fig\.|Figure|Table)\s*\d', text))
        set_par(p, 1.15 if is_caption else 2.0, WD_ALIGN_PARAGRAPH.LEFT, space_after=8)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    doc.save(out_path)
    print('wrote', out_path)
    if pdf:
        outdir = os.path.dirname(os.path.abspath(out_path))
        print("LibreOffice unavailable in this container; use scripts/build_pdf.py for PDF")

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    if len(a) < 2:
        print(__doc__); sys.exit(1)
    build(a[0], a[1], pdf='--pdf' in sys.argv, line_numbers='--line-numbers' in sys.argv)
