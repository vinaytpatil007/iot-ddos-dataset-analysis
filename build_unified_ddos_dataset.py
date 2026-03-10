import csv
import os
import sys
from glob import glob
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import numpy as np
import pandas as pd


BASE_DIR = Path(r"D:\ddos dataset")
OUTPUT_DIR = BASE_DIR / "processed_outputs"
REPORT_PATH = BASE_DIR / "dataset_cleaning_report.md"
CHUNK_SIZE = 100_000

DATASET_ROOTS = {
    "CIC_IOT_Dataset2023": BASE_DIR / "CIC_IOT_Dataset2023",
    "CICDDoS2019": BASE_DIR / "CICDDoS2019",
    "TON_IoT Dataset": BASE_DIR / "TON_IoT Dataset",
    "BoT-IOT": BASE_DIR / "BoT-IOT",
}

OUTPUT_FILES = {
    "CIC_IOT_Dataset2023": OUTPUT_DIR / "processed_CICIoT2023_ddos.csv",
    "CICDDoS2019": OUTPUT_DIR / "processed_CICDDoS2019_ddos.csv",
    "TON_IoT Dataset": OUTPUT_DIR / "processed_TONIoT_ddos.csv",
    "BoT-IOT": OUTPUT_DIR / "processed_BoTIoT_dos_optional.csv",
}

IDENTIFIER_TOKENS = {
    "flow_id",
    "timestamp",
    "ts",
    "src_ip",
    "dst_ip",
    "source_ip",
    "destination_ip",
    "saddr",
    "daddr",
    "stime",
    "ltime",
    "smac",
    "dmac",
}

