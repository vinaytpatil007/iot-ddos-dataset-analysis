from pathlib import Path

import pandas as pd
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


BASE_DIR = Path(r"D:\ddos dataset")
ANALYSIS_DIR = BASE_DIR / "analysis_results"
ADVANCED_DIR = ANALYSIS_DIR / "advanced_analysis"
OUTPUT_PATH = BASE_DIR / "iot_ddos_dataset_analysis_paper_v2.docx"

TITLE = "Comparative Analysis of Modern IoT DDoS Datasets: CICIoT2023, CICDDoS2019, and TON-IoT"
AUTHOR_NAME = "Vinay T. Patil"
AFFILIATION_1 = "Department of Computer Engineering"
AFFILIATION_2 = "Kavayitri Bahinabai Chaudhari North Maharashtra University"
AUTHOR_EMAIL = "Email: vinay@example.com"


def load_tables() -> dict:
    return {
        "dataset_comparison": pd.read_csv(ANALYSIS_DIR / "dataset_comparison_table.csv"),
        "dataset_difficulty": pd.read_csv(ANALYSIS_DIR / "dataset_difficulty_table.csv"),
        "feature_redundancy": pd.read_csv(ANALYSIS_DIR / "feature_redundancy_summary.csv"),
    }


def set_default_font(document: Document) -> None:
    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    style.font.size = Pt(11)


def set_margins(document: Document) -> None:
    for section in document.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)


def add_page_number(section) -> None:
    footer = section.footer
    paragraph = footer.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = paragraph.add_run()
    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")

    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = "PAGE"

    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")

    run._r.append(fld_char_begin)
    run._r.append(instr_text)
    run._r.append(fld_char_end)


