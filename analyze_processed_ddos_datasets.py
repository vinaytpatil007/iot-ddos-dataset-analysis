import csv
import math
import os
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


BASE_DIR = Path(r"D:\ddos dataset")
INPUT_DIR = BASE_DIR / "processed_outputs"
OUTPUT_DIR = BASE_DIR / "analysis_results"
FIGURES_DIR = OUTPUT_DIR / "figures"
FEATURE_DIST_DIR = FIGURES_DIR / "feature_distribution"

DATASETS = {
    "CICIoT2023": INPUT_DIR / "processed_CICIoT2023_ddos.csv",
    "CICDDoS2019": INPUT_DIR / "processed_CICDDoS2019_ddos.csv",
    "TONIoT": INPUT_DIR / "processed_TONIoT_ddos.csv",
    "BoTIoT_optional": INPUT_DIR / "processed_BoTIoT_dos_optional.csv",
}

MAIN_DATASETS = ["CICIoT2023", "CICDDoS2019", "TONIoT"]
MAX_ROWS_DISTRIBUTION = 250_000
MAX_ROWS_CORRELATION = 100_000
MAX_ROWS_IMPORTANCE = 120_000
TOP_FEATURES_TO_PLOT = 12
TOP_IMPORTANCE = 20
RANDOM_STATE = 42


def ensure_directories() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    FEATURE_DIST_DIR.mkdir(parents=True, exist_ok=True)


def read_header(path: Path) -> List[str]:
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.reader(handle)
        return next(reader)


def count_rows_and_labels(path: Path) -> Dict[str, int]:
    total = 0
    ddos = 0
    benign = 0

    for chunk in pd.read_csv(path, usecols=["label"], chunksize=100_000, dtype={"label": "string"}, low_memory=False):
        labels = pd.to_numeric(chunk["label"], errors="coerce").dropna().astype(int)
        counts = labels.value_counts().to_dict()
        total += int(len(labels))
        ddos += int(counts.get(1, 0))
        benign += int(counts.get(0, 0))

    return {"samples": total, "ddos": ddos, "benign": benign}


def load_sample(path: Path, max_rows: int) -> pd.DataFrame:
    frame = pd.read_csv(path, nrows=max_rows, low_memory=False)
    frame["label"] = pd.to_numeric(frame["label"], errors="coerce")
    frame = frame.dropna(subset=["label"]).copy()
    frame["label"] = frame["label"].astype(int)
    return frame


def load_balanced_model_sample(path: Path, max_rows: int) -> pd.DataFrame:
    target_per_class = max_rows // 2
    collected = {0: [], 1: []}
    counts = {0: 0, 1: 0}

    for chunk in pd.read_csv(path, chunksize=100_000, low_memory=False):
        chunk["label"] = pd.to_numeric(chunk["label"], errors="coerce")
        chunk = chunk.dropna(subset=["label"]).copy()
        chunk["label"] = chunk["label"].astype(int)

        for label_value in [0, 1]:
            if counts[label_value] >= target_per_class:
                continue
            subset = chunk[chunk["label"] == label_value]
            if subset.empty:
                continue
            needed = target_per_class - counts[label_value]
            take = subset.sample(
                n=min(needed, len(subset)),
                random_state=RANDOM_STATE,
            ) if len(subset) > needed else subset
            collected[label_value].append(take)
            counts[label_value] += len(take)

        if counts[0] >= target_per_class and counts[1] >= target_per_class:
            break

    frames = [pd.concat(collected[label], ignore_index=True) for label in [0, 1] if collected[label]]
    if not frames:
        return pd.DataFrame()
    result = pd.concat(frames, ignore_index=True)
    return result.sample(frac=1.0, random_state=RANDOM_STATE).reset_index(drop=True)


def numeric_feature_columns(frame: pd.DataFrame) -> List[str]:
    excluded = {"label", "attack_family", "source_dataset"}
    return [column for column in frame.columns if column not in excluded and pd.api.types.is_numeric_dtype(frame[column])]


def categorical_feature_columns(frame: pd.DataFrame) -> List[str]:
    excluded = {"label", "attack_family", "source_dataset"}
    return [column for column in frame.columns if column not in excluded and not pd.api.types.is_numeric_dtype(frame[column])]