CICDDOS_DDOS_LABELS = {
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


def normalize_column(name: str) -> str:
    text = name.strip().lower().replace(" ", "_").replace("-", "_").replace(".", "_")
    while "__" in text:
        text = text.replace("__", "_")
    return text


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


def reset_output(path: Path) -> None:
    if path.exists():
        path.unlink()


def count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        return max(sum(1 for _ in handle) - 1, 0)


def summarize_existing_output(dataset_name: str, output_path: Path) -> Dict[str, object]:
    if not output_path.exists():
        return {
            "dataset_name": dataset_name,
            "output_path": output_path,
            "input_files_used": [],
            "total_samples": 0,
            "ddos_samples": 0,
            "benign_samples": 0,
            "num_features": 0,
            "feature_set": set(),
            "per_chunk_feature_sets": [],
        }

    with output_path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.reader(handle)
        final_columns = next(reader)
        label_index = final_columns.index("label")
        label_counts = {0: 0, 1: 0}
        for row in reader:
            if len(row) <= label_index:
                continue
            value = row[label_index].strip()
            if value in {"0", "1"}:
                label_counts[int(value)] = label_counts.get(int(value), 0) + 1

    return {
        "dataset_name": dataset_name,
        "output_path": output_path,
        "input_files_used": [],
        "total_samples": int(sum(label_counts.values())),
        "ddos_samples": int(label_counts.get(1, 0)),
        "benign_samples": int(label_counts.get(0, 0)),
        "num_features": max(len(final_columns) - 3, 0),
        "feature_set": set(final_columns) - {"label", "source_dataset", "attack_family"},
        "per_chunk_feature_sets": [],
    }


def append_frame(frame: pd.DataFrame, output_path: Path) -> None:
    if frame.empty:
        return
    header = not output_path.exists()
    frame.to_csv(output_path, mode="a", header=header, index=False)


def rename_columns(frame: pd.DataFrame) -> pd.DataFrame:
    renamed = {column: normalize_column(column) for column in frame.columns}
    frame = frame.rename(columns=renamed)
    unnamed = [column for column in frame.columns if column.startswith("unnamed")]
    if unnamed:
        frame = frame.drop(columns=unnamed)
    return frame


def coerce_bool_like_columns(frame: pd.DataFrame) -> pd.DataFrame:
    for column in frame.columns:
        if frame[column].dtype == object:
            lowered = frame[column].astype(str).str.strip().str.lower()
            unique_values = set(lowered.dropna().unique().tolist())
            if unique_values and unique_values.issubset({"true", "false", "t", "f", "0", "1"}):
                frame[column] = lowered.map(
                    {
                        "true": 1,
                        "t": 1,
                        "1": 1,
                        "false": 0,
                        "f": 0,
                        "0": 0,
                    }
                )
    return frame


def remove_identifier_columns(frame: pd.DataFrame) -> pd.DataFrame:
    drop_columns = []
    for column in frame.columns:
        normalized = normalize_column(column)
        if normalized in IDENTIFIER_TOKENS:
            drop_columns.append(column)
            continue
        if normalized.endswith("_ip") or normalized.endswith("_mac"):
            drop_columns.append(column)
            continue
        if normalized in {"label", "source_dataset", "attack_family"}:
            continue
    if drop_columns:
        frame = frame.drop(columns=drop_columns, errors="ignore")
    return frame


def clean_numeric_features(frame: pd.DataFrame) -> pd.DataFrame:
    frame = remove_identifier_columns(frame)
    frame = coerce_bool_like_columns(frame)

    keep_columns = []
    for column in frame.columns:
        if column in {"label", "source_dataset", "attack_family"}:
            keep_columns.append(column)
            continue
        numeric = pd.to_numeric(frame[column], errors="coerce")
        if numeric.notna().sum() == 0:
            continue
        frame[column] = numeric
        keep_columns.append(column)

    frame = frame[keep_columns].copy()
    numeric_cols = [column for column in frame.columns if column not in {"label", "source_dataset", "attack_family"}]
    if numeric_cols:
        medians = frame[numeric_cols].median(numeric_only=True)
        frame[numeric_cols] = frame[numeric_cols].fillna(medians)
        frame[numeric_cols] = frame[numeric_cols].fillna(0)
    frame["label"] = frame["label"].astype(int)
    return frame


def filter_cic_iot(chunk: pd.DataFrame, source_path: Path) -> pd.DataFrame:
    attack_folder = source_path.parent.name
    if attack_folder == "Benign_Final":
        chunk["attack_family"] = "benign"
        chunk["label"] = 0
    elif attack_folder.startswith("DDoS-"):
        chunk["attack_family"] = attack_folder
        chunk["label"] = 1
    else:
        return pd.DataFrame()
    chunk["source_dataset"] = "CIC_IOT_Dataset2023"
    return chunk


def filter_cicddos(chunk: pd.DataFrame, _: Path) -> pd.DataFrame:
    chunk = rename_columns(chunk)
    if "label" not in chunk.columns:
        return pd.DataFrame()

    labels = chunk["label"].astype(str).str.strip()
    normalized = labels.str.lower()
    benign_mask = normalized.eq("benign")
    ddos_mask = normalized.isin(CICDDOS_DDOS_LABELS)
    filtered = chunk.loc[benign_mask | ddos_mask].copy()
    if filtered.empty:
        return filtered

    filtered["attack_family"] = filtered["label"].astype(str).str.strip()
    filtered["label"] = np.where(
        filtered["attack_family"].str.lower().eq("benign"),
        0,
        1,
    )
    filtered["source_dataset"] = "CICDDoS2019"
    return filtered


def filter_ton_iot(chunk: pd.DataFrame, _: Path) -> pd.DataFrame:
    chunk = rename_columns(chunk)
    label_column = "type" if "type" in chunk.columns else "attack_cat" if "attack_cat" in chunk.columns else None
    if label_column is None:
        return pd.DataFrame()

    labels = chunk[label_column].astype(str).str.strip().str.lower()
    filtered = chunk.loc[labels.isin({"ddos", "normal"})].copy()
    if filtered.empty:
        return filtered

    filtered["attack_family"] = labels.loc[filtered.index]
    filtered["label"] = np.where(filtered["attack_family"].eq("normal"), 0, 1)
    filtered["source_dataset"] = "TON_IoT Dataset"
    return filtered


def filter_bot_iot(chunk: pd.DataFrame, _: Path) -> pd.DataFrame:
    chunk = rename_columns(chunk)
    if "category" not in chunk.columns:
        return pd.DataFrame()

    categories = chunk["category"].astype(str).str.strip().str.lower()
    filtered = chunk.loc[categories.eq("dos")].copy()
    if filtered.empty:
        return filtered

    family_column = "subcategory" if "subcategory" in filtered.columns else "category"
    filtered["attack_family"] = filtered[family_column].astype(str).str.strip()
    filtered["label"] = 1
    filtered["source_dataset"] = "BoT-IOT"
    return filtered


def iter_csv_chunks(csv_path: Path) -> Iterable[pd.DataFrame]:
    delimiter = detect_delimiter(csv_path)
    for chunk in pd.read_csv(
        csv_path,
        sep=delimiter,
        chunksize=CHUNK_SIZE,
        encoding="utf-8",
        encoding_errors="ignore",
        low_memory=False,
    ):
        yield chunk


def process_files(
    dataset_name: str,
    file_paths: List[Path],
    filter_fn,
    output_path: Path,
) -> Dict[str, object]:
    reset_output(output_path)
    source_files = []
    feature_sets: List[Set[str]] = []
    ddos_samples = 0
    benign_samples = 0

    for csv_path in file_paths:
        file_written = False
        for chunk in iter_csv_chunks(csv_path):
            filtered = filter_fn(chunk.copy(), csv_path)
            if filtered.empty:
                continue
            filtered = rename_columns(filtered)
            cleaned = clean_numeric_features(filtered)
            feature_sets.append(
                {column for column in cleaned.columns if column not in {"label", "source_dataset", "attack_family"}}
            )
            ddos_samples += int((cleaned["label"] == 1).sum())
            benign_samples += int((cleaned["label"] == 0).sum())
            append_frame(cleaned, output_path)
            file_written = True
        if file_written:
            source_files.append(str(csv_path))

    total_samples = ddos_samples + benign_samples
    final_columns = []
    if output_path.exists():
        final_columns = pd.read_csv(output_path, nrows=0).columns.tolist()

    return {
        "dataset_name": dataset_name,
        "output_path": output_path,
        "input_files_used": source_files,
        "total_samples": total_samples,
        "ddos_samples": ddos_samples,
        "benign_samples": benign_samples,
        "num_features": max(len(final_columns) - 3, 0),
        "feature_set": set(final_columns) - {"label", "source_dataset", "attack_family"},
        "per_chunk_feature_sets": feature_sets,
    }


def get_cic_iot_files(root: Path) -> List[Path]:
    ddos_files = sorted(Path(path) for path in glob(str(root / "DDoS-*" / "*.csv")))
    benign_files = sorted(Path(path) for path in glob(str(root / "Benign_Final" / "*.csv")))
    return ddos_files + benign_files


def get_cicddos_files(root: Path) -> List[Path]:
    return sorted(Path(path) for path in glob(str(root / "**" / "*.csv"), recursive=True))


def get_ton_iot_files(root: Path) -> List[Path]:
    candidates = [
        root / "Processed_datasets" / "Processed_datasets" / "Processed_Network_dataset",
        root / "Processed_datasets" / "Processed_datasets" / "Processed_IoT_dataset",
    ]
    files: List[Path] = []
    for directory in candidates:
        files.extend(sorted(Path(path) for path in glob(str(directory / "*.csv"))))
    return files


def get_bot_iot_files(root: Path) -> List[Path]:
    preferred = [
        root / "5%" / "10-best features" / "UNSW_2018_IoT_Botnet_Final_10_Best.csv",
        root / "5%" / "10-best features" / "10-best Training-Testing split" / "UNSW_2018_IoT_Botnet_Final_10_best_Training.csv",
        root / "5%" / "10-best features" / "10-best Training-Testing split" / "UNSW_2018_IoT_Botnet_Final_10_best_Testing.csv",
    ]
    return [path for path in preferred if path.exists()]


def compute_shared_features(dataset_stats: Dict[str, Dict[str, object]]) -> Dict[str, Set[str]]:
    main_datasets = ["CIC_IOT_Dataset2023", "CICDDoS2019", "TON_IoT Dataset"]
    feature_sets = [dataset_stats[name]["feature_set"] for name in main_datasets]

    all_shared = set.intersection(*feature_sets) if all(feature_sets) else set()
    cic_pair = dataset_stats["CIC_IOT_Dataset2023"]["feature_set"] & dataset_stats["CICDDoS2019"]["feature_set"]
    ton_pair = dataset_stats["CICDDoS2019"]["feature_set"] & dataset_stats["TON_IoT Dataset"]["feature_set"]
    iot_pair = dataset_stats["CIC_IOT_Dataset2023"]["feature_set"] & dataset_stats["TON_IoT Dataset"]["feature_set"]

    return {
        "all_shared": all_shared,
        "cic_iot__cicddos": cic_pair,
        "cicddos__ton_iot": ton_pair,
        "cic_iot__ton_iot": iot_pair,
    }


def render_list(items: Iterable[str]) -> str:
    items = list(items)
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in sorted(items))


