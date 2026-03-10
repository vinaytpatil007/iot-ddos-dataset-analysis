import os
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd


DATASET_PATHS = {
    "CIC_IOT_Dataset2023": Path(r"D:\ddos dataset\CIC_IOT_Dataset2023"),
    "CICDDoS2019": Path(r"D:\ddos dataset\CICDDoS2019"),
    "TON_IoT Dataset": Path(r"D:\ddos dataset\TON_IoT Dataset"),
    "BoT-IOT": Path(r"D:\ddos dataset\BoT-IOT"),
}

LABEL_PRIORITY = [
    "attack_cat",
    "attack_category",
    "subcategory",
    "category",
    "type",
    "attack_type",
    "label",
    "class",
    "attack",
]
SAMPLE_FILES_PER_DATASET = 2
SAMPLE_ROWS = 5
CHUNK_SIZE = 100_000
REPORT_PATH = Path(r"D:\ddos dataset\dataset_analysis_report.md")


@dataclass
class CsvAnalysis:
    path: Path
    delimiter: str
    row_count: int
    columns: List[str]
    normalized_map: Dict[str, str]
    label_column: Optional[str]
    dtypes: Dict[str, str]
    numeric_columns: List[str]
    categorical_columns: List[str]
    missing_values: Dict[str, int]
    basic_stats: pd.DataFrame
    sample_rows: pd.DataFrame


def normalize_column(name: str) -> str:
    cleaned = name.strip().lower().replace(" ", "_")
    cleaned = cleaned.replace("-", "_").replace(".", "_")
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned


def detect_delimiter(csv_path: Path) -> str:
    with csv_path.open("r", encoding="utf-8", errors="ignore") as handle:
        header = handle.readline()

    counts = {
        ",": header.count(","),
        ";": header.count(";"),
        "\t": header.count("\t"),
        "|": header.count("|"),
    }
    delimiter = max(counts.items(), key=lambda item: item[1])[0]
    return delimiter if counts[delimiter] > 0 else ","


def count_data_rows(csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8", errors="ignore") as handle:
        return max(sum(1 for _ in handle) - 1, 0)


def iter_files(root: Path) -> Iterable[Path]:
    for current_root, _, files in os.walk(root):
        for file_name in sorted(files):
            yield Path(current_root) / file_name


def format_tree(root: Path) -> str:
    lines = [f"{root.name}"]

    def walk(directory: Path, prefix: str = "") -> None:
        entries = sorted(directory.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))
        for index, entry in enumerate(entries):
            connector = "`-- " if index == len(entries) - 1 else "|-- "
            lines.append(f"{prefix}{connector}{entry.name}")
            if entry.is_dir():
                extension = "    " if index == len(entries) - 1 else "|   "
                walk(entry, prefix + extension)

    walk(root)
    return "\n".join(lines)


def detect_label_column(columns: List[str]) -> Optional[str]:
    normalized = {normalize_column(column): column for column in columns}
    for candidate in LABEL_PRIORITY:
        if candidate in normalized:
            return normalized[candidate]
    return None


def load_csv_sample(csv_path: Path) -> pd.DataFrame:
    delimiter = detect_delimiter(csv_path)
    sample = pd.read_csv(
        csv_path,
        sep=delimiter,
        nrows=SAMPLE_ROWS,
        encoding="utf-8",
        encoding_errors="ignore",
        low_memory=False,
    )
    unnamed = [column for column in sample.columns if normalize_column(column).startswith("unnamed")]
    if unnamed:
        sample = sample.drop(columns=unnamed)
    return sample


def analyze_csv(csv_path: Path) -> CsvAnalysis:
    delimiter = detect_delimiter(csv_path)
    sample = pd.read_csv(
        csv_path,
        sep=delimiter,
        nrows=SAMPLE_ROWS,
        encoding="utf-8",
        encoding_errors="ignore",
        low_memory=False,
    )
    unnamed = [column for column in sample.columns if normalize_column(column).startswith("unnamed")]
    if unnamed:
        sample = sample.drop(columns=unnamed)

    columns = list(sample.columns)
    normalized_map = {normalize_column(column): column for column in columns}
    label_column = detect_label_column(columns)
    row_count = count_data_rows(csv_path)

    full_sample = pd.read_csv(
        csv_path,
        sep=delimiter,
        nrows=min(10_000, max(row_count, SAMPLE_ROWS)),
        encoding="utf-8",
        encoding_errors="ignore",
        low_memory=False,
    )
    unnamed_full = [column for column in full_sample.columns if normalize_column(column).startswith("unnamed")]
    if unnamed_full:
        full_sample = full_sample.drop(columns=unnamed_full)

    numeric_columns = full_sample.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = [column for column in full_sample.columns if column not in numeric_columns]
    missing_values = full_sample.isna().sum().to_dict()
    basic_stats = full_sample[numeric_columns].describe().transpose() if numeric_columns else pd.DataFrame()

    return CsvAnalysis(
        path=csv_path,
        delimiter=delimiter,
        row_count=row_count,
        columns=columns,
        normalized_map=normalized_map,
        label_column=label_column,
        dtypes={column: str(dtype) for column, dtype in full_sample.dtypes.items()},
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
        missing_values=missing_values,
        basic_stats=basic_stats,
        sample_rows=sample,
    )


