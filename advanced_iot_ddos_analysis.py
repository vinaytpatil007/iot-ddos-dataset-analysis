import math
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import entropy as shannon_entropy
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(r"D:\ddos dataset")
OUTPUT_DIR = BASE_DIR / "analysis_results" / "advanced_analysis"

DATASETS = {
    "CICIoT2023": BASE_DIR / "processed_outputs" / "processed_CICIoT2023_ddos.csv",
    "CICDDoS2019": BASE_DIR / "processed_outputs" / "processed_CICDDoS2019_ddos.csv",
    "TONIoT": BASE_DIR / "processed_outputs" / "processed_TONIoT_ddos.csv",
}

RANDOM_STATE = 42
COUNT_CHUNK = 100_000
MAX_VIS_ROWS = 100_000
MAX_TSNE_ROWS = 5_000
MAX_MODEL_ROWS = 120_000
MAX_REDUNDANCY_ROWS = 60_000
MAX_HEATMAP_FEATURES = 25
ENTROPY_BINS = 20


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def count_dataset(path: Path) -> Dict[str, int]:
    total = 0
    ddos = 0
    benign = 0
    for chunk in pd.read_csv(path, usecols=["label"], chunksize=COUNT_CHUNK, dtype={"label": "string"}, low_memory=False):
        labels = pd.to_numeric(chunk["label"], errors="coerce").dropna().astype(int)
        values = labels.value_counts().to_dict()
        total += int(len(labels))
        ddos += int(values.get(1, 0))
        benign += int(values.get(0, 0))
    return {"samples": total, "ddos": ddos, "benign": benign}


def sample_dataset(path: Path, max_rows: int, total_rows: int) -> pd.DataFrame:
    frac = min(1.0, max_rows / max(total_rows, 1))
    frames: List[pd.DataFrame] = []

    for chunk_index, chunk in enumerate(pd.read_csv(path, chunksize=COUNT_CHUNK, low_memory=False)):
        chunk["label"] = pd.to_numeric(chunk["label"], errors="coerce")
        chunk = chunk.dropna(subset=["label"]).copy()
        chunk["label"] = chunk["label"].astype(int)
        sampled = chunk.sample(frac=frac, random_state=RANDOM_STATE + chunk_index) if frac < 1.0 else chunk
        frames.append(sampled)

    if not frames:
        return pd.DataFrame()

    result = pd.concat(frames, ignore_index=True)
    if len(result) > max_rows:
        result = result.sample(n=max_rows, random_state=RANDOM_STATE).reset_index(drop=True)
    return result


def prepare_features(frame: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, List[str]]:
    numeric = frame.select_dtypes(include=[np.number]).copy()
    if "label" not in numeric.columns:
        raise ValueError("Expected numeric label column.")

    y = numeric["label"].astype(int)
    x = numeric.drop(columns=["label"], errors="ignore")
    x = x.replace([np.inf, -np.inf], np.nan)

    for column in x.columns:
        finite = x[column].dropna()
        if finite.empty:
            x[column] = 0.0
            continue
        lower = finite.quantile(0.001)
        upper = finite.quantile(0.999)
        x[column] = x[column].clip(lower=lower, upper=upper)
        x[column] = x[column].fillna(finite.median())

    return x, y, x.columns.tolist()


def scale_features(x: pd.DataFrame) -> np.ndarray:
    scaler = StandardScaler()
    return scaler.fit_transform(x)


def plot_embedding(points: np.ndarray, labels: pd.Series, title: str, out_path: Path) -> None:
    plot_df = pd.DataFrame({"x": points[:, 0], "y": points[:, 1], "label": labels.map({0: "Benign", 1: "DDoS"})})
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=plot_df,
        x="x",
        y="y",
        hue="label",
        palette={"Benign": "#2A9D8F", "DDoS": "#E76F51"},
        s=18,
        alpha=0.65,
        edgecolor=None,
    )
    plt.title(title)
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()


