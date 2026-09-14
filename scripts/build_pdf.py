#!/usr/bin/env python3
"""Render a Markdown manuscript to PDF with PyMuPDF's Story engine (LibreOffice is unavailable here).

Usage: python3 scripts/build_pdf.py manuscript/manuscript_v2.md submission/manuscript.pdf
"""
import re, sys, os
import markdown, pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = """
body{font-family:'Times New Roman',serif;font-size:11.5pt;line-height:1.9;color:#000}
h1{font-size:15pt;text-align:center;line-height:1.3;margin:0 0 12pt 0}
h2{font-size:12.5pt;margin:14pt 0 6pt 0} h3{font-size:12pt;font-style:italic;margin:10pt 0 4pt 0}
p{margin:0 0 8pt 0;text-align:justify}
table{border-collapse:collapse;font-size:9.5pt;line-height:1.25;margin:6pt 0 10pt 0}
td,th{border-top:0.6pt solid #000;border-bottom:0.6pt solid #000;padding:2pt 5pt;vertical-align:top}
th{font-weight:bold}
img{width:150mm} .caption{font-size:10.5pt;line-height:1.3;margin:2pt 0 12pt 0}
ul,ol{margin:0 0 8pt 18pt} li{margin:0}
"""

def md_to_html(md_text):
    md_text = re.sub(r'\^([^\^\s]{1,20})\^', r'<sup>\1</sup>', md_text)
    md_text = re.sub(r'(?<!~)~([^~\s]{1,20})~(?!~)', r'<sub>\1</sub>', md_text)
    md_text = re.sub(r'<!--.*?-->', '', md_text, flags=re.S)
    html = markdown.markdown(md_text, extensions=['tables', 'sane_lists'])
    html = re.sub(r'<p>(\s*(?:<strong>)?(?:Fig\.|Figure|Table)\s*\d[^<]*)', r'<p class="caption">\1', html)
    return html

def build(md_path, out_path, paper='a4', margin=56):
    md_text = open(md_path, encoding='utf-8').read()
    base = os.path.dirname(os.path.abspath(md_path))
    html = md_to_html(md_text)
    # make image srcs absolute-relative to archive root
    def fix(m):
        src = m.group(1)
        for b in (base, ROOT, os.getcwd()):
            cand = os.path.join(b, src)
            if os.path.exists(cand):
                return f'src="{os.path.relpath(cand, ROOT)}"'
        return m.group(0)
    html = re.sub(r'src="([^"]+)"', fix, html)
    story = pymupdf.Story(html=html, user_css=CSS, archive=pymupdf.Archive(ROOT))
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    writer = pymupdf.DocumentWriter(out_path)
    mediabox = pymupdf.paper_rect(paper)
    where = mediabox + (margin, margin, -margin, -margin)
    more, pages = True, 0
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page(); pages += 1
    writer.close()
    # page numbers
    doc = pymupdf.open(out_path)
    for i, page in enumerate(doc):
        page.insert_text((mediabox.width / 2 - 8, mediabox.height - 30), str(i + 1), fontsize=9, fontname='tiro')
    doc.save(out_path, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    print('wrote', out_path, 'pages', pages)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    build(sys.argv[1], sys.argv[2])
