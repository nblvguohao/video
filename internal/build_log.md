# Submission build log

## 1. Build commands run

```
mkdir -p /home/user/video/submission
python3 /home/user/video/scripts/build_docx.py manuscript/manuscript_v2.md submission/manuscript.docx --pdf --line-numbers
```

Result: DOCX written successfully. As expected, the script's own `--pdf` conversion step
failed with `LibreOffice unavailable in this container; use scripts/build_pdf.py for PDF`
(the script shells out to `soffice --headless --convert-to pdf`; the binary is present at
`/usr/bin/soffice` but conversion inside this sandbox does not complete — this matches the
task's own expectation that this would happen). Fell back to the dedicated PDF path:

```
python3 /home/user/video/scripts/build_pdf.py manuscript/manuscript_v2.md submission/manuscript.pdf
```

Result: `wrote submission/manuscript.pdf pages 35`.

## 2. Layout defect found and fixed: unrendered LaTeX math

Reading the PDF (`Read` on `submission/manuscript.pdf`, converted to page images via
PyMuPDF since `pdftoppm`/`poppler-utils` could not be installed — no network access to the
package mirror inside this sandbox) surfaced a real rendering bug: manuscript_v2.md uses
inline (`$...$`) and display (`$$...$$`) LaTeX math in Section 4.2–4.6 (the formal
specification, the $H_{ability}$/$H_{measure}$/$H_{threshold}$ hypothesis statements, and the
auxiliary-specification formulas) and once more in §6.1 (R13). Neither `build_docx.py` nor
`build_pdf.py` had any handling for `$...$` syntax, so the raw TeX source — backslashes,
`\text{}`, `\beta`, `_{...}`, `\mathbb{1}`, etc. — was being printed verbatim in both outputs.
Example, before the fix (page 11 of the original PDF):

> A naive specification of the form $Y \sim \text{channel} + \text{year} +
> \text{trial\_group} + \text{check} + \text{breeding\_system}$ is not estimable as written...

This is not a formatting nicety — a referee or copy editor reading either output would see
literal LaTeX commands in the middle of the empirical-strategy section, which is one of the
paper's most-read parts.

**Fix applied**: added a small, targeted `strip_latex_math()` / `_render_math()` pass to both
`scripts/build_pdf.py` and `scripts/build_docx.py`, applied to the raw Markdown text before
any other processing. It is not a general TeX engine — it recognises exactly the constructs
this manuscript actually uses (`\text{}`, `\mathbb{1}`, the Greek letters that appear, `\times`,
`\sim`, `\ge`/`\le`, `\Pr`, and braced/bare sub- and superscripts) and renders them as plain
Unicode (e.g. `\beta` → β, `Y_i` → Yᵢ, `\gamma_{c(i)}` → γ_(c(i))). After the fix, the same
passage renders as:

> A naive specification of the form Y ~ channel + year + trial_group + check + breeding_system
> is not estimable as written...

and the display equations render as, e.g., `c(i) = Yearᵢ × TrialGroupᵢ × Checkᵢ,` and
`Yᵢ = βNewChannelᵢ + γ_(c(i)) + δ_(b(i)) + εᵢ,`. This is legible, faithful to the original
formula, and not typeset like real math notation — a reasonable outcome for a Markdown→DOCX/PDF
pipeline with no TeX renderer, and a large improvement over raw source leaking into the
submission file. Verified by re-rendering pages 1, 2, 11, 12, 13, 21 and 35 to PNG (via
PyMuPDF) after the fix and re-checking the DOCX's paragraph text directly (`python-docx`) —
both outputs now show the rendered form, not the raw LaTeX, everywhere `$...$` appeared.

No manuscript content, number, or claim was changed by this fix — it only affects how the
existing formulas are typeset in the two derived submission files; `manuscript_v2.md` itself
is untouched (it should keep using `$...$` for anyone who later renders it with a real LaTeX
pipeline).

## 3. Other layout spot-checks

- **Headings**: H1 (numbered sections), H2 (subsections), italic H3 all render with correct
  size/weight hierarchy throughout the sampled pages (1, 2, 11–13, 21, 35).
- **Bullet/numbered lists**: render correctly (e.g. the highlights list on p.1, the
  H_ability/H_measure bullet list on p.12–13, the consolidated R1–R14 bullet list in §6.1 on
  p.21).
- **Italic/bold/quotation marks, em-dashes, Chinese characters (国审, 绿色通道, etc.), inline
  code spans (`` `quality_stated` ``)**: all render correctly in the sampled pages.
- **Page numbers and running header**: page numbers present bottom-centre on every sampled
  page; running title given on the title page.
- **Line numbering** (requested via `--line-numbers` for the DOCX): confirmed present in the
  DOCX's underlying XML (`<w:lnNumType>` element found in `word/document.xml`).

## 4. Tables and figures: not embedded — a pre-existing manuscript-source characteristic, not a build defect

`manuscript_v2.md` contains **no** Markdown image syntax (`![...](...)`) and **no** pipe-table
syntax (`| ... |`) anywhere in the body text — confirmed by `grep -c '!\[' ` and
`grep -c '^|'`, both returning 0, and confirmed this was **already true in manuscript_v1.md**
(same greps, same zero counts), so this is not something introduced by this revision cycle.
The manuscript instead refers to figures and tables only in prose ("Table 3", "Fig. 2, left
panel, blue markers", etc.) and via external file paths given in `figure_table_list.md`
(`tables/table3_main_results.csv`, `figures/fig2_forest_main.png`, etc.).

Because `build_docx.py`/`build_pdf.py` only embed what the Markdown source instructs them to
embed (an `![...]()` for a figure, a `| ... |` block for a table), and manuscript_v2.md
contains neither, **the built DOCX and PDF have zero embedded figures and zero embedded
tables** — confirmed directly: `python3 -c` iterating `page.get_images()` over every PDF page
returns 0 total images, and `python-docx`'s paragraph/table enumeration on the DOCX finds no
`Document.tables` entries either.

This is reported honestly rather than silently worked around: it is **not a bug in
build_pdf.py/build_docx.py** (both scripts do support image and pipe-table embedding, and
would render them correctly if the source contained them — this is exactly what let the LaTeX
fix above be verified so precisely), and it is **not something introduced during this proofing
task** — it is a structural property of how manuscript_v2.md (and v1 before it) was authored,
consistent with a submission workflow where figures/tables are supplied to the journal as
separate files (as `figure_table_list.md` itself documents: `figures/fig1_channel_stacked.png`
through `fig7_...`, `tables/table1_...csv` through `table7_...csv`) rather than inlined into
the main-text Markdown. If the author team wants a single self-contained DOCX/PDF with figures
and tables placed inline (as many journals' submission systems now prefer, or at minimum for
internal review copies), the fix is upstream of these build scripts: add `![caption](path)` and
pipe-table markup to manuscript_v2.md at the point each is first cited, then re-run these same
build commands — no script change is needed for that case.

## 5. File verification

```
$ ls -la /home/user/video/submission/
-rw-r--r-- manuscript.docx   73,495 bytes
-rw-r--r-- manuscript.pdf 4,995,516 bytes  (35 pages)
```

- **manuscript.docx**: valid Microsoft Word 2007+ (OOXML) file (`file` confirms), opens
  correctly with `python-docx`, 192 paragraphs, line numbering present, not empty/truncated.
- **manuscript.pdf**: valid PDF 1.7, 35 pages, not empty/truncated. Its size (~4.75 MB) is
  larger than the page count alone would suggest for a text-only document with no embedded
  images (confirmed zero embedded images) — this comes from PyMuPDF's Story/DocumentWriter
  embedding full font programs (Times New Roman regular/bold/italic and a symbol font for the
  superscript/subscript Unicode glyphs used by the math-rendering fix) rather than subsetting
  them; `doc.xref_length()` reports 262 internal objects. This is a known characteristic of
  this rendering path, not a corruption or content problem — every sampled page displays
  correctly — but is worth the author team's awareness if a stricter file-size cap applies at
  submission; the pre-existing (unfixed) build produced a very similarly sized file for the
  same reason, so this is not a side effect of today's math-rendering change.

## Summary

- DOCX build: **succeeded** directly via `build_docx.py`.
- PDF build: **succeeded** via the `build_pdf.py` fallback, exactly as the task anticipated
  (LibreOffice present but non-functional for headless conversion in this sandbox).
- Layout defect found: **raw LaTeX math source was rendering unrendered in both outputs** —
  fixed in both `scripts/build_pdf.py` and `scripts/build_docx.py` with a small, targeted
  Unicode-math renderer; re-verified by re-rendering affected pages.
- Layout finding reported, not fixed: **manuscript_v2.md embeds no figures or tables** (by
  design/pre-existing, confirmed also true of v1) — the build scripts correctly reflect this;
  fixing it would require adding image/table markup to the manuscript source itself, which is
  outside this proofing pass's remit of not altering manuscript content.
- Both files pass a basic integrity check (correct file type, non-trivial size, opens and
  parses cleanly).