def choose_sample_files(root: Path, limit: int = SAMPLE_FILES_PER_DATASET) -> List[Path]:
    candidates = [path for path in iter_files(root) if path.suffix.lower() == ".csv"]
    preferred = []
    for path in candidates:
        name = path.name.lower()
        if any(token in name for token in ("train", "test", "feature", "dataset", "flood", "drdos")):
            preferred.append(path)
    ordered = preferred + [path for path in candidates if path not in preferred]
    return ordered[:limit]


def count_labels_in_csv(csv_path: Path, label_column: str, delimiter: str) -> Counter:
    counts: Counter = Counter()
    usecols = [label_column]
    for chunk in pd.read_csv(
        csv_path,
        sep=delimiter,
        usecols=usecols,
        chunksize=CHUNK_SIZE,
        encoding="utf-8",
        encoding_errors="ignore",
        low_memory=False,
    ):
        series = chunk[label_column].astype(str).str.strip()
        counts.update(series.value_counts(dropna=False).to_dict())
    return counts


def aggregate_dataset_attacks(dataset_name: str, root: Path) -> Tuple[Counter, List[str]]:
    attack_counts: Counter = Counter()
    notes: List[str] = []

    for csv_path in iter_files(root):
        if csv_path.suffix.lower() != ".csv":
            continue

        delimiter = detect_delimiter(csv_path)
        try:
            header_df = pd.read_csv(
                csv_path,
                sep=delimiter,
                nrows=0,
                encoding="utf-8",
                encoding_errors="ignore",
                low_memory=False,
            )
        except Exception as exc:
            notes.append(f"Skipped label analysis for {csv_path.name}: {exc}")
            continue

        columns = [column for column in header_df.columns if not normalize_column(column).startswith("unnamed")]
        label_column = detect_label_column(columns)

        if dataset_name == "CIC_IOT_Dataset2023" and label_column is None:
            label_value = csv_path.parent.name
            attack_counts[label_value] += count_data_rows(csv_path)
            continue

        if label_column is None:
            notes.append(f"No label-like column detected in {csv_path.name}")
            continue

        try:
            csv_counts = count_labels_in_csv(csv_path, label_column, delimiter)
            attack_counts.update(csv_counts)
        except Exception as exc:
            notes.append(f"Failed to count labels in {csv_path.name}: {exc}")

    return attack_counts, notes


def summarize_file_types(root: Path) -> Counter:
    counts: Counter = Counter()
    for path in iter_files(root):
        suffix = path.suffix.lower() if path.suffix else "[no_extension]"
        counts[suffix] += 1
    return counts


def summarize_structure(root: Path) -> Dict[str, object]:
    files = list(iter_files(root))
    directories = []
    for current_root, subdirs, _ in os.walk(root):
        for subdir in subdirs:
            directories.append(str(Path(current_root) / subdir))

    return {
        "file_count": len(files),
        "subfolders": directories,
        "file_types": summarize_file_types(root),
        "tree": format_tree(root),
    }


def render_counter(counter: Counter, limit: Optional[int] = None) -> str:
    items = counter.most_common(limit)
    if not items:
        return "- None detected"
    return "\n".join(f"- {key}: {value}" for key, value in items)


def render_sample_rows(df: pd.DataFrame) -> str:
    if df.empty:
        return "No rows loaded."
    return df.to_string(index=False)


def render_basic_stats(stats: pd.DataFrame, limit: int = 10) -> str:
    if stats.empty:
        return "No numeric columns detected."
    clipped = stats[["count", "mean", "std", "min", "max"]].head(limit)
    return clipped.to_string()


def identify_ddos_presence(dataset_name: str, attack_counts: Counter) -> Tuple[bool, List[str]]:
    ddos_labels: List[str] = []
    cicddos_labels = {
        "drdos_dns",
        "drdos_ldap",
        "drdos_mssql",
        "drdos_netbios",
        "drdos_ntp",
        "drdos_snmp",
        "drdos_ssdp",
        "drdos_udp",
        "syn",
        "udp",
        "udp-lag",
        "udplag",
        "portmap",
        "tftp",
        "ldap",
        "mssql",
        "netbios",
        "webddos",
    }

    for label in attack_counts:
        normalized = str(label).strip().lower()
        if "ddos" in normalized:
            ddos_labels.append(str(label))
        elif dataset_name == "CICDDoS2019" and normalized in cicddos_labels:
            ddos_labels.append(str(label))

    return bool(ddos_labels), sorted(ddos_labels)


