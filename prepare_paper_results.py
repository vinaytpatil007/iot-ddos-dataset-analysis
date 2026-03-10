from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


BASE_DIR = Path(r"D:\ddos dataset")
ANALYSIS_DIR = BASE_DIR / "analysis_results"
ADVANCED_DIR = ANALYSIS_DIR / "advanced_analysis"
PAPER_FIGURES_DIR = ANALYSIS_DIR / "paper_figures"


def ensure_dirs() -> None:
    PAPER_FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    dataset_summary = pd.read_csv(ANALYSIS_DIR / "dataset_summary.csv")
    difficulty_scores = pd.read_csv(ADVANCED_DIR / "dataset_difficulty_scores.csv")
    redundancy = pd.read_csv(ADVANCED_DIR / "feature_redundancy_report.csv")
    return dataset_summary, difficulty_scores, redundancy


def build_dataset_comparison_table(dataset_summary: pd.DataFrame) -> pd.DataFrame:
    table = dataset_summary.copy()
    table["Class Imbalance Ratio"] = table.apply(
        lambda row: np.inf if row["Benign"] == 0 else row["DDoS"] / row["Benign"],
        axis=1,
    )
    table = table.rename(
        columns={
            "Samples": "Total Samples",
            "DDoS": "DDoS Samples",
            "Benign": "Benign Samples",
            "Features": "Features",
        }
    )
    table = table[
        ["Dataset", "Total Samples", "DDoS Samples", "Benign Samples", "Features", "Class Imbalance Ratio"]
    ]
    table.to_csv(ANALYSIS_DIR / "dataset_comparison_table.csv", index=False)
    return table


def build_dataset_difficulty_table(difficulty_scores: pd.DataFrame) -> pd.DataFrame:
    table = (
        difficulty_scores.pivot(index="Dataset", columns="Model", values="roc_auc")
        .reset_index()
        .rename(
            columns={
                "LogisticRegression": "LogisticRegression_AUC",
                "RandomForestClassifier": "RandomForest_AUC",
            }
        )
    )
    table.to_csv(ANALYSIS_DIR / "dataset_difficulty_table.csv", index=False)
    return table


def build_feature_redundancy_summary(redundancy: pd.DataFrame) -> pd.DataFrame:
    if redundancy.empty:
        summary = pd.DataFrame(columns=["Dataset", "Redundant Feature Pairs", "Correlation Value"])
    else:
        redundancy = redundancy.copy()
        redundancy["Redundant Feature Pairs"] = redundancy["Feature1"] + " vs " + redundancy["Feature2"]
        summary = redundancy[["Dataset", "Redundant Feature Pairs", "Correlation"]].rename(
            columns={"Correlation": "Correlation Value"}
        )
    summary.to_csv(ANALYSIS_DIR / "feature_redundancy_summary.csv", index=False)
    return summary


def plot_dataset_size(table: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=table, x="Dataset", y="Total Samples", hue="Dataset", palette="Blues_d", legend=False, ax=ax)
    ax.set_title("Dataset Size Comparison")
    ax.set_ylabel("Total Samples")
    ax.set_xlabel("")
    plt.tight_layout()
    plt.savefig(PAPER_FIGURES_DIR / "dataset_size_comparison.png", dpi=300)
    plt.close(fig)


def plot_class_imbalance(table: pd.DataFrame) -> None:
    plot_df = table.replace({"Class Imbalance Ratio": {np.inf: np.nan}}).dropna(subset=["Class Imbalance Ratio"])
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=plot_df,
        x="Dataset",
        y="Class Imbalance Ratio",
        hue="Dataset",
        palette="Reds_d",
        legend=False,
        ax=ax,
    )
    ax.set_title("Class Imbalance Comparison")
    ax.set_ylabel("DDoS / Benign Ratio")
    ax.set_xlabel("")
    plt.tight_layout()
    plt.savefig(PAPER_FIGURES_DIR / "class_imbalance_comparison.png", dpi=300)
    plt.close(fig)