def build_report(dataset_stats: Dict[str, Dict[str, object]], shared_features: Dict[str, Set[str]]) -> str:
    lines = ["# Dataset Cleaning Report", ""]
    lines.append("## Processing Summary")
    lines.append("- Objective: create cleaned DDoS-vs-benign research datasets without training any models.")
    lines.append("- Label standardization: `label = 0` for benign/normal, `label = 1` for DDoS.")
    lines.append("- Feature cleaning: removed identifier columns, dropped non-numeric columns, coerced retained features to numeric, imputed missing numeric values with per-chunk medians then `0` fallback.")
    lines.append("")

    lines.append("## Filtering Rules")
    lines.append("- CIC_IOT_Dataset2023: folder-derived labels, keep `DDoS-*` folders plus `Benign_Final`.")
    lines.append("- CICDDoS2019: keep rows with `label == BENIGN` or labels matching known DDoS families from the audit (`DrDoS_*`, `Syn`, `UDP`, `UDPLag`, `Portmap`, `TFTP`, `LDAP`, `MSSQL`, `NetBIOS`, `WebDDoS`).")
    lines.append("- TON_IoT Dataset: keep only `type == ddos` or `type == normal` from processed IoT and processed network CSVs.")
    lines.append("- BoT-IOT: excluded from the main unified dataset; saved separately as optional `DoS`-only data because the audit did not establish it as a clean DDoS benchmark.")
    lines.append("")

    lines.append("## Dataset Statistics")
    for dataset_name in ["CIC_IOT_Dataset2023", "CICDDoS2019", "TON_IoT Dataset", "BoT-IOT"]:
        stats = dataset_stats[dataset_name]
        lines.append(f"### {dataset_name}")
        lines.append(f"- Output file: `{stats['output_path']}`")
        if stats["input_files_used"]:
            lines.append(f"- Source files used: {len(stats['input_files_used'])}")
        else:
            lines.append("- Source files used: summarized from existing processed output")
        lines.append(f"- Total samples: {stats['total_samples']}")
        lines.append(f"- DDoS samples: {stats['ddos_samples']}")
        lines.append(f"- Benign samples: {stats['benign_samples']}")
        lines.append(f"- Number of cleaned numeric features: {stats['num_features']}")
        lines.append("")

    lines.append("## Feature Alignment Report")
    lines.append("- Shared features across `CIC_IOT_Dataset2023`, `CICDDoS2019`, and `TON_IoT Dataset` after strict numeric cleaning:")
    lines.append(render_list(shared_features["all_shared"]))
    lines.append("")
    lines.append("- Pairwise shared features:")
    lines.append("### CIC_IOT_Dataset2023 and CICDDoS2019")
    lines.append(render_list(shared_features["cic_iot__cicddos"]))
    lines.append("")
    lines.append("### CICDDoS2019 and TON_IoT Dataset")
    lines.append(render_list(shared_features["cicddos__ton_iot"]))
    lines.append("")
    lines.append("### CIC_IOT_Dataset2023 and TON_IoT Dataset")
    lines.append(render_list(shared_features["cic_iot__ton_iot"]))
    lines.append("")

    if not shared_features["all_shared"]:
        lines.append("## Constraint")
        lines.append("- No robust exact-name numeric feature intersection exists across all three main datasets after strict identifier removal.")
        lines.append("- Result: the saved processed CSVs are clean per-dataset research tables, but a single merged aligned table is intentionally not created in this step.")
        lines.append("- Next step for true cross-dataset fusion would require explicit semantic feature mapping or learned representation alignment.")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    selected = set(sys.argv[1:]) if len(sys.argv) > 1 else set(DATASET_ROOTS.keys())
    dataset_stats: Dict[str, Dict[str, object]] = {}

    jobs = {
        "CIC_IOT_Dataset2023": (
            get_cic_iot_files(DATASET_ROOTS["CIC_IOT_Dataset2023"]),
            filter_cic_iot,
        ),
        "CICDDoS2019": (
            get_cicddos_files(DATASET_ROOTS["CICDDoS2019"]),
            filter_cicddos,
        ),
        "TON_IoT Dataset": (
            get_ton_iot_files(DATASET_ROOTS["TON_IoT Dataset"]),
            filter_ton_iot,
        ),
        "BoT-IOT": (
            get_bot_iot_files(DATASET_ROOTS["BoT-IOT"]),
            filter_bot_iot,
        ),
    }

    for dataset_name, (files, filter_fn) in jobs.items():
        output_path = OUTPUT_FILES[dataset_name]
        if dataset_name in selected:
            dataset_stats[dataset_name] = process_files(dataset_name, files, filter_fn, output_path)
        else:
            dataset_stats[dataset_name] = summarize_existing_output(dataset_name, output_path)

    shared_features = compute_shared_features(dataset_stats)
    report = build_report(dataset_stats, shared_features)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