def recommendation_text() -> str:
    return "\n".join(
        [
            "1. Extract DDoS traffic by dataset-specific rules:",
            "   - CIC_IOT_Dataset2023: derive the label from the parent folder name and keep folders starting with `DDoS-`.",
            "   - CICDDoS2019: keep rows whose `Label` contains DDoS families such as `DrDoS_*`, `UDP`, `Syn`, `TFTP`, `Portmap`, and `UDPLag` based on your protocol scope.",
            "   - TON_IoT Dataset: keep rows where `type == ddos`; discard or separately archive other attack classes.",
            "   - BoT-IOT: treat `category == DoS` as related traffic, but validate whether it matches your DDoS definition before mixing it with reflection/flood datasets.",
            "",
            "2. Unify labels to a common schema such as:",
            "   - `binary_label`: `ddos` or `benign`",
            "   - `attack_family`: original dataset family name such as `DrDoS_DNS`, `DDoS-SYN_Flood`, or `ddos`",
            "   - `source_dataset`: dataset identifier",
            "",
            "3. Handle non-DDoS attack types by removing them for binary DDoS detection or storing them as a third `other_attack` class if you want open-set evaluation.",
            "",
            "4. Preprocessing strategy:",
            "   - remove obvious index columns such as `Unnamed: 0`",
            "   - normalize column names to lowercase snake_case",
            "   - cast labels consistently",
            "   - impute or flag missing values before scaling",
            "   - split by source file or capture session to reduce leakage",
            "",
            "5. Feature alignment strategy:",
            "   - keep dataset-specific models if feature overlap is low",
            "   - otherwise intersect shared flow features across datasets",
            "   - document delimiter, units, and feature meaning before merging",
            "   - avoid naive concatenation of unrelated schemas such as TON-IoT network logs and CIC flow statistics",
        ]
    )


def generate_report() -> str:
    sections: List[str] = ["# DDoS Dataset Analysis Report", ""]

    for dataset_name, root in DATASET_PATHS.items():
        structure = summarize_structure(root)
        sample_files = choose_sample_files(root)
        sample_analyses = [analyze_csv(path) for path in sample_files]
        attack_counts, attack_notes = aggregate_dataset_attacks(dataset_name, root)
        ddos_exists, ddos_labels = identify_ddos_presence(dataset_name, attack_counts)

        sections.append(f"## Dataset: {dataset_name}")
        sections.append(f"- Path: `{root}`")
        sections.append(f"- Total files: {structure['file_count']}")
        sections.append(f"- Total subfolders: {len(structure['subfolders'])}")
        sections.append("- File types:")
        sections.append(render_counter(structure["file_types"]))
        sections.append("")
        sections.append("### Folder Structure")
        sections.append("```text")
        sections.append(structure["tree"])
        sections.append("```")
        sections.append("")

        sections.append("### Schema Inspection")
        for analysis in sample_analyses:
            sections.append(f"#### Sample File: `{analysis.path}`")
            sections.append(f"- Delimiter: `{analysis.delimiter}`")
            sections.append(f"- Estimated rows: {analysis.row_count}")
            sections.append(f"- Number of features: {len(analysis.columns)}")
            sections.append(f"- Label column: `{analysis.label_column}`" if analysis.label_column else "- Label column: not detected")
            sections.append(f"- Numeric features: {len(analysis.numeric_columns)}")
            sections.append(f"- Categorical features: {len(analysis.categorical_columns)}")
            sections.append("- Columns:")
            sections.append("\n".join(f"  - {column}" for column in analysis.columns))
            if analysis.label_column and analysis.label_column in analysis.sample_rows.columns:
                categories = sorted(analysis.sample_rows[analysis.label_column].astype(str).str.strip().unique().tolist())
                sections.append("- Sample attack categories:")
                sections.append("\n".join(f"  - {value}" for value in categories))
            sections.append("- Sample rows:")
            sections.append(render_sample_rows(analysis.sample_rows))
            sections.append("- Missing values in sample:")
            missing_nonzero = {key: value for key, value in analysis.missing_values.items() if value > 0}
            sections.append(render_counter(Counter(missing_nonzero)) if missing_nonzero else "- None in sampled rows")
            sections.append("- Basic statistics for numeric features:")
            sections.append(render_basic_stats(analysis.basic_stats))
            sections.append("")

        sections.append("### Attack Type Analysis")
        sections.append(f"- DDoS present: {'Yes' if ddos_exists else 'No'}")
        sections.append(f"- DDoS-related labels: {', '.join(ddos_labels) if ddos_labels else 'None detected'}")
        sections.append("- Class distribution:")
        sections.append(render_counter(attack_counts))
        if attack_notes:
            sections.append("- Notes:")
            sections.append("\n".join(f"  - {note}" for note in attack_notes))
        sections.append("")

        representative = sample_analyses[0]
        sections.append("### Feature Analysis")
        sections.append(f"- Representative file: `{representative.path}`")
        sections.append(f"- Number of features: {len(representative.columns)}")
        sections.append(f"- Numeric feature count: {len(representative.numeric_columns)}")
        sections.append(f"- Categorical feature count: {len(representative.categorical_columns)}")
        sections.append("- Numeric features:")
        sections.append("\n".join(f"  - {column}" for column in representative.numeric_columns[:50]) or "  - None")
        sections.append("- Categorical features:")
        sections.append("\n".join(f"  - {column}" for column in representative.categorical_columns[:50]) or "  - None")
        sections.append("")

    sections.append("## Strategy Recommendation")
    sections.append(recommendation_text())
    sections.append("")
    return "\n".join(sections)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    report = generate_report()
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nReport written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