def sanitize_numeric_frame(frame: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    cleaned = frame.copy()
    for column in feature_cols:
        series = pd.to_numeric(cleaned[column], errors="coerce")
        series = series.replace([np.inf, -np.inf], np.nan)
        finite = series.dropna()
        if not finite.empty:
            upper = finite.quantile(0.999)
            lower = finite.quantile(0.001)
            series = series.clip(lower=lower, upper=upper)
            fill_value = finite.median()
        else:
            fill_value = 0.0
        cleaned[column] = series.fillna(fill_value)
    return cleaned


def save_dataset_summary(summary_rows: List[Dict[str, object]]) -> pd.DataFrame:
    summary_df = pd.DataFrame(summary_rows)
    summary_df = summary_df[["Dataset", "Samples", "DDoS", "Benign", "Features"]]
    summary_df.to_csv(OUTPUT_DIR / "dataset_summary.csv", index=False)
    return summary_df


def plot_class_distribution(dataset_name: str, ddos: int, benign: int) -> float:
    plt.figure(figsize=(6, 4))
    values = [benign, ddos]
    labels = ["Benign", "DDoS"]
    palette = ["#5B8E7D", "#D1495B"]
    ax = sns.barplot(x=labels, y=values, hue=labels, palette=palette, legend=False)
    ax.set_title(f"Class Distribution: {dataset_name}")
    ax.set_ylabel("Samples")
    for index, value in enumerate(values):
        ax.text(index, value, f"{value:,}", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"class_distribution_{dataset_name}.png", dpi=200)
    plt.close()
    return ddos / benign if benign > 0 else math.inf


def compute_feature_stats(frame: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    stats = frame[feature_cols].agg(["mean", "std", "min", "max", "skew"]).transpose()
    stats = stats.sort_index()
    return stats


def plot_feature_distributions(dataset_name: str, frame: pd.DataFrame, feature_cols: List[str]) -> List[str]:
    selected = feature_cols[:TOP_FEATURES_TO_PLOT]
    plotted = []
    for feature in selected:
        plt.figure(figsize=(7, 4))
        sns.histplot(frame[feature], bins=50, kde=False, color="#2A6F97")
        plt.title(f"{dataset_name}: {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.tight_layout()
        filename = FEATURE_DIST_DIR / f"{dataset_name}_{feature}_distribution.png"
        plt.savefig(filename, dpi=180)
        plt.close()
        plotted.append(filename.name)
    return plotted


def plot_correlation_heatmap(dataset_name: str, frame: pd.DataFrame, feature_cols: List[str]) -> None:
    selected = feature_cols[: min(25, len(feature_cols))]
    corr = frame[selected].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, cmap="coolwarm", center=0, square=True)
    plt.title(f"Correlation Heatmap: {dataset_name}")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"correlation_heatmap_{dataset_name}.png", dpi=220)
    plt.close()


def train_feature_importance(dataset_name: str, frame: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    if frame["label"].nunique() < 2:
        return pd.DataFrame(columns=["feature", "importance"])

    sample_size = min(MAX_ROWS_IMPORTANCE, len(frame))
    sampled = frame.sample(n=sample_size, random_state=RANDOM_STATE) if len(frame) > sample_size else frame.copy()

    x = sampled[feature_cols]
    y = sampled["label"]
    x_train, _, y_train, _ = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y if y.nunique() > 1 else None,
        random_state=RANDOM_STATE,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=RANDOM_STATE,
        n_jobs=1,
        class_weight="balanced_subsample",
    )
    model.fit(x_train, y_train)
    importances = pd.DataFrame(
        {
            "feature": feature_cols,
            "importance": model.feature_importances_,
        }
    ).sort_values("importance", ascending=False)

    top = importances.head(TOP_IMPORTANCE).sort_values("importance", ascending=True)
    plt.figure(figsize=(8, 7))
    plt.barh(top["feature"], top["importance"], color="#E09F3E")
    plt.title(f"Top Feature Importances: {dataset_name}")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"feature_importance_{dataset_name}.png", dpi=220)
    plt.close()

    importances.to_csv(OUTPUT_DIR / f"feature_importance_{dataset_name}.csv", index=False)
    return importances