def shade_cell(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def add_title_block(document: Document) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(TITLE)
    run.bold = True
    run.font.size = Pt(16)
    run.font.name = "Times New Roman"

    for line in [AUTHOR_NAME, AFFILIATION_1, AFFILIATION_2, AUTHOR_EMAIL]:
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run(line)

    document.add_paragraph("")


def add_heading(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.style = document.styles["Heading 1"]
    run = paragraph.add_run(text)
    run.bold = True


def add_body_paragraph(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph.paragraph_format.line_spacing = 1.15
    paragraph.add_run(text)


def add_keywords(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    lead = paragraph.add_run("Keywords: ")
    lead.bold = True
    paragraph.add_run(text)


def add_table(document: Document, dataframe: pd.DataFrame, caption: str) -> None:
    caption_p = document.add_paragraph()
    caption_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = caption_p.add_run(caption)
    run.bold = True

    table = document.add_table(rows=1, cols=len(dataframe.columns))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"

    header_cells = table.rows[0].cells
    for idx, column in enumerate(dataframe.columns):
        header_cells[idx].text = str(column)
        shade_cell(header_cells[idx], "D9EAF7")
        for paragraph in header_cells[idx].paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in paragraph.runs:
                r.bold = True

    for _, row in dataframe.iterrows():
        cells = table.add_row().cells
        for idx, value in enumerate(row):
            if isinstance(value, float):
                text = "inf" if value == float("inf") else f"{value:.6f}" if abs(value) < 1000 else f"{value:.2f}"
            else:
                text = str(value)
            cells[idx].text = text
            for paragraph in cells[idx].paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_paragraph("")


def add_figure(document: Document, image_path: Path, caption: str, width: float = 5.8) -> None:
    if not image_path.exists():
        return
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(image_path), width=Inches(width))

    cap = document.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_run = cap.add_run(caption)
    cap_run.italic = True


def abstract_text() -> str:
    return (
        "The rapid proliferation of Internet of Things (IoT) devices has expanded the cyberattack surface of modern "
        "digital infrastructure, making distributed denial-of-service (DDoS) attacks a critical security concern. "
        "Robust IoT intrusion-detection research requires benchmark datasets that are not only large and diverse, but "
        "also well understood in terms of feature structure, class imbalance, and practical learning difficulty. This "
        "study presents a comparative analysis of three contemporary IoT DDoS datasets: CICIoT2023, CICDDoS2019, and "
        "TON-IoT. The analysis integrates statistical profiling, class-distribution assessment, redundancy analysis, "
        "dimensionality-reduction visualization, and baseline machine-learning evaluation. The results indicate that "
        "CICIoT2023 and CICDDoS2019 are highly separable under baseline classifiers, whereas TON-IoT presents a more "
        "challenging classification setting for linear models despite strong nonlinear separability. The study also "
        "identifies substantial class imbalance, especially in CICDDoS2019, and highly redundant packet-count and "
        "packet-length feature groups across the compared datasets. These findings provide a clearer basis for "
        "benchmark selection, feature pruning, and future cross-dataset evaluation in IoT DDoS detection research."
    )


def introduction_text() -> str:
    return (
        "IoT systems now underpin a broad range of application domains, including industrial automation, healthcare "
        "monitoring, smart homes, and intelligent transportation. While this connectivity enables significant "
        "operational benefits, it also exposes large numbers of resource-constrained devices to cyber threats. DDoS "
        "attacks are particularly damaging because they can weaponize vulnerable IoT nodes into botnets capable of "
        "disrupting services at scale. Consequently, machine-learning-based DDoS detection has become a major research "
        "direction in IoT security. However, many published studies emphasize model accuracy while offering limited "
        "discussion of the datasets that drive those results. Without careful examination of dataset size, feature "
        "composition, redundancy, and imbalance, reported detection performance may be difficult to interpret or "
        "reproduce. This paper addresses that issue through a comparative dataset-centered analysis of CICIoT2023, "
        "CICDDoS2019, and TON-IoT."
    )


def related_work_text() -> str:
    return (
        "The literature on IoT security has introduced several benchmark datasets for intrusion detection and attack "
        "classification. Flow-based datasets such as CICDDoS2019 have been used extensively for DDoS detection, while "
        "TON-IoT has broadened evaluation by incorporating network and device-level observations across multiple attack "
        "types. More recently, CICIoT2023 has emerged as a large IoT-focused benchmark with multiple contemporary DDoS "
        "variants. In parallel, learning-based defenses have ranged from conventional classifiers such as Logistic "
        "Regression, Support Vector Machines, and Random Forests to deep learning architectures and hybrid pipelines. "
        "Despite these advances, fewer studies have concentrated on dataset quality itself, including separability, "
        "redundancy, and relative benchmark difficulty. A rigorous comparative dataset analysis remains necessary to "
        "support stronger empirical conclusions."
    )


def methodology_text() -> str:
    return (
        "The analysis pipeline consisted of six stages. First, benchmark datasets were acquired from local processed "
        "CSV outputs derived from CICIoT2023, CICDDoS2019, and TON-IoT. Second, dataset preprocessing standardized the "
        "binary label representation, removed non-numeric identifiers, and retained cleaned feature matrices for "
        "comparative study. Third, feature extraction was defined by the numeric attributes available in each cleaned "
        "dataset after preprocessing. Fourth, statistical analysis was performed to quantify dataset size, class "
        "distribution, feature skewness, entropy, and redundancy. Fifth, visualization techniques including principal "
        "component analysis (PCA) and t-distributed stochastic neighbor embedding (t-SNE) were used to inspect benign "
        "and DDoS separability in lower-dimensional spaces. Finally, baseline machine-learning models, specifically "
        "Logistic Regression and Random Forest, were evaluated using stratified train-test splits to estimate dataset "
        "difficulty under linear and nonlinear decision boundaries."
    )


def dataset_description_text() -> str:
    return (
        "The three datasets selected for this study differ substantially in scale, feature richness, and balance "
        "between benign and attack traffic. CICIoT2023 provides the largest IoT-focused benchmark, CICDDoS2019 offers "
        "the richest cleaned feature space, and TON-IoT provides a comparatively more balanced binary DDoS subset. "
        "These structural differences make them suitable for a comparative examination of benchmark behavior."
    )


def dataset_analysis_text() -> str:
    return (
        "The comparative statistics indicate pronounced differences in dataset size and class balance. CICIoT2023 "
        "contains the largest number of processed records, whereas CICDDoS2019 exhibits the most severe DDoS-to-benign "
        "imbalance. TON-IoT, although smaller, provides a less extreme class ratio and therefore offers a more "
        "demanding setting for balanced evaluation. Feature analysis further reveals several highly skewed variables and "
        "strong redundancy among feature pairs, particularly within flag counts and packet-length measurements."
    )


def experimental_results_text() -> str:
    return (
        "The reduced-dimensional visualizations and baseline classifier results provide complementary evidence about "
        "dataset separability. PCA and t-SNE suggest clear cluster separation for the CIC datasets, while TON-IoT "
        "displays a less trivial structure. The model-based analysis supports this interpretation: Logistic Regression "
        "achieves near-perfect performance on CICIoT2023 and CICDDoS2019, but lower ROC-AUC on TON-IoT, whereas Random "
        "Forest remains highly effective on all three datasets. This pattern indicates that TON-IoT presents a more "
        "complex, nonlinear classification problem."
    )


def discussion_text() -> str:
    return (
        "Several implications emerge from the comparative findings. First, severe class imbalance can inflate apparent "
        "performance if evaluation protocols do not explicitly account for the scarcity of benign traffic. Second, "
        "redundant features may increase model complexity while contributing limited new information, motivating feature "
        "selection or ablation studies. Third, benchmark difficulty is not interchangeable across datasets: models that "
        "perform exceptionally well on CICIoT2023 or CICDDoS2019 may still face more challenging decision boundaries on "
        "TON-IoT. Accordingly, dataset choice should be aligned with the intended research objective, whether that is "
        "benchmark optimization, cross-dataset robustness, or realistic deployment evaluation."
    )


def conclusion_text() -> str:
    return (
        "This journal-ready draft presented a comparative analysis of CICIoT2023, CICDDoS2019, and TON-IoT for IoT "
        "DDoS detection research. The study contributed a structured evaluation of dataset statistics, class imbalance, "
        "feature properties, visualization behavior, and baseline classification difficulty. The results demonstrate "
        "that the compared benchmarks differ substantially in balance, redundancy, and effective learning difficulty, "
        "highlighting the need for dataset-aware interpretation of detection results."
    )


def future_work_text() -> str:
    return (
        "Future research should investigate cross-dataset generalization to determine how well models trained on one "
        "IoT DDoS benchmark transfer to others. Additional work is also needed on deep learning architectures, "
        "representation learning, and sequence-based detection models that capture temporal dependencies in IoT traffic. "
        "Finally, future benchmark construction should prioritize realistic benign traffic, broader device diversity, "
        "and more contemporary real-world IoT attack scenarios."
    )


def references_list() -> list[str]:
    return [
        "[1] A. Author and B. Author, \"IoT intrusion detection research paper,\" Journal of Network Security, vol. 10, no. 2, pp. 1-12, 2023.",
        "[2] C. Author and D. Author, \"DDoS detection using machine learning,\" IEEE Access, vol. 11, pp. 1000-1015, 2023.",
        "[3] E. Author et al., \"CICIoT2023 dataset paper,\" in Proc. International Conference on Cybersecurity, 2023, pp. 55-62.",
        "[4] N. Moustafa, \"TON-IoT dataset paper,\" Future Generation Computer Systems, vol. 107, pp. 941-955, 2020.",
    ]


def main() -> None:
    data = load_tables()
    dataset_table = data["dataset_comparison"]
    difficulty_table = data["dataset_difficulty"]
    redundancy_table = data["feature_redundancy"].head(12)

    document = Document()
    set_default_font(document)
    set_margins(document)
    add_page_number(document.sections[0])

    add_title_block(document)

    add_heading(document, "Abstract")
    add_body_paragraph(document, abstract_text())

    add_heading(document, "Keywords")
    add_keywords(document, "IoT security, DDoS detection, dataset analysis, intrusion detection, machine learning")

    add_heading(document, "Introduction")
    add_body_paragraph(document, introduction_text())

    add_heading(document, "Related Work")
    add_body_paragraph(document, related_work_text())

    add_heading(document, "Methodology")
    add_body_paragraph(document, methodology_text())

    add_heading(document, "Dataset Description")
    add_body_paragraph(document, dataset_description_text())
    add_table(document, dataset_table, "Table 1. Comparative statistics of the analyzed IoT DDoS datasets.")

    add_heading(document, "Dataset Analysis")
    add_body_paragraph(document, dataset_analysis_text())
    add_figure(
        document,
        ANALYSIS_DIR / "paper_figures" / "dataset_size_comparison.png",
        "Figure 1. Dataset size comparison across IoT DDoS datasets.",
    )
    add_figure(
        document,
        ANALYSIS_DIR / "paper_figures" / "class_imbalance_comparison.png",
        "Figure 2. Class imbalance comparison across IoT DDoS datasets.",
    )
    add_table(document, redundancy_table, "Table 2. Representative highly redundant feature pairs across the analyzed datasets.")

    add_heading(document, "Experimental Results")
    add_body_paragraph(document, experimental_results_text())
    add_figure(
        document,
        ADVANCED_DIR / "pca_CICIoT2023.png",
        "Figure 3. PCA projection of CICIoT2023 benign and DDoS traffic.",
    )
    add_figure(
        document,
        ADVANCED_DIR / "pca_CICDDoS2019.png",
        "Figure 4. PCA projection of CICDDoS2019 benign and DDoS traffic.",
    )
    add_figure(
        document,
        ADVANCED_DIR / "pca_TONIoT.png",
        "Figure 5. PCA projection of TON-IoT benign and DDoS traffic.",
    )
    add_figure(
        document,
        ADVANCED_DIR / "tsne_CICIoT2023.png",
        "Figure 6. t-SNE projection of CICIoT2023 benign and DDoS traffic.",
    )
    add_figure(
        document,
        ADVANCED_DIR / "tsne_CICDDoS2019.png",
        "Figure 7. t-SNE projection of CICDDoS2019 benign and DDoS traffic.",
    )
    add_figure(
        document,
        ADVANCED_DIR / "tsne_TONIoT.png",
        "Figure 8. t-SNE projection of TON-IoT benign and DDoS traffic.",
    )
    add_table(document, difficulty_table, "Table 3. Baseline ROC-AUC comparison for Logistic Regression and Random Forest.")
    add_figure(
        document,
        ANALYSIS_DIR / "paper_figures" / "dataset_difficulty_comparison.png",
        "Figure 9. Dataset difficulty comparison using baseline ROC-AUC scores.",
    )

    add_heading(document, "Discussion")
    add_body_paragraph(document, discussion_text())

    add_heading(document, "Conclusion")
    add_body_paragraph(document, conclusion_text())

    add_heading(document, "Future Work")
    add_body_paragraph(document, future_work_text())

    add_heading(document, "References")
    for ref in references_list():
        add_body_paragraph(document, ref)

    document.save(str(OUTPUT_PATH))
    print(f"Journal-ready draft saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