def plot_dataset_difficulty(table: pd.DataFrame) -> None:
    plot_df = table.melt(
        id_vars="Dataset",
        value_vars=["LogisticRegression_AUC", "RandomForest_AUC"],
        var_name="Model",
        value_name="AUC",
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=plot_df, x="Dataset", y="AUC", hue="Model", palette="Set2", ax=ax)
    ax.set_title("Dataset Difficulty Comparison")
    ax.set_ylabel("ROC-AUC")
    ax.set_xlabel("")
    plt.tight_layout()
    plt.savefig(PAPER_FIGURES_DIR / "dataset_difficulty_comparison.png", dpi=300)
    plt.close(fig)


def write_markdown_summary(
    dataset_table: pd.DataFrame,
    difficulty_table: pd.DataFrame,
    redundancy_summary: pd.DataFrame,
) -> None:
    feature_stats_files = {
        "CICIoT2023": ANALYSIS_DIR / "feature_statistics_CICIoT2023.csv",
        "CICDDoS2019": ANALYSIS_DIR / "feature_statistics_CICDDoS2019.csv",
        "TONIoT": ANALYSIS_DIR / "feature_statistics_TONIoT.csv",
    }

    lines = ["# Paper Results Summary", ""]
    lines.append("## Dataset statistics")
    lines.append("```text")
    lines.append(dataset_table.to_string(index=False))
    lines.append("```")
    lines.append("")

    lines.append("## Feature analysis")
    for dataset_name, stats_path in feature_stats_files.items():
        stats = pd.read_csv(stats_path, index_col=0)
        skewed = stats.index[stats["skew"].abs() > 1.0].tolist()[:8]
        lines.append(f"### {dataset_name}")
        lines.append(f"- Highly skewed features: {', '.join(skewed) if skewed else 'None detected'}")
        lines.append("")

    lines.append("## Visualization insights")
    lines.append("- PCA and t-SNE figures indicate that all three datasets exhibit visible benign vs DDoS separation, with TONIoT showing the least trivial clustering structure.")
    lines.append("- The publication figures are saved in `analysis_results/paper_figures`.")
    lines.append("")

    lines.append("## Dataset difficulty discussion")
    lines.append("```text")
    lines.append(difficulty_table.to_string(index=False))
    lines.append("```")
    lines.append("- CICIoT2023 and CICDDoS2019 are highly separable under baseline models, suggesting relatively easy benchmark conditions.")
    lines.append("- TONIoT is more challenging for a linear model, which makes it useful for stronger generalization studies.")
    lines.append("")

    lines.append("## Redundancy highlights")
    preview = redundancy_summary.groupby("Dataset").head(5) if not redundancy_summary.empty else redundancy_summary
    lines.append("```text")
    lines.append(preview.to_string(index=False) if not preview.empty else "No redundant pairs above the threshold were found.")
    lines.append("```")
    lines.append("")

    lines.append("## Research takeaways")
    lines.append("- Severe class imbalance remains a major concern, especially in CICDDoS2019.")
    lines.append("- Feature redundancy suggests feature-pruning and ablation studies are justified before final model selection.")
    lines.append("- For a balanced and less trivial benchmark, TONIoT should be emphasized alongside one of the larger CIC datasets.")

    (ANALYSIS_DIR / "paper_results_summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    sns.set_theme(style="whitegrid")

    dataset_summary, difficulty_scores, redundancy = load_inputs()
    dataset_table = build_dataset_comparison_table(dataset_summary)
    difficulty_table = build_dataset_difficulty_table(difficulty_scores)
    redundancy_summary = build_feature_redundancy_summary(redundancy)

    plot_dataset_size(dataset_table)
    plot_class_imbalance(dataset_table)
    plot_dataset_difficulty(difficulty_table)
    write_markdown_summary(dataset_table, difficulty_table, redundancy_summary)

    print("Paper-ready tables and figures generated.")


if __name__ == "__main__":
    main()