def evaluate_classifier(model, x: pd.DataFrame, y: pd.Series, dataset_name: str, model_name: str) -> Dict[str, object]:
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.3,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    probabilities = model.predict_proba(x_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(x_test)

    return {
        "Dataset": dataset_name,
        "Model": model_name,
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1_score": f1_score(y_test, predictions, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probabilities),
    }


def compute_entropy_scores(dataset_name: str, x: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in x.columns:
        values = x[column].to_numpy()
        counts, _ = np.histogram(values, bins=ENTROPY_BINS)
        probs = counts[counts > 0] / counts.sum() if counts.sum() > 0 else np.array([1.0])
        rows.append({"Dataset": dataset_name, "Feature": column, "Entropy": float(shannon_entropy(probs, base=2))})
    return pd.DataFrame(rows).sort_values("Entropy", ascending=False)


def plot_entropy_top_features(entropy_df: pd.DataFrame) -> None:
    top_rows = []
    for dataset_name in entropy_df["Dataset"].unique():
        top_rows.append(entropy_df[entropy_df["Dataset"] == dataset_name].head(10))
    plot_df = pd.concat(top_rows, ignore_index=True)

    plt.figure(figsize=(12, 8))
    sns.barplot(data=plot_df, x="Entropy", y="Feature", hue="Dataset")
    plt.title("Top Feature Entropy Scores")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "entropy_top_features.png", dpi=300)
    plt.close()


def compute_redundancy(dataset_name: str, x: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    corr = x.corr().abs()
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    upper = corr.where(mask)
    rows = []
    for col1 in upper.columns:
        for col2, value in upper[col1].dropna().items():
            if value > 0.95:
                rows.append({"Dataset": dataset_name, "Feature1": col1, "Feature2": col2, "Correlation": value})
    report = pd.DataFrame(rows).sort_values("Correlation", ascending=False) if rows else pd.DataFrame(
        columns=["Dataset", "Feature1", "Feature2", "Correlation"]
    )
    return corr, report


def plot_redundant_feature_heatmap(corr_maps: Dict[str, pd.DataFrame], redundancy_reports: Dict[str, pd.DataFrame]) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for axis, dataset_name in zip(axes, DATASETS.keys()):
        report = redundancy_reports[dataset_name]
        corr = corr_maps[dataset_name]
        if not report.empty:
            features = pd.unique(report[["Feature1", "Feature2"]].values.ravel()).tolist()
        else:
            features = corr.columns[: min(10, len(corr.columns))].tolist()

        subset = corr.loc[features, features]
        sns.heatmap(subset, ax=axis, cmap="mako", square=True, cbar=axis is axes[-1])
        axis.set_title(dataset_name)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "redundant_feature_heatmap.png", dpi=300)
    plt.close()


def write_report(
    separability_df: pd.DataFrame,
    difficulty_df: pd.DataFrame,
    entropy_df: pd.DataFrame,
    redundancy_df: pd.DataFrame,
) -> None:
    lines = ["# Advanced Dataset Analysis", ""]
    lines.append("## 1 Dataset visualization results")
    lines.append("- PCA and t-SNE figures were generated for all three datasets after standardizing numeric features.")
    lines.append("- Visualization sampling was capped for tractability, with t-SNE using a smaller subset due its computational cost.")
    lines.append("")

    lines.append("## 2 Dataset separability comparison")
    lines.append("```text")
    lines.append(separability_df.to_string(index=False))
    lines.append("```")
    lines.append("")

    lines.append("## 3 Feature entropy insights")
    entropy_preview = entropy_df.groupby("Dataset").head(10)
    lines.append("```text")
    lines.append(entropy_preview.to_string(index=False))
    lines.append("```")
    lines.append("")

    lines.append("## 4 Feature redundancy discussion")
    redundancy_preview = redundancy_df.groupby("Dataset").head(10) if not redundancy_df.empty else redundancy_df
    lines.append("```text")
    lines.append(redundancy_preview.to_string(index=False) if not redundancy_preview.empty else "No feature pairs exceeded 0.95 correlation.")
    lines.append("```")
    lines.append("")

    lines.append("## 5 Dataset difficulty comparison")
    lines.append("```text")
    lines.append(difficulty_df.to_string(index=False))
    lines.append("```")
    lines.append("")

    lines.append("## 6 Implications for DDoS detection research")
    lines.append("- Higher separability scores indicate that a linear or tree-based baseline can already distinguish benign and DDoS traffic well in that dataset.")
    lines.append("- Strong redundancy suggests opportunities for feature pruning before downstream model training.")
    lines.append("- Entropy highlights features with richer variability, which can be useful for interpreting discriminative network behavior.")
    lines.append("- Differences between LogisticRegression and RandomForest performance indicate whether the decision boundary is closer to linear or nonlinear for each dataset.")
    (OUTPUT_DIR / "advanced_dataset_analysis.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ensure_output_dir()
    sns.set_theme(style="whitegrid")

    separability_rows: List[Dict[str, object]] = []
    difficulty_rows: List[Dict[str, object]] = []
    entropy_frames: List[pd.DataFrame] = []
    redundancy_frames: List[pd.DataFrame] = []
    corr_maps: Dict[str, pd.DataFrame] = {}
    redundancy_reports: Dict[str, pd.DataFrame] = {}

    for dataset_name, path in DATASETS.items():
        counts = count_dataset(path)
        vis_sample = sample_dataset(path, MAX_VIS_ROWS, counts["samples"])
        x_vis, y_vis, feature_names = prepare_features(vis_sample)
        x_vis_scaled = scale_features(x_vis)

        pca = PCA(n_components=2, random_state=RANDOM_STATE)
        pca_points = pca.fit_transform(x_vis_scaled)
        plot_embedding(pca_points, y_vis, f"PCA: {dataset_name}", OUTPUT_DIR / f"pca_{dataset_name}.png")

        tsne_source = vis_sample if len(vis_sample) <= MAX_TSNE_ROWS else vis_sample.sample(n=MAX_TSNE_ROWS, random_state=RANDOM_STATE)
        x_tsne, y_tsne, _ = prepare_features(tsne_source)
        x_tsne_scaled = scale_features(x_tsne)
        tsne = TSNE(n_components=2, perplexity=30, random_state=RANDOM_STATE, init="pca", learning_rate="auto")
        tsne_points = tsne.fit_transform(x_tsne_scaled)
        plot_embedding(tsne_points, y_tsne, f"t-SNE: {dataset_name}", OUTPUT_DIR / f"tsne_{dataset_name}.png")

        model_sample = sample_dataset(path, MAX_MODEL_ROWS, counts["samples"])
        x_model, y_model, _ = prepare_features(model_sample)
        x_model_scaled = scale_features(x_model)
        x_model_scaled_df = pd.DataFrame(x_model_scaled, columns=x_model.columns)

        logistic = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=RANDOM_STATE)
        rf = RandomForestClassifier(
            n_estimators=200,
            random_state=RANDOM_STATE,
            class_weight="balanced_subsample",
            n_jobs=1,
        )

        separability_rows.append(evaluate_classifier(logistic, x_model_scaled_df, y_model, dataset_name, "LogisticRegression"))
        difficulty_rows.append(evaluate_classifier(logistic, x_model_scaled_df, y_model, dataset_name, "LogisticRegression"))
        difficulty_rows.append(evaluate_classifier(rf, x_model, y_model, dataset_name, "RandomForestClassifier"))

        entropy_df = compute_entropy_scores(dataset_name, x_model)
        entropy_frames.append(entropy_df)

        redundancy_sample = sample_dataset(path, MAX_REDUNDANCY_ROWS, counts["samples"])
        x_red, _, _ = prepare_features(redundancy_sample)
        corr, redundancy_report = compute_redundancy(dataset_name, x_red.iloc[:, : min(MAX_HEATMAP_FEATURES, x_red.shape[1])])
        corr_maps[dataset_name] = corr
        redundancy_reports[dataset_name] = redundancy_report
        redundancy_frames.append(redundancy_report)

    separability_df = pd.DataFrame(separability_rows)
    difficulty_df = pd.DataFrame(difficulty_rows)
    entropy_df = pd.concat(entropy_frames, ignore_index=True)
    redundancy_df = pd.concat(redundancy_frames, ignore_index=True) if redundancy_frames else pd.DataFrame()

    separability_df.to_csv(OUTPUT_DIR / "dataset_separability_scores.csv", index=False)
    difficulty_df.to_csv(OUTPUT_DIR / "dataset_difficulty_scores.csv", index=False)
    entropy_df.to_csv(OUTPUT_DIR / "feature_entropy_scores.csv", index=False)
    redundancy_df.to_csv(OUTPUT_DIR / "feature_redundancy_report.csv", index=False)

    plot_entropy_top_features(entropy_df)
    plot_redundant_feature_heatmap(corr_maps, redundancy_reports)
    write_report(separability_df, difficulty_df, entropy_df, redundancy_df)
    print("Advanced analysis completed.")


if __name__ == "__main__":
    main()
