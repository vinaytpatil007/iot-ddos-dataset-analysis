from __future__ import annotations

import os
import re
import shutil
from io import BytesIO
from pathlib import Path
from typing import Iterable, List, Tuple

import pandas as pd
from PIL import Image
from docx import Document
from docx.document import Document as DocumentObject
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.table import Table
from docx.text.paragraph import Paragraph


INPUT_DOC = Path(r"D:\ddos dataset\iot_ddos_dataset_analysis_paper_v5_final.docx")
OUTPUT_DOC = Path(r"D:\ddos dataset\iot_ddos_dataset_analysis_paper_SensorsReady.docx")
PACKAGE_DIR = Path(r"D:\ddos dataset\submission_package")
FIGURES_DIR = PACKAGE_DIR / "figures"
TABLES_DIR = PACKAGE_DIR / "tables"
README_PATH = PACKAGE_DIR / "README.txt"
SUMMARY_PATH = PACKAGE_DIR / "summary_report.txt"

AUTHOR_LINES = [
    "Vinay T. Patil",
    "Department of Computer Engineering",
    "Kavayitri Bahinabai Chaudhari North Maharashtra University",
    "Correspondence: vinay@example.com",
    "ORCID: 0000-0000-0000-0000",
]

SENSORS_SECTIONS = [
    "Acknowledgments",
    "Funding",
    "Author Contributions",
    "Data Availability Statement",
    "Conflicts of Interest",
]


def iter_block_items(parent) -> Iterable[Paragraph | Table]:
    if isinstance(parent, DocumentObject):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc

    for child in parent_elm.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, parent)
        elif child.tag.endswith("}tbl"):
            yield Table(child, parent)


def set_default_font(document: Document) -> None:
    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    style.font.size = Pt(11)


def add_page_number(section) -> None:
    footer = section.footer
    paragraph = footer.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()

    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")

    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)


