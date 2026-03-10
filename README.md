# Comparative Feature and Complexity Analysis of Modern IoT DDoS Datasets

## Paper Reference

This repository accompanies the research paper:

**"Comparative Feature and Complexity Analysis of Modern IoT DDoS Datasets: CICIoT2023, CICDDoS2019, and TON-IoT"**

**Author**  
Vinay T. Patil  
Department of Computer Engineering  
Kavayitri Bahinabai Chaudhari North Maharashtra University

## Overview

This repository contains the preprocessing scripts, dataset analysis scripts, visualization pipeline, and manuscript-generation utilities used to study three modern IoT DDoS datasets:

- `CICIoT2023`
- `CICDDoS2019`
- `TON-IoT`

The workflow supports:

- preprocessing and cleaning of raw dataset files
- statistical comparison of dataset structure and class balance
- feature-level analysis including redundancy and entropy
- visualization using PCA, t-SNE, and publication-quality comparison plots
- manuscript and submission-package generation for research reporting

## Repository Structure

Example repository layout:

```text
iot-ddos-dataset-analysis
│
├── preprocessing
├── analysis
├── visualization
├── figures
├── results
└── README.md
```

In this workspace, the scripts currently correspond to these functional groups:

- `preprocessing`
  - `build_unified_ddos_dataset.py`
- `analysis`
  - `analyze_ddos_datasets.py`
  - `analyze_processed_ddos_datasets.py`
  - `advanced_iot_ddos_analysis.py`
  - `prepare_paper_results.py`
- `visualization`
  - generated under `analysis_results/figures`
  - generated under `analysis_results/advanced_analysis`

## Dataset Sources

The datasets used in this study must be obtained from their official sources:

- **CICIoT2023**  
  https://www.unb.ca/cic/datasets/iotdataset-2023.html

- **CICDDoS2019**  
  https://www.unb.ca/cic/datasets/ddos-2019.html

- **TON-IoT**  
  https://research.unsw.edu.au/projects/toniot-datasets

Datasets are **not redistributed** in this repository due to licensing, ownership, and usage restrictions imposed by the original data providers.

## Requirements and Dependencies

The project uses Python and the following libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`
- `python-docx`
- `pillow`

Recommended environment:

- Python `3.10+`

## Installation Instructions

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.

Example:

```bash
git clone <repository-url>
cd iot-ddos-dataset-analysis
python -m venv .venv
.venv\Scripts\activate
python -m pip install pandas numpy matplotlib seaborn scikit-learn scipy python-docx pillow
```

## How to Run the Pipeline

### Step 1: Run preprocessing scripts

Use the preprocessing pipeline to filter DDoS and benign traffic, clean features, and create processed datasets.

Example:

```bash
python build_unified_ddos_dataset.py
```

### Step 2: Run dataset analysis scripts

Run the dataset audit, processed dataset comparison, and advanced statistical analysis.

Examples:

```bash
python analyze_ddos_datasets.py
python analyze_processed_ddos_datasets.py
python advanced_iot_ddos_analysis.py
```

### Step 3: Run visualization scripts

Generate publication-ready tables and figures from the analysis outputs.

Examples:

```bash
python prepare_paper_results.py
python prepare_sensors_submission.py
```

If manuscript generation is required:

```bash
python generate_iot_ddos_paper_v5_final.py
```

## Output Files Generated

Typical outputs produced by the pipeline include:

- cleaned datasets
  - `processed_CICIoT2023_ddos.csv`
  - `processed_CICDDoS2019_ddos.csv`
  - `processed_TONIoT_ddos.csv`
- dataset summaries
  - `dataset_summary.csv`
  - `dataset_comparison_table.csv`
  - `dataset_difficulty_table.csv`
- analysis reports
  - `dataset_analysis_results.md`
  - `advanced_dataset_analysis.md`
  - `paper_results_summary.md`
- figures
  - class distribution plots
  - correlation heatmaps
  - feature importance plots
  - PCA and t-SNE visualizations
- manuscript outputs
  - Word document drafts
  - submission package assets

## Reproducibility Instructions

To reproduce the study:

1. Download the original datasets from the official sources listed above.
2. Place them in the expected local directory structure.
3. Run the preprocessing pipeline to generate cleaned binary DDoS datasets.
4. Run the comparative and advanced analysis scripts.
5. Regenerate the publication tables, figures, and manuscript drafts.

Recommended reproducibility practices:

- keep raw datasets unchanged
- document software versions
- use the same Python version and library versions where possible
- preserve generated intermediate outputs under a dedicated `results` directory

## Citation

If you use this repository, please cite the associated paper:

```bibtex
@misc{patil_iot_ddos_dataset_analysis,
  author       = {Vinay T. Patil},
  title        = {Comparative Feature and Complexity Analysis of Modern IoT DDoS Datasets: CICIoT2023, CICDDoS2019, and TON-IoT},
  year         = {2026},
  note         = {Research repository and analysis pipeline}
}
```

Please also cite the original dataset papers and official dataset sources.

## License

Code in this repository should be released under the project’s chosen open-source license.


Dataset files themselves are subject to the original providers’ licenses and terms of use.

## Contact Information

**Vinay T. Patil**  
Department of Computer Engineering  
Kavayitri Bahinabai Chaudhari North Maharashtra University  
Email: `vinayt.patil@outlook.com`