def plot_comparison(summary_df: pd.DataFrame, imbalance_map: Dict[str, float]) -> None:
    main_df = summary_df[summary_df["Dataset"].isin(MAIN_DATASETS)].copy()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=main_df, x="Dataset", y="Samples", hue="Dataset", palette="Blues_d", legend=False)
    plt.title("Dataset Size Comparison")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "dataset_size_comparison.png", dpi=220)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=main_df, x="Dataset", y="Features", hue="Dataset", palette="Greens_d", legend=False)
    plt.title("Feature Count Comparison")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "feature_count_comparison.png", dpi=220)
    plt.close()

    imbalance_df = pd.DataFrame(
        {"Dataset": list(imbalance_map.keys()), "ImbalanceRatio": list(imbalance_map.values())}
    )
    imbalance_df = imbalance_df[imbalance_df["Dataset"].isin(MAIN_DATASETS)]
    plt.figure(figsize=(8, 5))
    sns.barplot(data=imbalance_df, x="Dataset", y="ImbalanceRatio", hue="Dataset", palette="Reds_d", legend=False)
    plt.title("Class Imbalance Comparison (DDoS / Benign)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "class_imbalance_comparison.png", dpi=220)
    plt.close()


def build_report(
    summary_df: pd.DataFrame,
    stats_map: Dict[str, pd.DataFrame],
    skew_map: Dict[str, List[str]],
    imbalance_map: Dict[str, float],
    importance_map: Dict[str, pd.DataFrame],
) -> str:
    lines = ["# Dataset Analysis Results", ""]
    lines.append("## Dataset Comparison")
    lines.append("```text")
    lines.append(summary_df.to_string(index=False))
    lines.append("```")
    lines.append("")

    lines.append("## Class Imbalance Discussion")
    for dataset, ratio in imbalance_map.items():
        ratio_text = "infinite" if math.isinf(ratio) else f"{ratio:.2f}"
        lines.append(f"- {dataset}: DDoS/Benign ratio = {ratio_text}")
    lines.append("")

    lines.append("## Feature Statistics")
    for dataset in MAIN_DATASETS:
        stats = stats_map[dataset]
        lines.append(f"### {dataset}")
        lines.append("- Top skewed features:")
        if skew_map[dataset]:
            for feature in skew_map[dataset][:10]:
                lines.append(f"  - {feature}")
        else:
            lines.append("  - None detected above threshold")
        lines.append("- Summary statistics preview:")
        lines.append("```text")
        lines.append(stats.head(10).to_string())
        lines.append("```")
        top_importance = importance_map[dataset].head(10)
        lines.append("- Top feature importance preview:")
        lines.append("```text")
        lines.append(top_importance.to_string(index=False))
        lines.append("```")
        lines.append("")

    lines.append("## Strengths and Weaknesses")
    lines.append("- CICIoT2023: very large IoT-focused DDoS corpus with many DDoS families, but highly imbalanced and feature schema is specific to this dataset.")
    lines.append("- CICDDoS2019: strong network-flow benchmark with rich features, but the benign class is extremely small in the processed output and may limit fair evaluation.")
    lines.append("- TONIoT: contains both normal and DDoS samples with a more balanced cleaned subset than CICDDoS2019, but fewer numeric features after strict cleaning.")
    lines.append("- BoTIoT optional: useful for auxiliary DoS/botnet behavior analysis, but it remains unsuitable as a primary benign-vs-DDoS benchmark because the optional output has no benign class.")
    lines.append("")
    lines.append("## Output Notes")
    lines.append(f"- Summary CSV: `{OUTPUT_DIR / 'dataset_summary.csv'}`")
    lines.append(f"- Figures directory: `{FIGURES_DIR}`")
    lines.append(f"- Feature distribution figures: `{FEATURE_DIST_DIR}`")
    return "\n".join(lines)


def main() -> None:
    ensure_directories()
    sns.set_theme(style="whitegrid")

    summary_rows: List[Dict[str, object]] = []
    stats_map: Dict[str, pd.DataFrame] = {}
    skew_map: Dict[str, List[str]] = {}
    imbalance_map: Dict[str, float] = {}
    importance_map: Dict[str, pd.DataFrame] = {}

    for dataset_name, path in DATASETS.items():
        counts = count_rows_and_labels(path)
        sample = load_sample(path, MAX_ROWS_DISTRIBUTION)
        feature_cols = numeric_feature_columns(sample)
        categorical_cols = categorical_feature_columns(sample)
        sample = sanitize_numeric_frame(sample, feature_cols)

        summary_rows.append(
            {
                "Dataset": dataset_name,
                "Samples": counts["samples"],
                "DDoS": counts["ddos"],
                "Benign": counts["benign"],
                "Features": len(feature_cols) + len(categorical_cols),
            }
        )

        stats = compute_feature_stats(sample, feature_cols)
        stats.to_csv(OUTPUT_DIR / f"feature_statistics_{dataset_name}.csv")
        stats_map[dataset_name] = stats
        skewed = stats.index[stats["skew"].abs() > 1.0].tolist()
        skew_map[dataset_name] = skewed

        plot_feature_distributions(dataset_name, sample, feature_cols)

        if dataset_name in MAIN_DATASETS:
            imbalance_map[dataset_name] = plot_class_distribution(dataset_name, counts["ddos"], counts["benign"])

            corr_sample = sample if len(sample) <= MAX_ROWS_CORRELATION else sample.sample(
                n=MAX_ROWS_CORRELATION,
                random_state=RANDOM_STATE,
            )
            plot_correlation_heatmap(dataset_name, corr_sample, feature_cols)
            model_sample = load_balanced_model_sample(path, MAX_ROWS_IMPORTANCE)
            if not model_sample.empty:
                model_features = numeric_feature_columns(model_sample)
                model_sample = sanitize_numeric_frame(model_sample, model_features)
                importance_map[dataset_name] = train_feature_importance(dataset_name, model_sample, model_features)
            else:
                importance_map[dataset_name] = pd.DataFrame(columns=["feature", "importance"])
        else:
            importance_map[dataset_name] = pd.DataFrame(columns=["feature", "importance"])

    summary_df = save_dataset_summary(summary_rows)
    plot_comparison(summary_df, imbalance_map)
    report = build_report(summary_df, stats_map, skew_map, imbalance_map, importance_map)
    (OUTPUT_DIR / "dataset_analysis_results.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