def shade_cell(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def clear_paragraph(paragraph: Paragraph) -> None:
    p = paragraph._element
    for child in list(p):
        p.remove(child)


def insert_paragraph_after(paragraph: Paragraph, text: str = "", style: str | None = None) -> Paragraph:
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    if text:
        new_para.add_run(text)
    if style:
        new_para.style = style
    return new_para


def extract_and_save_figures(document: Document) -> List[Path]:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure_paths: List[Path] = []

    for index, shape in enumerate(document.inline_shapes, start=1):
        rid = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
        image_part = document.part.related_parts[rid]
        image = Image.open(BytesIO(image_part.blob)).convert("RGB")
        figure_path = FIGURES_DIR / f"fig{index}.png"
        image.save(figure_path, format="PNG", dpi=(300, 300))
        figure_paths.append(figure_path)

    return figure_paths


def export_tables_to_csv(document: Document) -> List[Path]:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    table_paths: List[Path] = []

    for index, table in enumerate(document.tables, start=1):
        rows = []
        for row in table.rows:
            rows.append([cell.text.strip() for cell in row.cells])
        df = pd.DataFrame(rows[1:], columns=rows[0] if rows else None)
        table_path = TABLES_DIR / f"table{index}.csv"
        df.to_csv(table_path, index=False)
        table_paths.append(table_path)

    return table_paths


def format_title_and_author_block(document: Document) -> None:
    title_para = document.paragraphs[0]
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title_para.runs:
        run.bold = True
        run.font.size = Pt(16)

    current = title_para
    # Replace the next few lines with a Sensors-style author block.
    for line in AUTHOR_LINES:
        current = insert_paragraph_after(current, line)
        current.alignment = WD_ALIGN_PARAGRAPH.CENTER

    current = insert_paragraph_after(current, "Manuscript prepared for submission to Sensors (MDPI).")
    current.alignment = WD_ALIGN_PARAGRAPH.CENTER


def ensure_section_headings(document: Document) -> None:
    existing = {p.text.strip() for p in document.paragraphs if p.text.strip()}
    anchor = None
    for paragraph in document.paragraphs:
        if paragraph.text.strip() == "References":
            anchor = paragraph
            break

    if anchor is None:
        anchor = document.add_paragraph()
        anchor.style = "Heading 1"
        anchor.add_run("References").bold = True

    insert_after = anchor
    for section_name in reversed(SENSORS_SECTIONS):
        if section_name not in existing:
            new_heading = insert_paragraph_after(insert_after, section_name, style="Heading 1")
            insert_paragraph_after(new_heading, placeholder_for_section(section_name))
        insert_after = anchor


def placeholder_for_section(section_name: str) -> str:
    placeholders = {
        "Acknowledgments": "The authors would like to acknowledge institutional and technical support. TODO: Add final acknowledgments.",
        "Funding": "Funding: This research received no external funding. TODO: Update funding statement if applicable.",
        "Author Contributions": "Author Contributions: Conceptualization, methodology, software, analysis, writing—original draft preparation, and writing—review and editing were performed by the author. TODO: Revise according to final authorship roles.",
        "Data Availability Statement": "Data Availability Statement: The datasets and analysis code are available at [GitHub placeholder] and [Zenodo placeholder]. TODO: Replace placeholders with final public links and access dates.",
        "Conflicts of Interest": "Conflicts of Interest: The author declares no conflict of interest. TODO: Update if needed.",
    }
    return placeholders[section_name]


def renumber_table_captions(document: Document) -> List[str]:
    notes = []
    table_index = 0
    blocks = list(iter_block_items(document))
    for i, block in enumerate(blocks):
        if isinstance(block, Table):
            table_index += 1
            caption_para = blocks[i - 1] if i > 0 and isinstance(blocks[i - 1], Paragraph) else None
            expected = f"Table {table_index}."
            if caption_para is None or not caption_para.text.strip().lower().startswith("table"):
                target = caption_para if caption_para else Paragraph(block._tbl.addprevious(OxmlElement("w:p")), document)
                # fallback note if insertion is not straightforward
                notes.append(f"TODO: Confirm placement of Table {table_index} near first citation.")
            else:
                parts = caption_para.text.split(".", 1)
                suffix = parts[1].strip() if len(parts) > 1 else "Table caption."
                caption_para.text = f"{expected} {suffix}"

            if not table_referenced_before(document, expected, block):
                note_para = caption_para if caption_para else document.add_paragraph()
                insert_paragraph_after(note_para, f"TODO: Cite {expected} in the surrounding text.")
                notes.append(f"Inserted TODO note for missing text reference to {expected}")
    return notes


def paragraph_contains_drawing(paragraph: Paragraph) -> bool:
    return bool(paragraph._element.xpath(".//w:drawing"))


def renumber_figure_captions(document: Document) -> List[str]:
    notes = []
    figure_index = 0
    paragraphs = document.paragraphs
    for idx, paragraph in enumerate(paragraphs):
        if not paragraph_contains_drawing(paragraph):
            continue
        figure_index += 1
        caption_text = f"Figure {figure_index}."
        caption_para = paragraphs[idx + 1] if idx + 1 < len(paragraphs) else None
        if caption_para is None or not caption_para.text.strip().lower().startswith("figure"):
            new_cap = insert_paragraph_after(paragraph, f"{caption_text} TODO: Add descriptive figure caption.")
            new_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            notes.append(f"Inserted placeholder caption for Figure {figure_index}")
        else:
            parts = caption_para.text.split(".", 1)
            suffix = parts[1].strip() if len(parts) > 1 else "Figure caption."
            caption_para.text = f"{caption_text} {suffix}"
            caption_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

        if not any(caption_text in p.text for p in paragraphs[:idx]):
            insert_paragraph_after(paragraphs[idx + 1], f"TODO: Cite {caption_text} in the surrounding text.")
            notes.append(f"Inserted TODO note for missing text reference to {caption_text}")
    return notes


def table_referenced_before(document: Document, caption_prefix: str, table: Table) -> bool:
    blocks = list(iter_block_items(document))
    for i, block in enumerate(blocks):
        if block is table:
            for prev in reversed(blocks[:i]):
                if isinstance(prev, Paragraph) and prev.text.strip():
                    return caption_prefix in prev.text
            break
    return False


def style_tables(document: Document) -> None:
    for table in document.tables:
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        if table.rows:
            for cell in table.rows[0].cells:
                shade_cell(cell, "D9EAF7")


def build_readme(figure_paths: List[Path], table_paths: List[Path]) -> None:
    text = [
        "Sensors Submission Package",
        "",
        "Contents:",
        f"- Manuscript: {OUTPUT_DOC.name}",
        f"- Figures folder: {FIGURES_DIR}",
        f"- Tables folder: {TABLES_DIR}",
        "",
        "Figures:",
    ]
    text.extend([f"- {path.name}" for path in figure_paths])
    text.append("")
    text.append("Tables:")
    text.extend([f"- {path.name}" for path in table_paths])
    text.append("")
    text.append("Data and code links:")
    text.append("- GitHub: TODO_INSERT_GITHUB_LINK")
    text.append("- Zenodo: TODO_INSERT_ZENODO_LINK")
    text.append("- Dataset root: D:\\ddos dataset")
    README_PATH.write_text("\n".join(text), encoding="utf-8")


def write_summary(notes: List[str], figure_paths: List[Path], table_paths: List[Path]) -> str:
    lines = [
        f"Input manuscript: {INPUT_DOC}",
        f"Output manuscript: {OUTPUT_DOC}",
        f"Figures extracted: {len(figure_paths)}",
        f"Tables exported: {len(table_paths)}",
    ]
    if notes:
        lines.append("Notes:")
        lines.extend([f"- {note}" for note in notes])
    summary = "\n".join(lines)
    SUMMARY_PATH.write_text(summary, encoding="utf-8")
    return summary


def main() -> None:
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    document = Document(str(INPUT_DOC))
    set_default_font(document)
    add_page_number(document.sections[0])

    format_title_and_author_block(document)
    ensure_section_headings(document)
    style_tables(document)

    figure_notes = renumber_figure_captions(document)
    table_notes = renumber_table_captions(document)

    OUTPUT_DOC.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(OUTPUT_DOC))

    figure_paths = extract_and_save_figures(Document(str(OUTPUT_DOC)))
    table_paths = export_tables_to_csv(Document(str(OUTPUT_DOC)))

    shutil.copy2(OUTPUT_DOC, PACKAGE_DIR / OUTPUT_DOC.name)
    build_readme(figure_paths, table_paths)
    summary = write_summary(figure_notes + table_notes, figure_paths, table_paths)
    print(summary)


if __name__ == "__main__":
    main()
